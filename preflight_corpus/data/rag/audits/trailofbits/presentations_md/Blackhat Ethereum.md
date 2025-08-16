# Blackhat Ethereum

CanSecWest 2018

1.
Introduction to Ethereum 2.
Extract useful information from the blockchain 3.
Audit contracts for vulnerabilities 4.
Write and throw an exploit
Agenda 2

• Ryan Stortz (@withzombies)
• In the industry for ~10 years
• Previously at Raytheon SI
• Used to play CTF: VedaGodz, HatesIrony, Marauders, Hacking4Danbi
• Used to host CTF: GhostInTheShellcode, CSAW CTF
• Past Presentations on Swift Reversing, Cyber Grand Challenge, Binary Ninja
• Jay Little (@computerality)
• In the industry for ~10 years
• Favorite keys to press in IDA: Y and D
• Used to play CTF: 0x28 Thieves, Whitehatters, VedaGodz, HatesIrony, Marauders,
Samurai
• Used to host CTF: GhostInTheShellcode
Who we are 3

4
Ethereum
•
Ethereum is an “alternate” blockchain implementation
•
Ethereum is smart contract oriented
•
Ethereum is the 2nd largest cryptocurrency by valuation

5
•
Bitcoin pioneered trustless money transfer
•
Ethereum is takes it further
•
Adds turning-complete machine for smart contracts
•
Supports rich applications
•
Enables tracking of assets: stocks, mortgages, domains names
•
The public only really hears about ICOs
•
“Initial Coin Offerings”
Smart Contracts and Transactions

Title
Title
Title
Title
Title
Title
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text 6
Ethereum Blockchain Terminology
Term
Non-Crypto Analogy
Ether / ETH
The base currency
Wei / Gwei 10-18 and 10-9 ETH
Gas
The amount on a postage stamp
Block
A list of transactions
Transaction
Sends ETH (and optionally a message) between addresses
Address 160-bit number, can be an account or contract
Banking routing number + account number
Account
A bank account, holds ETH, can send/receive
Contract
Account that autoruns code when it receives a message
DApp
Contract with a web UI in front of it

7
•
Ethereum is described by the Yellow Paper
•
Many unique implementations!
•
Do use: geth and parity
•
Don’t use: cpp-ethereum, pyethereum, EthereumJ
•
Clients are responsible for keeping the consensus
•
This includes the state of all smart contract transactions
Implementations

8
•
JavaScript-inspired high-level language for smart contracts
•
Compiles to EVM, a native machine code for Ethereum
•
Is the source of nearly all of Ethereum’s issues
Solidity

9
•
Stack machine
•
~181 opcodes
•
Native data width is 256 bits / 32 bytes
•
Many instructions are duplicates
•
PUSH1 – PUSH32
•
DUP1 – DUP16
•
SWAP1 – SWAP16
•
Instructions have a gas cost
• https://github.com/trailofbits/evm-opcodes
Ethereum Virtual Machine (EVM)

10
Stack Machine
Code
Stack
PUSH1 0x2 0x2
PUSH1 0x3
ADD
PUSH1 0x8
MUL
Code
Stack
PUSH1 0x2 0x2
PUSH1 0x3 0x3
ADD
PUSH1 0x8
MUL
Code
Stack
PUSH1 0x2 0x5
PUSH1 0x3
ADD
PUSH1 0x8
MUL
Code
Stack
PUSH1 0x2 0x5
PUSH1 0x3 0x8
ADD
PUSH1 0x8
MUL
Code
Stack
PUSH1 0x2 0x28
PUSH1 0x3
ADD
PUSH1 0x8
MUL

11
Hack = contract sends you more ETH than you send it
Typically logic flaws
But memory corruptions do happen!
What do hacks look like?
https://github.com/iveth/WHGBalanceVerification

12
Do we get to reverse engineer?
1,500,000 26,300 5,643 1,536 470
Contracts
With ETH
Unique Code
With Source
With >1 ETH

The Heist 13

Title
Title
Title
Title
Title
Title
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text 14
The Tools
Tool
What it does geth / parity
Ethereum clients / JSON RPC providers web3.js / web3.py
JSON / websocket clients for the clients
Etherscan.io
The most useful website
Remix / Oyente
Solidity source editor and static analyzer
Mythril
EVM, Solidity, Blockchain search
Manticore
EVM and Blockchain symbolic executor
Ethersplay
Disassembler

15
Ethereum clients typically serve JSON RPC
Options:
1. Connect to infura.io or myetherapi.com 2. Manually browse Etherscan.io 3. Run your own geth or parity client
How to get contracts

16 geth.exe --syncmode "fast" --cache 4096
My first experience can be summarized as follows:
ERROR[11-29|19:16:30] Failed to close database
database=/eth/.ethereum/geth/chaindata err="leveldb/table: corruption on data- block (pos=916560): checksum mismatch, want=0x0 got=0x2dd0aec0 [file=095339.ldb]“
ERROR[11-29|19:18:02] Section commit failed                    type=bloombits error="leveldb/table: corruption on data-block (pos=916560): checksum mismatch, want=0x0 got=0x2dd0aec0 [file=095339.ldb]“
ERROR[11-29|19:18:02] Section processing failed                type=bloombits error="leveldb/table: corruption on data-block (pos=916560): checksum mismatch, want=0x0 got=0x2dd0aec0 [file=095339.ldb]” geth

