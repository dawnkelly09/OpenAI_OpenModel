# Citizen Technologies: Practical

 Stealth Addresses
 Security Assessment
 March 7, 2023
 Prepared for:
 Ryan Shea
 Citizen Technologies
 Prepared by:  Opal Wright  and Joop van de Pol

 About Trail of Bits
 Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high- end security research with a real -world attacker mentality to reduce risk and fortify code. With 100+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
 We maintain an exhaustive list of publications at  https://github.com/trailofbits/publications , with links to papers, presentations, public audit reports, and podcast appearances.
 In recent years, Trail of Bits consultants have showcased cutting-edge research through presentations at CanSecWest, HCSS, Devcon, Empire Hacking, GrrCon, LangSec, NorthSec, the O’Reilly Security Conference, PyCon, REcon, Security BSides, and SummerCon.
 We specialize in software testing and code review projects, supporting client organizations in the technology, defense, and ﬁnance industries, as well as government entities. Notable clients include HashiCorp, Google, Microsoft, Western Digital, and Zoom.
 Trail of Bits also operates a center of excellence with regard to blockchain security. Notable projects include audits of Algorand, Bitcoin SV, Chainlink, Compound, Ethereum 2.0,
 MakerDAO, Matic, Uniswap, Web3, and Zcash.
 To keep up to date with our latest news and announcements, please follow  @trailofbits  on
 Twitter and explore our public repositories at  https://github.com/trailofbits .  To engage us directly, visit our “Contact” page at  https://www.trailofbits.com/contact ,  or email us at info@trailofbits.com .
 Trail of Bits, Inc.
 228 Park Ave S #80688
 New York, NY 10003 https://www.trailofbits.com info@trailofbits.com
 Trail of Bits 1

 Notices and Remarks
 Copyright and Distribution
 © 2023 by Trail of Bits, Inc.
 All rights reserved. Trail of Bits hereby asserts its right to be identiﬁed as the creator of this report in the United Kingdom.
 This report is considered by Trail of Bits to be public information;  it is licensed to Citizen
 Technologies under the terms of the project statement of work and has been made public at Citizen Technologies’ request.  Material within  this report may not be reproduced or distributed in part or in whole without the express written permission of Trail of Bits.
 The sole canonical source for Trail of Bits publications is the  Trail of Bits Publications page .
 Reports accessed through any source other than that page may have been modiﬁed and should not be considered authentic.
 Test Coverage Disclaimer
 All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and agreed upon project plan.
 Security assessment projects are time-boxed and often reliant on information that may be provided by a client, its aﬃliates, or its partners. As a result, the ﬁndings documented in this report should not be considered a comprehensive list of security issues, ﬂaws, or defects in the target system or codebase.
 Trail of Bits uses automated testing techniques to rapidly test the controls and security properties of software. These techniques augment our manual security review work, but each has its limitations: for example, a tool may not generate a random edge case that violates a property or may not fully complete its analysis during the allotted time. Their use is also limited by the time and resource constraints of a project.
 Trail of Bits 2

 Table of Contents
 About Trail of Bits 1
 Notices and Remarks 2
 Table of Contents 3
 Executive Summary 4
 Project Summary 6
 Project Goals 7
 Project Targets 8
 Project Coverage 9
 Summary of Findings 10
 Detailed Findings 11 1. Related-nonce attacks across keys allow root key recovery 11 2. Limited forgeries for related keys 13 3. Mutual transactions can be completely deanonymized 15 4. Allowing invalid public keys may enable DH private key recovery 17
 Summary of Recommendations 19
 A. Vulnerability Categories 20
 B. Mitigation Strategy Tradeoﬀs 22
 C. Minor Considerations 26
 D. Fix Review Results 27
 Detailed Fix Review Results 28
 Trail of Bits 3

 Executive Summary
 Engagement Overview
 Citizen Technologies engaged Trail of Bits to review the security of its stealth addresses protocol. From January 23 to January 27, 2023, a team of two consultants conducted a security review of the client-provided source code, with two person-weeks of eﬀort. Details of the project’s timeline, test targets, and coverage are provided in subsequent sections of this report.
 Project Scope
 Our testing eﬀorts were focused on the identiﬁcation of ﬂaws that could result in a compromise of conﬁdentiality, integrity, or availability of the target system. We conducted this audit with partial knowledge of the system. We had access to a high-level description of the protocol, a proof-of-concept implementation, and reference links to several related protocols. We performed a thorough cryptographic analysis of the proposed protocol, including checking relevant professional literature, assessment of full and partial key compromise situations, investigation of common implementation errors, and other mathematical analyses.
 Summary of Findings
 The audit uncovered signiﬁcant ﬁndings that could impact system conﬁdentiality, integrity, or availability. A summary of the ﬁndings and details on notable ﬁndings are provided below.
 EXPOSURE ANALYSIS
 Severity
 Count
 Medium 3
 Low 1
 CATEGORY BREAKDOWN
 Category
 Count
 Cryptography 4
 Trail of Bits 4

 Notable Findings
 Signiﬁcant ﬂaws that impact system conﬁdentiality, integrity, or availability are listed below.
 ●  TOB-CTSA-003
 Pairwise transactions (from Alice to Bob and from Bob to Alice) can be deanonymized because the shared secret is equal. As a result, the derived root public keys for pairwise transactions with the same index have a constant diﬀerence that can be detected by an attacker.
 ●  TOB-CTSA-004
 Allowing invalid public keys may enable DH private key recovery. An attacker can use the invalid public keys to cause the recipient to leak information on their DH private key according to well-known invalid point attacks. Once enough information is obtained using diﬀerent invalid public keys, it can be combined to recover the full
 DH private key.
 Trail of Bits 5

 Project Summary
 Contact Information
 The following managers were associated with this project:
 Dan Guido , Account Manager
 Jeﬀ Braswell , Project  Manager dan@trailofbits.com jeﬀ.braswell@trailofbits.com
 The following engineers were associated with this project:
 Joop van de Pol , Consultant
 Opal Wright , Consultant joop.vandepol@trailofbits.com opal.wright@trailofbits.com
 Project Timeline
 The signiﬁcant events and milestones of the project are listed below.
 Date
 Event
 Jan 20, 2023
 Pre-project kickoﬀ call
 Jan 27, 2023
 Status update meeting #1
 Feb 3, 2023
 Report readout meeting
 March 7, 2023
 Delivery of ﬁnal report
 Trail of Bits 6

 Project Goals
 The engagement was scoped to provide a security assessment of the Citizen Technologies
 Stealth Addresses protocol. Speciﬁcally, we sought to answer the following non-exhaustive list of questions:
 ●  Is there a way for a participant, malicious party, or outside observer to steal funds or track funds?
 ●  Are there any mathematical attacks that allow recovery of protected key material or signature forgeries?
 ●  Are there any attacks based on common implementation errors that could compromise the security of the system?
 ●  For any issues discovered, are there suitable mitigations, and what are the advantages and disadvantages of each mitigation?
 Trail of Bits 7

 Project Targets
 The engagement involved a review and analysis of the Stealth Address protocol.
 Stealth address protocol
 Protocol Spec
 Practical stealth addresses
 Implementation  Example implementation
 Platform
 N/A
 Version
 N/A
 Trail of Bits 8

 Project Coverage
 This section provides an overview of the analysis coverage of the review, as determined by our high-level engagement goals. Our approaches include the following:
 ●  Independent cryptographic analysis
 ●  Literature review
 ●  Comparison to related and prior protocols
 ●  Implementation consideration review
 ●  Project scale consideration
 Coverage Limitations
 Because of the time-boxed nature of testing work, it is common to encounter coverage limitations. The following list outlines the coverage limitations of the engagement and indicates system elements that may warrant further review:
 ●  Not every implementation error can be anticipated or considered; our implementation error analysis focused on common errors seen in previous audits
 (e.g., failure to reject invalid points during elliptic curve operations).
 ●  The protocol documentation received was very high-level. While the general mechanisms used for the protocol were clear, speciﬁc algorithms were not speciﬁed in most places. For example, it was clear that elliptic-curve Diﬃe-Hellman (ECDH)
 would be used, but speciﬁc hash functions were left out of the speciﬁcation (the example implementation used SHA-256). Even within an otherwise-secure protocol, the use of inappropriate cryptographic primitives can cause security problems.
 Trail of Bits 9

 Summary of Findings
 The table below summarizes the ﬁndings of the review, including type and severity details.
 ID
 Title
 Type
 Severity 1
 Related-nonce attacks across keys allow root key recovery
 Cryptography
 Medium 2
 Limited forgeries for related keys
 Cryptography
 Low 3
 Mutual transactions can be completely deanonymized
 Cryptography
 Medium 4
 Allowing invalid public keys may enable DH private key recovery
 Cryptography
 Medium
 Trail of Bits 10

 Detailed Findings 1. Related-nonce attacks across keys allow root key recovery
 Severity:  Medium
 Diﬃculty:  Undetermined
 Type: Cryptography
 Finding ID: TOB-CTSA-1
 Target: Root key
 Description
 Given multiple addresses generated by the same sender, if any two signatures with the associated private keys use the same nonce, then the recipient’s private root key can be recovered.
 Nonce reuse attacks are a known risk for single ECDSA keys, but this attack extends the vulnerability to  all  keys generated by a given sender.
 Exploit Scenario
 Alice uses Bob’s public key to generate addresses and
 𝐵  1 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||1 ) *  𝐺 +  𝐵  𝑟𝑜𝑜𝑡 and deposits funds in each. Bob’s corresponding private
 𝐵  2 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||2 ) *  𝐺  +   𝐵  𝑟𝑜𝑜𝑡 keys will be and
 . Note that, while Alice
 𝑏  1 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||1 ) +  𝑏  𝑟𝑜𝑜𝑡
 𝑏  2 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||2 ) +  𝑏  𝑟𝑜𝑜𝑡 does not know or
 , she does know the diﬀerence of the two:
 𝑏  1
 𝑏  2
 . As a result, she can write
 .
 𝑏  𝑑𝑖𝑓𝑓 =  𝑏  2 − 𝑏  1 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||2 ) − 𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||1 )
 𝑏  2 =  𝑏  1 +  𝑏  𝑑𝑖𝑓𝑓
 Suppose Bob signs messages with hashes and to transfer the funds out of and
 𝑚  1
 𝑚  2
 𝐵  1
 𝐵  2
 (respectively), and he uses the same nonce in both signatures. He will output signatures
 𝑘 and
 , where
 ,
 , and
 .
