# Careful with MAc-then-SIGn: A Computational Analysis of the EDHOC

Lightweight Authenticated Key Exchange Protocol
Felix G¨unther
ETH Zurich
Zurich, Switzerland mail@felixguenther.info
Marc Ilunga Tshibumbu Mukendi
Trail of Bits
New York City, USA marc.ilunga@trailofbits.com
Abstract—EDHOC is a lightweight authenticated key ex- change protocol for IoT communication, currently being standardized by the IETF. Its design is a trimmed-down version of similar protocols like TLS 1.3, building on the
SIGn-then-MAc (SIGMA) rationale. In its trimming, how- ever, EDHOC notably deviates from the SIGMA design by sending only short, non-unique credential identifiers, and letting recipients perform trial verification to determine the correct communication partner. Done naively, this can lead to identity misbinding attacks when an attacker can control some of the user keys, invalidating the original SIGMA security analysis and contesting the security of EDHOC.
In this work, we formalize a multi-stage key exchange security model capturing the potential attack vectors intro- duced by non-unique credential identifiers. We show that
EDHOC, in its draft version 17, indeed achieves session key security and user authentication even in a strong model where the adversary can register malicious keys with col- liding identifiers, given that the employed signature scheme provides so-called exclusive ownership. Through our security result, we confirm cryptographic improvements integrated by the IETF working group in recent draft versions of
EDHOC based on recommendations from our and others’ analysis.
1. Introduction
Low-powered devices such as smart appliances, col- loquially referred to as “Internet of Things” (IoT), are becoming increasingly ubiquitous in many public spaces and private homes [1]. Besides their computational lim- itations, IoT devices often operate in environments with stringent network constraints such as LoRaWAN [46].
The proliferation of IoT enables numerous fascinating applications and a certain level of convenience, but also brings its share of challenges. Security considerations are often out of the picture due to said restrictions of IoT applications, leading to the famous saying “the ’S’ in IoT stands for security”. Examples include applications trans- ferring sensitive data over an insecure channel or firmware updates over insecure channels allowing for injection of arbitrary code. To illustrate a few, [38] demonstrates how a network attacker can defeat smart locks to gain unautho- rized access to households, [3] exploits a vulnerability in baby monitoring cameras that gives an attacker access into the privacy of children, [2] demonstrates how a network attacker can exploit insecure smart fridges to get access to their owners’ Google accounts, and [18] shows how a malicious entity may interfere with highly intimate details of lovers. If compromised, the ubiquity of IoT devices gives attackers access to sensitive networks, compounding the initial low-cost compromise of the devices.
Designing a secure communication protocol for con- strained environments comes with two main challenges:
First, low-powered devices support only a limited set of cryptographic primitives. Second, IoT security pro- tocols must incur only minimal bandwidth, round-trip time, and power consumption overhead to fit the network constraints. The Internet Engineering Task Force (IETF)
set out to standardize protocols and efficient communi- cation data formats for constrained devices. Of particular relevance are: the Concise Binary Object Representation
(CBOR) data format (RFC 8949 [12]) for extremely small message formats; the CBOR Object Signing and Encryp- tion (COSE) protocol (RFC 9052 [54]) defining basic security services like signing, MACing, and encryption for CBOR-serialized data; and the Object Security for
Constrained RESTful Environments (OSCORE) protocol
(RFC 8613 [55]) for end-to-end application data encryp- tion based on CBOR and COSE. To protect application data, OSCORE requires that protocol participants have established a so-called “security context”, effectively a cryptographic session key. An essential missing piece in this technological chain is hence a lightweight and secure key exchange protocol establishing these session keys. To close this gap, the IETF Lightweight Authenti- cated Key Exchange (LAKE) working group was char- tered to standardize such a key exchange protocol. It leads the development of this standard under the name
EDHOC (“Ephemeral Diffie–Hellman Over COSE”) [56].
The working group has invited (and received) formal and computational security analysis of EDHOC [57]; at the time of this submission, the EDHOC draft standard is in
“Working Group Last Call” for final comments.
WHY NOT TLS 1.3?
One might ask why a dedicated key exchange protocol is needed for the LAKE setting.
After all, the IETF has already standardized several well- established key exchange protocols. One of the most prominent examples is the Transport Layer Security (TLS)
protocol; its latest version TLS 1.3 [52] has seen sub- stantial security analysis before and after standardiza- tion (e.g., [9], [10], [25], [28], [30], [31]). Additionally,
TLS 1.3 is efficient, widely adopted, and supported by several highly optimized and interoperable implementa-

tions [45]. EDHOC and the TLS 1.3 key exchange (“hand- shake”) even share a common design, inspired by the
“SIGn-and-MAc” (SIGMA) protocol family proposed by
Krawczyk [19], [43], also underlying the Internet Key
Exchange (IKE) protocol [40]. Lastly, both protocols draw from an overlapping range of cryptographic primitives for
Diffie–Hellman (X25519), signatures (Ed25519, ECDSA), key derivation (HMAC, HKDF), and authenticated en- cryption (AES-GCM, AES-CCM, Chacha20/Poly1305).
Naturally, one may wonder: why re-invent a new key exchange protocol and not simply use TLS 1.3 in
EDHOC? The answer lies again in the constraint envi- ronment: comparing the bandwidth overhead of TLS and
Datagram TLS (DTLS) with EDHOC, Mattsson et al. [47]
show that EDHOC, with a minimum total bandwidth usage as low as 101 bytes [56, Section 1.2], outperforms both TLS 1.3 and DTLS 1.3 by a factor up to 6. Notably,
EDHOC specifies four different modes (SIG-SIG, SIG-
STAT, STAT-SIG, STAT-STAT) with differing bandwidth characteristics; these modes result from the initiator and responder individually choosing whether they want to authenticate using signature keys (SIG) or static Diffie–
Hellman keys (STAT). In this work, we focus on the SIG-
SIG mode, which most closely follows the SIGMA design.
EDHOC achieves its low bandwidth usage through aggressive savings. Beyond message format optimizations, these in particular include the following two cryptograph- ically interesting changes:
•
MAC-THEN-SIGN.
In the classical SIGn-then-
MAc approach [43] employed by TLS 1.3, parties send a signature and then a MAC to authenti- cate. EDHOC instead uses a bandwidth-optimized
“MAc-then-SIGn” variant (discussed in [43] and also used in IKE [40]), where the MAC is com- puted first and not sent explicitly (thereby saving bandwidth), but instead put under the signature.
•
ABBREVIATED
IDENTIFIERS.
Usually, parties identify themselves by sending a certificate (e.g.,
X.509 certificates in TLS) or similar as a means for the communicating peer to unambiguously de- termine who they are supposedly talking to and should authenticate. By contrast, EDHOC assumes parties may already hold those certificates locally and sends only short so-called credential iden- tifiers instead of the full credentials. Crucially, these credential identifiers need not be unique:
recipients might associate multiple identities with one identifier and need to check—e.g., by trial signature verification—which is the right one.
It turns out that the combination of these two savings changes, if one is not being especially careful, has the potential to introduce new attack vectors.
ALL GOOD WITH MAC-THEN-SIGN?
To understand what could go wrong with the tweaks EDHOC introduces, let us recap the SIGMA design and its MAc-then-SIGn variant in a bit more detail. SIGMA, and EDHOC in SIG-
SIG mode, build upon a classic, unauthenticated Diffie–
Hellman (DH) protocol and then have peers authenticate through signatures under their long-term signing keys and
MACs derived from the shared DH key. In the MAc-then-
SIGn variant, the authenticating party P computes the
MAC tag τ to cover P, then computes the signature σ over the exchanged DH shares and τ, and finally sends σ but not τ. The latter is to save bandwidth, leveraging that τ can be recomputed locally by the receiving party.
Within the original SIGMA analysis paper by Canetti and
Krawczyk [19], this variant of SIGMA was analyzed as secure in a computational key exchange model building on the classical Bellare–Rogaway model [6].
EDHOC, however, deviates in one noticeable aspect from SIGMA: while user identities are assumed to be unique in the analysis of the latter, EDHOC sends only non-unique credential identifiers. This means that a re- ceiver of the signature σ above needs to trial-verify σ under possibly multiple public keys matching the sent cre- dential identifier. Such trial verification can be problematic when adversarially-controlled public keys are among the potential matching ones. Indeed, this is precisely the attack recipe for so-called “duplicate-signature key selection”
(DSKS) or “exclusive ownership” attacks [11], [42], [48],
[51], where an adversary creates a public key under which an (honestly generated) message-signature pair verifies. In the EDHOC setting, such an attack may translate to the adversary fooling the recipient of a signature to assume it originated from a different signer that happens to have a colliding credential identifier, which would violate the correct authentication of entities by the protocol.
To properly capture such attacks, we hence ought to study EDHOC in a model that allows the adversary to (1)
register its own (potentially maliciously generated) signa- ture keys—an approach similar to the ASICS model [13]
incorporating real-world certification— and (2) control the potentially colliding credential identifiers to capture their ambiguity. Worryingly, such a stronger model invalidates the original MAc-then-SIGn analysis in [19]—indeed, there is a trivial identity misbinding attack (the technical details of which we discuss in Appendix C): the attacker can register a degenerate key that makes one side of the communication accept with the wrong peer identifier, but the same session key, violating security. The question hence is: what does this mean for EDHOC?
1.1. Contributions
In this work, we perform a computational cryp- tographic analysis of EDHOC’s SIG-SIG mode with signature-based authentication. We confirm that, with a couple of recently introduced cryptographic improvements prompted by our and others’ analysis, the protocol in draft version 17 [56] achieves security even in a strong model where the adversary can register malicious keys with colliding identifiers. In more detail, our contributions are as follows.
CRYPTOGRAPHIC CORE OF EDHOC SIG-SIG.
With no prior computational analysis, our first step is to extract the core cryptographic operations of the EDHOC SIG-SIG mode (in draft 17 [56]), which we describe in Section 3.
Focusing on the SIG-SIG mode and a defined set of algo- rithms, we abstract away mode and algorithm negotiation, but consider detailed computation and key derivation steps and carefully capture EDHOC’s non-unique credential identifiers and the “trial verification” they require in the protocol execution.
2

STRONG KEY EXCHANGE SECURITY MODEL.
For our computational analysis, we base the security definition on the well-established Bellare–Rogaway model [6], captur- ing strong person-in-the-middle attacks where adversaries are allowed to compromise parties and established session keys. We incorporate a generalization of this model to capture multi-stage key exchange (MSKE) security [32],
[34], enabling a fine-grained analysis of the several keys derived in EDHOC (the final session key as well as intermediate keys for earlier data encryption). To capture the effects of EDHOC’s shortened and non-unique creden- tial identifiers discussed above, we ultimately extend the security model to allow adversaries to register malicious signing keys (akin to [13]) and specify the (potentially colliding) credential identifiers to be used in EDHOC. The result is a strong security model, given in Section 4, which asks for secure keys and entity authentication even in the presence of maliciously controlled keys whose identifiers may collide with keys of honest users. To avoid ambiguity, we fully specify our model in pseudocode.
COMPUTATIONAL
SECURITY
ANALYSIS
OF EDHOC
SIG-SIG.
Following the reductionist proof methodol- ogy, in Section 5 we then analyze EDHOC’s SIG-SIG mode in our extended MSKE security model. We show that, in its draft version 17, EDHOC SIG-SIG mode estab- lishes keys that are (forward) secure, with peers explicitly authenticated upon signature verification. Our security proof formally reduces the success probability of an ad- versary violating the key exchange security guarantees to the security of EDHOC’s building blocks (Diffie–Hellman key exchange, signatures, and key derivation). Of partic- ular interest is clearly the handling of EDHOC’s non- unique credential identifiers and their effect on explicit authentication: we show that through the way EDHOC includes (full, unique) identities under the signature and— following our suggestion—in the key derivation, secure authentication is indeed guaranteed based on the signature scheme’s (strong) unforgeability and an “exclusive own- ership” property (cf. Section 2), which are shown for the
Ed25519 signature scheme [14]; for ECDSA the picture is more blurry, as we discuss in Section 3.2 and our proof.
In Appendix C, we discuss the technical details why the original MAc-then-SIGn variant [43] would not be secure in our security model, formally underlining the need for a dedicated analysis of EDHOC.
IMPROVING THE DRAFT STANDARD.
Our security result makes use of a couple of improvements introduced in re- cent draft versions of EDHOC, based on recommendations we and authors of other security analyses (cf. Section 1.2 below) communicated to the IETF LAKE working group.
Most notably, we recommended (1) establishing a dedi- cated session key for key separation and composability;
(2) changes to the transcript hash computation to bind identities to keys; (3) reducing the dependency on en- cryption security; and (4) fixing key-reuse issues in the key derivation. All of these changes were incorporated into EDHOC (in draft 14 resp. 17) after fruitful interaction with the LAKE working group; they faciliated our security results. We conclude with a more detailed account of our contributions to the draft standard, as well as a discussion of limitations and open questions in Section 6.
1.2. Related Work
Krawczyk introduced the SIGMA [43] family of au- thenticated key exchange protocols. Among many others,
SIGMA informed the design of the Internet Key Exchange protocol [40], the TLS 1.3 handshake protocol [52], and the EDHOC SIG-SIG protocol [56]. A detailed secu- rity analysis of SIGMA and the MAc-then-SIGn variant on which EDHOC is built was given by Canetti and
Krawczyk [19]. TLS 1.3 was analyzed in the computa- tional setting by Dowling et al. [30], [31] in a multi-stage security model [32]; our model follows their approach, adapting the code-based version of Davis et al. [26].
Following the successful example of TLS 1.3’s stan- dardization process [50], the editors of the EDHOC draft standards co-authored a call for formal and computational security analysis by the research community [57], to which this work is not the first to answer. Bruni et al. [16]
performed a formal verification of EDHOC (draft 08)
using ProVerif. Norman et al. [49] extended that work to cover newly included mixed authentication modes. Cheval et al. [20] used their formal analysis tool chain, SAPIC+, for an initial analysis of EDHOC in draft 07. More re- cently, Jacomme et al. [36] substantially broadened this analysis, applying SAPIC+ to analyze all four authentica- tion methods in EDHOC draft 12 (and giving preliminary results on draft 14). Their work extensively covers all modes and various security properties in the symbolic model with enhanced idealizations of cryptographic prim- itives (including some, like key confirmation [?], [33], that we do not cover), whereas our work takes a lower- level, computational cryptography perspective and aims at the subtle effects that arise when modeling non-unique credential identifiers. Concurrent to our computational analysis, Cottier and Pointcheval [23] have worked on a tight computational analysis for the EDHOC STAT-STAT mode basing authentication on long-term, static Diffie–
Hellman keys. The latter work is closest to ours as it is also computational; it aims at proof tightness in the STAT-
STAT mode, whereas our focus is on the SIG-SIG mode and understanding the security ramifications of EDHOC’s non-unique credential identifiers.
2. Preliminaries 2.1. Notation
GROUPS
AND DIFFIE–HELLMAN.
Let (G, +) be a cyclic group of prime order q generated by G, i.e.,
G = ⟨G⟩= {xG : x ∈Zq}. For x ∈Zq and Y ∈G,
DH(x, Y ) denotes the Diffie–Hellman function that com- putes the shared secret S = xY .
GAMES, ADVERSARIES, AND ADVANTAGES.
We carry out our analysis of EDHOC in the code-based game- playing framework for provable security [7]. The security of a cryptographic scheme or protocol Π is captured by a game G(Π) played by an adversary A that interacts with the game through several named oracles. Each game provides (sometimes implicitly) two oracles INITIALIZE
(executed once at the outset of the game) and FINALIZE
(through which the adversary’s success is evaluated, called 3

once at the end); a winning condition is defined and the oracle FINALIZE outputs 1 if that condition is satisfied and 0 otherwise. The advantage of an adversary A in winning the game G(Π), denoted by AdvG
Π (A), captures the per- formance of A which is the probability that FINALIZE outputs 1, i.e.:
AdvG
Π (A) = Pr[G(Π) →1].
When the context is unambiguous, we simply write
AdvG(A) instead of AdvG
Π (A).
2.2. Cryptographic Primitives
The main cryptographic primitives in EDHOC are a cryptographic hash function denoted H, key deriva- tion functions Extract and Expand following the extract- then-expand paradigm of HKDF [44], a digital signa- ture scheme Sig, and an authenticated encryption scheme
AEAD. In the following, we recap some of the less estab- lished security properties of these schemes we will rely on for our security analysis. For further formal definitions and standard security notions (like collision resistance, signature unforgeability, etc.), see Appendix A.
2.2.1. Key derivation. EDHOC uses a key derivation function to derive session keys, but also MAC tags or IV values. The key derivation in EDHOC closely follows the design of HKDF [44], which is realized via two modules:
1)
Extract(s, ikm) extracts a pseudo-random key prk from some (high-entropy, but not necessarily uni- form) input material ikm using a salt s.
2)
Expand(prk, info, len) generates from a pseudo- random key prk a pseudo-random output string of length len bits, taking as further input a context string info.
We refer to [44] for the detailed rationale behind HKDF.
As we will see in more detail in Section 3, EDHOC uses Extract to derive from a Diffie–Hellman secret a uniformly random intermediate key and Expand to from that intermediate key derive the actual session keys and more. Analogous to prior computational analysis of real- world protocols like TLS 1.3 [31], we will employ the
PRF-ODH assumption [15], [37] on Extract and assume
Expand to be a pseudorandom function (with variable output length). See Appendices A.3, A.4 for more details.
2.2.2. Exclusive ownership of signatures.
Classi- cal unforgeability of signature schemes—existential
(EUF-CMA) or strong (SUF-CMA)—ask for signatures to be unforgeable for any message of an adversary’s choice, wrt. some fixed and honestly generated public key pk. In general, unforgeability does not imply that it is difficult to find a different, adversarially-chosen pub- lic key pk′ under which some honest message-signature pair (m, σ) also verifies. Indeed, such attacks are some- times easy and in the literature referred to as “duplicate- signature key selection” (DSKS) or “exclusive ownership” attacks [11], [42], [48], [51]. Such an attack vector would be problematic for EDHOC, as it interferes with its ap- proach to deduce the peer’s identity through “trial verifica- tion” against multiple, non-uniquely identified credentials.
INITIALIZE()
1 : (sk, pk) ←S.KGen 2 : M ←∅ 3 : return pk
FINALIZE(m, m′, σ, pk′)
1 : return


