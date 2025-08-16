# Weak Fiat-Shamir Attacks on

Modern Proof Systems
Quang Dao
Carnegie Mellon University
Jim Miller
Trail of Bits
Opal Wright
Trail of Bits
Paul Grubbs
University of Michigan
Abstract—A ﬂurry of excitement amongst researchers and practitioners has produced modern proof systems built using novel technical ideas and seeing rapid deployment, especially in cryptocurrencies. Most of these modern proof systems use the
Fiat-Shamir (F-S) transformation, a seminal method of removing interaction from a protocol with a public-coin veriﬁer. Some prior work has shown that incorrectly applying F-S (i.e., using the so-called “weak” F-S transformation) can lead to breaks of classic protocols like Schnorr’s discrete log proof; however, little is known about the risks of applying F-S incorrectly for modern proof systems seeing deployment today.
In this paper, we ﬁll this knowledge gap via a broad theoretical and practical study of F-S in implementations of modern proof systems. We perform a survey of open-source implementations and ﬁnd 36 weak F-S implementations affecting 12 different proof systems. For four of these—Bulletproofs, Plonk, Spartan, and Wesolowski’s VDF—we develop novel knowledge soundness attacks accompanied by rigorous proofs of their efﬁcacy. We perform case studies of applications that use vulnerable im- plementations, and demonstrate that a weak F-S vulnerability could have led to the creation of unlimited currency in a private blockchain protocol. Finally, we discuss possible mitigations and takeaways for academics and practitioners.
I. INTRODUCTION
Proof systems—cryptographic protocols in which a prover convinces a veriﬁer of the truth of some public statement— have seen an explosion of interest from academic researchers and practitioners. The resulting modern constructions, in par- ticular those enjoying an additional zero-knowledge property, are being widely deployed in blockchain and cryptocurrency settings
[5], [26], [55], [66], [68], [77], [80], [84], [94].
A critical security property shared by all proof systems is soundness—roughly, this guarantees a prover can only convince a veriﬁer of the truth of actually true statements.
Applications like cryptocurrencies rely on soundness to, e.g., prevent attackers from creating money out of thin air.
Most proof systems used in practice are non-interactive:
they consist of a single message from the prover to the veriﬁer. Though built using novel and varied technical tools, most modern non-interactive proof systems share a common design pattern: ﬁrst, build and analyze an interactive protocol where the veriﬁer’s messages consist solely of random values
(i.e., it is public-coin), then compile it to a non-interactive protocol using the Fiat-Shamir (F-S) transformation [35]. The transformation works by replacing the public-coin veriﬁer with a hash function: each veriﬁer challenge is derived by the prover by hashing the transcript of the prover’s messages thus far. A standard result [76] shows that if done correctly, this transformation preserves security if the hash function is modelled as a random oracle [9].
Unfortunately, it is surprisingly easy to implement F-S incorrectly. An important subtlety, which is not often dis- cussed, is whether it is necessary to include public information, such as the statement, in the transcript. The version of the transformation where the public information is not hashed is usually called weak F-S; if the public information is hashed, this is usually called strong F-S (or simply F-S). (See Figure 1 for an example of the differences for Schnorr’s discrete log proof.) Intuitively, hashing public information ensures that the proof depends on the public information, preventing a malicious prover from adaptively choosing it during, or even after, generating a proof. Prior work has shown that many classic proof systems, such as Schnorr [79] and Chaum-
Pedersen [25], cannot be adaptively sound if weak F-S is used; further, this lack of adaptive soundness breaks applications that use these proof systems. For example, an adaptive soundness attack on Chaum-Pedersen was shown to compromise the voting protocols Helios [13] and sVote [46].
Despite these important prior works, little is known about the risks of weak F-S for the modern proof systems being used in practice today. This gap in our knowledge is serious for at least two reasons. First, modern proof systems are built using newer and arguably more complex technical tools than classic schemes, meaning prior attacks do not easily translate.
Second, since more proof systems are being deployed than ever before, the potential attack surface is much larger, and the consequences of attacks could be more severe. Thus, it is crucial to understand whether vulnerable code exists and how it could be exploited.
Our contributions. In this paper, we ﬁll this gap with a broad study of the risks of weak F-S in modern proof systems. Our main contributions are fourfold: ﬁrst, we perform an extensive survey of over 75 open-source proof system implementations that use F-S, uncovering 36 weak F-S implementations across 12 different proof systems. Second, for four of the proof systems with at least one weak F-S implementation, we construct, analyze, and implement novel knowledge soundness attacks. Third, we perform case studies of how these proof systems are used in applications, to understand whether our weak F-S attacks would have led to breaks of real systems.
One case study shows that it would have been possible to create unlimited money in the Dusk Network testnet [92].

Interactive Schnorr protocol
P
V a
$←F
A = ga c c
$←F∗ z = a + cx z gz
?= A · Xc
Strong / Weak Fiat-Shamir transformation
P
V a
$←F, A = ga c = H

G, g, X , A
 z = a + cx
π = (A, z)
c = H

G, g, X , A
 gz
?= A · Xc
Attack against weak Fiat-Shamir
P
V
A
$←G c = H(A)
z
$←F
π = (A, z)
Proof veriﬁes for X = (gz/A)1/c.
Fig. 1: Example weak Fiat-Shamir attack against Schnorr proofs for relation {((G, g), X; x) | X = gx}
Finally, we explore the landscape of mitigations, identifying design criteria and studying how proposals would apply to
Merlin, a widely-used Rust library for implementing F-S.
Example of F-S for Schnorr.
Before describing our contri- butions in more detail, we will explain the basics of applying
F-S to the classic Schnorr protocol. The left-hand side of
Figure 1 describes the three moves of the interactive protocol for proving knowledge of the discrete log x of an element
X in a prime-order group G with generator g. For Schnorr, the group description and generator are examples of public parameters that deﬁne the set of provable statements. The group element X is the public input about which the prover is generating a proof, and the value x is the witness the prover wishes to hide.
The middle box of Figure 1 depicts the two ways of applying F-S to Schnorr. In weak F-S, only the prover’s ﬁrst message A is hashed. In strong F-S, the hash additionally includes the public parameters and public input. Finally, the right box of the ﬁgure depicts the adaptive attack (due to [13])
that is possible if weak F-S is used: by computing the public input X as a function of a randomly-generated proof, a malicious prover can convince a veriﬁer without knowing the witness. Intuitively, strong F-S prevents this because the public input X affects the derived challenge c.
Implementation survey.
Table I summarizes our imple- mentation survey of GitHub repositories containing imple- mentations of proof systems. We used a combination of manual search and automated dependency checking to ﬁnd the repositories. Overall, we identiﬁed at least 75 repositories that attempted to implement a non-interactive proof system using F-S. Of those, 36 used weak F-S. (For space reasons, our table lists only the 54 repos of the 12 proof systems that had at least one weak F-S implementation.) After a preliminary public disclosure [65] of some of our results, many repositories were ﬁxed and are marked as such. The main takeaway of our survey is that misuses of F-S are very widespread, and that even production-quality code written by experts—who in some cases are the creators of the proof system—implemented weak
F-S. Interestingly, we found several repositories that made even more severe mistakes in implementing F-S; Section VIII contains further discussion of these cases. We followed re- sponsible disclosure best practices in informing all repository owners about the vulnerabilities.
New attacks.
For four proof systems with at least one vulnerable implementation—Bulletproofs [22], Plonk [37],
Spartan [82], and Wesolowski’s VDF [90]—we show that using weak F-S leads to attacks on their soundness when the prover can choose the public inputs adaptively, as a function of the proof. Importantly, our results do not invalidate the security proofs for these schemes—when given explicitly, soundness proofs for non-interactive, weak F-S variants of these protocols provide only non-adaptive security.
In Section IV, we show an attack on the (adaptive) knowl- edge soundness of the Bulletproofs aggregate range proof, which would allow crafting Pedersen commitments to values that lie outside the speciﬁc range with high probability. In Sec- tions V and VI, we give our attacks on Plonk and Spartan, two proofs systems that prove NP-complete constraint satisfaction problems and are built using the recent polynomial interactive oracle proofs (IOPs) paradigm [23], [27]. Both work by having the malicious prover choose one of the public inputs to the constraint system as a function of the proof; the public input is chosen to ensure the veriﬁcation equation—in both cases, a polynomial identity—holds. Finally, in Section VII we give our attack on Wesolowski’s VDF. Our attack allows a malicious prover to craft a proof π for a small delay parameter t, then compute a much larger parameter T ≫t for which π is valid. Thus, the prover can claim to have done T sequential squarings while having done only t. We implement our attacks for Bulletproofs, Plonk, and Wesolowski’s VDF, and experimentally verify that forged proofs can be generated quickly: for example, our Bulletproofs attack can generate a forged range proof with 32-bit range in 86 milliseconds.
Aside from the attacks themselves, an important novelty of our work is that we rigorously prove all four attacks break a well-speciﬁed soundness property of the proof system. For
Bulletproofs, Plonk, and Spartan, we prove our attacks violate adaptive knowledge soundness via a meta-reduction argument:
roughly, we prove that if an extractor exists for our malicious prover, this extractor could be used to break a cryptographic hardness assumption like discrete log. This technique is similar to the one used in prior work [13], but applying it here

Proof System
Codebase
Weak F-S?
Bulletproofs [22]
bp-go [87]
 bulletproof-js [2]
 simple-bulletproof-js [83]

BulletproofSwift [20]
 python-bulletproofs [78]
 adjoint-bulletproofs [3]
 zkSen [98]
 incognito-chain [51]
o encoins-bulletproofs [33]
o
ZenGo-X [96]
o zkrp [52]
o ckb-zkp [81]
o bulletproofsrb [21]
o monero [68]
 dalek-bulletproofs [29]
 secp256k1-zkp [75]
 bulletproofs-ocaml [74]
 tari-project [85]

Litecoin [59]

Grin [44]

Bulletproofs variant [40]
dalek-bulletproofs [29]
o cpp-lwevss [60]

Sonic [61]
ebfull-sonic [18]
 lx-sonic [58]
 iohk-sonic [53]
 adjoint-sonic [4]

Schnorr [79]
noknow-python [7]

Proof System
Codebase
Weak F-S?
Plonk [37]
anoma-plonkup [6]
 gnark [17]
o dusk-network [31]
o snarkjs [50]
o
ZK-Garage [97]
o plonky [67]
 ckb-zkp [81]
 halo2 [93]
 o1-labs [71]
 jellyﬁsh [34]
 matter-labs [62]
 aztec-connect [8]

Wesolowski’s
VDF [90]
0xProject [1]

Chia [69]

Harmony [47]

POA Network [70]

IOTA Ledger [54]
 master-thesis-ELTE [48]

Hyrax [89]
ckb-zkp [81]
o hyraxZK [49]

Spartan [82]
Spartan [64]
o ckb-zkp [81]
o
Libra [91]
ckb-zkp [81]
o
Brakedown [43]
Brakedown [19]

