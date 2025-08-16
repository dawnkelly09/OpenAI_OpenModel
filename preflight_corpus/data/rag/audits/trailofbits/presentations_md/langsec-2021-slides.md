# Diﬀerential analysis of x86-64 decoders

William Woodruﬀ, Niki Carroll, Sebastiaan Peters

Contact Information
William Woodruﬀ
Trail of Bits william@trailofbits.com
@8x5clPW2
Niki Carroll
George Mason University ncarrol5@gmu.edu
@inventednight
Sebastiaan Peters
Eindhoven University of
Technology s.peters2@student.tue.nl 3 3

Items
●
Overview of instruction decoding
○
Why is x86-64 especially challenging?
●
Instruction decoding as an attack surface
●
Diﬀerential analysis of instruction decoders
●
Mishegos: a diﬀerential fuzzer for x86-64 decoders
●
Results and future work

Instruction decoding
●
Individual machine code instructions → assembler mnemonics
●
The fundamental building block for correct disassembly
○
Function, control/data ﬂow, call graph recovery all depend on correct decoding
○
Small mistakes → incorrect control/data ﬂow, misaligned decodings, …
●
Decoding depends on ISA/vendor-speciﬁc parameters:
○
Fixed length or variable length encoding?
○
Revisions to the ISA? Backwards compatible, incompatible?
○
Open, machine-readable speciﬁcation?
○
Hidden opcodes/unintended functionality?
○
Vendor-speciﬁc behavior?
○
Completeness vs. decoding what the common compilers emit?

Instruction decoding: not just for REs anymore!
●
Previously: primarily reverse engineers and debuggers
○
Decoder errors here are annoying, but there’s a human in the loop
○
Human ﬁxes/stubs the error and continues
●
Now: on the hotpath of user code:
○
Interpreted languages: JITs, sandboxes
○
Antivirus tools: static disassembly and analysis
○
Static & dynamic binary translation (Apple’s Rosetta)
○
Self-modifying code (runtime patching in the Linux kernel)
○
Constrained runtimes/VMs (WASM, eBPF)
○
No human in the loop to catch errors!

Can we exploit instruction decoding errors?
●
Errors in instruction decoding have security consequences
○
Sandboxes, VMs, JITs: run mis-generated code, escape the environment
■ eBPF: violate runtime guards
○
Antivirus: confuse AV checks into skipping/not ﬂagging malicious code
■
...or trip up code/data disambiguation
○
SBTs/DBTs: convert a benign program into a misbehaving one
■
Turn benign code into vulnerable code
■
Introduce timing channels or information leaks?
●
Speculation: x86-64’s complexity makes it particularly susceptible to decoder implementation errors

x86-64 decoding is (particularly) hard
●
Numerous features that make x86-64 hard to decode correctly:
✅
Complex, variable-length instruction format (up to 15 bytes per instruction)
✅
>40 years of semi-compatible ISA revisions
❌
No formal speciﬁcation, two separate major vendors with references aimed at developers rather than decoder implementers
❌
A long history of undocumented opcodes, including backdoors!
😭
Intel: AAD/AAM variants, SALC, ICEBP, UD1
😢
AMD: 3DNow! variants (Domas 2017)
😿
VIA: ALTINST + C3 family backdoors (Domas 2017)
❌
Variations in vendor behavior (operand size preﬁx, SYSRET diﬀerences)
❌
Under- and undeﬁned semantics
😈
Multiple preﬁxes, EFLAGS state on BSF/BSR variants

Where are the bugs in x86-64 decoders?
●
Speculation 1: many bugs will exist where discrete regions of the instruction format meet
○
Unlikely to completely mess up displacement decoding, but might mess up displacement decoding with multiple legacy preﬁxes and an uncommon SIB encoding
●
Speculation 2: many bugs will also exist where x86-64 has undergone historical changes
○
Subtleties with the REX preﬁx, validity of instructions in long mode, …
●
Speculation 3: x86-64 instruction decoders are primarily tested against compilers
○
Decoder authors under-test against instructions/formats that compilers don’t use
●
Speculation 4: most bugs in x86-64 instruction decoders won’t cause memory unsafety in the decoder itself
○
Not a good target for traditional crash-driven fuzzing…

Diﬀerential analysis of instruction decoders
Instruction decoders are an ideal target for diﬀerential fuzzing:
●
Relatively little memory unsafety → simple harnesses
●
Lots of competing (and open source!) implementations
●
Simple interfaces (byte string → instruction)
●
Lots of signals to diﬀ against:
○
Decoding success/failure, failure kind
○
Decoded length
○
Decoded semantics (instruction ground, operand count, …)

