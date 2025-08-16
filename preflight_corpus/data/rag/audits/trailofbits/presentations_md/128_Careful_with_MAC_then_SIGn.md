# Careful with MAc-then-SIGn:

A Computational Analysis of the EDHOC Lightweight
Authenticated Key Exchange Protocol
Felix G¨unther and Marc Ilunga
Felix G¨unther and Marc Ilunga
EDHOC

Context and Motivation
Proliferation of low-powered devices
Image by Moritz Kindler
Limited computing power
Bandwidth constraints
Plagued by vulnerabilities1 1Burgess, “Smart dildos and vibrators keep getting hacked – but Tor could be the answer to safer connected sex”.
Felix G¨unther and Marc Ilunga
EDHOC 1 / 15

Context and Motivation
Proliferation of low-powered devices
Image by Moritz Kindler
Limited computing power
Bandwidth constraints
Plagued by vulnerabilities1 1Burgess, “Smart dildos and vibrators keep getting hacked – but Tor could be the answer to safer connected sex”.
Felix G¨unther and Marc Ilunga
EDHOC 1 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
Authenticated Key Exchange (AKE) for constrained environments remains an issue
Missing satisfactory solutions
EDHOC: a proposal by the IETF LAKE WG
Use case: OSCORE1 protocol (secure transport)
4 mutual authentication methods (static DH and/or Signature)
This talk: SIG-SIG
Design similar to TLS1.3 and based on SIGMA2 1Selander et al., Object Security for Constrained RESTful Environments (OSCORE).
2Krawczyk, “SIGMA: The “SIGn-and-MAc” Approach to Authenticated Diffie-Hellman and Its Use in the IKE Protocols”.
Felix G¨unther and Marc Ilunga
EDHOC 2 / 15

Context and Motivation
TLS 1.3 is a secure authenticated key exchange protocol
Q: Why not simply use TLS 1.3?
A: It is not lightweight enough!
Felix G¨unther and Marc Ilunga
EDHOC 3 / 15

Context and Motivation
TLS 1.3 is a secure authenticated key exchange protocol
Q: Why not simply use TLS 1.3?
A: It is not lightweight enough!
Felix G¨unther and Marc Ilunga
EDHOC 3 / 15

Context and Motivation
(D)TLS 1.3 is not lightweight: up to 7x bandwidth usage
Total protocol size (bytes)1
DTLS 1.3 (ECDHE)
880
TLS 1.3 (ECDHE)
789
EDHOC (STAT-STAT)
101 1Mattsson, Palombini, and Vuˇcini´c, Comparison of CoAP Security Protocols.
Felix G¨unther and Marc Ilunga
EDHOC 4 / 15

EDHOC in SIG-SIG Mode: An AKE based on Diffie-Hellman
Gx
,
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
Initiator(2)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC in SIG-SIG Mode: An AKE based on Diffie-Hellman
Gx
,
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
Initiator(2)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC in SIG-SIG Mode: An AKE based on Diffie-Hellman
Gx
Gy, idB, σ2
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
τ2 ←MACKm(idB)
σ2 ←Sign(skR, τ2 . . .)
Initiator(2)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC in SIG-SIG Mode: An AKE based on Diffie-Hellman
Gx
Gy, idB, σ2 idW , σ3
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
τ2 ←MACKm(idB)
σ2 ←Sign(skR, τ2 . . .)
Initiator(2)
τ3 ←MACKm(idW )
σ3 ←Sign(skI , τ3 . . .)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC in SIG-SIG Mode: An AKE with identity protection
Gx
Gy, {idB, σ2}K2
{idW , σ3}K3,IV3
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
τ2 ←MACKm(idB)
σ2 ←Sign(skR, τ2 . . .)
Initiator(2)
τ3 ←MACKm(idW )
σ3 ←Sign(skI , τ3 . . .)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC in SIG-SIG Mode: An AKE ≈SIGMA
Gx
Gy , idB, σ2 idW , σ3
Initiator (1)
x
$←−Zq; Gx ←xG
Responder(1)
y
$←−Zq; Gy ←yG
τ2 ←MACKm(idB)
σ2 ←Sign(skR, τ2 . . .)
Initiator(2)
τ3 ←MACKm(idW )
σ3 ←Sign(skI , τ3 . . .)
Felix G¨unther and Marc Ilunga
EDHOC 5 / 15

EDHOC SIG-SIG ≈SIGMA: MAC ”under” signature
Gx
Gy, idB, σ2 idW , σ3
τ2 ←MACKm(idB)
σ2 ←Sign(skR, τ2 . . .)
0Selander, Mattsson, and Palombini, Ephemeral Diffie-Hellman Over COSE (EDHOC) – draft-ietf-lake-edhoc-17, Section 3.5.3.
Felix G¨unther and Marc Ilunga
EDHOC 6 / 15

