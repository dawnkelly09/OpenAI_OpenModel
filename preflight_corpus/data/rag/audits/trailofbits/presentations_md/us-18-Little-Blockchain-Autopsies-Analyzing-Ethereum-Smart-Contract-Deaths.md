# Blockchain Autopsies:

Analyzing Ethereum Smart
Contract Deaths
Jay Little
Blackhat USA 2018
August 6, 2018

Jay Little
Principal Security Engineer
@computerality
Favorite IDA Pro keyboard shortcuts : Y and D
Working with Smart Contracts  > 1 year

Cyber security research company - High-end security research with a real- world attacker mentality to reduce risk and fortify code.
Security Assessments
Security Engineering
Security Research
•
We offer security auditing for code and systems requiring extreme robustness and niche system expertise
•
We offer custom engineering for every stage of software creation, from initial planning to enhancing the security of completed works
•
As a leading cybersecurity research provider to DARPA, the
Army and the Navy – we create and release open source research tools
Trail of Bits

Agenda
●Introduction to Ethereum, EVM, and Solidity
●Vulnerabilities and Reversing Tools
●Ethereum Node Software
●Blockchain Contract Trace Analysis
●Analyze Contract Deaths

Prompt eth.getCode(0xcD6D2cD79fD754C6B909585E46541D32ec491962)
> 0x
●Where did the code go?
●Who created this contract?
●What was the last transaction to this contract?
●Why are articles only about open-source contracts?
●When did all of this happen?

Ethereum, EVM, and Solidity

Ethereum
●
A blockchain based distributed ledger
●
A “world computer” with “smart” contracts
●The 2nd largest cryptocurrency by valuation
●Mainnet started July 30 2015 https://coinmarketcap.com/currencies/ethereum/

Ethereum Implementation
●
Ethereum is formally described by the Yellow Paper
● https://github.com/ethereum/yellowpaper
● https://github.com/chronaeon/beigepaper

Accounts and Transactions and Blocks
!→"→#
!→"$→%
!→"$→%→"$→%
•
Account: !
•
Contract: %
• 1 Ether (ETH) = 1018 Wei
• 21000 Wei per TX
•
Contracts can call other contracts
&

EVM: Ethereum Virtual Machine
●
Big Endian stack machine
●
~185 opcodes
●
Native data width is 256 bits
●
Many instructions are similar
●
PUSH1 – PUSH32
●
DUP1 – DUP16
●
SWAP1 – SWAP16
●
Instructions have various gas cost
● ethervm.io or https://github.com/trailofbits/evm-opcodes

ABI and Address Spaces
●
EVM is a Harvard architecture
●
There are ~5 address spaces
●
Storage and memory are 256- bit address space
●
All execution enters at
PC=0x0
●
Jump destinations labeled with JUMPDEST
●
Functions dispatched based on first 4 bytes in TX input
Code
EVM, implements contract logic
Stack
Limited to 32 elements
Call Data
Invocation arguments
Memory
Non-persistent storage, per tx
Storage
Persistent storage

Solidity
●
JavaScript-inspired high-level language for smart contracts
●
Compiles to EVM

Sample Contract

Sample Contract Creation
! → "# → 0x0
$ owner: !
jar[]

Sample Contract Death close() = 0x43d726d6
! → close() → "
" → # → !
" = 0x owner:[]
jar[]

Sample Contract Usage bake() = 0xb0de262e
! → bake() → "
! → bake() → "
# → bake() → "
" owner:$ jar[#]=%% jar[!]=%%%%

Sample Contract Usage (2)
CookieShop.eat(5) = 0x85e0ebaf00000000000000 000000000000000000000000 000000000000000000000000 05
! → eat(5) → "
" owner:# jar[!]=$ jar[%]=$$$$

Sample Contract Usage (3)
! → eat(1) → "
" owner:# jar[$]=% jar[&]=%%%% jar[!]=
%%%%%%%%%%%%%%
%%%%%%%%%%%%%%
%%%%%%%%%%%%%%
%%%%%%%%%%%%%%
%%%%%%%%%%%%%%
%%%%%%%%%%%%%%

