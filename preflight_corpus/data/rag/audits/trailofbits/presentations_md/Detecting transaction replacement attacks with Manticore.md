# Detecting transaction displacement attacks with Manticore

Sam Moelius
Please do interrupt me with questions.

Transaction displacement attack1
An attacker replaces a legitimate transaction with their own, to steal something of value intended the legitimate transaction’s sender.
2 1 Shayan Eskandari, Seyedehmahsa Moosavi, Jeremy Clark. “SoK: Transparent Dishonesty: Front-Running
Attacks on Blockchain.” In Proceedings of Financial Cryptography and Data Security, 2019.

Eskandari, et al. 2019, “Transparent Dishonesty” 3

Eskandari, et al. 2019, “Transparent Dishonesty” 4

“Examples of displacement include:
5
●Alice trying to register a domain name and Mallory registering it ﬁrst...;
●Alice trying to submit a bug to receive a bounty and Mallory stealing it and submitting it ﬁrst...; and
●Alice trying to submit a bid in an auction and Mallory copying it.”2 2 Eskandari, et al. 2019, page 173

“Examples of displacement include:
6
●Alice trying to register a domain name and Mallory registering it ﬁrst...;
●Alice trying to submit a bug to receive a bounty and Mallory stealing it and submitting it ﬁrst...; and
●Alice trying to submit a bid in an auction and Mallory copying it.”2 2 Eskandari, et al. 2019, page 173

Detailed example contract AddressBounty { bool redeemed; address target; constructor(address _target) public payable { target = _target;
    } function submit(uint256 _x, uint256 _y) public { require(!redeemed, "already redeemed"); require(target == address(uint256(keccak256(abi.encodePacked(_x, _y)))), "invalid"); redeemed = true; msg.sender.transfer(address(this).balance);
    }
} 7

Ethereum 8
Alice
Bob
Charlie
Mallory Miner
✔ transaction succeeds     ✘ transaction reverts

Ethereum 9
Alice
Bob
Charlie
Mallory Miner
✔ transaction succeeds     ✘ transaction reverts
Send 10 Eth to Bob

Ethereum 10
Alice
Bob
Charlie
Mallory Miner
✔ transaction succeeds     ✘ transaction reverts
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz

Ethereum 11
Alice
Bob
Charlie
Mallory Miner
✔ transaction succeeds     ✘ transaction reverts
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty

Ethereum 12
Alice
Bob
Charlie
Mallory Miner
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty
✔ transaction succeeds     ✘ transaction reverts

Ethereum 13
Alice
Bob
Charlie
Mallory Miner
Alice: Send 10 Eth to Bob ✔
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty
✔ transaction succeeds     ✘ transaction reverts

Ethereum 14
Alice
Bob
Charlie
Mallory Miner
Alice: Send 10 Eth to Bob ✔
Bob: Call foo(“bar”) on contract baz ✘
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty
✔ transaction succeeds     ✘ transaction reverts

Ethereum 15
Alice
Bob
Charlie
Mallory Miner
Alice: Send 10 Eth to Bob ✔
Bob: Call foo(“bar”) on contract baz ✘
Mallory: Call submit(x, y) on AddressBounty ✔
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty
✔ transaction succeeds     ✘ transaction reverts

Ethereum 16
Alice
Bob
Charlie
Mallory Miner
Alice: Send 10 Eth to Bob ✔
Bob: Call foo(“bar”) on contract baz ✘
Mallory: Call submit(x, y) on AddressBounty ✔
Charlie: Call submit(x, y) on AddressBounty ✘
Send 10 Eth to Bob
Call foo(“bar”)
on contract baz
Call submit(x, y)
on AddressBounty
✔ transaction succeeds     ✘ transaction reverts

How to ﬁx?
●Instead of calling just submit(x, y), the sender calls commit(z) followed by reveal(x, y).
●The contract veriﬁes:
○the calls to commit and reveal are separated by at least n blocks
○z == hash(x, y, sender’s address)
○submit(x, y) would have succeeded 17