EDHOC SIG-SIG ≈SIGMA: Abbreviated identities
Gx
Gy, idB, σ2 idW , σ3 idX Short credential identifier for X size ≪X.509 Cert need not be unique1 applications MUST NOT assume that
’kid’ values are unique and several keys associated with a ’kid’ may need to be checked [by the recipient] before the correct one is found.
1Selander, Mattsson, and Palombini, Ephemeral Diffie-Hellman Over COSE (EDHOC) – draft-ietf-lake-edhoc-17, Section 3.5.3.
Felix G¨unther and Marc Ilunga
EDHOC 6 / 15

EDHOC SIG-SIG ≈SIGMA: Abbreviated identities
Gx
Gy, idB, σ2 idW , σ3 idX Short credential identifier for X size ≪X.509 Cert need not be unique1 applications MUST NOT assume that
’kid’ values are unique and several keys associated with a ’kid’ may need to be checked [by the recipient] before the correct one is found.
1Selander, Mattsson, and Palombini, Ephemeral Diffie-Hellman Over COSE (EDHOC) – draft-ietf-lake-edhoc-17, Section 3.5.3.
Felix G¨unther and Marc Ilunga
EDHOC 6 / 15

Abbreviated identifiers introduce new challenges
Gx
Gy, idB, σ2
What if an attacker also uses idB?
Duplicate Signature Key Selection attacks.
RunInit2
. . .
foreach (U, pkU) with idU = idB :
τ2 ←MAC(idU, . . .)
if Sig.Vf(pkU, τ2 . . . , σ2) = 1 :
pid ←U; endforeach abort if pid = ⊥
. . .
Felix G¨unther and Marc Ilunga
EDHOC 7 / 15

Abbreviated identifiers introduce new challenges
Gx
Gy, idB, σ2
What if an attacker also uses idB?
Duplicate Signature Key Selection attacks.
RunInit2
. . .
foreach (U, pkU) with idU = idB :
τ2 ←MAC(idU, . . .)
if Sig.Vf(pkU, τ2 . . . , σ2) = 1 :
pid ←U; endforeach abort if pid = ⊥
. . .
Felix G¨unther and Marc Ilunga
EDHOC 7 / 15

Abbreviated identifiers introduce new challenges
Gx
Gy, idB, σ2
What if an attacker also uses idB?
Duplicate Signature Key Selection attacks.
RunInit2
. . .
foreach (U, pkU) with idU = idB :
τ2 ←MAC(idU, . . .)
if Sig.Vf(pkU, τ2 . . . , σ2) = 1 :
pid ←U; endforeach abort if pid = ⊥
. . .
Felix G¨unther and Marc Ilunga
EDHOC 7 / 15

DSKS attacks: Signature unforgeability is not enough
EUF-CMA ⇏cannot find (pk∗, m∗):
Sig.Vf(pk∗, m∗, σ) = 1 (For honestly generated σ)
Andrew Ayer, 2015: DSKS attack in the ACME protocol with RSA signatures impacts Let’s Encrypt
Felix G¨unther and Marc Ilunga
EDHOC 8 / 15

DSKS attacks: Signature unforgeability is not enough
EUF-CMA ⇏cannot find (pk∗, m∗):
Sig.Vf(pk∗, m∗, σ) = 1 (For honestly generated σ)
Andrew Ayer, 2015: DSKS attack in the ACME protocol with RSA signatures impacts Let’s Encrypt
Felix G¨unther and Marc Ilunga
EDHOC 8 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
Gx
Gy, idB, σ2
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
NewUser(skA, pkA, idW )
Vf(pkA, ∗, ∗) = 1
Gx
Gy, idB, σ2
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
NewUser(skA, pkA, idW )
Vf(pkA, ∗, ∗) = 1
Gx
Gy, idB, σ2 idW , σ3
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
NewUser(skA, pkA, idW )
Vf(pkA, ∗, ∗) = 1
Gx
Gy, idB, σ2 idW , σ3
I am talking to user A.
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
NewUser(skA, pkA, idW )
Vf(pkA, ∗, ∗) = 1
Gx
Gy, idB, σ2 idW , σ3
I am talking to user A.
BADH-350 checks out!
I’ll send 350 cryptos to user A...
The secret top-up code is: BADH-350
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

DSKS vs SIGMA: identity misbinding (w/ strong attackers)
idW , (pkI , skI )
idB, (pkR, skR)
NewUser(skA, pkA, idW )
Vf(pkA, ∗, ∗) = 1
Gx
Gy, idB, σ2 idW , σ3
I am talking to user A.
BADH-350 checks out!
I’ll send 350 cryptos to user A...
The secret top-up code is: BADH-350
What about EDHOC?
Felix G¨unther and Marc Ilunga
EDHOC 9 / 15

Security Analysis
EDHOC provides strong authentication guarantees even under colliding identifiers
Assuming universal exclusive ownership1 of the signature schemes
S-UEO for signature scheme Σ (informal):
Key pair: (pk, sk)
$←−Σ.KGen()
Adversary A obtains set(mi, σi) (produced by sk)
Goal of A: Produce (pk∗, m∗) s.t Vf(pk∗, m∗, σj) = 1 and pk ̸= pk∗
S-UEO =⇒A cannot succeed.
1Pornin and Stern, “Digital Signatures Do Not Guarantee Exclusive Ownership”.
Felix G¨unther and Marc Ilunga
EDHOC 10 / 15