Features / Vulnerabilities

●
Division by zero
●
Race conditions
●
Replay attacks
●
Bad RNG
●
Time sensitivity
●
Blockchain as random
Solidity Behaviors and Issues
●
Int overflow/underflow
●
Incomplete initialization
●
Uninitialized variables
●
Callbacks / re-entrancy
●
Variable name shadowing
●
Type inference (var)
●
Unintentional visibility
●
Array.length
●
Delegatecall

Uninitialized Variables contract OpenAddressLottery{      0x741F1923974464eFd0Aa70e77800BA5d9ed18902 struct SeedComponents { https://www.reddit.com/r/ethdev/comments/7wp363 uint component1; uint component2;
} address owner; //address of the owner uint private secretSeed; //seed used to calculate number of an address function forceReseed() { require(msg.sender==owner);
SeedComponents s; s.component1 = uint(msg.sender); s.component2 = uint256(block.blockhash(block.number - 1));
}
}

Not So Smart Contracts https://github.com/trailofbits/not-so-smart-contracts

Analysis Tools

Ethersplay
Binary Ninja Plugin https://github.com/trailofbits/ethersplay

IDA-EVM
IDA Pro Module https://github.com/trailofbits/ida-evm

ethervm.io 26

Mythril https://github.com/consensys/mythril

Rattle https://github.com/trailofbits/rattle
Released this morning!
●Recovers EVM Control Flow
●Lifts EVM to IR to SSA IR
●Optimizes and simpliﬁes
●Recovers variables
●Generates function CFGs

Manticore https://github.com/trailofbits/manticore

Ethereum Software

Storage Requirements
Check stackexchange ﬁrst.
From @5chdn at https://wiki.parity.io/faq and https://ethereum.stackexchange.
com/questions/143/what-are-the- ethereum-disk-space-needs

Geth and Parity
Geth - official implementation, runs 75% public nodes
Written in Go/LevelDB
Parity - alternate implementation, runs 15% public nodes
Written in Rust/RocksDB
Client Type
Size
Time
Details
Full 100GB-1.5TB
~ Weeks to Forever
Large SSD, can fetch any TX
Fast 50-200GB
~ Hours to Days
SSD, Recent TX only
Light 50MB+
~ Minutes to Hours
HDD, Intended for “end user”

Geth Running Options
./geth --datadir /mnt/fastssd/.geth
--rpc --rpcapi=debug,eth,net,rpc,web3
--syncmode=full
--gcmode=archive
--cache 4096
--trie-cache-gens 1024

Parity Running Options parity -d /mnt/fastssd/.parity
--jsonrpc-apis web3,eth,net,parity,rpc,traces
--mode=active
--pruning=archive
--tracing=on --fat-db=on
--min-peers=50 --max-peers=100
--cache-size=4096
--db-compaction=ssd
--tx-queue-size=8192000
--scale-verifiers --num-verifiers=8
--jsonrpc-server-threads 4 --jsonrpc-threads 8

Client Operation Suggestions
●Have patience
●Troubleshoot with rm –rf and resync
●Use Linux
●Use the fastest SSDs you can aﬀord
●Ethereum clients and web browsing don’t mix

Many Days Later...

Contract Analysis

Answering Questions eth.getCode(0xcD6D2cD79fD754C6B909585E46541D32ec491962)
> 0x
●Who created this contract?
●What was the last transaction to this contract?
●Where did the code go?
●When did all of this happen?

Tracing
Parity:
trace_replayTransaction(tx_hash, [‘trace’])
Geth:
debug_traceTransaction(tx_hash)