How to detect?
18
In each of these examples, you would expect the legitimate transaction to revert following the fraudulent one:
●“Alice trying to register a domain name and Mallory registering it ﬁrst...;
●Alice trying to submit a bug to receive a bounty and Mallory stealing it and submitting it ﬁrst...; and
●Alice trying to submit a bid in an auction and Mallory copying it.”3 3 Eskandari, et al. 2019, page 173 (repeated)

Example revisited contract AddressBounty { bool redeemed; address target; constructor(address _target) public payable { target = _target;
    } function submit(uint256 _x, uint256 _y) public { require(!redeemed, "already redeemed"); require(target == address(uint256(keccak256(abi.encodePacked(_x, _y)))), "invalid"); redeemed = true; msg.sender.transfer(address(this).balance);
    }
} 19

Example revisited contract AddressBounty { bool redeemed; address target; constructor(address _target) public payable { target = _target;
    } function submit(uint256 _x, uint256 _y) public { require(!redeemed, "already redeemed"); require(target == address(uint256(keccak256(abi.encodePacked(_x, _y)))), "invalid"); redeemed = true; msg.sender.transfer(address(this).balance);
    }
} 20

Manticore4
●Trail of Bits’ symbolic execution tool
●Manticore can analyze the following types of programs:
○Ethereum smart contracts (EVM bytecode)
○Linux ELF binaries (x86, x86_64, aarch64, and ARMv7)
○WASM modules 21 4 https://github.com/trailofbits/manticore

✔ transaction succeeds     ✘ transaction reverts 22
●
Each circle in these diagrams represents a state of the blockchain.
●
Each arrow represents a transaction.
✔

✔ transaction succeeds     ✘ transaction reverts 23
✔
✔

✔ transaction succeeds     ✘ transaction reverts 24
✔
✔
✘

✔ transaction succeeds     ✘ transaction reverts 25
✔
✔
✘
✘

✔ transaction succeeds     ✘ transaction reverts
✘
✔
✔
✘
✘

✔ transaction succeeds     ✘ transaction reverts
U ✔
✘
✔
✔
✘
✘

✔ transaction succeeds     ✘ transaction reverts

✔ transaction succeeds     ✘ transaction reverts
U ✔
T0

✔ transaction succeeds     ✘ transaction reverts
U ✔
T0
T1
U ✔

✔ transaction succeeds     ✘ transaction reverts
U ✔
T0
T1
T2
U ✔
U ✘

✔ transaction succeeds     ✘ transaction reverts
U ✔
T0
T1
T2
U ✔
U ✘

Example re-revisited
#! /usr/bin/env python3 from manticore.ethereum import ManticoreEVM, DetectTransactionDisplacement
# Example due to Vincent Kobel:
#   https://kobl.one/blog/create-full-ethereum-keypair-and-address/ target = 0x0BED7ABD61247635C1973EB38474A2516ED1D884 x = 0x836B35A026743E823A90A0EE3B91BF615C6A757E2B60B9E1DC1826FD0DD16106 y = 0xF7BC1E8179F665015F43C6C81F39062FC2086ED849625C06E04697698B21855E mevm = ManticoreEVM()
mevm.register_detector(DetectTransactionDisplacement())
owner = mevm.create_account()
contract = mevm.solidity_create_contract("addressbounty.sol", owner=owner, args=(target,))
contract.submit(x, y)
mevm.finalize()
33

Example re-revisited
#! /usr/bin/env python3 from manticore.ethereum import ManticoreEVM, DetectTransactionDisplacement
# Example due to Vincent Kobel:
#   https://kobl.one/blog/create-full-ethereum-keypair-and-address/ target = 0x0BED7ABD61247635C1973EB38474A2516ED1D884 x = 0x836B35A026743E823A90A0EE3B91BF615C6A757E2B60B9E1DC1826FD0DD16106 y = 0xF7BC1E8179F665015F43C6C81F39062FC2086ED849625C06E04697698B21855E mevm = ManticoreEVM()
mevm.register_detector(DetectTransactionDisplacement())
owner = mevm.create_account()
contract = mevm.solidity_create_contract("addressbounty.sol", owner=owner, args=(target,))
contract.submit(x, y)
mevm.finalize()
34
This is where the magic happens.