Diﬀerential analysis of instruction decoders
Prior work:
●
Paleari et al. (2010): Compare N decoders against a hardware decoder as a source of ground truth
●
Jay & Miller (2018): Normalize each decoder’s assembly output and compare for discrepancies
Both approaches focus on false negatives; we also want to identify false positives!

Mutation strategies for x86-64
Prior work:
●
Paleari: Generate random input sequences, mix in with sequences from hardware-guided generation
●
Jay & Miller: Seed the mutator with valid inputs, perform bitﬂips and sample outputs based on inferred instruction structure
We want to do better than random generation without relying on hardware ground truth (Paleari) or structure inference from a potentially unreliable decoder (Jay & Miller)!

A “sliding” mutation strategy
Observation: the maximum x86-64 instruction length is 15 bytes
... but the maximum size of each instruction ﬁeld adds up to 26:
We can soundly overapproximate the structure of a potential x86-64 instruction by ﬁlling up to 26 bytes!
We can evaluate speculations 1 and 2 by being better-than-random about legacy preﬁxes, REX, ModR/M, SIB, etc.

A “sliding” mutation strategy
Mutation engine lifecycle
●
Generate a “maximal” overapproximated candidate
●
Extract individual 15-byte “sliding” candidates from the “maximal” candidate
●
Once the “maximal” is exhausted, generate a new one
●
Repeat until fuzzing is halted
Tests our speculations by feeding a wide range of preﬁx/structured interactions to the decoders!

Mishegos: our diﬀerential fuzzer for x86-64
●
Each “sliding” candidate is placed in an input slot, to be consumed by each decoder’s worker
●
Workers implement a simple ABI to wrap their underlying decoder
●
Each decoder’s worker puts its result for an input into an output slot; inputs are pruned once all workers have attempted it
●
Outputs are collected into “cohorts” of N for N decoders for a single input

Mishegos: analysis framework
●
Fuzzing with mishegos produces cohorts of outputs
○
Each output in a cohort contains the decoder state for the cohort’s input:
■
Status (success, failure, kind of failure)
■
# of bytes decoded
■
Disassembly of instruction, length of disassembly
●
Cohorts need to be analyzed for errors and discrepancies
○
Observation: analyses compose well, perform cheap + eﬀective ones ﬁrst
○
Remove cohorts that only contain errors, only contain successes, ...
○
Select cohorts where outputs disagree on status, length
○
Treat particular outputs as “high-quality” and use them as ground truth

Mishegos: the bird’s eye view

Mishegos: performance, results, evaluation
●
Fuzzer: 33M cohorts/hour → 228M decoder results/hour
●
Analyzer:
○ 68.4M decoder results/hour after deduplication
○ 130M net cohorts for a 4 hour campaign:
■ 15M status discrepancies (one or more decoders disagree on validity)
■ 3.4M size discrepancies (one or more decoders disagree on decoded length)
■ 59K cases of XED “overaccepting” instructions
●
Probably all others underaccepting e.g. multi-byte NOPs!
Decoders: XED, libopcodes, Zydis, Capstone, DynamoRIO, bddisasm, Iced
Evaluated on 8 physical cores of an Intel Xeon 6140, running 7 decoder workers + the mutation engine and collector process

Mishegos: analysis highlights
Discovered a variety of decoder bugs through discrepancies:
●
Capstone: Incorrect control ﬂow targets (call), incorrect length decoding esp. with legacy preﬁxes
●
XED: False positives and false negatives for ISA extensions
● bddisasm: False positives, particularly around decoding instructions that don’t work on AMD64 in long mode
● libopcodes (GNU bfd): Remarkably broken! Failed to decode a large number of valid instructions

Future research
Mishegos constitutes the ﬁrst step (discovery) in evaluating the security posture of instruction decoders
Important future work:
●
Evaluating the salience of discrepancies (control/data ﬂow, decoder confusion, misaligning the instruction stream)
●
Automatically emplacing discrepancies (generating
“schizophrenic” binaries)
●
Further reﬁnement of “sliding”; minimizing duplicate work

Resources
GitHub: https://github.com/trailofbits/mishegos
Blog post: Destroying x86-64 decoders with diﬀerential fuzzing
Selected citations:
Paleari et al. 2010: N-version disassembly
Jay & Miller 2018: FLEECE
Domas 2017: Breaking the x86 ISA