Nova [57]
Nova [63]
o
Gemini [16]
arkworks-gemini [38]
o
Girault [42]
zk-paillier [95]
o
TABLE I: Implementations surveyed. We include every proof system with at least one vulnerable implementation, and survey all implementations for each one (except classic protocols like Schnorr and Girault). o = has been ﬁxed as of May 15, 2023.
requires new technical ideas; e.g., for Plonk and Spartan, a trivial extractor may exist for an “easy” constraint system. Our proofs for Plonk and Spartan show that knowledge soundness breaks as soon as the relation satisﬁes a slight strengthening of worst-case hardness; our analysis here may be of independent interest.
Application case studies.
Dozen of implementations of the four proof systems we examined are vulnerable to these attacks, at least in theory. However, this does not necessarily mean the applications that use them are broken by these attacks—it could be that external application constraints pre- vent exploiting weak F-S. To answer this question, we next look at the applications that use vulnerable proof systems.
Here our ﬁndings are more mixed. While we identiﬁed one ap- plication that is unambiguously broken by a weak F-S attack— we show in Section V-C that it would have been possible to create unlimited money in the Dusk Network testnet—our other attacks do not appear to break applications. For Spartan, we were not able to identify any vulnerable applications. For
Bulletproofs, the implementations we found that were actually used in real applications were not vulnerable. Nevertheless, we give a “counterfactual” case study of the Mimblewimble protocol [55] to determine if our weak F-S attack could have led to an application break; we ﬁnd that creating unlimited money would have been possible. For Wesolowski’s VDF, constraints on the size of the delay parameter prevent our malicious proofs from breaking some applications, like the
Chia blockchain, but we found at least one case (the 0x VDF veriﬁer smart contract) where no constraints exist.
Mitigations.
Finally, in Section IX we discuss how to mit- igate weak F-S attacks. We explore creating tools that can detect weak F-S vulnerabilities in existing code, and also study how existing tools, such as the Merlin library for F-S [28], could be modiﬁed to make them harder to misuse. (Several vulnerable implementations we found used Merlin.) To detect weak F-S implementations, we describe how information-
ﬂow analysis could be used to ensure variables in common between the prover and veriﬁer are hashed in the transcript.
To make it harder to implement F-S incorrectly, we suggest modifying the Merlin API to force programmers to initialize protocol transcripts with public inputs, or to specify all F-
S inputs and challenges upon initialization of the transcript.
These approaches have some drawbacks, which we discuss in
Section IX-A. We leave an implementation and evaluation of these tools to future work.
A. Related Works
This paper extends and generalizes our preliminary results, which were posted in a series of blog posts [65]. Compared to the blog posts, we perform a more comprehensive imple- mentation survey which uncover more vulnerable implemen- tations, give attacks for two more proof systems (Spartan and

Wesolowski’s VDF), provide rigorous proofs that our attacks break security, and give new case studies of practical impacts.
Our work is about the Fiat-Shamir transformation, originally given in [35]. Our work also applies to variants of the transformation for multi-round protocols, such as the BCS transformation of [11]. We did not study protocols that use quantum variants of F-S, such as the Unruh’s transforma- tion [86]; our attacks should extend to these, but we leave the details to future work. Our attacks do not apply to proof systems that use only structured reference strings for non- interactivity, such as Groth16 [45].
Our work is indebted to the seminal paper on weak F-S by
Bernhard et al. [13], which highlighted this issue and gave attacks against Schnorr and Chaum-Pedersen. A key followup to [13] that uncovered other weak F-S attacks on similar sigma protocols, that also break voting systems, is [46]. As discussed above, our work examines weak F-S in the context of proof systems built in the last decade or so, which use new and very different building blocks from older schemes:
these include non-constant-round interactive protocols, such as Bulletproofs. We use a similar meta-reduction technique to [13] for analyzing our attacks, though heavily modiﬁed to account for the proof systems’ ability to prove more complex
(even NP-complete) relations.
Our work shows that the four non-interactive proof systems we studied are not sound in an adaptive setting. There has been some work ﬁnding different kinds of soundness bugs in proof systems; these bugs are caused by faulty proofs and apply even in the non-adaptive soundness setting. For example, [36]
found a soundness bug in the BCTV SNARK construction, and [72] found a soundness bug in vnTinyRAM. Our attacks do not stem from faulty proofs, but rather from a gap between what the proofs guarantee and the security that applications require.
II. PRELIMINARIES
A. Notation
We denote the security parameter by λ, and a negligible function in λ by negl(λ). Our relations, cryptographic objects, and adversaries all depend on λ; we often omit this depen- dency. We use game-based security deﬁnitions [10]; here a game GA1,...,An
S1,...,Sm denotes a run of parties A1, . . . , An on a pre-speciﬁed set of procedures given by S1, . . . , Sm, returning a bit b ∈{0, 1}. We denote by Pr h
GA1,...,An
S1,...,Sm i the probability, over the random coins used by all parties and the game itself, that the game’s output is 1.
We denote by G a group, either of prime order p or of unknown order, F a ﬁnite ﬁeld of prime order p, and use x
$←F to denote uniformly sampling an element in F. We denote vectors by boldface x ∈Fn, the inner product of two vectors x, y ∈Fn by ⟨x, y⟩, the element-wise product by x ◦y, subvectors by x[i:j] = (xi, xi+1, . . . , xj), vector subscripts by xa = (xa1, . . . , xam) where a ∈[n]m, and multi-exponentiation between g ∈Gn and x ∈Fn by gx.
For y ∈F, we denote yn = (1, y, . . . , yn−1). We write
Game DLA
G (λ)
h
$←G \ {g} a ←A(g, h)
return (ga = h)
Game DL-RELA
G,n(λ)
g1, . . . , gn
$←G
(a1, . . . , an) ←A(g1, . . . , gn)
return n
Y i=1 gai i
= 1
!
∧((a1, . . . , an) ̸= 0n)
Fig. 2: Games for Discrete Log p(X) ∈F<d[X] to denote a (univariate) polynomial of degree less than d, and p(X) ∈F[µ] to denote a multilinear polynomial in µ variables.
Lagrange basis.
Given a ﬁnite ﬁeld F and a subgroup H =
⟨ω⟩of order n, for every i ∈[n] we can deﬁne the Lagrange polynomial Li(X) to be the unique polynomial of degree n−1 that satisﬁes Li(ωi) = 1 and Li(ωj) = 0 for j ̸= i. For any vector x ∈Fn, there exists a unique polynomial p(X) of degree at most n −1 that satisﬁes p(ωi) = xi; we have the identity p(X) = Pn i=1 xi · Li(X).
Multilinear extension.
Given g : {0, 1}µ →F, we deﬁne eg(X1, . . . , Xµ) ∈F[X1, . . . , Xµ]
to be the unique multilinear polynomial with evaluation eg(y) = g(y) for all y ∈{0, 1}µ, called the multilinear extension of g. We have the identity g(X1, . . . , Xµ) =
X y∈{0,1}µ g(y) · eeq(X, y), where eq(X, Y ) =
µ
Y i=1
(Xi · Yi + (1 −Xi) · (1 −Yi)).
Here eeq(X, Y ) is the analogue of the Lagrange basis in the multilinear setting; we have eq(x, x) = 1 and eq(x, y) = 0 if x ̸= y.
B. Discrete Log Assumptions
Let G be a prime-order group (depending on λ), with generator g and scalar ﬁeld F.
Deﬁnition 1: We say that the discrete log (DL) assumption holds for G if for all PPT adversaries A, the following proba- bility is negligible in λ:
AdvDL
G (A) := Pr h
DLA
G(λ)
i
.
We say that the discrete log relation (DL-REL) assumption holds for G if for all PPT adversaries A and all n ∈N, the following probability is negligible in λ:
AdvDL-REL
G,n
(A) := Pr h
DL-RELA
G,n(λ)
i
.
The two discrete log assumptions are tightly related [41].
Lemma 1:
For every PPT adversary A against DL-REL, there exists a PPT adversary B against DL, nearly as efﬁcient

as A, such that
AdvDL-REL
G,n
(A) ≤AdvDL
G (B) + 1
|F|.
C. Interactive Arguments
An interactive argument for an
NP relation
R is a tuple of PPT algorithms Π
=
(Setup, P, V). Here
Setup(1λ) →pp produces public parameters pp given a security parameter 1λ, and ⟨P(w), V⟩(pp, x) →{0, 1} is an interactive protocol whereby the prover P, holding a witness w, interacts with the veriﬁer V on common input (pp, x) to convince V that (x, w) ∈R. At the end, V outputs a bit to accept or reject the proof.
We require that interactive arguments satisfy complete- ness and knowledge soundness. Completeness states that for every pp ←Setup(1λ) and (x, w) ∈R, we have
⟨P(w), V⟩(pp, x) →1. Knowledge soundness states that there exists an expected polynomial time extractor E such that for any stateful PPT adversary P∗, the probability that P∗ manages to convince V on an input x chosen by P∗, yet E cannot ﬁnd a witness w for x, is negligible. Here E gets black- box access to each of the next-message functions of P∗in the interactive protocol.
The interactive arguments we consider are public-coin, meaning that in each round the veriﬁer V samples its mes- sage uniformly at random from some challenge space. Such protocols have a (r +1)-round format where P sends the ﬁrst and last messages. In particular, the transcript is of the form
(a1, c1, . . . , ar, cr, ar+1), where (a1, . . . , ar+1) are messages sent by P and (c1, . . . , cr) are challenges sent by V.
D. Non-Interactive Arguments in the ROM
The Fiat-Shamir transformation (see Section II-E) is often used to compile public-coin interactive arguments into their non-interactive versions in the random oracle model (ROM)
[9]. We denote the random oracle by H : {0, 1}∗→{0, 1}∗.
Deﬁnition 2:
A non-interactive argument of knowledge
(NARK) in the ROM for a NP relation R is a tuple of PPT algorithms Π = (Setup, P, V), with P, V having black-box access to a random oracle H, with the following syntax:
• Setup(1λ) →pp : generates the public parameters for R,
• PH(pp, x, w) →π : generates a proof,
• VH(pp, x, π) →{0, 1} : checks whether a proof π is valid with respect to pp and input x.
We require NARKs to satisfy the following properties.
• Completeness. For every (x, w) ∈R,
Pr
"
VH(pp, x, π) = 1 :
pp ←Setup(1λ)
π ←PH(pp, x, w)
#
= 1.
• Knowledge soundness. For every PPT adversary P∗, there exists an extractor E running in expected polynomial time such that the following probability is negl(λ):
AdvKS
Π,R(E, P∗) :=

Pr[KSP∗ 0,Π(λ)] −Pr[KSE,P∗ 1,Π,R(λ)]

.
The KS games are deﬁned in Figure 3.
Game KSP∗ 0,Π(λ)
pp ←Setup(1λ)
(x, π) ←(P∗)H(pp)
b ←VH(pp, x, π)
return b
Game KSE,P∗ 1,Π,R(λ)
pp ←Setup(1λ)
(x, π) ←(P∗)H(pp)
b ←VH(pp, x, π)
w ←E(P∗, pp, x, π)
return b ∧(x, w) ∈R
Fig. 3: Knowledge soundness security games. Here the ex- tractor E is given the description of P∗; in particular, it may rewind P∗and reprogram the random oracle H.
We note that our knowledge soundness deﬁnition is both non- black-box, where the extractor may depend on (the code of)
the malicious prover P∗, and adaptive, meaning the malicious prover P∗can choose the pair (x, π) at the same time.
The adaptive strengthening is often necessary in practice, as evidenced by our case studies (e.g., see Section IV-C). We also discuss the situation where P∗may also inﬂuence the public parameters pp in Section VIII. On the other hand, non-black- box extraction is a weaker extractability requirement [24]1, including extracting using non-falsiﬁable knowledge assump- tions [12], [39], [45], [73]. Looking ahead, our results for
Plonk and Spartan ruling out non-black-box extraction for
“sufﬁciently hard” relations will also rule out black-box ex- traction.
E. The Fiat-Shamir Transformation
We deﬁne both variants (weak and strong) of the Fiat-
Shamir transformation.
Deﬁnition 3:
Let Π
=
(Setup, P, V) be a public- coin interactive argument with transcript of the form tr =
(a1, c1, . . . , ar, cr, ar+1). The strong Fiat-Shamir transforma- tion turns Π into a non-interactive argument ΠsFS where:
• SetupsFS(1λ) is the same as Setup(1λ),
• the prover PsFS, on input (pp, x, w), invokes P(pp, x, w), and instead of asking the veriﬁer for challenge ci in round i, queries the random oracle to get ci ←H(pp, x, a1, . . . , ai)
∀i = 1, . . . , r.
PsFS then outputs the proof π = (a1, . . . , ar, ar+1).
• the veriﬁer VsFS, on input (pp, x, π), derives challenges ci by querying the random oracle as above, then runs
V(pp, x) on transcript (a1, c1, . . . , ar, cr, ar+1) and out- puts what V outputs.
The weak Fiat-Shamir transformation is similar, except that we omit the public parameters pp and the input x from the hash, so that ci = H(a1, . . . , ai)
∀i = 1, . . . , r.
We denote the weak Fiat-Shamir transformed argument by
ΠwFS = (Setup, PwFS, VwFS).
1In contrast, black-box extraction requires a single extractor that works for all malicious provers, and may only rely on its input-output behavior.