( 𝑟 ,  𝑠  1 )
( 𝑟 ,  𝑠  2 )
 𝑟 = ( 𝑘 *  𝐺 ) 𝑥  𝑠  1 =  𝑘
− 1 ( 𝑚  1 +  𝑟 𝑏  1 )
 𝑠  2 =  𝑘
− 1 ( 𝑚  2 +  𝑟 𝑏  1 +  𝑟 𝑏  𝑑𝑖𝑓𝑓 )
 Subtracting the  -values gives us
 . Because all the terms
 𝑠
 𝑠  1 − 𝑠  2 =  𝑘
− 1 ( 𝑚  1 − 𝑚  2 − 𝑟 𝑏  𝑑𝑖𝑓𝑓 )
 except are known, Alice can recover and thus
 ,
 , and
 .
 𝑘
 𝑘
 𝑏  1  𝑏  2
 𝑏  𝑟𝑜𝑜𝑡 =  𝑏  2 − 𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||2 )
 Recommendations
 Consider using deterministic nonce generation in any stealth-enabled wallets. This is an approach used in multiple elliptic curve digital signature schemes, and can be adapted to
 ECDSA relatively easily; see  RFC 6979 .
 Trail of Bits 11

 Also consider root key blinding. Set
 .
 𝐵  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) *  𝐺  +   𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ||" 𝑟𝑜𝑜𝑡 " ) *  𝐵
 𝑟𝑜𝑜𝑡
 With blinding, private keys take the form
 .
 𝑏  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) +  𝑏  𝑟𝑜𝑜𝑡 ·  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ||" 𝑟𝑜𝑜𝑡 " )
 Since the terms no longer cancel out, Alice cannot ﬁnd
 , and the attack falls apart.
 𝑏  𝑟𝑜𝑜𝑡
 𝑏  𝑑𝑖𝑓𝑓
 Finally, consider using homogeneous key derivation. Set
 . The
 𝐵  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) *  𝐵  𝐷𝐻 +  𝐵  𝑟𝑜𝑜𝑡 private key for Bob is then
 . Because Alice does not know
 ,
 𝑏  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) ·  𝑏  𝐷𝐻 +  𝑏  𝑟𝑜𝑜𝑡
 𝑏  𝑑ℎ she cannot ﬁnd
 , and the attack falls apart.
 𝑏  𝑑𝑖𝑓𝑓
 References
 ●  ECDSA: Handle with Care
 ●  RFC 6979: Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic
 Curve Digital Signature Algorithm (ECDSA)
 Trail of Bits 12

 2. Limited forgeries for related keys
 Severity:  Low
 Diﬃculty:  Low
 Type: Cryptography
 Finding ID: TOB-CTSA-2
 Target: Stealth addresses generated by the same sender
 Description
 If Bob signs a message for an address generated by Alice, Alice can convert it into a valid signature for another address. She cannot, however, control the hash of the message being signed, so this attack is of limited value.
 As with the related-nonce attack, this attack relies on Alice knowing the diﬀerence in discrete logarithms between two addresses.
 Exploit Scenario
 Alice generates addresses and
 𝐵  1 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||1 ) *  𝐺 +  𝐵  𝑟𝑜𝑜𝑡
 𝐵  2 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  ||2 ) *  𝐺 +  𝐵  𝑟𝑜𝑜𝑡 and deposits funds in each account. As before, Alice knows
 , the diﬀerence of the
 𝑏  𝑑𝑖𝑓𝑓 discrete logs for and
 , and
 .
 𝐵  1
 𝐵  2
 𝐵  𝑑𝑖𝑓𝑓 =  𝐵  2 − 𝐵  1
 Bob transfers money out of
 , generating signature of a message with hash  ,
 𝐵  2
