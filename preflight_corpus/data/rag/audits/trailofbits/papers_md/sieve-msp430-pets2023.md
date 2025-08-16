# Efficient Proofs of Software Exploitability for Real-world Processors

Matthew Green1, Mathias Hall-Andersen2, Eric Hennenfent3, Gabriel Kaptchuk4, Benjamin
Perez3, and Gijs Van Laer1 1Johns Hopkins University, mgreen@cs.jhu.edu, gijs.vanlaer@jhu.edu 2Aarhus University, mathias@hall-andersen.dk 3Trail of Bits, eric.hennenfent@trailofbits.com, benperez1227@gmail.com 4Boston University, kaptchuk@bu.edu
Abstract
We consider the problem of proving in zero-knowledge the existence of vulnerabilities in executables compiled to run on real-world processors. We demonstrate that it is practical to prove knowledge of real exploits for real-world processor architectures without the need for source code and without limiting our consideration to narrow vulnerability classes. To achieve this, we devise a novel circuit compiler and a toolchain that produces highly optimized, non-interactive zero-knowledge proofs for programs executed on the MSP430, an ISA commonly used in embedded hardware.
Our toolchain employs a highly optimized circuit compiler and a number of novel optimizations to construct efficient proofs for program binaries. To demonstrate the capability of our system, we test our toolchain by constructing proofs for challenges in the Microcorruption capture the flag exercises.
1
Introduction
The proliferation of complex and critical software systems has given rise to the bug bounty paradigm, in which independent vulnerability research teams uncover and disclose ways to exploit deployed software in exchange for financial rewards. This process has resulted in the disclosure of several high-profile exploits in recent years [Pic21], and hundreds of millions of dollars are awarded in bounties annually.
While bug bounty programs are invaluable to improving the security of software, they are plagued by issues of trust. Because vulnerability researchers and bug bounty program managers are not part of the same organization—and likely have no prior relationship—each side must trust that the other will fulfill their obligations honestly. Specifically, bug bounty program managers must trust that vulnerability research teams are not overselling their capabilities and have discovered a serious exploit.
On the other hand, vulnerability research teams worry that those managing bug bounty programs will adaptively change the reward after disclosure of the exploit, claiming that the exploit does not meet some criteria.
Currently, vulnerability researchers and bug bounty program managers bridge this trust gap by having the vulnerability research team “prove” its knowledge of an exploit using a video recording. Concretely, the bug bounty program will challenge the vulnerability research team to perform an operation that should be impossible (e.g., launching the calculator application) and visually record the program execution. These proofs lack soundness, as video can easily be manipulated and cannot prove that the runtime environment matches the one specified by the bug bounty program. As such, the state of the art still leaves significant trust gaps within the bug bounty ecosystem.
In this work, we design a toolchain that bridges this trust gap using cryptographically sound proofs of exploit. These proofs give a computational guarantee that the vulnerability research team can exploit the system within the specified runtime environment, and they cannot be manipulated or forged. To ensure that these proofs do not disclose anything else to the bug bounty program team, we employ zero-knowledge 1

(ZK) [GMW87, GMW86] proofs, a class of proof systems that reveals nothing to the verifier beyond the veracity of the statement. Access to ZK proofs of exploit would allow vulnerability researchers and bug bounty programs to negotiate rewards without requiring significant leaps of faith.
Designing efficient ZK proofs of exploit requires both overcoming significant engineering challenges and non-trivial theoretical contributions.
While prior work [HK20b, HK20a] has contemplated similar appli- cations, their systems are limited to proving the existence of potential vulnerabilities or bugs in publicly available source code—falling short of meeting the needs of the vulnerability research market. In our work, we precisely model real processor architectures and runtime environments within the ZK protocol, allowing our proofs to reason directly about compiled binaries. Therefore, the proofs that our toolchain produces guarantee that the exploits will work on hardware. This level of fidelity is essential for allowing vulnerability research teams to precisely articulate and demonstrate their capabilities.
Envisioned Workflows. In order to illustrate the value of our techniques, consider three concrete ways that cryptographically sound proofs of exploit could be used:
(1) A vulnerability research (VR) team responds to a public bug bounty by submitting their ZK proof of exploit. Once the sponsor has verified the proof, a reward amount is determined and put into escrow until the VR team submits the exploit.
(2) A VR team discovers a bug in a piece of software for which there is no bug bounty program. If the developers choose not to award a bounty after initial discussions, the VR team could post the ZK proof of exploit to a public website, informing users that their existing systems are at risk. Critically, this does not reveal the exploit to malicious actors who might want to use the exploit to attack live systems. We note that this would also put pressure on developers to issue a bounty and patch their software, as responsible users will likely transition away from their products.
(3) A VR team discovers a bug in a piece of legacy software which is no longer maintained, or is running on devices that cannot perform firmware updates. The VR team can post the proof of vulnerability to a public website, creating a highly trustworthy warning against using the legacy software. If using the legacy software is unavoidable, we note that users could crowdsource funds to hire the VR team to design and issue a patch.
We note that these are only potential examples, and proofs of exploit may be valuable in other workflows.
1.1
Contributions
In this work, we design the first end-to-end modular toolchain that facilitates the creation of ZK proofs of program exploitability.1 The toolchain takes in two inputs: (1) a public compiled binary,2 and (2) the prover’s private input that exploits a vulnerability in that program. Given these inputs, it then produces a non-interactive zero-knowledge proof (NIZK) of correct execution. This is conducted by evaluating the binary as a RAM program using a Boolean processor circuit. While previous work has explored the evaluation of RAM machines using custom-built processors, our system employs real-world processor architectures; to make our system efficient, we introduce several novel processor-agnostic techniques that reduce the size of the resulting circuit. Specifically, we reduce the size of the circuit from O(t log(t)) to O(t), where t is the number of processor cycles executed during program execution.
To evaluate the effectiveness of our toolchain, we produced ZK proofs of exploit for MSP430 binaries.
First, we design a custom circuit implementation of the MSP430 processor that is optimized for ZK; this requires modeling system calls (syscalls) and complex addressing modes while minimizing the number of non-linear gates. Second, we provide the first public, generic implementation of the Katz, Kolesnikov, and
Wang (KKW) “MPC-in-the-head” ZK protocol [KKW18] and incorporate several significant improvements.
1Although prior work has explored the possibility of proving the existence of bugs in source code, our work addresses a fundamentally harder problem of demonstrating that a bug can be exploited into a full exploit. We carefully contrast these two approaches in Section 3.
2Our toolchain can naturally also operate from program source, which is compiled using a standard compiler.
2