user_00000005.tx (abbreviated)
...
Transactions No. 2
...
Data: 0x68284601836b35a026743e823a90a0ee3b91bf615c6a757e2b60b9e1dc1826fd0dd16106f7bc1e8179...06 (*)
Return_data: 0x ()
Function call: submit(59442405910536717807339445266761957645979351286933895105994337169002594394374, 112053651391312806093045014627548927131116995152518320482663926909859426043230) -> STOP (*)
Transactions No. 3
...
Data: 0x68284601836b35a026743e823a90a0ee3b91bf615c6a757e2b60b9e1dc1826fd0dd16106f7bc1e8179...06 (*)
Return_data:
0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000 00000000000000000000000000000000000010616c72656164792072656465656d6564000000000000000000000000000000 00 (y already redeemed) (*)
Function call: submit(59442405910536717807339445266761957645979351286933895105994337169002594394374, 112053651391312806093045014627548927131116995152518320482663926909859426043230) -> REVERT 35

user_00000005.tx (abbreviated)
...
Transactions No. 2
...
Data: 0x68284601836b35a026743e823a90a0ee3b91bf615c6a757e2b60b9e1dc1826fd0dd16106f7bc1e8179...06 (*)
Return_data: 0x ()
Function call: submit(59442405910536717807339445266761957645979351286933895105994337169002594394374, 112053651391312806093045014627548927131116995152518320482663926909859426043230) -> STOP (*)
Transactions No. 3
...
Data: 0x68284601836b35a026743e823a90a0ee3b91bf615c6a757e2b60b9e1dc1826fd0dd16106f7bc1e8179...06 (*)
Return_data:
0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000 00000000000000000000000000000000000010616c72656164792072656465656d6564000000000000000000000000000000 00 (y already redeemed) (*)
Function call: submit(59442405910536717807339445266761957645979351286933895105994337169002594394374, 112053651391312806093045014627548927131116995152518320482663926909859426043230) -> REVERT 36

Limitations (1 of 3): Expensive
●Adding a symbolic transaction to a run is expensive.
37

Limitations (2 of 3): False negatives
●Not every transaction displacement attack will cause a legitimate transaction to revert following a fraudulent one.
●Manticore’s search is not guaranteed to be exhaustive.
●For contracts involving hard computational problems, an example, successful transaction is a must.
●If transaction U is a CREATE, we ignore it.
38

Limitations (3 of 3): False positives
●“Unsound symbolication,”5 which turns the output of certain hash functions into free variables, causes false positives.
●Not every situation where a legitimate transaction would revert following a fraudulent one is worth ﬁxing.
39 5 “Unsound symbolication - A general approach to handle symbolic imprecisions” https://github.com/trailofbits/manticore/pull/1526

Real world “false positive”
/// @title Golem Network Token (GNT) - crowdfunding code for Golem Project contract GolemNetworkToken {
    ...
    function finalize() external {
        // Abort if not in Funding Success state.
        if (!funding) throw; if ((block.number <= fundingEndBlock || totalTokens < tokenCreationMin) && totalTokens < tokenCreationCap) throw;
        // Switch to Operational state. This is the only place this can happen.
        funding = false;
        ...
    }
    ...
} 40

Real world “false positive”
/// @title Golem Network Token (GNT) - crowdfunding code for Golem Project contract GolemNetworkToken {
    ...
    function finalize() external {
        // Abort if not in Funding Success state.
        if (!funding) throw;                       // if (funding) ...
        if ((block.number <= fundingEndBlock ||    // if ((block.number > fundingEndBlock && totalTokens < tokenCreationMin) &&    //     totalTokens >= tokenCreationMin) || totalTokens < tokenCreationCap) throw; //     totalTokens >= tokenCreationCap) ...
        // Switch to Operational state. This is the only place this can happen.
        funding = false;
        ...
    }
    ...
} 41

[WIP] Transaction displacement attack detector https://github.com/trailofbits/manticore/pull/1698 sam.moelius@trailofbits.com
Manticore team
Eric Hennenfent      Eric Kilmer      Brad Larsen
Felipe Manzano      Sonya Schriner

An example contract Basic { uint256 n; constructor(uint256 _n) public { n = _n;
    } function submit(uint256 _x) external { require(n == _x, "wrong value"); n++;
    }
} 43