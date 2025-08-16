# On the Optimization of Equivalent Concurrent

Computations
Henrich Lauko
Trail of Bits
New York, NY, USA henrich.lauko@trailofbits.com
Lukáš Korenčik
Trail of Bits
New York, NY, USA lukas.korencik@trailofbits.com
Peter Goodman
Trail of Bits
New York, NY, USA peter@trailofbits.com
Abstract
In this submission, we explore the use of equality satura- tion to optimize concurrent computations. A concurrent environment gives rise to new optimization opportunities, like extracting a common concurrent subcomputation. To our knowledge, no existing equality saturation framework allows such an optimization. The challenge with concur- rent environments is that they require non-local reasoning since parallel computations are inherently unrelated and dis- joint. This submission presents a new approach to optimizing equivalent concurrent computations: extending e-graphs to capture equal concurrent computations in order to replace them with a single computation.
CCS Concepts: • Theory of computation →Equational logic and rewriting.
Keywords: e-graphs, equality saturation, concurrency
ACM Reference Format:
Henrich Lauko, Lukáš Korenčik, and Peter Goodman. 2022. On the
Optimization of Equivalent Concurrent Computations. In Proceed- ings of ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI’22). ACM, New York, NY, USA, 3 pages.
1
Introduction
We will present our approach on a real-world example of a concurrent environment – combinational circuit Figure 1. It is a circuit constructed from integer and bit-manipulating operations with no clock, so all units execute, regardless of whether or not they ought to.
The challenge of unoptimized combinational circuits is that they perform huge amounts of repeated work in their components. Nonetheless, our setup permits us to examine the problem of circuit optimization through a new lens: all of this repeated work can be thought of as happening in par- allel. This visibility over every possible computation exposes optimization opportunities to discover the optimal sharing of sub-computations within circuit execution. An alternative way of thinking about our work is that typical sequential cpu circuits contain one or more hand-crafted execution units, such as arithmetic and logical units (alus), and our optimization process invents shared alus by observing and 2022.
out mul mul add in_1 10 in_2 add 10
Figure 1. An example of an artificial arithmetic circuit con- taining two grayed components with equivalent concurrent executions that may be part of a larger circuit merging redundant computations. Our technique might also be applied to a broader set of problems, such as optimization of shared computation in threaded programs.
In general, our problem consists of multiple concurrent computations in an acyclic data-flow graph that share an identical subcomputation. In this case, we may want to op- timize these computations by identifying where the com- putations overlap and replacing these areas with a single computation (see an example in Figure 2).
A comp
B comp optimize
B1 comp
B2
C comp
A1
A2
C1
C2
Figure 2. The common sub-computation comp replaces the three concurrent components A, B, and C.
The solution we propose is to extend e-graphs [1, 2] with a special bond node, so called b-node. The b-node serves to tie together multiple concurrent expressions. Consequently,