Specifically, we show that the MPC-in-the-head with preprocessing paradigm that they propose can be modified to allow for optimized ring switching between Boolean and arithmetic representations, resulting in significantly more efficient proofs. Finally, we demonstrate the effectiveness of our approach by producing proofs of exploit for the Microcorruption CTF [mic13a], a set of hacking challenges that run on an MSP430 processor and cover many common exploitation techniques such as buffer overflow, command injection, and
ROP gadgets.
The Microcorruption challenges also require bypassing mitigations such as address space layout randomization (ASLR), data execution protection (DEP), and stack canaries. Our toolchain can produce NIZK proofs about MSP430 programs at 216 instructions per second and 119 KB per instruction.3
Limitations. Our approach allows proofs about exploits that can be represented as a predicate over the processor states over a program’s execution.
This means that there are some classes of exploits about which we cannot provide proofs, like exploits that rely on microarchitectural bugs such as Spectre and
Meltdown. Similarly, Row Hammer-style exploits cannot be expressed as such a predicate, as they require modeling physical properties of RAM. Accurately modeling these systems is challenging, independent of zero-knowledge proving; as such, these exploits are beyond the scope of this work. We note, however, that only the most sophisticated actors could successfully launch such an attack, and there are no documented cases of such exploits being used in the wild.
We note that our proofs do not attempt to conceal the running time of the exploit; the number of processor ticks required is included as a public part of the statement.
This is a standard relaxation in prior work [BCGT13, BCG+13, BCTV14, HK20a], and given the trade-off of less efficient proofs, it is easy to “pad-out” the running time to conceal the trace length.
Additionally, we note that any low-entropy probabilistic protections (e.g. ASLR) will always be vulnerable to computationally powerful adversaries, both for adversaries attacking live systems, e.g. using brute force, and for a prover generating a proof of exploit, e.g. grinding on random seed selection. This means that the meaning of a proof of exploit that overcomes low-entropy probabilistic defenses are nuanced: (1) when a proof is generated interactively and the processor randomness is sampled by the verifier, the proof implies that the prover has an exploit strategy that works on average, but may not always work; (2) when the proof is generated non-interactively, i.e. a computationally powerful prover may (invisibly) expend significant resources generating an accepting proof, the proof implies that there exists processor randomness such that the prover possesses a working exploit strategy.
Finally, we note that while our solution demonstrates the proofs of exploit are already practical, there remains more effort—both research and engineering—for the solution to be simple and easy to use. For example, vulnerability researchers must select the statement that they wish to prove carefully. Choosing the wrong statement could result in a proof that verifies but is semantically meaningless.
Ethical Concerns. Software exploits can be used to cause harm to people and organizations and there exist online markets where exploits are sold for nefarious purposes. As such, the techniques that we develop might also be used by individuals intent on causing harm. We note, however, that our techniques do not meaningfully increase the capabilities of these communities; allowing hackers prove—with cryptographic soundness error—that they know an exploit only serves to make exploit markets more trustworthy and more easily monitored. Critically, our techniques do not make it easier for attackers to discover or exploit vulnerabilities or meaningfully increase a hacker’s power to conduct blackmail.
2
Technical Overview 2.1
Background: Zero-Knowledge and Ben-Sasson et al.’s RAM Reduction
Zero-knowledge proofs of knowledge (ZK) [GMW87, GMW86] allow a prover to convince a verifier that they hold a witness demonstrating that some public statement is a member of an NP language with- out revealing anything beyond the membership itself. ZK techniques are now concretely efficient [JKO13,
GMO16,CDG+17,AHIV17,KKW18,XZZ+19,BBB+18,BBHR19,BCR+19,HK20b,WYKW20,BN20,dOT21, 3For hardware specifications, see Section 8 3

One-Time Statement-Independent Preprocessing
Statement-Dependant Computation
Private Input
Software
(MSP430 Assembly)
Processor Model
(MSP430)
Processor
Emulator
(MSP430 Emulator)
Circuit Compiler
(Verilog and Yosys)
RAM Reduction Assembler
Single
Instruction
Processor
Permutation
Proof
Circuitry
Memory
Checker
Circuitry
Trace Length
Zero-Knowledge
Prover
(Reverie)
Witness: Program Trace
Statement:
Processor Circuit
π
Figure 1:
A high level overview of our toolchain for producing efficient zero-knowledge proofs for RAM programs on real processors. (1) The process starts with a one-time preprocessing phase which compiles the processor model into building blocks which are later assembled into a complete circuit. The circuit compiler (which we instantiate using Verilog and Yosys) generates the circuit for evaluating a single instruction, and the circuitry required to perform the permutation proof and check memory correctness. (2) When the prover wishes to create a proof, they feed the software, represented as assembly in the appropriate
ISA, and any private program inputs into the processor emulator. The processor emulator runs the program to its conclusion and outputs the execution trace. (3) Based on the length of the trace, the RAM Reduction Assembler takes the preprocessed circuit components and creates the completed circuit. (4) The program trace, produced by the processor emulator, and the completed circuit, produced by the RAM reduction assembler, into any zero-knowledge prover to produce the final proof. We include the instantiations we use for our proofs of vulnerability in parenthesis.
YSWW21] and power a number of practical applications [MGGR13,BCG+14,Zav20,se19]. For formal defi- nitions of ZK proofs of knowledge, see [Pas10].
Most research on ZK focuses on the case in which the statement is provided in a format amenable to efficient proving systems (e.g., a circuit or algebraic relation). Therefore, most proof techniques now require that the relations have such a representation. This requirement can be unnatural and cumbersome, forcing implementers to translate a relation from its “natural” representation to the representation supported by the prover. This process frequently involves error-prone manual effort or the use of an immature circuit compiler [MNPS04,BNP08,MGC+16b,WMK16].
RAM Reduction.
Ben-Sasson et al. [BCGT13, BCG+13, BCTV14] proposed an efficient circuit-based approach for proving the correct execution of RAM programs which has also been used by more recent works [HK20a, HYDK21, FKL+21]. They represent the execution of the RAM program with two different traces. The first is the execution-ordered trace, wherein each step represents a single iteration of a processor circuit, including instruction bytes, a register file, and the alleged contents of memory being accessed. The second is the memory-ordered trace, containing the set of memory reads and writes sorted by address, with ties broken by the operation that was executed first. Proving that these traces represent an honest execution of the RAM program consists of the following:
1. Execution Trace Consistency. For each step in the execution trace, the proof must demonstrate that the input and output states represent a valid transition. This is done using a circuit that represents the processor. The input to each evaluation of this circuit is a fixed number of values drawn from RAM, a register file, and other auxiliary data that may be useful in verifying correct execution. This circuit will output 1 if the circuit produces the same output as the real RAM program.
2. Memory Trace Consistency. Each step in the trace involves reading and writing some values from
RAM. Na¨ıvely ensuring that these reads and writes are consistent with the previously executed instructions would require verifying the entire contents of RAM in each step. Instead, they maintain an address-ordered list called the memory trace, consisting of tuples of the form (step, operation, address, value), where step 4

is a unique index in the execution trace, operation can either be read or write, and address is a location in memory [BCG+13]. The memory consistency circuit ensures that each read operation contains the same value as the most recent write operation to that address.
3. Permutation Check. The two proofs above ensure that the execution trace is consistent with the pro- cessor circuit and that the operations in the memory trace are valid. However, we must still demonstrate that these traces are consistent with one another; that is, the values provided to the execution trace consistency circuit correspond to the elements verified using the memory trace consistency circuit. To ensure this consistency, we employ a permutation check that proves a one-to-one mapping between each read/write in the execution trace and some entry in the memory trace.
2.2
Formalizing Exploits
In order to produce cryptographically sound proofs of exploitability, we must have a formal NP language of which we can show a binary is a member. In our work, we are able to prove any exploit that is an arbitrary boolean predicate over the execution trace. Specifically, we can show that repeatedly applying the processor circuit to the processor state (for some public number of iterations) resulted in a processor state (or series of process states) that should have been impossible under honest execution. As such, we begin by designing circuit representations of real-world processors that are ZK friendly.
MSP430. In this work, we demonstrate the concrete feasibility of producing proofs of exploit for unaltered
MSP430 binaries. MSP430 is a family of microprocessors commonly used in low-power environments. The version of the MSP430 ISA on which we focus has 27 instructions, including 12 double operand instructions
(e.g. MOV, ADD, AND, SUB), 7 single operand instructions (e.g. PUSH, CALL), and 8 jump instructions (e.g. JEQ,
JNE) [Ins06,Mic13b].
There are several significant obstacles to designing a circuit that implements the MSP430 instruction set architecture (ISA). MSP430 goes beyond a classic load/store architecture by incorporating 13 addressing modes. We augment our processor circuit using a set of memory hints in each step that provide the processor with the required information to complete the cycle’s operation. The contents of the memory hints are interpreted based on the current instruction and are verified using the memory checker.
Given that the MSP430 is a small embedded processor it does not have an equivalent to system calls
(syscalls) that are common in modern processors supported by full operating systems. Nevertheless, in some applications, including the Microcorruption CTFs, a library can introduce the equivalent of certain system calls. We take a similar approach as in the creators of the Microcorruption CTFs to add syscalls to the
MSP430 ISA. We will give more details about this modeling in Section 4.2.
Processor Predicates. There are many predicates over the execution trace that are highly relevant to demonstrating exploitability. For example, one simple predicate would be that the final program counter
(PC) in the trace is some particular challenge value; if an attacker can set the PC arbitrarily, they likely can execute arbitrary code. We also consider more complex predicates, like showing that a syscall was executed during the trace that should have been impossible (e.g. turning on the device’s microphone). Predicates about syscalls can also be used to show privilege escalation, by showing that the GETEUID syscall returned the value 0. Selecting the right predicate—or set of predicates—is an exploit-specific task that can be done by either the vulnerability researcher (once they have found an exploit) or the bug bounty program when setting their bounties.
To support such predicates, we add syscall support to our processor circuit, making it the first ZK processor to include syscalls. When the program encounters a syscall, the processor freezes the registers and enables the finite state machine. The processor executes the syscall for an arbitrary number of steps until some exit condition is met (e.g., for the GETS syscall, until the processor reads a maximum number of characters or encounters a null byte). The processor then unfreezes and continues execution. This allows syscalls to be unrolled on the fly without requiring significant, special-purpose circuitry.
5

2.3
Producing Efficient ZK Proofs of Exploit
With a formalization of exploits in hand, we develop a toolchain to produce proofs of exploit. An overview of our toolchain can be found in Figure 1, including a processor emulator, the RAM reduction assembler, and the ZK prover. The remaining task is to develop the necessary cryptographic optimizations such that the proofs of exploit that our toolchain produces are efficient.
Notation. We use [b] for a share of a bit b, similarly we will use JxK for an arithmetic share of an element x in the respective arithmetic ring.
Reverie.
Our second main technical contribution in this work is Reverie, the first publicly available,4 general use implementation of the KKW MPC-in-the-head ZK protocol [KKW18]. Reverie is written in
Rust and incorporates many optimizations to make it more efficient, including bit slicing, memory efficient representations of the circuit, and proof streaming. The prover can compute the root of a Merkle tree with 256 leaves in just 8 seconds, significantly faster than prior NIZK implementations (see Table 1 in Section 8).
Reverie also improves on KKW’s initial protocol by including efficient ring switching based on ed- aBits [EGK+20].
To switch an element between rings, the prover generates shares of random elements in the two relevant rings during preprocessing. The prover then masks the value, reconstructs it in the clear, ring switches the public element, and removes the secret-shared mask.
For example, consider ring switching a value v ∈F232 into an equivalent binary decomposition (v1, v2, . . . , v32) ∈F32 2 . The prover begins by generating random sharings of the values r ∈F232 and (r1, r2, . . . , r32) ∈F32 2 for the simulated players during the preprocessing, subject to the constraint r = P32 i=1 ri2i. During online execution, the simulated parties publicly reconstruct the value v + r and then decompose the public value into its binary representation (v1 +r1), . . . , (v32 +r32). The simulated parties then subtract their local shares of r1, . . . , r32, resulting in a valid secret sharing of the values (v1, v2, . . . , v32) ∈F32 2 . This ring switching protocol is very efficient because generating verifiable, structured correlated randomness during preprocessing is very communication and computation efficient when using the KKW ZK protocol.
Efficient Permutation Proof. The RAM reduction outlined in Section 2.1 uses a routing network to implement the permutation proof between the execution trace and the memory trace. The routing network has asymptotic complexity O(t log(t)), where t is the trace length, and large constants. A more efficient permutation proof, first explored by [Nef01,BCG+18], shows that two secret lists {Ai}i∈[ℓ] and {Bi}i∈[ℓ] are permutations by sampling a random challenge x
$←−Zq and testing if
ℓ
Y i=1
(Ai −x)
?=
ℓ
Y i=1
(Bi −x).
To ensure that this test has negligible soundness error, it must be performed in a large field. However, our MSP430 processor operates over F2. Thus, the ring switching technique introduced above is vital to facilitating this permutation proof. Without access to an efficient ring switching technique, the test would have to be carried out in a small field with large soundness error, or the processor would need to operate over a large field, which would introduce high computational overhead. Concretely, the permutation proof costs just 380 AND gates and 2 multiplications for each element in the list.
Evaluation. We evaluate our toolchain by producing ZK proofs of exploitability for the Microcorruption
Capture The Flag (CTF) exercises. Microcorruption CTF is a series of popular embedded device (MSP430)
exploitation exercises that are freely available online. These exercises serve as a common entry point for individuals wishing to learn binary exploitation. Each challenge is named after a world city (see Table 2), and the exercises cover many common exploit techniques, such as heap and buffer overflows. Additionally, the processor implements important mitigation strategies, such as stack canaries, DEP, and ASLR. Thus, pro- ducing proofs of exploits for the Microcorruption CTF exercises demonstrates a wide variety of exploitation techniques, demonstrating the practicality of our approach.
4https://github.com/trailofbits/reverie 6