Security Analysis
Security Model: Multi-Stage Key Exchange
Goals:
Key indistinguishability
Forward security
Explicit authentication
Modeling contributions:
NewUser(sk, pk, id)1 1Boyd et al., “ASICS: Authenticated Key Exchange Security Incorporating Certification Systems”, (Inspired by).
Felix G¨unther and Marc Ilunga
EDHOC 11 / 15

Security Analysis
MSKE Security of EDHOC SIG-SIG
MSKE security of EDHOC SIG-SIG
Let A be an MSKE adversary. For at most nU users and nS sessions, there exists adversaries
Bj such that:
AdvMSKE
A
(EDHOC-Sig-Sig) ≤nS 2 q +
AdvCR
B4 (H)+ 4nS

nU · AdvSUF-CMA
BI.2
(Sig)+
AdvS-UEO
BI.4
(Sig)
!
+ 4nS



 nU · AdvEUF-CMA
BII.A2
(Sig)+
AdvsnPRF-ODH
BII.B2
(Extract)+
AdvPRF
BII.B3(Expand)




Assumption scheme
Collision resistance
SHA2, Shake128
✓
SUF-CMA
Ed25519
✓
ECDSA
✘
S-UEO
Ed25519
✓
ECDSA
✘
EUF-CMA
Ed25519
✓
ECDSA
✓
PRF-ODH
HKDF.Extract
✓
KMAC
(?)
PRF
HKDF.Expand
✓
KMAC
✓
Felix G¨unther and Marc Ilunga
EDHOC 12 / 15

Security Analysis
MSKE Security of EDHOC SIG-SIG
MSKE security of EDHOC SIG-SIG
Let A be an MSKE adversary. For at most nU users and nS sessions, there exists adversaries
Bj such that:
AdvMSKE
A
(EDHOC-Sig-Sig) ≤nS 2 q +
AdvCR
B4 (H)+ 4nS

nU · AdvSUF-CMA
BI.2
(Sig)+
AdvS-UEO
BI.4
(Sig)
!
+ 4nS



 nU · AdvEUF-CMA
BII.A2
(Sig)+
AdvsnPRF-ODH
BII.B2
(Extract)+
AdvPRF
BII.B3(Expand)




Assumption scheme
Collision resistance
SHA2, Shake128
✓
SUF-CMA
Ed25519
✓
ECDSA
✘
S-UEO
Ed25519
✓
ECDSA
✘
EUF-CMA
Ed25519
✓
ECDSA
✓
PRF-ODH
HKDF.Extract
✓
KMAC
(?)
PRF
HKDF.Expand
✓
KMAC
✓
Felix G¨unther and Marc Ilunga
EDHOC 12 / 15

Security Analysis
ECDSA might be fine for EDHOC
S-UEO ✘: EDHOC includes the pub key alongside messages to be signed (✓)
SUF-CMA ✘: Implementations could use “canonical” signatures (✓?).
Felix G¨unther and Marc Ilunga
EDHOC 13 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Interaction with the IETF
Positive collaboration with the LAKE working group
Our work made several contributions to the EDHOC draft
Numerous contributions to EDHOC by several other parties
Jacomme et al.: Full symbolic analysis of latest draft1
Cottier & Pointcheval: Computation analysis of STAT-STAT2
Norman et al.: Early symbolic analysis3
Reminiscent of development of TLS 1.3 1Jacomme et al., “A comprehensive, formal and automated analysis of the EDHOC protocol”.
2Cottier and Pointcheval, Security Analysis of the EDHOC protocol.
3Norrman, Sundararajan, and Bruni, “Formal Analysis of EDHOC Key Establishment for Constrained IoT Devices”.
Felix G¨unther and Marc Ilunga
EDHOC 14 / 15

Conclusion
Conclusion
EDHOC is a LAKE for constrained environments with new security challenges
Our contributions:
Strong security model for the LAKE setting
Security analysis and proof that EDHOC(SIG-SIG) is a secure LAKE in a strong adversarial model
Design contributions to EDHOC
LAKE WG highly welcoming of security analysis and inputs
(eprint ia.cr/2022/1705)
Questions: mail@felixguenther.info marc.ilunga@trailofbits.com
Felix G¨unther and Marc Ilunga
EDHOC 15 / 15

Conclusion
Conclusion
EDHOC is a LAKE for constrained environments with new security challenges
Our contributions:
Strong security model for the LAKE setting
Security analysis and proof that EDHOC(SIG-SIG) is a secure LAKE in a strong adversarial model
Design contributions to EDHOC
LAKE WG highly welcoming of security analysis and inputs
(eprint ia.cr/2022/1705)
Questions: mail@felixguenther.info marc.ilunga@trailofbits.com
Felix G¨unther and Marc Ilunga
EDHOC 15 / 15