Transactions
{'blockNumber': '5269390',
'from': '0xcd6d2cd79fd754c6b909585e46541d32ec491962',
'hash':
'0x9ebcb287709403cb4c11d6c82203cfee0428b1dda72b417a65d2ba120fc70947',
'isError': '0',
'timeStamp': '1521260221',
'to': '0x3f9ed84ef180fae940ebf4bce4c4d70e2f751482',
'type': 'suicide',
'value': '298227981000000000'}

Who? What? When?
Block: 5245655
From: 0x00bb585e7be7b095be9aba3c5777121c5ba7924a
To: 0
[Contract 0xcd6d2cd79fd754c6b909585e46541d32ec491962
Created]
0x00bb585e7be7b095be9aba3c5777121c5ba7924a Adds 0.2 Ether 0x3f9ed84ef180fae940ebf4bce4c4d70e2f751482: 0xa840dda9 0x3f9ed84ef180fae940ebf4bce4c4d70e2f751482: kill()
0xcd6d2cd79fd754c6b909585e46541d32ec491962 => selfdestruct 0x3f9ed84ef180fae940ebf4bce4c4d70e2f751482

Scanning the Blockchain

Blockchain Data
Distributed Ledger != Distributed Database
Only a key/value store with list of blocks/transactions
No queryable structure
Ethereum is focused on recent transaction and current state, not history

The Block in Blockchain

web3.js and web3.py web3.js is official client library
●Many API changes between v0.20 and v1.0 web3.py is Python implementation of web3.js
●Version 4.0 switched to Python3.5+
Both communicate to Ethereum nodes via:
●IPC - use when local
●WebSockets - use when streaming events
●RPC - use in any other situation

Finding Contracts for b in range(0, 6000000):
block = w.eth.getBlock(b, full_transactions=True)
for tx in block.transactions:
if tx['to'] == None:
r = w.eth.getTransactionReceipt(tx['hash'])
address = r['contractAddress']
if address:
code = w.eth.getCode(address)
if code == '0x' and r['status'] == 1:
saveContract(block, address, tx['input'])

Geth Experience

Parity Experience
> eth.getBlock(427360)
> null

etherscan.io

Hybrid Approach
Local Ethereum software + Etherscan API https://etherscan.io/apis
●txlist
●txlistinternal

Empty Code Results
From block 0 to 6,000,000 (July 20 2018):
●1,799,570 total contracts
●1,745,317 alive, 54,253 empty contracts
●28,174 unique creation code for empty contracts
●32,308 empty contracts with 0 balance

First Contract Creation
Block 46402 (2015-08-07)
https://etherscan.io/tx/0x6c929e1c3d860ee225d7f3a7ad df9e3f740603d243260536dfa2f3cf02b51de4 00000000: PUSH1 0x60 00000002: PUSH1 0x40 00000004: MSTORE 00000005: PUSH1 0x0 00000007: DUP1 00000008: SLOAD 00000009: PUSH1 0x1 0000000b: PUSH1 0xa0 0000000d: PUSH1 0x2 0000000f: EXP 00000010: SUB 00000011: NOT 00000012: AND 00000013: CALLER 00000014: OR 00000015: SWAP1 00000016: SSTORE 00000017: PUSH1 0x6 00000019: DUP1 0000001a: PUSH1 0x23 0000001c: PUSH1 0x0 0000001e: CODECOPY 0000001f: PUSH1 0x0 00000021: RETURN 00000022: STOP 00000023: PUSH1 0x60 00000025: PUSH1 0x40 00000027: MSTORE 00000028: STOP

First Contract “Creation” (With Enough Gas)

First Contract Creation (With Code)
Block 48643 (2015-08-07)
Account 0x6516298e1c94769432ef6d5f450579094e8c21fa

Top Duplicates
Count: 10,072
Code:
0x5b620186a05a1315 601357600160205260 00565b600080601f60 0039601f565b6000f3

Top Duplicates (2)
Count: 9,512
Code:
0x
Total: 6203 ETH  (~$2,600,000)

Top Duplicates (3)
Count: 1,963
Code:
0x0000000000000000000000000000000000000000000000 0000000000000000000…00000000000000000000 6000 NULs (STOP)
*EIP-170 sets max size to 0x6000