The prover begins by initializing the processor emulator to a fresh state and loads the public binary. The prover then emulates the binary when run on the private input, which produces an execution trace containing the processor state for each step and a memory trace containing the memory operations for each step. This emulation process stops once the desired processor state is reached (e.g., the processor makes a restricted syscall). The prover then assembles the unrolled circuit from the pre-compiled library of components based on the length of the traces. The assembled circuit is provided as the statement to the ZK prover, and the traces are provided as a witness. Note that the only requirement we make of the ZK prover is that it is capable of performing ring switching.
Concretely, in one second, our implementation can produce a NIZK of correct processor execution of 216
MSP430 instructions requiring 119 KB of communication per instruction.
3
Related Work
Modeling RAM programs in ZK. TinyRAM [BCG+13] and BubbleRAM [HK20a] are two custom ISAs developed to maximize performance with existing ZK schemes. They both use a load/store architecture with fewer than 30 instructions and ensure that decoding each instruction is inexpensive within a ZK prover.
Among such works are vRAM [ZGK+18] which constructs verifiable computation with a universal trusted setup for the TinyRAM ISA. The aims of our work differs from those in the verifiable computation literature in a number of important ways: (1) the proof size is linear (in particular the verifier complexity is linear).
(2) we aim for concretely efficient prover complexity by using only symmetric key operations as opposed, e.g.
to pairings in vRAM. (3) our techniques do not rely on a trusted setup (universal or otherwise) (4) we target real-world architecture. Despite proving a much more complicated architecture the proving speed (emulated
CPU cycles/second) in this work (for MSP430) is ≈5 times greater than vRAM (for TinyRAM). While Ben
Sasson et al. [BCTV14] later modified TinyRAM to have a von Neumann architecture, BubbleRAM remains a Harvard architecture processor, which prevents it from reasoning about exploits that inject malicious code onto the stack or heap.
As we discuss in the next subsection, the use of these custom ISAs limits the capabilities of a prover. For example, provers compile source code to the custom ISA, and source code is not available for many pieces of security critical software.
Proofs of Exploitability. In discussing prior work, we emphasize the difference between a vulnerability and an exploit. An exploit is maliciously crafted program input that produces unintended program behavior—or may even allow an attacker to affect the state of the computer beyond the program itself. A vulnerability, on the other hand, is a software weakness that could potentially be used in designing an exploit, for example an out-of-bounds memory write or a use-after-free bug. Vulnerabilities do not depend on architecture-specific constructs like the stack, heap, or mitigations such as ASLR, DEP, and pointer authentication codes (PAC).
An exploit, however, is intrinsically linked to processor semantics. Therefore, it is not sufficient to reason only about source code when demonstrating the existence of an exploit.
Prior work on using ZK proofs for vulnerability disclosure [HK20b,HK20a] has focused on manually anno- tating C code with assertions that a prover must demonstrate they can violate. This is accomplished by com- piling the annotated code either directly to a circuit or to a custom ZK processor (e.g., TinyRAM [BCG+13]
or BubbleRAM/BubbleCache [HK20a,HYDK21]). While this approach is capable of proving many interest- ing vulnerabilities with extremely high efficiency, it has several drawbacks.
First, annotation of complex, real-world programs is time-consuming and error-prone. Source annotations cannot express many of the most commonly exploited classes of bugs [Sma19, Mil19], and even the bugs theoretically detectable with annotations are difficult for programmers to find. Even if all these limitations could be overcome, this approach inherently requires access to source code, which is often not available.
Second, bugs in source do not always translate to exploits on a real processor. The example used by
Heath and Kolesnikov [HK20b] focuses on proving the existence of an out-of-bounds memory access—an operation many compilers will automatically prevent.
Finally, while bugs in source are common, successful exploits are rare. Fuzzing campaigns often find a large number of software bugs, but rarely convert these bugs into meaningful exploits. Research teams 7

are unlikely to disclose a simple out-of-bounds read in ZK, as most such bugs do not lead to meaningful system compromise. Real bug bounties and vulnerability research consists of demonstrating how to leverage a vulnerability into an exploit (e.g., privilege escalation, arbitrary code execution, or reading protected memory). Proving these capabilities cannot be done with source alone and are intrinsically linked to the compiled binary and architecture.
For example, Heath et al. [HYDK21] claim that they can prove the existence of vulnerabilities in sed and gzip despite using a Harvard architecture. While it is true that they can prove vulnerabilities on such an architecture, they would not be able to demonstrate that the vulnerability is exploitable if the exploit involved executing malicious code off the stack, since the machine would not be able to fetch instructions stored in RAM.
4
Modeling Real-World Processors
In this section we discuss the technical details of modeling our target real-world processor, MSP430. First we discuss the necessary modeling to cover the basic MSP430 processor semantics and then discuss additions to the processor semantics that are helpful when modeling exploits.
4.1
Modeling MSP430 Processor Semantics
The MSP430 is a ubiquitous microcontroller [Odu20], making it the perfect target for proofs of exploit.
The MPS430 architecture contains 27 instructions, 13 addressing modes, and 16 registers with 16-bit words.
We design a circuit which models the state transition associated with each of these instructions. We note, however, that MSP430 is not a load/store architecture—unlike the processor designed for ZK proofs—which increases the complexity of modeling memory.
Modeling Memory. Prior work on ZK processors use load/store architectures to cleanly separate memory accesses and logical operations. This allows the RAM reduction to treat non-memory operations as no- ops when performing the memory consistency check and permutation proof.
However, many real-world processors, such as the MSP430, use a variety of addressing modes that prevent such a clean distinction from being made. For example, consider the instruction add add @r5, 2(r6), which adds the contents of memory at the address r5 to the contents of memory at address r6+2 and stores the result at address r6+2.
Not only does this instruction both access memory and use the processor’s ALU, but it actually performs two reads and a write.
Our processor model handles such instructions by augmenting each instruction in the program trace to include three memory hints, which are used by the decoded instruction and verified with the memory checker.
The hints are separated into two read hints, src and dst, and a single write hint. The hints each contain the relevant information for the implicit load/store operations encoded into some instructions (e.g. the address and value of memory to read/write). Specifically, the memory hints have the following structure:
• 1-bit On/Off indicator
• 16-bit Memory Address
• 19-bit Timestamp
• 1-bit Read/write indicator
• 1-bit Byte Mode indicator
• 1-bit Byte Mode Offset
• 16-bit Value
MSP430 supports byte operations on memory, so each memory hint indicates if it is in byte mode and the index of the byte on which the instruction is operating, if applicable.
Because MSP430 is a Von-Neumann architecture, fetching instructions constitutes a memory read. Each
MSP430 instruction consists of a one-word opcode and up to two immediates, each of which requires its own read hint. Thus, the memory trace will contain six entries for each entry in the program trace. Checking these memory operations for consistency is straightforward, requiring only 194 AND gates per entry, so the memory checker requires 1,164 AND gates/cycle.
8

4.2
Interacting with the Program
In order to facilitate proofs of exploit, we choose to extend the base MSP430 ISA with cleanly modeled methods that allows the prover to interact with the program. Specifically, we are concerned with loading the program into the runtime, getting user inputs, and providing the program with entropy. While there are many potential ways to add these capabilities to the base ISA, we choose to add system calls that support these capabilities. This choice is inspired by the Microcorruption CTF challenges, which modeled system calls similarly in their version of the MSP430 ISA; by mirroring the choices made by the designers of the
Microcorruption CTF challenges, we are able to “natively” support solutions for the challenges by directly mapping their syscalls onto our syscalls.
Modeling System Calls. System calls are an integral component of real-world software, providing the program access to key resources, including randomness, memory management, and user input. Many suc- cessful exploit strategies—and the techniques used to prevent such exploits—depend on the low-level details of syscall operations. For example, many processors implement memory protections such as ASLR by using system entropy to randomize the address space layout. Prior work on ZK processors ignores syscalls and does not provide the processor with randomness.
We provide a general approach to handling syscalls initiated via software interrupts. Our approach does not rely on adding new instructions or storing information in registers or memory, as this would change the low-level processor behavior we aim to preserve. Instead, we augment each trace entry with a 48-bit value that encodes a finite state machine representing the current syscall status. This finite state machine is fed to a co-processor which is only triggered once a software interrupt is called. When a syscall is triggered, the following sequence of events occurs:
1. The processor freezes the register file, turns on the syscall flag, and loads the arguments and opcode into the syscall register.
2. Execution continues, but the processor operates on the syscall register instead of the register file.
3. Once the exit condition has been met, the syscall flag is turned off and normal execution resumes.
To better demonstrate this approach, we give the full details for our implementation of the LOAD, GETS, and
RAND syscalls.
Getting user input. Before program execution begins, the prover uses the LOAD syscall to pre-load their input into a special memory bank that is read-only once program execution begins. Pre-loading input is im- portant for reasoning about exploits that circumvent ASLR and stack canaries, since knowing or influencing the random values used in such mitigations would make significant parts of the exploit trivial.
When the processor starts execution, the PC is set to the first instruction in the input binary, but the syscall co-processor is turned on and set to LOAD. The first instruction of the trace declares how many bytes of input will be loaded, and this value is placed in the syscall register. The processor will then continue to execute LOAD instructions, each time decrementing the syscall register until it reaches zero. At this point the syscall flag is turned off and program execution begins. At each step of the program, the processor checks that the prover cannot call LOAD after execution begins.
Once the input has been pre-loaded, the processor accesses it via the GETS syscall.
GETS takes two arguments off the stack: the address to which the input will be written, and the maximum allowed length of the input in bytes. The syscall will exit once a null byte is encountered in the input or the maximum number of bytes is written.
When our MSP430 model encounters a call to GETS, the register file is frozen by turning on the syscall flag, and the target address and length are loaded into the syscall register. Subsequent clock cycles will use the memory hints in the trace to load user input byte-by-byte into memory, incrementing the address and decrementing the length variable in the syscall register. At each step, the input is checked for a null byte and the length variable is verified not to be zero. If either is zero, the syscall flag is turned off and normal processor execution resumes. Using this approach, the processor can emulate syscall operations — including the unrolling of variable length loops within the syscall logic — without altering the binary or memory state.
9

