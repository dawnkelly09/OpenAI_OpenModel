# Testing and Verifying Smart

Contracts: From Theory to Practice
Formal Methods for Computer Security 2021

Who Am I?
●
Josselin Feist, josselin@trailofbits.com, @montyly
●
Trail of Bits: trailofbits.com
●
We help organizations build safer software
●
R&D focused: we use the latest program analysis techniques
●
McSema https://github.com/lifting-bits/mcsema
●
Manticore https://github.com/trailofbits/manticore
●
Slither https://github.com/crytic/slither
●
Echidna https://github.com/crytic/echidna 2

Goals
●
What is a Blockchain?
●
What is a smart contract?
●
What program analyses are applied in industry?
●
Current challenges and research opportunities 3

Blockchain

Blockchain
●
Ledger: Growing list of records 5

Blockchain
●
Distributed ledger: All participants store all the data
●
Decentralized consensus: Everyone agrees on the data 6

Blockchain Application
●
Bitcoin[1] (2009): First digital currency using blockchain
○
Solved the double spend problem
●
Ethereum[2] (2015): Extended blockchain to run apps
○
Store & execute code
Bitcoin: distributed database =>  Ethereum: distributed VM 7

Decentralized Application 8
Bob ran foo(0); it returned 42

Decentralized Application 9
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42
Bob ran foo(0); it returned 42

Smart Contracts
●
Smart Contracts: Applications that run on a blockchain
○
Everyone executes and veriﬁes it
○
Decentralized: nobody can stop or secretly modify data
○
=>  Ensures strong properties on your application 10

Smart Contract Usages
●
Digital currency is one example of an application
○
ICOs, Crowdfunding system
○
Game (ex: Poker, lotteries, ...)
○
Supply chain
○
…

11

DeFi
●
Decentralized Finance (DeFi)
○
Adapt ﬁnancial primitives to a permissionless and trusted execution
○
Lending and trading protocols
○
Signiﬁcant composability 12
[3]

DeFi
●
A lot of money is invested into smart contracts
○
~$40-50B of value locked in major DeFi protocols [4]
○
Uniswap ~$36B in trading volume last month
■
~5%-10% of crypto trades in decentralized exchanges 13

Smart Contract Risks
●
Smart contracts are programs = they have bugs
●
Adversarial environment
○
Attacker can steal directly funds
○
Rely on cryptographic primitives to hide funds and launder money
●
~$200M stolen in 2020 through smart contract hacks  [5]
14

Ethereum Internals

EVM
●
Ethereum runs EVM bytecode
○
VM with <150 opcodes
○ 1 register (PC)
○
Stack-based
●
Calling a function = making a transaction
○
It has a cost: gas, paid in ethers
●
Bytecode cannot be updated (!)
16

Solidity
●
Smart contracts are typically written in Solidity
○
High-level language in “Javascript style”
○
Contracts organized as a set of methods
○
State = contract variables + balance (# ethers)
17

18
Solidity: Example pragma solidity 0.8.0; // Compiler version contract Bank{
    mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}

19
Solidity: Example pragma solidity 0.8.0; contract Bank{ mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}

20
Solidity: Example pragma solidity 0.8.0; contract Bank{
    mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}

21
Solidity: Example pragma solidity 0.8.0; contract Bank{
    mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}

22
Solidity: Example pragma solidity 0.8.0; contract Bank{
    mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}

23
Solidity: Example pragma solidity 0.8.0; contract Bank{
    mapping(address => uint) private balances; constructor(uint initial_supply) public { balances[msg.sender] = initial_supply;
    } function transfer(address to, uint val) public { balances[msg.sender] -= val; balances[to] += val;
    } function balanceOf(address user) public view returns (uint){ return balances[user];
    }
}
Constructor
Public function
Constant function
(gas-free)
State variable

Example Vulnerabilities

●
The DAO (2016)
●
Re-enter in the contract before the balance is set to zero
○
Repeat n times => withdraws n times the original deposit
●
~$70 millions stolen
Reentrancy 25 if( ! (msg.sender.call.value(userBalance[msg.sender])() ) ){ throw;
    } userBalance[msg.sender] = 0;

Improperly restricted functions
●
Parity Wallet (2017)
○
Widely used library for storing ethers
●
Key function was callable by anyone
○
Someone destructed the contract
○
Broke all third-party integrations
●
$300 million of frozen assets 26

Oracle manipulation
●
Harvest Finance: DeFi yield aggregator (2020)
○
Users deposit assets, and Harvest invest funds into various protocols
○
Bug: incorrect usage of a price Oracle
■
Generate fake price, such that deposit to share ratio is increased
■
Deposit with fake ratio to get more share than expected
■
Replace with original price
■
Withdraw the share and received more than initial deposit
●
~$30M stolen 27

Program analysis

Program Analysis
●
Smart contracts are small
○
<1,000 LoC
●
Gas cost lead to bounded execution
●
High value = require high conﬁdence 29

Program Analysis
●
Fully automated
○
Detect common patterns
○
Static analysis / symbolic execution
●
Semi-automated
○
Property-based approach
○
Fuzzing / symbolic execution / abstract interpretation / ...
●
A lot of tools - not all maintained 30

Fully automated

Fully automated
●
Static analysis
○
Slither [6]
■
~100 detectors (~70 public)
■
+40 trophies
○
Maru
■
Closed source - SaaS (Mythx.io)
■ 28 detectors 32