( 𝑟 ,  𝑠 )
 𝑚
 𝑒 where  is the  -coordinate of
 (where is the nonce). The signature is validated by
 𝑟
 𝑥
 𝑘 *  𝐺
 𝑘 computing and verifying that the  -coordinate of matches  .
 𝑃 =  𝑒 𝑠
− 1 *  𝐺 +  𝑟 𝑠
− 1 *  𝐵  2
 𝑥
 𝑃
 𝑟
 Alice can convert this into a signature under for a message with hash
 .
 𝐵  1
 𝑒 ' =  𝑒 +  𝑟 𝑏  𝑑𝑖𝑓𝑓
 Verifying this signature under
 , computing becomes:
 𝐵  1
 𝑃
 𝑃 = ( 𝑒 +  𝑟 𝑏  𝑑𝑖𝑓𝑓 ) 𝑠
− 1 *  𝐺 +  𝑟 𝑠
− 1 *  𝐵  1
=  𝑒 𝑠
− 1 *  𝐺 +  𝑟 𝑏  𝑑𝑖𝑓𝑓  𝑠
− 1 *  𝐺 +  𝑟 𝑏  1  𝑠
− 1 *  𝐺
=  𝑒 𝑠
− 1 *  𝐺 +  𝑟 𝑠
− 1 ( 𝑏  1 +  𝑏  𝑑𝑖𝑓𝑓 ) *  𝐺
=  𝑒 𝑠
− 1 *  𝐺 +  𝑟 𝑠
− 1 *  𝐵  2
 This is the same relation that makes a valid signature on a message with hash  , so
