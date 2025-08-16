# Static and Dynamic

Analysis
Tool Shootout

Interesting and Novel Binary Occultism Tradeshow 2016

2
Introduc+on to Cyber Grand Challenge
The challenge sets
Por+ng status
Some analysis results
Agenda

Cyber Grand Challenge

DARPA created a “Grand Challenge” to improve automated soBware analysis.
By puFng on a machine-on-machine CTF.
They spent millions crea+ng the infrastructure:
•  A custom OS ABI – DECREE
•  Hundreds of challenge sets
•  Tes+ng Infrastructure
Cyber Grand Challenge 5

6
A binfmt Linux ABI meant to reduce complexity.
Implements only 7 syscalls:
•  exit, send, recv, mmap, munmap, select, getrandom
•  These syscalls are neutered
No modern security mi+ga+ons (e.g. ASLR, NX Stack)
DARPA distributed Linux VMs that supported both ELF and DECREE
DECREE

7 247 C & C++ network services
•  Implemen+ng things like mail servers, like Bp servers, etc
•  Except all have custom protocols, no real RFCs allowed
All have 1 or more exploitable or crashing vulnerability.
You’re expected to develop a “Proof of Vulnerability”
Challenge Sets

8
Each challenge has:
•  A detailed readme
• 
Vulnerability Descrip+on
• 
Vulnerability CWE
• 
A “Challenges” sec+on
•  Polls (aka input generators) with high code coverage
•  One or more Proof of Vulnerability triggers
•  Included patches, guarded by compile-+me #ifdefs
Challenge Sets (Continued)

9
Descrip(on: In our society, family structures have changed such that tradi+onal Family Tree soBware cannot properly model all current family structures. In response to this diverse environment, Family Rela+ons Inc.
brings to you our latest app, Modern Family Tree. It is the premier family tree building soBware for today's society.

Two vulnerabili(es: 2x Heap Buﬀer overﬂows due to indexing 1 item too far

CWE-122 Heap-based Buﬀer Overﬂow
CWE-129 Improper Valida+on of Array Index
CWE-193 Oﬀ-by-one Error
CWE-788 Access of Memory Loca+on ABer End of Buﬀer

Example: Modern Family Tree 2527 lines of C 946 lines of Python (poll generator)

10
DECREE isn’t all that useful
These challenges are a great test set so we decided to port them to
Linux and OS X!
Por+ng Status:
• 
Rewrote the build system to be Cmake.
• 
Wrote C shim layers between decree ABI and posix
• 
Everything is dynamically linked now
• 
All build, almost all pass their polls
• 
Need to normalize it a bit more
Porting Status

The Shootout 11

Originally wanted to compare sta+c analysis tools such as angr, pysymemu, klee, kite, cloud9.
And tools like clang-sta+c-analyzer, coverity scan, pvs studio, etc.
…but I ran out of +me
Setup

13
I took 23 binaries, 12 c3.xlarge ec2 instances, and 3 conﬁgura+ons of
AFL.
•  AFL with a single 4 byte input “eeee”
•  AFL with 5 inputs ripped from the “transmit” side of the polls
•  AFL + LAF* with 5 inputs

Each ran un+l the ﬁrst crash or 10 hours. This turned out to be a mistake.
AFL vs. AFL vs. AFL (w/LAF)

14
Trail of Bits  |  Sta+c and Dynamic Analysis Tool Shootout  |  09.29.2016  |
trailorits.com
Number of Execu+ons

15
Trail of Bits  |  Sta+c and Dynamic Analysis Tool Shootout  |  09.29.2016  |
trailorits.com
Number of Paths

16
Trail of Bits  |  Sta+c and Dynamic Analysis Tool Shootout  |  09.29.2016  |
trailorits.com
Number of Crashes

Questions?
•  Sorry about the lack of data. Expect a follow up blog post @ htps://blog.trailorits.com

•  Challenge repository here:
htps://github.com/trailorits/cb-mul+os
•  Ques+ons?
ryan@trailorits.com
@withzombies
Principal Security Researcher
Ryan Stortz