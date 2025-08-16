# CYBERDYNE:

Automatic bug-finding at scale
Peter Goodman
COUNTERMEASURE   2016

2
Finds bug in binaries
Combines different techniques

Coverage-guided fuzzing

Symbolic execution
Cyberdyne (ex)terminates  bugs

3
Part 1: high level architecture

How to coordinate bug-finding tools
Part 2: low level tools

How do the bug-finding tools work?
Get  to  know  the  mind  of  the  machine

4
History: Cyber  Grand  Challenge  (1)

5
Capture-the-flag (CTF) competition

Goal: find and exploit bugs in binaries

Goal: patch binaries
Competitors were programs

“Cyber Reasoning Systems” (CRS)
History: Cyber  Grand  Challenge  (2)

6
Shaped the design of Cyberdyne
Distributed system

Runs on any number of nodes
Automated system

No human intervention required
History:  Cyber Grand  Challenge  (3)

Part  1
Skeleton  of  a  bug-finding
system 7

8
Find bugs

Simple, right?
Work on real programs
Be easy to scale
Ideally, a  bug-finding  system should …

9
When  I  grow  up …

10
First  kill:  simple  fuzzing  (1)
Splice
Slice
Bit flips
Byte flips
Seed Inputs
Mutation
Engine
Mutated Inputs

11
First  kill:  simple  fuzzing  (1)
Seed Inputs
Mutation
Engine
Mutated Inputs
Radamsa, zzuf, etc.

12
First  kill:  simple  fuzzing  (2)
Mutate inputs
Execute inputs
…
Profit?

Find bugs!


 12 1 2 3 4 5 6 7 8 9 10 11