Noise / Spam 0x7F62E6C7Ec6700187aB99f71997912A9CDF184D1
PUSH20 0xff5932556071d5ac315d240b92b97a3b4f7daf3d
SELFDESTRUCT 0, 1 or 2 Wei transferred 1988 contracts after ﬁltering

Massive selfdestruct https://etherscan.io/tx/0x0bb3c5ec638d167a00d3e790cbf769 2b39e70d343ad4900ef241c21e10d016a0

Massive selfdestruct (2)
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!
!→"#→!

Analyzing 2,000 Deaths

Criteria
! → " →#
! → "$ → # → " → %
& → "$ → # → " → &

Creator != selfdestruct destination
From trace, we know the destination of selfdestruct
Filter when this is not the original contract creator 630 contracts remaining 10 of these send ETH to address 0x0

50ETH to 0x0 0xf73d247ffDBD5A9964d1a1444c86343650b67ed4 https://etherscan.io/address/0xf73d247ffdbd5a9964d1a1444 c86343650b67ed4
Function: kill(address _to) MethodID: 0xcbf0b0c0
[0]:
000000000000000000000000000000000000000000000000 0000000000000000

10,000 ETH!
0xf199Af8B17D81c41ABe6220a1D7C9fe04d0d9d2c
Parity multisig wallet initWallet() attack?
https://blog.zeppelin.solutions/on-the-parity-wallet-multisig- hack-405a8c12e8f7

Creator != selfdestruct transaction originator 159 contracts meet these conditions 25 contracts sent > 0.1 ETH
Only 16 contracts sent >= 1 ETH

300ETH selfdestruct
Account:0x96f65700904cB464F3D153a2744B84FCa27ABF9C
Sent 300ETH to 0xCafe00be401442Bfb5E480C355393FD8C147abBB
Function: changeOwner(address _from, address _to) ***
MethodID: 0xf00d4b5d
[0]:  000000000000000000000000374139a05ac55917badd3f934f1b93f5c8623ded
[1]:  000000000000000000000000cafe00be401442bfb5e480c355393fd8c147abbb

Dice2Win 0xD1CEeee6B94DE402e14F24De0871580917ede8a7
Sent 65.7 ETH to 0xD1CEeee271fD5a8B0e2BFc12Ea5B5b2E5CeDEc95
Function: approveNextOwner(address _nextOwner)
MethodID: 0xd579fd44
[0]:  000000000000000000000000d1ceeee271fd5a8b0e2bfc12ea5b5b2e5cedec95

Etherwow 0x4DF6DE08D11f11EBAd5d9E136B768849426fB8a7
Function: ownerChangeOwner(address newOwner)
MethodID: 0x4f44728d
[0]:  0000000000000000000000007d138be0eed529ae42a468472b2beb0314af5e28
Function: ownerkill()
/** @dev owner selfdestruct contract
***BE CAREFUL! EMERGENCY ONLY
/ CONTRACT UPGRADE*** */ function ownerkill() publiconlyOwner
{ selfdestruct(owner); }

Becoming Mortal 0xf4D3CEd0929eA3F3Fd94F32ba460a66b428932F2 function mortal() { owner = msg.sender; } function kill() { if(msg.sender == owner) selfdestruct(owner);
}

Conclusion
If you are developing contracts:
●Understand and fix all warnings
●Add an Echidna test
●Write exhaustive positive/negative tests
●
Perform an rigorous assessment
If you are a security researcher:
●
Become a blockchain explorer
●
Have patience
●
Symbolically execute with Manticore
●
Work with us
Contact
Jay Little, Principal Security Engineer jay@trailofbits.com
@computerality
@trailofbits www.trailofbits.com github.com/trailofbits blog.trailofbits.com
We’re Hiring!
Trail of Bits is hiring engineers and vulnerability researchers who are excited about C++ code, blockchain software, and smart contracts.