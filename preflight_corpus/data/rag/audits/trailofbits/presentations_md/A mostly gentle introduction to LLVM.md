# 1


2
A mostly gentle introduction to LLVM
UMD-CSEC

3
Hi
●
Me
○
Previously: UMD-CSEC 2014-2018
○
Currently: Senior security engineer @ Trail of Bits
■
Program analysis research (LLVM, x86)
■
Open source engineering (package managers, Python, Rust)
●
Trail of Bits
○
NYC-based security and research consultancy
○
~100 people spread around the world, >50% remote
○
Research (DARPA), engineering (commercial, OSS), assurance
(commercial)
○
Summer and winter internships
Introductions & Agenda

4
This talk
Goals: LLVM will no longer be just a C/C++ compiler to you
Whirlwind tour (that means you’re encouraged to stop and ask questions):
●
The Clang frontend (CFE) and what you can do with it
●
LLVM IR and what’s in it
○
Writing static analyses using the pass APIs
●
How the sausage is made
○
The LLVM middle end, target {in,}dependent instruction selection and lowering
●
Bonus: Using LLVM for things it wasn’t designed for
Agenda

5
Why should you care?
You’re in a cybersecurity club, compilers are just tools, right?
●
You want to ﬁnd bugs in programs
○
Virtually all static and dynamic analysis requires compiler fundamentals
■
Even fuzzing: AFL etc. use the compiler to instrument programs for coverage tracking
○
IRs and normalized forms, control and dataﬂow analyses are essential building blocks
●
You want to make software more secure
○
The future of unsafe programming languages (C/C++) is safer compilers and more compiler-introduced/enforced mitigations
○
The future of programming languages in general is smarter compilers that can prove more properties about programs (both for optimization and safety)
●
You want to be 31337 and stunt on people with your CS skillz
Motivation

6
Originally: Low Level Virtual Machine: not low level, not really virtual
Actually: A massive compiler infrastructure project, encompassing:
● clang: A GCC-compatible C/C++/Objective-C frontend (“CFE”)
●
A ﬂexible target independent* intermediate representation (LLVM IR)
● opt: an optimizer for LLVM IR
●
Target dependent code generators, a modern linker, assembler, …
●
…and so much more:
○
A debugger (lldb)
○
Modern C++ runtime (libc++)
○
Symex engine (KLEE)
But what is LLVM?
History and background

7
From the top: the frontend
You already know this part: it’s the program that wraps all of LLVM’s subcomponents into a single tool that produces binaries.
CFE has two primary tasks:
●
Provide a familiar CLI to engineers (clang and clang++)
○
Engineers and build systems know GCC’s ﬂags, so CFE attempts to be compatible with them
○
Translate ﬂags and options into various compilation decisions
●
Lex C/C++ inputs, parse into abstract syntax trees, and then “lower” those ASTs into LLVM IR for subsequent optimization
“Compile foo.c into foo, embedding debug info
(-g) and optimizing aggressively (-O3)”

8
The frontend
We can tell CFE to dump the generated AST:

9
The frontend
…or even dump and query as JSON!
“Dump the AST as JSON, reducing to only nodes that match foo”

10
The Clang CLI is the most limited way to interact with the frontend’s internals; we can use the CFE’s C++ APIs to do much more powerful things.
Built-in examples:
● clang-format: reformat code according to a standard style
● clang-tidy: lint C/C++ for common errors, like implicit conversions
○
Automatically apply ﬁxes to codebases!
External examples:
● constexpr-everything: automatically rewrite C++ code to qualify as many things as constexpr as possible
Key APIs: RecursiveASTVisitor, ASTFrontendAction, FixItRewriter
Frontend: wrapup

11
LLVM IR and the optimizer
The frontend’s ultimate job is to translate the program’s AST into LLVM’s
Intermediate Representation so that the optimizer can reﬁne it.
LLVM IR looks a bit like funky C:
Stack allocations!
Function calls/returns!
Literals and constants!
Function declarations and deﬁnitions!

12
LLVM IR: key properties and semantics
Generally speaking, LLVM IR follows C abstract machine semantics: pointers, functions, etc. all behave the way they do in
C.
Oversimpliﬁcation: LLVM IR is a load-store architecture: there are two storage areas
(registers and memory), with separate instructions to access each. Memory can be heap, stack, global, etc., and is accessed via load and store.
Key property: LLVM IR registers (“variables”)
are in single static assignment (SSA) form:
every variable is written to exactly once, and there are an inﬁnite number of variables.
This property forms the backbone of many of
LLVM’s optimizations.
int main(void) { int x = 123; x += 1; return x;
}

13
LLVM IR: SSA construction
●
The naive SSA form is very inefficient: lots of memory locations means lots of loads/stores that slow down execution.
●
One of LLVM’s earliest optimization passes is mem2reg, which “lifts” any alloca that has only loads and stores into one or more SSA variables.
opt -S -mem2reg test.ll
��
Constant folding opportunity!

