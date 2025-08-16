# A Broad Comparative

Evaluation of Software
Debloating Tools
USENIX Security 2024
Michael D. Brown 15 August 2024

Why Evaluate Software Debloaters?
2
Software debloating is an emerging research area aiming to remove unnecessary code from programs to:
-
Improve performance
-
Improve security posture (less code, less attack surface)
However, evaluations of tools to date are limited in scope and use inconsistent sets of metrics.
This makes it hard for potential users to know what tools to use, what benefits to expect, and whether they are safe/effective.

Motivating Questions 3
We designed an evaluation for SotA debloating tools to answer:
1.   How can debloating tools be evaluated?
᠆
What metrics should be used?
᠆
What benchmarks should be used?
1. How well do these tools perform relative to each other?
1. What barriers to adoption exist for software debloaters?

Some Background

Survey of Debloating Techniques 5
There have been over 70 publications in the last 10 years for removing bloat in:
᠆
Software (Source, Binary, IR)
᠆
Containers
᠆
OSes and their APIs
᠆
Firmware
᠆
Test cases
᠆
Build dependencies
᠆
And more
We focus on software for x86[_64] architectures

How Do Debloaters Work, Generally?
6
Analysis
Transformation
Specification
Output
Validation
Input

Types of Bloat 7
Two categories of software bloat:
Type I: Universally unnecessary for all intended uses
᠆
E.g., Library code, API functions that are never called
Type II: Conditionally unnecessary depending on intended use
᠆
E.g., Features a particularly user doesn’t need, code for targeting multiple architectures

Types of Debloaters (Type I)
8
●
Dynamic version of SL debloaters
●
Uses reachability information at runtime to select, excise, or blank bloat library functions
●
Pros: Avoids library fragmentation
●
Cons: Very complex, significant overheads
Runtime
Static Library (SL)
●
Target unnecessary library functions
(dynamically loaded)
●
Analyze call graph to find unnecessary library functions, then remove or blank them
●
Pros: Low soundness risks, do not require specs
●
Cons: Fragments shared libraries on system

Types of Debloaters (Type II)
9
●
Binary version of S2S debloaters
●
Requires binary disassembly / decompilation / lifting
●
Pros: Can debloat legacy binaries
●
Cons: High risk of soundness issues, removing code is challenging (blanking is typical)
Binary to Binary (B2B)
Source to Source (S2S)
●
Target unnecessary program features user doesn’t need
●
Analysis maps features to code, then removes code associated with unwanted features
●
Pros: Targets richest program rep, compiler helps identify problems
●
Cons: Can require exhaustive test cases, requires source code

Types of Debloaters (Type I + II)
10
Compiler-Based Specializers (CBS)
●
Can target multiple types of bloat
●
User specifies one or more arguments as compile-time constants, use compiler to remove bloat as “dead code”
●
Pros: Low soundness risks, specs are easy to generate
●
Cons: Limited to aggressive debloating of CLI applications only

Debloater Metrics 11 30 different evaluation metrics found:
1. Performance: e.g., runtime, size, memory consumption 2.  Correctness / Robustness: e.g., failures and crashes 3.  Security Improvement: e.g., CVEs removal, code reusability

Evaluation

Tool Selection 13

Tool Selection 14

Metric Selection 15

Benchmark Selection 16

Evaluation Setup 17

Results

How well did tools perform?
19
●Only 15 tool / benchmark incompatible combinations
●
C++, Multithreading
●More complexity -> more resources
●Takes less than 20 mins and 4 GB memory to run
●
Notable exception: CHISEL S2S debloaters take hours / days to run
● some benchmark outliers

How well did debloated programs perform?
20

How well did debloated programs perform?
21
●Reductions in static binary size as expected
●
Come tools increase size due to design decisions
●CPU runtime and peak memory consumption not materially changed before / after debloating
●
As expected - the code being removed is unnecessary

How safe was debloating?
22

How did debloating affect security posture?
23
●Debloating has mixing effect that breaks portability of code reuse exploits
●Other code reusability metrics were not materially impacted by debloating

Key Findings

Key Takeaways 1. Software debloaters currently have low maturity
᠆
Slim 42.5% overall success rate passing functionality tests
᠆
Drops to 22% when excluding low-complexity benchmarks 2.  Software debloaters have soundness issues
᠆
Only 26 of 200 attempts produced a sound debloated program
᠆ 20 of those were attempts to remove Type I bloat 3. Software debloaters have marginal benefits
᠆
Only binary size and gadget locality are routinely improved 25

Contact 26
Michael D. Brown
Principal Security Engineer michael.brown@trailofbits.com