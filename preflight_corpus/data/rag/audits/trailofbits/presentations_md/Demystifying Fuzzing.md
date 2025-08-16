# 1

Demystifying Fuzzing
Nat Chin

2
Hi! I’m Nat!
●
Blockchain Security Engineer at Trail of Bits
●
I ﬁgure out where things can break
●
Fell down the rabbit hole in 2017
●
Former smart contract developer & blockchain professor
●
Author of solc-select
●
Twitter: @0xicingdeath

3
Agenda
●
Deﬁning Invariants
●
Writing properties
●
Fuzzing!
●
Finding fun bugs

4
Fuzzing
●
Deﬁne assumptions meant to hold true
●
Exploration of contracts with randomized arguments
●
Checks dangerous contract states

5
What’s an invariant?
●
“Invariant Testing” = “Property
Testing”
●
System properties that should always be true

6 for value in [0, 255] { call function; if invariant is broken { profit
}
}
●
Even with constraint smart contracts, astronomical search space
●
What if the invariant is only broken for a single, unique input?
●
Multiple accounts/contracts interacting with each other?
Fuzzing is Easy!
But It’s Also Hard!

7
Echidna

8
How do I start?
1.
Identify your properties in English 2.
Convert your properties to code 3.
Run Echidna 4.
FIND BUGS

9 1: Identify your Invariants
IN ENGLISH WORDS.

10
Invariants
●
They’re everywhere!
●
Token Invariants
●
Mathematical invariants

11
Token Invariants – Total Supply
User balance never exceeds total supply

12
Token Invariants – Transfer
Users cannot transfer more than they own

13
Mathematical Invariant – Association 1 + 2 = 3 2 + 1 = 3

14
Mathematical Invariant – Identity 1 * 2 = 2 0 + x = x

15
Mathematical Invariant – Addition / Subtraction x + 5 - 5 = x

16 2: Convert into Code
IT’S EASIER THAN IT SOUNDS.

17
Token Invariants – Total Supply

18
Mathematical Invariant – Association

19
Mathematical Invariant – Identity

20
Mathematical Invariant – Addition / Subtraction

21
Example - rmm-core

22
Liquidity Pools
●
Allocate assets into the pool
●
Remove assets from the pool
●
Swap assets

23
Liquidity Pools x
+ 5
  (5)
——— x
●
Initial pool balance: x
●
Deposit: 5
●
Withdraw: 5
What value do you expect the pool balance to be?

24
Allocate/Remove Functions

25
What should the test do?
1.
Start with initial reserve and liquidity balance 2.
Allocate funds into the system 3.
Remove funds from the system 4.
Balance before and after transactions should be equal

26
Invariant Test
Step 1

27
Invariant Test
Step 2

28
Invariant Test
Step 3

29
Invariant Test
Step 4

30
Echidna Results

31
Events

32
Event Results
Amount allocated
Amount removed
Delta
Token 1 6361150874 6361150873 1

33
Event Results
Amount allocated
Amount removed
Delta
Token 1 6361150874 6361150873 1
Token 2 64,302,260,917,206, 574,294,870 643022609152865326 47367 1,920,041,647,503

34
What does it mean?
●
Adding and removing funds are not exact inverses
●
Users will actually receive 1,920,041,647,503 less

35
Why is there a delta?
toUint128()

36
Why is toUint128() important?
●
Converts FixedPoint 64x64 to uint128
●
Truncates numbers too large
●
Used in both allocation and removal functions

37
With that in mind….

38
How can it be ﬁxed?

39

40
It can’t, but….it can be mitigated
●
Deﬁning an acceptable delta
●
Round in a direction to beneﬁt a pool

41
Only the tip of the iceberg…
●
Access Controls
●
Correct Bookkeeping
●
Token balances
●
Differential Fuzzing

42
What next?
●
Talk to us!
●
Go through Echidna tutorials on building-secure-contracts
●
Use Echidna on your codebase
●
Join Empire Hacking