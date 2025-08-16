# 1


2
Test Your Tests
The Dos and Don’ts of testing
Blockchain Team
@trailofbits phaze
@lovethewired

3
Overview
●
Motivation for topic
●
Examples: Testing shortcomings
●
Exploring various testing strategies
●
Takeaways

4
The Role of Testing
●
Fault identiﬁcation
●
Invariant validation
●
Spec adherence
●
Build up conﬁdence and trust in performance
●
Guarding code functionality: Regression tests
But: No testing method is foolproof.
Testing is an ongoing process of reﬁnement, not a ﬁnal endpoint!

5
Motivation for Topic
●
Reﬂections on past shortcomings
●
Improving development and testing process
●
Driver for becoming security-oriented

6
Improving ERC721A

7
ERC721A Optimization

8
ERC721A Optimization
●
Save gas on all future transfers
●
Store boolean nextTokenDataSet in ownership slot
●
Only touch subsequent token data if !nextTokenDataSet

9
Development & Testing Approach
●
Test-driven
●
“Sufficient testing will uncover ﬂaws”
●
Quality through quantity
But: Lost sight of the bigger picture

10
Unit-Testing Functionality

11
Unit-Testing Functionality

12
Unit-Testing Functionality
How??!

13
Apply Patch and Test
Fixed!!
All tests pass…

14
Apply Patch and Test
Fixed!!
All tests pass…
Fixed!! (Not quite)
All tests pass…

15
What Went Wrong?
●
Lacking systematic testing approach and structure

16
What Went Wrong?
●
Lacking systematic testing approach and structure
●
Missing important edge-cases

17
What Went Wrong?
●
Lacking systematic testing approach and structure
●
Missing important edge-cases
●
Testing multiple things at once

18
What Went Wrong?
●
Lacking systematic testing approach and structure
●
Missing important edge-cases
●
Testing multiple things at once
●
Lacking expressive and meaningful fuzz tests
○
Multiple transfers
○
Random ids
○
Arbitrary actors

19
What Went Wrong?
●
Lacking systematic testing approach and structure
●
Missing important edge-cases
●
Testing multiple things at once
●
Lacking expressive and meaningful fuzz tests
○
Multiple transfers
○
Random ids
○
Arbitrary actors 100% code line & branch coverage != 100% state coverage

20
Good Testing is Hard…

21
Shortcomings Exempliﬁed:
Testing WAD Conversions

22
Testing WAD Conversions

23
Testing WAD Conversions

24
Testing WAD Conversions
Testing WAD Conversions (DON’T)

25
Testing WAD Conversions
Testing WAD Conversions (DON’T)

26
Testing WAD Conversions
Testing WAD Conversions (DON’T)

27
Testing WAD Conversions
●
Know your tool!
Testing WAD Conversions (DON’T)

28
Testing WAD Conversions
●
Know your tool!
●
Don’t solely rely on one type of tests
Testing WAD Conversions (DON’T)

29
Test WAD Conversions (DO)
○
Split tests by outcome/behavior
●
Know your tool!
●
Don’t solely rely on one type of tests
●
Restructure tests

30
Test WAD Conversions (DO)
○
Split tests by outcome/behavior
○
Ensure coverage around boundary points
●
Know your tool!
●
Don’t solely rely on one type of tests
●
Restructure tests

31
Test WAD Conversions (DO)
○
Split tests by outcome/behavior
○
Ensure coverage around boundary points
○
Reduce complex decision trees
●
Know your tool!
●
Don’t solely rely on one type of tests
●
Restructure tests

32
Test WAD Conversions (DO)
○
Split tests by outcome/behavior
○
Ensure coverage around boundary points
○
Reduce complex decision trees
○
Expect speciﬁc revert
●
Know your tool!
●
Don’t solely rely on one type of tests
●
Restructure tests

33
Shortcomings Exempliﬁed:
Testing WAD Multiplication

34
Testing WAD Multiplication
Testing WAD Multiplication (DON’T)
&&
&&

35
Testing WAD Multiplication

36
Testing WAD Multiplication

37
Testing WAD Multiplication
Testing WAD Multiplication (DON’T)

38
Testing WAD Multiplication
Testing WAD Multiplication (DON’T)
&&
&&

39
Exploring Various Testing Strategies (DO)
●
Include unit tests for special cases

40
Exploring Various Testing Strategies (DO)
●
Include unit tests for special cases
●
Fuzz test multiple properties

41
Exploring Various Testing Strategies (DO)
●
Include unit tests for special cases
●
Fuzz test multiple properties
●
Re-implement logic from a different angle

42
Exploring Various Testing Strategies (DO)
●
Include unit tests for special cases
●
Fuzz test multiple properties
●
Re-implement logic from a different angle
●
Use differential fuzzing

43
Key Takeaways
●
Treat your tests as production code

44
Key Takeaways
●
Treat your tests as production code
●
Understand limitations of testing and tooling

45
Key Takeaways
●
Treat your tests as production code
●
Understand limitations of testing and tooling
●
Explore different testing strategies and techniques

46
Key Takeaways
●
Treat your tests as production code
●
Understand limitations of testing and tooling
●
Explore different testing strategies and techniques
●
Examine assumptions, preconditions, and conclusions of tests

47
Key Takeaways
●
Treat your tests as production code
●
Understand limitations of testing and tooling
●
Explore different testing strategies and techniques
●
Examine assumptions, preconditions, and conclusions of tests
●
Test your tests

48
Oﬀensive Testing
Case Study:
Primitive Finance - Hyper

49
Primitive Finance - Hyper
●
CFMM with time-dependent curves (options-like trading)
●
Central pool balance accounting and batch swapping functionality
●
Non-trivial function approximations
●
Use of assembly and inconsistent rounding methods
=> Fuzz the swap function

50
Fuzz Test:
Swapping
Back
And Forth

51

52
Reﬁning the Testing
Strategy
●
Address all reverts and bound parameters

53
Reﬁning the Testing
Strategy
●
Address all reverts and bound parameters
●
Sanity check setup and improve coverage insight

54
Reﬁning the Testing
Strategy
●
Address all reverts and bound parameters
●
Sanity check setup and improve coverage insight
●
Question assumptions and conclusions in testing

55
Takeaway
●
Offensive testing requires a persistent, dynamic approach
●
Aim to actively ﬁnd potential cracks rather than just conﬁrming robustness
●
Question assumptions and validate your setup

56
Full-length blog post lovethewired.github.io/blog/2023/test-your-tests
Stay in Touch 56 phaze
@lovethewired
Questions?