17 geth, part 2

18
./parity -d /mnt/fastssd/chain --cache-size=4096
Use v1.9.4
Parity

19
•
Have patience
•
The only troubleshooting step is rm –rf and resync
•
Use Linux
•
Use a fast SSD
•
Ethereum clients and web browsing don’t mix
•
Make a directory structure for all of your contracts
Ethereum client pro tips summary

Several days later… 20

21
You get a key value store, no structure
Ethereum is focused on recent transaction and current state, not history
Distributed ledger != distributed database

22
BLOCK
Block
Transaction
From/To
Receipt
Contract Address
From/To
Transaction
Gas
Input
Creation Code

23
•
Official interface to Ethereum clients
• v0.20 is a pain and v1.0 is better but also not done
•
Introducing Promises on all APIs but they didn’t work consistently
•
Gave up and used Python
•
Now you can finally run our “5” lines of Python:
for b in range(blockNumber('latest’)):
block = getBlockByNumber(b)
for tx in block['transactions']:
r = getTransactionReceipt(tx['hash'])
the_code = getCode(r['address'])
web3.js / web3.py

24
•
Now we have all ~1.5 million contracts in a folder!
•
Except for selfdestruct-ed contracts
•
Except for contract creation code, stored in tx[‘input’]
•
Had to re-run the script, took another 4 days
•
Chain directory grew 5x in size
Five days later… sync’d!

The Target 25

•
We chose contract:
0xcd6d2cd79fd754c6b909585e46541d32ec491962
•
We were able to extract the bytecode using web3
•
No source code was available
Analyzing the contract 26

•
EVM is a Harvard architecture!
•
There are ~5 address spaces
•
Code, Stack, Call data, Storage, Memory
•
All execution enters at PC 0x0 and functions are dispatched based on call data
•
Functions are dispatched based on sha3(prototype).digest()[:4].encode[‘hex’]
• e.g., SetOwner(address) = 0x167d3e9c
•
Call data is 32-byte aligned (after the initial 4 bytes)
EVM ABI 27

28

29

Identifying the vulnerability 30

31
Writing the exploit

32
Throwing the exploit

Do your own heist 33

34
• Integer overflow/underflow
• Incomplete initialization
• Uninitialized variables
• Callbacks / re-entrancy
• Variable name shadowing
• Type inference (var keyword)
• Array.length
• Inline Assembly
• Divide by zero
• Race conditions / replay attacks
• Bad random number generation
• Time sensitive
• Using blockchain as random
Knowledge

Etherscan.io 35

36
• https://github.com/ethereum/remix-ide
• https://github.com/melonproject/oyente
Remix / Oyente

• https://github.com/ConsenSys/mythril
Mythril 37

• https://github.com/MAIAN-tool/MAIAN
MAIAN 38

• https://github.com/trailofbits/manticore
Manticore
$ manticore simple.sol
[25981] m.main:INFO: Beginning analysis
[25981] m.ethereum:INFO: Starting symbolic transaction: 1
[25981] m.ethereum:INFO: Generated testcase No. 0 - REVERT
[25981] m.ethereum:INFO: Generated testcase No. 1 - REVERT
[25981] m.ethereum:INFO: Finished symbolic transaction: 1 | Code Coverage: 100% |
Terminated States: 3 | Alive States: 1
[32058] m.ethereum:INFO: Generated testcase No. 2 - STOP
[25981] m.ethereum:INFO: Results in /examples/mcore_zua0Yl 39

40
• https://github.com/trailofbits/ethersplay
Ethersplay

41
• https://github.com/trailofbits/ida-evm
IDA-EVM

42
•
Our own EVM binary analysis framework
•
Recovers EVM CFG
•
Converts stack machine to SSA form
•
Optimizes and simplifies the logic
•
Recover storage and memory variables, as well as function arguments
Rattle

Title
Title
Title
Title
Title
Title
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text
Text 43
/r/ethdev
Solidity Docs
Smart Contract Resources
Resource
URL
/r/ethdev https://reddit.com/r/ethdev
Solidity Docs https://solidity.readthedocs.io
Beige Paper https://github.com/chronaeon/beigepaper
Not So Smart Contracts https://github.com/trailofbits/not-so-smart-contracts
Ethersplay https://github.com/trailofbits/ethersplay
EVM-opcodes https://github.com/trailofbits/evm-opcodes
Rattle
Released soon!
Echidna https://github.com/trailofbits/echidna
Manticore https://github.com/trailofbits/manticore
Mythril https://github.com/ConsenSys/mythril
MAIAN https://github.com/MAIAN-tool/MAIAN

Questions?
ryan@trailofbits.com
@withzombies
Principal Security Researcher
Ryan Stortz jay@trailofbits.com
@computerality
Principal Security Researcher
Jay Little