(m, σ) ∈M
∧pk ̸= pk′
∧S.Vf(pk′, m′, σ) = 1


SIGN(m)
1 : σ
$
←−S.Sign(sk, m)
2 : M ←M ∪{(m, σ)} 3 : return σ
Figure 1.
The strong universal exclusive ownership (S-UEO) game
GS-UEO for a signature scheme S.
In our analysis, we therefore rely on the following addi- tional security property of signature schemes introduced as strong universal exclusive ownership by [14] when establishing this property for Ed25519.
Definition 2.1 (Strong universal exclusive ownership). A signature scheme S is said to provide strong universal exclusive ownership (S-UEO) against an adversary A if the following advantage of A in the game GS-UEO defined in Figure 1 is small:
AdvS-UEO
S
(A) = Pr

GS-UEO(S) →1

.
The S-UEO notion implies two related and weaker notions; namely, strong conservative exclusive owner- ship (S-CEO) and strong destructive exclusive ownership
(S-DEO). The former corresponds to the case where the adversary must have queried the signing oracle to obtain a signature for m′. This scenario captures, for instance, duplicate signature key selection attacks (DSKS) [11],
[48]. The latter encodes that m′ must not have been queried to the signing oracle. Conversely, S-CEO and
S-DEO jointly imply S-UEO. We refer to [24] for further details.
3. EDHOC and Its SIG-SIG Mode
The EDHOC protocol is a lightweight authenticated key exchange that enables constrained devices to estab- lish a shared session key that is secret and mutually authenticated. Its lightweight operations and very compact messages target, for instance, Internet of Things (IoT)
devices operating in low-bandwidth environments such as LoRaWAN [46]. The primary goal of EDHOC is to establish a security context for the OSCORE protocol [55], i.e., key material for constrained application-layer end-to- end encryption, but also allows deriving keys for other applications.
EDHOC specifies four authentication modes, depend- ing on whether the initiator resp. responder authenticates itself through signatures (SIG) or static Diffie–Hellman keys (STAT). In this work, we focus on the SIG-SIG mode of EDHOC which is inspired by the SIGMA
(“SIGn-and-MAc”) family of key exchange protocols of
Krawczyk [43]. The SIGMA design involves an unauthen- ticated, ephemeral Diffie–Hellman key exchange that is authenticated through signatures and MACs sent by both peers. It is the basis of widely deployed protocols like the
Internet Key Exchange (IKE) protocol [35], [40] and the
Transport Layer Security (TLS) protocol [52].
To save on bandwidth, EDHOC’s SIG-SIG mode fol- lows the “MAc-then-SIGn” version of SIGMA [43, Sec- 4

tion 5.4].1 Here, instead of sending first a signature and then the MAC (covering the signature), the MAC tag is put “under” the signature and recomputed locally by the receiver, thereby avoiding the need to send the MAC.
In addition, EDHOC assumes that devices usually store the credentials of peers (e.g., X.509 certificates) locally.
Further bandwidth savings (compared to, e.g., TLS 1.3)
can then be achieved by sending only a short credential identifier kid rather than the credential itself. Notably, these credential identifiers need not be unique:
applications MUST NOT assume that ’kid’ values are unique and several keys associated with a ’kid’ may need to be checked [by the recipient] before the correct one is found.
[56, Section 3.5.3]
EDHOC is a self-negotiating protocol, meaning par- ticipants agree on the authentication mode and the further cryptographic components (the so-called “cipher suite”)
within the first two protocol messages. We do not capture negotiation here, but focus on the SIG-SIG mode of authentication and assume participants agree on a cipher suite (defining the to-be-used algorithms for authenticated encryption, hashing, DH key exchange, signatures, etc.), omitting the corresponding values from the protocol de- scription.
3.1. Protocol Details
The EDHOC protocol consists of three mandatory messages2 (msg1, msg2, msg3) exchanged between the initiator I and the responder R. The EDHOC SIG-SIG protocol flow is illustrated in Figure 2 and goes like this:
EDHOC message 1.
The initiator begins by sampling an ephemeral Diffie–Hellman secret x and forms its DH share
Gx = xG. It sends Gx together with a connection identi- fier CI and optional external authorization data ead1.3
EDHOC message 2.
Upon receiving msg1, the respon- der also generates an ephemeral Diffie–Hellman secret y.
It computes its DH share Gy = yG and the shared DH secret Gxy = yGx. From the shared DH secret, it derives
EDHOC’s core secret value PRK2e = Extract(th2, Gxy)
from which all further keys will be derived, using the
HKDF Extract function [44].
To authenticate itself, the responder first computes a
MAC tag τ2 via HKDF Expand, keyed width PRK2e, covering in particular its credential identifier kidR, the hashed transcript so far th2, and its credential credR. It then signs the same values together with τ2, obtaining a signature σ2. The signature together with kidR and further optional external authorization data ead2 form a plaintext ptxt2, which is XOR-encrypted into ctxt2 with a keystream K2 derived from PRK2e as Expand(PRK2e, (0, 1. This is similar to the IKE design [35], [40], but differs from the more common “SIGn-then-MAc” approach used, e.g., in TLS 1.3 [52].
2. The responder sends a fourth message for key confirmation if
EDHOC is used for authentication only and no application data is exchanged. We focus on the three-message case.
3. Applications may send external authorization data (EAD) to “re- duce round trips and the number of messages” [56, Section 3.8] by transporting “authorization related data.” EAD is opaque to EDHOC
(and we treat it as such), but can benefit from the security of keys it is encrypted under—see ead2 and ead3 in message 2 and 3 below.
Initiator I
Responder R x
$
←−Zq, Gx ←xG
G X: Gx;
C I: CI;
EAD 1: ead1 msg1 = (G X, C I, EAD 1)
y
$
←−Zq, Gy ←yG
G Y: Gy;
C R: CR
Gxy ←yGx
PRK2e ←Extract(th2, Gxy)
th2 ←H(Gy, CR, H(Gx, CI, ead1))
τ2 ←Expand(PRK2e, (2, kidR, th2, credR, ead2, tl), tl)
σ2 ←Sig.Sign(skR, (lsig, kidR, th2, credR, ead2, τ2))
ptxt2 ←(kidR, σ2, ead2)
accept K2 ←Expand(PRK2e, (0, th2, |ptxt2|), |ptxt2|)
stage 1 ctxt2 ←ptxt2 ⊕K2
CIPHERTEXT 2: ctxt2 msg2 = (G Y, CIPHERTEXT 2, C R)
(Gy, ctxt2, CR) ←msg2
Gxy ←xGy
PRK2e ←Extract(th2, Gxy)
ptxt2 := (kidR, σ2, ead2) ←ctxt2 ⊕K2 foreach (U, pkU, credU) with kidU = kidR:
τ2 ←Expand(PRK2e, (2, kidU, th2, credU, ead2, tl), tl)
if Sig.Vf(pkU, (lsig, kidU, th2, credU, ead2, τ2), σ2) = 1:
pid ←U; endforeach abort if pid = ⊥ th3 ←H(th2, ptxt2, credR)
τ3 ←Expand(PRK2e, (6, kidI, th3, credI, ead3, tl), tl)
σ3 ←Sig.Sign(skI, (lsig, kidI, th3, credI, ead3, τ3))
ptxt3 ←(kidI, σ3, ead3)
accept K3/IV3 ←Expand(PRK2e, (3/4, th3, kl/il), kl/il)
stage 2 ad3 ←(laead, "", th3)
ctxt3 ←AEAD.Enc(K3, IV3, ad3, ptxt3)
CIPHERTEXT 3: ctxt3 msg3 = (CIPHERTEXT 3)
ctxt3 ←msg3 ad3 ←(laead, "", th3)
ptxt3 := (kidI, σ3, ead3) ←AEAD.Dec(K3, IV3, ad3, ctxt3)
foreach (U, pkU, credU) with kidU = kidI:
τ3 ←Expand(PRK2e, (6, kidU, th3, credU, ead3, tl), tl)
if Sig.Vf(pkU, (lsig, kidU, th3, credU, ead3, τ3), σ2) = 1:
pid ←U; endforeach abort if pid = ⊥ th4 ←H(th3, ptxt3, credI)
accept K4/IV4 ←Expand(PRK2e, (8/9, th4, kl/il), kl/il)
stage 3 accept PRKout ←Expand(PRK2e, (7, th4, kl), kl)
stage 4
Figure 2. The EDHOC SIG-SIG protocol with three messages. MSG terms highlight message components in the terminology of the EDHOC specification [56] for better reference.
5

th2, |ptxt2|), |ptxt2|). Finally, the responder sends as sec- ond message its DH share Gy, connection identifier CR, and the ciphertext ctxt2.
EDHOC message 3.
Upon receiving msg2, the initiator computes Gxy = xGy, then derives PRK2e and K2 to decrypt ctxt2. It now needs to determine the responder’s identity/credential credR from the not necessarily unique credential identifier kidR. The EDHOC draft [56] is cur- rently underspecified in how ambiguous identifiers should be handled; we assume a “trial verification” loop is per- formed: For every identity U with matching kidU = kidR, the initiator computes a trial MAC τ2 and assumes kidR identifies U if the received signature σ2 verifies for the corresponding credential credU and τ2. Note that there might potentially be multiple identities U for which the signature verifies and hence the protocol participants may assume a wrong peer; in our security analysis in Section 5 we will implicitly give the adversary control over the order of trials to capture this.
If the signature does not verify against any match- ing user, the initiator aborts. Otherwise, the initiator authenticates by producing a MAC tag τ3 and signa- ture σ3 similarly to the responder’s in msg2, but for its own credentials and the extended transcript hash th3 =
H(th2, ptxt2, credR). It sends the plaintext ptxt3
=
(kidI, σ3, ead3), AEAD-encrypted into ctxt3 using a key K3 = Expand(PRK2e, (3, th3, kl), kl) and correspond- ing initialization vector/nonce IV3 derived from PRK2e.
(Here, ead3 is again optional external authorization data, to be protected under K3.)
Upon receiving msg3, the receiver derives K3/IV3 and decrypts ctxt3. Like the initiator, it performs a trial verification loop to determine the initiator’s identity from the possibly ambiguous credential identifier kidI. After successfully sending/processing msg3, both parties com- pute two final keys from PRK2e: key and IV K4/IV4 for optionally sending a fourth EDHOC message for key confirmation in authentication-only mode (which we omit in our analysis), and key PRKout as the final “session key” that is used to derive application-level keys.
Key exporter, the OSCORE context, and key updates.
From the established session key PRKout, initiator and responder can derive different application keys as needed.
To this end, EDHOC derives an exporter key PRKexp from
PRKout with Expand. Any application-specific key is then derived from PRKexp using distinct labels. In particular, for the OSCORE security context, the exporter mechanism is used to derive a master key and master salt.
EDHOC further allows to update PRKout to extend the lifetime of an EDHOC connection while providing forward security. For this, a new session key PRKout is derived by invoking Expand on the old PRKout and a designated key-update label.
The full key schedule of EDHOC in SIG-SIG mode including keys, IVs, the key export and (optional) key update mechanisms are shown in Figure 3.
3.2. Cryptographic Algorithms in EDHOC
Our analysis of EDHOC treats its cryptographic build- ing blocks generically; see Section 2 and Appendix A for their syntax and security definitions. Nevertheless,
Gxy
Ext
K2
τ2
K3 / IV3
τ3
K4 / IV4
PRKout
Exp
Exp
Exp
Exp
Exp
Exp
Exp
Exp
PRKexp
Exp
APP KEY
PRK2e th2 th2 context2 th3 context3 th4 th4
"" context context
Legend
Ext
Extract(salt, key)
Exp
Expand(key, label, context, len)
Gxy
Shared Diffie-Hellman Secret
PRK2e
Extracted Pseudo-Random Key
Ki/IVi/τi Stage Key/IV resp. MAC tag
Key update
Key exporter th2
H(Gy, CR, H(Gx, CI, ead1))
th3
H(th2, ptxt2, credR)
th4
H(th3, ptxt3, credI)
salt key key context
Figure 3. The EDHOC SIG-SIG key schedule, including the key update and exporter mechanism. The transcript hashes (th2, th3, th4) are summarized in the legend; context values (context2, context3) as well as labels and output lengths (label, len) for Expand are given in
Figure 2.
in the following we briefly summarize the cryptographic algorithms specified for EDHOC in its cipher suites [56,
Section 3.6];
•
The hash function H is instantiated with one of
SHA2, Shake128, or Shake256. Shake128 and
Shake256 are sponge-based extendable output functions (XOF [41]). In our analysis, we require
H to be collision resistant.
•
The KDF extraction function Extract is instan- tiated with HKDF.Extract = HMAC [4] when the hash function is SHA2. For hash algo- rithm Shake128 or Shake256, it is instanti- ated with KMAC [41] as Extract(s, ikm)
=
KMAC(s, ikm, len, "") with the desired output length len. In our analysis, we employ the PRF-
ODH assumption [15], [37] on Extract.
•
The KDF expansion function Expand is instan- tiated with HKDF.Expand, an iterated applica- tion of HMAC [4]. For hash algorithm Shake128 or Shake256, it is instantiated with KMAC as
KMAC(prk, info, len, ""). In our analysis, we as- sume Expand to be a pseudorandom function (with variable output length).
•
The signature scheme Sig is instantiated with either Ed25519 [8] or ECDSA [39]. In our analysis, we require strong unforgeability
(SUF-CMA)
and strong universal exclusive ownership (S-UEO) [14] from the signature.
We note here that Ed25519 was studied by Bren- del et al. [14] and was shown to be SUF-CMA and S-UEO secure, making our results directly applicable to it. In contrast, plain ECDSA is only 6

