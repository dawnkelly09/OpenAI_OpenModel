# 1


2
Building secure contracts:
How to fuzz like a pro

3
Who are we?
●
Nat Chin (@0xicingdeath)
●
Josselin Feist (@montyly)
●
Trail of Bits: trailofbits.com
○
We help developers to build safer software
○
R&D focused: we use the latest program analysis techniques
○
Slither, Echidna, Tealer, Amarna, solc-select, ..

4
Agenda
●
How to ﬁnd bugs?
●
What is property based testing?
●
How to deﬁne good invariants?
●
Where to focus?
●
Comparison with similar tools
Goal: understand how to leverage fuzzing to write better code

5
How to Find Bugs?
/// @notice Allow users to buy token. 1 ether = 10 tokens
/// @param tokens The numbers of token to buy
/// @dev Users can send more ether than token to be bought, to give gifts to the team.
function buy(uint tokens) public payable{
    _valid_buy(tokens, msg.value);
    _mint(msg.sender, tokens);
}
/// @notice Compute the amount of token to be minted. 1 ether = 10 tokens
/// @param desired_tokens The number of tokens to buy
/// @param wei_sent The ether value to be converted into token function _valid_buy(uint desired_tokens, uint wei_sent) internal view{ uint required_wei_sent = (desired_tokens / 10) * decimals; require(wei_sent >= required_wei_sent);
}

6
How to Find Bugs?
● 4 main techniques
○
Unit tests
○
Manual analysis
○
Fully automated analysis
○
Semi automated analysis

7
How to Find Bugs?
●
Unit tests
○
Beneﬁts
■
Well understood by developers
○
Limitations
■
Mostly cover “happy paths”
■
Might miss edge cases

8
How to ﬁnd bugs?
function test_buy(uint256 tokens_to_receive, uint256 ether_to_send) public { uint256 pre_buy_balance = token.balanceOf(address(this)); mock.buy.call{value: ether_to_send)(tokens_to_receive); assert(token.balanceOf(address(this)) == pre_buy_balance + tokens_to_receive)
}

9
How to Find Bugs?
●
Manual review
○
Beneﬁts
■
Can detect any bug
○
Limitations
■
Time consuming
■
Require speciﬁc skills
■
Does not track code changes
○
Ex: Security audit

10
How to Find Bugs?
●
Fully automated analysis
○
Beneﬁts
■
Quick & easy to use
○
Limitations
■
Cover only some class of bugs
○
Ex: Slither

11
Slither Action

12
How to Find Bugs?
●
Semi automated analysis
○
Beneﬁts
■
Great for logic-related bugs
○
Limitations
■
Require human in the loop
○
Ex: Property based testing with Echidna (today’s topic)

13
What is property based testing?

14
Fuzzing
●
Stress the program with random inputs
○
Most basic fuzzer: randomly type on your keyboard
●
Fuzzing is well established in traditional software security
○
AFL, Libfuzzer, go-fuzz, ..

15
Property based testing
●
Traditional fuzzer usually for crashes
○
Smart contracts don’t (really) have crashes
●
Property based testing
○
User deﬁnes invariants
○
Fuzzer generates random inputs to check the invariants
○
“Unit tests on steroids”

16
Invariant
●
Something that must always be true

17
Echidna
●
Smart contract fuzzer
●
Open source:
github.com/crytic/echidna
●
Heavily used in audits & mature codebases

18
Invariant - Token’s total supply
User balance never exceeds total supply

19
Echidna - Workﬂow
●
Write invariant as Solidity code
●
“User balance never exceeds total supply” function echidna_balance_of_total_supply() public returns(bool){ return balanceOf(msg.sender) <= _totalSupply;
}

20
Echidna - Workﬂow contract Token { uint256 totalSupply; mapping (address => uint256) balances; function transfer(address to, uint256 amount) {
}
}
Smart Contract Code require(balance[msg.sender] <= totalSupply);
Property Invariant
Can Echidna break the invariant?
Echidna Tests input

21
Echidna - Demo pragma solidity 0.7.0; contract Token{ mapping(address => uint) public balances; function transfer(address to, uint value) public{ balances[msg.sender] -= value; balances[to] += value;
    }
 }

22
Echidna - Demo pragma solidity 0.7.0; contract TestToken is Token { address echidna_caller = msg.sender; constructor() public { balances[echidna_caller] = 10000;
    }
    // the property function echidna_test_balance() public view returns (bool) { return balances[msg.sender] <= 10000;
    }
}

23
Echidna - Demo https://github.com/crytic/building-secure-contracts/blob/master/program-analysis/echidna/Exercise-1.md

24
How to deﬁne good invariants

25
Deﬁning good invariants
●
Start small, and iterate
●
Steps 1.
Deﬁne invariants in English 2.
Write the invariants in Solidity 3.
Run Echidna
■
If invariants broken: investigate
■
Once all the invariants pass, go back to (1)

26
Identify invariants
●
Sit down and think about what the contract is supposed to do
●
Write the invariant in plain
English

27
Identify invariants: Maths
●
Math library
○
Commutative property
■ 1 + 2 = 2 + 1
○
Identity property
■ 1 * 2 = 2
○
Inverse property
■ x + (-x) = 0

