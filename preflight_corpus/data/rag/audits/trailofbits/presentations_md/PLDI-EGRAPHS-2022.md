# 1


2
On the Optimization of
Equivalent Concurrent Computations*
Henrich Lauko, Lukáš Korenčik & Peter Goodman
*Research funded by DARPA SIEVE program.

3
On the Optimization of
Equivalent Concurrent Computations
Common Subexpressions*
Henrich Lauko, Lukáš Korenčik & Peter Goodman
*Research funded by DARPA SIEVE program.

4
Problem Statement f(e(a₁, a₂)) ∧ h(e(b₁, b₂))
↓ f(g(a₁, a₂)) ∧ h(g(b₁, b₂)) ∧ g(c₁, c₂) = e(c₁, c₂)
●
Find common subexpressions independent of their arguments
●
Factor out all of them or none to a separate function

5
Pattern Extraction Example v₁ = a₁ × (a₂ × 2) ∧ v₂ = b₁ × (b₂ << 1)
↓ extract pattern of form c₁ × (c₂ × 2)
↓ v₁ = g(a₁, a₂) ∧ v₂ = g(b₁, b₂) ∧ g(c₁, c₂) = c₁ × (c₂ × 2)

6
Applications
●
Program refactoring
●
Term simpliﬁcation
Optimization of arithmetic circuits for ZK proofs
●
Application targets optimization of circuits for the ZK proofs
●
Extraction of common arithmetic logic units from generated circuit

7
Problems to Solve 1.
Keep the equality saturation algorithm 2.
Extend  the ematch to ﬁnd common subexpressions 3.
Represent subexpression relation in the e-graph 4.
Extract refactored structure

8 1. Apply rewrite rules as usual
Original formula: v₁ = a₁ × (a₂ × 2) ∧ v₂ = b₁ × (b₂ << 1)
Rewrite rule:   ? << 1 → ? × 2
× a₁ a₂ 2
×
= v₁ b₁ 1 b₂
×
= v₂
<<
→
× a₁ a₂ 2
×
= v₁ b₁ 1 b₂
×
= v₂
<<
×

9 2. Find common subexpression
●
New ematch rule:  (let E (?₁ × (?₂ × 2))) (match E…) →
●
Eagerly match all patterns of a given form
× a₁ a₂ 2
×
= v₁ b₁ 1 b₂
×
= v₂
<<
×

10 3. Relate common subexpressions
●
Extend E-GRAPH by a new type of node – b-node (bond node)
●
Represents relation between multiple e-classes
●
Keeps relation between parent and children e-classes
●
New rule action:  (let E (?₁ × (?₂ × 2))) (match E…) → (bond E…)
bond
×
= v₁
×
= v₂
×
= v₁
×
= v₂
→

11
Bond lowering bond
×
= v₁
×
= v₂ g
×
= v₁
×
= v₂
= v₁ g
= v₂

12
Bond lowering bond
×
= v₁
×
= v₂ g
×
= v₁
×
= v₂ g
= v₁ g
= v₂ a₁ b₂ a₂ b₁

13 c₁ c₂
The ﬁnal bonding rule application
(let E (?₁ × (?₂ × 2))) (match E… with vars ?₁ ?₂)  →
((let G (g(c₁, c₂) = c₁ × (c₂ × 2))) (bond E… with g(?₁ ,?₂)))
× a₁ a₂ 2
×
= v₁ b₁ 1 b₂
×
= v₂
<<
×
× a₁ a₂ 2
×
= v₁ b₁ 1 b₂
×
= v₂
<<
×
= g bond g(?₁ ?₂)
→

14
Experiments
Benchmark
Circuit Size
AND Gates
Multiplications
UNOPTIMIZED
EQSAT
UNOPTIMIZED
EQSAT
UNOPTIMIZED
EQSAT x86 mul-forms 94,286 71,102 42,591 31,043 25 5 3D toolkit 124,795 97,881 61,783 49,590 12 2
Router sim.
109,596 86,585 55,242 40,757 13 2
LAN simulator 126,657 104,184 63,430 49,232 19 3

15
Implementation
●
Inspired by egg
●
Soon to be released as C++ library:
https://github.com/lifting-bits/eqsat
●
Extends the language of patterns and e-graph modiﬁers
●
Used as optimization ZK circuit compiler in the tool circuitous

16
Implementation
●
Inspired by egg
●
Soon to be released as C++ library:
https://github.com/lifting-bits/eqsat
●
Extends the language of patterns and e-graph modiﬁers
●
Used as optimization ZK circuit compiler in the tool circuitous
Thank You