F. Polynomial Interactive Oracle Proofs
We describe the formalism of polynomial IOPs [23], [27]
that underlies Plonk and Spartan.
Polynomial IOP.
A (public-coin) polynomial IOP for a
NP relation R (depending on a ﬁeld F) is a tuple of PPT algorithms (I, P, V) with the following protocol format. In the preprocessing phase, the indexer I(F, R) outputs a list of preprocessed polynomial oracles i. In the interaction phase, the prover P is given (i, x, w) and the veriﬁer V is given
(i, x). In each round i, P sends a list of polynomial oracles pi, and V responds with a random challenge ci. In the query phase, V may query any of the polynomial oracle p, obtained as part of i or pi for some round i, at any evaluation point z to get the corresponding evaluation p(z). V then outputs accept or reject. Completeness and knowledge soundness for polynomial
IOPs are deﬁned similarly to interactive arguments; see [27]
for full deﬁnitions.
Polynomial Commitment Scheme.
A polynomial commit- ment scheme (PC) is a tuple of PPT algorithms PC =
(Setup, Commit) and an interactive argument Open with the following syntax:
• Setup(1λ, µ, D) →pp : sets up public parameters pp given number of variables µ and maximum individual degree D,
• Commit(pp, p; ω) →[p] : outputs a commitment [p] to a polynomial p ∈F≤D[X1, . . . , Xµ], using randomness ω,
• Open := ⟨PPC(p, ω), VPC⟩(pp, [p], x, v) →{0, 1} is a public-coin interactive argument for the relation p(x) = v and [p] = Commit(pp, p; ω).
We consider two types of PCs in our paper, one for univariate polynomials (µ = 1) and one for multilinear polynomials
(D = 1). We deﬁne completeness and knowledge soundness of PC to be the corresponding property for Open.
Compiling to non-interactive arguments.
Any polynomial
IOP can be composed with any polynomial commitment scheme PC to form a public-coin interactive argument Π =
(Setup, P, V), which can then be turned non-interactive via
Fiat-Shamir. The former step is done as follows:
• Setup(1λ) : runs PC.Setup(1λ) →ppPC, I(F, R) →i, and PC.Commit(ppPC, i) →[i] for all i ∈i. Outputs pp = (ppPC, ([i])i∈i).
• ⟨P(w), V⟩(pp, x) : emulate the interaction phase of the polynomial IOP, with P sending a polynomial commit- ment [p] instead of an oracle for each polynomial p. P, V then emulate the query phase, with each query v ←p(z)
replaced by P sending the evaluation v, followed by an execution of PC.Open to prove that v = p(z).
III. ATTACK OVERVIEW
In this section, we give a common template for our attacks against weak Fiat-Shamir transformations, with the attack on
Schnorr (see Figure 1) as an explicit example. In the following sections, we will use this template to instantiate attacks against
Bulletproofs, Plonk, Spartan, and Wesolowski’s VDF. Since the details vary greatly between each proof system, we urge the reader to cross-reference the template here with the details of each attack.
1) First, we identify the part of the public statement that is not included in the Fiat-Shamir transformation (e.g., certain public parameters or public inputs to a circuit).
For Schnorr, this includes the public input X.
2) We then identify the veriﬁcation step that relies on these public values. For Schnorr, the check is gz ?= A · Xc.
3) We select arbitrary witness values and randomness for proof generation, then use them to compute all intermedi- ate proof values. For Schnorr, we sample random A
$←G and z
$←F.
4) Finally, we use the intermediate values from step 3 to solve for the public value that will always pass the veriﬁcation step from step 2. For Schnorr, we set
X = (gz/A)1/c.
We leave to future work the task of using this template to instantate attacks against other proof systems, especially the ones appearing in Table I for which we did not give attacks in this paper.
IV. BULLETPROOFS
In this section, we describe an attack that is possible when the Bulletproofs aggregate range proof protocol (BP-ARP)
[22] is instantiated with weak Fiat-Shamir and consider the practical impacts of such an attack on MimbleWimble [55].
A. Protocol Description
Aggregate range proof relation.
In an aggregate range proof, the public input is a vector of commitments V =
(Vi)i∈[m], and the prover’s task is to show that Vi is a commitment of a value vi belonging to small range [0, 2n−1].
Formally, we consider the relation
RBP-ARP =
(
((m, n, g, h, g, h, u), V, (v, γ)) :
Vj = gvjhγj ∧vj ∈[0, 2n −1] ∀j ∈[1, m]
)
Here m, n are powers of 2, and g, h ∈Gm·n, g, h, u ∈G are generators with unknown discrete log relations.
Converting to inner product argument.
To prove vi ∈
[0, 2n−1] for all i ∈[m], the prover will commit to the bit de- composition aL of v1, . . . , vm and prove that: (1) aL ◦aR = 0 where aR = aL −1m·n, and (2) ⟨(aL)[(i−1)n,in−1], 2n⟩= vi for all i ∈[m]. To achieve zero-knowledge, the prover also samples blinding vectors sL, sR
$←Fm·n and computes two vector polynomials ℓ(X), r(X) ∈Fm·n[X], which encodes all checks above into a single inner product claim. Finally, the inner product claim is proved using the Bulletproofs’ inner product argument BP-IPA.
We describe the protocol BP-ARP in Figure 5, which uses the BP-IPA subprotocol in Figure 4. The single range proof protocol BP-RP is a special case of BP-ARP when m = 1.

Inner Product Relation. Given a power of two n = 2k and vectors of group elements g, h ∈Gn,
RIPA = n
((n, g, h, u), P, (a, b)) | P = gahbu⟨a,b⟩o
.
Interaction Phase. Set n0
← n, g(0)
← g, h(0)
← h,
P (0) ←P, a(0) ←a, b(0) ←b.
For i = 1, . . . , k:
1) P computes ni
← ni−1/2, cL
←
⟨a(i)
[:ni], b(i)
[ni:]⟩, cR ←⟨a(i)
[ni:], b(i)
[:ni]⟩, and
Li ←
 g(i−1)
[ni:]
a(i)
[:ni]  h(i−1)
[:ni]
b(i)
[ni:] ucL,
Ri ←
 g(i−1)
[:ni]
a(i)
[ni:]  h(i−1)
[ni:]
b(i)
[:ni] ucR.
P sends Li, Ri to V.
2) V sends challenge xi
$←F∗.
3) P, V both compute g(i) ←
 g(i−1)
[:ni]
x−1 i
◦
 g(i−1)
[ni:]
xi , h(i) ←
 h(i−1)
[:ni]
xi ◦
 h(i−1)
[ni:]
x−1 i
,
P (i) ←L x2 i i P (i−1)R x−2 i i
.
4) P computes a(i)
← a(i−1)
[:ni]
· x−1 i
+ a(i−1)
[ni:]
· xi and b(i) ←b(i−1)
[:ni] · xi + b(i−1)
[ni:] · x−1 i
.
After k rounds, P sends a(k), b(k) to V.
Veriﬁcation. V checks whether
P (k)
?=
 g(k)a(k)  h(k)b(k)
ua(k)·b(k).
Fig. 4: Bulletproofs’ Inner Product Argument BP-IPA
B. Attack Explanation
When BP-ARP is instantiated with a weak Fiat-Shamir transformation, the challenges are derived without hashing the commitments V. In this case, we describe an attack against
BP-ARPwFS in Figure 6. Our attack differs from an honest prover’s algorithm in two ways—ﬁrst, we sample t1, t2, τx uniformly at random, and second, we choose vi, γi for i ∈[m]
after computing the proof π. Our attack extends to the single
(i.e. non-aggregate) range proof as well.
Correctness and performance.
We show that our attack produces accepting proofs. Recall from Figure 5 that the veriﬁer for BP-ARPwFS checks the following: (1) whether
πBP-IPA is accepting, and (2) whether gˆthτx = V(z2,...,zm+1) · gδ(y,z) · T x 1 · T x2 2
(2)
Since our attack uses a valid witness (l, r) to generate πBP-IPA, this proof will be accepted by the veriﬁer. Our choice of vi, γi for i ∈[m] in step 8 of our attack then ensures that Equation 2 holds as well.
We implemented our attack in about 100 lines of Go, and veriﬁed that our forged proofs are accepted by zkrp [52].
Public Parameters. (m, n, g, h, g, h, u).
Public Input. (Vi)i∈[m]
Witness. (vi, γi)i∈[m].
Interaction Phase.
1) P samples α, ρ
$←F, sL, sR
$←Fm·n and computes aL ∈{0, 1}m·n such that
⟨(aL)[(j−1)n,jn−1], 2n⟩= vj ∀j ∈[1, m], aR = aL −1m·n,
A = hαgaLhaR,
S = hρgsLhsR.
P sends A, S to V.
2) V sends challenges y, z
$←F∗.
3) P samples τ1, τ2
$←F and computes
ℓ(X) = (aL −z · 1m·n) + sL · X, r(X) = ym·n ◦(aR + z · 1m·n + sR · X)
+ m
X j=1 zj+1 ·
 0(j−1)n∥2n∥0(m−j)n
, t(X) = ⟨ℓ(X), r(X)⟩= t0 + t1 · X + t2 · X2,
T1 = gt1hτ1,
T2 = gt2hτ2.
P sends T1, T2 to V.
4) V sends challenge x
$←F∗.
5) P computes l = ℓ(x), r = r(x),
ˆt = ⟨l, r⟩,
µ = α + ρ · x,
τx = τ2 · x2 + τ1 · x + m
X j=1 zj+1 · γj.
P sends ˆt, τx, µ to V.
6) V sends challenge w
$←F∗.
7) P, V both compute h′ = hy−m·n, u′ = uw, and
P ′ = h−µ · A · Sx · g−z·1m·n · (h′)z·ym·n
· m
Y j=1
(h′)zj+1·2n
[(j−1)n,jn−1](u′)
ˆt.
8) P, V engage in
BP-IPA for the triple
((m · n, g, h′, u′), P ′, (l, r)).
Veriﬁcation.
1) V rejects if BP-IPA fails.
2) V computes
δ(y, z) = (z −z2) · ⟨1m·n, ym·n⟩− m
X j=1 zj+2 · ⟨1n, 2n⟩,
R = Vz2·zm · gδ(y,z) · T x 1 · T x2 2 .
3) V checks whether g
ˆthτx
?= R.
Fig. 5: Bulletproofs’ Aggregate Range Proof BP-ARP
We benchmarked forged proof generation on an Intel Core i9 running at 2.4 GHz with 16 GB of RAM. Our implementation was able to generate single range proofs (i.e. m = 1) for 8-bit ranges in about 23.9 milliseconds, for 16-bit ranges in 44.7 milliseconds, and for 32-bit ranges in 86.0 milliseconds. Due to limitations of the zkrp library, larger ranges could not be tested.

0) Initialize empty proof π = ϵ.
1) Sample aL
$←{0, 1}n, α, ρ
$←F, sL, sR
$←Fn, and compute aR = aL −1n,
A ←hαgaLhaR,
S ←hρgsLhsR.
Append A, S to π.
2) Query challenges y, z ←H(π).
3) Sample t1, t2
$←F, τ1, τ2
$←F and compute
T1 ←gt1hτ1,
T2 ←gt2hτ2.
Append T1, T2 to π.
4) Query challenge x ←H(π).
5) Compute l ←(aL −z · 1n) + sL · x, r ←yn ◦(aR + z · 1n + sR · x) + z2 · 2n,
ˆt = ⟨l, r⟩,
µ ←α + ρ · x.
Sample τx
$←F and append ˆt, τx, µ to π.
6) Query challenge w ←H(π).
7) Compute h′, u′, P ′ as in Figure 5, and a proof πBP-IPA for the statement P ′ = gl (h′)r (u′)
ˆt. Append πBP-IPA to π.
8) Choose v1, . . . , vm, γ1, . . . , γm ∈F such that v1z2 + · · · + vmzm+1 = ˆt −t1 · x −t2 · x2 −δ(y, z),
(1)
γ1z2 + · · · + γmzm+1 = τx −τ2 · x2 −τ1 · x.
Set Vi = gvihγi for all i ∈[m] and V = (Vi)i∈[m].
9) Output (V, π).
Fig. 6: Weak Fiat-Shamir Attack Against BP-ARPwFS
Provable insecurity. We show that BP-ARPwFS is not knowl- edge sound if the discrete log relation assumption holds in the underlying group, and if 2n/|F| is negligible. (Note that this is usually the case in practice, with typical parameters of n ≤64 and |F| ≥2256.) The intuition is that at least one of the values vi computed by the malicious prover falls outside the range
[0, 2n −1] with overwhelming probability. Hence no efﬁcient extractor could recover values in the range consistent with the commitments, since that would lead to a non-trivial discrete log relation.
Theorem 4: Assume G satisﬁes DL-REL, and that 2n/|F| = negl(λ). Then BP-ARPwFS is not knowledge sound.
Proof: Denote by P∗the weak Fiat-Shamir malicious prover described in Figure 6, with the following speciﬁcation for step 8: P∗chooses v2, . . . , vm uniformly at random, then sets v1 to satisfy Equation 1. Since P∗always outputs accepting proofs, we have Pr h
KSP∗ 0,BP-ARPwFS i
= 1. We will show that for every extractor E, there exists an adversary A, nearly as efﬁcient as
E, against DL-REL such that
Pr h
KSE,P∗ 1,BP-ARPwFS,R i
≤AdvDL-REL
G,2
(A) + negl(λ).
Thus, if DL-REL holds in G, then E has a negligible chance of outputting a valid witness, and thus BP-ARPwFS cannot be knowledge sound against P∗. Before we describe A, we note the following fact about the distribution of v1. By construction,
P∗chooses v1 to be the unique value such that v1 = z−2 ·
 ˆt −t1 · x −t2 · x2 −δ(y, z)

