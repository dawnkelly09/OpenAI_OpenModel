# Binary symbolic execution with

KLEE-Native
Sai Vegasena

The Team
Sai Vegasena
Security Engineering Intern sai.vegasena@trailofbits.com
@svegas18
Peter Goodman
Senior Security Engineer peter@trailofbits.com
@peter_a_goodman

- Developed a fork of KLEE that operates on raw binaries
- Translated machine code to LLVM bitcode with Remill and ran it in KLEE
- Wrote a custom allocator to accurately model heap memory in KLEE’s emulator
- Implemented virtualized system calls that productively handled symbolic data
- Developed a new forking model for KLEE’s symbolic executor
- Reproduced a CVE used in an old ChromeOS exploit chain
During my internship I ...

- Applied in software testing and veriﬁcation
- Dynamically generates high-coverage producing inputs
- Leverages a custom runtime environment
KLEE is a symbolic virtual machine that executes LLVM bitcode
Bugs Galore :)

-
Sometimes need source
-
Build systems, conﬁgs, and dependencies
-
Manually Injecting KLEE-API calls into the source
-
McSema is an option but CFG recovery is limiting and there are occasional inaccuracies
KLEE’s greatest strength is also its greatest weakness
Cons of running LLVM bitcode
Pros of running LLVM bitcode
-
Allows for custom runtime deﬁnitions and intrinsics
-
Executes anything clang can compile
- i.e  C, C++, Rust, Swift, Go,, etc

KLEE-Native operates on snapshotted program binaries
- Binaries are snapshotted with user deﬁned breakpoints
-
Static breakpoints
-
Dynamic breakpoints for ASLR
-
./klee-snapshot-7.0 --workspace_dir ws --dynamic --breakpoint 0x1337
--arch amd64_avx -- ./a.out
- Remill lifts machine code instructions to LLVM bitcode
- KLEE-Native executes the runtime and the lifted LLVM
./klee-exec-7.0 --workspace_dir ws

Runtime is the kernel and the machine
-
Remill async hyper call is deﬁned in runtime
-
“Implements” OS functionality
-
Execution is passed to a linux system call wrapper in runtime
-
Custom ABI extracts arch info from state
-
Store return value
-
Extract args
-
Find syscall number
    -      Wrappers do error checking done by OS
-
Gives a kernel-level “insight”

Simplifying lifted libc functions with accuracy
- Problem
-
Lifting libc functions is slow
-
Unnecessary state forking on symbolic data
- LD_PRELOAD-based library into snapshotted programs
-
Lets us interpose and hook to simple libc variant in the runtime
- Variants handle symbolic data in a simple way with no lifting

Heap memory is accurately modeled with libc intercepts
- Lifted mallocs call brk or mmap
-
Technically accurate but bad for bug-ﬁnding
-
No clarity for bounds checks on allocations
-
Hard to oversee UAFS, double frees, and access violations
- Utilize the intercept hook to organize allocations in a uniform structure
- Basically implemented a custom allocator
- Custom address encoding  helps “locate” allocations in alloc lists on mallocs and frees

Encoding

It is possible to fall back to real libc functions in KLEE-Native
Before Snapshot
Fallback to real libc malloc just in case
Emulated in KLEE-Native

It is possible to fall back to real libc functions in KLEE-Native
Before Snapshot
Fallback to real libc malloc just in case
Emulated in KLEE-Native
NOP when we load state

It is possible to fall back to real libc functions in KLEE-Native
Before Snapshot
Fallback to real libc malloc just in case
Emulated in KLEE-Native
NOP when we load state
Skip the ret in emulator

Eager concretization is better than eager forking
-
Closer in spirit to SAGE, a static symbolic symbolic executor
-
Akin to lazy evaluation
-
“State continuations” are moral equivalent of a
Python generator, and may be invoked to give “the next viable fork at this point”
-
Continuations are enqueued and scheduled later
-
Handle branches and symbolic addresses

KLEE-Native can identify real bugs
- Make a snapshot in vulnerable function
- Run klee-exec

 klee-exec-7.0 --workspace_dir ws_CVE
- Policy handler provides an interesting feature that Valgrind and Asan don’t klee-snapshot-7.0 --workspace_dir ws_CVE --dynamic --breakpoint 0xb33 --arch amd64_avx -- ./c_ares_repro

Symex on Binary Snapshots with
KLEE-Native
Sai Vegasena: sai.vegasena@trailofbits.com
Peter Goodman: peter@trailofbits.com