Henrich Lauko, Lukáš Korenčik, and Peter Goodman we can unify a b-node with our desired expression to form a single equality class and utilize a generic equality saturation algorithm. When extracting an optimal solution from the final equality graph, we can treat bond nodes as generic nodes (i.e., we can pick either a b-node and all its children or any other node in the same equality class). Finally, we replace all bond nodes with adequate data-flow edges and obtain a valid circuit. We describe this process more formally in the next section.
2
E-Graph Extension
To be able to perform the optimization in Figure 2, we need to allow the e-graph to capture the information of related disjoint expressions. For this purpose, we extend the e-graphs with bonding b-nodes, which allow relating multiple nodes.
Informally, an extended e-graph consists of e-classes, as in the general case. The difference is that, in an extended e-graph, we allow an e-class to contain a mixed set of e- nodes and b-nodes at once. As in the original definition [3], e-nodes represent terms of a modeled language, and b-nodes represent semantically bonded nodes. The b-node allows one to replace all bonded nodes at once because one can treat all bonded nodes as a single node. More formally, e-nodes and b-nodes are defined as follows:
• An e-node is a function symbol paired with a list of children e-classes.
• A b-node is a unique symbol that also keeps a bond- map, a mapping between its parent and children e- classes.
Two b-nodes are considered equal when their bond-maps are identical.
This representation allows us to capture in an e-graph that some e-classes are related (e.g., in our case, they perform the same computation concurrently).
Imagine that we have three e-classes denoted as 𝑝𝑖, each with two children 𝑐𝑖𝑗. To relate these e-classes via a bond, we store the bond-map [𝑝1 →{𝑐11,𝑐12}, 𝑝3 →{𝑐21,𝑐22}, 𝑝2 →
{𝑐31,𝑐32}, ] The corresponding e-graph with bonded nodes is depicted in Figure 3.
𝑎1
𝑎2
𝑎
𝑏1
𝑏2
𝑏
𝑎1
𝑎2
𝑏1
𝑏2
𝑎
𝑏
Figure 3. Nodes 𝑎and 𝑏on the left are bonded by the b-node on the right, denoted by the center black node
We store the bond-map so that the b-node can be removed after the equality saturation process finishes. It might hap- pen that a b-node is an optimal representation of an e-class.
However, we do not want to preserve b-nodes in the final solution. Therefore, we utilize their bond-maps to disperse the b-nodes by linking parents with their children from the bond-maps. In other words, dispersion is an inverse operation to bonding.
Example 2.1. In our circuit use case, we aim to extract shared arithmetic computations (e.g., multiplications or ad- ditions). This use case is unique in how it treats operation inputs; we can synthesize a special advice input that essen- tially behaves like any input from concurrent environments.
Therefore, we can bond all concurrent multiplications re- gardless of their inputs and unify the b-node with a single multiplication with advice in place of all inputs. This opti- mization can be viewed as extracting an alu for a particular operation in the circuit. Our rewrite patterns for multiplica- tion optimization are as follows:
1. First, we perform upcasting of all multiplications with various bitwidths, bw, to the largest bitwidth of 64 bits:
(mul:bw ?a ?b) =>
(trunc:bw (mul:64 (zext:64 ?a) (zext:64 ?b)))
2. Then, we gather all 64-bit multiplications and bond them:
(let Muls (mul:64)...) => (let Bond (bond Muls...))
3. Lastly, we unify the bonded nodes with a single replace- ment multiplication that takes advice values as input:
(unify Bond (mul:64 advice:64 advice:64))
3
Limitations
Unfortunately, bonding is sensitive to dependencies of rewrite rules. Suppose you have a rule that generates a new possi- bility to extend a bond set every time. If such a rule is inter- leaved with a bonding rule, it may cause an infinite chain of b-nodes. To mitigate this issue, we utilize a suboptimal solu- tion that bonds nodes only before or after generic equality saturation.
Another challenging problem arises when candidates for bonding need to satisfy some constraints. In such a case, one needs to find a maximal satisfiable set or generate a combinatorial number of b-nodes. Again, we have opted for a suboptimal solution that eagerly finds some possible set to mitigate this problem.
4
Conclusion
In this submission, we presented ongoing work on concur- rency optimization. We challenge the locality of equality op- timization and introduce a new kind of e-graph node, called the b-node, to reason about disjoint computations. This al- lows us to apply equality saturation to a new set of problems, especially the extraction of common subcomputations in a concurrent environment. We discussed new challenges in- troduced by node bonding and its relationship to traditional equality saturation. We demonstrated our approach using a real example of circuit optimization.

On the Optimization of Equivalent Concurrent Computations 5
Acknowledgement
This research was developed with funding from the Defense
Advanced Research Projects Agency (DARPA).
The views, opinions and/or findings expressed are those of the author and should not be interpreted as representing the official views or policies of the Department of Defense or the U.S. Government.
DISTRIBUTION STATEMENT A
Approved for public release, distribution unlimited.
References
[1] Charles Gregory Nelson. 1980. Techniques for Program Verification. Ph.D.
Dissertation. Stanford University, Stanford, CA, USA. AAI8011683.
[2] Robert Nieuwenhuis and Albert Oliveras. 2005. Proof-Producing Con- gruence Closure. In Proceedings of the 16th International Conference on
Term Rewriting and Applications (Nara, Japan) (RTA’05). Springer-Verlag,
Berlin, Heidelberg, 453–468. https://doi.org/10.1007/978-3-540-32033- 3_33
[3] Max Willsey, Chandrakana Nandi, Yisu Remy Wang, Oliver Flatt,
Zachary Tatlock, and Pavel Panchekha. 2021. Egg: Fast and Exten- sible Equality Saturation. Proc. ACM Program. Lang. 5, POPL, Article 23
(jan 2021), 29 pages. https://doi.org/10.1145/3434304