14
LLVM IR: Optimizing and optimizer passes
●
At -O1 and higher, the clang frontend will run mem2reg and a variety of other default optimizations: constant folding, dead code elimination, control
ﬂow graph simpliﬁcation, etc.
●
Each of these optimizations is written as LLVM passes, which visit the IR in different ways
(entire program, per-function, per-loop, callgraph, etc.)
●
The pass API is a public C++ API, and we can write our own!
$ cargo install llvm-passgen
# create a function pass named Test
$ llvm-passgen Test \
  --kind function
$ cd Test/build
$ cmake ..
$ cmake --build .
# run the Test pass on test.ll
$ opt -S \
  -load LLVMTest.so --Test \
  ~/test.ll

15
● runOnFunction executes once for each llvm::Function in the llvm::Module, and returns true if it modiﬁes the function.
●
Lots of interesting program state:
each function can iterate over its basic blocks (≈ control ﬂow) and constituent instructions
●
Passes can register dependencies on other passes, causing LLVM to run those passes ﬁrst and collect their results
●
Passes can invalidate the results of earlier passes (e.g. changing the call graph), requiring them to be re-run if needed later

16
From IR to machine code
Real computer architectures are not like LLVM IR:
●
Inﬁnite, typed SSA registers → ﬁnite, untyped machine registers
●
Modules, functions, basic blocks → translation units, stack frames
●
Parallel operations (no data deps) → limited execution slots and units
●
Not all LLVM instructions correspond to machine instructions
○
One-to-many, many-to-one depending on ISA support for multiplication, vectorized ops, etc.
LLVM goes through several phases to get to machine code; at a high level:
●
Instruction selection (ISel): LLVM IR → SelectionDAG
●
Scheduling: SelectionDAG → MachineInstrs
●
Register allocation: select concrete registers for MachineInstrs
●
Prologue/Epilogue Insertion (PEI): MachineFunctions have concrete stack frames and setup/teardown code
●
Emission: Conversion into actual target assembly/raw machine code

17
Machine code generation: ﬁddly bits
●
How do you go from inﬁnite registers to ﬁnite registers?
○
Register allocation!
●
Naive: ﬁll each GPR with an SSA variable until you run out, “spill” the rest onto the stack
○
Problems with this? Can we do better?
○
Can the compiler/IR help us?
●
Different performance tradeoffs
○
Normally we don’t care (much) about compilation time, but sometimes we do (JITs)
●
In the abstract: register allocation is reducible to k-coloring
○
NP-hard!
○
Real world adds additional annoyances:
■
Some ISAs “pre-color” the graph (e.g. specifying registers for params, return)
■
Some ISAs have aliased registers (AMD64: al/ax/eax/rax)

18
Machine code generation: other ﬁddly bits
●
Middle and late optimization
○
Most optimization is done on LLVM IR, but some things are better suited for lower representations: instruction fusion, peephole optimization, modulo scheduling
●
Prologue/epilogue insertion
○
Need to compute stack frame size, inject exception handling code, lots of other small things
●
Many other things
○
Call lowering (GOT/PLT, direct & indirect calls)
○
Hardening and mitigations (canaries, ASLR)
○
Debug information (DWARF, PDB)
○
Object ﬁle formats (PE, Mach-O, COFF, ELF)
○
Linking….
○
Recently: binary layout optimization (PGO on steroids): BOLT
●
There’s a lot going on!

19
What else can we do?
●
LLVM normally turns source code into machine code
○
But LLVM IR is extremely useful…
○
What if we go in the other direction?
●
Binary lifting/translation: faithfully decompile (“lift”) machine instructions/functions/entire programs to LLVM IR
○
McSema / Remill / Anvill
○
Iteratively “brighten” the IR so that it resembles what a frontend like Clang would produce
○
Why would we do this?
○
Challenges: CFG recovery, state decomposition (revert x86 context to SSA)
■
The opposite of register allocation!
●
We don’t always want to compile programs
○
LLVM IR has a lot of detail in it; it’s a pretty good starting point for static analyses

20
●
LLVM is an extremely large project; we’ve only scratched the surface
●
Not all is perfect in heaven:
○
LLVM started as a C/C++ compiler; lots of leaky abstractions in the IR
■
We can talk about all the ways this causes problems for Rust and others
○
Designed in tandem with the CFE, so LLVM recognizes IR patterns that CFE uses
■
Deviate from those patterns, and the optimizer suﬀers
○
LLVM IR is complex, both structurally and semantically
■
For good reasons! But it’s not the most straightforward example of an SSA IR
Wrapup

21
Resources
●
LLVM’s documentation
○
Writing an LLVM Pass
○
The LLVM Language Reference
○
LLVM Developers' Meeting Archives (lots of good talks)
●
Trail of Bits blog: https://blog.trailofbits.com/
●
Trail of Bits GitHub: https://github.com/trailofbits
○
Rellic, McSema, Remill, Anvill
●
Personal blog: https://blog.yossarian.net
○
LLVM-speciﬁc posts: https://blog.yossarian.net/tags#llvm
●
Personal GitHub: https://github.com/woodruffw
○ llvm-passgen, mollusc