# McSema:

Static Translation of
X86 Instructions to
LLVM
ARTEM DINABURG, ARTEM@TRAILOFBITS.COM
ANDREW RUEF, ANDREW@TRAILOFBITS.COM
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

About Us
Artem
◦Security Researcher
◦blog.dinaburg.org
Andrew
◦PhD Student, University of Maryland
◦Trail of Bits
◦www.cs.umd.edu/~awruef
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

What is McSema?
Translate existing programs into a representation that can be easily manipulated and reasoned about.
The representation we chose is LLVM IR.
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

What is LLVM?
Modern Optimizing Compiler Infrastructure
◦Infrastructure first, compiler second
Easy to learn and modify (for a compiler)
Very permissive licensing
Core
Optzn xforms
X86
Support
Code gen
Target
PPC
DWARF analysis
LTO linker
LL IO
BC IO
System
CBE
GC
IPO
GCC
JIT clang
...
...
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

What is LLVM IR?
Like a higher level assembly language
Typed, Static Single Assignment
Simplifies program analysis and transformation define i32 @main(i32 %argc, i8** %argv) {
%1 = alloca i32, align 4
%2 = alloca i32, align 4
%3 = alloca i8**, align 8 store i32 0, i32* %1 store i32 %argc, i32* %2, align 4 store i8** %argv, i8*** %3, align 8
%4 = call i32 (i8*, ...)* @printf(… <omitted>)
ret i32 0 }
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Why translate x86 to LLVM IR?
Use all existing LLVM tools
◦Optimization
◦Test Generation
◦Model Checking
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Why translate x86 to LLVM IR?
Portability aarch64 arm hexagon mips mips64 msp430 nvptx nvptx64 ppc32 ppc64 r600 sparc sparcv9 systemz thumb x86 x86-64 xcore
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Why translate x86 to LLVM IR?
DLL
LLVM IR
EXE
McSema
SOURCE
Foreign Code Integration and Re-Use
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Why translate x86 to LLVM IR?
Add obfuscation and/or security to existing code.
DLL
DLL’
LLVM IR
McSema
Other Tools
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Demo 1
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Prior Work
Dagger
Second Write
Fracture
◦Draper Lab
BAP
◦CMU
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Why McSema
Open Source
Documentation and Unit Tests
FPU and SSE Support (incomplete)
Modular architecture
◦Separate control flow recovery from translation
◦Designed to translate code from arbitrary sources
◦Control flow graphs specified as Google protocol buffers
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Open Source
McSema is DARPA funded.
It is in the process of being open sourced.
These things take time.
Permissively licensed.
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Unit Tests
Google test powered unit test for instruction semantics
Compares McSema CPU context to native CPU state
...
ADD
FADD
FMUL
...
...
PASS
PASS
FAIL
...
Intel
PIN
Native
State
Mc
Sema
LLVM
JIT
McSema
State
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

FPU And SSE Support
Nearly Complete FPU Support
◦Many instructions
◦Some core issues remain:
◦Precision Control
◦Rounding Control
SSE Support is architecturally implemented
◦Register state is complete
◦Needs more instructions
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

McSema Architecture
CFG
Protobuf
IDA bin_decsen d
…
Instruction
Translation
LLVM IR
Separate control flow recovery from translation
Designed to translate code from arbitrary sources
Control flow graphs specified as Google protocol buffers
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Control Flow Recovery 1) Start at the entry point 2) BFS through all discovered basic blocks 3) ???
4) Recover CFG
What could go wrong???
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

CFG Recovery Challenges
Indirect Calls
◦JMP EAX
Jump Tables
◦JMP [EAX*4+OFFSET]
Mixed Code and Data
◦0x40040: RET
◦0x40041: db ‘H’,’e’,’l’,’l’,’o’,’
‘,’W’,’o’,’r’,’l’,’d’,’\0’
◦0x40056: PUSH EBP
Constant, Data, or Code?
◦0x40000: MOV EAX, 0x40040
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

CFG Recovery Solutions
Relocation Entries
◦Reliably identify pointers
◦Required for ASLR on Windows
API Domain Knowledge
◦Argument types to help solve code/data question
◦Need to know about APIs later anyway
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

CFG Recovery Solutions
Let IDA do it!
◦McSema comes with an IDAPython script to dump the CFG from IDA
Why IDA
◦Countless man-hours spent on CFG recovery
◦The CFG will be at least as good as what you see in IDA
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

CFG Recovery Solutions
In the future
◦CFG recovery via symbolic execution
◦Static call resolution drastically improves binary size
◦Even external code vs. translated code would be a big improvement
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation: CPU
Model as operations on CPU context
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Demo 2
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation:
Memory Model
Manipulates actual memory
Stack pointer is set to a translator stack
Stack variable recovery would be ideal
◦Create LLVM IR alloca values for function stack locals
◦Not always possible for sound variable recovery
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation:
Functions
F(A,B):
EAX = ESP[-4]
EBX = ESP[-8]
EAX += EBX
END
TRANSLATED_F(RegContext):
VAR_EAX = RegContext.EAX
VAR_EBX = RegContext.EBX
VAR_ESP = RegContext.ESP
VAR_EAX = VAR_ESP[-4]
VAR_EBX = VAR_ESP[-8]
VAR_EAX += VAR_EBX
RegContext.EAX = VAR_EAX
RegContent.EBX = VAR_EBX
RegContent.ESP = VAR_ESP
END
Spill Context, Translate, Store Context
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation:
Lazy Translation
OPTIMIZED_F(RegContext):
VAR_ESP = RegContext.ESP
VAR_EAX = VAR_ESP[-4]
VAR_EBX = VAR_ESP[-8]
RegContext.EAX =
VAR_EAX + VAR_EBX
RegContent.EBX = VAR_EBX
END
Let the optimizer make it better!
TRANSLATED_F(RegContext):
VAR_EAX = RegContext.EAX
VAR_EBX = RegContext.EBX
VAR_ESP = RegContext.ESP
VAR_EAX = VAR_ESP[-4]
VAR_EBX = VAR_ESP[-8]
VAR_EAX += VAR_EBX
RegContext.EAX = VAR_EAX
RegContent.EBX = VAR_EBX
RegContent.ESP = VAR_ESP
END
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation:
Externals
Parse Windows DLLs to extract API signatures
◦Simple text-based format
◦Easy to add custom mappings
Match import names
Emit as an extern function in LLVM IR
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

McSema Context
Native Context
McSema Context
Instruction Translation:
CALL REG/MEM
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Instruction Translation:
Callbacks
Native Context
McSema Context
Native Context
Create ‘drivers’ that translate context
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Development Progress: What
Works
Integer instructions
Unit Tests
FPU registers
FPU instructions (some)
SSE registers
SSE instructions (very few)
Callbacks
External Calls
Jump Tables
Data References
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Demo 3
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Development Progress: What
Needs to be Done
FPU Instructions (some)
SSE Instructions (most)
Exceptions
Privileged instructions
Need more unit tests!
Better optimization
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Future Plans
More instructions support
Memory modeling
Optimization
Rigorous Testing
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”

Questions?
“This research was developed with funding from the Defense Advanced Research Projects Agency (DARPA).”