# 1

Slither: a Vyper and Solidity static analyzer
By: Troy Sargent

2
Security Engineer at Trail of Bits:
●
Work on smart contracts, blockchain nodes, rollups, VMs
●
Core contributor to Slither
●
@0xalpharush on Twitter/Github
Trail of Bits:
●
Combine manual review with practical program analysis
●
Apply fuzzing and static analysis to Golang, Rust, Cairo, Solana, etc
Background

3
Slither
●
Static analysis framework for smart contracts
○
Vulnerability detection
○
Optimization detection
○
Assisted code review https://github.com/crytic/slither pip3 install -u slither-analyzer

4
Slither now supports Vyper!
●
Vyper is a pythonic smart contract language
●
Initial support for Vyper 0.3.7 (Aug. 2023)
○
Worked with Vyper Foundation to support 3 codebases
(Yearn, Curve, and Lido)
●
Very little changes required for the 90+ existing detectors
●
Bonus: Vyper can be fuzzed with Echidna/ Medusa

5
Agenda
●
Find bugs and explore Vyper codebases
● 2 tips to use Slither eﬀectively
Not in this talk:
●
Lowering Vyper to Slither’s intermediate representation

6
Finding Vulnerabilities and
Understanding Code
●
The best use of static analysis results is to identify concerns and see if relevant queries surface anything

7
Vulnerability Detectors (reentrancy)
What Slither offers

8
Understand code
What Slither offers

9
Understand code (continued)
●
Slither’s printers provide quick insights into functions and contracts with out-of-the-box analyses
●
For example, the “vars-and-auth” printer will show:
○
What state variables each function updates
○
Uses of msg.sender (e.g. is the sender the owner?)
What Slither offers

10
Code comprehension (continued)
How can we make this content digestible for large codebases?
Command line magic:
What Slither offers

11 2 Tips to Effectively Use
Slither
●
The best use of static analysis results is to identify concerns and see if relevant queries surface anything

12
Tip 1: Run speciﬁc detectors
The best use of static analysis results is to identify concerns and see if relevant queries surface anything
Effective use of Slither

13
Tip 2: Sarif
What is a productive way to triage static analysis results?
●
Use sarif (standard ﬁle format) with powerful editor integrations
○
IDE diagnostics (Microsoft sarif viewer VSCode extension)
○
Marking whether ﬁnding is valid
○
Note taking
○
Share triage results with collaborators
Usage:
Effective use of Slither

14
Tip 2: Sarif (continued)
The best medium to review static analysis results is in your editor with context
Effective use of Slither

15
Tip 3: Github Action
●
The best time to review a static analysis result is when the code is fresh in your mind (slither-action)
Effective use of Slither

16
Future Work
●
Fix and test any gaps in the initial language support
○
Vyper has a greater number of builtins (also more complex)
●
Add support for newer Vyper as the language evolves
○ 0.4 module system
●
Pursue upstream improvements in the semantic info contained within Vyper’s AST
○
Referenced declarations (could also beneﬁt language server implementations)
●
Write Vyper-speciﬁc detectors
○
Side eﬀects in lazily evaluated contract like (x in [f(), g()]).

17
Future Work
●
●
Improve support for Solidity and Vyper interoperability
○
Retrieve AST from frameworks like Ape (pending ﬁxes upstream)
○
At each callsite to an interface, instantiate candidates and gather information from their source code (cross-contract analysis)
●
Increase effectiveness for developers and researchers
○
Each potential vulnerability should suggest how to triage/ drive the decision
○
Documentation and tutorials on writing detectors

18
Reach out
●
Have questions or ideas?
○
@0xalpharush / troy.sargent@trailofbits.com
●
Find these slides:
https://github.com/trailofbits/publications#blockchain