−v2z −· · · −vmzm−1.
Since t1, t2, v2, . . . , vm are sampled uniformly at random, it follows that v1 is uniformly distributed. Since 2n/|F| = negl(λ), we have v1 ∈[0, 2n −1] with negligible probability.
The adversary A now works as follows: ﬁrst, it receives generators g, h
$←G in the DL-REL game. A then sam- ples extra random generators g, h, u and sets up the game
KSE,P∗ 1,BP-ARPwFS,R with pp = (m, n, g, h, g, h, u). A runs P∗ once to produce (V, π), then gives E the description of P∗ along with (V, π). When E returns a witness (v′ i, γ′ i)i∈[m], A returns (v1 −v′ 1, γ1 −γ′ 1) in the DL-REL game. If E outputs a valid witness, we have a discrete log relation gv1hγ1 = V1 = gv′ 1hγ′ 1 with v′ 1 ∈[0, 2n −1]. As mentioned above, we know that v1 ∈[0, 2n−1] with negligible probability; as long as that does not happen, A wins whenever E outputs a valid witness.
This concludes our proof.
C. Practical Impacts
We surveyed 20 implementations of Bulletproofs and 2 implementations of a Bulletproofs variant [40] to determine if they were vulnerable to a weak Fiat-Shamir attack. Of the 22 codebases surveyed, we found 14 of them to be vulnerable. Of these 14 vulnerable implementations, 7 of them appear to be more experimental implementations, describing themselves as "university projects" or "proofs of concept." 5 of the vulnerable implementations, which have now been
ﬁxed, were developed by organizations, seemingly with the intent of being used. We believe it is likely that this high fraction of vulnerable implementations is the result of a typo
(which has been ﬁxed) in the original Bulletproofs paper, which speciﬁed a weak Fiat-Shamir implementation. Most of the 7 non-vulnerable implementations, on the other hand, were audited and maintained by organizations with the intent of using them in production.
Attacking applications that use weak Fiat-Shamir.
To understand how our attack on the soundness of Bulletproofs could lead to attacks on applications that use vulnerable im- plementations, we surveyed the applications that use the Bul- letproofs implementations in our repositories. The two main applications represented are both privacy-preserving payments protocols: Monero [68] and MimbleWimble [55]. Fortunately, it appears that the Bulletproofs repositories used by these applications implement strong Fiat-Shamir transformations, so no concrete applications are vulnerable. 2
Because we want to understand how future applications could be broken by weak Fiat-Shamir transformations, though, we believe it is useful to perform a counterfactual case study:
2After this paper was accepted, we discovered another vulnerable im- plementation of Bulletproofs used by Incognito Chain [51], whose privacy protocol shares similarities with that of Monero. At the time of writing, the vulnerability has been patched; we will defer a full writeup to a future version of our paper.

what if an implementation of the MimbleWimble protocol had used a vulnerable Bulletproofs implementation?
MimbleWimble background.
MimbleWimble [55] is a cryptocurrency protocol that uses Bulletproofs to achieve con-
ﬁdential transactions. Coins are represented as Pedersen com- mitments to a value v and blinding factor r. Coins are spent by transactions consisting of input coins {Cin,1, ..., Cin,n}, output coins {Cout,1, ..., Cout,m}, a value S, and a “transaction kernel” consisting of different types of validity proofs. The number of input and output coins is limited in some cases to small values like 20 and 30, respectively, though Litecoin’s implementation
[59] could potentially allow hundreds of output coins. Among these proofs is a range proof that the value of each input and output coin is in a speciﬁed range small enough to ensure the sums Pn i=1 vin,i and Pm i=1 vout,i do not overﬂow modulo the group order p. (A typical choice for p will be roughly 256 bits.) To be a valid transaction, the equation n
X i=1 vin,i − m
X i=1 vout,i = S mod p
(3)
must be satisﬁed. An important additional constraint is that the public supply value S is relatively small — e.g., in Litecoin
[59], they must be in the range [0, 264].
Attacking MimbleWimble.
Ordinarily, the range proofs prevent the committed coin values from being large enough to overﬂow mod p; however, our attack allows one to compute valid range proofs for commitments to uniformly random elements of Zp (which are highly likely to be outside the range). Thus, to craft a valid transaction that forges money, an attacker need only construct output coins with values that satisfy Equation 3. The difﬁculty of doing this depends on whether the protocol uses the aggregate range proof for all coins, or a single range proof for each coin.
In the case where each output coin has its own range proof—and therefore each value can be chosen independently of all others—we can express this as a generalized birthday problem [88] with as many lists as there are output coins.
For simplicity, assume the attacker uses 30 output coins. In expectation, as soon as each list has 2⌈log p⌉/30 ≈29 elements, a solution will exist, but may be difﬁcult to compute efﬁciently.
By applying the k-sum algorithm of [88] for k = 30, we can compute a solution in time roughly 243 after computing roughly 243 forged proofs for each of the 30 coins. (For simplicity, we ignore other choices an attacker could make, such as choosing S or some of the input coins, that might make the attack less expensive.)
Our attack relies on being able to choose each output coin’s value independently of all others. If MimbleWimble used the
Bulletproofs aggregate range proof protocol, our generalized birthday attack would not obviously translate, since the last step of the weak Fiat-Shamir forgery would choose all 30 output coins at the same time. Surprisingly, we show that an even easier attack is possible against MimbleWimble if an aggregate range proof is used. (See Figure 6, which shows our attack against BP-ARP instantiated with a weak Fiat-Shamir transformation.) Note in the ﬁgure that in the last step, the public input V is chosen by solving linear equations for the values and blinding factors. Adding in Equation 3 as another linear constraint on the values, we only have two constraints and 30 variables. Thus, the attacker can freely choose the values of 28 of the output coins, and must only set the last two so that the forged proof is valid and the balance equation holds. This attack is very fast, needing only to solve a small linear system in F.
In both cases, once the attacker has crafted a valid transac- tion with forged output coins, they have created funds out of thin air by overﬂowing the balance equation. To spend newly- created coins whose values are outside the allowed range, the attacker would need to craft another weak F-S proof that overﬂows the balance equation again.
V. PLONK
A. Protocol Description
Constraint system.
Plonk handles fan-in two arithmetic circuits with unlimited fan-out. For such a circuit with n gates and m wires, we deﬁne a constraint system C = (V, Q) where
• V = (a, b, c) ∈([m]n)3 consists of the left, right, and output sequence.
• Q = (qL, qR, qO, qM, qC) ∈(Fn)5 consists of selector vectors.
Here F is a ﬁnite ﬁeld containing a subgroup H = ⟨ω⟩of order n. An assignment of values to wires x ∈Fm satisﬁes C if qL ◦xa + qR ◦xb + qO ◦xc + qM ◦xa ◦xb + qC = 0.
To deﬁne a relation R based on C, we set a subset {1, . . . , ℓ} of the wires to be public inputs PI and the rest to be the witness. The constraint system is set up so that the ﬁrst ℓ constraints are of the form xai −PIi = 0, where ai = i.
Converting to polynomial constraints.
Plonk proves the satisﬁability of its constraint system by reducing to certain polynomial identities. We encode vectors into polynomials in the Lagrange basis, i.e. we deﬁne qY(X) = Pn i=1(qY)iLi(X)
for Y ∈{L, R, O, M, C}. The public input and witness are encoded into three polynomials p(X) = Pn i=1 xpiLi(X) for p ∈{a, b, c}. Circuit satisﬁability then reduces to checking that eq(X) vanishes on H, where eq(X) = a(X)b(X)qM(X) + a(X)qL(X) + b(X)qR(X)
+ c(X)qO(X) + PI(X) + qC(X).
We also need to check the consistency of the wiring. [37]
deﬁnes a permutation σ : [3n] →[3n] that encodes this consistency check, converts it into polynomial constraints by letting the prover send a polynomial z(X), and then checks that the following holds over H: (1) (z(X) −1)L1(X) = 0 and (2) per(X) = 0, where per(X) = (a(X) + βX + γ)(b(X) + βk1X + γ)
(c(X) + βk2X + γ)z(X) −(a(X) + βSσ1(X) + γ)
(b(X) + βSσ2(X) + γ)(c(X) + βSσ3(X) + γ)z(ωX).

Preprocessed Polynomials.
• Selector polynomials qL(X), qR(X), qO(X), qM(X), qC(X).
• Permutation polynomials (Sσ1(X), Sσ2(X), Sσ3(X)).
Public Input. (wi)i∈[ℓ].
Witness. (wi)i∈[ℓ+1,3n].
Interaction Phase.
1) P samples b1, . . . , b6
$←F and sends wire polynomials a(X) = n
X i=1 wiLi(X) + (b1X + b2)ZH(X), b(X) = n
X i=1 wn+iLi(X) + (b3X + b4)ZH(X), c(X) = n
X i=1 wn+iLi(X) + (b5X + b6)ZH(X).
2) V sends permutation challenges β, γ
$←F.
3) P samples b7, b8, b9
$←F and sends permutation polynomial z(X) = (b7X2 + b8X + b9)ZH(X) + L1(X) + n
X i=2
Li(X) · i−1
Y j=1
(wj+βωj−1+γ)(wn+j+βk1ωj−1+γ)(w2n+j+βk2ωj−1+γ)
(wj+βω∗(j)+γ)(wn+j+βω∗(n+j)+γ)(w2n+j+βω∗(2n+j)+γ).
4) V sends quotient challenge α
$←F.
5) P computes quotient polynomial t(X) = 1
ZH(X)
 eq(X) + α per(X) + α2(z(X) −1)L1(X)
 split into three parts t(X) = t′ lo(X) + Xnt′ mid(X) + X2nt′ hi(X).
P then samples b10, b11
$←F and sends polynomials tlo(X) = t′ lo(X) + b10Xn, tmid(X) = t′ mid(X) −b10 + b11Xn, thi(X) = t′ hi(X) −b11.
Query Phase.
1) V samples evaluation challenge z
$←F.
2) V queries the polynomial oracles qY(X)
for
Y
∈
{L, R, O, M, C}, Sσj(X) for j
∈
{1, 2, 3}, a(X), b(X), c(X), z(X), tlo(X), tmid(X), thi(X) at z, and z(X) at zω. V receives the corresponding evaluations from P.
3) V computes ZH(z) = zn −1, L1(z) =
ω(zn−1)
n(z−ω) , and
PI(z) = P i∈[ℓ] wiLi(z).
4) V uses the above evaluations to check that Equation 4 holds at z, namely that eq(z) + α · per(z) + α2 · (z(z) −1)L1(z)
= ZH(z)(tlo(z) + zntmid(z) + z2nthi(z)).
Fig. 7: The Plonk Polynomial IOP
Here Sσj(X) are uniquely deﬁned based on σ for j ∈
{1, 2, 3}, k1, k2 are chosen such that H ̸= k1H ̸= k2H, and
β, γ are the veriﬁer’s challenges. The three vanishing claims over H can be batched together with a challenge α, and by the prover sending a quotient polynomial t(X) satisfying eq(X)+α·per(X)+α2 ·(z(X)−1)L1(X) = ZH(X)t(X),
(4)
where ZH(X) = Q h∈H(X −h).
The Plonk polynomial IOP.
We now describe Plonk as a polynomial IOP; see Figure 7 for the full protocol. By a slight abuse of notation, we use Plonk (and later Spartan) to refer to both the polynomial IOP and the interactive argument obtained after instantiating with a polynomial commitment scheme; the usage will be clear from context. The preprocessed polynomials consist of the selector polynomials qY(X) for
Y ∈{L, R, O, M, C}, and the polynomials Sσj(X) for j ∈
{1, 2, 3}. In the ﬁrst round, the prover P sends polynomials a(X), b(X), c(X) encoding the public input and witness.
The veriﬁer V responds with challenges β, γ
$←F used in the permutation argument. In the second round, P sends the permutation polynomial z(X), and V responds with challenge
α
$←F used in batching the polynomial checks. In the third round, P sends the quotient polynomial t(X), broken down into three parts tlo(X), tmid(X), thi(X) of small degree to be compatible with the polynomial commitment scheme. (To achieve zero-knowledge, all the polynomials sent here by P are blinded.) In the query phase, V samples an evaluation point z
$←F, then checks the polynomial identity (4) at z by querying all polynomials sent by P at that point.
Our exposition differs from [37], which described Plonk with certain optimizations speciﬁc to the KZG polynomial commitment scheme [56]. This does not affect the applicability of our attack, as discussed next.
B. Attack Explanation
We consider the weak Fiat-Shamir variant PlonkwFS, which is the non-interactive argument obtained by applying the trans- formation in Section II-F to the Plonk polynomial IOP. Our attack is presented in Figure 8; there, we assume that Plonk is instantiated with a polynomial commitment scheme supporting polynomials of degree up to n + 5, and denote by [p] the commitment to a polynomial p(X). Since the public input PI is not bound to the challenges, our cheating prover will do the following: (1) in the ﬁrst three rounds, send commitments to arbitrarily chosen polynomials, (2) provide a proof of correct evaluations for all polynomials at the challenge point, and (3)
set the public input PI to satisfy the veriﬁer’s check.
Specializing our attack to [37].
The Plonk protocol in
[37] leverages the homomorphic property of KZG to make the following optimizations. First, the prover only needs to send evaluations (a(z), b(z), c(z), Sσ1(z), Sσ2(z), z(ωz)), and the veriﬁer will homomorphically compute a commitment to the linearized polynomial r(X). Instead of checking that
Equation 4 holds at z, the veriﬁer only needs to check r(z) = 0. Second, the evaluation checks can be batched together with challenges u, v
$←F. Our attack easily spe- cializes to these optimizations, with the only change in step 7. In that step, the malicious prover will compute evaluations
(a(z), b(z), c(z), Sσ1(z), Sσ2(z), z(ωz)) and append them to π, query challenge v ←H(π), then compute a batched proof of correct evaluations and append it to π.

