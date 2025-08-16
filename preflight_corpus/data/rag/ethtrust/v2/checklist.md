<a href="checklist.html" class="logo"><img src="eea_logo.svg" id="eea-logo" width="180" height="90" alt="EEA" /></a>

# Checklist for EEA EthTrust Security Levels Version 2

## EEA Document 13 December 2023

This version:
[https://entethalliance.org/specs/ethtrust-sl/v2/checklist.html](checklist.html)

Latest editor's draft:
<https://entethalliance.github.io/eta-registry/checklist.html>

Copyright © 2023 [Enterprise Ethereum Alliance](https://entethalliance.org/).

------------------------------------------------------------------------

## Status of This Documen

*This section describes the status of this document at the time of its publication. Newer documents may supersede this document.*

This specification is licensed by the Enterprise Ethereum Alliance, Inc. (EEA) under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) \[<a href="checklist.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\]. Unless otherwise explicitly authorised in writing by the EEA, you can only use this document in accordance with those terms.

Unless required by applicable law or agreed to in writing, this document is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

Please send any comments to the EEA at <https://entethalliance.org/contact/>, or as issues via the [EthTrust-public GitHub repository](https://github.com/EntEthAlliance/EthTrust-public/issues/).

The Working Group *expects* at the time of publication to publish the next release version of this checklist alongside the next version of the Specification, in 2025.

## Table of Contents

1.  <a href="checklist.html#sec-introduction" class="tocxref">1. Introduction</a>
    1.  <a href="checklist.html#sec-typographic-conventions" class="tocxref">1.1.2 Typographic Conventions</a>
2.  <a href="checklist.html#conformance" class="tocxref">2. Conformance</a>
    1.  <a href="checklist.html#sec-conformance-claims" class="tocxref">2.1 Conformance Claims</a>
    2.  <a href="checklist.html#sec-summary-of-requirements" class="tocxref">2.2 Security Level Requirements</a>
    3.  <a href="checklist.html#sec-summary-recommended" class="tocxref">2.3 Recommended Good Practices</a>
3.  <a href="checklist.html#sec-additional-information" class="tocxref">A. Additional Information</a>
    1.  <a href="checklist.html#sec-definitions" class="tocxref">A.1 Defined Terms</a>
4.  <a href="checklist.html#references" class="tocxref">B. References</a>
    1.  <a href="checklist.html#normative-references" class="tocxref">B.1 Normative references</a>
    2.  <a href="checklist.html#informative-references" class="tocxref">B.2 Informative references</a>

## 1. Introduction<a href="checklist.html#sec-introduction" class="self-link" aria-label="§"></a>

*This section is non-normative.*

This companion document is a checklist for \[<a href="checklist.html#bib-ethtrust-sl-v2" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification, Version 2">EthTrust-sl-v2</a>\], the EEA EthTrust Security Levels Specification. It lists the requirements for granting <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> to a smart contract written in Solidity as a convenience for security reviewers, developers, or others, who are familiar with the EEA EthTrust Security Levels Specification, and want an *aide memoire*.

In case of any discrepancy between this checklist, and the relevant version of the EEA EthTrust Security Levels Specification, readers should assume that this document is in error, and the definitive version is the text in the specification.

<a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is a claim by a security reviewer that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is not vulnerable to a number of known attacks or failures to operate as expected, based on the reviewer's assessment against those specific requirements.

<a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> **does not and cannot** ensure that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is completely secure from any attack.

#### 1.1.2 Typographic Conventions<a href="checklist.html#sec-typographic-conventions" class="self-link" aria-label="§"></a>

Definitions of terms are formatted Like this. Most of the terms are defined in the main specification document. Some definitions are repeated in this document. References to defined terms are rendered as links <a href="index.html#dfn-like-this" class="internalDFN" data-link-type="dfn">Like This</a>.

References to other documents are links to the relevant entry in the <a href="checklist.html#references" class="sec-ref">§ B. References</a> section, within square brackets, such as: \[<a href="checklist.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\].

Links to requirements begin with a <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a>: **\[S\]**, **\[M\]** or **\[Q\]**, and recommended good practices begin with **\[GP\]**. They then include the requirement or good practice name. They are rendered as links in bold type, for example:

Example of a link to [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented).

Variables, introduced to be described further on in a statement or requirement, are formatted as `var`.

## 2. Conformance<a href="checklist.html#conformance" class="self-link" aria-label="§"></a>

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) \[<a href="checklist.html#bib-rfc2119" class="bibref" data-link-type="biblio" title="Key words for use in RFCs to Indicate Requirement Levels">RFC2119</a>\] \[<a href="checklist.html#bib-rfc8174" class="bibref" data-link-type="biblio" title="Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words">RFC8174</a>\] when, and only when, they appear in all capitals, as shown here.

The EthTrust Security Levels Specification defines a number of requirements. As described in more detail by <a href="index.html#sec-reading-requirements" class="sec-ref">§ 1.1.3 How to Read a Requirement</a> of that document, each requirement has a Security Level (**\[S\]**, **\[M\]** or **\[Q\]**), and a statement of the requirement that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet.

In order to achieve <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at a specific Security Level, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet **all the requirements for that Security Level**, including all the requirements for lower Security Levels. Some requirements can either be met directly, or by meeting one or more <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirements</a> that mean the requirement is considered met.

Section <a href="checklist.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>, contains further recommendations. Although they are formatted similarly to requirements, they begin with a "level" marker **\[GP\]**. There is no requirement to test for these; however careful implementation and testing is *RECOMMENDED*.

Note that good implementation of the Recommended Good Practices can enhance security, but in some cases incomplete or low-quality implementation could **reduce** security.

To provide as strong a level of assurance as possible, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements as possible at all Security Levels.

This document does not create an affirmative duty of compliance on any party, though requirements to comply with it could be created by contract negotiations or other processes with prospective customers or investors.

### 2.1 Conformance Claims<a href="checklist.html#sec-conformance-claims" class="self-link" aria-label="§"></a>

To grant <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> EEA EthTrust Certification, an auditor provides a <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>, that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirements of the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> for which it is certified.

There is no required format for a <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid conformance claim</a> for Version 1 of this specification, beyond being legible and containing the required information as specified in this section.

A Valid Conformance Claim *MUST* include:

- The date on which the certification was issued, in 'YYYY-MM-DD' forma
- The <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> (of those listed at \[<a href="checklist.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]) for which the certification is valid
- The version of the EEA EthTrust Security Levels specification for which the contract is certified (this specification is version 1)
- A name and a URL for the organisation or software issuing the certification
- The <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> (**\[S\]**, **\[M\]** or **\[Q\]**) that the <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> claims.
- A \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the compiled bytecode for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number
- A \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the Solidity source code for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number
- The compiler options applied for each compilation
- The contract metadata generated by the compiler
- A list of the requirements which were tested and a statement for each one, noting whether the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. This *MAY* include further information.
- An explicit notice stating that <a href="checklist.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> does not provide any warranty or formal guarantee
  - of the overall security of the <a href="checklist.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, nor
  - that the project is free from bugs or vulnerabilities. This notice *SHOULD* state that <a href="checklist.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> represents the best efforts of the issuer to detect and identify certain known vulnerabilities that can affect Smart Contracts.
- For conformance claims where certification is granted because the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> met an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, the conformance claim *MUST* include the results for the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> met, and *MAY* omit the results for the requirement(s) whose results were thus unnecessary to determine conformance.

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> for <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> *MUST* contain a \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the documentation provided to meet [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented) and [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system).

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *SHOULD* include

- a contact address for questions about or challenges to the certification.
- descriptions of conformance to the good practices described in <a href="checklist.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>.

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* include:

- An address where a \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the conformance claim has been recorded on an identified network, e.g. Ethereum Mainnet.
- An address of the contract deployed on an identified network, e.g. Ethereum Mainnet.

### 2.2 Security Level Requirements<a href="checklist.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

Requiremen

Status

[**\[S\] Encode Hashes with `chainid`**](index.html#req-1-eip155-chainid) **<a href="checklist.html#summ-req-1-eip155-chainid" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* create hashes for transactions that incorporate `chainid` values following the recommendation described in \[<a href="checklist.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\]

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No `CREATE2`**](index.html#req-1-no-create2) **<a href="checklist.html#summ-req-1-no-create2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction.
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](checklist.html#summ-req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented),

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin) **<a href="checklist.html#summ-req-1-no-tx.origin" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](checklist.html#summ-req-3-verify-tx.origin)

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check) **<a href="checklist.html#summ-req-1-exact-balance-check" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable
**unless** it meets the Overriding Requirement [**\[M\] Verify Exact Balance Checks**](checklist.html#summ-req-2-verify-exact-balance-check).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict) **<a href="checklist.html#summ-req-1-inheritance-conflict" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* include more than one variable, or operative function with different code, with the same name
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Document Name Conflicts**](checklist.html#summ-req-2-safe-inheritance-order).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Hashing Consecutive Variable Length Arguments**](index.html#req-1-no-hashing-consecutive-variable-length-args) **<a href="checklist.html#summ-req-1-no-hashing-consecutive-variable-length-args" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct) **<a href="checklist.html#summ-req-1-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](checklist.html#summ-req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No `assembly {}`**](index.html#req-1-no-assembly) **<a href="checklist.html#summ-req-1-no-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly {}` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly {}` Attack Vectors**](checklist.html#summ-req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](checklist.html#summ-req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-7**](checklist.html#summ-req-2-compiler-SOL-2022-7),
- [**\[M\] Compiler Bug SOL-2022-4**](checklist.html#summ-req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](checklist.html#summ-req-2-compiler-SOL-2021-3), **and**
- if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in \`assembly {}\`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo) **<a href="checklist.html#summ-req-1-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the [Unicode Direction Control Characters](index.html#dfn-unicode-direction-control-characters) `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](checklist.html#summ-req-2-unicode-bdo).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Check External Calls Return**](index.html#req-1-check-return) **<a href="checklist.html#summ-req-1-check-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call()`, `delegatecall()`, `staticcall()`, and `send()`) *MUST* check the returned value from each usage to determine whether the call failed,
**unless** it meets the Overriding Requirement [**\[M\] Handle External Call Returns**](checklist.html#summ-req-2-handle-return).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i) **<a href="checklist.html#summ-req-1-use-c-e-i" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect External Calls**](checklist.html#summ-req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented)

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](checklist.html#summ-req-3-external-calls),
- [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented),
- [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](checklist.html#summ-req-3-implement-as-documented).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall) **<a href="checklist.html#summ-req-1-delegatecall" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[M\] Protect External Calls**](checklist.html#summ-req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented).

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[Q\] Verify External Calls**](checklist.html#summ-req-3-external-calls),
- [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented),
- [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](checklist.html#summ-req-3-implement-as-documented).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow) **<a href="checklist.html#summ-req-1-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Safe Overflow/Underflow**](checklist.html#summ-req-2-overflow-underflow), **and**
- [**\[M\] Document Special Code Use**](checklist.html#summ-req-2-documented).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2023-3** **<a href="checklist.html#summ-req-1-compiler-SOL-2023-3" class="selflink">🔗</a>**
](index.html#req-1-compiler-SOL-2023-3)Tested code that includes Yul code and uses the \`verbatim\` instruction twice, in each case surrounded identical code, MUST disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2022-6**](index.html#req-1-compiler-SOL-2022-6) **<a href="checklist.html#summ-req-1-compiler-SOL-2022-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a `struct`, `return` value, or paramater list) with the ABIEncoderV2, that includes a dynamic component and whose last element is a `calldata` static array of base type `uint` or `bytes32` *MUST NOT* use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push) **<a href="checklist.html#summ-req-1-compiler-SOL-2022-5-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2022-3**](index.html#req-1-compiler-SOL-2022-3) **<a href="checklist.html#summ-req-1-compiler-SOL-2022-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2022-2**](index.html#req-1-compiler-SOL-2022-2) **<a href="checklist.html#summ-req-1-compiler-SOL-2022-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2022-1**](index.html#req-1-compiler-SOL-2022-1) **<a href="checklist.html#summ-req-1-compiler-SOL-2022-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use Solidity compiler version 0.8.11 nor 0.8.12.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2021-4**](index.html#req-1-compiler-sol-2021-4) **<a href="checklist.html#summ-req-1-compiler-sol-2021-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *MUST NOT* use Solidity compiler version 0.8.8.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2021-2**](index.html#req-1-compiler-SOL-2021-2) **<a href="checklist.html#summ-req-1-compiler-SOL-2021-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory`, *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2021-1**](index.html#req-1-compiler-SOL-2021-1) **<a href="checklist.html#summ-req-1-compiler-SOL-2021-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the Optimizer with a Solidity compiler version older than 0.8.3.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-11-push**](checklist.html#security-levels-spec.htmlreq-1-compiler-SOL-2020-11-push) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-11-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array using `push()` *MUST NOT* use a Solidity compiler version older than 0.7.4.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-10**](checklist.html#security-levels-spec.htmlreq-1-compiler-SOL-2020-10) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-10" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an array of types shorter than 16 bytes to a longer array *MUST NOT* use a Solidity compiler version older than 0.7.3.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-9**](checklist.html#security-levels-spec.htmlreq-1-compiler-SOL-2020-9) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-9" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> *MUST NOT* use Solidity compiler version 0.7.1.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-8**](index.html#req-1-compiler-SOL-2020-8) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-8" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls internal library functions with `calldata` parameters called via `using for` *MUST NOT* use Solidity compiler version 0.6.9.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-6**](index.html#req-1-compiler-SOL-2020-6) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that accesses an array slice using an expression for the starting index that can evaluate to a value other than zero *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.6.0 and 0.6.7 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-7**](index.html#req-1-compiler-SOL-2020-7) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that passes a string literal containing two consecutive backslash ("\\) characters to an encoding function or an external call *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.5.14 and 0.6.7 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-5" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines a contract that does not include a constructor, but has a base contract that defines a constructor not defined as `payable` *MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive), **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Check Constructor Payment**](checklist.html#summ-req-2-compiler-check-payable-constructor).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-4**](index.html#req-1-compiler-SOL-2020-4) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes assignments to tuples tha

- have nested tuples, **or**
- include a pointer to an external function, **or**
- reference a dynamically sized `calldata` array

*MUST NOT* use a Solidity compiler version older than 0.6.4.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-3**](checklist.html#summ-req-1-compiler-SOL-2020-3) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares arrays of size larger than 2^256-1 *MUST NOT* use a Solidity compiler version older than 0.6.5.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Compiler Bug SOL-2020-1**](index.html#req-1-compiler-SOL-2020-1) **<a href="checklist.html#summ-req-1-compiler-SOL-2020-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares variables inside a `for` loop that contains a `break` or `continue` statement *MUST NOT* use the Yul Optimizer with Solidity compiler version 0.6.0 nor a Solidity compiler version between 0.5.8 and 0.5.15 (inclusive).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060) **<a href="checklist.html#summ-req-1-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as if they were <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[S\] Compiler Bug SOL-2020-11-length**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2020-11-length)
- [**\[S\] Compiler Bug SOL-2019-10**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-10)
- [**\[S\] Compiler Bugs SOL-2019-3,6,7,9**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-3679)
- [**\[S\] Compiler Bug SOL-2019-8**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-8)
- [**\[S\] Compiler Bug SOL-2019-5**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-5)
- [**\[S\] Compiler Bug SOL-2019-4**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-4)
- [**\[S\] Compiler Bug SOL-2019-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-2)
- [**\[S\] Compiler Bug SOL-2019-1**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-1)
- [**\[S\] Explicit Storage**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-explicit-storage) (including through its overriding requirement [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage) if appropriate)
- [**\[S\] Compiler Bug SOL-2018-4**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-4)
- [**\[S\] Compiler Bug SOL-2018-3**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-3)
- [**\[S\] Compiler Bug SOL-2018-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-2)
- [**\[S\] Compiler Bug SOL-2018-1**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-1)
- [**\[S\] Compiler Bug SOL-2017-5**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-5)
- [**\[S\] Compiler Bug SOL-2017-4**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-4)
- [**\[S\] Compiler Bug SOL-2017-3**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-3)
- [**\[S\] Compiler Bug SOL-2017-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-2)
- [**\[S\] Compiler Bug SOL-2017-1**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-1)
- [**\[S\] Compiler Bug SOL-2016-11**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-11)
- [**\[S\] Compiler Bug SOL-2016-10**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-10)
- [**\[S\] Compiler Bug SOL-2016-9**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-9)
- [**\[S\] Compiler Bug SOL-2016-8**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-8)
- [**\[S\] Compiler Bug SOL-2016-7**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-7)
- [**\[S\] Compiler Bug SOL-2016-6**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-6)
- [**\[S\] Compiler Bug SOL-2016-5**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-5)
- [**\[S\] Compiler Bug SOL-2016-4**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-4)
- [**\[S\] Compiler Bug SOL-2016-3**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-3)

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[S\] No Ancient Compilers**](index.html#req-1-no-ancient-compilers) **<a href="checklist.html#summ-req-1-no-ancient-compilers" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.3.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Pass Security Level \[S\]**](index.html#req-2-pass-l1) **<a href="checklist.html#summ-req-2-pass-l1" class="selflink">🔗</a>**
To be eligible for <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="checklist.html#sec-levels-one" class="sec-ref">§ 4.1 Security Level [S]</a>.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Explicitly Disambiguate Evaluation Order**](index.html#req-2-enforce-eval-order) **<a href="checklist.html#summ-req-2-enforce-eval-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain statements where variable evaluation order can result in different outcomes

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] No Failing `assert()` Statements**](index.html#req-2-no-failing-asserts) **<a href="checklist.html#summ-req-2-no-failing-asserts" class="selflink">🔗</a>**
`assert()` statements in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* fail.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Verify Exact Balance Checks** **<a href="checklist.html#summ-req-2-verify-exact-balance-check" class="selflink">🔗</a>**
](index.html#req-2-verify-exact-balance-check)Tested code that checks whether the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable. MUST protect itself against transfers affecting the balance tested.
This is an Overriding Requirement for [**\[S\] No Exact Balance Check**](checklist.html#summ-req-1-exact-balance-check).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo) **<a href="checklist.html#summ-req-2-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characters**](checklist.html#summ-req-1-unicode-bdo).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] No Homoglyph-style Attack**](index.html#req-2-no-homoglyph-attack) **<a href="checklist.html#summ-req-2-no-homoglyph-attack" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks if the impact is misleading.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Protect External Calls**](index.html#req-2-external-calls) **<a href="checklist.html#summ-req-2-external-calls" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls:

- all addresses called by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, *MUST* correspond to the exact code of the contracts tested **and**
- all contracts called *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, **and**
- all contracts called *MUST* be controlled by the same entity, **and**
- the protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](checklist.html#summ-req-3-external-calls),
- [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented),
- [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](checklist.html#summ-req-3-implement-as-documented).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](checklist.html#summ-req-1-use-c-e-i).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Avoid Read-only Re-entrancy Attacks**](index.html#req-2-avoid-readonly-reentrancy) **<a href="checklist.html#summ-req-2-avoid-readonly-reentrancy" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Handle External Call Returns**](index.html#req-2-handle-return) **<a href="checklist.html#summ-req-2-handle-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.
This is an Overriding Requirement for [**\[S\] Check External Calls Return**](checklist.html#summ-req-1-check-return).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Document Special Code Use**](index.html#req-2-documented) **<a href="checklist.html#summ-req-2-documented" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* document the need for each instance of:

- `CREATE2`,
- `assembly {}`,
- `selfdestruct()` or its deprecated alias `suicide()`,
- external calls,
- `delegatecall()`,
- code that can cause an overflow or underflow,

use of `block.number` or `block.timestamp`, **or**

use of oracles and pseudo-randomness,

**and** *MUST* describe how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, **and** the documentation *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of

- [**\[S\] No `CREATE2`**](checklist.html#summ-req-1-no-create2),
- [**\[S\] No `selfdestruct()`**](checklist.html#summ-req-1-self-destruct),
- [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly),
- [**\[S\] Use Check-Effects-Interaction**](checklist.html#summ-req-1-use-c-e-i),
- [**\[S\] No Overflow/Underflow**](checklist.html#summ-req-1-overflow-underflow), and
- [**\[S\] No `delegatecall()`**](checklist.html#summ-req-1-no-delegatecall).

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Ensure Proper Rounding of Computations Affecting Value**](index.html#req-2-check-rounding) **<a href="checklist.html#summ-req-2-check-rounding" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* identify and protect against exploiting rounding errors:

- The possible range of error introduced by such rounding *MUST* be documented.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* unintentionally create or lose value through rounding.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct) **<a href="checklist.html#summ-req-2-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author.

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>[**\[Q\] Enforce Least Privilege**](checklist.html#summ-req-3-access-control)

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `selfdestruct()`**](checklist.html#summ-req-1-self-destruct).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly) **<a href="checklist.html#summ-req-2-safe-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly {}` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2) **<a href="checklist.html#summ-req-2-protect-create2" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses the `CREATE2` instruction, any contract to be deployed using `CREATE2`

- *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* use any `selfdestruct()`, `delegatecall()` nor `callcode()` instructions, **and**
- *MUST* be fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](checklist.html#summ-req-3-external-calls),
- [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented),
- [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](checklist.html#summ-req-3-implement-as-documented).

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `CREATE2`**](checklist.html#summ-req-1-no-create2).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] No Overflow/Underflow**](index.html#req-2-overflow-underflow) **<a href="checklist.html#summ-req-2-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Overflow/Underflow**](checklist.html#summ-req-1-overflow-underflow).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order) **<a href="checklist.html#summ-req-2-safe-inheritance-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* clearly document the order of inheritance for each function or variable that shares a name with another function or variable.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Conflicting Names**](checklist.html#summ-req-1-inheritance-conflict).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Sources of Randomness**](index.html#req-2-random-enough) **<a href="checklist.html#summ-req-2-random-enough" class="selflink">🔗</a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse) **<a href="checklist.html#summ-req-2-block-data-misuse" class="selflink">🔗</a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Proper Signature Verification**](index.html#req-2-signature-verification) **<a href="checklist.html#summ-req-2-signature-verification" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* properly verify signatures to ensure authenticity of messages that were signed off-chain.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay) **<a href="checklist.html#summ-req-2-malleable-signatures-for-replay" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST* ensure that signatures cannot be reused:

- In the same function to verify the same message,
- In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>,
- In more than one contract address to verify the same message, in which the same account(s) may be signing messages, **and**
- In the same contract address across multiple chains.

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Intended Replay**](checklist.html#summ-req-3-intended-replay). Additionally, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Solidity Compiler Bug 2023-1**](index.html#req-2-compiler-SOL-2023-1) **<a href="checklist.html#summ-req-2-compiler-SOL-2023-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses `.selector` *MUST* use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7) **<a href="checklist.html#summ-req-2-compiler-SOL-2022-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing `return()` or `stop()` instructions, *MUST NOT* not use a Solidity compiler version between 0.8.13 and 0.8.17 inclusive.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly) **<a href="checklist.html#summ-req-2-compiler-SOL-2022-5-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an `assembly {}` instruction that reads that data without explicitly matching the length that was copied, *MUST NOT* use a Solidity compiler version older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4) **<a href="checklist.html#summ-req-2-compiler-SOL-2022-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly {}` instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, and code in a another `assembly {}` instruction refers to that memory, *MUST NOT* use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3) **<a href="checklist.html#summ-req-2-compiler-SOL-2021-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly {}` instruction *MUST NOT* use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](checklist.html#summ-req-1-no-assembly).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Compiler Bug Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor) **<a href="checklist.html#summ-req-2-compiler-check-payable-constructor" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is

- defined in a base contract, **and**
- used by default in another contract without an explicit constructor, **and**
- not explicity marked `payable`,

*MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2020-5**](checklist.html#summ-req-1-compiler-SOL-2020-5).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060) **<a href="checklist.html#summ-req-2-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as if they were <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[M\] Compiler Bug SOL-2020-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2)
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly)
- [**\[M\] Compiler Bug Check Identity Calls**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls)
- [**\[M\] Validate `ecrecover()` input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input)
- [**\[M\] Compiler Bug No Zero Ether Send**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send)
- [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage)

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Pass Security Level \[M\]**](index.html#req-3-pass-l2) **<a href="checklist.html#summ-req-3-pass-l2" class="selflink">🔗</a>**
To be eligible for <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="checklist.html#sec-levels-two" class="sec-ref">§ 4.2 Security Level [M]</a>.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Code Linting**](index.html#req-3-linted) **<a href="checklist.html#summ-req-3-linted" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert()` statements, **and**
- *MUST NOT* contain a function that has the same name as the smart contract **unless** it is explicitly declared as a constructor using the `constructor` keyword, **and**
- *MUST* explicitly declare the visibility of all functions and variables.

<!-- -->

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Manage Gas Use Increases**](index.html#req-3-enough-gas) **<a href="checklist.html#summ-req-3-enough-gas" class="selflink">🔗</a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Protect Gas Usage**](index.html#req-3-protect-gas) **<a href="checklist.html#summ-req-3-protect-gas" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect against malicious actors stealing or wasting gas.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles) **<a href="checklist.html#summ-req-3-check-oracles" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect itself against malfunctions in <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> it relies on.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Protect against Front-Running**](index.html#req-3-block-front-running) **<a href="checklist.html#summ-req-3-block-front-running" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* require information in a form that can be used to enable a <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attack.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev) **<a href="checklist.html#summ-req-3-block-mev" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Protect against Governance Takeovers**](index.html#req-3-protect-governance) **<a href="checklist.html#summ-req-3-protect-governance" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system *MUST* protect against one external entity taking control via exploit of the governance design.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs) **<a href="checklist.html#summ-req-3-all-valid-inputs" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] State Changes Trigger Events**](index.html#req-3-event-on-state-change) **<a href="checklist.html#summ-req-3-event-on-state-change" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] No Private Data**](index.html#req-3-no-private-data) **<a href="checklist.html#summ-req-3-no-private-data" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Intended Replay**](index.html#req-3-intended-replay) **<a href="checklist.html#summ-req-3-intended-replay" class="selflink">🔗</a>**
If a signature within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance *MUST* be intended, documented, **and** safe for re-use.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](checklist.html#summ-req-2-malleable-signatures-for-replay).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Document Contract Logic**](index.html#req-3-documented) **<a href="checklist.html#summ-req-3-documented" class="selflink">🔗</a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Document System Architecture**](index.html#req-3-document-system) **<a href="checklist.html#summ-req-3-document-system" class="selflink">🔗</a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate) **<a href="checklist.html#summ-req-3-annotate" class="selflink">🔗</a>**
All public interfaces contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="checklist.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation.">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented) **<a href="checklist.html#summ-req-3-implement-as-documented" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented), **and** [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control) **<a href="checklist.html#summ-req-3-access-control" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that enables privileged access *MUST* implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Protect Self-destruction**](checklist.html#summ-req-2-self-destruct).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Use Revocable and Transferable Access Control Permissions**](index.html#req-3-revocable-permisions) **<a href="checklist.html#summ-req-3-revocable-permisions" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* implement a mechanism to revoke and transfer those permissions.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] No Single Admin EOA for Privileged Actions**](index.html#req-3-no-single-admin-eoa) **<a href="checklist.html#summ-req-3-no-single-admin-eoa" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privilieged actions, it *MUST* ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Verify External Calls**](index.html#req-3-external-calls) **<a href="checklist.html#summ-req-3-external-calls" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] Use Check-Effects-Interaction**](checklist.html#summ-req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](checklist.html#summ-req-2-external-calls).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin) **<a href="checklist.html#summ-req-3-verify-tx.origin" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](checklist.html#summ-req-3-documented) or [**\[Q\] Document System Architecture**](checklist.html#summ-req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](checklist.html#summ-req-1-no-tx.origin).

- Not Tested
- Passes
- Not Applicable (Passes)
- Incomplete (Fails)
- Fails

### 2.3 Recommended Good Practices<a href="checklist.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Recommended Practice</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="index.html#req-R-check-new-bugs"><strong>[GP] Check For and Address New Security Bugs</strong></a> <strong><a href="checklist.html#summ-req-R-check-new-bugs" class="selflink">🔗</a></strong><br />
Check [<a href="checklist.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>] and other sources for bugs announced after 1 November 2023 and address them.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-meet-all-possible"><strong>[GP] Meet As Many Requirements As Possible</strong></a> <strong><a href="checklist.html#summ-req-R-meet-all-possible" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-use-latest-compiler"><strong>[GP] Use Latest Compiler</strong></a> <strong><a href="checklist.html#summ-req-R-use-latest-compiler" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> use the latest available stable Solidity compiler version.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-clean-code"><strong>[GP] Write clear, legible Solidity code</strong></a> <strong><a href="checklist.html#summ-req-R-clean-code" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> be written for easy understanding.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-follow-erc-standards"><strong>[GP] Follow Accepted ERC Standards</strong></a> <strong><a href="checklist.html#summ-req-R-follow-erc-standards" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> conform to finalized [<a href="checklist.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>] standards when it is reasonably capable of doing so for its use-case.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-define-license"><strong>[GP] Define a Software License</strong></a> <strong><a href="checklist.html#summ-req-R-define-license" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> define a software license.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-notify-news"><strong>[GP] Disclose New Vulnerabilities Responsibly</strong></a> <strong><a href="checklist.html#summ-req-R-notify-news" class="selflink">🔗</a></strong><br />
Security vulnerabilities that are not addressed by this specification <em>SHOULD</em> be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="checklist.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Applicable</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-fuzzing-in-testing"><strong>[GP] Use Fuzzing</strong></a> <strong><a href="checklist.html#summ-req-R-fuzzing-in-testing" class="selflink">🔗</a></strong><br />
<a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> <em>SHOULD</em> be used to probe <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for errors.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-formal-verification"><strong>[GP] Use Formal Verification</strong></a> <strong><a href="checklist.html#summ-req-R-formal-verification" class="selflink">🔗</a></strong><br />
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> undergo formal verification.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-multisig-threshold"><strong>[GP] Select an appropriate threshold for multisig wallets</strong></a> <strong><a href="checklist.html#summ-req-R-multisig-threshold" class="selflink">🔗</a></strong><br />
Multisignature requirements for privileged actions <em>SHOULD</em> have a sufficient number of signers, and NOT require "1 of N" nor all signatures.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Applicable</li>
<li>Not Implemented</li>
</ul></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-timelock-for-privileged-actions"><strong>[GP] Use TimeLock delays for sensitive operations</strong></a> <strong><a href="checklist.html#summ-req-R-timelock-for-privileged-actions" class="selflink">🔗</a></strong><br />
Sensitive operations that affect all or a majority of users <em>SHOULD</em> use [<a href="checklist.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>] delays.</p></td>
<td><ul>
<li>Not Tested</li>
<li>Implemented</li>
<li>Not Applicable</li>
<li>Not Implemented</li>
</ul></td>
</tr>
</tbody>
</table>

## A. Additional Information<a href="checklist.html#sec-additional-information" class="self-link" aria-label="§"></a>

### A.1 Defined Terms<a href="checklist.html#sec-definitions" class="self-link" aria-label="§"></a>

The following terms are defined in this document:

- <a href="checklist.html#dfn-eea-ethtrust-certification" id="dfnanchor-5">EEA Ethtrust Certification</a>
- <a href="checklist.html#dfn-valid-conformance-claim" id="dfnanchor-47">Valid Conformance Claim</a>

The following terms used in this checklist are defined in the [EEA EthTrust Security Levels Specification](index.html).

- <a href="index.html#dfn-checks-effects-interactions" id="dfnanchor-3">checks-effects-interactions</a>
- <a href="index.html#dfn-evm-version" id="dfnanchor-8">EVM Versions</a>
- <a href="index.html#dfn-free-functions" id="dfnanchor-12">Free Functions</a>
- <a href="index.html#dfn-front-running" id="dfnanchor-13">Front-running</a>
- <a href="index.html#dfn-future-block-attacks" id="dfnanchor-14">Future Block Attacks</a>
- <a href="index.html#dfn-fuzzing" id="dfnanchor-15">Fuzzing</a>
- <a href="index.html#dfn-low-level-call-functions" id="dfnanchor-23">Low-level Call Functions</a>
- <a href="index.html#dfn-malleable-signatures" id="dfnanchor-24">Malleable Signatures</a>
- <a href="index.html#dfn-mev" id="dfnanchor-25">MEV</a>
- <a href="index.html#dfn-oracles" id="dfnanchor-27">Oracles</a>
- <a href="index.html#dfn-overriding-requirement" id="dfnanchor-28">Overriding Requirements</a>
- <a href="index.html#dfn-private-data" id="dfnanchor-29">Private Data</a>
- <a href="index.html#dfn-re-entrancy-attacks" id="dfnanchor-32">Re-entrancy Attacks</a>
- <a href="index.html#dfn-read-only-re-entrancy-attack" id="dfnanchor-33">Read-only Re-entrancy Attack</a>
- <a href="index.html#dfn-related-requirements" id="dfnanchor-34">Related Requirements</a>
- <a href="index.html#dfn-sandwich-attacks" id="dfnanchor-35">Sandwich Attacks</a>
- <a href="index.html#dfn-security-level-s" id="dfnanchor-36">Security Level [S]</a>
- <a href="index.html#dfn-security-level-m" id="dfnanchor-36">Security Level [M]</a>
- <a href="index.html#dfn-security-level-q" id="dfnanchor-37">Security Level [Q]</a>
- <a href="index.html#dfn-security-levels" id="dfnanchor-39">Security Levels</a>
- <a href="index.html#dfn-set-of-contracts" id="dfnanchor-40">Set of Contracts</a>
- <a href="index.html#dfn-sets-of-overriding-requirements" id="dfnanchor-41">Set of Overriding Requirements</a>
- <a href="index.html#dfn-tested-code" id="dfnanchor-42">Tested Code</a>
- <a href="index.html#dfn-unicode-direction-control-characters" id="dfnanchor-45">Unicode Direction Control Characters</a>

## B. References<a href="checklist.html#references" class="self-link" aria-label="§"></a>

### B.1 Normative references<a href="checklist.html#normative-references" class="self-link" aria-label="§"></a>

\[CWE\]
[Common Weakness Enumeration](https://cwe.mitre.org/index.html). MITRE. URL: <https://cwe.mitre.org/index.html>

\[EIP-155\]
[Simple Replay Attack Protection](https://eips.ethlibrary.io/eip-155.html). Ethereum Foundation. URL: <https://eips.ethlibrary.io/eip-155.html>

\[ERC\]
[ERC Final - Ethereum Improvement Proposals](https://eips.ethereum.org/erc). Ethereum Foundation. URL: <https://eips.ethereum.org/erc>

\[EthTrust-sl-v2\]
[EEA EthTrust Security Levels Specification. Version 2](index.html). Enterprise Ethereum Alliance. URL: [https://entethalliance.org/specs/ethtrust-sl/v2/](index.html)

\[EVM-version\]
[Using the Compiler - Solidity Documentation. (§Targets)](https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options>

\[NatSpec\]
[NatSpec Format - Solidity Documentation.](https://docs.soliditylang.org/en/latest/natspec-format.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/natspec-format.html>

\[RFC2119\]
[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

\[RFC8174\]
[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

\[SHA3-256\]
[FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions](http://dx.doi.org/10.6028/NIST.FIPS.202). The National Institute of Standards (US Department of Commerce). URL: <http://dx.doi.org/10.6028/NIST.FIPS.202>

\[solidity-alerts\]
[Solidity Blog - Security Alerts](https://blog.soliditylang.org/category/security-alerts/). Ethereum Foundation. URL: <https://blog.soliditylang.org/category/security-alerts/>

\[solidity-bugs\]
[List of Known Bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst>

\[solidity-bugs-json\]
[A JSON-formatted list of some known security-relevant Solidity bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.json). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.json>

\[swcregistry\]
[Smart Contract Weakness Classification Registry](https://swcregistry.io). ConsenSys Diligence. URL: <https://swcregistry.io>

\[TimeLock\]
[Protect Your Users With Smart Contract Timelocks](https://blog.openzeppelin.com/protect-your-users-with-smart-contract-timelocks/). OpenZeppelin. URL: <https://blog.openzeppelin.com/protect-your-users-with-smart-contract-timelocks/>

### B.2 Informative references<a href="checklist.html#informative-references" class="self-link" aria-label="§"></a>

\[License\]
[Apache license version 2.0](http://www.apache.org/licenses/LICENSE-2.0). The Apache Software Foundation. URL: <http://www.apache.org/licenses/LICENSE-2.0>

[↑](checklist.html#title)
