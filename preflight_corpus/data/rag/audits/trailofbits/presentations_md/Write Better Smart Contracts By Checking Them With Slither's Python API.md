# Write Better Smart Contracts

By Checking Them With Slither's
Python API
Troy Sargent

●
Security Engineer at Trail of Bits
○
Work on smart contracts and blockchains
○
Contributor to Slither
○
@0xalpharush / troy.sargent@trailofbits.com
●
Trail of Bits:
○
We help organizations build high assurance software
○
R&D focused: we use the latest program analysis techniques
■
Slither, Echidna, Tealer, Amarna, Circomspect ...
Background 2

●
What is Slither
●
How it works
●
How to use it
●
Conclusion
Plan 3

●
Static analysis framework for smart contracts
○
Vulnerability detection
○
Optimization detection
○
Assisted code review https://github.com/crytic/slither pip3 install -u slither-analyzer 5

Features 6
● 80+ detectors
●
Supports Solidity from 0.4 to 0.8
●
Supports compilation frameworks out of the box
○
Hardhat, brownie, foundry, …
●
Supports deployed contracts through Etherscan

How it works

8

Demo Contract 9
Alarm Clock:
●
Has an owner
●
Has privileged functions
●
Has refund mechanism
●
Has user input

API Usage

The Basics 13
Contract
Function
Node
Operation

Demo Contract (slithIR and CFG)
14
Operation
Node
Function

Demo Contract (data dependency)
17
Translation
Root cause: a sensitive operation uses user-controlled input

Can the user manipulate refunds?
18
Check that all Transfer operations are not tainted by user input:
Let’s run it!

Conclusion

●
Slither: a static analyzer for smart contracts
●
Developers can leverage its powerful API
○
Built-in analyses
○
Supports most solidity versions and frameworks
○
Actively maintained codebase
Conclusion 20

Conclusion
●
Try our tutorials and exercises in building-secure-contracts
●
Have questions or ideas? Reach out
○
@0xalpharush / troy.sargent@trailofbits.com
○
Slack: https://empireslacking.herokuapp.com
●
Find these slides:
https://github.com/trailofbits/publications#blockchain
21