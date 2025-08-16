# 1


2
Fuzzing like a security engineer

3
Who am I?
●
Nat Chin (@0xicingdeath)
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
How do we ﬁnd bugs?
●
What is property based testing?
●
How to deﬁne good invariants?
●
Comparison with similar tools
Goal: understand how to leverage fuzzing to write better code

5
Let’s start git clone https://github.com/crytic/building-secure-contracts.git git checkout eth-taipei-workshop

6
How do we ﬁnd bugs?
●
Unit testing
●
Manual Analysis
●
Automated Analysis – fully automated or semi automated

7
Fully automated
●
Results in many ﬁndings
●
Usually requires manual triaging

8
Full automated - Example

9
Semi-automated analysis
●
Beneﬁts
○
Great for logic-related bugs
●
Limitations
○
Require human in the loop
●
Ex: Property based testing with Echidna (today’s topic)

10
What is property based testing?

11
Fuzzing
●
Stress the program with random inputs*
○
Most basic fuzzer: randomly type on your keyboard
●
Fuzzing is well established in traditional software security
○
AFL, Libfuzzer, go-fuzz, ..

12
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

13
Invariant
●
Something that must always be true

14
Echidna

15
Echidna
●
Smart contract fuzzer
●
Open source:
github.com/crytic/echidna
●
Heavily used in audits & mature codebases

16
Exercises

17
Step 0: Install Echidna
Mac OS X
brew install echidna
Linux
nix-env -i -f https://github.com/crytic/echidna/tarball/master
Otherwise
Download binaries from crytic/echidna

18
Exercise 1
● program-analysis/echidna/Exercise-1.md
●
Exercise-1.md
●
Goal: implement basic arithmetic checks
●
Note: use Solidity 0.7 (see solc-select if needed)
First: try without the template!

19
Invariant - Token’s total supply
User balance never exceeds total supply

20
Echidna - Workﬂow
●
Write invariant as Solidity code
●
“User balance never exceeds total supply” function echidna_balance_of_total_supply() public returns(bool){ return balanceOf(msg.sender) <= _totalSupply;
}

21
Exercise 1 - Template contract TestToken is Token { address echidna_caller = msg.sender; constructor() public { balances[echidna_caller] = 10000;
   }
   // add the property
}

22
Exercise 1 - Solution contract TestToken is Token { address echidna_caller = msg.sender; constructor() public { balances[echidna_caller] = 10000;
   } function echidna_test_balance() view public returns(bool) { return balances[echidna_caller] <= 10000;
   }
}

23
Echidna - Workﬂow contract Token { uint256 totalSupply; mapping (address => uint256) balances; function transfer(address to, uint256 amount) {
}
}
Smart Contract Code require(balance[msg.sender] <= totalSupply);
Property Invariant
Can Echidna break the invariant?
Echidna Tests input

24
Echidna - Workﬂow pragma solidity 0.7.0; contract Token {   //address(0x0)       1 function transfer(address to, uint value)
public{ balances[msg.sender] -= value; balances[to] += value;
    }
}
Smart Contract Code require(balance[msg.sender] <= totalSupply);
Property Invariant transfer(0x0, 1)
Echidna Tests input

25
How to deﬁne good invariants

26
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

27
Identify invariants
●
Sit down and think about what the contract is supposed to do
●
Write the invariant in plain English

28
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

29
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
Sender balance should decrease by amount
■
Receiver balance should increase by amount
○
If the destination is myself, my balance should be the same
○
If I don’t have enough funds, the transaction should revert/return false

30
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
Sender balance should decrease by amount
■
Receiver balance should increase by amount
○
If self transfer is attempted => identical balance
○
If insuﬃcient funds => tx should revert / return false

31
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

32
Function-level invariant
●
Inherit the target
●
Create function and call the targeted function
●
Use assert to check the property contract TestMath is Math{ function test_commutative(uint a, uint b) public { assert(add(a, b) == add(b, a));
   }
}

33
●
Require initialization
○
Simple initialization: constructor or inheritance
○
Complex initialization: leverage your unit test/deployment scripts etheno
●
Echidna will explore all the other functions
System level invariant

34
System level invariant contract TestToken is Token { address echidna_caller = 0x00a329C0648769a73afAC7F9381e08fb43DBEA70; constructor() public{ balances[echidna_caller] = 10000;
    } function test_balance() public{ assert(balances[echidna_caller] <= 10000);
    }
}

35
Exercise 2

36
Exercise 2
● program-analysis/echidna/Exercise-2.md
●
Exercise-2.md
●
Goal: BREAK MORE STUFF!
●
Note: use Solidity 0.8.0 (see solc-select if needed)
We’ll work together ﬁrst ;)

37
Where to focus?

38
Where to focus?
●
In practice: you don’t know where the bugs are
●
Code coverage vs behavior coverage
○
Cover as many functions as possible or;
○
Focus on speciﬁc components?

39
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

40
●
Start simple, then think about composition, related behaviors, etc…
○
Can transfer and transferFrom be equivalent?
■ transfer(to, value) ?= transferFrom(msg.sender, to, value)
○
Is transfer additive-like?
■ transfer(to, v0), transfer(to, v1) ?= transfer(to, v0 + v1)?
Where to focus?

41
Where to focus?
●
Building your own experience will make you more efficient over time
●
Learn on how to think about invariants is a key component to write better code

42
Comparison with similar tools

43
Other fuzzers
●
Inbuilt in dapp, brownie, foundry, ..
●
Might be easier for simple test, however
○
Less powerful (e.g. not stateful in foundry)
○
Require speciﬁc compilation framework

44
Formal methods based approach
●
Manticore, KEVM, Certora, ..
●
Provide proofs, however
○
More diﬃcult to use
○
Return on investment is signiﬁcantly higher with fuzzing

45
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

46
Conclusion

47
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
Try Echidna on your current project*
○
Watch out for development on Medusa