0) Initialize empty proof π = ϵ. Compute preprocessed poly- nomials qY(X) for Y
∈
{L, R, O, M, C} and Sσj(X) for j ∈{1, 2, 3}. Compute their commitments {[qY]}, {[Sσj]} and append them to pp.
1) Choose arbitrary polynomials a(X), b(X), c(X) ∈F<n[X].
Compute [a], [b], [c] and append them to π.
2) Query challenges β, γ ←H(π).
3) Choose an arbitrary polynomial z(X) ∈F<n[X]. Compute
[z] and append it to π.
4) Query challenge α ←H(π).
5) Choose arbitrary polynomials tlo(X), tmid(X) ∈F<n[X] and thi(X) ∈F<n+5[X]. Compute [tlo], [tmi], [thi] and append them to π.
6) Query challenge z ←H(π).
7) Compute evaluations at z of polynomials
{qY(X)}Y∈{L,R,O,M,C}, {Sσj(X)}j∈[3], a(X), b(X), c(X), z(X), z(ωX), tlo(X), tmid(X), thi(X), along with proofs of correct evaluations. Append evaluations and their proofs to π.
8) Set the public input PI ∈Fℓto satisfy the equation
ℓ
X i=1
PIi · Li(z) = ZH(z)
 tlo(z) + zntmid(z) + z2nthi(z)

−eq′(z) −α · per(z) −α2 · (z(z) −1)L1(z),
(5)
where eq′(z) = a(z)b(z)qM(z) + a(z)qL(z) + b(z)qR(z)
+ c(z)qO(z) + qC(z).
9) Output (PI, π).
Fig. 8: Weak Fiat-Shamir Attack Against PlonkwFS
Efﬁciency.
Asymptotically, our attack runs in time O(n), which is faster than the O(n log n) time of generating honest proofs due to the use of FFTs. When ℓ≥2, given a proof generated according to our attack, one can reuse the same proof for different choices of PI as long as PI is chosen to satisfy Equation 5.
We implemented our attack in 300 lines of JavaScript and veriﬁed our proofs are accepted by snarkjs. We benchmarked the forged proof generation on the same machine as our
Bulletproofs attack in Section IV. Our implementation was able to generate proofs for constraint systems of size 256 in 5167 milliseconds and for constraint systems of size 2048 in 8057 milliseconds.
Provable insecurity.
We show that our attack breaks the knowledge soundness of PlonkwFS, assuming the Plonk re- lation R satisﬁes a variant of worst-case hardness.
Deﬁnition 5:
A relation R ⊆Fℓ× Fn satisﬁes all-but- one (worst-case) hardness (ABO-H) if there exists i ∈[ℓ] and
PI[ˆi ] ∈Fℓ−1 such that for all PPT adversaries A, the following probability is negligible in λ:
AdvABO-H
R
(A) := Pr h
(PI, w) ∈R | (PIi, w) ←A(PI[ˆi ])
i
.
Here PI[ˆi ] denotes the public input without the ith entry.
We brieﬂy comment on the strength of this hardness notion.
If R is not hard in the worst case, any proof system for
R trivially satisﬁes knowledge soundness, since there exists a PPT extractor E that brute forces the witness from any public input. Therefore, worst-case hardness is a necessary assumption; our notion is slightly stronger than the worst-case hardness for R by requiring that for some i ∈[ℓ], worst-case hardness holds for a related relation Ri that puts PIi as part of the witness instead of the public input. We expect ABO-H to hold for many relations in practice, such as the relation for the pre-image of a hash.
Theorem 6:
Assume the Plonk relation R satisﬁes ABO-H.
Then PlonkwFS is not knowledge sound.
The intuition for the proof is as follows. Note that for any i ∈[ℓ] and x ∈Fℓ−1, the malicious prover in our attack can construct an accepting proof with PI[ˆi ] = x. Thus, an extractor would have to ﬁnd a witness for that choice of PI[ˆi ], which breaks the ABO-H property of R.
Proof: Assume that the Plonk relation R satisﬁes ABO-H, and let i ∈[ℓ], x ∈Fℓ−1 be the hard instance for R. Denote by P∗ the malicious prover for the attack described in Figure 8, with the following speciﬁcation for step 8: P∗sets PI[ˆi ] = x, then computes the unique value of PIi that satisﬁes Equation 5. We will show that for every extractor E, there exists an adversary
A, nearly as efﬁcient as E, against ABO-H of R such that
Pr h
KSE,P∗ 1,PlonkwFS,R i
≤AdvABO-H
R
(A).
Similar to the above proof, this will imply that PlonkwFS is not knowledge sound. The adversary A works as follows. A receives x from the ABO-H game. A then computes the public paramters pp (which includes the preprocessed polynomial commitments), and runs P∗once to get a pair (PI, π) with
PI[ˆi ] = x. It then sends (P∗, pp, PI, π) to E, and once E returns a witness w, A outputs (PI, w). We can easily see that if game KSE,P∗ 1,PlonkwFS,R outputs 1, then E outputs a valid witness; hence, A wins the ABO-H game as well.
C. Practical Impacts
Affected implementations. We surveyed 12 implementations of Plonk to determine if they were vulnerable to an attack against their Fiat-Shamir transformations. Of the 12 imple- mentations surveyed, we found 5 to be vulnerable, 4 of which have now been ﬁxed. To understand how our attack on the soundness of Plonk could impact applications using vulnerable implementations, we investigate the application of one of the vulnerable implementations we found: Dusk Network. We selected Dusk because it is a nontrivial application of Plonk for which we found a vulnerable implementation, and it’s fairly well-documented. The Dusk Network protocol is currently in its Daylight Testnet launch with a full deployment of the protocol on the roadmap for the near future.
Dusk Network background.
Dusk Network is a privacy- preserving distributed ledger protocol [32]. It uses a UTXO- based transaction model called Phoenix, which works over
“notes” stored on the ledger. (We will explain only the details

relevant for our attack.) For simplicity, we can think of each note as being a commitment to a value. A transaction is deﬁned by a set of input notes (in1, . . . , inm), a set of (newly-created)
output notes (out1, . . . , outn), and a zero-knowledge proof of correctness π generated using Plonk. To spend each input note, the payer must reveal its nulliﬁer—a random, unique identiﬁer of an input that prevents double-spending, but does not reveal the input itself. In Dusk, the nulliﬁer is computed as a hash of the note’s index in the Merkle tree and the opening of its commitment.
The transaction circuit (described in more detail in [30], §3)
takes as public inputs the Merkle root, the output notes, and the nulliﬁers of the input notes. It takes as private input the input notes, their openings, their Merkle paths, and the openings of the output notes. It veriﬁes that each nulliﬁer corresponds to a valid input note, each input note has a valid path to the Merkle root, the output commitment is well-formed, and that the sums of the values of the inputs and outputs are equal.
Attacking Dusk Network.
Our attack on PlonkwFS’s weak
Fiat-Shamir transformation lets us obtain a satisfying proof for an arbitrary witness by setting the public input to be a speciﬁc value that will satisfy the veriﬁer’s check. Notably, our attack actually allows for an attacker to set all but one of the public inputs to arbitrary values; the last public input must be set to the (unique) value that causes the veriﬁer’s check to pass. To use our attack against Dusk, then, we must make sure that there is some public input that can be set arbitrarily and is not checked elsewhere in the protocol. We observe that the nulliﬁer is a natural choice for this—its only external constraint is a check that it has not been used by any previous transaction; further, by design it is a random-looking value.
Thus, an attacker can use our attack to create verifying transactions that do not satisfy the circuit’s constraints. One clear way to exploit this is to steal funds from the Dusk
Network: an attacker can create a transaction that spends one input and sends outputs with arbitrarily large values to themselves. Because the output coins can be chosen freely, the attacker can ensure the output notes are well-formed and can be later traded for other coins.
VI. SPARTAN
A. Protocol Description
Constraint system. Spartan proves the satisﬁability of rank- one constraint systems (R1CS). A R1CS relation is deﬁned by a tuple (F, A, B, C, m, n, ℓ) where A, B, C ∈Fm×m are matrices, each with at most n = Ω(m) non-zero entries, and m ≥ℓ+ 1. Given a R1CS public input PI ∈Fℓ, a R1CS witness is a vector w ∈Fm−ℓ−1 such that if Z = (PI, 1, w), then (A · Z) ◦(B · Z) = C · Z. Spartan also requires that m = 2µ is a power of two, and ℓ= m/2 −1.
Converting to polynomial constraints.
We interpret the matrices A, B, C as functions from {0, 1}µ × {0, 1}µ to F, and similarly Z : {0, 1}µ →F, by writing the indices as their
Protocol Notation.
e ←⟨PSC(p), VSC(r)⟩(µ, d, T), where p ∈F≤d[X1, . . . , Xµ] satisﬁes P x∈{0,1}µ g(x) = T, and r = (r1, . . . , rµ) ∈Fµ is VSC’s randomness.
Interaction Phase. For i = 1, . . . , µ:
1) P computes and sends pi(X) =
X xi+1,...,xµ∈{0,1} p(r1, . . . , ri−1, X, xi+1, . . . , xµ).
2) V sends ri
$←F.
Query Phase.
1) V checks that p1(0) + p1(1) = T.
2) V checks that pi(0) + pi(1) = pi−1(ri−1) for 2 ≤i ≤µ.
Output. P, V outputs e
= pµ(rµ) supposedly equal to p(r1, . . . , rµ).
Fig. 9: The Sumcheck Protocol
Preprocessed Polynomials. Multilinear extensions e
A(X, Y ), eB(X, Y ), eC(X, Y ) of R1CS matrices A, B, C ∈Fm×m.
Public Input. PI ∈Fm/2−1.
Witness. w ∈Fm/2.
Interaction Phase. Let µ = log m.
1) P sends the multilinear extension ew of the witness w.
2) V sends challenge τ
$←Fµ.
3) P and V engage in a sumcheck protocol for ex ←⟨PSC(GPI,τ), VSC(rx)⟩(µ, 3, 0), where GPI,τ(X) is deﬁned as in Equation 6.
4) P computes vA = A(rx), vB = B(rx), vC = C(rx) and sends (vA, vB, vC) to V.
5) V sends challenges rA, rB, rC
$←F.
6) P and V engage in another sumcheck protocol for ey ←⟨PSC(Hrx), VSC(ry)⟩(µ, 2, T), where Hrx(Y ) and T are deﬁned as in Equation 7.
Query Phase.
1) Reject if either of the sumcheck instances fail.
2) Check that ex
?= (vA · vB −vC) · eeq(rx, τ).
3) Query e
A, eB, eC at (rx, ry) and receive evaluations v1, v2, v3 respectively.
4) Query ew at (ry)[1:] and receive evaluation vw.
5) Check that ey
?= (rA · v1 + rB · v2 + rC · v3) · vZ, where vZ =

(ry)0 · ^
(PI, 1)((ry)[1:]) + (1 −(ry)0) · vw

.
Fig. 10: The Spartan Polynomial IOP binary representation. We then consider the multilinear exten- sions eA, eB, eC, eZ of these functions, and deﬁne the polynomial
FPI(X) = A(X) · B(X) −C(X), where
M(X)
=
P y←{0,1}µ f
M(X, y) · eZ(y)
for