EUF-CMA secure and fails to meet SUF-CMA security4 as well as S-DEO (and hence S-UEO)
security [51]. The former can be fixed by making signatures unique, the latter can be mitigated by including the verification key under the signa- ture [51], as done in EDHOC. Formally estab- lishing these properties for ECDSA as used in
EDHOC is however beyond the scope of this work.
•
The
AEAD scheme
AEAD is instantiated with one of
AES-GCM,
AES-CCM, or
ChaCha20/Poly1305.
For the goals of our analysis, we do not need to make any assumptions on the AEAD scheme beyond correctness.
4. Security Model
We analyze EDHOC in a computational security model in the style of the classical Bellare–Rogaway key exchange model [6], adapted to the multi-stage (MSKE)
setting [32], [34], and with our own extensions to capture the specifics of EDHOC. Through the Bellare–Rogaway basis of our model, it captures strong adversaries with full control over the network, able to passively observe and actively modify messages arbitrarily: The adver- sary can create protocol participants via a NEWUSER oracle and orchestrate protocol sessions (i.e., the ex- ecution of the protocol by one party) between these participants via a SEND oracle. The adversary is fur- ther allowed to reveal established session keys (through a REVSESSIONKEY oracle) and compromise long-term signing keys (REVLONGTERMKEY).
On a high level, the targeted security guarantees are:
1)
Key indistinguishability. An adversary cannot distinguish an established session key from ran- dom (via a TEST oracle), as long as it is not trivially compromised (“fresh”).
2)
Forward security.
Keys are indistinguishable from random even if the long-term secrets of involved parties are later compromised.
3)
Explicit authentication. When a session accepts with an authenticated peer, there is indeed a corresponding session of that peer.
These guarantees apply to all keys established in the protocol and must hold even if other keys in the same sessions are compromised. For example, in EDHOC, an attacker might leverage leakage of the intermediate key K2 to attack the indistinguishability or authentication of K3.
This is the multi-stage aspect of our model, a state-of- the-art concept that has been applied to other modern real-world protocols like TLS 1.3 [31] or Signal [21]. To minimize ambiguity, we give both a high-level description as well as a fully code-based description of our model in the following; the latter is based on the model for TLS 1.3 by Davis et al. [26].
4.1. Capturing EDHOC’s Specifics
Recall that, in EDHOC, participant’s credentials are identified through short credential identifier values kid (cf.
4. For an ECDSA signature σ = (r, s) ∈F2 q, on m, (r, −s) is also a valid signature on m.
Figure 2). As per the underlying COSE standard [54],
“applications MUST NOT assume that ‘kid’ values are unique.” In contrast, key exchange models generally as- sume parties (and their key material) are uniquely identi- fiable by protocol participants.
To properly capture the non-uniqueness of credential identifiers in EDHOC, in our extension of the MSKE model we grant the adversary additional power when it comes to creating participants in the model: it can register users with long-term keys of its choice (as an option in the NEWUSER oracle, drawing inspiration from Boyd et al. [13]) and, most importantly, specify their (potentially colliding) credential identifiers. Protocol sessions can then address the true (unique) identities and public keys of other participants through lists peerpk kid indexed by (non- unique) credential identifiers kid. This mimics EDHOC’s process of potentially having to check several candidate credentials matching some identifier kid and allows us to capture the security requirements emerging from it.
4.2. Model Syntax
In our model, a key exchange protocol KE is abstracted as a triple of algorithms (KGen, Activate, Run).
•
KGen() generates long-term signing and verifica- tion key pairs for a protocol participant.
•
Activate(U, i, skU, {pid}U, peerpk, role)
$−→(πi
U, m)
starts a new session πi
U owned by the user U, with a list {pid}U of peers that the user U is willing to engage with in the key exchange protocol. If role = initiator, Activate returns the first proto- col message m and ⊥otherwise.
•
Run(πi
U, skU, peerpk, m)
$−→(πi
U, m′) delivers the protocol message m to the session πi
U. The mes- sage m is processed according to the protocol specification, and πi
U is updated accordingly. Fi- nally, Run outputs a response message m′ or the symbol ⊥in case of an error.
4.2.1. Protocol properties. The key exchange proto- col KE is augmented with the following variables which will determine its aimed-at security properties:
•
KE.S: the number of stages in the protocol (i.e., first-order keys to be derived).
•
KE.use[s]: whether the s-th stage key is used within the protocol (internal) or not.
•
KE.eauth[r, s]: the stage upon whose acceptance a session in role r considers the peer explicitly authenticated in stage s.5
•
KE.fs[s]: whether stage s is forward secure.
4.2.2. Session variables. The i-th session owned by user U is denoted by πi
U. Each session holds, among others, the following variables:
•
πi
U.pid: the identity of the intended peer.
•
πi
U.role: the role of the session owner.
•
πi
U.stage: the current execution stage.
•
πi
U.status[s]: the state of execution of stage s.
5. This in particular captures “retroactive” authentication [31]: E.g., eauth[resp, 1] = 3 encodes that the stage-1 key accepted by a responder will be explicitly authenticated once stage 3 is reached.
7

GMSKE
A
(KE)
INITIALIZE 1 : time ←0 2 : b
$
←−{0, 1} 3 : peerpk ←∅
NEWUSER(sk, pk, kid)
1 : time ←time + 1 2 : users ←users + 1 3 : U ←users 4 : (pkU, skU)
$
←−KGen()
5 : revltkU ←∞ 6 : if pk ̸= ⊥and (sk, pk) is valid key pair :
7 : / only valid key pairs allowed, i.e., sk must match pk (but beyond that is adversarially generated)
8 :
(skU, pkU) ←(sk, pk)
9 :
revltkU ←time 10 :
/ adversarially-registered keys are considered compromised 11 : / Add (U, pkU ) to peerpkkid 12 : peerpk kid ←peerpk kid ∪{(U, pkU)} 13 : return pkU
NEWSESSION(U, i, skU, {pid}U, peerpk, role)
1 : time ←time + 1 2 : if πi
U ̸= ⊥:
return ⊥ 3 : (πi
U, m)
$
←−Activate(U, i, skU, {pid}U, peerpk, role)
4 : πi
U.id ←U 5 : πi
U.role ←role 6 : return m
SEND(U, i, m)
1 : time ←time + 1 2 : if πi
U = ⊥:
return ⊥ 3 : (πi
U, m′)
$
←−Run(πi
U, skU, peerpk, m)
4 : s ←πi
U.stage 5 : if πi
U.status[s] = accepted :
6 :
πi u.accepted[s] ←time 7 :
if b = 0 and KE.use[s] = internal : / Random world: if key is used internally...
8 :
∃πj
V : (πi
U, πj
V ) ∈Ps and πj
V .tested = true : / and partnered session was tested 9 :
πi
U.key[s] ←πj
V .key[s] / copy the key from the partner for consistency 10 : return (πi
U.status[s], m′)
REVSESSIONKEY(U, i, s)
1 : time ←time + 1 2 : if πi
U = ⊥or πi
U.status[s] ̸= accepted :
3 :
return ⊥ 4 : πi
U.revealed[s] ←true 5 : Rs ←Rs ∪{πi
U} 6 : return πi
U.key[s]
REVLONGTERMKEY(U)
1 : time ←time + 1 2 : revltkU ←time 3 : return skU
TEST(U, i, s)
1 : time ←time + 1 2 : if πi
U = ⊥or 3 :
πi
U.status[s] ̸= accepted or 4 :
πi
U.tested[s] = true :
5 :
return ⊥ 6 : if ∃πj
V : (πi
U, πj
V ) ∈Ps and / πj
V is partnered to πi
U and...
7 :
KE.use[s] = internal and / the key is used internally and...
8 :
πj
V .status[s + 1] ̸= ⊥: / the partnered already proceeded to the next stage 9 :
return ⊥/ reject the request (since the stage-s key may have been used already)
10 : πi
U.tested[s] ←true 11 : Ts ←Ts ∪{πi
U} 12 : k0
$
←−Ki 13 : k1 ←πi
U.key[s]
14 : if b = 0 and KE.use[s] = internal : / Random world: if key is used internally 15 :
πi
U.key[s] ←kb / copy the key in the session for consistency 16 : return kb
FINALIZE(b′)
1 : / The adversary wins by...
2 : if ¬Sound : return 1 / breaking soundeness or...
3 : if ¬ExplicitAuth : return 1 / explicit authentication or..
4 : if ¬Fresh : b′ ←0 / (if it respected freshness)...
5 : return b = b′ / ...by guessing the challenge bit
Figure 4. The multi-stage key exchange security game for a key exchange protocol KE. The predictates Sound, ExplicitAuth and Fresh are given in Figure 5.
•
πi
U.key[s]: the session key of stage s.
•
πi
U.revealed[s], πi
U.accepted[s], πi
U.tested[s]: the time at which the s-th stage key was revealed, accepted, resp. tested in the game.
•
πi
U.sid[s], πi
U.cid[r, s]: the session and contributive identifiers of stage s (and role r), explained next.
4.2.3. Session and contributive identifiers. We use ses- sion identifiers [5] to define when two sessions are con- sidered partnered, namely if they hold the same session identifier at a given stage. Partnering in turn is used to exclude trivial winning conditions in our model, for instance, an adversary testing and revealing two partnered sessions. A session records its session identifier for stage s in πi
U.sid[s].
Furthermore, we use contributive identifiers [30] to specify the values a session must have honestly received before allowing the adversary to test a stage without authenticated peer. Contributive identifers hence let the key exchange model capture the (passive) security of unauthenticated keys. The session variable πi
U.cid[r, s]
holds the contributive identifier for the role r session in the protocol run, for stage s. Let r denote the role opposite to r, then πi
U.cid[r, s] contains the values that the session πi
U in role r should have honestly received to allow testing it if stage s is not authenticated.
4.2.4. Game variables. In addition to the protocol prop- erties and session variables, the security game tracks the following game-specific variables:
•
Ts: the set of all sessions that A tested in stage s.
•
Rs: the set of all sessions for which A revealed the s-th stage key.
•
Ps: the set of sessions partnered in stage s, eval- 8

Fresh 1 : / The same session was tested and revealed in stage s 2 : if ∃s : Ts ∩Rs ̸= ∅then 3 :
return false 4 : / Partnered sessions...
5 : if ∃s : Ps ∩Rs × Ts then 6 :
/ one tested, one revealed in stage s 7 :
return false 8 : / Forward-secure stages are allowed to be tested unless...
9 : if ∃s, πi
U ∈Ts : KE.fs[s] = fs 10 :
/ they accepted after peer compromise and...
11 :
∧(revltkπi
U .pid < πi
U.accepted[s])
12 :
/ they do not have a contributive partner 13 :
∧∀πj
V : πi
U.cid

πi
U.role, s

̸= πj
V .cid

πi
U.role, s
 14 :
return false 15 : / Unauthenticated stages are allowed to be tested unless...
16 : if ∃s, πi
U ∈Ts : eauth

πi
U.role, s

= ⊥ 17 :
/ they do not have a contributive partner 18 :
∧∀πj
V : πi
U.cid

πi
U.role, s

̸= πj
V .cid

πi
U.role, s
 19 :
return false 20 : return true
ExplicitAuth 1 : / Explicit authentication requires that, for all sessions and stages s...
2 : ∀(πi
U, s, s′) : πi
U.accepted[s]∧ 3 :
eauth[πi
U.role, s] = s′ < ∞/ that should achieve expl. auth. at stage s′...
4 :
∧πi
U.accepted[s′] < revltkπi
U .pid / and accepted stage s′ before peer compromise, ...
5 :
=⇒∃πj
V : / there exists a session...
6 :
πi
U.pid = V / owned by V , the peer that πi
U considers communicating with, and...
7 :
∧πi
U.sid[s′] = πj
V .sid[s′] / partnered with πi
U in stage s′, and...
8 :
/ if πj
V accepts stage s before U is comprised, partnered with πi
U also in stage s.
9 :
∧πj
V .accepted[s] < revltkπi
U .id =⇒πi
U.sid[s] = πj
V .sid[s]
Sound 1 : / More than two sessions are partnered in statge s 2 : if ∃s, πi
U, πj
V , πk
W : (πi
U, πj
V ) ∈Ps∧ 3 :
(πi
U, πk
W ) ∈Ps ∧(πj
V , πk
W ) ∈Ps then 4 :
return false 5 : / Partnered sessions...
6 : if ∃s, (πi
U, πj
V ) ∈Ps :
7 :
∧(πi
U.accepted[s] ∧πj
V .accepted[s])
8 :
∧(πi
U.key[s] ̸= πj
V .key[s]) then 9 :
/ have different keys 10 :
return false 11 : / Partnered sessions...
12 : if ∃s, (πi
U, πj
V ) ∈Ps :
13 :
(πi
U.role = πj
V .role) then 14 :
/ in the same role 15 :
return false 16 : / Partnered sessions...
17 : if ∃s, (πi
U, πj
V ) ∈Ps, r ∈{init, resp} :
18 :
πi
U.cid[r, s] ̸= πj
V .cid[r, s] then 19 :
/ do not agree on contributive identifiers 20 :
return false 21 : / Partnered sessions...
22 : if ∃s, (πi
U, πj
V ) ∈Ps :
23 :
πi
U.pid ̸= ⊥̸= πj
V .pid ∧/ upon authentication/setting pid...
24 :
(πi
U.pid ̸= V ∨πj
V .pid ̸= V ) then 25 :
/ set the wrong peer identity 26 :
return false 27 : / Session identifiers...
28 : if ∃s ̸= t, πi
U, πj
V :
29 :
(πi
U.sid[s] = πj
V .sid[t]) then 30 :
/ collide across different stages 31 :
return false 32 : return true
Figure 5. The predicates Fresh, ExplicitAuth, and Sound used in the MSKE game (Figure 4).
uated dynamically as
Ps =

(πi
U, πj
V ) : πi
U.sid[s] = πj
V .sid[s]

.
• users: the current number of users in the game.
• time: a discrete value used to order queries/events in the game.
• revltk U: the time at which the long-term secret of
U was compromised; set to ∞by default.
• peerpk kid: the set of all credentials identified by some credential identifier kid.
4.3. Adversary Model and Goal
Adversary A interacts with the protocol KE through a security game GMSKE(KE) with the following oracles.
We summarize the oracles’ main functionality here and give their detailed, code-based definition in Figure 4.
•
NEWUSER(sk, pk, kid). Register a new user U
(with honestly generated keys if pk = ⊥, else adversarially-controlled keys) and credential iden- tifier kid; add {(U, pkU)} to peerpk kid.
•
NEWSESSION(U, i, skU, {pid}U, peerpk, role).
Create and activate a new session πi
U.
•
SEND(U, i, m). Let πi
U process message m and return the response to A.
•
REVSESSIONKEY(U, i, s).
Reveal the session key πi
U.key[s] to A and mark it as revealed.
•
REVLONGTERMKEY(U). Reveal the long-term signing key skU of U to A and mark U as compromised.
•
TEST(U, i, s). Depending on the game’s challenge bit b, return either the real session key πi
U.key[s]
or a randomly sampled key. (The oracle ensures consistency across multiple TEST queries and of internal-use keys.)
4.4. Security
The adversary’s goal in the security game GMSKE is to violate the protocol’s 1)
soundness, negating a predicate Sound which checks that the protocol-specified session identi- fiers correctly capture partnering (e.g., that part- nered session derive the same keys, that at most two sessions are partnered, etc.), or 2)
explicit authentication, negating a predicate
ExplicitAuth which, in essence, checks that any session that accepts a stage s and is promised 9

explicit authentication as per eauth indeed has an honest partner in stage s (unless the involved parties were compromised prior to accepting), or 3)
key indistinguishability, by correctly guessing the challenge bit b after testing only fresh sessions; freshness is encoded via a predicate Fresh which checks that tested sessions are not trivially re- vealed, their forward-security conditions are met, and when unauthenticated, they have an honest contributive-identifier partner.
See Figure 5 for the full, code-based definition of the predicates Sound, ExplicitAuth, and Fresh.
Definition 4.1 (Multi-stage key exchange security). Let
KE be a key exchange protocol. Let GMSKE(KE) be the
MSKE game defined above and formalized in Figure 4. We define the advantage of an MSKE adversary A against KE as:
AdvMSKE
A
(KE) = 2 · Pr

GMSKE(KE) →1