Processor Entropy. Our target version of MSP430 uses the RAND syscall to generate random values. In general, generation of high-entropy random values can be done using Fiat-Shamir. However, sometimes applications may use low-entropy random values, which cannot be generated using Fiat-Shamir while pro- viding strong soundness guarantees, as the prover could grind to ensure that the randomness has the desired value. For example, 16-bit random values are used when calculating ASLR offsets and stack canaries. This limitation is inherent in the architecture itself — defenses that rely on low-entropy randomness will always be vulnerable to computationally powerful adversaries.
To provide some meaningful soundness in the case where low entropy defenses are used, we design our processor to naturally extend to interactive proofs in which the verifier can supply randomness directly.
First, the prover commits to all inputs that will be fed into the program by loading these values into a special memory bank prior to program execution, as specified in the previous section. Then, the verifier supplies a random seed value seed from which all randomness for the RAND syscall will be generated.
Specifically, the processor executes a special GETRANDSEED syscall to load the verifier supplied randomness seed into an auxiliary RAND register. The GETRANDSEED syscall can only be called once and only after the initial LOAD syscall has finished executing.
The processor circuit will fail if the prover attempts to call
GETRANDSEED again.
Once the prover has completed the LOAD phase, they execute the following steps in the clear:
1. Show the verifier that the PC is set to the program entry point, the syscall flag is turned on, and the syscall opcode is set to GETRANDSEED 2. Acquire the randomness seed from the verifier 3. Load the randomness into a public auxiliary RAND register 4. Turn the syscall flag off
Since the syscall flag is turned off once GETRANDSEED is finished, program execution must proceed normally from the binary entry point. During each processor cycle, the prover will evaluate PRF(seed, step), where
PRF is a pseudorandom function, and step is a counter indicating the number of processor cycles that have been executed. The first 16 bits of the output are then fed into the processor as the potential output of the
RAND syscall. We emphasize that returning only 16 bits of randomness is inherent to the architecture. By making the prover commit to all their inputs to the program before learning the seed, they must commit to an exploit strategy that can work for any value of randomness generated. We repeat that the meaning of a proof of exploit that circumvents low-entropy protections is nuanced; we refer the reader back to Section 1.1 for a discussion.
Users are provided with the option to disable processor randomness, since many applications do not need this feature. Additionally, note that running these proofs interactively is only necessary when there are low-entropy defense mechanisms that the prover must overcome, like ASLR.
5
Formalizing Exploits
Our aim is to provide vulnerability researchers with the necessary tools to precisely demonstrate exploits in real software without revealing underlying techniques. Therefore, we focus on creating a system that allows the prover to show that it knows some inputs such that running a public binary on those inputs on a real machine would result in a concrete exploit. This proof requires two components: demonstrating a given trace is valid, and demonstrating the trace triggered an exploit. The first component is handled using the previously discussed RAM reduction. We now discuss how exploits are shown during execution.
Many exploits can be detected by determining whether the attacker has arbitrary PC control. In this setting, the verifier challenges the prover to demonstrate they were able to produce a valid program trace concluding with the PC set to the challenge address. A similar protocol is used in the context of exploits that gain the ability to arbitrarily read or write memory.
A variety of exploits conclude with the execution of a syscall that should not have been accessible to the attacker. In an embedded systems context, this may manifest itself as turning on a microphone, turning 10

off a security camera, or unlocking a door. This particular notion of exploit is relatively straightforward to formalize in a ZK context. The prover simply needs to demonstrate that at some point during a valid program execution, a known malicious syscall was executed. This can be checked at the processor level by checking at each step whether the syscall flag is on and then examining the syscall opcode as specified in Section 4. All of these checks can be fed to a large OR statement at the conclusion of the proof to demonstrate whether a malicious syscall was executed. As we discuss in Section 8, this is how we formalize the Microcorruption exploits, all of which conclude in a call to the special UNLOCK interrupt.
Proving privilege escalation exploits — exploits which allow the prover to execute commands with root privileges on the machine — is more complicated. Generally, this would involve calling the GETEUID syscall and demonstrating the output is 0, using a similar approach as above. However, this would require modeling a runtime environment complex enough to have a notion of user privileges. We leave modeling a complex runtime environment as important future work.
Generally speaking, our approach facilitates proofs about exploits that can be represented as a Boolean expression on each processor state across the entire program execution. All of the above techniques are examples of this broader paradigm (e.g., there exists a step of execution such that the instruction loaded by the processor is a malicious syscall). While this approach is sufficiently general to cover most common exploits, it has some fundamental limitations. In particular, our proof of exploit toolchain is incapable of reasoning about exploits that rely on microarchitectural bugs such as Spectre and Meltdown. Similarly, a
Row Hammer type attack would also be out of scope since unintended physical properties of RAM cannot be simulated within a ZK context. Fortunately, most real-world exploits do not rely on microarchitectural bugs, so we do not view this as a major limitation.
Barriers to Easy Use. Although our toolchain allows provers to produce proofs for any predicate over the processor states, the process of selecting the right predicate may be non-trivial—especially for vulnerability researchers without zero-knowledge expertise. Indeed, in our envisioned workflow (Section 1), we imagine that a sponsor might post a bug bounty to which vulnerability researchers could respond. One approach would be to have the bug bounty itself formalize the statement to prove in zero-knowledge; this approach is implicitly used in the Microcorruption CTF exercises, as the UNLOCK syscall is part of the challenge description. In more complex systems, there may be a huge number of potential processor states that would be considered problematic, such that enumerating all the processor states would be impractical. In such cases, the burden of selecting the correct statement—and demonstrating the statement’s importance—would fall to the vulnerability researcher. Making these processes easier is important future work.
6
Circuit Compiler
The ZK proof system that we target accepts statements as either Boolean or arithmetic circuits. There are several tools created specifically for ZK statement generation such as Frigate [MGC+16a], libsnark [lib20], and Circom [cir18], but they mostly target arithmetic circuits, which are not performant when handling real-world processor models. Frigate synthesizes code written in a subset of C. However, we found that it did not give us the granularity necessary to optimize circuits for MSP430.
Instead, we chose to write our processor circuit in Verilog, a widely used hardware description language
(HDL) with mature open-source tooling. In particular, we used Yosys [Wol] to synthesize our core circuit components and Icarus Verilog for simulation and testing. Using Verilog allowed us to divide our RAM reduction into a collection of discrete Boolean modules, including the single-step MSP430 processor circuit and the memory consistency checker. We use Yosys to synthesize these components to a BLIF [19992] file that encodes the hierarchical arrangement of the components and their logic gates. Finally, we assemble these components into a flat, non-hierarchical encoding of the RAM reduction in the Bristol Fashion [AAL+22]
using a circuit flattening library.
We designed our in-house flattener to take advantage of the fact that our circuit is highly structured, so we can aggressively cache flattened versions of the components and avoid repeating work. Using this approach of flattening components once and stapling them together, our flattening library can assemble the 11