M
∈{A, B, C}. Note that FPI(X) vanishes on {0, 1}µ if and only if Z satisﬁes the R1CS relation. We turn this vanishing condition into a sumcheck instance by deﬁning
GPI,τ(X) = FPI(X) · eeq(X, τ) for a random τ ∈Fµ, supplied by the veriﬁer. The goal is then to prove that
X x∈{0,1}µ
GPI,τ(x) = 0.
(6)
The Spartan polynomial IOP.
We describe the full protocol in Figure 10, which uses the sumcheck protocol described in
Figure 9. The preprocessed polynomials consist of the mul- tilinear extensions eA(X, Y ), eB(X, Y ), eC(X, Y ) of the R1CS matrices A, B, C. In the ﬁrst round, the prover P sends the multilinear extension ew, and V sends challenge τ
$←Fµ.
Both parties then engage in a sumcheck protocol to prove
Equation 6; after this V receives an evaluation ex supposedly equal to GPI,τ(rx), where rx is V’s randomness during the run of sumcheck. Since V cannot evaluate this itself, both parties engage in another run of sumcheck. P sends three values vA, vB, vC supposedly equal to A(rx), B(rx), C(rx)
respectively, and V checks that ex = (vA · vB −vC) · eeq(rx, τ).
Next, V responds with three challenges rA, rB, rC
$←F to batch three sumcheck instances into one. The second sumcheck instance is then
X y∈{0,1}µ
Hrx(y) = T,
(7)
where
Hrx(Y ) =
 rA eA(rx, Y ) + rB eB(rx, Y ) + rC eC(rx, Y )
 eZ(Y ),
T = rA · vA + rB · vB + rC · vC.
After running sumcheck on Equation 7, V receives an evaluation ey supposedly equal to (rA e
A(rx, ry)+rB eB(rx, ry)+ rC eC(rx, ry)) eZ(ry), for V’s randomness ry during the run of sumcheck. V now queries eA, eB, eC at (rx, ry) for evaluations v1, v2, v3, and ew at (ry)[1:] for evaluation vw, and checks that ey = (rA · v1 + rB · v2 + rC · v3) · vZ,
(8)
where vZ =

(ry)0 · ^
(PI, 1)((ry)[1:]) + (1 −(ry)0) · vw

. V also performs checks for each sumcheck instance and rejects the results if either of the instances rejects them.
B. Attack Explanation
Figure 11 gives an attack against SpartanwFS, which is the non-interactive argument obtained by applying the trans- formation in Section II-F to the Spartan polynomial IOP described in Figure 10. The attack is similar to the one against
PlonkwFS: ﬁrst, the malicious prover P∗chooses polynomials
(including witnesses) that will satisfy all veriﬁcation equations except Equation 8. Then, to ﬁnish P∗crafts PI according to
Equation 9 so as to satisfy this ﬁnal check.
0) Compute commitments [ e
A], [ eB], [ eC] and append them to pp.
Initialize empty proof π = ϵ.
1) Choose arbitrary multilinear polynomial ew ∈F[µ], compute
[w] and append it to π.
2) Query challenge τ ←H(π).
3) For each of the two sumcheck instances:
a)
In each round i ∈[µ], sample an arbitrary polynomial pi(X) of appropriate degree that satisﬁes pi(0) + pi(1) = pi−1(ri−1).
Compute [pi] and append it to π.
b)
Query challenge ri ←H(π).
4) Between the two sumchecks, choose arbitrary vA, vB, vC ∈F such that ex = (vA · vB −vC) · eeq(rx, τ).
Query challenges rA, rB, rC ←H(π).
5) Compute evaluations v1
= e
A(rx, ry), v2
= eB(rx, ry), v3 = eC(rx, ry), vw = ew((ry)[1:]) and valid proofs of openings.
Append evaluations and opening proofs to π.
6) Set the public input PI ∈Fℓto satisfy the equation
^
(PI, 1)((ry)[1:]) = (ry)−1 0
· (vZ −(1 −(ry)0) · vw) ,
(9)
where vZ = ey · (rA · v1 + rB · v2 + rC · v3)−1.
7) Output (PI, π).
Fig. 11: Weak Fiat-Shamir Attack Against SpartanwFS
Provable insecurity.
Our attack against SpartanwFS satisﬁes the same properties as with our attack on PlonkwFS—namely that a malicious prover can arbitrarily choose all entries of
PI except one. Thus, we can prove that our attack breaks the knowledge soundness of SpartanwFS assuming the same
ABO-H property of the R1CS relation R. The proof is similar to that of Theorem 6.
Theorem 7:
Assume the R1CS relation R satisﬁes ABO-H.
Then SpartanwFS is not knowledge sound.
Proof: Assume that the R1CS relation R satisﬁes ABO-H, and let i ∈[ℓ], x ∈Fℓ−1 be the hard instance for R. Denote by
P∗the malicious prover for the attack described in Figure 11, with the following speciﬁcation for step 8: P∗sets PI[ˆi ] = x, then computes the unique value of PIi that satisﬁes Equation 9.
Note that P∗can do this since we can write
^
(PI, 1)(r) =
X y∈{0,1}µ−1
(PI, 1)(y) · eeq(r, y)
= m/2−2
X k=1
PIk · eeq(r, bin(k)) + eeq(r, bin(m/2 −1)).
Here we denote r
= (ry)[1:], and bin(k) is the binary representation of k. Since this is a linear equation in terms of PIk’s, to solve ^
(PI, 1)(r) = v for any value v, we can
ﬁx all but one entry PI[ˆi ] and ﬁnd a unique solution for the remaining entry PIi.

• Setup(1λ): Generate a ﬁnite abelian group G of unknown order. Pick an efﬁciently computable hash functions HG
:
{0, 1}∗
→
G to be modeled as a random oracle. Return pp = (G, HG).
• Eval(pp, T, x):
1) Compute y ←HG(x)2T by repeated squaring.
2) Compute π ←PFS(pp, T, x, y) as the F-S transformed prover of the interactive argument VDF.
• Verify(pp, T, x, y, π): Return the result of the F-S veriﬁer
VFS(pp, x, y, π).
Interactive Argument VDF:
RVDF = n
(pp, (T, x, y), ∅) | y = HG(x)2T o
.
1) V sends to P a 2λ-bit prime ℓuniformly at random.
2) Let g = HG(x). P computes π = g⌊2T /ℓ⌋and sends π to V.
3) V computes r = 2T mod ℓand accepts if and only if πℓ· gr = y.
Fig. 12: Wesolowski’s veriﬁable delay function. The Fiat-
Shamir transformed argument is described in prose below.
We now show that for every extractor E, there exists an adversary A, nearly as efﬁcient as E, against ABO-H of R such that
Pr h
KSE,P∗ 1,SpartanwFS,R i
≤AdvABO-H
R
(A).
Similar to the above proof, this will imply that SpartanwFS is not knowledge sound. The adversary A receives x from the
ABO-H game, then computes pp ←Setup(1λ) and (PI, π) ←
P∗(pp) such that PI[ˆi ] = x. It then sends (P∗, pp, PI, π) to
E, and when E outputs w, A outputs (PI, w). We can see that if the game KSE,P∗ 1,SpartanwFS,R returns 1, then E ﬁnds a valid witness w; thus, A wins in the ABO-H game. This proves the inequality.
C. Practical Impacts
We found two implementations of Spartan; both were vul- nerable to this attack but were ﬁxed following an initial public disclosure of our results. Interestingly, the reference imple- mentations of two follow-ups to Spartan, Brakedown [43] and
Nova [57], were also vulnerable. Our attack has no impact on applications—as far as we know, no applications currently use
Spartan (or related protocols) in production. Still, our attack gives ﬁrm evidence that future applications of Spartan should use strong F-S.
VII. WESOLOWSKI’S VDF
We describe an attack against a weak Fiat-Shamir transfor- mation in a veriﬁable delay function (VDF) [14] constructed by Wesolowski [90]. In Section VII-C, we discuss how our attack affects the security of vulnerable implementations in practice.
Veriﬁable delay functions.
A VDF is a function whose out- put is only known after a certain time delay, and additionally comes with a proof of correct evaluation. Formally, it is a tuple of three algorithms:
• Setup(1λ) →pp outputs public parameters,
• Eval(pp, T, x) →(y, π) evaluates the VDF with time delay T on input x, returning output y along with a proof
π. Eval is required to generate y deterministically,
• Verify(pp, T, x, y, π) veriﬁes the proof.
VDFs are required to satisfy completeness, soundness, and sequentiality; for full deﬁnitions see e.g. [14], [15], [90]. We note one signiﬁcant departure of our syntax from the syntax of previous works: we allow the time delay T to be an input to the
Eval algorithm, instead of T being determined ahead of time as a parameter to Setup. We also consider an adaptive soundness notion for VDF, i.e. given pp ←Setup(1λ), an attacker cannot output (T, x, y, π) with y ̸= Eval(pp, T, x) that would make
Verify accept the proof; previous works did not allow an attacker to choose the delay parameter. We believe that our modeling choices are closer to practice, as many applications
(see Section VII-C) do afford attackers such capabilities.
A. Protocol Description
We describe the interactive argument of [90] in Figure 12.
The argument uses a function HG that hashes bit strings into the group G. Let g = HG(x). To convince the veriﬁer it has computed y that equals g2T , the prover (implicitly) begins by sending y to the veriﬁer. Then, the veriﬁer samples a random prime ℓof 2λ bits, where λ is the security parameter, and sends
ℓto the prover. The prover replies with the value π = g⌊2T /ℓ⌋;
ﬁnally, the veriﬁer computes the residue r = 2T mod ℓand accepts if πℓgr = y. Applying the Fiat-Shamir transformation to this argument entails deriving ℓby hashing the prover’s
ﬁrst message with a hash function Hprime that outputs 2λ- bit primes. The paper speciﬁes the exact transformation to be used as ℓ= Hprime(g, y). We call the resulting non-interactive argument VDFwFS.
B. Attack Explanation
We observe that the paper [90] speciﬁed a F-S transfor- mation that leaves out several parameters, such as the time delay T and the group description G; thus, the paper is recommending weak F-S. This allows us to break the adaptive soundness of the VDF (deﬁned above); our attack is presented in Figure 13. In our attack, the malicious prover ﬁrst computes a legitimate proof for a small time delay t. Then, because this proof does not depend on t, the prover will choose a much larger delay T that leads to the veriﬁer computing the same r value in the last step. The proof will still verify for the larger delay T, though the prover only did t sequential squarings. By our choice of T, with high probability we will have y ̸= HG(x)2T ; otherwise, we know that HG(x)2T −2t = 1, which allows us to deduce the group order of G, breaking the low order assumption (as stated in [15]). We summarize with the following theorem.
Theorem 8:
VDFwFS does not satisfy adaptive soundness.