Fully automated - Slither
●
Common ﬂaws
○
Reentrancy, unprotected function, ...
●
Many language-level issues
○
Variable shadowing, missing return statements, ...
33

Fully automated
●
Symbolic execution
○
Oyente [7] (< 10 detectors)
●
Unmainted tools
○
Securify [8]
○
SmartCheck [9]
34

Fully automated - Example

Ernst & Young Nightfall
● github.com/EYBlockchain/nightfall/
● zk-SNARK-based platform to allow private asset transfer on Ethereum
●
Users deposit assets, and get a “withdrawal proof”, allowing to withdraw the assets with another account 36

Ernst & Young Nightfall
● transferFrom returns a boolean, indicating if the transfer was a success
●
Nightfall was not checking the returned value
●
Create a withdrawal proof without transferring the asset
●
Found by Slither [15]
37

Semi-automated

User-deﬁned property
●
User-deﬁned property
○
DSL or Solidity’s assert
●
Target business logic
○
State machine transition
○
Access controls
○
Arithmetic operations
○
External interactions 39

Semi-Automated
●
Fuzzers
○
Echidna [10]
○
ContractFuzzer [11]
○
Harvey (Closed source - SaaS (Mythx.io)
40

Semi-Automated
●
Formal method based approach
○
Manticore [12] - Symbolic execution
○
K [13] - Symbolic execution
○
Verisol - Solidity to Boogie
○
Mythx - Symbolic execution (Closed source - SaaS (Mythx.io)
○
Certora - Abstract interpretation (Closed source)
41

Semi-Automated
●
Fuzzing versus formally-based methods
○
From experience, fuzzing is more eﬀective to ﬁnds bugs
○
But formal methods lead to higher conﬁdence
●
Require expertise and deep understanding of the target 42

Semi-Automated 43

Semi-automated - Example

Balancer
● https://balancer.ﬁnance
●
Trading platform
○
Liquidity provider earn interests
■
Bookkeeping: the share of the pool’s liquidity, not of the assets sent
○
Complex arithmetics 45

●
“How many assets I should send to receive poolAmountOut liquidity share?”
Balancer 46

Balancer
●
Fixed-point arithmetic
● c = ((a * b) + BONE / 2 ) / BONE
●
If ((a * b) + BONE / 2 ) < BONE, returns 0 47

Balancer
●
You could receive pool’s share for free for pool with low liquidity
●
Found with Echidna & Manticore 48

Semi-automated - Limitations

Property limitations
●
Aave was “formally veriﬁed”
●
Bug was found [16], allowed for property break
●
Veriﬁcation did not consider the code in its whole architecture 50

Program analysis in practice

Industry usage
●
Fully automated tool  - Slither
○
All our audits
●
Semi-automated tools - Echidna/Manticore
○
~50% of the audits
○
Some clients write properties before our engagements 52

Industry Usage
●
Example: Yield Protocol
●
Diﬀerent levels of properties
●
End-to-end
●
Scenario-based
●
Single component property 53

Program analysis challenges

Challenges  - Engineering
●
Not all tools have the same maturity
●
Space evolving fast
●
Solidity/EVM updates
●
New application trends require new heuristics
●
No property writing standard
●
Solidity’s assert, but limited 55

Challenges - Research
●
Contract composability
●
Small code, but high interactions
●
Solidity/EVM speciﬁcity
●
Array indexes are the results of hash functions
●
Gas modeling
●
Application speciﬁc modeling
●
DeFi
●
Combining techniques 56

Conclusion

Conclusion 58
●
Blockchain: new technology
○
With challenges and research opportunities for program analysis
●
Tools are already helping developers and auditors
●
Crytic $10k Prize
○
Reward academic publications built on top of ToB tools (inc.
Slither/Echidna/Manticore)

References 1.
Bitcoin: A Peer-to-Peer Electronic Cash System - Satoshi Nakamoto 2.
https://ethereum.github.io/yellowpaper/paper.pdf - G.Wood 3.
SoK: Decentralized Finance (DeFi), Sam M. Werner and al. (preprint)
4.
Dex Volume, Dex to Cex Spot trade volume (%) - dex-non-custodial 5.
The 2021 Crypto Crime Report - Chainalysis 6.
Slither: A Static Analysis Framework For Smart Contracts, Josselin Feist and al - WETSEB '19 7.
Making Smart Contracts Smarter, Loi Luu and al - CCS16 8.
Securify: Practical Security Analysis of Smart Contracts, Petar Tsankov and al - CCS18 9.
SmartCheck: Static Analysis of Ethereum Smart Contracts, Sergei Tikhomirov and al  - WETSEB18 10.
Echidna: eﬀective, usable, and fast fuzzing for smart contracts, Gustavo Grieco, Will Song, Artur Cygan, Josselin Feist, Alex Groce - ISSTA '20 11.
ContractFuzzer: Fuzzing Smart Contracts for Vulnerability Detection, Bo Jiang - ASE18 12.
Manticore: A User-Friendly Symbolic Execution Framework for Binaries and Smart Contracts, Mark Mossberg and al - WETSEB18 59

References 13.
Kevm: A complete formal semantics of the ethereum virtual machine, Everett Hildenbrandt  and al - CSF18 14.
Formal Speciﬁcation and Veriﬁcation of Smart Contracts for Azure Blockchain, Yuepeng Wang and al 15.
Bug Hunting with Crytic 16.
Breaking Aave Upgradeability 60