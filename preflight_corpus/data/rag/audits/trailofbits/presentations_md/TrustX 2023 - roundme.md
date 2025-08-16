# 1


2
RoundMe: rounding analysis made simpler

3
Who am I?
●
Josselin Feist (@montyly)
●
Trail of Bits: trailofbits.com
○
We help developers build safer software
○
R&D focused: we use the latest program analysis techniques
○
Slither, Echidna, Tealer, Caracal, solc-select, ..
ToB Twitter list

4
Agenda
●
Rounding risks
●
How to ﬁnd and ﬁx
●
RoundMe: automated analysis

5
Why a talk about rounding?
●
Rounding is frequently ignored or an afterthought
○
Can be diﬃcult to reason with
○
But can lead to theft of funds
●
Lack of recommendations and tooling

6 101 on precision loss
●
Finite bit representation of number
●
Division truncates

7 101 on precision loss
●
Finite bit representation of number
●
Division truncates

8 101 Fixed point arithmetic
●
Decimals is ﬁxed
○ 123.456789 with a decimals of 6 -> “123456789”
○
Floating repr. equivalent: “4638387916139006731” ( IEEE 754 - 64 bits)
●
“Simple” implementations
○
DSmath, Prb-math, solmate, ..

9 101 Fixed point arithmetic
●
Multiplication loss precision, can round up or down
●
Same for pow, sqrt, …
Solmate’s  FixedPointMathLib.sol

10
Does it matter?
●
Examples:
○
JetProtocol
○
Solana Program Library (SPL)
○
Uniswap (audit)
○
Yield V2
○
PRBMath
○
Balancer

11
Case study

12
Case study: swap out
●
~ the number of token I receive (out) depends on how much I increase the second token’s supply (in)
○
Token out: what you receive
○
Token in: what you pay

13
Case study: swap out
●
Ratio is less than 1
●
~ “ratio based on how much the token supply increase”
○
More you sent, the lower the result
●
What if it rounds toward zero?

14
Case study: swap out

15
Case study: swap out
●
Token out = balance out
●
You receive all the tokens
○
(but you pay a lot)

16
Case study: swap out
●
And so?
○
“It’s just a trade”
○
“It will never happen”

17
Case study: swap out
●
And so?
○
“It’s just a trade”
○
“It will never happen”
●
Attack
○
Force the pool to be unbalanced
○
Receiving all the balance out can be proﬁtable

18
Case study: attack

19
Case study: attack

20
Case study: attack

21
Case study: attack

22
Case study: attack

23
Case study: attack

24
Case study: attack
●
Round down (↓)
○
Swap 2* 10**18 B for ~10**38
●
If round up (↑)
○
Swap 2* 10**18 B for ~10**38 - 100*10**18

25
Recommendations

26
Operation order
●
Multiply ﬁrst, divide after
○
(a * b) / c instead of a * (b / c)
●
Use slither’s divide-before-multiply detector

27
Finding rounding direction
●
Formulas can become really complex

28
Finding rounding direction
●
Start from the outer result
○
Token out => round down (↓)

29
Finding rounding direction
●
Start from the outer result
○
Token out => round down (↓)

30
Finding rounding direction
● a ** ( needs to round down (↓)
○
If a >= 1
■ to ↓ , c/d needs to ↓
○
If a < 1
■ to↓,  c/d needs to ↑
●
The rounding direction depends on the value’s context

31
Finding rounding direction
●
Right side needs to round down (↓)
○ 1 - X  needs to round down (↓)
○
X needs to round up (↑)
○ etc..

32
General recommendations
●
Analyze the arithmetics step by step
○
Always round to beneﬁt the protocol
○
Start from the outer component toward the inner components
●
Use tools
○
Fuzzing
○
RoundMe (see next)

33
General recommendations - Developers
●
Create primitives to round up / down
○ mul_up, mul_down, …
○
Make every rounding explicit
●
Rewrite the formula
○
Multiply before divide
○
Reduce number of operation
○
Avoid expression that can be positive and negative
●
Document and test known precision loss

34
Introducing roundme

35
RoundMe
●
Human-assisted rounding analyzer
○
User provides the formula
○
Roundme automatizes the step by step process
● https://github.com/crytic/roundme
○
Rust
●
Early stage
○ 6 rounding rules - more to come
○
Only unsigned ﬁxed point integers

36
RoundMe

37
RoundMe

38
RoundMe
●
Generate reports in latex/PDF

39
Conclusion

40
Conclusion
●
Pay attention to the roundings
●
Make all roundings explicit
○ https://github.com/crytic/roundme will help
●
Use a fuzzer
●
Interested in fuzzing?
○
“How to fuzz like a pro” at 6pm (sponsor zone)
○
Invariant as a service