1) Pick a small time delay t. For an arbitrary x ←{0, 1}∗, compute y = g2t where g = HG(x).
2) Compute the proof π ←PFS(pp, T, x, y), which in particular is equal to π = g⌊2t/ℓ⌋where ℓ= Hprime(g, y).
3) Pick a large T such that 2T ≡2t mod ℓ. In particular, we can pick T = t + ℓ−1. More generally, we can pick T = t + o where o is the order of 2 modulo ℓ.
4) Output ((T, x, y), π).
Fig. 13: Weak Fiat-Shamir Attack Against VDFwFS
Note that we are not claiming the soundness result in [90] is incorrect, merely that it implicitly assumes the delay parameter is ﬁxed.
C. Practical Impacts
Affected implementations.
To assess the practical impacts of our attack against the VDF’s weak Fiat-Shamir Transforma- tion, we ﬁrst checked if any implementations use weak F-S.
We found that every implementation of Wesolowski’s VDF we checked implemented weak F-S. We suspect this is because the paper [90] explicitly recommends weak F-S.
On the adaptivity of attackers in choosing T.
Next, we looked at the applications that use vulnerable implementations.
We found that the dominant use of VDFs in practice are in cryptocurrency protocols for some kind of proof of work— for example, the Chia protocol uses VDFs to let miners prove they have reserved some amount of storage space for some amount of time. These protocols allow the delay to change dynamically, depending on the state of the chain; thus, an attacker could still (in principle) inﬂuence the chosen delay.
Further constraints in practice.
Our attack is theoretically possible, but turns out not to affect most implementations because of a small, but consequential, implementation choice:
the data type used for the delay parameter T is often much too small to ﬁt a delay parameter chosen by our malicious prover.
For example, in Chia, the delay parameter is a 64-bit integer, but our malicious prover’s delay parameter will be roughly 256 bits, unless 2 has small order modulo the challenge prime
ℓ. We suspect that this happens with very small probability; assuming the order of 2 modulo ℓis uniformly distributed, the probability of choosing ℓthat gives such a small order is about 2−192.
Nevertheless, for implementation choices that allow the time delay to be up to 256 bits, our attack is realizable. Such is the case for two VDF veriﬁers written in Solidity and Python [1]:
Solidity’s default integer type is 256 bits, and Python does not have a priori bounds on its integers. We developed a proof- of-concept exploit for those veriﬁers; forged proof generation takes less than a second.
In summary, our attack only leads to a latent vulnerability for applications where the delay parameter T is constrained to be much smaller than the challenge prime ℓ. An interesting question for future work is whether it is possible to prove adaptive soundness for VDFwFS when this condition is en- forced. Still, we believe strong F-S (i.e., hashing all public information, including the delay parameter and the group description) is the right choice for implementations.
VIII. DISCUSSION
In this section, we discuss some general points related to our attacks. We discuss whether our attacks could be detected, document other kinds of broken F-S implementations we found, and study one case in more detail.
Detection of weak F-S attacks.
Understanding how de- tectable our attacks are in practice requires answering two related questions. First, do forged public inputs have the same distribution as real ones? And second, do our proofs have the same distribution as honestly-generated ones?
Our attacks rely on choosing part of the public inputs as a function of the proof; thus, the public inputs output by our attacks do not necessarily have the same distribution as real ones. For Bulletproofs, the public input is a perfectly hiding commitment in both the real case and for our forger. The public inputs of our Wesolowski attack seem easily detectable, since actually performing ≈2256 squarings in an RSA group— as our forged proofs show the prover did—would be virtually impossible. For Plonk and Spartan, only one public input is chosen as a function of the proof and the other public inputs; intuitively, this input looks like a uniformly random
ﬁeld element. Reasoning about whether this is detectable is difﬁcult, since it is highly contextual.
The proofs output by our attacks have the same distribution as honest ones in some cases, but not others: e.g., our forged
Plonk proofs consist of hiding commitments to polynomials and their evaluations; the hiding property guarantees the distribution is the same as an honest prover. In contrast, though, our attack on Wesolowski’s VDF outputs proofs that are distinguishable from honest ones, since they prove false statements—any party that computes the real VDF output can tell our claimed value is not correct.
In cases where our public inputs and forged proofs have the right distribution, any detection of attacks against weak F-S will have to rely on outside heuristics; for instance, monitoring the public supply in, e.g. MimbleWimble, could help detect if funds are being stolen through such an attack. Determining who is responsible for the attack would likely be more difﬁcult.
Other misuses of Fiat-Shamir.
Our implementation survey uncovered other kinds of F-S mistakes:
1) Not including one (or more) of the prover’s messages in the hash computation.
2) Initializing a new transcript when invoking the prover/veriﬁer for a subprotocol.
3) Not including all public parameters (e.g., R1CS matrices or group generators) in the hash computation.
Case 2 can be thought of as a special case of case 1; by initalizing a new transcript, one effectively excludes the prover’s messages from earlier in the protocol. Both cases 1

and 2 trivially lead to soundness attacks, even in the non- adaptive case.
For case 3, the impact is going to depend on whether the public parameters are ﬁxed, or could be attacker-chosen in some cases. Some public parameters, like generators for cyclic groups, are nearly always hard-coded and so may not need to be hashed. However, a public parameter that could be attacker- chosen is the circuit/R1CS representation for a proof system like Plonk or Spartan. If the veriﬁer accepts arbitary circuits from a prover, and this circuit is not included in the Fiat-
Shamir computation, then this can be abused. We wish to highlight this as a case deserving further study, since in many emerging applications of proof systems (such as private smart contract platforms like Aleo [5]), user-speciﬁed circuits that represent arbitrary programs are a feature of the application.
IX. MITIGATING WEAK F-S
In this section, we suggest how academic researchers can clarify the evident confusion about the correct use of F-S.
We also suggest designs for tools that can detect weak F-
S implementations programmatically, and make it easier to implement F-S correctly.
Suggestions for researchers.
In reading recent papers about proof systems that use F-S, we noticed a clear pattern that may explain why confusion is so widespread. Most papers present and analyze the interactive version of the protocol, then state that F-S can be used to make the protocol non-interactive, but without specifying how this should be done, or giving too little information. An example is simply stating the “transcript” should be hashed, without saying what the transcript includes.
We suggest that, to minimize misconceptions and possi- bilities for error, researchers who present new protocols as interactive should be very precise about the way F-S should be applied to render their protocol non-interactive. Ideally, this includes explicitly identifying the public parameters, inputs, and prover messages that should be hashed, and specifying how to hash them.
This is not a perfect solution, since misunderstandings exist even amongst researchers: the few papers that attempt to be prescriptive about the exact transformation sometimes even state it incorrectly. For example, the original versions of both the Bulletproofs and Wesolowski’s VDF papers explicitly rec- ommend weak F-S. (We notiﬁed the authors; the Bulletproofs paper has since been updated.)
A. Automated Tooling
We explore some programmatic solutions that can either detect the incorrect use of the Fiat-Shamir transformation, or help the programmer in implementing the transformation correctly.
Criteria. We identify four key criteria to evaluate our tooling proposals, as well as any existing tooling for Fiat-Shamir, in the context of reducing weak F-S vulnerabilities.
1) Correctness: for detection, the tool should have a low error rate, and for implementation, the tool should result in correct implementations of Fiat-Shamir, 2) Simplicity: the tool should be easy to use, requiring minimal modiﬁcation to the pracitioner’s workﬂow, 3) Misuse-resistance: it should be difﬁcult to use the tool in incorrect or unintended ways, 4) Efﬁciency: the tool should add negligible overhead to the runtime of the proof system.
For existing tooling, we are aware of the Merlin library
[28] that implements a Transcript object with two operations:
one for adding messages and one for deriving challenges.
The library provides support for domain separation, message framing, and protocol composition; it has been used in many proof system libraries written in Rust. However, despite its intentional design, Merlin does not enforce the correct use of Fiat-Shamir, and indeed many of the weak Fiat-Shamir implementations we found used Merlin.
We present a few different ideas for discouraging and detecting incorrect Fiat-Shamir usage. First, Merlin could be extended to have an explicit function for adding in the public statement to the transcript. If the user does not call this function, Merlin can raise a warning alerting the user to a potential weak F-S attack. Although this would not automatically prevent incorrect instances of Fiat-Shamir, we believe it would reduce the likelihood of users missing these public values, which were the most common implementation mistake we found.
In addition to the above measure for discouraging misuse, we’ve also begun implementing an extension to Merlin that requires developers to specify all Fiat-Shamir inputs and chal- lenges when the transcript is initialized. Generating challenges without providing all the required inputs will result in an error, alerting developers to potential weak Fiat-Shamir transforma- tions. Additionally, explicitly listing the Fiat-Shamir inputs and challenges encourages developers to carefully consider Fiat-
Shamir requirements.
For detection, we can utilize information ﬂow analyses to determine which objects ﬂow to both the proof and veriﬁcation result (either directly or indirectly). We can compare these objects to those passed to the transcript. If there is a mismatch, then it is likely that Fiat-Shamir is implemented incorrectly.
Since the tool acts as a plug-in during testing, it adds zero overhead (efﬁciency), and ideally only requires few changes to be integrated (simplicity and misuse-resistance). However, this approach suffers from a false negative rate, as it would not be able to check whether two objects are equal, even though they might be computed differently, i.e. the prover computes a proof element, while the veriﬁer receives such a proof element. Detecting when these values are missing from the Fiat-Shamir computation would require dynamic equality checking on values shared between the prover and the veriﬁer.
Even though this approach would reduce the false negative rate, it would increase the false positive rate, as many of these shared values will not be required for Fiat-Shamir.
ACKNOWLEDGEMENTS
The authors thank Trail of Bits, Ian Smith, Riad Wahby,
Fraser Brown, and the anonymous reviewers at IEEE S&P