−1.
5. Security Analysis
We are now ready to analyze the EDHOC SIG-SIG protocol in the security model of Section 4.
5.1. Protocol Properties
For our analysis, we first need to specify the protocol’s targeted properties: its stages, how keys are used, when explicit authentication is expected, and whether stages are forward secure.
Stages.
EDHOC consists of S = 4 stages. These corre- spond to establishing the keys (and potentially associated
IVs) K2, K3/IV3, K4/IV4, resp. PRKout.
Key usage.
The first three stage keys (and IVs) K2,
K3/IV3, and K4/IV4 are used internally within the pro- tocol to encrypt EDHOC messages. In contrast, we will show that PRKout is fit for external use, e.g., to protect application data, as intended. I.e., use = [internal, internal, internal, external].
Explicit authentication.
For initiator sessions, stages 2, 3, and 4 are explicitly authenticated upon acceptance of stage 2; stage 1 then receives explicit authentication retroactively. For responder sessions, the peer is explicitly authenticated upon acceptance of stage 3; hence, stages 3 and 4 are explicitly authenticated upon acceptance of stage 1, while stages 1 and 2 receive explicit authenti- cation retroactively.
Formally, for a given role r and stage s, we define eauth[r, s] as:
∀s ∈[1, 4] :
eauth[init, s] = 2, eauth[resp, s] = 3.
Forward security.
Through the ephemeral
Diffie–
Hellman shares freshly sampled by both participants in each run of the protocol run and keys derived from them, all four stages are forward secure: fs = [fs, fs, fs, fs].
Session identifiers.
The session identifier for stage s is a tuple (“s”, txs, auths), where “s” serves as unique label, txs is the plaintext message transcript containing elements that enter the key schedule, and auths is the
(potentially empty) list of identities of the peers that are explicitly authenticated at stage s. Within auths, I is a placeholder for the identity of the initiator session, and R for the responder’s identity.
Concretely, the session identifiers sid for s ∈[1, 4] are defined as follows:
sid[1] = (“1”, Gx, CI, ead1, Gy, CR), sid[2] = (“2”, Gx, CI, ead1, Gy, CR, kidR, σ2, ead2, R), sid[3] = (“3”, Gx, CI, ead1, Gy, CR, kidR, σ2, ead2, kidI, σ3, ead3, R, I), sid[4] = (“4”, Gx, CI, ead1, Gy, CR, kidR, σ2, ead2, kidI, σ3, ead3, R, I).
Contributive identifiers.
The contributive identifier for a stage s corresponds to the values that a session π must have honestly received (i.e., untampered) from a peer session to allow testing π in the unauthenticated stage s.
Such testing is then allowed, even when other message parts are not or only partially delivered to either party involved in that protocol run. To allow the adversary to test as many sessions as possible, we shall choose the entries in the contributive identifiers to be minimal.
For a session π in the role role ∈{init, resp}, let role denote the opposite role. The contributive identifier
π.cid[role, s] captures the messages that π must have received honestly from its peer as a prerequisite to allow testing π in stage s, if s is unauthenticated.
For EDHOC, we have the initiator (resp. responder)
set cid[init, 1] to (“1”, Gx) upon sending (resp. receiving)
message 1, which captures that an initiator must have con- tributed a DH share Gx as a prerequisite to allow testing of the responder session in stage 1. At a later point, the ini- tiator (resp. responder) sets cid[resp, 1] to (“1”, Gx, Gy)
upon receiving (resp. sending) message 2. This captures that the responder must have contributed its Gy share before a legitimate test query against an initiator session is allowed (without authentication). For all other stages s ∈{2, 3, 4}, cid[init, s] = cid[resp, s] = (“s”, Gx, Gy).
In summary:
cid[init, 1] = (“1”, Gx), cid[resp, 1] = (“1”, Gx, Gy), cid[init, s] = cid[resp, s] = (“s”, Gx, Gy) ∀s∈{2, 3, 4}.
5.2. Security Result
For EDHOC SIG-SIG, we establish the following se- curity theorem, which bases the protocol’s MSKE security on the used hash function’s collision resistance (CR), the signature’s unforgeability (SUF-CMA) and strong univer- sal exclusive ownership (S-UEO), the PRF-ODH [15]
security of Extract, and the PRF security of Expand. We give the main proof steps here, focusing on the technically challenging bits when establishing explicit authentication despite EDHOC’s use of non-unique credential identifiers; the full proof can be found in Appendix B.
10

Theorem 5.1 (MSKE security of EDHOC SIG-SIG). Let
EDHOC-Sig-Sig be the EDHOC SIG-SIG protocol as defined in Section 3, using a cyclic group G of order q.
Let A be an MSKE adversary against EDHOC-Sig-Sig, interacting with at most nU users and nS sessions. Then we can construct adversaries B4, BI.2, BI.4, BII.A2,
BII.B2, BII.B3 such that
AdvMSKE
EDHOC-Sig-Sig(A) ≤nS 2 q
+ AdvCR
H (B4)
+ 4nS ·
 nU · AdvSUF-CMA
Sig
(BI.2) + AdvS-UEO
Sig
(BI.4)

+ 4nS ·


 nU · AdvEUF-CMA
Sig
(BII.A2)
+ nS ·

AdvsnPRF-ODH
Extract
(BII.B2)
+ AdvPRF
Expand(BII.B3)
!


.
Proof (main steps). The proof proceeds via a series of games starting with the MSKE game as defined in Sec- tion 4 and ending with games where the adversary has zero advantange. Each game hop introduces a slight variation; bounding the advantage difference introduced by those variations yields the stated theorem bound. (See the full proof in Appendix B for detailed reductions for all advan- tage bounds.) The high-level strategy is to first ensure that soundness holds (Sound = true), then to split into two disjoint cases: Branch I treats the case that the adversary breaks explicit authentication (ExplicitAuth), Branch II shows that the adversary cannot guess the challenge bit when satisfying the Fresh condition. In the explicit au- thentication branch of the proof, we carefully analyze the effect of non-unique credential identifiers, which is the most critical part of the proof. We show that the specific usage of signatures in EDHOC provides S-UEO security, thereby preventing attacks on explicit authentication that would exploit the ambiguity of credential identifiers.
GAME G0.
The unmodified MSKE game.
GAMES G1/G2.
We introduce a “bad event”, aborting the game whenever two honest sessions sample the same
DH key shares. By the birthday bound, this bad event happens with probability at most nS 2/q. We argue (in
Appendix B.1) that if G2 does not abort (i.e., if no DH shares collide), then the adversary A cannot cause the
Sound predicate to become false by definition of the session identifers.
GAMES G3/G4.
We log all hash function computations done by honest sessions and abort the game if a hash col- lision occurs. The probability of this happening translates into a reduction B4 breaking H’s collision resistance.
At this point, we split the proof into two disjoint branches, I and II, each starting from Game G4. In
Branch I, the adversary attempts to break explicit authenti- cation for at least one session. In Branch II, the adversary attempts to violate key indistinguishability by guessing the challenge bit, assuming explicit authentication is not violated. The adversary’s advantage in G4 is then bounded by the sum of its advantage in the two branches.
Branch I. Ensuring explicit authentication. We first treat explicit authentication.
GAME GI.
Continuing from G4, we first guess at ran- dom a session πi
U ∈[1..nS] and stage s ∈[1..4] for which
A breaks explicit authentication, introducing a factor 4nS.
In the following, we refer to πi
U as the target session.
GAMES GI.1/GI.2.
We abort the game if the target session πi
U receives a message-signature pair which is valid under the public key of a non-corrupted user but was not produced by an honest session of that user. This would constitute a SUF-CMA forgery and hence can be bound by nU ·AdvSUF-CMA
Sig
(BI.2) via a reduction BI.2 that first guesses the peer user of πi
U and outputs the forgery when it occurs.
ON SUF-CMA SECURITY.
EDHOC including signa- tures in the key derivation means any modification to signatures implies different keys computed by initiator and responder. As soundness requires same session identifiers implying same keys, we consequently include the signa- tures in the session identifiers. Explicit authentication then requires agreement on these signatures (as a modification would lead to non-partnered sessions, violating explicit authentication), which brings up SUF-CMA here.6
We remark that since the initiator-to-responder sig- nature is AEAD-protected within msg3, one might be able to leverage AEAD integrity in this direction. Our analysis however intentionally does not rely on AEAD security but allows revealing of internal keys like K2,
K3, capturing key independence [32]. These keys enable protection of identities and EAD; modeling them as stage keys facilitates a composable treatment [17], [26], [30].
In the following games, we carefully analyze the con- sequences on authentication due to non-unique credential identifiers. More precisely, we show that an honest session will not set a wrong peer identifier.
GAME GI.3.
In this game, we set a flag sigambigous if a session accepts a message-signature pair (m′, σ)
verifying under a public key pkU ′ such that: (1) there exists an uncompromised user U and both pkU and pkU ′ are identified by the same credential identifier kid, and
(2) an honest session πi
U of U produced the signature
σ on some message m. Note that pkU ′ is a key that is potentially chosen and registered maliciously by A.
GAME
GI.4.
We now abort the game whenever sigambigous is set. We first observe that each session signs a message that includes the user’s credentials credU, which uniquely identifies the user identity U. Therefore, it must be that m′ ̸= m, as the accepted message m′ must have included U ′, but the honest session πi
U would only sign a message including U. Additionally, we can restrict our analysis to pkU ̸= pkU ′: if pkU = pkU ′ uncompromised, m would have been a forgery caught in the prior games.
By definition of sigambigous, we can now directly relate Pr[sigambigous ←true] to the advantage of an
S-UEO adversary BI.4. More precisely, BI.4 associates pkU with the challenge public key pk∗received in the
S-UEO game, i.e., set pkU = pk∗. The reduction uses the S-UEO signing oracle whenever it needs to sign a message on behalf of U; for all other users it, picks the key itself and answers oracles in the usual manner. If 6. Note that, in contrast to SIGMA which only requires EUF-CMA security, EDHOC has the MAC “under” the signature, meaning the former cannot guarantee integrity of the latter.
11

sigambigous is set for a public key pkU ′ and message- signature pair (m′, σ), BI.4 outputs (pkU ′, m′) to win the
S-UEO game.
Conclusion of Branch I.
At this point, we argue that if GI.4 does not abort, then the adversary cannot win by causing the predicate ExplicitAuth to evaluate to false.
Let us recall what it means for explicit authentication to be violated for a session πi
U and stage s which should be ex- plicitly authentication once stage s′ = eauth[πi
U.role, s]
is reached. For this, πi
U must have accepted stage s, and accepted stage s′ while its peer V = πi
U.pid was not compromised, and one of the following must hold:
(I.a)
No (honest) session πj
V is partnered with πi
U in stage s′.
(I.e., πi
U has no stage-s′ partner, despite s′ giving the explicit authentication.)
(I.b)
There exists πj
V partnered with πi
U in stage s′; however, the two sessions are not partnered in stage s although πi
U accepts stage s while U is uncompromised.
(I.e., πi
U reaches stage s uncompromised (note that possibly s ≥s′), but does not have a stage-s partner as promised by explicit authentication.)
Recall from Section 5.1 that session identifiers, de- termining partnering, include the exchange message tran- script as well as the so-far authenticated peers. Non- partnered sessions must hence disagree on one or the other.
The case (I.a) corresponds to one of two attacks:
Either, there is no session πj
V agreeing on the message transcript part of the session identifier; that means the adversary must have forged the signature πi
U received, but this is excluded through Game GI.2. Or, πj
V agrees on the transcript, but not on the authenticated identities, i.e.,
πi
U accepts with an “erroneous” peer identity. However, this corresponds to the ambiguous signatures ruled out in
Game GI.4. Hence, case (I.a) cannot occur anymore at this point.
For case (I.b), we first note that if s ≤s′, agreement on sid[s′] implies agreement on sid[s] as the latter contains a subset of elements of the former. For the later stages s ∈{3, 4}, the disagreement in the session identifier can be traced to either a forged or an ambiguous signature, which are ruled out in Game GI.2 resp. GI.4. So also case (I.b) cannot occur anymore at this point, and hence the explicit authentication properties are guaranteed.
Branch II. Ensuring key indistinguishability. We now turn to the proof branch handling challenge bit guesses of the adversary on fresh, tested sessions.
GAME GII.
Continuing from Game G4, we begin by restricting the adversary A to a single TEST query only.
In the following, πi
U refers to the tested session. Following
Dowling et al. [31], the advantage loss can be bounded by a factor at most nS ·S (the maximum number of TEST queries possible), via a hybrid argument. Here, nS is the number of sessions and S = 4 is the number of stages.
Therefore, we get the following bound:
AdvG4(A) ≤4nS · AdvGII(A).
We proceed with our analysis of Branch II by consid- ering two disjoint cases, predicated on whether the tested session has a contributive partner in the first stage or not. We start by analyzing the case with no contributive partner.
GAME GII.A1/GII.A2.
We abort the game whenever the tested session πi
U accepts a signature that verifies under an honest user’s public key for some message that was never signed by a session of that user. Simi- larly to Games GI.1/GI.2 in Branch I, this reduces to the existential7 unforgeability of the signature scheme, times a factor for guessing the involved peer, i.e., nU ·
AdvEUF-CMA
Sig
(BII.A2).
With forgeries rules out, a tested session only accepts authenticated stages s ≥2 (as initiator) resp. s ≥3
(as responder) if it received a valid signature from an honest session; since this honest session however then agrees on the contributive identifier, the test session has a contributive partner, contradicting the assumption. For unauthenticated stage 1 (and stage 2 for responders), a session without contributive identifier cannot be tested (as otherwise freshness is violated). Hence, at this point, the adversary cannot issue a valid TEST query, leaving it with guessing the challenge bit and AdvGII.A2(A) = 0.
We now turn to πi
U having a contributive partner.
GAME GII.B1.
We start by guessing the contributively partnered session πj
V , introducing a guessing factor of nS.
From this point on, we know both the tested session and its contributive partner at the outset of the game.
GAME GII.B2.
We now replace PRK2e computed by the tested session with a uniform random value ^
PRK2e.
Likewise, we replace PRK2e with ^
PRK2e at the contribu- tive partner πj
V if the πj
V holds the same two DH shares as the tested session. We rely on the snPRF-ODH security of Extract to justify this step, where the challenge DH shares are embedded as the shares of the tested session and its contributive partner, PRK2e is the challenge PRF value, and we use the DH oracle to compute a deviat- ing PRK2e value in case a contributive-partner initiator session receives an adversarially-modified DH share.
GAME GII.B3.
Finally, we replace the function Expand keyed with ^
PRK2e with a (variable output length) random function F at the tested session (as well as the contributive partner if it shares ^
PRK2e). We justify this step by the PRF security of Expand. The result of this step is that all keys derived in the tested session are replaced with uniformly random values (and likewise for the partnered session).
At this point, the tested session key is random and independent of the challenge bit. It remains to argue that
REVSESSIONKEY queries on non-partnered sessions do not help the adversary. Interestingly, this is not straightfor- ward in EDHOC, again due to the ambiguity of credential identifiers: sessions might agree on the entire message transcript (only including the non-unique credential identi- fiers), but disagree on the obtained identities. Fortunately, 7. Here we only care about the messages (containing the contributive identifier) being signed, not the signatures themselves; hence existential unforgeability suffices in this case.
12

(since draft version 16) EDHOC in addition to the tran- script also hashes the identities into th3 and th4, which in turn enter the key derivation and, by Game G4 do not collide. Hence, non-partnered sessions derive different keys, making REVSESSIONKEY useless and leaving the adversary with no chance to win.
Through the initial games and Branches I and II, we now guaranteed Sound, ExplicitAuth and key indis- tinguishability. This completes the proof; collecting the bounds gives the result in Theorem 5.1.
6. Conclusion and Discussion
In this work, we analyzed EDHOC in SIG-SIG mode for authentication and proved its security in a strong, multi-stage model for authenticated key exchange. We gave a security proof EDHOC SIG-SIG, carefully an- alyzing its authentication guarantees when an attacker is allowed to leverage EDHOC’s non-unique credential identifiers. Our analysis also reveals that the “MAc-the-
SIGn” variant of the SIGMA protocol [43] can be a bit brittle in terms of security when giving the adversary more control over how signatures are verified.
6.1. Contributions to EDHOC
During our analysis, we provided several recommen- dations to the IETF LAKE working group that led to constructive and fruitful discussions and have by now been integrated into draft version 17. We provide some further detail on the most notable proposed cryptographic improvements and their consequences for our analysis:
•
DEDICATED SESSION KEY.
We recommended establishing a dedicated session key instead of re- using the last key-exchange–internal key (K4) for clear key separation and composable security [17],
[34]. Such key was added (PRKout) in draft 14, in agreement with a similar proposal by Jacomme et al. [36].8 Our analysis confirms that PRKout is a secure “external” key, i.e., can be used securely and independently of the other keys established.
•
TRANSCRIPT HASHES.
To strengthen EDHOC against potential attacks taking advantage of non- unique credential identifiers, we suggested that the transcript hashes (th3, th4) should include the full/unique credentials of the party just au- thenticated (responder, resp. initiator). This pre- vents parties from deriving the same keys without agreeing on peer identities, which we leverage in
Branch II of our security proof. The proposed change was incorporated in draft 17:9
By including the authentication credentials in the transcript hash,
EDHOC protects against Duplicate
Signature Key Selection (DSKS)-like identity misbinding attack that the
MAC-then-Sign variant of SIGMA-I is otherwise vulnerable to.
[56, Section 8.1]
We further suggested to build transcript hashes based on the plaintext, not the ciphertext, version 8. https://github.com/lake-wg/edhoc/pull/276 9. https://github.com/lake-wg/edhoc/pull/318 of messages (similar to TLS 1.3); a change in- tegrated in draft 14.10 Our analysis confirms that this avoids depending on integrity properties of the message encryption for key exchange security.
•
KEY
SEPARATION
IN
KEY
DERIVATION.
We suggested to not reuse keys across HKDF calls of
Extract and Expand for key separation; a change executed in draft 14.11 This enables cleanly apply- ing PRF security of both functions independently.
6.2. Limitations and Open Research Questions
Our analysis of the EDHOC protocol is limited to the
SIG-SIG mode for authentication, although some of our comments to the working group also affect other authenti- cation methods. In particular, the concern that non-unique credential identifiers can lead to ambiguous signatures is also valid for the STAT-SIG and SIG-STAT modes and should be analyzed in those contexts as well. We focus on the generic security properties of EDHOC’s building blocks when proving our results, but not on tightness of our bounds. Indeed, due to various guessing steps in our proof (cf. Section 5), our security bound is rather loose. Tighter bounds are desirable as they meaningfully inform the choice of concrete parameters to instantiate the protocol both securely and efficiently, We anticipate that recent advances in proving tight security for real- world protocols like TLS 1.3 [22], [26], [27], [29] can be applied to EDHOC as well and that to this end the tight analysis of EDHOC’s STAT-STAT mode by Cottier and Pointcheval [23] could potentially be combined with our SIG-SIG analysis.
We restricted our analysis to the cryptographic core of EDHOC, striving for an appropriate balance between abstraction and completeness. Hence, we do not capture all aspects of this complex protocol like negotiation of authentication mechanisms and cipher suites or properties like key confirmation, neither do we consider other attack surfaces in low-powered devices (e.g., due to insecure im- plementations) that may undermine the security guarantee of EDHOC. Tool-based analyses like those of EDHOC by Norrman et al. [49] or Jacomme et al. [36] can paint a more complete picture of protocol interactions across dif- ferent modes, at a complexity level that is potentially out- of-reach for classical pen-and-paper computational anal- yses. We view those approaches as complementary, with computational analyses providing insights into the security of lower-level wiring cryptographic building blocks into protocols.
To the best of our knowledge, the OSCORE protocol has not yet received a formal security analysis. Tran- scribing compositional results by Brzuska et al. [17] for
Bellare–Rogaway key exchange and follow-up ones for
MSKE [32], our analysis suggests that the final session key PRKout in EDHOC can be securely composed with symmetric-key primitives. This enables a modular security analysis limited to the OSCORE protocol itself which, to- gether with our results, then would give further confidence in the overall protocol to be deployed.
10. https://github.com/lake-wg/edhoc/pull/277 11. https://github.com/lake-wg/edhoc/pull/286 13

