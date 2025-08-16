# Buckle Up, Buttercup: Our

Experience Competing in the AI
Cyber Challenge 9 August 2025

Our Team
Michael D. Brown
Overall Team Lead
Lead Designer of Buttercup
Ian Smith
Vuln Discovery Lead
Co-Designer of Buttercup
Ronald Eytchison
AI-Based Seed Generation Lead

Our Team
Henrik Brodin
Orchestration Lead
(Finals)
Eric Kilmer
Orchestration Co-Lead
(Semi-Finals)
Francesco Bertolaccini
Orchestration Co-Lead
(Semi-Finals)

Our Team
Riccardo Schirrone
Patcher Lead
Evan Downing
Contextualization Lead
Boyan Milanov
System Developer

Our Team
Alessandro Gario
Challenge Creator
(Internal Red Team)
Brad Swain
Challenge Creator
(Internal Red Team)

Our Team
Will Tan
Systems Developer
(Semi-ﬁnals)
Alan Cao
Systems Developer
(Semi-ﬁnals)
Akshay Kumar
Challenge Creation
(Semi-ﬁnals)

A Brief Origin Story

AI Cyber Challenge (AIxCC)
AIxCC is a competition to design a novel automated AI system (CRS) that can find and patch bugs in real-world open-source software.
Spring ‘24
Summer ‘24

AIxCC Competition Structure
CRS Code
CRS Infrastructure
Internet
AIxCC API
LLMs
CP 1
CP …
CP 2
CP n
CP 3

CP 1
CP …
CP 2
CP n
CP 3
CRS Code
CRS Infrastructure
Internet
AIxCC API
(1) Vuln
(2) Points
AIxCC Competition Structure
LLMs

CRS Code
CRS Infrastructure
Internet
AIxCC API
(3) Patch
(4) Points
AIxCC Competition Structure
LLMs
CP 1
CP …
CP 2
CP n
CP 3

Buttercup’s Design

Our Approach
Guiding Principles
●
Conventional software analysis works really well for certain problems.
●
AI/ML-based analysis works really well for certain problems.
●
Often, one approach works well where the other does not.
Break the problem down, use the best technique to solve each sub-problem.
Don’t expect LLMs to do things they aren’t good at!

Problem Breakdown 1)
Discover / prove existence of vulnerabilities 2)
Contextualize vulnerabilities 3)
Create and Validate patches 4)
Orchestrate these tasks to:
a)
Effectively allocate resources b)
Maximize score

CRS Architecture (Concept Paper)
Buttercup

CRS Architecture
ID the
BIC
Buttercup

CRS Architecture (Competition)
Buttercup

Buttercup in the Semiﬁnals

Performance by CWE type

Buttercup 2.0

Lessons Learned from semi-finals:
●
Validated our overall approach
●
Need better testing / handling of Java challenges
●
CWE-type specific seed-generation may have helped
Rule changes for finals:
●
Massive scale and budget (time, compute, and AI) increases
●
Several exhibition rounds
●
More complex scoring (SARIFs, bundles, duplication penalties)
●
Custom AI/ML models allowed
How did Buttercup evolve for the ﬁnals?

Building Buttercup 2.0
Buttercup 2.0 is essentially a from-scratch rebuild.
Driven by need for:
● more technically complex analysis components
● ability to easily change scale / cost of deployment for various rounds
● high degree of reliability and robustness to errors
Still, our high-level Buttercup remained the same as the semi-finals

CRS Architecture (Competition)
Buttercup

Buttercup 2.0 Technical Details

Orchestration - Submission Processing
Filter
Vulnerability discovery produces many PoVs -
ﬁlter stack traces already seen
Group by stacktrace
Group PoVs with similar stack traces - examples
of the same underlying
vulnerability.
Group by patch
Group PoVs remediated by the same patch - same underlying vulnerability
Monitor
As new PoVs come in merge by fuzzy stack match and patches.
Rebuild bundles as needed.
PoV - Proof of Vulnerability

Vulnerability Discovery
●
Strategy: Combine fuzzing and LLM input generation
●
Use standard OSS-Fuzz fuzzers:
○
LibFuzzer for C/C++
○
Jazzer for Java
●
Fuzzer bots sample active harnesses to run short fuzz campaigns
●
Fuzzing corpus:
○
Merger bots merge a fuzzer bot’s local corpus to the shared corpus
○
LLM input generation also submits to the corpus

Vulnerability Discovery: LLM “seed-gen”
Design
●
Several tasks that use LLMs to create seeds and/or PoVs
●
All tasks use tools to collect context from the codebase before generating inputs
Goal 1: Support Fuzzing
Goal 2: Independently Find Bugs
●
Init task: Bootstrap fuzzer with initial seed inputs that exercise harness
●
Explore task: Increase coverage for a target function
●
Vuln discovery task: Identify and validate vulnerabilities in target to create PoVs
○
Most expensive task to thoroughly explore code and test hypotheses

Contextualization
●
Constructs program model using CodeQuery + Tree-sitter
●
Supports querying program properties (functions & types)
●
Called by LLMs from Seed
Generator and Patcher using
LangGraph’s Tool library

●
LLM-based multi-agent system
○
Software, Security, and Quality Engineer Agents working together
●
Programmatic agents hand-off
○
Data flow between agent is (mostly) deterministic
○
More control over the process
○
Error handling relies on LLMs to determine resolution steps
●
Implementation
○
Less than 6K LOC, Python
○
LangChain/LangGraph
○
Preferred model: OpenAI/GPT-4.1
Patcher

Patcher: ﬂow

Patcher: patch creation
Code Snippet
Identiﬁer: <identiﬁer>
File Path: <ﬁle-path>
Start/End Lines: <start>/<end>
Code:
<existing-code>
LLM
Code Snippet
Identiﬁer: <identiﬁer>
File Path: <ﬁle-path>
Old Code:
<existing-code>
New Code:
<modiﬁed-code>

Buttercup in the Finals

Buttercup was the best performing CRS in Round 1:
●
Found and patched a vulnerability in both challenges with 100% accuracy
●
Used only ~$1000 of available $30,000 budget
But we crashed hard in Round 2:
●
Issue with filename length in vulnerability discovery component
●
Caused a hard failure after only 3/18 challenges were processed
●
We later reproduced Round 2 and Buttercup was successful on all challenges
And bounced back in Round 3:
●
Buttercup found and/or patched vulnerabilities in 20/26 challenges!
How did Buttercup do in Exhibition Rounds?

Buttercup came in second place, winning $3 million!
●
Found 28 vulnerabilities, patched 19
●
Used only ~$40,000 of available budget
●
~90% Accuracy
●
Found at least one PoV no one else did
●
Found at least one non-synthetic vulnerability
Keys to success:
●
Accuracy
●
Scoring well across all tasks
How did Buttercup do in the scored round?

I want to try Buttercup!

You’re in Luck….
Buttercup is Open Source!
The exact code we submitted for the semi-finals and finals code is available on our company github organization!
●
Buttercup 1.0 https://github.com/trailofbits/asc-buttercup
●
Buttercup 2.0 https://github.com/trailofbits/afc-buttercup
Fair warning: Buttercup was designed to run on competition infrastructure and at massive scale, so this version of Buttercup isn’t terribly user friendly…

And we’ll do you one better!
A standalone variant of Buttercup is also available!
We’ve also created a version of Buttercup that runs on commodity (laptop) and typical server-grade hardware. You can check it out at:
●
Buttercup standalone https://github.com/trailofbits/buttercup
Enjoy!

Thanks for Coming!