2023 for their helpful comments and suggestions. This re- search was supported by DARPA under Agreement No.
HR00112020022. Any opinions, ﬁndings and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reﬂect the views of the United
States Government or DARPA.
REFERENCES
[1] 0x Project. A solidity implementation of a vdf veriﬁer contract. https:
//github.com/0xProject/VDF, 2022.
[2] J. Abfalter.
bulletproofs-js.
https://github.com/jafalter/bulletproof-js, 2022.
[3] Adjoint Inc. Adjoint bulletproofs. https://github.com/sdiehl/bulletproofs, 2022.
[4] Adjoint Inc. Sonic implementation. https://github.com/adjoint-io/sonic, 2022.
[5] Aleo. https://www.aleo.org/, 2022.
[6] Anoma. Proof system with plonkup back-end proving arguments. https:
//github.com/anoma/plonkup/, 2022.
[7] A. Archer. Zero-knowledge proof implementation for passwords and other secrets. https://github.com/GoodiesHQ/noknow-python, 2022.
[8] Aztec
Protocol.
aztec connect repository.
https://github.com/AztecProtocol/aztec-connect, 2022.
[9] M. Bellare and P. Rogaway. Random oracles are practical: A paradigm for designing efﬁcient protocols. In D. E. Denning, R. Pyle, R. Ganesan,
R. S. Sandhu, and V. Ashby, editors, ACM CCS 93, pages 62–73. ACM
Press, Nov. 1993.
[10] M. Bellare and P. Rogaway. The security of triple encryption and a framework for code-based game-playing proofs. In S. Vaudenay, editor,
EUROCRYPT 2006, volume 4004 of LNCS, pages 409–426. Springer,
Heidelberg, May / June 2006.
[11] E. Ben-Sasson, A. Chiesa, and N. Spooner. Interactive oracle proofs. In
M. Hirt and A. D. Smith, editors, TCC 2016-B, Part II, volume 9986 of LNCS, pages 31–60. Springer, Heidelberg, Oct. / Nov. 2016.
[12] E. Ben-Sasson, A. Chiesa, E. Tromer, and M. Virza.
Succinct non- interactive zero knowledge for a von neumann architecture. In K. Fu and J. Jung, editors, USENIX Security 2014, pages 781–796. USENIX
Association, Aug. 2014.
[13] D. Bernhard, O. Pereira, and B. Warinschi. How not to prove yourself:
Pitfalls of the Fiat-Shamir heuristic and applications to Helios.
In
X. Wang and K. Sako, editors, ASIACRYPT 2012, volume 7658 of LNCS, pages 626–643. Springer, Heidelberg, Dec. 2012.
[14] D. Boneh, J. Bonneau, B. Bünz, and B. Fisch. Veriﬁable delay functions.
In H. Shacham and A. Boldyreva, editors, CRYPTO 2018, Part I, volume 10991 of LNCS, pages 757–788. Springer, Heidelberg, Aug. 2018.
[15] D. Boneh, B. Bünz, and B. Fisch. A survey of two veriﬁable delay functions. Cryptology ePrint Archive, Report 2018/712, 2018. https:
//eprint.iacr.org/2018/712.
[16] J. Bootle, A. Chiesa, Y. Hu, and M. Orrù. Gemini: Elastic SNARKs for diverse environments. In O. Dunkelman and S. Dziembowski, editors,
EUROCRYPT 2022, Part II, volume 13276 of LNCS, pages 427–457.
Springer, Heidelberg, May / June 2022.
[17] G. Botrel, T. Piellard, Y. E. Housni, I. Kubjas, and A. Tabaie. Consen- sys/gnark: v0.6.4, Feb. 2022.
[18] S. Bowe. Sonic. https://github.com/ebfull/sonic, 2022.
[19] Brakedown reference implementation.
https://github.com/conroi/
Spartan/tree/brakedown, 2022.
[20] Bulletproof range proof implementation in pure swift.
https://github.
com/shamatar/BulletproofSwift, 2022.
[21] A ruby implementation of bulletproofs.
https://github.com/azuchi/ bulletproofsrb/, 2023.
[22] B. Bünz, J. Bootle, D. Boneh, A. Poelstra, P. Wuille, and G. Maxwell.
Bulletproofs: Short proofs for conﬁdential transactions and more. In 2018 IEEE Symposium on Security and Privacy, pages 315–334. IEEE
Computer Society Press, May 2018.
[23] B. Bünz, B. Fisch, and A. Szepieniec. Transparent SNARKs from DARK compilers. In A. Canteaut and Y. Ishai, editors, EUROCRYPT 2020,
Part I, volume 12105 of LNCS, pages 677–706. Springer, Heidelberg,
May 2020.
[24] M. Campanelli, C. Ganesh, H. Khoshakhlagh, and J. Siim. Impossibili- ties in succinct arguments: Black-box extraction and more. Cryptology ePrint Archive, Report 2022/638, 2022. https://eprint.iacr.org/2022/638.
[25] D. Chaum and T. P. Pedersen.
Wallet databases with observers.
In
E. F. Brickell, editor, CRYPTO’92, volume 740 of LNCS, pages 89– 105. Springer, Heidelberg, Aug. 1993.
[26] Chia network. https://www.chia.net/, 2022.
[27] A. Chiesa, Y. Hu, M. Maller, P. Mishra, N. Vesely, and N. P. Ward.
Marlin: Preprocessing zkSNARKs with universal and updatable SRS.
In A. Canteaut and Y. Ishai, editors, EUROCRYPT 2020, Part I, volume 12105 of LNCS, pages 738–768. Springer, Heidelberg, May 2020.
[28] H. de Valence.
Merlin: composable proof transcripts for public-coin arguments of knowledge. https://merlin.cool/, 2022.
[29] H. de Valence, C. Yun, and O. Andreev. A pure-rust implementation of bulletproofs using ristretto.
https://github.com/dalek-cryptography/ bulletproofs, 2022.
[30] Dusk genesis circuits.
https://github.com/dusk-network/rusk/blob/ master/circuits/transfer/doc/dusk-genesis-circuits.pdf, 2022.
[31] Pure rust implementation of the plonk zkproof system done by the dusk- network team. https://github.com/dusk-network/plonk, 2022.
[32] The dusk network whitepaper, version 2.0.0.
https://dusk.network/ uploads/dusk-whitepaper.pdf, 2019.
[33] Encoins bulletproofs.
https://github.com/encryptedcoins/ encoins-bulletproofs, 2023.
[34] Espresso Systems. A rust implementation of the plonk zkp system and extensions. https://github.com/EspressoSystems/jellyﬁsh, 2022.
[35] A. Fiat and A. Shamir.
How to prove yourself: Practical solutions to identiﬁcation and signature problems.
In A. M. Odlyzko, editor,
CRYPTO’86, volume 263 of LNCS, pages 186–194. Springer, Heidel- berg, Aug. 1987.
[36] A. Gabizon. On the security of the BCTV pinocchio zk-SNARK variant.
Cryptology ePrint Archive, Report 2019/119, 2019. https://eprint.iacr.
org/2019/119.
[37] A. Gabizon, Z. J. Williamson, and O. Ciobotaru.
PLONK: Permu- tations over lagrange-bases for oecumenical noninteractive arguments of knowledge.
Cryptology ePrint Archive, Report 2019/953, 2019.
https://eprint.iacr.org/2019/953.
[38] An elastic proof system based on arkworks.
https://github.com/ arkworks-rs/gemini, 2022.
[39] R. Gennaro, C. Gentry, B. Parno, and M. Raykova.
Quadratic span programs and succinct NIZKs without PCPs. In T. Johansson and P. Q.
Nguyen, editors, EUROCRYPT 2013, volume 7881 of LNCS, pages 626– 645. Springer, Heidelberg, May 2013.
[40] C. Gentry, S. Halevi, and V. Lyubashevsky. Practical non-interactive pub- licly veriﬁable secret sharing with thousands of parties. In O. Dunkelman and S. Dziembowski, editors, EUROCRYPT 2022, Part I, volume 13275 of LNCS, pages 458–487. Springer, Heidelberg, May / June 2022.
[41] A. Ghoshal and S. Tessaro. Tight state-restoration soundness in the alge- braic group model. In T. Malkin and C. Peikert, editors, CRYPTO 2021,
Part III, volume 12827 of LNCS, pages 64–93, Virtual Event, Aug. 2021.
Springer, Heidelberg.
[42] M. Girault. Self-certiﬁed public keys. In D. W. Davies, editor, EURO-
CRYPT’91, volume 547 of LNCS, pages 490–497. Springer, Heidelberg,
Apr. 1991.
[43] A. Golovnev, J. Lee, S. Setty, J. Thaler, and R. S. Wahby. Brakedown:
Linear-time and post-quantum SNARKs for R1CS. Cryptology ePrint
Archive, Report 2021/1043, 2021. https://eprint.iacr.org/2021/1043.
[44] Grin. https://github.com/mimblewimble/grin, 2022.
[45] J. Groth. On the size of pairing-based non-interactive arguments. In
M. Fischlin and J.-S. Coron, editors, EUROCRYPT 2016, Part II, volume 9666 of LNCS, pages 305–326. Springer, Heidelberg, May 2016.
[46] T. Haines, S. J. Lewis, O. Pereira, and V. Teague. How not to prove your election outcome. In 2020 IEEE Symposium on Security and Privacy, pages 644–660. IEEE Computer Society Press, May 2020.
[47] Harmony.
The ﬁrst go implementation of veriﬁable delay function
(VDF). https://github.com/harmony-one/vdf, 2022.
[48] D. Hosszejni. Veriﬁable delay function as part of a master thesis. https:
//github.com/hdarjus/master-thesis-ELTE, 2022.
[49] Hyrax reference implementation. https://github.com/hyraxZK/hyraxZK, 2022.
[50] iden3. zksnark implementation in javascript & WASM. https://github.
com/iden3/snarkjs, 2022.
[51] Incognito chain. https://incognito.org/, 2023.
[52] ING Bank. Reusable library for creating and verifying zero-knowledge range proofs and set membership proofs. https://web.archive.org/web/ 20201111215751/https://github.com/ing-bank/zkrp, 2022.
[53] IOHK. Sonic protocol. https://github.com/input-output-hk/sonic, 2022.

[54] IOTA Ledger.
Implementation of veriﬁable delay function.
https:
//github.com/iotaledger/vdf, 2022.
[55] T. E. Jedusor. Mimblewimble. https://download.wpsoftware.net/bitcoin/ wizardry/mimblewimble.txt, 2016.
[56] A. Kate, G. M. Zaverucha, and I. Goldberg.
Constant-size com- mitments to polynomials and their applications.
In M. Abe, editor,
ASIACRYPT 2010, volume 6477 of LNCS, pages 177–194. Springer,
Heidelberg, Dec. 2010.
[57] A. Kothapalli, S. Setty, and I. Tzialla. Nova: Recursive zero-knowledge arguments from folding schemes.
In Y. Dodis and T. Shrimpton, editors, CRYPTO 2022, Part IV, volume 13510 of LNCS, pages 359–388.
Springer, Heidelberg, Aug. 2022.
[58] LayerX. Sonic implementation in rust. https://github.com/LayerXcom/ lx-sonic, 2022.
[59] Litecoin. https://github.com/ltc-mweb/litecoin, 2022.
[60] C++ implementation of vss using lwe encryption and proofs.
https:
//github.com/shaih/cpp-lwevss, 2021.
[61] M. Maller, S. Bowe, M. Kohlweiss, and S. Meiklejohn. Sonic: Zero- knowledge SNARKs from linear-size universal and updatable structured reference strings.
In L. Cavallaro, J. Kinder, X. Wang, and J. Katz, editors, ACM CCS 2019, pages 2111–2128. ACM Press, Nov. 2019.
[62] Matter Labs. Bellman zksnark library for community with ethereum’s bn256 support. https://github.com/matter-labs/bellman, 2022.
[63] Microsoft. Nova: Recursive snarks without trusted setup. https://github.
com/microsoft/Nova, 2022.
[64] Microsoft. Spartan: High-speed zksnarks without trusted setup. https:
//github.com/microsoft/Spartan, 2022.
[65] J. Miller.
Coordinated disclosure of vulnerabilities affecting girault, bulletproofs, and plonk. https://blog.trailofbits.com/2022/04/13/part-1- coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs- and-plonk/, 2022.
[66] Mina protocol. https://minaprotocol.com/, 2022.
[67] Mir Protocol. Recursive snarks based on plonk and halo. https://github.
com/mir-protocol/plonky, 2022.
[68] Monero: the secure, private, untraceable cryptocurrency. https://github.
com/monero-project/monero, 2022.
[69] C. Network.
Chia VDF utilities.
https://github.com/Chia-Network/ chiavdf, 2022.
[70] P. Network. An implementation of veriﬁable delay functions in rust.
https://github.com/poanetwork/vdf, 2022.
[71] O(1) Labs. The proof systems used by mina. https://github.com/o1-labs/ proof-systems, 2022.
[72] B. Parno.
A note on the unsoundness of vnTinyRAM’s SNARK.
Cryptology ePrint Archive, Report 2015/437, 2015. https://eprint.iacr.
org/2015/437.
[73] B. Parno, J. Howell, C. Gentry, and M. Raykova. Pinocchio: Nearly practical veriﬁable computation. In 2013 IEEE Symposium on Security and Privacy, pages 238–252. IEEE Computer Society Press, May 2013.
[74] J. Pascoal and S. M. de Sousa. Bulletproofs-Ocaml. https://gitlab.com/ releaselab/bulletproofs-ocaml/, 2022.
[75] A.
Poelstra.
https://github.com/apoelstra/secp256k1-zkp/tree/ bulletproofs, 2022.
[76] D. Pointcheval and J. Stern. Security arguments for digital signatures and blind signatures. Journal of Cryptology, 13(3):361–396, June 2000.
[77] Polygon. https://polygon.technology/, 2022.
[78] Python3 implementation of bulletproofs. https://github.com/wborgeaud/ python-bulletproofs, 2022.
[79] C.-P. Schnorr. Efﬁcient identiﬁcation and signatures for smart cards. In
G. Brassard, editor, CRYPTO’89, volume 435 of LNCS, pages 239–252.
Springer, Heidelberg, Aug. 1990.
[80] Scroll. https://scroll.io/, 2022.
[81] SECBIT Labs. Zero knowledge proofs toolkit for CKB. https://github.
com/sec-bit/ckb-zkp, 2022.
[82] S. Setty.
Spartan: Efﬁcient and general-purpose zkSNARKs with- out trusted setup.
In D. Micciancio and T. Ristenpart, editors,
CRYPTO 2020, Part III, volume 12172 of LNCS, pages 704–737.
Springer, Heidelberg, Aug. 2020.
[83] O. Shlomovits. Javascript code for one-round single bulletproof. https:
//github.com/omershlo/simple-bulletproof-js, 2022.
[84] Starkware. https://starkware.co/, 2022.
[85] Tari bulletproofs+.
https://github.com/tari-project/bulletproofs-plus, 2023.
[86] D. Unruh.
Non-interactive zero-knowledge proofs in the quantum random oracle model. In E. Oswald and M. Fischlin, editors, EURO-
CRYPT 2015, Part II, volume 9057 of LNCS, pages 755–784. Springer,
Heidelberg, Apr. 2015.
[87] W. Vasquez.
Bulletproofs implementation in Go.
https://github.com/ wrv/bp-go, 2022.
[88] D. Wagner.
A generalized birthday problem.
In M. Yung, editor,
CRYPTO 2002, volume 2442 of LNCS, pages 288–303. Springer,
Heidelberg, Aug. 2002.
[89] R. S. Wahby, I. Tzialla, a. shelat, J. Thaler, and M. Walﬁsh. Doubly- efﬁcient zkSNARKs without trusted setup. In 2018 IEEE Symposium on Security and Privacy, pages 926–943. IEEE Computer Society Press,
May 2018.
[90] B. Wesolowski.
Efﬁcient veriﬁable delay functions.
In Y. Ishai and
V. Rijmen, editors, EUROCRYPT 2019, Part III, volume 11478 of LNCS, pages 379–407. Springer, Heidelberg, May 2019.
[91] T. Xie, J. Zhang, Y. Zhang, C. Papamanthou, and D. Song.
Libra:
Succinct zero-knowledge proofs with optimal prover computation. In
A. Boldyreva and D. Micciancio, editors, CRYPTO 2019, Part III, volume 11694 of LNCS, pages 733–764. Springer, Heidelberg, Aug.
2019.
[92] Dusk network. https://dusk.network/, 2022.
[93] ZCash. halo2. https://github.com/zcash/halo2, 2022.
[94] Zcash. https://z.cash/, 2022.
[95] ZenGo-X. A collection of paillier cryptosystem zero knowledge proofs.
https://github.com/ZenGo-X/zk-paillier, 2022.
[96] Zengo x bulletproofs. https://github.com/ZenGo-X/bulletproofs, 2023.
[97] ZK Garage.
A pure rust plonk implementation using arkworks as a backend. https://github.com/ZK-Garage/plonk, 2022.
[98] Implementation of bulletproof for zk spl token.
https://github.com/
DescartesNetwork/zkSen, 2023.