References
[1]
Cisco Annual Internet Report (2018–2023) White Paper. https:// www.cisco.com/c/en/us/solutions/collateral/executive-perspectives/ annual-internet-report/white-paper-c11-741490.html.
[2]
Samsung connected home fridge becomes weapon in
MITM attacks.
https://www.zdnet.com/article/ samsung-connected-home-fridge-becomes-weapon-in-mitm-attacks,
August 2015.
[3]
National Vulnerability Database CVE-2021-28372. https://nvd.nist.
gov/vuln/detail/CVE-2021-28372, August 2021.
[4]
Mihir Bellare, Ran Canetti, and Hugo Krawczyk.
Keying hash functions for message authentication.
In Neal Koblitz, editor,
CRYPTO’96, volume 1109 of LNCS, pages 1–15. Springer, Hei- delberg, August 1996.
[5]
Mihir Bellare, David Pointcheval, and Phillip Rogaway. Authen- ticated key exchange secure against dictionary attacks.
In Bart
Preneel, editor, EUROCRYPT 2000, volume 1807 of LNCS, pages 139–155. Springer, Heidelberg, May 2000.
[6]
Mihir Bellare and Phillip Rogaway. Entity authentication and key distribution. In Douglas R. Stinson, editor, CRYPTO’93, volume 773 of LNCS, pages 232–249. Springer, Heidelberg, August 1994.
[7]
Mihir Bellare and Phillip Rogaway.
The security of triple en- cryption and a framework for code-based game-playing proofs.
In Serge Vaudenay, editor, EUROCRYPT 2006, volume 4004 of
LNCS, pages 409–426. Springer, Heidelberg, May / June 2006.
[8]
Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe, and
Bo-Yin Yang.
High-speed high-security signatures.
Journal of
Cryptographic Engineering, 2(2):77–89, September 2012.
[9]
Karthikeyan Bhargavan, Bruno Blanchet, and Nadim Kobeissi.
Verified models and reference implementations for the TLS 1.3 standard candidate.
In 2017 IEEE Symposium on Security and
Privacy, pages 483–502. IEEE Computer Society Press, May 2017.
[10] Karthikeyan
Bhargavan,
Christina
Brzuska,
C´edric
Fournet,
Matthew
Green,
Markulf
Kohlweiss, and
Santiago
Zanella-
B´eguelin.
Downgrade resilience in key-exchange protocols.
In 2016 IEEE Symposium on Security and Privacy, pages 506–525.
IEEE Computer Society Press, May 2016.
[11] Simon Blake-Wilson and Alfred Menezes.
Unknown key-share attacks on the station-to-station (STS) protocol. In Hideki Imai and Yuliang Zheng, editors, PKC’99, volume 1560 of LNCS, pages 154–170. Springer, Heidelberg, March 1999.
[12] C. Bormann and P. Hoffman. Concise Binary Object Representa- tion (CBOR). RFC 8949 (Internet Standard), December 2020.
[13] Colin Boyd, Cas Cremers, Michele Feltz, Kenneth G. Paterson,
Bertram Poettering, and Douglas Stebila. ASICS: Authenticated key exchange security incorporating certification systems.
In
Jason Crampton, Sushil Jajodia, and Keith Mayes, editors, ES-
ORICS 2013, volume 8134 of LNCS, pages 381–399. Springer,
Heidelberg, September 2013.
[14] Jacqueline Brendel, Cas Cremers, Dennis Jackson, and Mang Zhao.
The provable security of Ed25519: Theory and practice. In 2021
IEEE Symposium on Security and Privacy, pages 1659–1676. IEEE
Computer Society Press, May 2021.
[15] Jacqueline Brendel, Marc Fischlin, Felix G¨unther, and Chris- tian Janson.
PRF-ODH: Relations, instantiations, and impossi- bility results.
In Jonathan Katz and Hovav Shacham, editors,
CRYPTO 2017, Part III, volume 10403 of LNCS, pages 651–681.
Springer, Heidelberg, August 2017.
[16] Alessandro Bruni, Thorvald Sahl Jørgensen, Theis Grønbech Pe- tersen, and Carsten Sch¨urmann. Formal Verification of Ephemeral
Diffie-Hellman Over COSE (EDHOC). In Cas Cremers and Anja
Lehmann, editors, Security Standardisation Research (SSR 2018), volume 11322, pages 21–36. Springer International Publishing,
Cham, 2018. Series Title: Lecture Notes in Computer Science.
[17] Christina
Brzuska,
Marc
Fischlin,
Bogdan
Warinschi, and
Stephen C. Williams.
Composability of Bellare-Rogaway key exchange protocols.
In Yan Chen, George Danezis, and Vitaly
Shmatikov, editors, ACM CCS 2011, pages 51–62. ACM Press,
October 2011.
[18] Matt Burgess. Smart dildos and vibrators keep getting hacked – but Tor could be the answer to safer connected sex. WIRED UK,
February 2018.
[19] Ran Canetti and Hugo Krawczyk.
Security analysis of IKE’s signature-based key-exchange protocol.
In Moti Yung, editor,
CRYPTO 2002, volume 2442 of LNCS, pages 143–161. Springer,
Heidelberg, August 2002. https://eprint.iacr.org/2002/120/.
[20] Vincent Cheval, Charlie Jacomme, Steve Kremer, and Robert
K¨unnemann. SAPIC+: protocol verifiers of the world, unite! In
Kevin R. B. Butler and Kurt Thomas, editors, USENIX Security 2022, pages 3935–3952. USENIX Association, August 2022.
[21] Katriel Cohn-Gordon, Cas Cremers, Benjamin Dowling, Luke
Garratt, and Douglas Stebila. A formal security analysis of the signal messaging protocol.
Journal of Cryptology, 33(4):1914– 1983, October 2020.
[22] Katriel Cohn-Gordon, Cas Cremers, Kristian Gjøsteen, H˚akon Ja- cobsen, and Tibor Jager. Highly efficient key exchange protocols with optimal tightness.
In Alexandra Boldyreva and Daniele
Micciancio, editors, CRYPTO 2019, Part III, volume 11694 of
LNCS, pages 767–797. Springer, Heidelberg, August 2019.
[23] Baptiste Cottier and David Pointcheval.
Security Analysis of the EDHOC protocol. https://arxiv.org/abs/2209.03599, September 2022.
[24] Cas Cremers, Samed D¨uzl¨u, Rune Fiedler, Marc Fischlin, and
Christian Janson.
BUFFing signature schemes beyond unforge- ability and the case of post-quantum signatures.
In 2021 IEEE
Symposium on Security and Privacy, pages 1696–1714. IEEE
Computer Society Press, May 2021.
[25] Cas Cremers, Marko Horvat, Jonathan Hoyland, Sam Scott, and
Thyla van der Merwe. A comprehensive symbolic analysis of TLS 1.3. In Bhavani M. Thuraisingham, David Evans, Tal Malkin, and
Dongyan Xu, editors, ACM CCS 2017, pages 1773–1788. ACM
Press, October / November 2017.
[26] Hannah Davis, Denis Diemert, Felix G¨unther, and Tibor Jager. On the concrete security of TLS 1.3 PSK mode. In Orr Dunkelman and
Stefan Dziembowski, editors, EUROCRYPT 2022, Part II, volume 13276 of LNCS, pages 876–906. Springer, Heidelberg, May / June 2022.
[27] Hannah Davis and Felix G¨unther. Tighter proofs for the SIGMA and TLS 1.3 key exchange protocols. In Kazue Sako and Nils Ole
Tippenhauer, editors, ACNS 21, Part II, volume 12727 of LNCS, pages 448–479. Springer, Heidelberg, June 2021.
[28] Antoine Delignat-Lavaud, C´edric Fournet, Markulf Kohlweiss,
Jonathan Protzenko, Aseem Rastogi, Nikhil Swamy, Santiago
Zanella-B´eguelin, Karthikeyan Bhargavan, Jianyang Pan, and
Jean Karim Zinzindohoue. Implementing and proving the TLS 1.3 record layer. In 2017 IEEE Symposium on Security and Privacy, pages 463–482. IEEE Computer Society Press, May 2017.
[29] Denis Diemert and Tibor Jager.
On the tight security of TLS 1.3: Theoretically sound cryptographic parameters for real-world deployments. Journal of Cryptology, 34(3):30, July 2021.
[30] Benjamin Dowling, Marc Fischlin, Felix G¨unther, and Douglas
Stebila.
A cryptographic analysis of the TLS 1.3 handshake protocol candidates. In Indrajit Ray, Ninghui Li, and Christopher
Kruegel, editors, ACM CCS 2015, pages 1197–1210. ACM Press,
October 2015.
[31] Benjamin Dowling, Marc Fischlin, Felix G¨unther, and Douglas
Stebila.
A cryptographic analysis of the TLS 1.3 handshake protocol. Journal of Cryptology, 34(4):37, October 2021.
[32] Marc Fischlin and Felix G¨unther. Multi-stage key exchange and the case of Google’s QUIC protocol. In Gail-Joon Ahn, Moti Yung, and Ninghui Li, editors, ACM CCS 2014, pages 1193–1204. ACM
Press, November 2014.
[33] Marc Fischlin, Felix G¨unther, Benedikt Schmidt, and Bogdan
Warinschi. Key confirmation in key exchange: A formal treatment and implications for TLS 1.3. In 2016 IEEE Symposium on Security and Privacy, pages 452–469. IEEE Computer Society Press, May 2016.
[34] Felix G¨unther. Modeling Advanced Security Aspects of Key Ex- change and Secure Channel Protocols. Ph.D. Thesis, Technische
Universit¨at Darmstadt, 2018.
14

[35] Dan Harkins and Dave Carrel. The Internet Key Exchange (IKE).
IETF RFC 2409 (Proposed Standard), 1998.
[36] Charlie Jacomme, Elise Klein, Steve Kremer, and Ma¨ıwenn Racou- chot.
A comprehensive, formal and automated analysis of the
EDHOC protocol. In 32nd USENIX Security Symposium, USENIX
Security 2023, Anaheim, CA, United States, August 2023.
[37] Tibor Jager, Florian Kohlar, Sven Sch¨age, and J¨org Schwenk. On the security of TLS-DHE in the standard model.
In Reihaneh
Safavi-Naini and Ran Canetti, editors, CRYPTO 2012, volume 7417 of LNCS, pages 273–293. Springer, Heidelberg, August 2012.
[38] Jmaxxz.
DEF CON 24 - Backdooring the Frontdoor.
https:
//archive.org/details/youtube-MMB1CkZi6t4, October 2022.
[39] Don Johnson, Alfred Menezes, and Scott Vanstone. The Elliptic
Curve Digital Signature Algorithm (ECDSA). International Jour- nal of Information Security, 1(1):36–63, August 2001.
[40] C. Kaufman, P. Hoffman, Y. Nir, P. Eronen, and T. Kivinen. Internet
Key Exchange Protocol Version 2 (IKEv2). RFC 7296 (Internet
Standard), October 2014.
Updated by RFCs 7427, 7670, 8247, 8983.
[41] John Kelsey, Shu-jen Chang, and Ray Perlner.
SHA-3 Derived
Functions: cSHAKE, KMAC, TupleHash, and ParallelHash. Tech- nical Report NIST Special Publication (SP) 800-185, National
Institute of Standards and Technology, December 2016.
[42] Neal Koblitz and Alfred Menezes.
Another look at security definitions. Advances in Mathematics of Communications, 7(1):1– 38, February 2013.
[43] Hugo Krawczyk.
SIGMA: The “SIGn-and-MAc” approach to authenticated Diffie-Hellman and its use in the IKE protocols. In
Dan Boneh, editor, CRYPTO 2003, volume 2729 of LNCS, pages 400–425. Springer, Heidelberg, August 2003.
[44] Hugo Krawczyk. Cryptographic extraction and key derivation: The
HKDF scheme. In Tal Rabin, editor, CRYPTO 2010, volume 6223 of LNCS, pages 631–648. Springer, Heidelberg, August 2010.
[45] Hyunwoo Lee, Doowon Kim, and Yonghwi Kwon. TLS 1.3 in
Practice:How TLS 1.3 Contributes to the Internet. In Proceedings of the Web Conference 2021, WWW ’21, pages 70–79, New York,
NY, USA, April 2021. Association for Computing Machinery.
[46] LoRa Alliance.
Long range wide area network (LoRaWAN)
specification. https://lora-alliance.org/about-lorawan/.
[47] John Preuß Mattsson, Francesca Palombini, and Maliˇsa Vuˇcini´c.
Comparison of CoAP Security Protocols. Internet Draft draft-ietf- lwig-security-protocol-comparison-05, Internet Engineering Task
Force, November 2020. Num Pages: 39.
[48] Alfred Menezes and Nigel P. Smart.
Security of signature schemes in a multi-user setting. Designs, Codes and Cryptography, 33(3):261–274, November 2004.
[49] K. Norrman, V. Sundararajan, and A. Bruni.
Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices. In
SECRYPT, 2021.
[50] Kenneth G. Paterson and Thyla van der Merwe.
Reactive and proactive standardisation of TLS.
In Lidong Chen, David A.
McGrew, and Chris J. Mitchell, editors, Security Standardisation
Research (SSR 2016), volume 10074 of Lecture Notes in Computer
Science, pages 160–186, Gaithersburg, MD, USA, December 2016.
Springer.
[51] Thomas Pornin and Julien P. Stern. Digital signatures do not guar- antee exclusive ownership. In John Ioannidis, Angelos Keromytis, and Moti Yung, editors, ACNS 05, volume 3531 of LNCS, pages 138–150. Springer, Heidelberg, June 2005.
[52] E. Rescorla. The Transport Layer Security (TLS) Protocol Version 1.3. RFC 8446 (Proposed Standard), August 2018.
[53] Phillip Rogaway. Authenticated-encryption with associated-data.
In Vijayalakshmi Atluri, editor, ACM CCS 2002, pages 98–107.
ACM Press, November 2002.
[54] J. Schaad. CBOR Object Signing and Encryption (COSE): Struc- tures and Process. RFC 9052 (Internet Standard), August 2022.
[55] G. Selander, J. Mattsson, F. Palombini, and L. Seitz.
Object
Security for Constrained RESTful Environments (OSCORE). RFC 8613 (Proposed Standard), July 2019.
[56] G¨oran Selander, John Preuß Mattsson, and Francesca Palombini.
Ephemeral Diffie-Hellman Over COSE (EDHOC) – draft-ietf- lake-edhoc-17. https://tools.ietf.org/html/draft-ietf-lake-edhoc-17,
October 2022.
[57] Mali˘sa Vu˘cini´c, G¨oran Selander, John Preuss Mattsson, and
Thomas Watteyne. Lightweight authenticated key exchange with
EDHOC. Computer, 55(4):94–100, 2022.
A. Cryptographic Primitives
A.1. Hash Functions
A hash function deterministically computes a short fingerprint for inputs of arbitrary length. In the context of EDHOC, the hash function’s primary usage is to hash the communication transcript, which is used to assert the authenticity of the key exchange and the peer.
Definition A.1. (Collision-resistant hash function) A hash function H : {0, 1}∗→{0, 1}λ, λ ∈N is a deterministic mapping H(m) = hm ∈{0, 1}λ, ∀m ∈{0, 1}∗. The rele- vant security notion is collision resistance (CR), namely the (in)feasibility of producing values m ̸= m′ such that
H(m) = H(m′) for a given adversary A. More precisely, collision resistance is captured by a game GCR
A (H). The advantage of A is defined as:
AdvCR
H (A) = Pr