Input. Secret lists A = {Ai}i∈[ℓ] and B = {Bi}i∈[ℓ].
Public Input. A random challenge x ∈Zq.
Circuit. Compute and compare
ℓ
Y i=1
(Ai −x)
?=
ℓ
Y i=1
(Bi −x)
Output. 1 if the above check is valid, 0 otherwise.
Figure 2: Unknown Permutation Proof Circuit (Cshuffle). The circuit checks if two secret lists are permutations of each other.
full RAM reduction for traces with 7k steps in 6 minutes using 20GB of RAM—an improvement of 99% in running time and 88% in RAM usage over using Yosys for flattening.
As described in Section 7.1, our permutation proof is prohibitively complex to be evaluated via a Boolean circuit, so we elected to specify it via an arithmetic circuit on Z264. Yosys and Verilog are only designed to operate on Boolean circuits, which presents a problem because using a HDL like Verilog is substantially easier than working at the level of individual gates when designing complex circuits.
We, however, use blackbox modules—a feature of Yosys designed to connect circuits to unknown hardware— to create models for the arithmetic logic gates in Verilog, which we then used to specify our permutation proof circuit. While we still had to ultimately specify the circuit at the gate level, working in Verilog broke up the circuit into hierarchical modules and assigned names to wires, greatly reducing debugging time.
After synthesizing the permutation circuit to a BLIF file, we pass it to our circuit compositor—a modified version of the circuit flattener that can accept a flattened Boolean circuit and a flattened arithmetic circuit and generate a specification for connecting the outputs of the Boolean circuit to the inputs of the arithmetic circuit using specialized BooleanToArithmetic gates. The 3-tuple of circuits consisting of the Boolean circuit, the connection circuit, and the arithmetic circuit is then passed to Reverie, which evaluates it as the complete
ZK statement.
7
Cryptographic Optimizations
Choice of Proof System. To instantiate our toolchain and optimize our proof system, we must first select a proof system.
A number of considerations are relevant when selecting a suitable proof system for our particular application, most notably: (1) Prover/Verifier Complexity: Many widely deployed ZK proof systems are based on succinct non-interactive arguments of knowledge (SNARKs) (e.g. [PHGR13,
Gro16]), which produce compact proof size at the expense of high prover runtime, complicated knowledge assumptions, and a trusted setup phase. While these tradeoffs are practical for space-limited applications, e.g.
decentralized ledgers, the overhead of this approach would limit the complexity of RAM programs and exploits about which we could reason. Therefore we prioritize reducing concrete prover time rather than bandwidth. In order to somewhat offset the larger proof size we ensure that proofs can be verified in a streaming manner, meaning the verifier can process the proof as he is downloading it (without storing it).
(2) Interactive vs Non-interactive: While interactive (private-coin) proofs systems can enable more efficient/flexible proofs, we opt for non-interactive proofs to enable a wider variety of use cases, as discussed in the introduction. This includes posting the proof for public verification and inclusion in long-term bug tracking logs. Non-interactivity can also be valuable when the prover may no longer be online or moving proofs across air-gaps (security researchers might be wary about allowing arbitrary people to open connections to the server holding the sensitive zero-day exploit).
These considerations lead us to believe that the KKW proof system [KKW18] is well-suited for our application. We give a summary of MPC-in-the-head and the KKW proof system in Appendix A. Throughout this section we denote the party that executes the preprocessing in KKW as P0 and use n to denote the number of parties in the MPC. We note that several improvements to the initial KKW system have been proposed recently, e.g. [BN20,dOT21], that could be integrated into our approach in future work.
12

7.1
Memory Permutation Proof (over Zq)
An unknown permutation proof is a zero-knowledge proof of knowledge that shows that the prover has two lists that are a permutation of each other, i.e. list A = {Ai}i∈[ℓ] and B = {Bi}i∈[ℓ] such that π(A) = B for some permutation π. As the verifier does not know the lists nor the permutation, the proof is done with respect to a commitment to each list. We require an unknown permutation proof that will be efficient within
MPC-in-the-head.
We implement the unknown permutation proof using the circuit defined in Figure 2 over a large ring, based on techniques first introduced by Bootle et al. [BCG+18], and first explored by Neff [Nef01]. This stand-alone circuit receives two secret shared lists and a public randomly selected challenge x. Within the circuit, we view A and B as the set of roots of two polynomials, evaluate them at x and check equality, i.e. asserting Q i(Ai −x) = Q i(Bi −x). Intuitively, perfect completeness follows on the commutativity of multiplication, while statistical soundness relies on the Swartz-Zippel lemma stating that two polynomials with distinct roots share an evaluation at a random point only with small probability5.
For soundness, the random challenge x must be selected after the prover has committed to the secret shared lists, however the subsequent computation depends on the challenge.
We accommodate this by introducing an additional round (5 rounds total)6 in which the verifier samples x, after the prover has committed to the inputs/witness, but before committing to the views of every party.
Theorem 1 (Unknown Permutation Proof) Given two lists A and B with ℓelements in Zq and an instance of the KKW protocol with n participants and m preprocessing repetitions. Using the above circuit and the challenge input inside a KKW protocol is an honest-verifier ZKPoK to prove knowledge of two lists A and B such that there exists a permutation π such that π(A) = B with soundness/knowledge error max n 1 m, 1 n +
ℓ q−1 −
ℓ q−1 1 n o
.
The proof of this theorem can be found in Appendix B.1.
When amplifying the soundness by parallel repetitions, the soundness error of the permutation proof is dominated by the soundness error of KKW. As such, it is straightforward to observe that using this permutation proof does not introduce the need for any additional repetitions of the proof. We show this formally in Appendix C, along with discussing the technical detail of performing these operations in a ring, rather than a field 7.2
Ring Switching
One drawback of the permutation proof described in the previous section is that it relies on a large field/ring for soundness which leads to inefficient proofs of Boolean circuits. Unfortunately, real-world processors are most efficiently realized as Boolean circuits that pay a high cost for multiplication gates. The permutation proof can be implemented in a Boolean circuit by simulating a larger ring, however the log2(q) overhead introduced by simulating the ring multiplication negates the improvements over the routing network used in the work of Ben-Sasson et al. To avoid simulating arithmetic in a large ring, while still enabling application logic (CPU specification) to be proved using a Boolean circuit we rely on ring-switching techniques: enabling us to switch/pack a collection of Booleans into an element in a ring of sufficiently large order. This technique introduces an overhead of 3 AND-gates for every bit that needs translating. In our case, where we will switch to Z264, this means 192 AND-gates for every element in both lists. We base our ring-switching technique on the use of edaBits as introduced by Escudero et al. [EGK+20], which in turn was based on daBits by Rotaru and Wood [RW19]. We will apply the preprocessing optimization of KKW to achieve these results.
Preprocessing.
Let ξ be the number of bits required to represent values of the larger field.
During the preprocessing phase, we generate secret shares for the MPC players of the correlated random values r 5When the size of the field dominates the degree of the polynomials. Note we do not need the soundness error to be negligible, but only to be dominated by n−1/n from KKW.
6We reason that this additional round does not affect the knowledge error of the Fiat-Shamir transform, compared to the original 3 rounds. Note that, in general, soundness of the Fiat-Shamir transform decreases exponentially in the number of rounds.
13

and r0, . . . , rξ−1, where r is a value in the larger ring and r0, . . . , rξ−1 are Boolean values, subject to the constraint r = Pξ−1 i=0 ri2i, in the larger field. Thus, the players receive Boolean sharings [r0], . . . , [rξ−1] and an arithmetic sharing JrK. Note that none of the participants have any of the values r, r0, . . . , rξ−1 in the clear, they only possess a share of these values. Generation of this correlated randomness can be done using the same techniques used for Beaver triple generation in KKW: the dealer (P0) generates and “sends” the shares to the respective players.
Online. The translation of ([x0], . . . , [xξ]) into JxK with x =
ξ
X i=0 xi2i is done in the following way:
(1) In the Boolean circuit compute the Zq addition of r + x using a full adder, i.e. compute:
[(x + r)0], . . . , [(x + r)ξ−1] =
([x0], . . . , [xξ−1]) +Zq ([r0], . . . , [rξ]))
(2) Reconstruct the masked bits (x + r)0, . . . (x + r)ξ−1 ∈Z2, lift the bits to the ring Zq and and convert the decomposition into x + r ∈Zq by publically computing the linear combination: x′ = x + r =
Pξ−1 i=0 2i(x + r)i ∈Zq
(3) In the arithmetic circuit subtract the randomness r from x′ the input coming from the Boolean circuit, i.e. x = x′ −r.
Note that only (1) has non-linear (over Z2) operations.
Theorem 2 (Ring Switching) Given a Boolean circuit Cbool and an arithmetic circuit Carith that need to be run consecutively, a definition of which output wires from Cbool are going into Carith, and an instance of the KKW protocol with n participants and m preprocessing repetitions. The above protocol is an honest- verifier ZKPoK with soundness/knowledge error max
 1 m, 1 n

.
The proof of this theorem can be found in Appendix B.2. Note that the soundness error is exactly the same as for the original KKW protocol, therefore, no extra iterations of the protocol are needed because of the addition of the ring switching.
8
Implementation and Evaluation
Reverie. Our prover ‘Reverie’ [rev22] is an optimized implementation of the KKW [KKW18] proof system in the Rust programming language. Reverie is generic and can be instantiated over any commutative ring.
Reverie optimizes KKW for our particular application as follows:
• Streaming. Rather than compute the correlated randomness for the entire circuit before evaluation,
Reverie interleaves the preprocessing with the online execution: in effect player P0 is implemented as a coroutine. This avoids storing all the preprocessed material in memory.
• Bit Slicing. Every online player in KKW executes the same simple operation during the evaluation of addition and multiplication gates, hence bit-slicing ‘across the players’ allows executing every player in parallel, e.g. for the ring R = F2 and n = 64 the values of two wires can be added using a single XOR of 64-bit integers.
14