28
Identify invariants: tokens
●
ERC20.total_supply
○
No user should have a balance > total_supply
●
ERC20.transfer:
○
After calling transfer
■
My balance should have decreased by the amount
■
The receiver’s balance should have increased by the amount
○
If the destination is myself, my balance should be the same
○
If I don’t have enough funds, the transaction should revert/return false

29
Write invariants in Solidity
●
Identify the target of the invariant
○
Function-level invariant
■
Ex: arithmetic’s associativity
■
Usually stateless invariants
■
Can craft scenario to test the invariant
○
System-level invariant
■
Ex: user’s balance < total supply
■
Usually stateful invariants
■
All functions must be considered

30
Function-level invariant
●
Inherit the targets
●
Create function and call the targeted function
●
Use assert to check the property contract TestMath is Math{ function test_commutative(uint a, uint b) public { assert(add(a, b) == add(b, a));
   }
}

31
●
Require initialization
○
Simple initialization: constructor
○
Complex initialization: leverage your unit tests framework with etheno
●
Echidna will explore all the other functions
System level invariant

32
System level invariant contract TestToken is Token { address echidna_caller = 0x00a329C0648769a73afAC7F9381e08fb43DBEA70; constructor() public{ balances[echidna_caller] = 10000;
    } function test_balance() public{ assert(balances[echidna_caller] <= 10000);
    }
}

33
Where to focus?

34
Where to focus?
●
In practice: you don’t know where the bugs are
●
Code coverage vs behavior coverage
○
Cover as many functions as possible or;
○
Focus on speciﬁc components?

35
●
Try different strategies
○
Behavior coverage ﬁrst
■
Focus on 1 or 2 components
○
Code coverage ﬁrst
■
Cover many functions with simple properties
○
Alternate: 1 day on behavior coverage, then 1 day on code coverage,
…
○
No right or wrong approach: try and see what works for you
Where to focus?

36
●
Start simple, then think about composition, related behaviors, etc…
○
Can transfer and transferFrom be equivalent?
■ transfer(to, value) ?= transferFrom(msg.sender, to, value)
○
Is transfer additive-like?
■ transfer(to, v0), transfer(to, v1) ?= transfer(to, v0 + v1)?
Where to focus?

37
●
Start simple, then think about composition, related behaviors, etc…
○
Can transfer and transferFrom be equivalent?
■ transfer(to, value) ?= transferFrom(msg.sender, to, value)
○
Is transfer additive-like?
■ transfer(to, v0), transfer(to, v1) ?= transfer(to, v0 + v1)?
■
Spoiler: this won’t hold; why?
Where to focus?

38
Where to focus?
●
Building your own experience will make you more efficient over time
●
Learn on how to think about invariants is a key component to write better code

39
Demo

40
Demo
/// @notice Allow users to buy token. 1 ether = 10 tokens
/// @param tokens The numbers of token to buy
/// @dev Users can send more ether than token to be bought, to give gifts to the team.
function buy(uint tokens) public payable{
    _valid_buy(tokens, msg.value);
    _mint(msg.sender, tokens);
}
/// @notice Compute the amount of token to be minted. 1 ether = 10 tokens
/// @param desired_tokens The number of tokens to buy
/// @param wei_sent The ether value to be converted into token function _valid_buy(uint desired_tokens, uint wei_sent) internal view{ uint required_wei_sent = (desired_tokens / 10) * decimals; require(wei_sent >= required_wei_sent);
}

41
Demo
● buy is stateful
●
_valid_buy is stateless
○
Start with it

42
Demo
●
What invariants?
function _valid_buy(uint desired_tokens, uint wei_sent) internal view{ uint required_wei_sent = (desired_tokens / 10) * decimals; require(wei_sent >= required_wei_sent);
}

43
Demo
●
What invariants?
○
If wei_sent is zero, desired_tokens must be zero function _valid_buy(uint desired_tokens, uint wei_sent) internal view{ uint required_wei_sent = (desired_tokens / 10) * decimals; require(wei_sent >= required_wei_sent);
}

44
Demo function assert_no_free_token(uint desired_amount) public { require(desired_amount>0);
     _valid_buy(desired_amount, 0); assert(false); // this should never be reached
}

45
Demo
<Demo>

46
Comparison with similar tools

47
Other fuzzers
●
Inbuilt in dapp, brownie, foundry, ..
●
Might be easier for simple test, however
○
Less powerful (e.g. not stateful in foundry)
○
Require speciﬁc compilation framework

48
Formal methods based approach
●
Manticore, KEVM, Certora, ..
●
Provide proofs, however
○
More diﬃcult to use
○
Return on investment is signiﬁcantly higher with fuzzing

49
Echidna’s advantages
●
Echidna has unique additional advanced features
○
Can target high gas consumption functions
○
Diﬀerential fuzzing
○
Works with any compilation framework
○
Diﬀerent APIs
■
Boolean property, assertion, dapptest/foundry mode, …
●
Free & open source

50
Conclusion

51
Conclusion
● https://github.com/crytic/echidna
●
To learn more: github.com/crytic/building-secure-contracts
●
Start by writing invariants in English, then write Solidity properties
○
Start simple and iterate
●
Your mission
○
Try Echidna on your current project
ToB is hiring (https://jobs.lever.co/trailofbits)
●
Security Consultants & Apprentices