(m, m′)
$←−A : H(m) = H(m′)
∧m ̸= m′

.
A.2. Pseudo-Random Functions
EDHOC generates multiple keys, IVs, and MAC tags from an already established session key using pseudo- random functions.
Definition A.2. (Pseudo-random function) A pseudo- random function F : K × X →Y is a deterministic function that takes as input a key k and a value x and outputs a value y. Intuitively, F is a PRF if for a randomly chosen key k, it is computationally indistinguishable from a function f : X →Y chosen uniformly at random from
Funcs[X, Y], the set of all functions from X to Y.
Security of PRFs.
We use the term “PRF” to refer to a function defined in this section and the associated security notion that we formalize next. Let A be any efficient distinguisher for F in the sense of the game
GPRF (Figure 6). We define A’s advantage against the
PRF security of F as follows:
AdvPRF
F
(A) = 2 · Pr

GPRF(F) →1

−1.
Key expansion as a PRF in EDHOC.
The Expand module in EDHOC defined as Expand(k, (label, context, len), len) (cf. Section 2.2.1 and [56, Section 4.1.2]) is a variable output length PRF that outputs bit strings of length len when queried on the key k and input label.
A.3. Key Derivation Functions
To derive the final key and other keys used dur- ing the key exchange, EDHOC uses a key derivation function. The key derivation in EDHOC closely follows 15

INITIALIZE()
1 : b
$
←−{0, 1} 2 : f
$
←−Funcs[X, Y]
3 : k
$
←−K
PRF(x)
1 : y0 = F (k, x)
2 : y1 = f(x)
3 : return yb
FINALIZE(b′)
1 : return b′ = b
Figure 6. The PRF security game GPRF(F) for a function F.
the design of HKDF [44], it is realized via two mod- ules. The first Extract(s, ikm) that extracts a pseudo- random key from ikm. The second module is the function
Expand(prk, info, len) that generates from the pseudo- random key prk another length-len pseudo-random key.
A.3.1. The Extract module. The output of the anony- mous Diffie–Hellman key exchange protocol is a group element, and its bitstring representation is usually not a uniform random variable. Hence, one needs a so-called extractor to extract a uniform random key. We note that
Krawczyk described assumptions required for the func- tion HKDF.Extract in [44]. In our analysis of EDHOC, we will rely on the PRF-ODH assumption described in
Appendix A.4.
A.3.2. The
Expand module.
Once a pseudo- random key prk is obtained from the extractor, one wishes to use it to generate other keys. The
Expand(prk, (label, context, len), len) module is used for this purpose. We assume that Expand is a PRF as defined in Appendix A.2.
A.4. Pseudo-Random
Function
Diffie–Hellman
Oracle Assumption
The PRF-ODH [15], [37] assumption has been in- troduced and used to analyze real-world Diffie–Hellman based key exchange protocols
(including
TLS 1.2,
TLS 1.3, Signal, Wireguard). In DH-based protocols, par- ticipants exchange DH shares xG, yG and compute the shared secret ss = DH(x, yG), which is further processed into a session key k with a key derivation function and other auxiliary inputs. The assumption arises naturally in such protocols in the presence of an active adver- sary who may, for instance, obtain one or more values ss′ = DH(v, xG) for an adversarially chosen v. Therefore, by the PRF-ODH assumption, we can consider the final session key k to be an independent pseudo-random value even though ss and ss′ are related in a nontrivial manner.
In EDHOC, we will rely on the snPRF-ODH security of the Extract function.
Definition A.3 (The snPRF-ODH assumption). Let G =
⟨G⟩be a cyclic group of order q, let F : G × X →Y be a PRF (see Appendix A.2) that takes a key k ∈G, an input x ∈X and outputs a value y = F(k, x) ∈Y. The snPRF-ODH assumption essentially states that F(k, ·) is a PRF keyed with k = u(vG) for (u, v)
$←−Z2 q. Similiarly to the usual PRF security notion, an adversary is given access to an oracle CHALL (once) that returns either the output of F or a uniform random value. In addition, the adversary is given uG, vG, and also access to an oracle U that can be called once on input (T, x) ̸= (vG, x∗) to compute F(T u, x). The security notion is made more for-
INITIALIZE()
1 : b
$
←−{0, 1} 2 : (u, v)
$
←−Z2 q 3 : return (uG, vG)
CHALL(x∗)
1 : y∗ 0 ←F (u(vG), x∗)
2 : y∗ 1
$
←−Y 3 : return y∗ b
FINALIZE(b′)
1 : return b = b′
U(T, x)
1 : if T /∈G :
2 :
return ⊥ 3 : if (T, x) = (vG, x∗) :
4 :
return ⊥ 5 : y ←F (uT, x)
6 : return y
Figure 7. The snPRF-ODH game GsnPRF-ODH(F). The adversary may call each of the oracles CHALL and U only once, and must call
CHALL first.
mal in the game GsnPRF-ODH (Figure 7). The advantage of an adversary A is defined as:
AdvsnPRF-ODH
F
(A) = 2 · Pr

GsnPRF-ODH(F) →1

−1.
The PRF-ODH assumption was studied in [15], and the authors showed that in the random oracle model, the strongest PRF-ODH variant is achievable under the strong Diffie–Hellman assumption.
PRF-ODH security of Extract.
Brendel et al. [15]
showed that HMAC is snPRF-ODH-secure in the random oracle model, i.e., it is a PRF F(k, x) = HMAC(x, k).
The authors remark that the results will likely apply if a sponge-based construction replaces the underlying hash function. However, in EDHOC, sponge-based hashes are not used within the HMAC construction. Instead,
EDHOC directly uses KMAC for MAC-ing and Shake128 or Shake256 for hashing and as XOFs. Therefore, it seems to be an open question whether we can also assume the use of KMAC in Extract snPRF-ODH-secure. In our analysis, we assume that this is the case.
A.5. Digital Signatures
A digital signature scheme allows a message sender
(and only them) to produce publicly verifiable proof that the message is authentic. In EDHOC, signatures are used to authenticate the peers.
Definition A.4 (Digital signature scheme). A digital sig- nature scheme S is a triple of efficiently computable algorithms (KGen, Sign, Vf) where:
•
KGen is a probabilistic algorithm that generates a signature key pair (sk, pk) ∈Ksk × Kpk.
•
Sign : Ksk × M →Σ is a (possibly proba- bilistic) algorithm that on input a signature key sk and a message m computes a signature σ
$←−
Sign(sk, m).
•
Vf : Kpk × M × Σ →{0, 1} is a deterministic algorithm that takes as input a public key pk, and a message m, and a signature σ and outputs a bit b = Vf(pk, m, σ). The output is 1 when the signature is valid and 0 otherwise.
Correctness.
∀(sk, pk)
$←−
KGen, m
∈
M
:
Pr[Vf(pk, m, Sign(sk, m))] = 1.
16

GEUF-CMA
INITIALIZE()
1 : (sk, pk) ←S.KGen 2 : M ←∅ 3 : return pk
FINALIZE(m, σ)
1 : return

S.Vf(pk, m, σ) = 1
∧m /∈M

SIGN(m)
1 : M ←M ∪{m} 2 : return S.Sign(sk, m)
GSUF-CMA
INITIALIZE(m)
1 : (sk, pk) ←S.KGen 2 : M ←∅ 3 : return pk
FINALIZE(m, σ)
1 : return

S.Vf(pk, m, σ) = 1
∧(m, σ) /∈M

SIGN(m)
1 : σ
$
←−S.Sign(sk, m)
2 : M ←M ∪{(m, σ)} 3 : return σ
Figure 8. The EUF-CMA game (top) and SUF-CMA game (bottom)
for a signature scheme S.
A.5.1. Security of Digital Signatures Schemes.
Definition A.5 (Existential unforgeability under cho- sen-message attacks). For a signature scheme S and an efficient adversary A, existential unforgeability under chosen-message attacks (EUF-CMA) is a security notion capturing A’s success in forging signatures for new mes- sages given access to a signing oracle (See Figure 8). The advantage of A is defined by:
AdvEUF-CMA
S
(A) = Pr

GEUF-CMA(S) →1

.
Definition A.6 (Strong unforgeability under chosen-mes- sage attacks). For a signature scheme S and an efficient adversary A, strong unforgeability under chosen-message attacks (SUF-CMA) is a security notion that captures A’ success in forging a new message-signature pair given access to a signing oracle (see Figure 8). We define A’s advantage as follows:
AdvSUF-CMA
S
(A) = Pr

GSUF-CMA(S) →1

.
A.6. Authenticated Encryption
An authenticated encryption scheme with associated data (AEAD) is an encryption scheme in which, given a message m and additional data ad, the scheme ensures confidentiality for m and integrity for both m and ad. In
EDHOC, AEAD is used to encrypt part of the handshake.
We use the nonce-based syntax for AEAD [53].
Definition A.7 (Nonce-based authenticated encryption with associated data). A nonce-based authenticated en- cryption scheme with additional data E is a triple of effi- ciently computable algorithms (KGen, Enc, Dec) where:
•
KGen is a probabilistic algorithm that generates a random key k ∈K.
•
Enc : K × M × AD × N →C = {0, 1}∗is a deterministic algorithm that takes a key k ∈K, a message m ∈M, an additional data ad ∈AD, a nonce n ∈N and returns a ciphertext c =
E.Enc(k, m, ad, n) ∈C.
•
Dec : K × C × AD × N →M ∪{⊥} is a deterministic algorithm that takes a key k ∈K, a ciphertext c ∈C, an additional data ad ∈AD, a nonce n ∈N and returns a message m ∈M or a distinguished error symbol ⊥.
Correctness.
We demand that for all k ∈K, m ∈M, ad ∈AD, n ∈N:
Dec(k, Enc(k, m, ad, n), ad, n) = m.
B. Full Proof of Theorem 5.1
We provide here a full proof for Theorem 5.1.
Proof. Let
A be an
MSKE-adversary against
EDHOC-Sig-Sig, we bound A’s advantage, denoted by AdvMSKE
EDHOC-Sig-Sig(A), with the following sequence of games.
B.1. Phase 1: Ensuring Soundness
GAME G0.
We start with the normal MSKE game de- fined in Figure 4 and played by A. By definition,
AdvG0(A) = AdvMSKE
EDHOC-Sig-Sig(A).
GAME G1.
In this game, we log all Diffie-Hellman shares chosen by honest sessions in a table Tdh. Addition- ally, we set the flag dhcoll to true whenever a collision occurs in Tdh, i.e., when two honest sessions sample the same DH key shares. These changes are not noticeable to the adversary, therefore:
AdvG1(A) = AdvG0(A).
GAME G2.
This game aborts whenever dhcoll is set.
Before dhcoll is set, G2 is equivalent to G1. By the identical-until-bad lemma of [7], the advantage difference of A can be bounded as follows:
|AdvG2(A) −AdvG1(A)| ≤Pr[dhcoll ←true].
We use the birthday paradox to bound Pr[dhcoll ←true].
Let q = |G| be the order of the prime-order group used in EDHOC-Sig-Sig and assuming that DH shares are chosen uniformly at random, we directly obtain the bound
Pr[dhcoll ←true] ≤nS 2 q , where nS is the total number of sessions. As a consequence:
|AdvG2(A) −AdvG1(A)| ≤nS 2 q .
Conclusion of Phase 1.
At this point, we argue that if
G2 does not abort, then the adversary A cannot cause the
Sound predicate to become false. Recalling the definition of the predicate Sound in our MSKE model (see Figure 5), there are six events, at least one of which must occur for
Sound to be false. In the following, we argue that if G2 did not abort, then none of the six events occurred.
Proposition B.1. At any given stage, no more than two sessions share the same session identifier.
Proof. We show that there is no “triple-partnering”.
Assume that ∃s, x, y, z : (x, y) ∈Ps, (x, z) ∈Ps, (y, z) ∈ 17

Ps, that is, sessions x, y, z are pair-wise partnered in stage s. We have three pairs of partnered sessions, but at most two DH shares12. We recall that in G2, the challenger aborts the game if such a situation occurs, which contradicts the assumption of triple partnering.
Therefore, from now on, we assume that at most two sessions are partnered.
Proposition B.2. Matching session identifiers for a given stage implies matching stage session keys.
Proof. We show that matching session identifiers implies that partnered sessions derive the same shared DH secret and transcript hashes, which is sufficient to compute the stage keys deterministically. We recall that the key sched- ule of EDHOC-Sig-Sig (Figure 3) starts by computing the key PRK2e = Extract(th2, Gxy), where Gxy is the shared
Diffie-Hellman secret. Hence, the equality of the session identifiers implies the equality of the derived PRK2e. The key schedule proceeds to derive further stage keys (and po- tentially associated IVs) using the Expand function keyed with PRK2e. For each key/IV, Expand is evaluated on an input composed of the (partial) transcript hash and a stage-specific label. By the definition of transcript hashes, the equality of session identifiers implies the equality of the transcript hash. Therefore, two partnered sessions at any stage s will always derive the same stage key and IV if the latter is required.
Proposition B.3. Matching stage session identifiers im- plies opposite roles.
Proof. Assume that not more than two sessions have the same session identifier for a given stage (Proposition B.1)
i.e., ∀s ∈S : ¬∃x, y, z : (x, y) ∈Ps ∧(x, z) ∈Ps ∧
(y, z) ∈Ps. Each session includes its DH share kG in the session identifier at a fixed position. Having Two sessions with the same session identifier and the same role at a given stage implies that the sessions sampled the same
DH key shares, which contradicts the uniqueness of the
DH key shares guaranteed at this point since G2 did not abort.
Proposition B.4. Matching session identifiers for a given stage implies agreed-upon contributive identifiers.
Proof. For any stage s ∈[1, 4], the session identifier for that stage includes the DH shares of both parties. We recall that the contributive identifiers for EDHOC-Sig-Sig are defined as follows: cid[init, 1] = (“1”, Gx) and for all roles r and stages s, cid[r, s] = (“s”, Gx, Gy). Therefore, matching session identifiers means agreement on the DH shares, which in turn means agreement on the contributive identifiers.
Proposition B.5. Matching session identifiers in authen- ticated stages implies that the partner session is intended.
Proof. Assuming that agreement on the session identifier
(sid[s]) for an authenticated stage s implies different roles
(see Proposition B.3), honest initiators and responders write their identity in the I/R placeholder in the session identifier. If these values are both honestly set, agreement on the session identifier implies agreement on the peer’s identity and respective roles.
12. Every session identifier includes two DH shares.
Proposition B.6. Session identifiers are different across stages.
Proof. For any stage s ∈[1, 4], the session identifier sid[s] = (“s”, . . .) is a sequence whose first element is
“s′′. For any t ̸= s, sid[t] = (“t′′, . . .) ̸= (“s′′, . . .).
Therefore, session identifiers are distinct across stages
B.2. Phase 2: Ensuring Explicit Authentication and Key Indistinguishability
We proceed with the second phase of our proof, as- suming that soundness is unconditionally guaranteed from now on. In this phase, we show that the adversary cannot win by breaking explicit authentication or distinguishing the challenge bit.
Preparing for our analysis of Phase 2, we introduce the following two games to exclude collisions in the partial transcript hashes. Moreover, from now on, we drop
EDHOC-Sig-Sig from advantage expressions for the sake of readability.
GAME G3.
In this game, we log the hash values com- puted by honest sessions in a table Thash that provides efficient lookups. Given an arbitrary value m, Thash maps
H(m) to m, that is, Tdh[h] ←m. Additionally, we set the flag hashcoll if an honest session computes a hash h on a value m such that h ∈Thash and Thash[h] ̸= m. These changes are unobservable to the adversary, therefore
AdvG3(A) = AdvG2(A).
GAME G4.
The G4 aborts whenever hashcoll is set.
Using the identical-until-bad lemma, we have that
|AdvG4(A) −AdvG3(A)| ≤Pr[hashcoll ←true].
We bound Pr[hashcoll ←true] using a reduction B4 to the collision resistance of H. B4 honestly, simulates G4 towards A; whenever hashcoll is set, B4 wins the collision resistance game by outputting the strings m ̸= m′ that caused the collisions. Therefore, Pr[hashcoll ←true] ≤
AdvCR
H (B4) and as consequence:
|AdvG4(A) −AdvG3(A)| ≤AdvCR
H (A).
At this point, we split the proof into two branches I and II, each starting from G4 and proceeding with the games GI and, GII respectively. In the first branch, the adversary attempts to break explicit authentication for at least one session; in the second branch, explicit authen- tication is unconditionally guaranteed, and the adversary attempts to guess the challenge bit. Since the two cases are disjoint, we have the following bound:
AdvG4
A ≤max(AdvGI
A , AdvGII
A ) ≤AdvGI
A + AdvGII(A).
We start with branch Branch I.
B.2.1. Branch I: The adversary cannot break explicit authentication. In this branch, we use a hybrid argument to analyze explicit authentication. Namely, we will zoom in on a single session for which A attempts to break explicit authentication. We will use the term targeted session to refer to the session for which the adversary attempts to break explicit authentication.
18