Table 1: Comparative Measurements for NIZKs computing 511 iterations of SHA256 (Merkle tree with 256 leaves).
Mea- surements for prior work from [XZZ+19] on an Amazon EC2 c5.9xlarge with 70GB of RAM and Intel Xeon platinum 8124m
CPU with 18 3GHz virtual cores. Because these proof systems and implementations were unable to exploit parallelism, all benchmarks were run on a single thread. Reverie was benchmarked on a Digital Ocean virtual machine with 32 virtual cores and 256GB of memory. We note that our choice of protocol and our implementation is able to take advantage of the parallelism offer by the multiple cores, which is part of the reason Reverie is able to dramatically out-perform prior work.
Proof System
Gen
(sec)
Prove
(sec)
Ver
(sec)
Size
(KB)
Aurora [BCR+19]
- 3,199 15.2 174.3
Bulletproofs [BBB+18]
- 2,555 98 2 libSTARK [BBHR18]
- 2,022 0.044 s 395
Hyrax [WTs+18]
- 1,041 9.9 185
Ligero [AHIV17]
- 400 4 1,500 libSNARK [BCTV14]
1027 360 0.002
.013
Libra [XZZ+19]
210 201 0.71 51
Reverie (This Work)
- 8 7.67 113,848
• Shadowing. The model of execution in ‘Reverie’ is a straight-line RAM program: there is an array of cells and a program consists of a list of Input/Add/Mul/Output instructions reading/writing to cells. A circuit is a straight-line program in single assignment form (i.e. every cell is only written to once). Since the execution of a CPU is very local, this allows us to reclaim memory by overwriting cells, in practice reclaiming > 95% over na¨ıvely loading the circuit.
• Parallel. KKW requires many repetitions for soundness, these are executed in parallel.
All of these optimizations contribute to Reverie’s exceptionally fast performance. Reverie is able to prove 511 iterations of SHA256 in 8 seconds.
We compare this to the benchmarks reported in prior work from [XZZ+19] in Table 1. We note that these are not strictly apples-to-apples comparisons as we were unable to control for the benchmarking environment for prior work. However, we note that Reverie does strikingly well. Libsnark requires 1,387 seconds, Bulletproofs requires 2,555 seconds, and Ligero requires 400 seconds (see Table 1). The proofs generated by Reverie are larger than the other three, but since it supports streaming all that is required is a network connection between prover and verifier with modest bandwidth.
Proofs of Exploitability: Microcorruption. We chose to use the Microcorruption CTF as a benchmark set for our ZK proof of vulnerability system. The CTF challenges involve hacking a smart lock controlled by an MSP430 using common exploitation techniques such as buffer overflows, code injection, and bypassing memory protections. While the challenges contain a wide variety of bugs, ultimately they all conclude with a call to the UNLOCK system call. For example, the Addis Ababa challenge can be solved by using a format string vulnerability to overwrite a segment of memory that contains information about whether the correct password was entered or not, leading to a successful call to the UNLOCK system call.7.
Therefore our ZK proofs of vulnerability check both that the witness trace is valid, and that at least one step of execution was a call to the UNLOCK system call. An advantage of this approach is that all ZK performance metrics are linear in the trace size, regardless of exploit technique.
Performance. We present benchmarks for a representative set of the Microcorruption exercises in Table 2.
This set of benchmarks covers many of the most important exploit types, including buffer overflow, code injection, and bypassing memory protection. Each of these benchmarks was computed on a Digital Ocean virtual machine with 32 virtual cores and 256GB of memory. We found that our implementation produces a proof for 216 MSP430 instructions every second. Overall, each instruction requires 10,691 AND gates to 7For more details about the Microcorruption challenges, we point the reader to https://microcorruption.com or the refer- ence manual [Mic13b]
15

Table 2: Benchmarks for proofs of exploits (at 128 bits of security) for a representative subset of the Microcorruption exercises.
The selected exercises cover the most important exploit categories, including buffer overflow, code injection, and bypassing memory protection. These exercises are ordered by the difficulty of the exercise, as estimated by the Microcorruption creators.
Exercise Name
Processor Cycles
Prover (sec)
Verifier (sec)
Size (mb)
Exploit Type
New Orleans 2392 22 7 295
Password embedded in binary
Hanoi 6199 25 18 322
Buffer overflow
Cusco 5178 21 15 269
Buffer overflow
Montevideo 6676 28 20 358
Code injection via strcpy bug
Johannesburg 6311 26 19 332
Stack cookie bypass
Santa Cruz 12835 754 39 680
Code injection via strcpy bug
Addis Ababa 5360 23 17 296
Format string vulnerability
Novosibirsk 19833 89 63 1100
Format string vulnerability
Vladivostok 50823 454 152 6048
ASLR bypass
Table 3: Breakdown of processor circuit components
Component
Non-linear Gates Per Instruction
Memory checker 1,164
Permutation proof 2,280
Processor 7,247
Decoder 568
ALU 549
Hint verifier 237
Operand fetching 2,176
Register file 2,880 execute. In Table 3, we give a breakdown of the gate count for each component of the RAM reduction, along with the major components of the processor. Although the resulting proofs produced are large and may take a non-trivial time to create, we note that these resources and time are insignificant compared to the effort it takes to develop the exploit and the time that the parties would spend negotiating disclosure.
9
Conclusion
We have presented a toolchain that can practically prove knowledge of real exploits for real-world processor architectures without the need for source code. Our approach offers a concrete solution to a real-world problem: how should vulnerability researchers demonstrate their capabilities to the managers of bug bounty programs?
Using our proof system, the managers of bug bounty programs need not be concerned that vulnerability researchers are overstating their findings and vulnerability researchers are protected against preemptive disclosure. Moreover, our techniques can be used to enhance the current bug bounty ecosystem by allowing robust, trustworthy public disclosure of vulnerabilities without handing attackers live exploits.
Given the importance of bug bounty programs to security critical software, we believe that our work repre- sents a significant step forward.
Acknowledgements
This work is supported by DARPA under agreement No. HR001120C0084. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the United States Government or DARPA. The first author is also supported in part by 16

NSF under awards CNS-1653110, and CNS-1801479, the Office of Naval Research under contract N00014-19- 1-2292, as well as a Security and Privacy research award from Google. The second author is also funded by
Concordium Blockchain Research Center, Aarhus University, Denmark. The forth author is also supported by the National Science Foundation under Grant #2030859 to the Computing Research Association for the
CIFellows Project and is also supported by DARPA under Agreement No. HR00112020021.
References
[19992]
Berkeley logic interchange format (blif). 1992.
[AAL+22]
David Archer, Victor Arribas Abril, Steve Lu, Pieter Maene, Nele Mertens, Danilo Sijacic, and
Nigel Smart. ’bristol fashion’ mpc circuits. https://homes.esat.kuleuven.be/~nsmart/MPC/, 2022.
[AHIV17]
Scott Ames, Carmit Hazay, Yuval Ishai, and Muthuramakrishnan Venkitasubramaniam. Ligero:
Lightweight sublinear arguments without a trusted setup. In Bhavani M. Thuraisingham, David
Evans, Tal Malkin, and Dongyan Xu, editors, ACM CCS 2017, pages 2087–2104. ACM Press,
October / November 2017.
[AMS08]
V. Arvind, P. Mukhopadhyay, and S. Srinivasan. New results on noncommutative and commu- tative polynomial identity testing. In 2008 23rd Annual IEEE Conference on Computational
Complexity, pages 268–279, 2008.
[BBB+18]
Benedikt B¨unz, Jonathan Bootle, Dan Boneh, Andrew Poelstra, Pieter Wuille, and Greg
Maxwell. Bulletproofs: Short proofs for confidential transactions and more. In 2018 IEEE
Symposium on Security and Privacy, pages 315–334. IEEE Computer Society Press, May 2018.
[BBHR18]
Eli Ben-Sasson, Iddo Bentov, Yinon Horesh, and Michael Riabzev. Scalable, transparent, and post-quantum secure computational integrity. Cryptology ePrint Archive, Report 2018/046, 2018. https://eprint.iacr.org/2018/046.
[BBHR19]
Eli Ben-Sasson, Iddo Bentov, Yinon Horesh, and Michael Riabzev. Scalable zero knowledge with no trusted setup. In Alexandra Boldyreva and Daniele Micciancio, editors, CRYPTO 2019,
Part III, volume 11694 of LNCS, pages 701–732. Springer, Heidelberg, August 2019.
[BCG+13]
Eli Ben-Sasson, Alessandro Chiesa, Daniel Genkin, Eran Tromer, and Madars Virza. SNARKs for C: Verifying program executions succinctly and in zero knowledge. In Ran Canetti and
Juan A. Garay, editors, CRYPTO 2013, Part II, volume 8043 of LNCS, pages 90–108. Springer,
Heidelberg, August 2013.
[BCG+14]
Eli Ben-Sasson, Alessandro Chiesa, Christina Garman, Matthew Green, Ian Miers, Eran
Tromer, and Madars Virza. Zerocash: Decentralized anonymous payments from bitcoin. In 2014 IEEE Symposium on Security and Privacy, pages 459–474. IEEE Computer Society Press,
May 2014.
[BCG+18]
Jonathan Bootle, Andrea Cerulli, Jens Groth, Sune K. Jakobsen, and Mary Maller.
Arya:
Nearly linear-time zero-knowledge proofs for correct program execution. In Thomas Peyrin and
Steven Galbraith, editors, ASIACRYPT 2018, Part I, volume 11272 of LNCS, pages 595–626.
Springer, Heidelberg, December 2018.
[BCGT13]
Eli Ben-Sasson, Alessandro Chiesa, Daniel Genkin, and Eran Tromer. Fast reductions from
RAMs to delegatable succinct constraint satisfaction problems: extended abstract. In Robert D.
Kleinberg, editor, ITCS 2013, pages 401–414. ACM, January 2013.
17