( 𝑟 ,  𝑠 )
 𝑒
 𝑃 will be correct.
 Trail of Bits 13

 Note that Alice has no control over the value of  , so to make an eﬀective exploit, she
 𝑒 ' would have to ﬁnd a preimage of under the given hash function. Computing
 𝑚 '
 𝑒 ' preimages is, to date, a hard problem for SHA-256 and related functions.
 Recommendations
 Consider root key blinding, as above. The attack relies on Alice knowing
 , and root key
 𝑏  𝑑𝑖𝑓𝑓 blinding prevents her from learning it.
 Consider homogeneous key derivation, as above. Once again, depriving Alice of  𝑏  𝑑𝑖𝑓𝑓 obviates the attack completely.
 Trail of Bits 14

 3. Mutual transactions can be completely deanonymized
 Severity:  Medium
 Diﬃculty:  Medium
 Type: Cryptography
 Finding ID: TOB-CTSA-3
 Target: Anonymity of mutual transactions
 Description
 When Alice and Bob both make stealth payments to each other, they generate the same
 Shared Secret #i for transaction i, which is used to derive destination keys for Bob and
 Alice:
 Symbol
 Description
 Alice’s derivation
 Bob’s derivation s  i
 Shared secret #i hash(a  dh  * B  dh  , i)
 hash(b  dh  * A  dh  , i)
 B  i
 Bob’s destination key #i
 B  r  + s  i  * G
 A  i
 Alice’s destination key #i
 A  r  + s  i  * G
 However, as a result, the destination keys of Bob and Alice for the same transaction number #i will always have the constant diﬀerence B  i  - A  i  = B  r  - A  r  .
 Exploit Scenario
 An attacker records all root public keys from the database, computes the pairwise diﬀerences B  i  - A  i  for every pair of users A and  B they want to monitor, and stores the diﬀerences in a list.
 The attacker subsequently reviews all pairs of public keys associated with transactions on the blockchain, computes the diﬀerences between the public keys, and compares the x coordinates to the stored list of pairwise diﬀerences.
 If a match is found, the attacker knows that those transactions correspond to stealth transactions between A and B with some index i. The attacker can also determine which transaction went from A to B and vice versa by considering the y coordinates of the public keys and pairwise diﬀerences.
 Because the attack compromises the anonymity of pairs of users without giving access to funds, we consider this issue to have medium severity. As the attack requires both users in the pair to make transactions to each other, and as it requires a potentially signiﬁcant
 Trail of Bits 15

 calculation eﬀort (proportional to the square of the number of transactions), we consider this issue to have medium diﬃculty.
 Recommendations
 There are several ways to mitigate this issue:
 ●  Root key blinding, as described in the recommendations for  TOB-CTSA-1 .
 ●  Diversify the shared secret #i, e.g., by adding the DH key of the receiver to the hash
 , or to any other known
 𝑠  𝑖 , 𝐵 =  𝐻𝑎𝑠ℎ  ( 𝑎  𝑑ℎ   ·   𝐵  𝑑ℎ   ||  𝑖  ||  𝐵  𝑑ℎ ) =  𝐻𝑎𝑠ℎ  ( 𝑏  𝑑ℎ ·  𝐴  𝑑ℎ  ||  𝑖  ||  𝐵  𝑑ℎ )
 identiﬁer for the receiver (e.g., public root key B  r  , a unique predetermined string that is stored in the public key database).
 ●  Homogenize the destination keys by including both the root key and the DH key of the receiver, i.e.,
 , with corresponding private key
 𝐵  𝑖   =   𝐵  𝑟   +   𝑠  𝑖   *   𝐵  𝑑ℎ
 .
 𝑏  𝑖 =  𝑏  𝑟 +   𝑠  𝑖   ·   𝑏  𝑑ℎ
 The advantages and disadvantages of each of these mitigation methods is discussed in detail in  Appendix B .
 Trail of Bits 16

 4. Allowing invalid public keys may enable DH private key recovery
 Severity:  Medium
 Diﬃculty:  High
 Type: Cryptography
 Finding ID: TOB-CTSA-4
 Target:  DH private key
 Description
 Consider the following three assumptions:
 1.  Alice can add points that are not on the elliptic curve to the public key database, 2.  Bob does not verify the public key points, and 3.  Bob's scalar multiplication implementation has some speciﬁc characteristics.
 Assumptions 1 and 2 are currently not speciﬁed in the speciﬁcation, which motivates this
 ﬁnding.
 If these assumptions hold, then Alice can recover Bob's DH key using a complicated attack, based on the  CRYPTO 2000 paper by Biehl et al.  and  the  DCC 2005 paper by Ciet et al . What follows is a rough sketch of the attack. For more details, see the reference publications, which also detail the speciﬁc characteristics for Assumption 3.
 Exploit Scenario
 Alice roughly follows the following steps:
 1.  Find a point which
 𝑃 ' a.  is not on the curve used for ECDH, and b.  when used in Bob’s scalar multiplication, is eﬀectively on a diﬀerent curve  𝐸 ' with (a subgroup of) small prime order  .
 𝑝 ' 2.  Brute-force all possible values of for
 , and sends funds to all
 𝑥 ·  𝑃 ' 0 ≤ 𝑥  <  𝑝 ' addresses with shared secret
 , i.e.,
 .
 𝐻𝑎𝑠ℎ ( 𝑥 ·  𝑃 '  ||  0 )
 𝐵  𝑥   =   𝐵  𝑟   +   𝐻𝑎𝑠ℎ ( 𝑥 ·  𝑃 '||  0 ) *  𝐺 3.  Monitor all resulting addresses associated with until Bob withdraws funds from
 𝐵  𝑥 the unique stealth address associated with
 . This happens because
 𝑥 ' =  𝑏  𝑑ℎ   𝑚𝑜𝑑  𝑝 '
 .
 𝑏  𝑑ℎ ·  𝑃 '  =   ( 𝑏  𝑑ℎ   𝑚𝑜𝑑  𝑝 ' ) ·  𝑃 ' 4.  Repeat steps 1–3 for new points with diﬀerent small prime orders to recover
 𝑃  𝑗  '
 𝑝  𝑗  '
 .
 𝑏  𝑑ℎ   𝑚𝑜𝑑  𝑝  𝑗  ' 5.  Use the Chinese Remainder Theorem to recover from
 .
 𝑏  𝑑ℎ
 𝑏  𝑑ℎ   𝑚𝑜𝑑  𝑝  𝑗  '
 Trail of Bits 17

 As a result, Alice can now track all stealth payments made to Bob (but cannot steal funds).
 To understand the complexity of this attack, it is suﬃcient for Alice to repeat steps 1–3 for the ﬁrst 44 primes (numbers between 2 and 193). This requires Alice to make 3,831 payments in total (corresponding to the sum of the ﬁrst 44 primes).
 There is a tradeoﬀ where Alice uses fewer primes, which means that fewer transactions are needed. However, it means that Alice does not recover the full b  dh  . To compensate for this,
 Alice can brute-force the discrete logarithm of B  dh  guided by the partial information on b  dh  .
 Because the attack compromises anonymity for a particular user without giving access to funds, we consider this issue to have medium severity. As this is a complicated attack with various assumptions that requires Bob to access the funds from all his stealth addresses, we consider this issue to have high diﬃculty.
 Recommendations
 The speciﬁcation should enforce that public keys are validated for correctness, both when they are added to the public database and when they are used by senders and receivers.
 These validations should include point-on-curve checks, small-order-subgroup checks (if applicable), and point-at-inﬁnity checks.
 References
 ●  Diﬀerential Fault Attacks on Elliptic Curve Cryptosystems, Biehl et al., 2000
 ●  Elliptic Curve Cryptosystems in the Presence of Permanent and Transient Faults, Ciet et al., 2005
 Trail of Bits 18

 Summary of Recommendations
 The Citizen Technologies Practical Stealth Addresses proposal is a work in progress with multiple planned iterations. Trail of Bits recommends that Citizen Technologies address the
 ﬁndings detailed in this report and take the following additional steps prior to deployment:
 ●  Update the speciﬁcation to ensure that the public key database enforces the validity of the elliptic curve points corresponding to the public keys. Additionally, specify that both sender and receiver should perform their own input validation of elliptic curve points.
 ●  Update the speciﬁcation to recommend deterministic nonce generation for signatures to avoid nonce re-use, if this is not yet speciﬁed for the used signature scheme.
 ●  Consider the various proposed mitigation methods that are summarized and analyzed in more detail in  Appendix B  and implement  the mitigations that provide the desired trade-oﬀs in terms of performance and security.
 Trail of Bits 19

 A. Vulnerability Categories
 The following tables describe the vulnerability categories, severity levels, and diﬃculty levels used in this document.
 Vulnerability Categories
 Category
 Description
 Access Controls
 Insuﬃcient authorization or assessment of rights
 Auditing and Logging
 Insuﬃcient auditing of actions or logging of problems
 Authentication
 Improper identiﬁcation of users
 Conﬁguration
 Misconﬁgured servers, devices, or software components
 Cryptography
 A breach of system conﬁdentiality or integrity
 Data Exposure
 Exposure of sensitive information
 Data Validation
 Improper reliance on the structure or values of data
 Denial of Service
 A system failure with an availability impact
 Error Reporting
 Insecure or insuﬃcient reporting of error conditions
 Patching
 Use of an outdated software package or library
 Session Management
 Improper identiﬁcation of authenticated users
 Testing
 Insuﬃcient test methodology or test coverage
 Timing
 Race conditions or other order-of-operations ﬂaws
 Undeﬁned Behavior
 Undeﬁned behavior triggered within the system
 Trail of Bits 20

 Severity Levels
 Severity
 Description
 Informational
 The issue does not pose an immediate risk but is relevant to security best practices.
 Undetermined
 The extent of the risk was not determined during this engagement.
 Low
 The risk is small or is not one the client has indicated is important.
 Medium
 User information is at risk; exploitation could pose reputational, legal, or moderate ﬁnancial risks.
 High
 The ﬂaw could aﬀect numerous users and have serious reputational, legal, or ﬁnancial implications.
 Diﬃculty Levels
 Diﬃculty
 Description
 Undetermined
 The diﬃculty of exploitation was not determined during this engagement.
 Low
 The ﬂaw is well known; public tools for its exploitation exist or can be scripted.
 Medium
 An attacker must write an exploit or will need in-depth knowledge of the system.
 High
 An attacker must have privileged access to the system, may need to know complex technical details, or must discover other weaknesses to exploit this issue.
 Trail of Bits 21

 B. Mitigation Strategy Tradeoąs
 The following table provides a comparison of the diﬀerent proposals linked in the protocol document. Please note that this merely comprises a comparison based on the analysis of the target proposal. It should not be interpreted as a full analysis of all proposals.
 The following notation is used:
 ●  M is the number of elliptic curve multiplications.
 ●  A is the number of elliptic curve additions.
 ●  H is the number of hash function calls.
 ●  N  pk  is the number of users (i.e., sets of public keys)  in the database.
 ●  N  rtxs  is the number of stealth transactions received.
 ●  N  I  is the number of input keys.
 ●  Tx is Transaction.
 Reference
 Target proposal
 Robin Linus, 2022
 Ruben
 Somsen, 2022  (base only)
 BIP351
 EIP-5564
 Key pairs
 All users: 2
 All users: 1
 All users: 1
 Receivers: 1
 Senders: 1 or more for each receiver 1 for each send transaction
 (ephemeral)
 2 for all receivers
 Detection cost
 (operations)
 (2M, A, H)
 per (N  pk  +
 N  rtxs  )
 (M, A) per
 (N  pk  )
 (2M, A, H)
 per (N  I  )
 (M, H) per notiﬁcation
 (A, H) per Tx
 (M, H) per announce,
 (M, A, H) per
 Tx
 Detection cost
 (monitoring)
 N  pk addresses 1 address
 All transactions,
 N  I  addresses
 All blocks, 1 address per match
 All announce, 1 address per match
 Unique receive address
 Yes (index)
 No
 Per input key
 Yes
 (counter)
 Yes
 (ephemeral sender key)
 Separate
 Yes
 No
 No
 No
 Yes
 Trail of Bits 22

 scan/spend keys
 Stateless
 No
 Yes
 Yes
 No
 Yes
 Resistant to
 TOB-CTSA-1
 No
 No
 No
 No
 No
 Resistant to
 TOB-CTSA-2
 No
 No
 No
 No
 No
 Resistant to
 TOB-CTSA-3
 No
 No
 If same input key is not reused for multiple recipients
 Yes
 Yes
 Resistant to
 TOB-CTSA-4
 No
 No
 No
 No
 No
 In general, the core concept of each of the stealth address protocol proposals seems cryptographically sound. The  EUROCRYPT 2022 paper  by Groth et al.  gives a formal security proof for ECDSA with additive key derivation, which corresponds to the key tweaking that is used in most stealth address proposals. This shows that it is at least diﬃcult to steal funds by forging signatures based on keys derived from the root key.
 The paper does note that there is a security gap when using additive key derivation. A security gap in a formal security proof does not mean that there exists a practical attack against the scheme, but it theoretically “leaves room” for such an attack to exist. To close this gap, the authors propose homogeneous key derivation, which corresponds to one of the proposed mitigations in this report.
 As a result, the ﬁndings in this report follow from subtle implementation ﬂaws and reuse of
 DH shared secrets for distinct purposes. The following mitigations were proposed for these
 ﬁndings:
 ●  Deterministic nonce generation (e.g., using  RFC 6979  for ECDSA).
 ●  Root key blinding:
 , with
 𝐵  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) *  𝐺  +   𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ||" 𝑟𝑜𝑜𝑡 " ) *  𝐵
 𝑟𝑜𝑜𝑡 corresponding private key
 .
 𝑏  𝑖 =  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ) +  𝑏  𝑟𝑜𝑜𝑡 ·  𝐻𝑎𝑠ℎ ( 𝑠  𝑎𝑏  || 𝑖 ||" 𝑟𝑜𝑜𝑡 " )
 ●  Diversiﬁcation of shared secret with recipient data:
 .
 𝑠  𝑖 , 𝐵 =  𝐻𝑎𝑠ℎ  ( 𝑎  𝑑ℎ   ·   𝐵  𝑑ℎ   ||  𝑖  ||  𝐵  𝑑ℎ ) =  𝐻𝑎𝑠ℎ  ( 𝑏  𝑑ℎ ·  𝐴  𝑑ℎ  ||  𝑖  ||  𝐵  𝑑ℎ )
 Trail of Bits 23

 ●  Homogenize the destination keys by adding DH:
 ,  with
 𝐵  𝑖   =   𝐵  𝑟   +   𝑠  𝑖   ·   𝐵  𝑑ℎ corresponding private key
 .
 𝑏  𝑖 =  𝑏  𝑟 +   𝑠  𝑖   ·   𝑏  𝑑ℎ
 The following table lists these mitigations and their impact on the current proposal. Note that deterministic nonce generation is not included, as it does not directly aﬀect the protocol and addresses only  TOB-CTSA-1 . It can be  implemented along with any other proposed mitigation, and it is independently useful to avoid nonce reuse.
 Reference
 Target proposal
 Diversify shared secret with recipient data
 Root key blinding
 Homogenize destination keys by adding
 DH
 Key pairs 2 2 2 2
 Detection cost
 (operations)
 (2M, A, H) per
 (N  pk  + N  rtxs  )
 (2M, A, H) per
 (N  pk  + N  rtxs  )
 (2M, A, 2H) per
 (N  pk  + N  rtxs  )
 (2M, A, H) per
 (N  pk  + N  rtxs  )
 Detection cost
 (monitoring)
 N  pk  addresses
 N  pk  addresses
 N  pk  addresses
 N  pk  addresses
 Unique receive address
 Yes
 Yes
 Yes
 Yes
 Separate scan/spend keys
 Yes
 Yes
 Yes
 Yes
 Stateless
 No
 No
 No
 No
 Resistant to
 TOB-CTSA-1
 No
 No
 Yes
 Yes
 Resistant to
 TOB-CTSA-2
 No
 No
 Yes
 Yes
 Resistant to
 TOB-CTSA-3
 No
 Yes
 Yes
 Yes
 Trail of Bits 24

 This table does not list  TOB-CTSA-4  because the corresponding mitigation is merely to update the speciﬁcation. This can be done in conjunction with any other mitigation or scheme.
 References
 ●  Improved Stealth Addresses, Linus, 2022
 ●  Silent Payments, Somsen, 2022
 ●  BIP351: Private Payments, Hodler et al., 2022
 ●  EIP-5564: Non-Interactive Stealth Address Generation, Wahrstätter et al., 2022
 ●  On the security of ECDSA with additive key derivation and presignatures, Groth et al., EUROCRYPT 2022
 Trail of Bits 25

 C. Minor Considerations
 The following considerations do not rise to the level of cryptographic vulnerabilities, but should be taken into account when reﬁning the protocol or developing software to implement it.
 Do not use raw hashes to derive key material.
 When deriving key material from a shared secret, it is better to use a key derivation function such as HKDF. KDFs are more ﬂexible, allowing multiple keys to be safely derived from the same shared secret.
 Consider the implications of statefulness.
 The transaction index used in the derivation of the base point multiplier needs to be tracked for all potential senders in the public key directory. Maintaining this state, recovering from a failure to maintain state, and dealing with other parties who fail to maintain the same state are complex technical problems.
 Consider the overhead of the public directory.
 Which responsibilities will the public directory take on? Will the public directory validate keys before publishing them? Will the public directory have DoS/DDoS protections in place?
 How are compromised/expired keys updated within the public directory? Is there a maximum size for the public directory?
 Trail of Bits 26

 D. Fix Review Results
 When undertaking a ﬁx review, Trail of Bits reviews the ﬁxes implemented for issues identiﬁed in the original report. This work involves a review of speciﬁc areas of the source code and system conﬁguration, not comprehensive analysis of the system.
 On February 16 2023, Trail of Bits reviewed the ﬁxes and mitigations implemented by the
 Citizen Technologies team for the issues identiﬁed in this report. We reviewed each ﬁx to determine its eﬀectiveness in resolving the associated issue.
 Citizen Technologies weighed the pros and cons of several options to mitigate the related-key attacks identiﬁed in this report, and settled on using the key homogenization approach. Further, they integrated on-curve checks into the protocol, reducing the risk of oﬀ-curve attacks. Finally, they updated the protocol to use HKDF when deriving secret multipliers, and speciﬁed a multiplier size that should reduce mod bias.
 In summary, Citizen Technologies has resolved all four of the issues described in this report. For additional information, please see the Detailed Fix Review Results below.
 ID
 Title
 Severity
 Status 1
 Related-nonce attacks across keys allow root key recovery
 Medium
 Resolved 2
 Limited forgeries for related keys
 Low
 Resolved 3
 Mutual transactions can be completely deanonymized
 Medium
 Resolved 4
 Allowing invalid public keys may enable DH private key recovery
 Medium
 Resolved
 Trail of Bits 27

 Detailed Fix Review Results
 TOB-CTSA-1:  Related-nonce attacks across keys allow  root key recovery
 Resolved in 30 January 2023 protocol update.
 The new key homogenization approach replaces with
 𝐵  𝑖 =  𝐻𝑎𝑠ℎ  𝑠  𝑎𝑏  || 𝑖