GAME GI.
Continuing from G4, in this game, we guess a session-stage pair
 πi
U, s
 such that ExplicitAuth eval- uates to false since the adversary broke explicit authentica- tion of πi
U in stage s. This restriction to a single targeted session and stage reduces the advantage by a factor of nS × S, where nS is the total number of sessions, and S is the number of stages. We therefore get the following:
AdvG4(A) ≤4nS · AdvGI(A).
From now on, πi
U refers to the targeted session.
GAME GI.1.
In this game, we log all messages signed by honest users in a table Tsig with efficient lookups, along with the corresponding public key and the signature produced. More precisely, for a (honest) user U that owns the long-term key pair (skU, pkU), let σ = Sign(skU, m)
be the signature computed on a message m, then Tsig is a list of tuples (m, σ, pkU, U). In concrete terms, an initiator session with identity I will sign a mes- sage of the form m3 = (lsig, kidI, th3, credI, ead3, τ3).
Whereas, the responder R will sign a message of the form m2 = (lsig, kidR, th2, credR, ead2, τ2). Due to cre- dential identifiers potentially referencing multiple creden- tials, protocol participants may have to verify the received signatures against multiple public keys. Upon receiving the protocol message msg2 that includes the credential identifier kidU, initiator sessions will attempt to validate the received signature σ2 against each public key pkU referenced by kidU, adapting the a priori signed message to the messages mU = (lsig, kidU, th2, credU, ead2, τ2).
These validation attempts are performed until for one public key Vf(pkU, σ2, mU) = 1; otherwise, the protocol is aborted. Similarly, responder sessions verify the signa- ture σ3 received within msg3 and all possible messages mU = (lsig, kidU, th3, credU, ead3, τ3) against each public key pkU.
In addition to logging messages, we set the flag sigforged if the targeted session receives and validates a message signature pair (m, σ) under the public key pkV of an honest13 user V such that (m, σ, pkV , V ) /∈Tsig. These changes are only administrative and are not observable by the adversary. Therefore:
AdvGI.1
A
= AdvGI(A).
GAME GI.2.
In this game, we abort whenever sigforged is set. We bound Pr[sigforged ←true] by a reduction
BI.2 to the SUF-CMA security of Sig. Namely, BI.2 first guesses the identity (V ) of the peer session which reduces the advantage by a factor nU and associates pkV with the public key pk∗from the SUF-CMA challenge i.e. pk∗= pkV . The reduction answers all game queries and calls its signing oracle whenever a query needs V to produce a signature. Upon sigforged being set, BI.2 outputs the message signature pair (m, σ) that caused sigforged to be set and aborts GI.2. See Section 5.2 for further discussion on the need for SUF-CMA security.
Simulation soundness. Besides REVLONGTERMKEY queries, BI.2 can consistently answer all queries. Next, we argue that REVLONGTERMKEY queries are of no concern. Indeed, after sigforged is set, we do not need 13. More precisely, we only expect that V is honest at the time the message-signature pair is received.
to answer this query. Before the flag is set, such a query does not help the adversary either. The ExplicitAuth predicate requires the value of revltk V designates a time after acceptance of the stage s′, where the stage s receives explicit authentication, perhaps retroactively. Since the tar- geted session must have accepted stage s′, which requires receiving and accepting a message-signature pair under pkV ; therefore, a REVLONGTERMKEY(V ) query before sigforged is unhelpful for the adversary in its quest to break explicit authentication. Hence, the reduction need not answer REVLONGTERMKEY queries.
Validity of the Forgery. By definition of Tsig, the flag sigforged is set only when the targeted session receives and accepts a message signature pair (m, σ) under a pkV such that (m, σ, pkV , V ) /∈Tsig. This implies that
(m, σ) is a new message-signature pair that V did not previously produce. Therefore, BI.2 produces a legitimate
SUF-CMA forgery, and we have the following:
Pr[sigforged ←true] = AdvSUF-CMA
Sig
(A).
And as a consequence:
|AdvGI.2(A) −AdvGI.1(A)| ≤nU · AdvSUF-CMA
Sig
(A).
GAME GI.3.
In this game, we set the flag sigambigous if there exists an honest session π that receives and accepts a message-signature pair (m′, σ) under a public key pkU ′, where a session of some user U produced σ on some other message m, and there exists a value kid such that
(pkU, U) ∈peerpk kid and (pkU ′, U ′) ∈peerpk kid. In other words, kid identifies both pkU and pkU ′; and for some m it holds that (m, σ, pkU, U) ∈Tsig. We view pkU ′ as a key chosen by the adversary A and registered using the query NEWUSER(skU ′, pkU ′, kid). From the standpoint of π, there is an ambiguity about the identity of the peer that (presumably) authenticated themselves via the received message signature pair (m′, σ). These changes are unobservable to the adversary, therefore:
AdvGI.3
A
= AdvGI.4(A).
GAME GI.4.
The game aborts whenever sigambigous is set. We first observe that for m and m′ as described in the previous game, it is always the case that m′ ̸= m. This is because each session signs a message that includes the user’s credentials, i.e., each user U ′ signs a message of the form (lsig, kidU ′, th, credU ′, ead, τ). Furthermore, the credentials are unique to each identity, and the CBOR encoding is unambiguous. Consequently, we can restrict our analysis to pkU ̸= pkU ′. If pkU = pkU ′, the attacker knows the secret key, or they have to devise a forgery since m is never signed by U. By definition of sigambigous, we can relate Pr[sigambigous ←true] to the advantage of an S-UEO adversary BI.4 against Sig. More precisely,
BI.4 associates pkU with the public key from the pk∗ received from the challenger S-UEO, i.e. pkU = pk∗.
The reduction uses the signing oracle of its challenger whenever a query needs U to sign a message; else, it responds to the other oracle queries in the usual manner.
It aborts the game when sigambigous is set.
Simulation soundness: We only need to consider the
REVLONGTERMKEY(U) queries, as the reduction can answer all other queries consistently. On the one hand, we 19

do not need to consider what happens after sigambigous is set. The simulation aborts and need not answer
REVLONGTERMKEY(U) queries. On the other hand, the predicate ExplicitAuth requires pkU is not compromised before the session π accepts stage s. Therefore, for our reduction, the REVLONGTERMKEY(U) queries are not a concern, and the simulation is sound.
Validity of the attack. If the flag sigambigous is set, π accepted and verified a message signature pair (m′, σ) un- der a public key pkU ′ and ∃t ∈Tsig : t = (m, σ, pkU, U).
As observed above, m ̸= m′; therefore, no honest ses- sion sought to sign m. As a consequence, the tuple
(m, m′, σ, pk, pk′) is a valid S-UEO forgery. Therefore, we get that
Pr[sigambigous ←true] ≤AdvS-UEO
Sig
(A).
Finally, we get:
|AdvGI.4(A) −AdvGI.3(A)| ≤nS · AdvS-UEO
Sig
(A).
Note.
The signature schemes in EDHOC are Ed25519 and ECDSA. The former is known to be S-UEO- secure [14]. Moreover, in EDHOC, the signing algorithm unambiguously places the public key of the message together with the actual message via the credential. There- fore, we could view the signature scheme (Sig) in EDHOC as another scheme c
Sig that takes a message and signs the message along with the corresponding verification key.
That is, for a key pair (sk, pk), the signing algorithm is modified and behaves as follows: c
Sig.Sign(sk, m) =
Sig.Sign(sk, (m, pk)). Pornin and Stern [51] showed that unambiguous inclusion of the verification key is enough to thwart S-UEO attacks, provided there are no weak keys. This property holds for ECDSA, assuming that the concrete implementation of ECDSA performs all the necessary checks to prevent ”weak keys.” Finally, we note that Destructive Ownership would be sufficient.
Establishing ExplicitAuth = true.
At this point, we argue that if GI.4 does not abort, then the adversary cannot win by causing the predicate ExplicitAuth to evaluate to false.
The predicate ExplicitAuth and its negation are shown in Figure 9 for illustration. When explicit au- thentication is violated (¬ExplicitAuth in Figure 9), the following holds:
1)
πi
U accepted stage s (resp. s′) at time t (resp. t′).
The session accepts with a peer identity πi
U.pid =
V (one must be set).14 2)
V ’s long-term secret was not compromised at time t′.
3)
(I.a) Either, no (honest) session πj
V is partnered with πi
U in stage s′.
4)
(I.b) Or, There exists an honest session πj
V that is partnered with πi
U in stage s′; however, the two sessions are not partnered in stage s.
For an initiator session, stages 2, 3, and 4 are explicitly authenticated once stage 2 is accepted; stage 1 receives au- thentication retroactively. For a responder session, stages 3 14. Note that we can focus on potential partner sessions owned by πi
U.pid = V , as sessions πk
V ′ for V ′ ̸= V trivially satisfy the
πi
U.pid ̸= V of the ∀clause of ¬ExplicitAuth.
and 4 are explicitly authenticated once stage 3 is accepted; previous stages receive authentication retroactively. Re- gardless of the role, each session must have received a valid signature σ on a MAC tag before accepting the relevant s’th stage. Concretely, an initiator session with identity I must have received from its responder peer with identity R a valid signature σ2 within the message msg2, where σ2 is computed over a message of the form m2 = (lsig, kidR, th2, credR, ead2, τ2). The responder ses- sion must have received a signature σ3 over the message m3 = (lsig, kidI, th3, credI, ead3, τ3) within the message msg3. The attacker breaks explicit authentication if either case (I.a) or (I.b) occurs. We address the possibility that either event occurs.
Case (I.a).
The targeted session, πi
U, accepted a message signature pair (m, σ) under the public key of V , i.e.,
Vf(pkV , m, σ) = 1, but no session πj
V is partnered with
πi
U in stage 2 (resp. stage 3) if πi
U is the initiator (resp.
responder). We consider two cases that we call (i) and
(ii), based on whether the message and signature received by πi
U verifies the following: (m, σ, pkV , V ) /∈Tsig. By the definition of case (i), no honest session produced the pair of message signatures (m, σ). Therefore, the adversary must have forged a signature. At this point, if GI.2 did not abort, then the adversary could not have forged a signature. If case (ii) occurs, an honest session πj
V produced the message signature pair received and accepted by πi
U. In particular, if πi
U is in the initiator role, the message (lsig, kidR, th2, credR, ead2, τ2) was signed (resp.
verified) by πj
V (resp. πi
U). Hence, πi
U and πj
V agree on the values of σ2, kidR, ead2 in sid[2]. Additionally, they also agree on the values of th2 = H(Gy, CR, H(msg1)).
Thanks to G4, partial collisions in transcript hashes are excluded. Therefore, πi
U must also agree on the values of Gy, CR, and and therefore agree on their respective stage-2 session identifiers and are partnered in stage 2, contradicting the assumption that πi
U does not have a partner session in stage 2. Analogously, if πi
U is a respon- der session (πj
V is an initiator), the message signed is of the form m3 = (lsig, kidI, th3, credI, ead3, τ3). Therefore, there is agreement on the values of σ3, kidI and ead3.
Furthermore, agreement on th3 = H(th2, ptxt2, credR)
implies agreement on the remaining values of the stage 3 session identifiers, thanks to G4.
Finally, suppose that the targeted session πi
U is in the responder role. The attacker can cause case (ii) to occur by mounting an attack against the intended initiator session πj
V such that πj
V would accept with a malicious peer identity U ′ while not modifying the conversation transcript. The subtlety of this attack is that although πj
V has been “tricked” into accepting with an unintended peer, the adversary does not, in fact, break explicit authentica- tion for πj
V ; the adversary broke explicit authentication for the responder session πi
U. At the end of the protocol run, πi
U ends up without a partner in stage 2 and above; hence πi
U is indeed the targeted session. We expand a bit more on the details of this attack that exploit ambiguity about the identity of the responder πi
U. Upon receiving msg2 from πi
U, A registers a new key pair by calling
NEWUSER(skU ′, pkU ′, kidU). The malicious key pair is selected such that πj
V would accept σ2 under pkU ′ when delivered via the relevant SEND query. Careful observation 20

ExplicitAuth :=
∀(πi
U, s, s′) :






























πi
U.accepted[s]
∧ eauth[πi
U.role, s] = s′ < ∞
∧
πi
U.accepted[s′] < revltk πi
U.pid





=⇒
∃πj
V :





πi
U.pid = V
∧
πi
U.sid[s′] = πj
V .sid[s′]
∧
πj
V .accepted[s] < revltk πi
U.id
=⇒
πi
U.sid[s] = πj
V .sid[s]






























.
¬ExplicitAuth :=
∃(πi
U, s, s′) :






























πi
U.accepted[s]
∧ eauth[πi
U.role, s] = s′ < ∞
∧
πi
U.accepted[s′] < revltk πi
U.pid





^
∀πj
V :





πi
U.pid ̸= V
∨
πi
U.sid[s′] ̸= πj
V .sid[s′]
∨
πj
V .accepted[s] < revltk πi
U.id
∧
πi
U.sid[s] ̸= πj
V .sid[s]






























.
Figure 9. The top predicate corresponds to explicit authentication (predicate ExplicitAuth) being satisfied, the bottom predicate is its negation and corresponds to explicit authentication being violated; used when establishing ExplicitAuth = true in the proof in Game GI.4.
of the protocol specification reveals that such an attack would not disturb the protocol run. However, the result is an identity misbinding attack.
Thanks to GI.4, ambiguity about the responder of the initiator is excluded. Furthermore, if the initiator ses- sion πj
V accepts another peer identity U ′, the value of th3 computed by πi
U (resp. πj
V ) are H(th2, ptxt2, credU)
(resp. H(th2, ptxt2, credU ′)). These are different values, and since honest sessions only sign transcript hashes corresponding to their session identifiers, the adversary must come up with a new forgery for πi
U to later accept msg3.
We have shown that case (I.a) does not occur. Next, we analyze the case (I.b).
Case (I.b).
Let s′ be the stage in which πi
U receives explicit authentication. Recall that s′ = 2 if πi
U is in the initiator role and s′ = 3 if πi
U is in the responder role. For a given stage s ∈[1, 4], we use sid[s] to denote the sub- sequence of sid[s] that does not contain the stage label.
We proceed with this analysis stage by stage, assuming that πi
U.sid[s′] = πj
V .sid[s′].
•
Stage 1. This stage receives retroactively explicit authentication upon acceptance of stage 2 for ini- tiator sessions and upon acceptance of stage 3 for responder sessions. Assuming that πi
U.sid[s′] =
πj
V .sid[s′], we also know that sid[1] ≺sid[s] for s ∈{2, 3}. Therefore, case (I.b) cannot occur for s = 1.
•
Stage 2. For initiation sessions, case (I.b) is triv- ially impossible since s = s′ = 2. For responder session, sid[2] ≺sid[3] and thus case (I.b) cannot occur.
•
Stage 3. In case πi
U is in the responder role, then case (I.b) is trivially excluded since s = s′ = 3.
For an initiator session, the only possible diver- gences in πi
U.sid[3] and πj
V .sid[3] are (i) different values in the field corresponding to msg3 or (ii)
different values in the initiator placeholder po- sition (I). Case (i) comprises modifications that would require the adversary to forge a signa- ture; since honest sessions only sign messages in transcript hashes that correspond to their ses- sion identifiers, and the predicate ExplicitAuth requires that πi
U’s long-term secret, skU, is not comprised before πj
V accepts stage 3. Therefore, case (i) is prevented thanks to GI.2 where forg- eries are excluded. Case (ii) requires that the at- tacker can create ambiguity about the initiator’s identity. Namely, the attacker would have to mount an attack such that πj
V accepts the peer identity U ′ after receiving msg3. Thanks to GI.4, this cannot occur.
•
Stage 4. We observe that sid[4] = sid[3]. There- fore, the analysis of stag 4 is identical to the analysis of stage 3.
Since adversaries A cannot break explicit authentica- tion, they can no longer win in this branch of the proof.
Thus,
AdvGI.4(A) ≤0.
Conclusion of Branch I.
We have shown that the adver- sary cannot break explicit authentication. We now analyze the key secrecy properties of stage keys in EDHOC, assuming that the predicate ExplicitAuth is always true.
We do so by showing that the challenge bit is random and independent of the adversary’s guess.
B.2.2. Branch II: Ensuring that the challenge bit is random and independent of the adversary’s guess.
GAME GII.
Continuing from G4, in this game, we restrict the adversary A by allowing a single TEST query.
From this point on, we assume that the tested session is known in the subsequent games, and we will talk of the tested session, πi
U. We follow the approach of Dowling 21