[BCR+19]
Eli Ben-Sasson, Alessandro Chiesa, Michael Riabzev, Nicholas Spooner, Madars Virza, and
Nicholas P. Ward. Aurora: Transparent succinct arguments for R1CS. In Yuval Ishai and
Vincent Rijmen, editors, EUROCRYPT 2019, Part I, volume 11476 of LNCS, pages 103–128.
Springer, Heidelberg, May 2019.
[BCTV14]
Eli Ben-Sasson, Alessandro Chiesa, Eran Tromer, and Madars Virza. Succinct non-interactive zero knowledge for a von neumann architecture.
In Kevin Fu and Jaeyeon Jung, editors,
USENIX Security 2014, pages 781–796. USENIX Association, August 2014.
[BFH+20]
Rishabh Bhadauria, Zhiyong Fang, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam,
Tiancheng Xie, and Yupeng Zhang. Ligero++: A new optimized sublinear IOP. In Jay Ligatti,
Xinming Ou, Jonathan Katz, and Giovanni Vigna, editors, ACM CCS 2020, pages 2025–2038.
ACM Press, November 2020.
[BN20]
Carsten Baum and Ariel Nof.
Concretely-efficient zero-knowledge arguments for arithmetic circuits and their application to lattice-based cryptography.
In Aggelos Kiayias, Markulf
Kohlweiss, Petros Wallden, and Vassilis Zikas, editors, PKC 2020, Part I, volume 12110 of
LNCS, pages 495–526. Springer, Heidelberg, May 2020.
[BNP08]
Assaf Ben-David, Noam Nisan, and Benny Pinkas. FairplayMP: a system for secure multi-party computation. In Peng Ning, Paul F. Syverson, and Somesh Jha, editors, ACM CCS 2008, pages 257–266. ACM Press, October 2008.
[CDG+17]
Melissa Chase, David Derler, Steven Goldfeder, Claudio Orlandi, Sebastian Ramacher, Chris- tian Rechberger, Daniel Slamanig, and Greg Zaverucha. Post-quantum zero-knowledge and signatures from symmetric-key primitives. In Bhavani M. Thuraisingham, David Evans, Tal
Malkin, and Dongyan Xu, editors, ACM CCS 2017, pages 1825–1842. ACM Press, Octo- ber / November 2017.
[cir18]
Circom: a circuit compiler for zksnarks, 2018. https://github.com/iden3/circom.
[dOT21]
Cyprien de Saint Guilhem, Emmanuela Orsini, and Titouan Tanguy. Limbo: Efficient zero- knowledge MPCitH-based arguments. In Giovanni Vigna and Elaine Shi, editors, ACM CCS 2021, pages 3022–3036. ACM Press, November 2021.
[EGK+20]
Daniel Escudero, Satrajit Ghosh, Marcel Keller, Rahul Rachuri, and Peter Scholl. Improved primitives for MPC over mixed arithmetic-binary circuits. In Daniele Micciancio and Thomas
Ristenpart, editors, CRYPTO 2020, Part II, volume 12171 of LNCS, pages 823–852. Springer,
Heidelberg, August 2020.
[FKL+21]
Nicholas Franzese, Jonathan Katz, Steve Lu, Rafail Ostrovsky, Xiao Wang, and Chenkai Weng.
Constant-overhead zero-knowledge for RAM programs.
Cryptology ePrint Archive, Report 2021/979, 2021. https://eprint.iacr.org/2021/979.
[GMO16]
Irene Giacomelli, Jesper Madsen, and Claudio Orlandi.
ZKBoo: Faster zero-knowledge for
Boolean circuits. In Thorsten Holz and Stefan Savage, editors, USENIX Security 2016, pages 1069–1083. USENIX Association, August 2016.
[GMW86]
Oded Goldreich, Silvio Micali, and Avi Wigderson. Proofs that yield nothing but their validity and a methodology of cryptographic protocol design (extended abstract). In 27th FOCS, pages 174–187. IEEE Computer Society Press, October 1986.
[GMW87]
Oded Goldreich, Silvio Micali, and Avi Wigderson. How to prove all NP-statements in zero- knowledge, and a methodology of cryptographic protocol design. In Andrew M. Odlyzko, editor,
CRYPTO’86, volume 263 of LNCS, pages 171–185. Springer, Heidelberg, August 1987.
18

[Gro16]
Jens Groth. On the size of pairing-based non-interactive arguments. In Marc Fischlin and Jean-
S´ebastien Coron, editors, EUROCRYPT 2016, Part II, volume 9666 of LNCS, pages 305–326.
Springer, Heidelberg, May 2016.
[HK20a]
David Heath and Vladimir Kolesnikov. A 2.1 KHz zero-knowledge processor with BubbleRAM.
In Jay Ligatti, Xinming Ou, Jonathan Katz, and Giovanni Vigna, editors, ACM CCS 2020, pages 2055–2074. ACM Press, November 2020.
[HK20b]
David Heath and Vladimir Kolesnikov. Stacked garbling for disjunctive zero-knowledge proofs.
In Anne Canteaut and Yuval Ishai, editors, EUROCRYPT 2020, Part III, volume 12107 of
LNCS, pages 569–598. Springer, Heidelberg, May 2020.
[HYDK21]
David Heath, Yibin Yang, David Devecsery, and Vladimir Kolesnikov.
Zero knowledge for everything and everyone: Fast ZK processor with cached ORAM for ANSI C programs. In 2021 IEEE Symposium on Security and Privacy, pages 1538–1556. IEEE Computer Society
Press, May 2021.
[IKOS07]
Yuval Ishai, Eyal Kushilevitz, Rafail Ostrovsky, and Amit Sahai. Zero-knowledge from secure multiparty computation. In David S. Johnson and Uriel Feige, editors, 39th ACM STOC, pages 21–30. ACM Press, June 2007.
[Ins06]
Texas Instruments. Msp430x1xx family user guide. https://www.ti.com/lit/ug/slau049f/ slau049f.pdf, 2006.
[JKO13]
Marek Jawurek, Florian Kerschbaum, and Claudio Orlandi.
Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently. In Ahmad-Reza Sadeghi, Virgil D.
Gligor, and Moti Yung, editors, ACM CCS 2013, pages 955–966. ACM Press, November 2013.
[KKW18]
Jonathan Katz, Vladimir Kolesnikov, and Xiao Wang. Improved non-interactive zero knowledge with applications to post-quantum signatures. In David Lie, Mohammad Mannan, Michael
Backes, and XiaoFeng Wang, editors, ACM CCS 2018, pages 525–537. ACM Press, October 2018.
[lib20]
libsnark: a c++ library for zksnark proofs, 2012-2020.
https://github.com/scipr-lab/ libsnark.
[MGC+16a] B. Mood, D. Gupta, H. Carter, K. Butler, and P. Traynor. Frigate: A validated, extensible, and efficient compiler and interpreter for secure computation. In 2016 IEEE European Symposium on Security and Privacy (EuroS P), pages 112–127, 2016.
[MGC+16b] Benjamin Mood, Debayan Gupta, Henry Carter, Kevin Butler, and Patrick Traynor. Frigate:
A validated, extensible, and efficient compiler and interpreter for secure computation. In 2016
IEEE European Symposium on Security and Privacy (EuroS&P), pages 112–127. IEEE, 2016.
[MGGR13]
Ian Miers, Christina Garman, Matthew Green, and Aviel D. Rubin. Zerocoin: Anonymous distributed E-cash from Bitcoin. In 2013 IEEE Symposium on Security and Privacy, pages 397–411. IEEE Computer Society Press, May 2013.
[mic13a]
Microcorruption: Embedded security ctf, 2013. https://microcorruption.com.
[Mic13b]
Microcorruption.
Lockitall lockit pro user guide. https://microcorruption.com/public/ manual.pdf, 2013.
[Mil19]
Matt Miller. Trends, challenges, and strategic shifts in the software vulnerability mitigation landscape.
https://github.com/Microsoft/MSRC-Security-Research/blob/master/ presentations/2019_02_BlueHatIL/2019_01\%20-\%20BlueHatIL\%20-\%20Trends\
%2C\%20challenge\%2C\%20and\%20shifts\%20in\%20software\%20vulnerability\
%20mitigation.pdf, Feb 2019.
19

[MNPS04]
Dahlia Malkhi, Noam Nisan, Benny Pinkas, and Yaron Sella.
Fairplay - secure two-party computation system. In Matt Blaze, editor, USENIX Security 2004, pages 287–302. USENIX
Association, August 2004.
[Nef01]
C. Andrew Neff. A verifiable secret shuffle and its application to e-voting. In Michael K. Reiter and Pierangela Samarati, editors, ACM CCS 2001, pages 116–125. ACM Press, November 2001.
[Odu20]
Emmanuel Odunlade.
Top 10 popular microcontrollers among makers.
https://www.
electronics-lab.com/top-10-popular-microcontrollers-among-makers/, Jun 2020.
[Pas10]
Rafael Pass and abhi shelat.
A Course In Cryptography.
https://www.cs.cornell.edu/ courses/cs4830/2010fa/lecnotes.pdf, January 2010.
[PHGR13]
Bryan Parno, Jon Howell, Craig Gentry, and Mariana Raykova. Pinocchio: Nearly practical verifiable computation. In 2013 IEEE Symposium on Security and Privacy, pages 238–252.
IEEE Computer Society Press, May 2013.
[Pic21]
Ryan Pickren.
Hacking the apple webcam (again).
https://www.ryanpickren.com/ safari-uxss, 2021.
[rev22]
Reverie: An efficient and generalized implementation of the ikos-style kkw proof system, 2022.
https://github.com/trailofbits/reverie.
[RW19]
Dragos Rotaru and Tim Wood. MArBled circuits: Mixing arithmetic and Boolean circuits with active security. In Feng Hao, Sushmita Ruj, and Sourav Sen Gupta, editors, INDOCRYPT 2019, volume 11898 of LNCS, pages 227–249. Springer, Heidelberg, December 2019.
[se19]
swisspost evoting.
E-voting system 2019.
https://gitlab.com/swisspost-evoting/ e-voting-system-2019, 2019.
[Sma19]
Yannis Smaragdakis. Sound analysis: Can we tell the truth about programs? https://blog.
sigplan.org/2019/09/18/sound-analysis-can-we-tell-the-truth-about-programs/,
Sep 2019.
[WMK16]
Xiao Wang, Alex J. Malozemoff, and Jonathan Katz. Emp-toolkit: Efficient multiparty com- putation toolkit. Available At https://github.com/emp-toolkit, 2016.
[Wol]
Clifford Wolf. Yosys open synthesis suite. http://www.clifford.at/yosys/.
[WTs+18]
Riad S. Wahby, Ioanna Tzialla, abhi shelat, Justin Thaler, and Michael Walfish. Doubly-efficient zkSNARKs without trusted setup. In 2018 IEEE Symposium on Security and Privacy, pages 926–943. IEEE Computer Society Press, May 2018.
[WYKW20] Chenkai Weng, Kang Yang, Jonathan Katz, and Xiao Wang. Wolverine: Fast, scalable, and communication-efficient zero-knowledge proofs for boolean and arithmetic circuits. Cryptology ePrint Archive, Report 2020/925, 2020. https://eprint.iacr.org/2020/925.
[XZZ+19]
Tiancheng Xie, Jiaheng Zhang, Yupeng Zhang, Charalampos Papamanthou, and Dawn Song.
Libra:
Succinct zero-knowledge proofs with optimal prover computation.
In Alexandra
Boldyreva and Daniele Micciancio, editors, CRYPTO 2019, Part III, volume 11694 of LNCS, pages 733–764. Springer, Heidelberg, August 2019.
[YSWW21] Kang Yang, Pratik Sarkar, Chenkai Weng, and Xiao Wang. QuickSilver: Efficient and affordable zero-knowledge proofs for circuits and polynomials over any field. In Giovanni Vigna and Elaine
Shi, editors, ACM CCS 2021, pages 2986–3001. ACM Press, November 2021.
[Zav20]
Greg Zaverucha. The picnic signature algorithm. Technical report, 2020. https://github.
com/microsoft/Picnic/raw/master/spec/spec-v3.0.pdf.
20

