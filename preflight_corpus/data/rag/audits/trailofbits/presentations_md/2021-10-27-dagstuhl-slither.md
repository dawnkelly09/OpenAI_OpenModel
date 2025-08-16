# Building a Practical Static Analyzer for Smart Contracts

Rigorous Methods for Smart Contracts

Who am I?
●
Josselin Feist
○ josselin@trailofbits.com, @Montyly
○ github.com/montyly/publications
●
Trail of Bits: trailofbits.com
○
We help organizations build safer software
○
R&D focused: we use the latest program analysis techniques
■
Slither, Echidna, Tealer, Manticore, ...
2

●
What is Slither
●
How it works
●
Industry & academic impacts
●
Conclusion
Plan 3

Slither

Slither
●
Static analysis framework for smart contract
○
Vulnerability detection
○
Optimization detection
○
Code understanding
○
Assisted code review https://github.com/crytic/slither pip3 install -u slither-analyzer 5

Features 6
● 70+ public detectors
●
Support Solidity from 0.4 to 0.8
●
Support the compilation frameworks out of the box
○
Hardhat, truﬄe, dapp, embark, …
●
Support deployed contracts through etherscan/bscan/...

Vulnerability Detection https://asciinema.org/a/eYrdWBvasHXelpDob4BsNi6Qg 7

contract Contract1{ uint myvar; function myfunc() public{}
} contract Contract2{ uint public myvar2; function myfunc2() public{} function privatefunc() private{}
} contract Contract3 is Contract1, Contract2{ function myfunc() public{} // override myfunc
}
Printers: Inheritance Graph 8

Inbuilt tools
● slither-check-erc
●
Check for ERC speciﬁcation conformance
● slither-check-upgradability
●
Help to review delegatecall proxy contract
● slither-prop
●
Automatic unit test and property generation
● slither-simil
●
ML based code similarity
●
Echidna’s integration
●
Helping fuzzing through static information 9

Custom scripts
●
Python API to help during a code review
○
Inspect contract information
○
Including data dependency/taint analysis
●
Ex: creating a whitelist of protected functions
○
Every function must have onlyOwner, or being whitelisted
○ https://github.com/trailofbits/publications/blob/master/reviews/Advanc edBlockchain.pdf 10

How it works

Slither 12

SlithIR
●
Codebase information from solc’s AST
○
Contracts, functions, CFG
●
SlithIR: Slither Intermediate Representation
○
Solidity → Human usage
○
SlithIR → Code analysis usage 13

SlithIR
●
Less than 40 instructions
●
Linear IR (no jump)
○
Based on Slither CFG
●
Flat IR
●
Code transformation/simpliﬁcation
○
Ex: removal of ternary operator 14

SlithIR Instructions
●
Binary/Unary
○
LVALUE = RVALUE + RVALUE
○
LVALUE = ! RVALUE
○
…
●
Index
○
REFERENCE -> LVALUE [ RVALUE ]
15

●
Member
○
REFERENCE -> LVALUE . RVALUE
●
New
○
LVALUE = NEW_ARRAY ARRAY_TYPE DEPTH
○
LVALUE = NEW_CONTRACT CONSTANT
○
LVALUE = NEW_STRUCTURE STRUCTURE note: no new_structure operator in Solidity
SlithIR Instructions 16

Expression: allowance[_from][msg.sender] -= _value
IRs:
REF_1 -> allowance[_from]
REF_2 -> REF_1[msg.sender]
REF_2 -= _value
SlithIR Instructions 17

SlithIR SSA
●
SSA (Static Single Assignment) form
○
A variable is assigned only one time
○
Needed for precise data dependency analysis
○
Usually, ϕ indicates multiple deﬁnitions of a variable 18 a_0 = 0 if(){ a_1 = b_0;
} a_2 = ϕ(a_0, a_1)
a_3 = a_2 + 1; a = 0 if(){ a = b;
} a = a + 1;

SlithIR SSA
●
SlithIR SSA features
○
Include:
■
State variables
■
Alias analysis on storage reference pointers
○
Inter-procedural
■
Track internal calls
○
Inter-transactional
■
Take in consideration the state-machine aspect of smart contracts 19

Data dependency uint my_state_A; uint my_state_B;

function direct_set(uint input) public { my_state_A = input;
} function indirect_set() public { my_state_B = my_state_A;
}
20

Data dependency uint my_state_A; uint my_state_B;

function direct_set(uint input) public { my_state_A = input;
} function indirect_set() public { my_state_B = my_state_A;
}
21
Dependencies:
● my_state_A depends on input
● my_state_B depends on my_state_A
○
But also input?

SSA Inter-Transactional Example uint my_state_A; uint my_state_B;

function direct_set(uint input) public { my_state_A = input;
} function indirect_set() public { my_state_B = my_state_A;
}
22

my_state_A_0; my_state_B_0; direct_set(uint input_0):
my_state_A_1 := input_0 indirect_set():
    my_state_A_2 := ϕ(my_state_A_0,

  my_state_A_1)
my_state_A_2 := my_state_A_2

SlithIR: Code Analysis
●
Data dependency
○
Pre-computed, free for analyses
○
Level: function/contract
●
Read/Write of variables
○
Level: node/function/contract
●
Protected functions
○
What functions need ownership?
23

Industry & academic impacts

Industry impact 25 github.com/crytic/slither/blob/master/trophies.md

Academic impact github.com/crytic/slither/blob/master/README.md#external-publications 26

Conclusion

●
Slither: a general static analyzer for smart contracts
●
Researchers can leverage its engineering work
○
Inbuilt analyses
○
Multiple solidity versions and frameworks support
○
Maintained codebase
Conclusion 28

Conclusion
●
Try our tutorials in building-secure-contracts
○
Got an research idea? Contact us for help
■
Slack: https://empireslacking.herokuapp.com (#ethereum)
■ josselin@trailofbits.com
●
Crytic prize: $10k for best open academic researches
○
Include Slither, Echidna, Tealer, Manticore, ...
29