et al. [31] who presented a careful hybrid argument for their analysis of TLS 1.3 and argued that this restriction reduces the advantage of A by a factor at most nS · S.
Here, nS is the number of sessions, and S = 4 is the number of stages. Therefore, we get the following bound:
AdvG4
A ≤4nS · AdvGII(A).
We proceed with our analysis of Branch II by consid- ering two disjoint cases. Namely,
•
Case A: the tested session does not have a (honest)
contributive partner in the first stage, i.e.,
∀π ̸= πi
U : πi
U.cid

πi
U.role, 1

̸= π.cid

πi
U.role, 1

.
•
Case B: The tested session has a (honest) con- tributive partner in the first stage, that is,
∃π ̸= πi
U : πi
U.cid

πi
U.role, 1

= π.cid

πi
U.role, 1

.
Since the two cases above are disjoint, we can bound
A’s advantage as follows:
AdvGII(A) ≤AdvGII case A(A) + AdvGII case B(A).
Case A: The tested session has no contributive partner.
As a first observation, the adversary cannot test for unau- thenticated stages; such a test query is considered non- fresh in the model (see Figure 5). In particular, A may not test stage 1 nor stage 2 in the case of a responder session.
TEST queries are only allowed from stage 2 onward for an initiator session and from stage 3 onwards for a responder.
Having established the appropriate restrictions on TEST queries, we now analyze the conditions under which a session accepts a stage that can be legally tested. For an initiator session, acceptance of stage 2 is predicated on the reception of a valid tuple (σ2, kidR, ead2) con- taining a signature and a key identifier. Analogously, a responder session accepts stage 3 only if it received a valid triple (σ3, kidI, ead3). Finally, we also observe that a TEST query is allowed only before the long-term key of
πi
U’s peer is compromised, that is, TEST must be issued before REVLONGTERMKEY(πi
U.pid). Based on the three observations previously made, one sees that a prerequisite for A to have a chance of winning the game is to be able to send valid messages and signatures to the tested session on behalf of honest users. In the next game hops, we analyze A’s likelihood of causing such an event.
GAME GII.A1.
In this game, we set a flag sigforged whenever the tested session πi
U in the role of initiator
(resp. responder) receives a tuple (kidR, σ2, ead2) (resp.
(kidI, σ3, ead3)) such that the signature verifies under an honest public key pkV ∈peerpk kidR (resp. peerpk kidI).
These changes are only administrative and unobservable to A, therefore:
AdvGII.A1
A
= AdvG4(A).
GAME GII.A2.
The Game GII.A2 aborts whenever sigforged is set. By the identical-until-bad lemma, we have that
|AdvGII.A2(A) −AdvGII.A1(A)| ≤Pr[sigforged ←true].
We bound Pr[sigforged ←true] by a reduction BII.A2, to the EUF-CMA security of the signature scheme. BII.A2, an EUF-CMA adversary, emulates GII.A2 towards A. To this end, BII.A2 first guesses the identity V of πi
U’s peer, and associates the challenge public key pk∗to V ’s long- term verification key, i.e. pkV = pk∗. Consequently, A’ s advantage is reduced by a factor nU where nU is the total number of users. For each SEND query that requires V to produce a signature, BII.A2 queries its signing oracle with the message to be signed. Otherwise, BII.A2 answers the remaining queries from GII.A2 as appropriate. Finally, if sigforged is set, BII.A2 outputs the relevant message- signature pair (m, σ) as its forgery towards its EUF-CMA challenger. Here, σ is the signature value received by the tested session, and m is the message for which the tested session verified the signature.
Simulation soundness. We argue that BII.A2’s sim- ulation of GII.A2 is sound. First, we observe that
BII.A2 can perfectly answer all queries in GII.A2 but
REVLONGTERMKEY(V ) given that the secret key cor- responding to pkV = pk∗is unknown. However, BII.A2 does not need to be able to answer such queries. Namely, if such a query is issued before acceptance of the tested stage, the test query is now non-fresh, and the attacker loses the game. On the other hand, BII.A2 cannot be bothered by REVLONGTERMKEY(V ) queries issued after sigforged is set. By then, BII.A2 has a valid forgery for the EUF-CMA game and can abort the game. This shows that until sigforged is set, the GII.A2 and GII.A1 are equivalent, and the simulation is sound.
Validity of the forgery. Having shown simulation soundness, it remains to show that (m, σ) is a valid forgery, that is, when
BII.A2 outputs
(m, σ), the
EUF-CMA challenger also outputs 1. In EDHOC, signa- tures are computed on (amongst other things) the MAC tag
(τ) and the transcript hashes (th). More precisely, the mes- sages to be signed is m = (lsig, kidU, th, credU, ead, τ).
credU is the credential of U that contains pkU and U’s unique identity. Recall that for signature verification, when an initiator (resp. responder) session receives message 2
(resp. message 3), the session may verify the signature against multiple public keys if the received kidU refers to multiple credentials. In this case, for each credX associated with kidU, the message(s) to be verified is mX = (lsig, kidU, th, credX, ead, τ) until one verification is successful. Due to the game G4, collisions in the transcript hashes are excluded if G4 did not abort. This implies that without a contributive partner, no honest session signed the message that the tested session received and accepted after successfully validating the signature.
As a result, given the challenge (EUF-CMA) public key pk∗, BII.A2 can verify that the pair (m, σ) is a valid forgery; allowing BII.A2 to abort the game and present
(m, σ) to the challenge EUF-CMA. Therefore, we have:
Pr[sigforged ←true] ≤nU · AdvEUF-CMA
Sig
(A).
It follows that:
|AdvGII.A2(A) −AdvGII.A1(A)| ≤nU · AdvEUF-CMA
Sig
(A).
At this point, we remark that if sigforged is never set, then the tested session without a contributive partner never accepts either stage 2 or stage 3. Consequently, an attacker 22

cannot make a valid TEST query, and their guess bit b′ is truly independent of the challenge bit b.
Case B: The tested session has a contributive partner.
GAME GII.B1.
In this game, we guess the session πj
V that is contributive partner of the tested session πi
U. This step reduces the advantage of A by a factor nS and we get:
AdvG4(A) ≤nS · AdvGII.B1(A).
From this point on, we consider the games to have a specified tested session and its partner at the outset.
GAME GII.B2.
In this game, we replace PRK2e com- puted by the tested session with a uniform random value
^
PRK2e
$←−KPRK2e. where KPRK2e is the key space of
PRK2e. We note here that the cid partner is not guaranteed to have received the honest DH shares from the tested session; namely, if the cid partner is in the initiator role, the adversary A could have delivered a malicious share, for which A could even know the corresponding secret scalar. Therefore, we also replace PRK2e at the contribu- tive partner with the same ^
PRK2e only if the contributive partner holds the same DH shares as the tested session. To justify this step, we exhibit a reduction to an snPRF-ODH adversary BII.B2 which, at a high level, receives Diffie-
Hellman shares from its challenger and encodes them in the shares Gx and Gy used by the partnered sessions.
Simulation soundness. BII.B2 simulates GII.B2 to- wards A and must answer all queries consistently. The queries of interest here are SEND queries that induce the computation of the PRK2e at the tested session πi
U and eventually at its partnered session πj
V . BII.B2 consistently answers all other queries. We observe that if the tested session is in the initiator role, then πi
U and πj
V have the same ^
PRK2e. If, however, πi
U is a responder session, πj
V may have received a modified G′ y for which the attacker knows the private scalar z such that G′ y = zG. BII.B2 must be able to compute xzG, which is achievable given access to the ”left” PRF-ODH oracle Ox(S, v). Finally, we observe that in EDHOC, A is only allowed to deliver a potentially modified G′ y once to πj
V ; this implies that the reduction only needs access to a single Ox(S, v) query.
Details of the reduction. BII.B2 receives DH shares uG and vG from its snPRF-ODH challenger and simu- lates GII.B2 towards A answering all queries unrelated to PRK2e as needed. BII.B2 encodes the received DH shares (uG, vG) into the Diffie–Hellman shares (Gx, Gy)
of the tested session and its partner, respectively. To derive
PRK2e, BII.B2 makes a PRF query on input th2 (recall that PRK2e = Extract(th2, Gxy)) and copies the result into the state of the tested session. BII.B2 copies PRK2e into the state of the contributive partner if it received the
DH share Gy. If the partner session receives a modified
G′ y, BII.B2 calls the left oracle Ox(S, v) on the inputs
S = G′ y and v = H(G′ y, CR, H(Gx, CI, ead1)).
As a consequence, the advantage difference between
GII.B1 and GII.B2 can be bounded by the advantage of the snPRF-ODH adversary BII.B2, and we get:
|AdvGII.B2(A) −AdvGII.B1(A)| ≤AdvsnPRF-ODH
Extract
(A).
GAME GII.B3.
In this game, we replace the function
Expand keyed with ^
PRK2e with a random function F at the tested session. The contributive partner also replaces
Expand with F only if it received honest DH shares. We justify this step by relating and bounding the advantage difference of A to the advantage of an PRF adversary
BII.B3. BII.B3 simulates GII.B3 towards A, answering all queries that do not trigger a call to Expand. To answer queries that require deriving any key, IV, or MAC tag derived from PRK2e, BII.B3 queries its PRF oracle with the appropriate input. By the Game GII.B2, we have replaced PRK2e by a random value, and each key, IV, or MAC tag is computed with a unique and distinct label. Therefore, the simulation is sound, and we get the following:
|AdvGII.B3(A) −AdvGII.B3(A)| ≤AdvPRF
Expand(A).
Having replaced Expand with a random function F, we can readily replace all values derived by the tested session using a call to Expand with uniform random values. Again, we replace these values in the partner session only if it received an honest DH share. Con- cretely, we replace in the tested session (and possibly in the contributing partner) the keys (K2, K3, K4, PRKout), the initialization vectors (IV3, IV4), and the mac tags
(τ2, τ3) with values drawn at random from the corre- sponding domains. We call the newly sampled values f
K2, f
K3, f
K4, ^
PRKout, f
IV3, f
IV4, eτ2, eτ3. Since all values are derived in EDHOC by evaluating the random function
F on a unique input per value, F produces independent random values. Here, one may object that the key spaces
Kk, k ∈{K2, K3, . . . , τ3} may be different; therefore, it is not clear that F can produce random values from each key space. We note that Kk = {0, 1}klen, where klen is the length of k. Furthermore, we assume that F is a variable-length random function with output space
{0, 1}∗. Therefore, all keys can be computed accordingly.
Remark. At this stage, all keys are random values independent of the challenge bit b, and it remains to argue that REVSESSIONKEY queries do not help the adversary.
Interestingly, keys may not necessarily be independent when sessions are not partnered. The following problem may arise in EDHOC: With credential identifiers (kid)
that can refer to multiple identities and associated public keys, a session may believe they are talking to a session with a different identity than the one involved in the protocol. By the definition of the session identifiers, the two sessions will no longer be partnered. However, the two sessions will derive the same stage keys. Therefore, the adversary may use REVSESSIONKEY queries to guess the challenge bit with high probability. Fortunately, EDHOC includes the identities in the transcript hashes. Therefore, disagreement on the peer’s identity leads to divergent keys.
Conclusion of Branch II.
Given that the adversary does not break explicit authentication in this branch of the proof, we conclude that the challenge bit is random and independent of the adversary’s guess. Therefore:
AdvGII.B3(A) ≤0.
To summarize the proof:
1)
Sound.
As discussed in the conclusion of
Phase 1, the predicate Sound remains true.
23

2)
ExplicitAuth. As discussed in the conclusion of
Phase 2, Branch I, the predicate ExplicitAuth remains true.
3)
Key secrecy. As discussed in the conclusion of
Phase 2, Branch II, the adversary A cannot guess the challenge bit with non-negligible probability, which proves that the stage keys are indistin- guishable from uniform random values.
Therefore, we have shown that all the security properties defined in our MSKE model for EDHOC-Sig-Sig hold, which concludes the proof of Theorem 5.1.
C. Identity Misbinding in MAc-then-SIGn
Under Strong Adversaries
In the following, we discuss an identity misbinding attack in our model on the MAc-then-SIGn protocol [43], hereafter denoted by SIGMA σ
τ for “MAC under the sig- nature”.15 We stress that this attack does not contradict the original security analysis of SIGMA’s MAc-then-SIGn variant by Canetti and Krawczyk [19]; it arises through giving an adversary the ability to register its own ma- licious keys in the key exchange model, as our model does to capture the potential ambiguous interpretation of credential identifiers in EDHOC (cf. Section 4).
The core issue is caused by a lack of explicit ver- ification of the MAC tag; instead, the tag is implicitly verified through the verification of the signature. The original analysis [19] requires that a secure instantiation must use an unforgeable signature scheme. We show that for the security of SIGMA σ
τ against adversaries that can register malicious keys, it is not enough for the signa- ture scheme to be EUF-CMA secure; it must indeed be unforgeable for all keys. In particular, there cannot be any weak key, for instance, one that accepts any message- signature pair. We note that this observation is in line with a remark by Pornin and Stern [51] that weak keys can lead to DSKS/exclusive ownership attacks. (An alternative approach, which is beyond the scope of this work, would be to establish security for SIGMA σ
τ under an exclusive ownership property of the signature scheme, akin to our
EDHOC analysis.)
THE SETUP.
Recall that in SIGMA σ
τ , the initiator sends the first message (Gx). The responder picks its own
DH share Gy and computes a shared session key K and a MAC key Km from Gxy using a key derivation function. It responds with the second protocol message
(R, Gy, σR = Sign(skI, Gx, Gy, MAC(Km, R))).16
The initiator completes the key exchange by sending the third message, (I, σI = Sign(skI, Gy, Gx, MAC(Km, I))).
Assume now that the attacker intercepts the second message and modifies the responder’s identity to some R′; i.e., sends to the initiator the message (R′, Gy, σ). For the identity R′, the adversary has registered a weak verification key pk such that for all messages m and signatures σ, Vf(pk, m, σ) = 1. As a consequence, the attacker need not know the MAC key, yet the initiator will accept the signature with peer identity R′. Furthermore, the attack modifies the second message only; in particular, 15. For simplicity, we exclude identity protection from our treatment.
16. We omit further distinguishing label inputs for clarity.
it does not modify the keys computed by the initiator and the responder. Hence, the responder successfully accepts the initiator’s final message—which the adversary relays unmodified. The result is an identity misbinding attack:
initiator I and responder R share the same session key, but the initiator (incorrectly) thinks it is talking to R′, while the responder correctly deems I as its peer.
THE ISSUE.
At a high level, in MAc-then-SIGn, peers do not explicitly prove knowledge of the key via the
MAC. Instead, the MAC is only implicitly verified once the signature is accepted. The insufficiency of the standard
EUF-CMA unforgeability notion is that it only captures
“average-case” unforgeability, i.e., for an honestly, ran- domly generated key. In contrast, the attack described here requires unforgeability essentially for all keys, as the adversary is able to register them with the key exchange game.
Formally, EUF-CMA security is insufficient by the following separating example. Let Sig be a EUF-CMA secure signature scheme. Define c
Sig such that the key space of c
Sig is the key space of Sig augmented with the special key pair (sk∗, pk∗). Signing in c
Sig is as before unless the signing key is sk∗, in which case a random signature value is returned. The verification algorithm is also the same, except that when the verification key is pk∗, verification always returns 1. Observe that c
Sig is still
EUF-CMA as the advantage of any EUF-CMA adversary is only increased by the probability that the challenge key pair happens to be (sk∗, pk∗), which for practical key spaces of Sig is small. However, the SIGMA σ
τ protocol is clearly vulnerable to the attack described above if instantiated with c
Sig.
24