[ZGK+18]
Yupeng Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, and Charalampos
Papamanthou.
vRAM: Faster verifiable RAM with program-independent preprocessing.
In 2018 IEEE Symposium on Security and Privacy, pages 908–925. IEEE Computer Society Press,
May 2018.
A
KKW18 MPC-in-the-head
Ishai et al. [IKOS07] demonstrated that it is possible to construct ZKPs from secure multiparty compu- tation (MPC). Their technique, commonly called MPC-in-the-head or IKOS, has since inspired several concretely efficient concrete protocols, including ZKBoo [GMO16], ZKB++ [CDG+17], KKW18 [KKW18], and Ligero [AHIV17,BFH+20].
In IKOS, the prover first secret shares the witness among n virtual parties, and then emulates the MPC execution for the computation of the NP predicate on the (secret shared) witness among the virtual parties.
The prover then commits to each emulated party’s view, and the verifier then selects n′ ⊂n views to check for consistency, where n′ is smaller than the MPC’s privacy threshold. When the MPC is semi-honest the knowledge error is n′/n, and parallel repetition can be used to amplify soundness. IKOS is both flexible and can be made non-interactive using the Fiat-Shamir heuristic.
The KKW [KKW18] proof system is an instantiation of the IKOS framework, using a semi-honest, dishonest-majority (n′ = n −1) MPC protocol in the broadcast setting using additive sharings over any commutative ring. In this MPC protocol, the (emulated) players compute an arithmetic circuit in a gate-by- gate manner: for each wire α, the players P1, . . . , Pn maintain additive shares [mα](1), ..., [mα](n) of a ‘mask’ mα = P i[mα](i). The value zα assigned to the α wire is masked as ˆzα = zα −mα and the ‘correction’ zα is known to all players. Linear operations are executed locally by the players, while multiplication of wire values is handled using standard Beaver multiplication.
Because the prover’s evaluation of the circuit is privacy-free, the MPC protocol generates the Beaver triples in a privacy-free way using a central coordinator. We denote this special player that generates the preprocessing as P0.
This coordinator only distributes preprocessing to the other players and does not participate in the online evaluation.
To ensure honest behavior by the coordinator KKW relies on cut-and-choose: the prover runs the MPC protocol many times, and in a subset of the executions the verifier opens and checks the view of P0 (i.e.
checks that the preprocessing has been done honestly), in the remaining executions the verifier opens an n −1 size subset of the players P1, . . . , Pn and checks these views for consistency.
B
Proofs
B.1
Proof of Theorem 1
Perfect completeness follows from the completeness of the KKW protocol as well as from the correctness of the circuit, which can be easily verified by inspection. Therefore, we will focus on proving honest-verifier zero-knowledge and soundness.
To prove that this protocol achieves perfect zero-knowledge, we can take the simulator SKKW that was used in KKW. The only change we have to make is that the simulator also chooses the challenge x ∈Zq uniformly at random. The same hybrid argument can be used as in the original proof. Given that the original simulator was indistinguishable from a real execution, we can conclude that this simulator is also indistinguishable from a real execution.
Similarly, to prove witness extraction, we can use the witness extractor from KKW. Note that after a full run of the protocol we have all messages as if we ran a normal KKW protocol for the circuit Cshuffle, with a public input x, i.e. we don’t have to extract x because it is part of the transcript. Hence, we can use the witness extractor as described in KKW to extract A and B, such that π(A) = B, for some permutation
π(·).
21

The soundness error induced by the shuffle proof is
ℓ q−1, which follow directly from the Schwartz-Zippel lemma. To see this, note that the x is selected at random and the number of points that are shared by the two polynomials is bounded by their degree ℓ.
The soundness of the MPC-in-the-head protocol is max
 1 m, 1 n

, as we are only considering the non-amplified version of KKW. To violate soundness, the prover must either succeed in the cheating during the preprocessing or the online phase. During the preprocessing, the probability is 1 m. During the online phase, either the prover must cheat or produce an invalid shuffle proof.
The probability of this happening is 1 n +
ℓ q−1 −
ℓ q−1 1 n. Therefore, the overall soundness error is max n 1 m, 1 n +
ℓ q−1 −
ℓ q−1 1 n o
.
B.2
Proof of Theorem 2
Completeness follows immediately from the completeness of the KKW protocol as well as the basic arithmetic used for transforming output from the boolean circuit to input to the arithmetic circuit.
To show perfect zero-knowledge we build the following simulator:
• Use the simulator SKKW on Cbool,
• Actually do the transformation as it is done in the real protocol.
• Use the simulator SKKW on Carith,
Because SKKW generates a proof transcript that is indistinguishable form a real proof, and the second step is done exactly like it is done in the real protocol, we can conclude that this new simulator also produces a proof transcript that is indistinguishable from a real execution.
Witness extraction can be shown by first extracting the witness of the second circuit, and then using that witness for extracting the witness of the first circuit, which is also the witness for the complete circuit.
Soundness error is the maximum between both circuits of the soundness error as computed in KKW. To achieve better soundness, we can choose the number of executions according to the circuit with the worst soundness error.
C
Knowledge Error of Permutation Proof
When amplifying the soundness by parallel repetitions, the soundness error of the permutation proof is dominated by the soundness error of KKW. We computed the soundness error for several different parameters, i.e. changing the size of the arithmetic group, the number of players, and the number of repetitions, these results are shown in Table 4 and Figure 3. Hence, we can optimize for speed and proof size while targeting an error of ϵ ≤2−128. Similar to computing the number of repetitions required for the KKW protocol, we can compute the number of parallel repetitions required to amplify the soundness of the permutation proof.
The probability of a cheating prover passing the preprocessing phase is:
max m−τ≤k≤m
( k m −τ

·
 m m −τ
−1)
Which is exactly as shown in KKW [KKW18]. Conditioned on the cheating prover passing the preprocessing phase, the probability of passing the online phase is:
max m−τ≤k≤m
( 1 n +
ℓ q −1 −
ℓ q −1 1 n
m−τ−k)
With ℓthe number of elements in the lists, and q the order of the field in which the elements are contained.
The term 1 n is the soundness error for the KKW online phase, we add the soundness error of the permutation 22

ρ = 128 n 4 8 16 32 64 128 m 218 293 352 606 842 1291
τ 65 43 33 26 22 19
Table 4: Sample values for the number of preprocessing repetitions m, players n, and online repetitions τ, similar to the values in KKW [KKW18].
Figure 3: Soundness error with permutation proof for 64 players, list of size ℓ= 216, number of preprocessing runs m = 842, and online runs τ = 22.
proof as the term
ℓ q−1, lastly, we subtract the term
ℓ q−1 1 n, which is the probability of both soundness errors occurring. Thus, we minimize the number of online repetitions τ such that
ϵ(m, n, τ)
def
= max m−τ≤k≤m





 k m−τ

  m m−τ

·

(q−1)n q−1+nℓ−ℓ
m−τ−k




 is ≤2−128 for different values of n. For a list size ℓ= 216 and a field size q = 264, the soundness error that we have added by introducing the permutation proof gets fully reduced in the same number of rounds that are needed to amplify the soundness error introduced by KKW. Hence, no extra repetitions are needed for adding the unknown permutation proof inside a KKW protocol. Sample satisfying values can be found in Table 4.
Using a Ring Instead of a Field. It is much easier to efficiently implement our scheme over a ring of size q = 2t, for some t ∈N. However, the original Schwartz-Zippel lemma only works for polynomials over a field. As a general optimization, we work over the ring Z2n, where we choose n to be 64. Fortunately, a more general form of the Schwartz-Zippel lemma, introduced by Arvind et al. [AMS08], can be applied in this setting. They show that the Schwartz-Zippel lemma still holds when the random assignment to the polynomial is chosen within a finite subset of an integral domain contained within the ring. Within Z2n all odd numbers form such integral domain.
To make sure that our permutation proof still holds, the verifier needs to pick the challenge to be an odd number. The impact on the soundness is that instead of using the size of the overall ring, we have to use the size of the integral domain. This hardly impacts the soundness as long as the ring size is still large enough, which is the case for Z264.
In Figure 3 we show the impact of the arithmetic ring size on the soundness error, given a list size of
ℓ= 216 and number of players n = 64. We choose the number of preprocessing repetitions m = 842 and 23

online repetitions τ = 22. Based on this figure we can conclude that the most optimal ring size is 236, but for ease of implementation we’ve implemented a ring of size 264.
24