(
) *  𝐺 +  𝐵  𝑟𝑜𝑜𝑡
 , preventing  known relations between secret keys and for
 𝐵  𝑖 =  𝐻𝑎𝑠ℎ  𝑠  𝑎𝑏  || 𝑖
(
) *  𝐵  𝑑ℎ +  𝐵  𝑟𝑜𝑜𝑡
 𝑏  𝑖
 𝑏  𝑗
 .
 𝑖 ≠ 𝑗
 Further, the implementation notes for the protocol state that implementers  must  use deterministic nonce derivation for ECDSA signatures. This reduces the risk of nonce reuse and related nonce attacks against individual keys.
 TOB-CTSA-2:  Limited forgeries for related keys
 Resolved in the January 30, 2023 protocol update.
 As with TOB-CTSA-1, key homogenization prevents known relations between secret keys, which prevents the attack.
 TOB-CTSA-3:  Mutual transactions can be completely  deanonymized
 Resolved in the January 30, 2023 protocol update.
 As with TOB-CTSA-1 and TOB-CTSA-2, key homogenization prevents known relations between secret keys, which prevents the attack.
 TOB-CTSA-4:  Allowing invalid public keys may enable  DH private key recovery
 Resolved in the January 30, 2023 protocol update.
 Implementation notes state that “clients  must  check  the validity of public keys before doing calculations with them.” An implementation that fails to check the validity of public keys would thus be non-compliant with the standard.
 Minor Considerations:
 The January 30, 2023 protocol update states:
 Hashes should be derived using the key-derivation function HKDF and the hashing function SHA256, with no salt, with info set to the string Key-${i} where "i" is the index of the key, and with a key length of 40 bytes. The number should then be mapped onto the curve order using a modular operation.
 Replacing direct use of SHA-256 for key derivation with HKDF addresses several minor risks.
 Trail of Bits 28

 In previous versions of the protocol, if were leaked for some  , an
 𝐻  𝑖 =  𝑆𝐻𝐴 256  𝑠  𝑎𝑏  || 𝑖
(
)
 𝑖 attacker might be able to exploit length extension attacks to determine for
 𝐻  1 0
 𝑛  𝑖 + 𝑘 and
 , which would deanonymize those  future transactions.
 0 ≤ 𝑘 <  10
 𝑛 >  0
 Additionally, the use of a 320-bit output reduces the eﬀects of mod bias in the resulting multiplier of the Diﬃe-Hellman key.
 Trail of Bits 29