Terminator pag@sloth:~/ cyberdyne start pag@sloth:~/ cyberdyne analyze –program foo –binaries bar pag@sloth:~/ cyberdyne seed –program foo – inputs ./inputs/*

13
First  kill:  simple  fuzzing  (2)
Mutate inputs
Execute inputs
…
Profit?

Find bugs!


 12 1 2 3 4 5 6 7 8 9 10 11
Terminator pag@sloth:~/ cyberdyne start pag@sloth:~/ cyberdyne analyze –program foo –binaries bar pag@sloth:~/ cyberdyne seed –program foo – inputs ./inputs/*

14
First  kill:  simple  fuzzing  (2)
Mutate inputs
Execute inputs
…
Profit?

Find bugs!


 12 1 2 3 4 5 6 7 8 9 10 11
Terminator pag@sloth:~/ cyberdyne start pag@sloth:~/ cyberdyne analyze –program foo –binaries bar pag@sloth:~/ cyberdyne seed –program foo – inputs ./inputs/*

15
First  kill:  simple  fuzzing  (2)
Mutate inputs
Execute inputs
…
Profit?

Find bugs!

Right????


 12 1 2 3 4 5 6 7 8 9 10 11
Terminator pag@sloth:~/ cyberdyne start pag@sloth:~/ cyberdyne analyze –program foo –binaries bar pag@sloth:~/ cyberdyne seed –program foo – inputs ./inputs/*

16
First  kill:  simple  fuzzing  (2)



Terminator pag@sloth:~/ cyberdyne start pag@sloth:~/ cyberdyne analyze –program foo –binaries bar pag@sloth:~/ cyberdyne seed –program foo – inputs ./inputs/*
Mutate inputs
Execute inputs
…
Risk of loss!

No bugs found

Lost cycles, time

17
Searching for bugs takes time
Need accountability

Is it worth it to keep searching?

Is progress being made?
How do we measure progress?
Misfire:  Check  your  targets

18
Idea: has something new happened?
Track when new code is executed

Code coverage: Instrument program to detect when new code is executed

Inputs that cover new code signal progress
Reload:  Track  bug-finding  progress

19
Eventually hit a “coverage ceiling”

Decreasing marginal returns
Need heavier guns

Coverage-guided fuzzing: re-seed with inputs that got new coverage (next)

Symbolic execution (later)
Need  more  ammo

Crashes!
20
Coverage-guided  mutational  fuzzing  (1)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
Step 1
Mutate inputs
Step 2
Execute mutations
Step 3
Gets new
Coverage?
Step 4
Re-seed mutator

Crashes!
21
Coverage-guided  mutational  fuzzing  (1)
Step 1
Mutate inputs
Step 2
Execute mutations
Step 3
Gets new
Coverage?
Step 4
Re-seed mutator
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
AFL

22
Trivially parallelizable

Run mutation engines concurrently
Scaling fuzzing in Cyberdyne

Fuzzer service internalizes mutation, execution, code coverage

Runs many fuzzers, one mutator each
Coverage-guided  mutational  fuzzing  (2)

Look  under  the  skin  of  Cyberdyne  (1)
23

24
Look  under  the  skin  of  Cyberdyne  (2)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

25
Look  under  the  skin  of  Cyberdyne  (3)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
Fuzzer (with GRR)

Mutates and executes inputs

Easy to scale

26
Look  under  the  skin  of  Cyberdyne  (4)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
PySymEmu

Coverage-guided binary symbolic executor

Harder to scale

27
Look  under  the  skin  of  Cyberdyne  (5)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
KLEE (with McSema)

LLVM bitcode symbolic executor

Hard to use

Hard to scale

28
Look  under  the  skin  of  Cyberdyne  (6)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
Oracle
Gatekeeper for minset
Detects crashes
Easy to scale

29
Look  under  the  skin  of  Cyberdyne  (7)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes
Minset

Finds inputs that get new code coverage

One input at a time

Bottleneck?

Part  2
The  servos  and  the  gears 30

31
What is it?

Minimum set of inputs that produce maximum code coverage
Why use it?

Identify “interesting” inputs

Good candidates for exploration
How  it  works:  Minset  (1)

32
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (2)
2 3 4 4 3 1 2 3 4 2 1 1

3 4 33
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (3)
2 4 3 1 2 3 4 1 2 1

4 2 3 34
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (4)
4 1 2 3 4 1 3 2 1
𝐶𝑜𝑣(𝐼3) ⊆𝐶𝑜𝑣(𝐼1) ∪𝐶𝑜𝑣(𝐼2)

2 3 35
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (5)
4 1 2 3 4 3 2 1 4 1

36
Redundancy within the Minset

First input tested guaranteed entry

Newly added inputs tend to cover same code as old inputs
Idea: fold the minset

Reconstruct it in reverse order
How  it  works:  Minset  (6)

2 37
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (7)
1 2 4 1 1 2 4 4

1 2 38
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (8)
1 2 4 1 2 4 4

2 1 39
Trail of Bits  |  CYBERDYNE: Automatic Bug-Finding at Scale  |  09.17.2016  |  trailofbits.com
How  it  works:  Minset  (9)
1 2 4 2 4 4 1
𝐶𝑜𝑣(𝐼1) ⊆𝐶𝑜𝑣(𝐼4) ∪𝐶𝑜𝑣(𝐼2)

40
Corpus distillation is fast and easy

If bottleneck, map and reduce
What they don’t tell you

What you measure is important

Different metrics, different features

Fold to compose metrics/features
How  it  works:  Minset  (10)

41
Minset is friendly

Doesn’t care who or what produced the inputs (e.g. fuzzer, symexec)
Challenge: cooperation

Make two independent bug-finding tools coordinate to discover bugs
The  gears  don’t  fit

42
Cooperation  among  friends  (1)
Symbolic executor produces an input
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes ssssss ssssss

43
Cooperation  among  friends  (2)
Input from symexec is added to minset
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

44
Cooperation  among  friends  (3)
Input from symexec seeds the fuzzer
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

45
Cooperation  among  friends  (4)
Fuzzer mutates input from symexec
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

46
Cooperation  among  friends  (5)
Mutated input is added to the minset
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

47
Cooperation  among  friends  (6)
How do we symexec a fuzzed input?
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes

48
Cooperation  among  friends  (7)
Easy way to scale:
partial symexec
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes ssssss ssssss

49
Symbolic executors are monolithic
Reason about all program paths
Somehow use theorem provers
Bugs fall out the other end…?
Challenge: make symexec cooperate in a scalable way
Some  friendships  are  a  lot  of  work

50
All input bytes are “symbols”
Fork execution when if-then-else branch depends on symbolic input
Follow feasible branches, record tested constraints down each path
How  it  works:  symbolic  execution  (1)

51
Special kind of CPU emulator

Registers/memory can hold bytes, symbols, or symbolic expressions

Instructions emulated in software

Simulates operations of instructions to work with symbols and bytes
How  it  works:  symbolic  execution  (2)

How  it  works:  symbolic  execution  (3)
52 eax = BitVec(32)   symbol ϵ [-231, 231-1]

How  it  works:  symbolic  execution  (4)
53 eax = BitVec(32)   symbol ϵ [-231, 231-1]
eax >= 0xa symbol ϵ [10, 231-1)
eax < 0xa symbol ϵ [-231, 10)

How  it  works:  symbolic  execution  (5)
54 eax = BitVec(32)   symbol ϵ [-231, 231-1]
eax >= 0xa symbol ϵ [10, 231-1)
return eax < 0xa symbol ϵ [-231, 10)
symbol ϵ [0, 10)
jump with table symbol ϵ [-231, 0)
error?!

There’s  too  many  of  them!
55

56
Symbolic executors fork a lot!
Branches, loops, branches in loops
Takes too long to get deep into the program, only finds shallow bugs
Heuristics, like coverage-guided exploration, are band-aids
Symbolic  execution  is  hard  to  scale

57
Partial symbolic execution
Jump deep into a program using a concrete input prefix
Trivially parallelizable
Run independent symbolic executors with different prefixes
Easy  way  to  scale  symbolic  execution

End  of  days 58

59
Skeleton  of  a  bug-finding  system  (1)
Terminator cyberdyne start cyberdyne analyze –pr… cyberdyne launch nukes ssssss ssssss ssssss ssssss ssssss ssssss

60
Started with simple fuzzing
Added accountability
Coverage-guided mutational fuzzing
Sets groundwork for new tools
Going from there
Minset as the mediator
Skeleton  of  a  bug-finding  system  (2)

61
Mediating with the minset
Fuzzer cooperates with anything
Symbolic executors need a bit more massaging
The path to scalability
Go for trivial parallelization
The  servos  and  the  gears

Cyberdyne  kills  bugs...now  you  can  too!
62

Let’s  chat peter@trailofbits.com
Senior Security Engineer
Peter Goodman