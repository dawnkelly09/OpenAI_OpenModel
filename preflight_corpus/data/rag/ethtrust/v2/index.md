<a href="index.html" class="logo"><img src="eea_logo.svg" id="eea-logo" width="180" height="90" alt="EEA" /></a>

# EEA EthTrust Security Levels Specification version 2

## EEA Specification 13 December 2023

This Version:
[https://entethalliance.org/specs/ethtrust-sl/v2/](index.html)

Latest editor's draft:
<https://entethalliance.github.io/eta-registry/security-levels-spec.html>

Editor:
<a href="https://entethalliance.org/cdn-cgi/l/email-protection#3e5d565f5f524d7e5b504a5b4a565f5252575f505d5b10514c59" class="ed_mailto u-email email p-name">Chaals Nevile</a> (Enterprise Ethereum Alliance)

Previous release:
<https://entethalliance.org/specs/ethtrust-sl/v1/>

Latest release URL:
<https://entethalliance.org/specs/ethtrust-sl/>

Contributors to this version:
Andrew Anderson (OpenZeppelin), Ismael Arribas (LACChain), Gianfranco Bazzani (OpenZeppelin), Kenan Bešić (ChainSecurity), Christopher Cordi (Individual), Stepan Chekhovskoi / Степан Чековской (Hacken), Jan Gorzny (Quantstamp), Opal Graham (CertiK), George Kobakhidze (ConsenSys), Michael Lewellen (OpenZeppelin), Dominik Muhs (ConsenSys), Carlo Parisi (Hacken), Anton Permenev (ChainSecurity), Marta Piekarska (Consensys), Przemek Siemion (Banco Santander), Grant Southey (ConsenSys), David Tarditi (CertiK / Individual), Michael Theriault (DTCC), Ben Towne (SAE), Morgan Weaver (OpenZeppelin), Gal Weizman (ConsenSys), Mehdi Zerouali

Copyright © 2020-2023 [Enterprise Ethereum Alliance](https://entethalliance.org/).

------------------------------------------------------------------------

## Abstrac

This document defines the requirements for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, a set of certifications that a smart contract has been reviewed and found not to have a defined set of security vulnerabilities.

## Status of This Documen

*This section describes the status of this document at the time of its publication. Newer documents may supersede this document.*

This document is an EEA Specification, published by the Enterprise Ethereum Alliance, Inc.

This specification is licensed by the Enterprise Ethereum Alliance, Inc. (EEA) under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) \[<a href="index.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\] Unless otherwise explicitly authorised in writing by the EEA, you can only use this specification in accordance with those terms.

Unless required by applicable law or agreed to in writing, this specification is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

This is the second version of the EEA EthTrust Security Levels Specification. This specification has been reviewed and approved for publishing by the EEA EthTrust Security Levels Working Group, and the EEA Board.

This version **supersedes** [version 1](https://entethalliance.org/specs/ethtrust-sl/v1/) of this Specification.

Please send any comments other than vulnerability notifications to the EEA through <https://entethalliance.org/contact/>, or as issues via the [EthTrust-public GitHub Repository](https://github.com/EntEthAlliance/eta-registry/issues/). To notify EEA of vulnerabilities, please follow the procedures outlined in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.

The Working Group *expects* at the time of publication to publish the next version of the Specification in 2025.

## Table of Contents

1.  <a href="index.html#sec-introduction" class="tocxref">1. Introduction</a>
    1.  <a href="index.html#sec-reading-the-spec" class="tocxref">1.1 How to read this specification</a>
        1.  <a href="index.html#sec-document-overview" class="tocxref">1.1.1 Overview of this Document</a>
        2.  <a href="index.html#sec-typographic-conventions" class="tocxref">1.1.2 Typographic Conventions</a>
        3.  <a href="index.html#sec-reading-requirements" class="tocxref">1.1.3 How to Read a Requirement</a>
            1.  <a href="index.html#sec-overriding-requirements" class="tocxref">1.1.3.1 Overriding Requirements</a>
            2.  <a href="index.html#sec-related-requirements" class="tocxref">1.1.3.2 Related Requirements</a>
    2.  <a href="index.html#sec-intro-why-certify-contracts" class="tocxref">1.2 Why Certify Contracts?</a>
    3.  <a href="index.html#sec-intro-developing-secure-contracts" class="tocxref">1.3 Developing Secure Smart Contracts</a>
    4.  <a href="index.html#sec-notifying-new-vulnerabilities" class="tocxref">1.4 Feedback and new vulnerabilities</a>
2.  <a href="index.html#conformance" class="tocxref">2. Conformance</a>
    1.  <a href="index.html#sec-conformance-claims" class="tocxref">2.1 Conformance Claims</a>
    2.  <a href="index.html#who-can-audit" class="tocxref">2.2 Who can offer EEA EthTrust Certification?</a>
    3.  <a href="index.html#sec-source-and-contracts" class="tocxref">2.3 Identifying what is certified</a>
3.  <a href="index.html#sec-security-considerations" class="tocxref">3. Security Considerations</a>
    1.  <a href="index.html#sec-eth-broader-considerations" class="tocxref">3.1 Smart Contracts in context - broader considerations</a>
    2.  <a href="index.html#sec-proxy-contract-considerations" class="tocxref">3.2 Upgradable Contracts</a>
    3.  <a href="index.html#sec-oracle-considerations" class="tocxref">3.3 Oracles</a>
    4.  <a href="index.html#sec-reentrancy-considerations" class="tocxref">3.4 External Interactions and Re-entrancy Attacks</a>
    5.  <a href="index.html#sec-signature-considerations" class="tocxref">3.5 Signature Mechanisms</a>
    6.  <a href="index.html#sec-gas-considerations" class="tocxref">3.6 Gas and Gas Prices</a>
    7.  <a href="index.html#sec-mev-considerations" class="tocxref">3.7 MEV (Maliciously Extracted Value)</a>
    8.  <a href="index.html#sec-source-compiler-considerations" class="tocxref">3.8 Source code, pragma, and compilers</a>
    9.  <a href="index.html#sec-deployment-considerations" class="tocxref">3.9 Contract Deployment</a>
    10. <a href="index.html#sec-realtime-monitoring-considerations" class="tocxref">3.10 Post-deployment Monitoring</a>
    11. <a href="index.html#sec-netupgrades-considerations" class="tocxref">3.11 Network Upgrades</a>
4.  <a href="index.html#sec-levels" class="tocxref">4. EEA EthTrust Security Levels</a>
    1.  <a href="index.html#sec-levels-one" class="tocxref">4.1 Security Level [S]</a>
        1.  <a href="index.html#sec-1-unicode" class="tocxref">4.1.1 Text and homoglyphs</a>
        2.  <a href="index.html#sec-1-external-calls" class="tocxref">4.1.2 External Calls</a>
        3.  <a href="index.html#sec-1-compile-improvements" class="tocxref">4.1.3 Improved Compilers</a>
        4.  <a href="index.html#sec-1-compiler-bugs" class="tocxref">4.1.4 Compiler Bugs</a>
    2.  <a href="index.html#sec-levels-two" class="tocxref">4.2 Security Level [M]</a>
        1.  <a href="index.html#sec-2-unicode" class="tocxref">4.2.1 Text and homoglyph attacks</a>
        2.  <a href="index.html#sec-2-external-calls" class="tocxref">4.2.2 External Calls</a>
        3.  <a href="index.html#sec-2-special-code" class="tocxref">4.2.3 Documented Defensive Coding</a>
        4.  <a href="index.html#sec-2-signature-requirements" class="tocxref">4.2.4 Signature Management</a>
        5.  <a href="index.html#sec-level-2-compiler-bugs" class="tocxref">4.2.5 Security Level [M] Compiler Bugs and Overriding Requirements</a>
    3.  <a href="index.html#sec-levels-three" class="tocxref">4.3 Security Level [Q]</a>
        1.  <a href="index.html#sec-3-documentation" class="tocxref">4.3.1 Documentation requirements</a>
        2.  <a href="index.html#sec-3-access-control" class="tocxref">4.3.2 Access Control</a>
    4.  <a href="index.html#sec-good-practice-recommendations" class="tocxref">4.4 Recommended Good Practices</a>
5.  <a href="index.html#sec-additional-information" class="tocxref">A. Additional Information</a>
    1.  <a href="index.html#sec-definitions" class="tocxref">A.1 Defined Terms</a>
    2.  <a href="index.html#sec-summary-of-requirements" class="tocxref">A.2 Summary of Requirements</a>
    3.  <a href="index.html#sec-acknowledgments" class="tocxref">A.3 Acknowledgments</a>
    4.  <a href="index.html#sec-changes" class="tocxref">A.4 Changes</a>
        1.  <a href="index.html#new-requirements" class="tocxref">A.4.1 New Requirements</a>
        2.  <a href="index.html#updated-requirements" class="tocxref">A.4.2 Updated Requirements</a>
        3.  <a href="index.html#requirements-removed" class="tocxref">A.4.3 Requirements removed</a>
6.  <a href="index.html#references" class="tocxref">B. References</a>
    1.  <a href="index.html#normative-references" class="tocxref">B.1 Normative references</a>
    2.  <a href="index.html#informative-references" class="tocxref">B.2 Informative references</a>

## 1. Introduction<a href="index.html#sec-introduction" class="self-link" aria-label="§"></a>

This document is the second version of the [**EEA EthTrust Security Levels Specification**](https://entethalliance.org/specs/ethtrust-sl/), that defines the requirements for granting <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> to a smart contract written in Solidity.

This version **supersedes** the first version of this specification, the [EEA EthTrust Security Levels Specification version 1](https://entethalliance.org/specs/ethtrust-sl/v1/) \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

<a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is a claim by a security reviewer that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is not vulnerable to a number of known attacks or failures to operate as expected, based on the reviewer's assessment against those specific requirements.

No amount of security review can guarantee that a smart contract is secure against **all possible** vulnerabilities, as explained in <a href="index.html#sec-security-considerations" class="sec-ref">§ 3. Security Considerations</a>. However reviewing a smart contract according to the requirements in this specification provides assurance that it is not vulnerable to a known set of potential attacks.

This assurance is backed not only by the reputation of the reviewer, but by the collective reputations of the multiple experts in security from many competing organizations, who collaborated within the EEA to ensure this specification defines protections against a real and significant set of known vulnerabilities.

### 1.1 How to read this specification<a href="index.html#sec-reading-the-spec" class="self-link" aria-label="§"></a>

*This section is non-normative.*

This section describes how to understand this specification, including the conventions used for examples and requirements, core concepts, references, informative sections, etc.

#### 1.1.1 Overview of this Document<a href="index.html#sec-document-overview" class="self-link" aria-label="§"></a>

Broadly, the document is structured as follows:

Front matter
Basic information about the document - authors, copyright, etc.

Conformance section
What it means and looks like to claim conformance to this specification.

Security Considerations
A general introduction to key security concepts relevant to Smart Contracts.

EthTrust Security Levels
The core of the document. Requirements that security reviews should meet, grouped by levels and then thematically.

Additional Information
- A glossary of terms defined.
- A summary of each requirement that can be used as a checklist for readers familiar with the details.
- A summary of substantial changes made since the previous release version.
- Acknowledgements

References
Further reading, including normative references necessary to the requirements and informative references that expand on topics described in the specification.

This specification is accompanied by a [Checklist](checklist.html), that lists the requirements in a handy table. That checklist can be used to help developers or reviewers familiar with the specification to quickly remind themselves of each individual requirement and track whether they have tested it. In case of any discrepancy, the normative text is in this specification document.

#### 1.1.2 Typographic Conventions<a href="index.html#sec-typographic-conventions" class="self-link" aria-label="§"></a>

The structure and formatting of requirements is described in detail in <a href="index.html#sec-reading-requirements" class="sec-ref">§ 1.1.3 How to Read a Requirement</a>.

Examples are given in some places. These are not requirements and are not normative. They are distinguished by a background with a border and generally a title, like so:

<a href="index.html#example-1-example-an-example-example" class="self-link">Example 1</a>: Example: An example example

There can be text with `code()` inline in an example, as well as blocks of code:

``` solidity
  // SPDX-License-Identifier: MIT
  pragma solidity 0.8.0;

  contract HelloWorld{
      string public greeting = "Hello World";
  }

```

Some examples are given of vulnerable code, or what NOT to do. It is a very bad idea to copy such examples into production code. These are marked as warnings:

Warning

<a href="index.html#example-2-example-problem-don-t-copy-this" class="self-link">Example 2</a>: Example problem: Don't copy this

Deploying code that has not been reviewed for security is a bad idea.

Definitions of terms are formatted Like This and subsequent references to defined terms are rendered as links <a href="index.html#dfn-like-this" class="internalDFN" data-link-type="dfn">Like This</a>.

References to other documents are links to the relevant entry in the <a href="index.html#references" class="sec-ref">§ B. References</a>, within square brackets: \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\].

Links to requirements begin with a <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a>: **\[S\]**, **\[M\]** or **\[Q\]**, and <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a> begin with **\[GP\]**. They then include the requirement or good practice name. They are rendered as links in bold type:

Example of a link to [**\[M\] Document Special Code Use**](index.html#req-2-documented).

Variables, introduced to be described further on in a statement or requirement, are formatted as `var`.

Occasional explanatory notes, presented as follows, are not normative and do not specify formal requirements.

Note: Notes are explanatory

The content of a Note is meant to be useful, but does not form a requirement.

#### 1.1.3 How to Read a Requirement<a href="index.html#sec-reading-requirements" class="self-link" aria-label="§"></a>

The core of this document is the requirements, that collectively define <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

Requirements have

- a [Security Level](index.html#sec-levels) that is one of "[**\[S\]**](index.html#sec-levels-one)", "[**\[M\]**](index.html#sec-levels-two)", or "[**\[Q\]**](index.html#sec-levels-three)",
- a name,
- a link (identified with "🔗") to its URL, and
- a statement of what *MUST* be achieved to meet the requirement.

Some requirements at the same <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> are grouped in a subsection, because they are related to a particular theme or area of potential attacks.

Requirements are followed by explanation, that can include why the requirement is important, how to test for it, links to <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>, test cases, and links to other useful information.

As well as Requirements, this document includes some <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>, that are formatted similarly with an apparent Security Level of "**\[GP\]**". It is not necessary to implement these in order to conform to the specification, but if carefully implemented they can improve the security of smart contracts.

The following requirement:

<a href="index.html#example-3-a-simple-requirement" class="self-link">Example 3</a>: A simple requiremen

**\[S\] Compiler Bug SOL-2022-5 with `.push()` <a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

Until Solidity compiler version 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using code through `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly).

is a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, denoted by the "**\[S\]**" before its name. Its name is **Compiler Bug SOL-2022-5 with `.push()`**. Its URL **in this version 2 of the specification**, as linked from the " 🔗 " character, is [https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2022-5-push](index.html#req-1-compiler-SOL-2022-5-push).

The statement of requirement is:

> <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

Following the requirement is a brief explanation of the relevant vulnerability, and links to further information.

Note

Good Practices are formatted the same way as Requirements, with an apparent level of **\[GP\]**. However, as explained in <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a> meeting them is not necessary and does not in itself change conformance to this specification.

##### 1.1.3.1 Overriding Requirements<a href="index.html#sec-overriding-requirements" class="self-link" aria-label="§"></a>

For some requirements, the statement will include an alternative condition, introduced with the keyword **unless**, that identifies one or more Overriding Requirements. These are requirements at a higher Security Level, that can be satisfied to achieve conformance if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet the lower-level requirement as stated. In some cases it is necessary to meet more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> to meet the requirement they override. In this case, the requirements are described as a Set of Overriding Requirements. It is necessary to meet all the requirements in a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> in order to meet the requirement that is overriden.

In a number of cases, there will be more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> that can be met in order to satisfy a given requirement. For example, it is sometimes possible to meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> Requirement either by directly fulfilling it, or by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, or by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>.

<a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> enable simpler testing for common simple cases. For more complex <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, that uses features which need to be handled with extra care to avoid introducing vulnerabilities, they ensure such usage is appropriately checked.

In a typical case of an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, they apply in relatively unusual cases or where automated systems are generally unable to verify that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. Further verification of the applicable <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> can determine that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is using a feature appropriately, and therefore passes the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement.

If there is not an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for a requirement that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> does not meet, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is not eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. However, even for such cases, note the Recommended Good Practice [**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible); meeting any requirements in this specification will improve the security of smart contracts.

In the following requirement:

- the Security Level is "**\[S\]**",

- the name is "**No `tx.origin`**", and

- the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> is "[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)".

  <a href="index.html#example-4-example-a-requirement-with-an-overriding-requirement" class="self-link">Example 4</a>: Example: A requirement with an Overriding Requiremen
  **\[S\] No `tx.origin` [🔗](index.html#req-1-no-tx.origin)**
  <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain a `tx.origin` instruction
  **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin).

The requirement that the tested code does not contain a `tx.origin` instruction is automatically verifiable.

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that does have a valid use for `tx.origin`, as decided by the auditor, and meets the Security Level \[Q\] <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin) conforms to this Security Level \[S\] requirement.

Requirements that are an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for another, or are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, expicitly mention that:

<a href="index.html#example-5-example-overriding-requirement" class="self-link">Example 5</a>: Example: Overriding Requiremen

**\[M\] No Unnecessary Unicode Controls [🔗](index.html#req-2-unicode-bdo)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirement</a> for [\[S\] No Unicode Direction Control Characters](index.html#req-1-unicode-bdo).

##### 1.1.3.2 Related Requirements<a href="index.html#sec-related-requirements" class="self-link" aria-label="§"></a>

Many requirements have Related Requirements, which are requirements that address thematically related issues.

The links to them are provided as useful information. Unlike <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>, meeting Related Requirements does not substitute for meeting a specific requirement in order to achieve conformance.

### 1.2 Why Certify Contracts?<a href="index.html#sec-intro-why-certify-contracts" class="self-link" aria-label="§"></a>

*This section is non-normative.*

A number of smart contracts that power decentralized applications on Ethereum have been found to contain security issues, and today it is often difficult or impossible in practice to see how secure an address or contract is before initiating a transaction. The Defi space in particular has exploded with a flurry of activity, with individuals and organizations approving transactions in token contracts, swapping tokens, and adding liquidity to pools in quick succession, sometimes without stopping to check security. For Ethereum to be trusted as a transaction layer, enterprises storing critical data or financial institutions moving large amounts of capital need a clear signal that a contract has had appropriate security audits.

Reviewing early, in particular before production deployment, is especially important in the context of blockchain development because the costs in time, effort, funds, and/or credibility, of attempting to update or patch a smart contract after deployment are generally much higher than in other software development contexts.

This smart contract security standard is designed to increase confidence in the quality of security audits for smart contracts, and thus to raise trust in the Ethereum ecosystem as a global settlement layer for all types of transactions across all types of industry sectors, for the benefit of the entire Ethereum ecosystem.

Certification also provides value to the actual or potential users of a smart contract, and others who could be affected by the use or abuse of a particular smart contract but are not themselves direct users. By limiting exposure to certain known weaknesses through <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, these stakeholders benefit from reduced risk and increased confidence in the security of assets held in or managed by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This assurance is not complete; for example it relies on the competence and integrity of the auditor issuing the certification. That is generally not completely knowable. Professional reputations can change based on subsequent performance of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. This is especially so if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> becomes sufficiently high-profile to motivate exploitation of any known weaknesses remaining after certification.

Finally, smart contract developers and ecosystem stakeholders receive value when others (including direct competitors) complete the certification process, because it means those other contracts are less likely to generate exploitation-related headlines which can lead to negative perceptions of Ethereum technology as insecure or high risk, by the general public including business leaders, prospective customers/users, regulators, and investors.

The value of smart contract security certification is in some ways analogous to the certification processes applicable to aircraft parts. Most directly, it helps reduce risks for part manufacturers and the integrators who use those parts as components of a more complex structure, by providing assurance of a minimum level of quality. Less directly, these processes significantly reduce aviation accidents and crashes, saving lives and earning the trust of both regulators and customers who consider the safety and risk of the industry and its supporting technology as a whole. Many safety certification processes began as voluntary procedures created by a manufacturer, or specified and required by a consortium of customers representing a significant fraction of the total market. Having proven their value, some of these certification processes are now required by law, to protect the public (including ground-based bystanders).

We hope the value of the certification process motivates frequent use, and furthers development of automated tools that can make the evaluation process easier and cheaper.

As new security vulnerabilities, issues in this specification, and challenges in implementation are discovered, we hope they will lead to both change requests and increased participation in the [Enterprise Ethereum Alliance](https://entethalliance.org)'s [EthTrust Security Levels Working Group](https://entethalliance.org/groups/EthTrust/) or its successors, responsible for developing and maintaining this specification.

### 1.3 Developing Secure Smart Contracts<a href="index.html#sec-intro-developing-secure-contracts" class="self-link" aria-label="§"></a>

*This section is non-normative.*

Security issues that this specification calls for checking are not necessarily obvious to smart contract developers, especially relative newcomers in a quickly growing field.

By walking their own code through the certification process, even if no prospective customer requires it, a smart contract developer can discover ways their code is vulnerable to known weaknesses and fix that code prior to deployment.

Developers ought to make their code as secure as possible. Instead of aiming to fulfil only the requirements to conform at a particular Security Level, ensuring that code implements as many requirements of this specification as possible, per [**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible), helps ensure the developer has considered all the vulnerabilities this specfication addresses.

Aside from the obvious reputational benefit, developers will learn from this process, improving their understanding of potential weaknesses and thus their ability to avoid them completely in their own work.

For an organization developing and deploying smart contracts, this process reduces the amount of work required for security reviews, and risks both to their credibility, and to their assets and other capital.

### 1.4 Feedback and new vulnerabilities<a href="index.html#sec-notifying-new-vulnerabilities" class="self-link" aria-label="§"></a>

The Working Group seeks feedback on this specification: Implementation experience, suggestions to improve clarity, or questions if a particular section or requirement is difficut to understand.

We also explicitly want feedback about the use of a standard machine-readable format for <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claims</a>, whether being suitable for storing on a blockchain is important for such a format, and for other use cases.

EEA members are encouraged to provide feedback through joining the Working Group. Anyone can also provide feedback through the a href="https://github.com/EntEthAlliance/eta-registry/issues/"\>EthTrust-public GitHub Repository, or via EEA's contact pages at <https://entethalliance.org/contact/> and it will be forwarded to the Working Group as appropriate.

We expect that new vulnerabilities will be discovered after this specification is published. To ensure that we consider them for inclusion in a revised version, we welcome notification of them. EEA has created a specific email address to let us know about new security vulnerabilities: [\[email protected\]](https://entethalliance.org/cdn-cgi/l/email-protection#84f7e1e7f1f6edf0fda9eaebf0ede7e1f7c4e1eaf0e1f0ece5e8e8ede5eae7e1aaebf6e3). Information sent to this address *SHOULD* be sufficient to identify and rectify the problem described, and *SHOULD* include references to other discussions of the problem. It will be assessed by EEA staff, and then forwarded to the Working Group to address the issue.

When these vulnerabilities affect the Solidity compiler, or suggest modifications to the compiler that would help mitigate the problem, the Solidity Development community *SHOULD* be notified, as described in \[<a href="index.html#bib-solidity-reports" class="bibref" data-link-type="biblio" title="Reporting a Vulnerability, in Security Policy">solidity-reports</a>\].

## 2. Conformance<a href="index.html#conformance" class="self-link" aria-label="§"></a>

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) \[<a href="index.html#bib-rfc2119" class="bibref" data-link-type="biblio" title="Key words for use in RFCs to Indicate Requirement Levels">RFC2119</a>\] \[<a href="index.html#bib-rfc8174" class="bibref" data-link-type="biblio" title="Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words">RFC8174</a>\] when, and only when, they appear in all capitals, as shown here.

This specification defines a number of requirements. As described in <a href="index.html#sec-reading-requirements" class="sec-ref">§ 1.1.3 How to Read a Requirement</a>, each requirement has a Security Level (\[S\], \[M\] or \[Q\]), and a statement of the requirement that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet.

In order to achieve <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at a specific Security Level, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet **all the requirements for that Security Level**, including all the requirements for lower Security Levels. Some requirements can either be met directly, or by meeting one or more <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirements</a> that mean the requirement is considered met.

This document does not create an affirmative duty of compliance on any party, though requirements to comply with it could be created by contract negotiations or other processes with prospective customers or investors.

Section <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>, contains further recommendations. Although they are formatted similarly to requirements, they begin with a "level" marker \[GP\]. There is no requirement to test for these; however careful implementation and testing is *RECOMMENDED*.

Note that good implementation of the <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a> can enhance security, but in some cases incomplete or low-quality implementation could **reduce** security.

### 2.1 Conformance Claims<a href="index.html#sec-conformance-claims" class="self-link" aria-label="§"></a>

To grant <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> EEA EthTrust Certification, an auditor provides a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>, that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirements of the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> for which it is certified.

There is no required format for a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid conformance claim</a> for Version 1 of this specification, beyond being legible and containing the required information as specified in this section.

Note: Machine-readable formats

The Working Group believes that a standard machine-readable format for Conformance Claims would be useful, and seeks feedback on this question as well as concrete proposals for such a format, which *MAY* be adopted in a subsequent version.

A Valid Conformance Claim *MUST* include:

- The date on which the certification was issued, in 'YYYY-MM-DD' format.
- The <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> (of those listed at \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]) for which the certification is valid.
- The version of the EEA EthTrust Security Levels specification for which the contract is certified (this specification is "Version 2").
- A name and a URL for the organisation or software issuing the certification.
- The <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> (**"S"**, "**M**", or "**Q**") that the <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> claims.
- A \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the compiled bytecode for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number.
- A \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the Solidity source code for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number.
- The compiler options applied for each compilation.
- The contract metadata generated by the compiler.
- A list of the requirements which were tested and a statement for each one, noting whether the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. This *MAY* include further information.
- An explicit notice stating that <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> does not provide any warranty or formal guarantee
  - of the overall security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, nor
  - that the project is free from bugs or vulnerabilities.

  This notice *SHOULD* state that <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> represents the best efforts of the issuer to detect and identify certain known vulnerabilities that can affect Smart Contracts.
- For conformance claims where certification is granted because the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> met an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, the conformance claim *MUST* include the results for the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> met, and *MAY* omit the results for the requirement(s) whose results were thus unnecessary to determine conformance.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> for <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> *MUST* contain a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the documentation provided to meet [**\[Q\] Document Contract Logic**](index.html#req-3-documented) and [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *SHOULD* include:

- A contact address for questions about or challenges to the certification.
- Descriptions of conformance to the good practices described in <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* include:

- An address where a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the conformance claim has been recorded on an identified network, e.g. Ethereum Mainnet.
- An address of the contract deployed on an identified network, e.g. Ethereum Mainnet.

Valid values of EVM versions are those listed in the Solidity documentation \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]. As of November 2023 the two most recent are `shanghai` and `paris`.

### 2.2 Who can offer EEA EthTrust Certification?<a href="index.html#who-can-audit" class="self-link" aria-label="§"></a>

*This section is non-normative.*

This version of the specification does not make any restrictions on who can perform an audit and provide <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. There is no certification process defined for auditors or tools who grant certification. This means that Auditors' claims of performing accurate tests are made by themselves. There is always a possibility of fraud, misrepresentation, or incompetence on the part of any auditor who offers "EEA EthTrust certification" for Version 1.

Note

In principle anyone can submit a smart contract for verification. However submitters need to be aware of any restrictions on usage arising from copyright conditions or the like. In addition, meeting certain requirements can be more difficult to demonstrate in a situation of limited control over the development of the smart contract.

The Working Group expects its own members, who wrote the specification, to behave to a high standard of integrity and to know the specification well, and notes that there are many others who also do so.

The Working Group or EEA *MAY* seek to develop an auditor certification program for subsequent versions of the EEA EthTrust Security Levels Specification.

### 2.3 Identifying what is certified<a href="index.html#sec-source-and-contracts" class="self-link" aria-label="§"></a>

An EEA EthTrust evaluation is performed on Tested Code, which means the Solidity source code for a smart contract or several related smart contracts, along with the bytecode generated by compiling the code with specified parameters.

If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is divided into more than one smart contract, each deployable at a single address, it is referred to as a Set Of Contracts.

## 3. Security Considerations<a href="index.html#sec-security-considerations" class="self-link" aria-label="§"></a>

*This section is non-normative.*

Security of information systems is a major field of work. There are risks inherent in any system of even moderate complexity.

This specification describes testing for security problems in Ethereum smart contracts. However there is no such thing as perfect security. EEA EthTrust certification means that at least a defined minimum set of checks has been performed on a smart contract. **This does not mean the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> definitely has no security vulnerabilities**. From time to time new security vulnerabilities are identified. Manual auditing procedures require skill and judgement. This means there is always a possibility that a vulnerability is not noticed in review.

### 3.1 Smart Contracts in context - broader considerations<a href="index.html#sec-eth-broader-considerations" class="self-link" aria-label="§"></a>

Ethereum is based on a model of account holders authorising transactions between accounts. It is very difficult to stop a malicious actor with a privileged key from using that to cause undesirable or otherwise bad outcomes.

Likewise, in practice users often interact with smart contracts through a "Ðapp" or "distributed app". Web Application Security is its own extensive area of research and development, beyond the scope of this specification.

### 3.2 Upgradable Contracts<a href="index.html#sec-proxy-contract-considerations" class="self-link" aria-label="§"></a>

Smart contracts in Ethereum are immutable by default. However, for some scenarios, it is desirable to modify them, for example to add new features or fix bugs. An Upgradable Contract is any type of contract that fulfills these needs by enabling changes to the code executed via calls to a fixed address.

Some common patterns for Upgradable Contracts use a Proxy Contract: a simple wrapper that users interact with directly that is in charge of forwarding transactions to and from another contract (called the Execution Contract in this document, but also known as a Logic Contract), which contains the code that actually implements the Smart Contract's behaviour.

The <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be replaced while the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>, acting as the access point, is never changed. Both contracts are still immutable in the sense that their code cannot be changed, but one <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be swapped out with another. The <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> can thus point to a different implementation and in doing so, the software is "upgraded".

This means that a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> that follow this pattern to make an <a href="index.html#dfn-upgradable-contract" class="internalDFN" data-link-type="dfn">Upgradable Contract</a> generally cannot be considered immutable, as the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> itself could redirect calls to a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a>, which could be insecure or malicous. By meeting the requirements for [access control](index.html#sec-3-access-control) in this specification to restrict upgrade capabilities enabling new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contracts</a> to be deployed, and by documenting upgrade patterns and following that documentation per [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), deployers of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can demonstrate reliability. In general, EthTrust certification of a <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> does not apply to the internal logic of an Upgradable Contract, so a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> needs to be certified before upgrading to it through the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>.

There are several possible variations on this core structure, for example having a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> that includes multiple <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contracts</a>. In the attack known as a Metamorphic Upgrade, a series of Smart Contracts are used to convince people (e.g. voters in a DAO) to approve a certain piece of code for deployment, but one of the proxy contracts in the chain is updated to deploy different, malicious, code.

Other patterns rely on using the `CREATE2` instruction to deploy a Smart Contract at a known address. It is currently possible to remove the code at that address using the `selfdestruct()` method, and then deploy new code to that address. This possibility is sometimes used to save Gas Fees, but it is also used in a <a href="index.html#dfn-metamorphic-upgrade" class="internalDFN" data-link-type="dfn">Metamorphic Upgrade</a> attack.

### 3.3 Oracles<a href="index.html#sec-oracle-considerations" class="self-link" aria-label="§"></a>

A common feature of Ethereum networks is the use of Oracles: functions that can provide information sourced from on-chain or off-chain data. Oracles solve a range of problems, from providing random number generation to asset data, managing the operation of liquidity pools, and enabling access to weather, sports, or other special-interest information. Oracles are used heavily in DeFi and gaming, where asset data and randomization are central to protocol design.

This specification contains requirements to check that smart contracts are sufficiently robust to deal appropriately with whatever information is returned, including the possibility of malformed data that can be deliberately crafted for oracle-specific attacks.

While some aspects of <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are within the scope of this specification, it is still possible that an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> provides misinformation or even actively produces harmful disinformation.

The two key considerations are the risk of corrupted or manipulated data, and the risk of oracle failure. Vulnerabilities related to these considerations - excessive reliance on <a href="index.html#dfn-twap" class="internalDFN" data-link-type="dfn">TWAP</a>, and unsafe management of oracle failure - have occurred repeatedly leading to the loss of millions of dollars of value on various DeFi protocols.

While many high-quality and trusted <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are available, it is possible to suffer an attack even with legitimate data. When calling on an Oracle, data received needs to be be checked for staleness to avoid <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-running</a> attacks. Even in non-DeFi scenarios, such as a source of randomness, it is often important to reset the data source for each transaction, to avoid arbitrage on the next transaction.

A common strategy for pricing Oracles is to provide a time-weighted average price (known as TWAP). This provides some level of security against sudden spikes such as those created by a Flashloan attack, but at the cost of providing stale information.

It is important to choose time windows carefully: when a time window is too wide, it won't reflect volatile asset prices, leaking opportunities to arbitrageurs. However the "instantaneous" price of an asset is often not a good data point: It is the most manipulable piece of Oracle data, and in any event it will always be stale by the time a transaction is executed.

Oracles that collate a wide variety of source data, clean outliers from their data, and are well-regarded by the community, are more likely to be reliable. If an Oracle is off-chain, whether it reflects stale on-chain data, or reliable and accurate data that is truly off-chain, is an important consideration.

Even an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> using a well-chosen <a href="index.html#dfn-twap" class="internalDFN" data-link-type="dfn">TWAP</a> can enable a liquidity pool or other DeFi structure to be manipulated, especially by taking advantage of flashloans and flashswaps to cheaply raise funds. If an asset targeted for manipulation has insufficient liquidity this can render it vulnerable to large price swings by an attacker holding only a relatively small amount of liquidity.

The second important consideration when using <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> is that of a graceful failure scenario. What happens if an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> no longer returns data, or suddenly returns an unlikely value? At least one protocol has suffered losses due to 'hanging' on a minimum value in the rare event of a price crash rather than truly dropping to zero, with traders who accumulated large amounts of a near zero-priced asset able to sell it back to the protocol. Hardcoding a minimum or maximum value can lead to problems reflecting reality.

### 3.4 External Interactions and Re-entrancy Attacks<a href="index.html#sec-reentrancy-considerations" class="self-link" aria-label="§"></a>

Code that relies on external code can introduce multiple attack vectors. This includes cases where an external dependency contains malicious code or has been subject to malicious manipulation through security vulnerabilities. However, failure to adequately manage the possible outcomes of an external call can also introduce security vulnerabilities.

One of the most commonly cited vulnerabilities in Ethereum Smart Contracts is Re-entrancy Attacks. These attacks allow malicious contracts to make a call back into the contract that called it before the originating contract's function call has been completed. This effect causes the calling contract to complete its processing in unintended ways, for example, by making unexpected changes to its state variables.

A Read-only Re-entrancy Attack arises when a view function is reentered. These are a particular additional danger because such functions often lack safeguards since they don't modify the contract's state. However, if the state is inconsistent, incorrect values could be reported. This deception can mislead other protocols into reading inaccurate state values, potentially leading to unintended actions. This issue primarily affects other contracts that rely on the accurate reporting of state from these view functions, rather than the contract itself being reentered.

### 3.5 Signature Mechanisms<a href="index.html#sec-signature-considerations" class="self-link" aria-label="§"></a>

Some requirements in the document refer to Malleable Signatures. These are signatures created according to a scheme constructed so that, given a message and a signature, it is possible to efficiently compute the signature of a different message - usually one that has been transformed in specific ways. While there are valuable use cases that such signature schemes allow, if not used carefully they can lead to vulnerabilities, which is why this specification seeks to constrain their use appropriately. In a similar vein, Hash Collisions could occur for hashed messages where the input used is malleable, allowing the same signature to be used for two distinct messages.

Other requirements in the document are related to exploits which take advantage of ambiguity in the input used to created the signed message. When a signed message does not include enough identifying information concerning where, when, and how many times it is intended to be used, the message signature could be used (or reused) in unintended functions, contracts, chains, or even at unintended times.

For more information on this topic, and the potential for exploitation, see also \[<a href="index.html#bib-chase" class="bibref" data-link-type="biblio" title="Malleable Signatures: New Definitions and Delegatable Anonymous Credentials">chase</a>\].

### 3.6 Gas and Gas Prices<a href="index.html#sec-gas-considerations" class="self-link" aria-label="§"></a>

Gas Griefing is the deliberate abuse of the Gas mechanism that Ethereum uses to regulate the consumption of computing power, to cause an unexpected or adverse outcome much in the style of a Denial of Service attack. Because Ethereum is designed with the Gas mechanism as a regulating feature, it is insufficient to simply check that a transaction has enough Gas; checking for Gas Griefing needs to take into account the goals and business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements.

Gas Siphoning is another abuse of the Gas mechanism that Ethereum uses to regulate the consumption of computing power, where attackers steal Gas from vulnerable contracts either to deny service or for their own gain (e.g. to mint <a href="index.html#dfn-gas-tokens" class="internalDFN" data-link-type="dfn">Gas Tokens</a>). Similar to Gas Griefing, checking for Gas Siphoning requires careful consideration of the goals and business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements.

Gas Tokens use Gas when minted and free slightly less Gas when burned. Gas Tokens minted when Gas prices are low can be burned to subsidize Ethereum transactions when Gas prices are high.

In addition, a common feature of Ethereum <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a> is to change the Gas Price of specific operations. EEA EthTrust certification only applies for the <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> specified; it is not valid for other <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>. Thus it is important to recheck code to ensure its security properties remain the same across <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a>, or take remedial action.

### 3.7 MEV (Maliciously Extracted Value)<a href="index.html#sec-mev-considerations" class="self-link" aria-label="§"></a>

MEV, used in this document to mean "Maliciously Extracted Value", refers to the potential for block producers or other paticipants in a blockchain to extract value that is not intentionally given to them, in other words to steal it, by maliciously reordering transactions, as in <a href="index.html#dfn-timing-attacks" class="internalDFN" data-link-type="dfn">Timing Attacks</a>, or suppressing them.

<a href="index.html#example-6-an-mev-attack" class="self-link">Example 6</a>: An MEV attack

A Smart Contract promises an award for the first transaction that answers a question. A block producer that knows the answer can drop all transactions that send the answer, except for their own in the block.

Note

The term MEV is commonly expanded as "Miner Extracted Value", and sometimes "Maximum Extractable Value". As in the example above, sometimes block miners can take best advantage of a vulnerability. But MEV can be exploited by other participants, for example duplicating most of a submitted transaction, but offering a higher fee so it is processed first.

Some MEV attacks can be prevented by careful consideration of the information that is included in a transaction, including the parameters required by a contract.

Other strategies include the use of hash commitment schemes \[<a href="index.html#bib-hash-commit" class="bibref" data-link-type="biblio" title="Commitment scheme - WikiPedia">hash-commit</a>\], batch execution, private transactions \[<a href="index.html#bib-eea-clients" class="bibref" data-link-type="biblio" title="Enterprise Ethereum Client Specification - Editors&#39; draft">EEA-clients</a>\], Layer 2 \[<a href="index.html#bib-eea-l2" class="bibref" data-link-type="biblio" title="Introduction to Ethereum Layer 2">EEA-L2</a>\], or an extension to establish the ordering of transactions before releasing sensitive information to all nodes participating in a blockchain.

The Ethereum Foundation curates up to date information on MEV \[<a href="index.html#bib-ef-mev" class="bibref" data-link-type="biblio" title="Maximal Extractable Value (MEV)">EF-MEV</a>\].

Censorship Attacks occur when a block processor actively suppresses a proposed transaction, for their own benefit.

Future Block Attacks are those where a block proposer knows they will produce a paticular block, and uses this information to craft the block to maliciously extract value from other transactions. See for example \[<a href="index.html#bib-futureblock" class="bibref" data-link-type="biblio" title="Future-block MEV in Proof of Stake">futureblock</a>\] or \[<a href="index.html#bib-postmerge-mev" class="bibref" data-link-type="biblio" title="Why is Oracle Manipulation after the Merge so cheap? Multi-Block MEV">postmerge-mev</a>\].

Timing Attacks are a class of MEV attacks where an adversary benefits from placing their or a victim's transactions earlier or later in a block. They include <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, <a href="index.html#dfn-back-running" class="internalDFN" data-link-type="dfn">Back-Running</a>, and <a href="index.html#dfn-sandwich-attacks" class="internalDFN" data-link-type="dfn">Sandwich Attacks</a>.

Front-Running is based on the fact that transactions are visible to the participants in the network before they are added to a block. This allows a malicious participant to submit an alternative transaction, frustrating the aim of the original transaction.

<a href="index.html#example-7-front-running-attack-strategy" class="self-link">Example 7</a>: Front Running Attack strategy

In a system designed to attest original authorship, a malicious participant uses the information in a claim of authorship to create a rival claim, and adds their claim to a block first.

Back-Running is similar to <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, except the attacker places their transactions after the one they are attacking.

In Sandwich Attacks, an attacker places a victim's transaction undesirably between two other transactions.

<a href="index.html#example-8-sandwich-attack-strategy" class="self-link">Example 8</a>: Sandwich Attack strategy

An attacker creates a buy and sell transaction before and after a victim's buy transaction, artificially driving the price up for the victim and providing no-risk profit for the attacker at the victim's expense.

### 3.8 Source code, pragma, and compilers<a href="index.html#sec-source-compiler-considerations" class="self-link" aria-label="§"></a>

This version of the specification requires the compiled bytecode as well as the Solidity Source Code that together constitute the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Solidity is by a large measure the most common programming language for Ethereum smart contracts, and benefits of requiring source code in Solidity include

- it simplifies a number of tests, and
- there is substantial security research done on Solidity source code.

Solidity allows the source code to specify the Solidity compiler version used with a `pragma` statement. This specification currently has no requirement for a specific `pragma`, but it is good practice to ensure that the pragma refers to a bounded set of Solidity compiler versions, where it is known that those Solidity compiler versions produce identical bytecode from the given source code.

There are some drawbacks to requiring Solidity Source code. The most obvious is that some code that is not written in Solidity. Different languages have different features and often support different coding styles.

Perhaps more important, it means that a deployed contract written in Solidity cannot be tested directly without someone making the source code available.

Another important limitation introduced by reading source code is that it is subject to <a href="index.html#dfn-homoglyph-attacks" class="internalDFN" data-link-type="dfn">Homoglyph Attacks</a>, where characters that look the same but are different such as Latin "p" and Cyrillic "р", can deceive people visually reading the source code, to disguise malicious behaviour. There are related attacks that use features such as <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode Direction Control Characters</a> or take advantage of inconsistent normalisation of combining characters to achieve the same type of deceptions.

### 3.9 Contract Deployment<a href="index.html#sec-deployment-considerations" class="self-link" aria-label="§"></a>

This specification primarily addresses vulnerabilities that arise in Smart Contract code. However it is important to note that the deployment of a smart contract is often a crucial element of protocol operation. Some aspects of smart contract security primarily depend on how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> gets deployed. Even audited protocols can be easily exploited if deployed naively.

Code written for a specific blockchain might depend on features available in that blockchain, and when the code is deployed to a different chain that is compatible (e.g. it uses the same <a href="index.html#dfn-evm" class="internalDFN" data-link-type="dfn">EVM</a> to process smart contracts), the difference in features can expose a vulnerability. For any contract deployed to a blockchain or parachain that uses a patched fork of the EVM, common security assumptions may no longer apply to that EVM. It is valuable to deploy <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EthTrust Certified</a> contracts to a testnet for each chain first, and undergo thorough penetration testing.

Of particular concern is the issue of upgradeable proxy-type contracts, and any contract utilizing an initializer function in deployment. Many protocols have been hacked due to accidentally leaving their initializer functions unprotected, or using a non-atomic deployment in which the initializing function is not called in the same transaction as the contract deployment. This scenario is ripe for <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-running</a> attacks, and can result in protocol takeover by malicious parties, and theft or loss of funds. Initializing any initializable contract in the same transaction as its deployment reduces the risk that a malicious actor takes control of the contract.

Moreover, the deployment implications of assigning access roles to `msg.sender` or other variables in constructors and initializers need careful consideration. This is discussed further in <a href="index.html#sec-3-access-control" class="sec-ref">§ 4.3.2 Access Control</a> requirements.

Several libraries and tools exist specifically for safe proxy usage and safe contract deployment. From command-line tools to libraries to sophisticated UI-based deployment tools, many solutions exist to prevent unsafe proxy deployments and upgrades.

Using access control for a given contract's initializer, and limiting the number of times an initializer can be called on or after deployment, can enhance safety and transparency for the protocol itself and its users. Furthermore, a function that disables the ability to initialize an <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can prevent any future initializer calls after deployment, preventing later attacks or accidents.

Although this specification does not require that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> has been deployed, some requirements are more easily tested when code has been deployed to a blockchain, or can only be thoroughly tested "*in situ*".

### 3.10 Post-deployment Monitoring<a href="index.html#sec-realtime-monitoring-considerations" class="self-link" aria-label="§"></a>

While monitoring Smart Contracts after deployment is beyond the formal scope of this specification, it is an important consideration for Smart Contract security. New attack techniques arise from time to time, and some attacks can only be prevented by active measures implemented in real time. Monitoring of on-chain activity can help detect attacks before it is too late to stop them.

Monitoring, backed by an automated dataset, can enable identifying an attack that has occurred elsewhere, even on other blockchains.

Automated monitoring can facilitate rapid response, producing alerts or automatically initiating action, improving the security of contracts that might be compromised when security responses are delayed by even a few blocks.

However, it can be difficult to determine the difference between an attack and anamolous behaviour on the part of individuals. Relying purely on automated monitoring can expose a blockchain to the risk that a malicious actor deliberately triggers an automated security response to damage a blockchain or project, analogous to a Denial of Service attack.

### 3.11 Network Upgrades<a href="index.html#sec-netupgrades-considerations" class="self-link" aria-label="§"></a>

The EVM, or Ethereum Virtual Machine, acts as a distributed state machine for the Ethereum network, computing state changes resulting from transactions. The EVM maintains the network state for simple transfers of Ether, as well as more complex Smart Contract interactions. In other words, it is the "computer" (although in fact it is software) that runs the code of Smart Contracts.

From time to time the Ethereum community implements a Network Upgrade, sometimes also called a **hard fork**. This is a change to Ethereum that is backwards-incompatible. Because they *typically* change the EVM, Ethereum Mainnet <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a> generally correspond to <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>.

A <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can affect more or less any aspect of Ethereum, including changing EVM opcodes or their Gas price, changing how blocks are added, or how rewards are paid, among many possibilities.

Because <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a> are not guaranteed to be backwards compatible, a newer <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version</a> can process bytecode in unanticipated ways. If a <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> changes the EVM to fix a security problem, it is important to consider that change, and it is a good practice to follow that upgrade.

Because claims of conformance to this specification are only valid for specific <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>, a <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can mean an updated audit is needed to maintain valid <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for a current Ethereum network.

Network Upgrades typically only impact a few features. This helps limit the effort necessary to audit code after an upgrade: often there will be no changes that affect the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, or review of a small proportion that is the only part affected by a Network Upgrade will be sufficient to renew <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

## 4. EEA EthTrust Security Levels<a href="index.html#sec-levels" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is available at three Security Levels. The Security Levels describe minimum requirements for certifications at each Security Level: **\[S\]**, **\[M\]**, and **\[Q\]**. These Security Levels provide successively stronger assurance that a smart contract does not have specific security vulnerabilities.

- [Security Level \[S\]](index.html#sec-levels-one) is designed so that for most cases, where common features of Solidity are used following well-known patterns, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be certified by an automated "static analysis" tool.
- [Security Level \[M\]](index.html#sec-levels-two) mandates a stricter static analysis. It includes requirements where a human auditor is expected to determine whether use of a feature is necessary, or whether a claim about the security properties of code is justified.
- [Security Level \[Q\]](index.html#sec-levels-three) provides analysis of the business logic the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements, and that the code not only does not exhibit known security vulnerabilities, but also correctly implements what it claims to do.

The optional <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a>, correctly implemented, further enhance the Security of smart contracts. However it is not necessary to test them to conform to this specification.

Note

This scheme has been compared to the conformance approach used in the "OWASP Application Security Verification Standard" specification family \[<a href="index.html#bib-asvs" class="bibref" data-link-type="biblio" title="OWASP Application Security Verification Standard">ASVS</a>\]. There are some clear differences, largely resulting from the differences between the general applicability ASVS aims to achieve, and this specification's very precise focus on the security of Ethereum smart contracts written in Solidity.

The vulnerabilities addressed by this specification come from a number of sources, including Solidity Security Alerts \[<a href="index.html#bib-solidity-alerts" class="bibref" data-link-type="biblio" title="Solidity Blog - Security Alerts">solidity-alerts</a>\], the Smart Contract Weakness Classification \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], TMIO Best practices \[<a href="index.html#bib-tmio-bp" class="bibref" data-link-type="biblio" title="Best Practices for Smart Contracts (privately made available to EEA members)">tmio-bp</a>\], various sources of Security Advisory Notices, discussions in the Ethereum community and academics presenting newly discovered vulnerabilities, and the extensive practical experience of participants in the Working Group.

### 4.1 Security Level \[S\]<a href="index.html#sec-levels-one" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> is intended to allow an unguided automated tool to analyze most contracts' bytecode and source code, and determine whether they meet the requirements. For some situations that are difficut to verify automatically, usually only likely to arise in a small minority of contracts, there are higher-level <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> that can be fulfilled instead to meet a requirement for this Security Level.

To be eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for Security Level \[S\], <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* fulfil all <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements, **unless** it meets the applicable **<a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a>** for any <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement it does not meet.

**\[S\] Encode Hashes with `chainid` <a href="index.html#req-1-eip155-chainid" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* create hashes for transactions that incorporate `chainid` values following the recommendation described in \[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\].

\[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\] describes an enhanced hashing rule, incorporating a chain identifier in the hash. While this only provides a guarantee against replay attacks if there is a unique chain identifier, using the mechanism described provides a certain level of robustness and makes it much more difficult to execute a replay attack.

**\[S\] No `CREATE2` <a href="index.html#req-1-no-create2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

The `CREATE2` opcode provides the ability to interact with addresses that do not exist yet on-chain but could possibly eventually contain code. While this can be useful for deployments and counterfactual interactions with contracts, it can allow external calls to code that is not yet known, and could turn out to be malicous or insecure due to errors or weak protections.

**\[S\] No `tx.origin` <a href="index.html#req-1-no-tx.origin" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)

`tx.origin` is a global variable in Solidity which returns the address of the account that sent the transaction. A contract using `tx.origin` can allow an authorized account to call into a malicious contract, enabling the malicious contract to pass authorization checks in unintended cases. Use `msg.sender` for authorization instead of `tx.origin`.

See also [SWC-115](https://swcregistry.io/docs/SWC-115) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[S\] No Exact Balance Check <a href="index.html#req-1-exact-balance-check" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check).

Testing the balance of an account as a basis for some action has risks associated with unexpected receipt of ether or another token, including tokens deliberately transfered to cause such tests to fail as an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev), subsection <a href="index.html#sec-mev-considerations" class="sec-ref">§ 3.7 MEV (Maliciously Extracted Value)</a> of the Security Considerations for this specification, [SWC-132](https://swcregistry.io/docs/SWC-132) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and improper locking as described in \[<a href="index.html#bib-cwe-667" class="bibref" data-link-type="biblio" title="CWE-667: Improper Locking">CWE-667</a>\].

**\[S\] No Conflicting Names <a href="index.html#req-1-inheritance-conflict" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* include more than one variable, or operative function with different code, with the same name
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order).

In most programming languages, including Solidity, it is possible to use the same name for variables or functions that have different types or (for functions) input parameters. This can be hard to interpret in the source code, meaning reviewers misunderstand the code or are maliciously misled to do so, analogously to <a href="index.html#dfn-homoglyph-attacks" class="internalDFN" data-link-type="dfn">Homoglyph Attacks</a>.

This requirement means that unless the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> is met, any function or variable name will not be repeated, to eliminate confusion. It does however allow functions to be overridden, e.g. from a Base contract, so long as there is only one version of the function that operates within the code.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2020-2**](index.html#req-2-compiler-SOL-2020-2), and the [documentation of function inheritance](https://docs.soliditylang.org/en/latest/contracts.html#inheritance) in \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\].

**\[S\] No Hashing Consecutive Variable Length Arguments <a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

The elements of each variable-length argument to `abi.encodePacked()` are packed in order prior to hashing. <a href="index.html#dfn-hash-collisions" class="internalDFN" data-link-type="dfn">Hash Collisions</a> are possible by rearranging the elements between consecutive, variable length arguments while maintaining that their concatenated order is the same.

**\[S\] No `selfdestruct()` <a href="index.html#req-1-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, sending any Ether held by the contract, thus potentially stealing it. This feature can often break immutability and trustless guarantees to introduce numerous security issues. In addition, once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

`selfdestruct()` is officially deprecated, its usage discouraged, since Solidity compiler version 0.8.18 \[<a href="index.html#bib-solidity-release-818" class="bibref" data-link-type="biblio" title="Solidity 0.8.18 Release Announcement">solidity-release-818</a>\].

See also [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], \[<a href="index.html#bib-eip-6049" class="bibref" data-link-type="biblio" title="Deprecate SELFDESTRUCT">EIP-6049</a>\].

**\[S\] No `assembly {}` <a href="index.html#req-1-no-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly {}` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in \`assembly {}\`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/).

The `assembly {}` instruction allows lower-level code to be included. This give the authors much stronger control over the bytecode that is generated, which can be used for example to optimise gas usage. However, it also potentially exposes a number of vulnerabilites and bugs that are additional attack surfaces, and there are a number of ways to use `assembly {}` to introduce deliberately malicious code that is difficult to detect.

#### 4.1.1 Text and homoglyphs<a href="index.html#sec-1-unicode" class="self-link" aria-label="§"></a>

**\[S\] No Unicode Direction Control Characters <a href="index.html#req-1-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the Unicode Direction Control Characters `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

Changing the apparent order of characters through the use of invisible <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> can mask malicious code, even in viewing source code, to deceive human auditors.

More information on <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> is available in the W3C note [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls) \[<a href="index.html#bib-unicode-bdo" class="bibref" data-link-type="biblio" title="How to use Unicode controls for bidi text">unicode-bdo</a>\].

#### 4.1.2 External Calls<a href="index.html#sec-1-external-calls" class="self-link" aria-label="§"></a>

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[M\] Protect External Calls**](index.html#req-2-external-calls), and [**\[Q\] Verify External Calls**](index.html#req-3-external-calls).

**\[S\] Check External Calls Return <a href="index.html#req-1-check-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call()`, `delegatecall()`, `staticcall()`, and `send()`) *MUST* check the returned value from each usage to determine whether the call failed,
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return).

Normally, exceptions in calls cause a reversion. This will "bubble up", unless they are handled in a `try`/`catch`. However Solidity defines a set of Low-level Call Functions:

- `call()`,
- `delegatecall()`,
- `staticcall()`, and
- `send()`.

Calls using these functions behave differently. Instead of reverting on failure they return a boolean indicating whether the call completed successfully.

Not testing explicitly for the return value could lead to unexpected behavior in the caller contract. Assuming these calls reverting on failure *will* lead to unexpected behaviour when they are not successful.

See also [SWC-104](https://swcregistry.io/docs/SWC-104) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], error handling documentation in \[<a href="index.html#bib-error-handling" class="bibref" data-link-type="biblio" title="Control Structures - Solidity Documentation. Section &#39;Error handling: Assert, Require, Revert and Exceptions&#39;">error-handling</a>\], unchecked return value as described in \[<a href="index.html#bib-cwe-252" class="bibref" data-link-type="biblio" title="CWE-252: Unchecked Return Value">CWE-252</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return), and [**\[Q\] Verify External Calls**](index.html#req-3-external-calls).

**\[S\] Use Check-Effects-Interaction <a href="index.html#req-1-use-c-e-i" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The Checks-Effects-Interactions pattern ensures that validation of the request, and changes to the state variables of the contract, are performed before any interactions take place with other contracts. When contracts are implemented this way, the scope for <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> is reduced significantly.

As well as checking the particular contract effects, it is possible as part of this pattern to test protocol invariants, to provide a further assurance that a request doesn't produce an unsafe outcome.

See also <a href="index.html#sec-reentrancy-considerations" class="sec-ref">§ 3.4 External Interactions and Re-entrancy Attacks</a>, the explanation of "Checks-Effects-Interactions" \[<a href="index.html#bib-c-e-i" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation. Section &#39;Use the Checks-Effects-Interactions Pattern&#39;">c-e-i</a>\] in "Solidity Security Considerations" \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], "[Checks Effects Interactions](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\], and \[<a href="index.html#bib-freipi" class="bibref" data-link-type="biblio" title="You&#39;re writing require statements wrong">freipi</a>\].

**\[S\] No `delegatecall()` <a href="index.html#req-1-delegatecall" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[M\] Protect External Calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The `delegatecall()` instruction enables an external contract to manipulate the state of a contract that calls it, because the code is run with the caller's balance, storage, and address.

#### 4.1.3 Improved Compilers<a href="index.html#sec-1-compile-improvements" class="self-link" aria-label="§"></a>

Note

Implementing the Recommended Good Practice [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes the requirement in this subsection.

**\[S\] No Overflow/Underflow <a href="index.html#req-1-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

Like most programming languages, the EVM and Solidity represent numbers as a set of bytes that by default has a fixed length. This means arithmetic operations on large numbers can "overflow" the size by producing a result that does not fit in the space allocated. This results in corrupted data, and can be used as an attack on code. The \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\] registry of generic code vulnerabilities contains many overflow attacks; it is a well-known vector that is exposed in many systems and has regularly been exploited.

There are many ways to check for overflows, or underflows (where a negative number is large enough in magnitude to trigger the same effect). Since Solidity compiler version 0.8.0 there is built-in arithmetic overflow protection. <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> compiled with an earlier Solidity compiler version needs to check explicitly to mitigate this potential vulnerability.

See also [SWC-101](https://swcregistry.io/docs/SWC-101) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

#### 4.1.4 Compiler Bugs<a href="index.html#sec-1-compiler-bugs" class="self-link" aria-label="§"></a>

There are a number of known security bugs in different Solidity compiler versions. The requirements in this subsection ensure that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not trigger these bugs. The name of the requirement includes the `uid` first recorded for the bug in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\], as a key that can be used to find more information about the bug. \[<a href="index.html#bib-solidity-bugs" class="bibref" data-link-type="biblio" title="List of Known Bugs">solidity-bugs</a>\] describes the conventions used for the JSON-formatted list of bugs.

The requirements in this subsection are ordered according to the latest Solidity compiler versions that are vulnerable.

Note

Implementing the Recommended Good Practice [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes all requirements in this subsection.

Some compiler-related bugs are in the <a href="index.html#sec-level-2-compiler-bugs" class="sec-ref">§ 4.2.5 Security Level [M] Compiler Bugs and Overriding Requirements</a> as <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirements, either because they are <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for requirements in this subsection, or because they are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements that already ensure that the bug cannot be triggered.

Some bugs were introduced in known Solidity compiler versions, while others are known or assumed to have existed in all Solidity compiler versions until they were fixed.

**\[S\] Compiler Bug SOL-2023-3 <a href="index.html#req-1-compiler-SOL-2023-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that includes Yul code and uses the `verbatim` instruction twice, in each case surrounded by identical code, *MUST* disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).

From Solidity compiler version 0.8.5 until 0.8.22, the block deduplicator incorrectly processed `verbatim` items, meaning that sometimes it conflated two items based on the code surrounding them instead of comparing them properly.

See also the [8 November 2023 security alert](https://soliditylang.org/blog/2023/11/08/verbatim-invalid-deduplication-bug/).

**\[S\] Compiler Bug SOL-2022-6 <a href="index.html#req-1-compiler-SOL-2022-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a `struct`, `return` value, or a parameter list) that includes a dynamic component with the ABIEncoderV2, and whose last element is a `calldata` static array of base type `uint` or `bytes32`, *MUST NOT* use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).

From Solidity compiler version 0.5.8 until 0.8.15, ABI encoding a tuple whose final component is a `calldata` static array of base type `uint` or `bytes32` with the ABIEncoderV2 could result in corrupted data.

See also the [8 August 2022 security alert](https://blog.soliditylang.org/2022/08/08/calldata-tuple-reencoding-head-overflow-bug/).

**\[S\] Compiler Bug SOL-2022-5 with `.push()` <a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

Until Solidity compiler version 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using code through `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly).

**\[S\] Compiler Bug SOL-2022-3 <a href="index.html#req-1-compiler-SOL-2022-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

Solidity compiler versions from 0.6.9 until it was fixed in 0.8.13 had a bug that incorrectly allowed internal or public calls to use a simpification only valid for external calls, treating `memory` and `calldata` as equivalent pointers.

See also the 17 May 2022 [security alert](https://blog.soliditylang.org/2022/05/17/data-location-inheritance-bug/).

**\[S\] Compiler Bug SOL-2022-2 <a href="index.html#req-1-compiler-SOL-2022-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

Solidity compiler versions from 0.5.8 until it was fixed in 0.8.13 had a bug that meant a single-pass encoding and decoding of a nested array could read data beyond the `calldatasize()`.

See also the 17 May 2022 [security alert](https://blog.soliditylang.org/2022/05/17/calldata-reencode-size-check-bug/).

**\[S\] Compiler Bug SOL-2022-1 <a href="index.html#req-1-compiler-SOL-2022-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use Solidity compiler version 0.8.11 nor 0.8.12.

Solidity defines a set of types for variables known collectively as `bytesNN` or Fixed-length Variable types, that specify the length of the variable as a fixed number of bytes, following the pattern

- `bytes1`
- `bytes2`
- ...
- `bytes10`
- ...
- `bytes32`

Solidity compiler versions 0.8.11 and 0.8.12 had a bug that meant literal parameters were incorrectly encoded by `abi.encodeCall()` in certain circumstances.

See also the 16 March 2022 [security alert](https://blog.soliditylang.org/2022/03/16/encodecall-bug/).

**\[S\] Compiler Bug SOL-2021-4 <a href="index.html#req-1-compiler-sol-2021-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *MUST NOT* use Solidity compiler version 0.8.8.

Solidity compiler version 0.8.8 had a bug that assigned a full 32 bytes of storage to custom types that did not need it. This can be misused to enable reading arbitrary storage, as well as causing errors if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> contains code compiled using different Solidity compiler versions.

See also the 29 September 2021 [security alert](https://blog.soliditylang.org/2021/09/29/user-defined-value-types-bug/)

**\[S\] Compiler Bug SOL-2021-2 <a href="index.html#req-1-compiler-SOL-2021-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory` *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).

Solidity compiler version 0.4.16 introduced a bug, fixed in 0.8.4, that meant the ABIEncoderV2 incorrectly validated pointers when reading `memory` byte arrays, which could result in reading data beyond the array area due to an overflow error in calculating pointers.

See also the 21 April 2021 [security alert](https://blog.soliditylang.org/2021/04/21/decoding-from-memory-bug/).

**\[S\] Compiler Bug SOL-2021-1 <a href="index.html#req-1-compiler-SOL-2021-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the Optimizer with a Solidity compiler version older than 0.8.3.

Solidity compiler versions before 0.8.3 had an Optimizer bug that meant keccak hashes, calculated for the same content but different lengths that were not multiples of 32 bytes, incorrectly used the first value from cache instead of recalculating.

See also the 23 March 2021 [security alert](https://blog.soliditylang.org/2021/03/23/keccak-optimizer-bug/).

**\[S\] Compiler Bug SOL-2020-11-push <a href="index.html#req-1-compiler-SOL-2020-11-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array using `push()` *MUST NOT* use a Solidity compiler version older than 0.7.4.

Solidity compiler versions before 0.7.4 had a bug that meant data would be packed after an empty array, and if the length of the array is subsequently extended by `push()`, that data would be readable from the array.

See also the 19 October 2020 [security alert](https://blog.soliditylang.org/2020/10/19/empty-byte-array-copy-bug/).

**\[S\] Compiler Bug SOL-2020-10 <a href="index.html#req-1-compiler-SOL-2020-10" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an array of types shorter than 16 bytes to a longer array *MUST NOT* use a Solidity compiler version older than 0.7.3.

Solidity compiler versions before 0.7.3 had a bug that meant when array data for types shorter than 16 bytes are assigned to a longer array, the extra values in that longer array are not correctly reset to zero.

See also the 7 October 2020 [security alert](https://blog.soliditylang.org/2020/10/07/solidity-dynamic-array-cleanup-bug).

**\[S\] Compiler Bug SOL-2020-9 <a href="index.html#req-1-compiler-SOL-2020-9" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> *MUST NOT* use Solidity compiler version 0.7.1.

Solidity compiler version 0.7.1 introduced Free Functions \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\]: Functions that are defined in the source code of a smart contract but outside the scope of the formal contract declaration. <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> have `internal` visibility, and the compiler "inlines" them to the contracts that call them. The solidity documentation explains that they are:

> executed in the context of a contract. They still have access to the variable `this`, can call other contracts, send them Ether and destroy the contract that called them, among other things. The main difference to functions defined inside a contract is that free functions do not have direct access to storage variables and functions not in their scope.
>
> <https://docs.soliditylang.org/en/latest/contracts.html#functions>

Solidity compiler version 0.7.1 did not correctly distinguish overlapping <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Function</a> declarations, meaning that the wrong function could be called.

See examples of a [passing contract](https://entethalliance.github.io/eta-registry/examples/SOL-2020-9-fail.sol) and a [failing contract](https://entethalliance.github.io/eta-registry/examples/SOL-2020-9-fail.sol) for this requirement.

**\[S\] Compiler Bug SOL-2020-8 <a href="index.html#req-1-compiler-SOL-2020-8" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls internal library functions with `calldata` parameters called via `using for` *MUST NOT* use Solidity compiler version 0.6.9.

Solidity compiler version 0.6.9 incorrectly copied `calldata` parameters passed to internal library functions with `using for` as if they were calling to external library functions, leading to stack corruption and an incorrect jump destination.

See also a [Github issue with a code example](https://github.com/ethereum/solidity/issues/9172).

**\[S\] Compiler Bug SOL-2020-6 <a href="index.html#req-1-compiler-SOL-2020-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that accesses an array slice using an expression for the starting index that can evaluate to a value other than zero *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.6.0 and 0.6.7 (inclusive).

Solidity compiler version 0.6.0 introduced a bug fixed in 0.6.8 that incorrectly calculated index offsets for the start of array slices, used in dynamic `calldata` types, when using the ABIEncoderV2.

**\[S\] Compiler Bug SOL-2020-7 <a href="index.html#req-1-compiler-SOL-2020-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that passes a string literal containing two consecutive backslash ("\\) characters to an encoding function or an external call *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.5.14 and 0.6.7 (inclusive).

Solidity compiler version 0.5.14 introduced a bug fixed in 0.6.8 that incorrectly encoded consecutive backslash characters in string literals when passing them to an external function, or an encoding function, when using the ABIEncoderV2.

**\[S\] Compiler Bug SOL-2020-5 <a href="index.html#req-1-compiler-SOL-2020-5" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines a contract that does not include a constructor, but has a base contract that defines a constructor not defined as `payable` *MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive), **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor).

Solidity compiler version 0.4.5 introduced a check intended to result in contract creation reverting if value is passed to a constructor that is not explicitly marked as `payable`. If the constructor was inherited from a base instead of explicitly defined in the contract, this check did not function properly until Solidity compiler version 0.6.8, meaning the creation would not revert as expected.

**\[S\] Compiler Bug SOL-2020-4 <a href="index.html#req-1-compiler-SOL-2020-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes assignments to tuples tha

- have nested tuples, **or**
- include a pointer to an external function, **or**
- reference a dynamically sized `calldata` array

*MUST NOT* use a Solidity compiler version older than 0.6.5.

Solidity compiler version 0.1.6 introduced a bug, fixed in Solidity compiler version 0.6.5, that meant tuple assignments involving nested tuples, pointers to external functions, or references to dynamically sized `calldata` arrays, were corrupted due to incorrectly calculating the number of stack slots.

**\[S\] Compiler Bug SOL-2020-3 <a href="index.html#req-1-compiler-SOL-2020-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares arrays of size larger than 2^256-1 *MUST NOT* use a Solidity compiler version older than 0.6.5.

Solidity compiler version 0.2.0 introduced a bug, fixed in Solidity compiler version 0.6.5, that meant no overflow check was performed for the creation of very large arrays, meaning in some cases an overflow error would occur that would result in consuming all gas in a transaction due to the memory handling error introduced in compiling the contract.

**\[S\] Compiler Bug SOL-2020-1 <a href="index.html#req-1-compiler-SOL-2020-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares variables inside a `for` loop that contains a `break` or `continue` statement *MUST NOT* use the Yul Optimizer with Solidity compiler version 0.6.0 nor a Solidity compiler version between 0.5.8 and 0.5.15 (inclusive).

A bug in the Yul Optimiser in Solidity compiler versions from 0.5.8 to 0.5.15 and in Solidity compiler version 0.6.0 meant assignments for variables declared inside a `for` loop that contained a `break` or `continue` statement could be removed.

**\[S\] Use a Modern Compiler <a href="index.html#req-1-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

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

There are a number of known compiler bugs that affect Solidity Compiler Versions older than 0.6.0, but research into compiler bugs tends to focus on those that affect relatively modern Solidity Compiler versions, so any further bugs in older Solidity Compiler versions are only likely to be discovered and generally known as a result of being exploited.

It is a good practice to use a modern Solidity Compiler Version. In the rare cases where it is not possible to use a Solidity Compiler Version later than 0.6.0, it is possible to achieve <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> by conforming to the relevant <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> that were defined in version 1 of this specification \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060), covering Solidity Compiler bugs that require review for <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>.

**\[S\] No Ancient Compilers <a href="index.html#req-1-no-ancient-compilers" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.3.

Compiler bugs are not tracked for compiler Solidity compiler versions older than 0.3. There is therefore a risk that unknown bugs create unexpected problems.

See also "SOL-2016-1" in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\].

### 4.2 Security Level \[M\]<a href="index.html#sec-levels-two" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[M\] means that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> has been carefully reviewed by a human auditor or team, doing a manual analysis, and important security issues have been addressed to their satisfaction.

This level includes a number of <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for cases when <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement directly, because it uses an uncommon feature that introduces higher risk, or because in certain circumstsances testing that the requirement has been met requires human judgement. Passing the relevant <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> tests that the feature has been implemented sufficiently well to satisfy the auditor that it does not expose the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to the known vulnerabilities identified in this Security Level.

**\[M\] Pass Security Level \[S\] <a href="index.html#req-2-pass-l1" class="selflink">🔗</a>**
To be eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">§ 4.1 Security Level [S]</a>.

**\[M\] Explicitly Disambiguate Evaluation Order <a href="index.html#req-2-enforce-eval-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain statements where variable evaluation order can result in different outcomes

The evaluation order of functions is not entirely deterministic in Solidity, and is not guaranteed to be consistent across Solidity compiler versions. This means that the outcome of a statement calling multiple functions that each have side effects on shared stateful objects can lead to different outcomes if the order that the called functions were evaluated varies.

Also, the evaluation order in events and the instructions `addmod` and `modmul` generally does not follow the **usual** pattern, meaning that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using those instructions could produce unexpected outcomes.

Warning

<a href="index.html#example-9-variant-evaluation-order" class="self-link">Example 9</a>: variant evaluation order

If functions `g` and `h` change the state of any variable that the result of a function `f` depends on, a call such as `f(g(x), h(y))` cannot be guaranteed to return repeatable results.

A common approach to addressing this vulnerability is the use of temporary results, to ensure evaluation order will be the same.

<a href="index.html#example-10-using-temporary-values-to-enforce-evaluation-order" class="self-link">Example 10</a>: Using temporary values to enforce evaluation order

If functions `g` and `h` change the state of any variable that the result of a function `f` depends on, then it is important that the code **explicitly** determines the order of execution, for example using a temporary variable as in the following example:

``` solidity
  // SPDX-License-Identifier: MIT
  pragma solidity 0.8.18;

  uint256 public myNumber;
  uint256 public yourNumber;

  function firstTransform(uint256 someNumber) public returns uint256 {
    myNumber += 1; // side effec
    return someNumber.mul(myNumber);
  }

  function secondTransform(uint256 someNumber) public returns uint256 {
    yourNumber += 3; // side effec
    return someNumber.div(yourNumber);
  }

  function deterministicResult(uint256 someNumber) public returns uint256 {
    uint256 firstResult = firstTransform(someNumber);
    return secondTransform(firstResult);
  }

```

See also \[<a href="index.html#bib-richards2022" class="bibref" data-link-type="biblio" title="Solidity Underhanded Contest 2022. Submission 9 - Tynan Richards">richards2022</a>\], \[<a href="index.html#bib-solidity-cheatsheet" class="bibref" data-link-type="biblio" title="Solidity Documentation: Cheatsheet - Order Of Precedence Of Operators">solidity-cheatsheet</a>\], and the [19 July 2023 Solidity Compiler Security Bug notification](https://blog.soliditylang.org/2023/07/19/full-inliner-non-expression-split-argument-evaluation-order-bug/) for Solidity Compiler Security Bug 2023-2, noted in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\].

**\[M\] No Failing `assert()` Statements <a href="index.html#req-2-no-failing-asserts" class="selflink">🔗</a>**
`assert()` statements in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* fail.

`assert()` statements are meant for invariants, not as a generic error-handling mechanism. If an `assert()` statement fails because it is being used as a mechanism to catch errors, it is better to replace it with a `require()` statement or similar mechanism designed for the use case. If it fails due to a coding bug, that needs to be fixed.

This requirement is based on \[<a href="index.html#bib-cwe-670" class="bibref" data-link-type="biblio" title="CWE-670: Always-Incorrect Control Flow Implementation">CWE-670</a>\] Always-Incorrect Control Flow Implementation.

**\[M\] Verify Exact Balance Checks <a href="index.html#req-2-verify-exact-balance-check" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that checks whether the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable. *MUST* protect itself against transfers affecting the balance tested.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check).

If a Smart Contract checks that an account balance is some particular exact value at some point during its execution, it is potentially vulnerable to an attack, where a transfer to the account can be used to change the balance of the account causing unexpected results such as a transaction reverting. If such checks are used it is important that they are protected against this possibility.

#### 4.2.1 Text and homoglyph attacks<a href="index.html#sec-2-unicode" class="self-link" aria-label="§"></a>

The requirements in this section are related to the security advisory \[<a href="index.html#bib-cve-2021-42574" class="bibref" data-link-type="biblio" title="National Vulnerability Database CVE-2021-42574">CVE-2021-42574</a>\] and \[<a href="index.html#bib-cwe-94" class="bibref" data-link-type="biblio" title="CWE-94: Improper Control of Generation of Code (&#39;Code Injection&#39;)">CWE-94</a>\], "Improper Control of Generation of Code", also called "Code Injection".

**\[M\] No Unnecessary Unicode Controls <a href="index.html#req-2-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

<a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> permits the use of <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> in text strings, subject to analysis of whether they are necessary.

**\[M\] No Homoglyph-style Attack <a href="index.html#req-2-no-homoglyph-attack" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks, if the impact is misleading.

Techniques such as substituting characters from different alphabets (e.g. Latin "a" and Cyrillic "а" are not the same) can be used to mask malicious code, for example by presenting variables or function names designed to mislead auditors. These attacks are known as Homoglyph Attacks. Several approaches to successfully exploiting this issue are described in \[<a href="index.html#bib-ivanov" class="bibref" data-link-type="biblio" title="Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts">Ivanov</a>\].

In the rare case when there is a valid use of characters from multiple Unicode blocks (see \[<a href="index.html#bib-unicode-blocks" class="bibref" data-link-type="biblio" title="Blocks-14.0.0.txt">unicode-blocks</a>\]) in a variable name or label (most likely to be mixing two languages in a name), requirements at this level allow them to pass <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> so long as they do not mislead or confuse.

This level requires checking for homoglyph attacks including those within a single character set, such as the use of "í" in place of "i" or "ì", "ت" for "ث", or "1" for "l". When the reviewer judges that the result is misleading or confusing, the relevant code does not meet the <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirements.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a>: [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

#### 4.2.2 External Calls<a href="index.html#sec-2-external-calls" class="self-link" aria-label="§"></a>

**\[M\] Protect External Calls <a href="index.html#req-2-external-calls" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls:

- all addresses called by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* correspond to the exact code of the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> tested, **and**
- all contracts called *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, **and**
- all contracts called *MUST* be controlled by the same entity, **and**
- the protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

<a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> allows calling within a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">set of contracts</a> that form part of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. This ensures all contracts called are audited together at this Security Level.

If a contract calls a well-known external contract that is not audited as part of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, it is possible to certify conformance to this requirement through the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>, which allow the certifier to claim on their own judgement that the contracts called provide appropriate security. The extended requirements around documentation of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that apply when claiming conformance through implementation of the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> in this case reflect the potential for very high risk if the external contracts are simply assumed by a reviewer to be secure because they have been widely used.

Unless the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> deploys contracts, and retrieves their address accurately for calling, it is necessary to check that the contracts are really deployed at the addresses assumed in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

The same level of protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> has to be provided to the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> overall as for the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement.

**\[M\] Avoid Read-only Re-entrancy Attacks <a href="index.html#req-2-avoid-readonly-reentrancy" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.

As described in <a href="index.html#sec-reentrancy-considerations" class="sec-ref">§ 3.4 External Interactions and Re-entrancy Attacks</a>, code that reads information from a function can end up reading inconsistent or incorrect information. When the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> calls a function in which this possibility arises, the calling code needs an appropriate mechanism to avoid it happening.

One potential mechanism is for view functions to have a modifier that checks whether the data is currently in an inconsistent state, in the manner of a lock function. This enables calling code to explicitly avoid viewing inconsistent data.

Warning

<a href="index.html#example-11-insecure-approach-relaying-on-values-of-view-functions-that-can-be-reentered" class="self-link">Example 11</a>: INSECURE approach: relaying on values of view functions that can be reentered

This is a simple case of read-only-reentrancy attack.

The contract `Reentered` has a view function that determines a price based on `totalSupply` and `numberOfEther` in a specific LPToken, and a public non-Reentrant function that sells the LP token and sends the ETH received to the users that called it.

When the attack function is called in the `Attacker` contract it will reduce the value of `numberOfEther` in the `Reentered` contract, and trigger the `Attacker` contract's `receive()` function, **before** updating `totalSupply`, by preventing the instruction `LPToken.burnFrom(msg.sender, amount);` from executing.

The `receive()` function of the `Attacker` contract calls the `buyToken()` function of the `Reentered` contract under attack. Since the value of `numberOfEther` has been modified, but the `totalSupply` has not, the `buyToken()` function in the attacked contract will request the wrong number of tokens in exchange.

``` solidity
  // SPDX-License-Identifier: MIT
  pragma solidity 0.8.18;

  Contract Reentered{

function getPrice() public returns uint256 {
  return totalSupply / numberOfEther; //view function that calculates the price of the LP token
}

function sellLPToken(uint256 amount) public nonReentrant {
  [...]
  numberOfEther -= amountToReceive; //reduces the numberOfEth by the amount that will be sent to the user
  (bool success, ) = msg.sender.call{value: amountToReceive}(""); //transfers ETH when the LP token is sold
  require(success, "Transfer failed");
  LPToken.burnFrom(msg.sender, amount); //burns the LP token and changes the totalsupply by doing so
}

  }

  Contract Attacked{

function buyToken(uint256 amount) public{
  [...]
  uint256 tokenToReceive = Reentered.getPrice() * amount;
  [...]
}

  }

  Contract Attacker{

function attack() public{
  Reentered.sellLPToken(LPToken.balanceOf(address(this))); //starts the transaction to sell the LP tokens on the reentered contrac
} // this will trigger the Eth transfer that will activate the receive() function on this contrac

receive() external payable{
  Attacked.buyToken(1000);
}

  }

```

**\[M\] Handle External Call Returns <a href="index.html#req-2-handle-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Check External Calls Return**](index.html#req-1-check-return).

It is important that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> works as expected, to the satisfaction of the auditor, when the return value is the result of a possible error, such as if a call to a non-existent function triggers a fallback function instead of simply reverting, or an external call using a low-level function does not revert.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a>: [**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs).

#### 4.2.3 Documented Defensive Coding<a href="index.html#sec-2-special-code" class="self-link" aria-label="§"></a>

**\[M\] Document Special Code Use <a href="index.html#req-2-documented" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* document the need for each instance of:

- `CREATE2`,
- `assembly {}`,
- `selfdestruct()` or its deprecated alias `suicide()`,
- external calls,
- `delegatecall()`,
- code that can cause an overflow or underflow,
- `block.number` or `block.timestamp`, **or**
- Use of oracles and pseudo-randomness,

**and** *MUST* describe how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, **and** the documentation *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of

- [**\[S\] No `CREATE2`**](index.html#req-1-no-create2),
- [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct),
- [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly),
- [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i),
- [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow), and
- [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall).

There are legitimate uses for all of these coding patterns, but they are also potential causes of security vulnerabilities. <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> therefore requires testing that the use of these patterns is explained and justified, and that they are used in a manner that does not introduce known vulnerabilities.

The requirement to document the use of external calls applies to **all** external calls in the tested code, whether or not they meet the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related requirements</a>: [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), [**\[Q\] Verify External Calls**](index.html#req-3-external-calls), [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Ensure Proper Rounding of Computations Affecting Value <a href="index.html#req-2-check-rounding" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* identify and protect against exploiting rounding errors:

- The possible range of error introduced by such rounding *MUST* be documented.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* unintentionally create or lose value through rounding.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.

Smart Contracts typically implement mathematical formulas over real numbers using integer arithmetic. Such code can introduce rounding errors because integers and rational numbers whose size is bounded cannot precisely represent all real numbers in the same range.

If a procedure that uses rounding results in a predictable amount of error, that increases the value produced by the round-trip, it is possible to exploit that difference by repeating the procedure to cumulatively siphon a large sum.

Warning

<a href="index.html#example-12-insecure-approach-rounding-can-create-value" class="self-link">Example 12</a>: INSECURE approach: rounding can create value

A simple swap that rounds to the nearest usable number can mean that a round-trip effectively creates an off-by-one error, so swapping the right number of tokens back and forth will in each transaction produce more value than was started with:

``` solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

function xChangeTo(uint256 numberOfEth) public returns uint256 {
  return numberOfEth.mul(rateThatCausesRounding); //mul rounds to "nearest"
}

function xChangeFrom(uint256 numberOfOtherToken) public returns uint256 {
  return numberOfOtherToken.div(rateThatCausesRounding); //div rounds to "nearest"
}

```

To protect against this vulnerability, the "Keep the Change" approach ensures that any difference created does not provide an advantage to an attacker repeatedly calling a smart contract. It is important to note that differences do still accrue. A contract could use "over-servicing", repeatedly calling a swap protected by the "Keep the Change" approach, to steal from a user.

<a href="index.html#example-13-rounding-with-the-keep-the-change-approach" class="self-link">Example 13</a>: Rounding with the 'Keep the Change' approach

A simple approach to preventing an attacker from benefiting from rounding in a contract that implements a swap is to round so that the contract "keeps the change". There is then no advantage to an attacker in round tripping:

``` solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.18;

function xChangeTo(uint256 numberOfEth) public returns uint256 {
  return numberOfEth.mulDown(rateThatCausesRounding); //round the result down
}

function xChangeFrom(uint256 numberOfOtherToken) public returns uint256 {
  return numberOfOtherToken.divDown(rateThatCausesRounding); //round the result down
}

```

This vulnerability has been discovered in practice in DeFi protocol Smart Contracts that could have put hundreds of millions of dollars at risk. Further explanation is available in the [presentation slides](https://archive.devcon.org/resources/6/tackling-rounding-errors-with-precision-analysis.pdf) for the DevCon 2023 talk \[<a href="index.html#bib-devcon-rounding" class="bibref" data-link-type="biblio" title="Tackling Rounding Errors with Precision Analysis">DevCon-rounding</a>\]. An example of a thorough mathematical analysis of integer rounding for an automated market maker is available in \[<a href="index.html#bib-rounding-errors" class="bibref" data-link-type="biblio" title="Formal Specification of Constant Product (x × y = k) Market Maker Model and Implementation">rounding-errors</a>\].

This requirement is based on \[<a href="index.html#bib-cwe-1339" class="bibref" data-link-type="biblio" title="CWE-1339: Insufficient Precision or Accuracy of a Real Number">CWE-1339</a>\] Insufficient Precision or Accuracy of a Real Number.

**\[M\] Protect Self-destruction <a href="index.html#req-2-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, and potentially steal any Ether held by the contract. In addition, this can disrupt other users of the contract since once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

See also [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

This vulnerability led to the [Parity MultiSig Wallet Failure](https://www.parity.io/blog/parity-technologies-multi-sig-wallet-issue-update/) that blocked around 1/2 Million Ether on mainnet in 2017.

**\[M\] Avoid Common `assembly {}` Attack Vectors <a href="index.html#req-2-safe-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly {}` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

The `assembly {}` instruction provides a low-level method for developers to produce code in smart contracts. Using this approach provides great flexibility and control, for example to reduce gas cost. However it also exposes some possible attack surfaces where a malicious coder could introduce attacks that are hard to detect. This requirement ensures that two such attack surfaces that are well-known are not exposed.

See also [SWC-124](https://swcregistry.io/docs/SWC-124) and [SWC-127](https://swcregistry.io/docs/SWC-127) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Protect `CREATE2` Calls <a href="index.html#req-2-protect-create2" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses the `CREATE2` instruction, any contract to be deployed using `CREATE2`

- *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* use any `selfdestruct()`, `delegatecall()` nor `callcode()` instructions, **and**
- *MUST* be fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

The `CREATE2` opcode's ability to interact with addresses whose code does not yet exist on-chain makes it important to prevent external calls to malicous or insecure contract code that is not yet known.

The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> needs to include any code that can be deployed using `CREATE2`, to verify protections are in place and the code behaves as the contract author claims. This includes ensuring that opcodes that can change the immutability or forward calls in the contracts deployed with `CREATE2`, such as `selfdestruct()`, `delegatecall()` and `callcode()`, are not present.

If any of these opcodes are present, the additional protections and documentation required by the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> are necessary.

**\[M\] No Overflow/Underflow <a href="index.html#req-2-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow).

There are a few rare use cases where arithmetic overflow or underflow is intended, or expected behaviour. It is important such cases are protected appropriately. Note that these are harder to implement since Solidity compiler version 0.8.0 which introduced overflow protection that causes transactions to revert.

See also [SWC-101](https://swcregistry.io/docs/SWC-101) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[M\] Document Name Conflicts <a href="index.html#req-2-safe-inheritance-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* clearly document the order of inheritance for each function or variable that shares a name with another function or variable.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict).

As noted in [**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict). using the same name for different functions or variables can lead to reviewers misunderstanding code, either inadvertently or due to deliberately malicious code. Explicitly documenting any occurrences of doing this helps security audits, and makes it clear to others using the code where they need to pay close attention to the scope of variable or function declarations.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2020-2**](index.html#req-2-compiler-SOL-2020-2), and the [documentation of function inheritance](https://docs.soliditylang.org/en/latest/contracts.html#inheritance) in \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\]

**\[M\] Sources of Randomness <a href="index.html#req-2-random-enough" class="selflink">🔗</a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

This requirement involves careful evaluation for each specific contract and case. Some uses of randomness rely on no prediction being more accurate than any other. For such cases, values that can be guessed at with some accuracy or controlled by miners or validators, like block difficulty, timestamps, and/or block numbers, introduces a vulnerability. Thus a "strong" source of randomness like an oracle service is necessary.

Other uses are resistant to "good guesses" because using something that is close but wrong provides no more likelihood of gaining an advantage than any other guess.

Warning

<a href="index.html#example-14-randomness-vulnerable-to-approximate-guessing" class="self-link">Example 14</a>: Randomness vulnerable to approximate guessing

A competition to guess the block number of a chain at a specific time, that rewards the answer closest to the correct answer is using a source of "randomness" that is vulnerable to approximate guessing.

<a href="index.html#example-15-randomness-resistant-to-approximation" class="self-link">Example 15</a>: Randomness resistant to approximation

A lottery that will only pay if a number is submitted that exactly matches a winning entry in an off-chain lottery to be held in the future, offers no advantage in being able to approximate the answer.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[M\] Don't Misuse Block Data <a href="index.html#req-2-block-data-misuse" class="selflink">🔗</a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

Block numbers are vulnerable to approximate prediction, although they are generally not reliably precise indicators of elapsed time. `block.timestamp` is subject to manipulation by malicious actors. It is therefore important that these data are not trusted by <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to function as if they were highly reliable or random information.

The description of [SWC-116](https://swcregistry.io/docs/SWC-116) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] includes some code examples for techniques to avoid, for example using `block.number / 14` as a proxy for elapsed seconds, or relying on `block.timestamp` to indicate a precise time has passed.

For low precision, such as "a few minutes", `block.number / 14 > 1000` can be sufficient on main net, or a blockchain with a similar regular block period of around 14 seconds. But using it to determine that e.g. "exactly 36 seconds" have elapsed fails the requirement. A contract that relies on a specific block period can introduce serious risks if it is deployed on another blockchain with a very different block frequency.

Likewise, because block.timestamp depends on settings that can be manipulated by a malicious node operator, in cases likes Ethereum mainnet it is suitable for use as a coarse-grained approximation (on a scale of minutes) but the same code on a different blockchain can be vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks.

Note that this is related to the use of <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a>, which can also provide inaccurate information.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

#### 4.2.4 Signature Management<a href="index.html#sec-2-signature-requirements" class="self-link" aria-label="§"></a>

**\[M\] Proper Signature Verification <a href="index.html#req-2-signature-verification" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* properly verify signatures to ensure authenticity of messages that were signed off-chain.

Some smart contracts process messages that were signed off-chain to increase flexibility, while maintaining authenticity. Smart contracts performing their own signature verification need to verify such messages' authenticity.

Using `ecrecover()` for signature verification, it is important to validate the address returned against the expected outcome. In particular, a return value of `address(0)` represents a failure to provide a valid signature.

See also [SWC-122](https://swcregistry.io/docs/SWC-122) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

For code that does use `ecrecover()`, see the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060).

**\[M\] No Improper Usage of Signatures for Replay Attack Protection <a href="index.html#req-2-malleable-signatures-for-replay" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST* ensure that signatures cannot be reused:

- In the same function to verify the same message,
- In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>,
- In more than one contract address to verify the same message, in which the same account(s) may be signing messages, **and**
- In the same contract address across multiple chains.

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Intended Replay**](index.html#req-3-intended-replay). Additionally, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

In Replay Attacks, an attacker replays correctly signed messages to exploit a system. The signed message needs to include enough identifying information so that its intended setting is well-defined.

<a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a> allow an attacker to create a new signature for the same message. Smart contracts that check against hashes of signatures to ensure that a message has only been processed once could be vulnerable to replay attacks if malleable signatures are used.

#### 4.2.5 Security Level \[M\] Compiler Bugs and Overriding Requirements<a href="index.html#sec-level-2-compiler-bugs" class="self-link" aria-label="§"></a>

Some solidity compiler bugs described in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 4.1.4 Compiler Bugs</a> have <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, and some have trigger conditions that are not readily detectable in software.

Note

Implementing the Recommended Good Practice [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes all requirements in this subsection.

**\[M\] Solidity Compiler Bug 2023-1 <a href="index.html#req-2-compiler-SOL-2023-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses `.selector` *MUST* use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.

A bug introduced in Solidity compiler version 0.6.2 and fixed in Solidity compiler version 0.8.21 meant that when compound expressions accessed the `.selector` member, the expression would not be evaluated, unless the viaIR pipeline was used. Thus any side effects caused by the expression would not occur.

See also the [19 July 2023 security alert](https://blog.soliditylang.org/2023/07/19/missing-side-effects-on-selector-access-bug/).

**\[M\] Compiler Bug SOL-2022-7 <a href="index.html#req-2-compiler-SOL-2022-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing `return()` or `stop()` instructions *MUST NOT* use a Solidity compiler version between 0.8.13 and 0.8.17 inclusive.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

A bug fixed in Solidity compiler version 0.8.17 meant that storage writes followed by conditional early terminations from inline assembly functions would sometimes be erroneously dropped during optimization.

See also the [5 September 2022 security alert](https://blog.soliditylang.org/2022/09/08/storage-write-removal-before-conditional-termination/).

**\[M\] Compiler Bug SOL-2022-5 in `assembly {}` <a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an `assembly {}` instruction that reads that data without explicitly matching the length that was copied, *MUST NOT* use a Solidity compiler version older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Until Solidity compiler version 0.8.15 copying `memory` or `calldata` whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push), [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Compiler Bug SOL-2022-4 <a href="index.html#req-2-compiler-SOL-2022-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly {}` instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, and code in a another `assembly {}` instruction refers to that memory, *MUST NOT* use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Solidity compiler version 0.8.13 introduced a yulOptimizer bug, fixed in Solidity compiler version 0.8.15, where memory created in an `assembly {}` instruction but only read in a different `assembly {}` instruction was discarded.

See also the [17 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/inline-assembly-memory-side-effects-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Compiler Bug SOL-2021-3 <a href="index.html#req-2-compiler-SOL-2021-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly {}` instruction *MUST NOT* use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Solidity compiler version 0.6.8 introduced a bug, fixed in Solidity compiler version 0.8.9, that meant immutable signed integer types shorter than 256 bits could be read incorrectly in inline `assembly {}` instructions.

See also the [29 September 2021 security alert](https://blog.soliditylang.org/2021/09/29/signed-immutables-bug/), and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Safe Use of `assembly {}`**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), and [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4).

**\[M\] Compiler Bug Check Constructor Payment <a href="index.html#req-2-compiler-check-payable-constructor" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is

- defined in a base contract, **and**
- used by default in another contract without an explicit constructor, **and**
- not explicity marked `payable`,

*MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5).

Solidity compiler versions from 0.4.5 set the expectation that payments to a constructor that was not expicitly denoted as `payable` would revert. But when the constructor is inherited from a base contract, this reversion does not happen using Solidity compiler versions before 0.6.8.

**\[M\] Use a Modern Compiler <a href="index.html#req-2-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[M\] Compiler Bug SOL-2020-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2),
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly),
- [**\[M\] Compiler Bug Check Identity Calls**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls),
- [**\[M\] Validate `ecrecover()` input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input),
- [**\[M\] Compiler Bug No Zero Ether Send**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send), and
- [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060), covering Solidity Compiler bugs that require review for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>.

### 4.3 Security Level \[Q\]<a href="index.html#sec-levels-three" class="self-link" aria-label="§"></a>

In addition to automatable static testing verification (<a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>), and a manual audit (<a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>), <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[Q\] means checking that the intended functionality of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is sufficiently well documented that its functional correctness can be verified, that the code and documentation has been thoroughly reviewed by a human auditor or audit team to ensure that they are both internally coherent and consistent with each other, carefully enough to identify complex security vulnerabilities.

This level of review is especially relevant for tokens using ERC20 \[<a href="index.html#bib-erc20" class="bibref" data-link-type="biblio" title="EIP-20: Token Standard">ERC20</a>\], ERC721 \[<a href="index.html#bib-erc721" class="bibref" data-link-type="biblio" title="ERC 721: Non-fungible Token Standard">ERC721</a>\], and others; \[<a href="index.html#bib-token-standards" class="bibref" data-link-type="biblio" title="Ethereum Development Documentation - Token Standards">token-standards</a>\] identifies a number of other standards that can define tokens.

At this Security Level there are also checks to ensure the code does not contain errors that do not directly impact security, but do impact code quality. Code is often copied, so <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> requires code to be as well-written as possible. The risk being addressed is that it is easy, and not uncommon, to introduce weaknesses by copying existing code as a starting point.

**\[Q\] Pass Security Level \[M\] <a href="index.html#req-3-pass-l2" class="selflink">🔗</a>**
To be eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">§ 4.2 Security Level [M]</a>.

**\[Q\] Code Linting <a href="index.html#req-3-linted" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert()` statements, **and**
- *MUST NOT* contain a function that has the same name as the smart contract **unless** it is explicitly declared as a constructor using the `constructor` keyword, **and**
- *MUST* explicitly declare the visibility of all functions and variables.

Code is often copied from "good examples" as a starting point for development. Code that has achieved <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is meant to be high quality, so it is important to ensure that copying it does not encourage bad habits. It is also helpful for review to remove pointless code.

Code designed to trap unexpected errors, such as `assert()` instructions, is explicitly allowed, because it would be very unfortunate if defensively written code that successfully eliminates the possibility of triggering a particular error could not achieve <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

**\[Q\] Manage Gas Use Increases <a href="index.html#req-3-enough-gas" class="selflink">🔗</a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

Some structures such as arrays can grow, and the value of variables is (by design) variable. Iterating over a structure whose size is not clear in advance, whether an array that grows, a bound that changes, or something determined by an external value, can result in significant increases in gas usage.

What is reasonable growth to expect needs to be considered in the context of the business logic intended, and how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against <a href="index.html#dfn-gas-griefing" class="internalDFN" data-link-type="dfn">Gas Griefing</a> attacks, where malicious actors or errors result in values occurring beyond the expected reasonable range(s).

See also [SWC-126](https://swcregistry.io/docs/SWC-126), [SWC-128](https://swcregistry.io/docs/SWC-128) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> in <a href="index.html#sec-3-documentation" class="sec-ref">§ 4.3.1 Documentation requirements</a>.

**\[Q\] Protect Gas Usage <a href="index.html#req-3-protect-gas" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect against malicious actors stealing or wasting gas.

Smart contracts allowing "gasless" transactions enable users to submit transactions without having to supply their own gas. They need to be carefully implemented to prevent Denial of Service from <a href="index.html#dfn-gas-griefing" class="internalDFN" data-link-type="dfn">Gas Griefing</a> and <a href="index.html#dfn-gas-siphoning" class="internalDFN" data-link-type="dfn">Gas Siphoning</a> attacks.

See also [The Gas Siphon Attack: How it Happened and How to Protect Yourself](https://archive.devcon.org/archive/watch/5/the-gas-siphon-attack-how-it-happened-and-how-to-protect-yourself/) from the DevCon 2019 talk \[<a href="index.html#bib-devcon-siphoning" class="bibref" data-link-type="biblio" title="The Gas Siphon Attack: How it Happened and How to Protect Yourself">DevCon-siphoning</a>\].

**\[Q\] Protect against Oracle Failure <a href="index.html#req-3-check-oracles" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect itself against malfunctions in <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> it relies on.

Some <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are known to be vulnerable to manipulation, for example because they derive the information they provide from information vulnerable to <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>, or manipulation of prices through the use of flashloans to enable an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack, among other well-known attacks.

In addition, as networked software <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> can potentially suffer problems ranging from latency issues to outright failure, or being discontinued.

It is important to check the mechanism used by an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> to generate the information it provides, and the potential exposure of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that relies on that <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> to the effects of it failing, or of malicious actors manipulating its inputs or code to enable attacks.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[Q\] Protect against Front-running**](index.html#req-3-block-front-running), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[Q\] Protect against Front-Running <a href="index.html#req-3-block-front-running" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* require information in a form that can be used to enable a <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attack.

In <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attacks, an attacker places their transaction in front of a victim's. This can be done by a malicious miner or by an attacker monitoring the mempool, and preempting susceptible transactions by broadcasting their own transactions with higher transaction fees. Removing incentives to front-run generally means applying mitigations such as hash commitment schemes \[<a href="index.html#bib-hash-commit" class="bibref" data-link-type="biblio" title="Commitment scheme - WikiPedia">hash-commit</a>\] or batch execution.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Protect against Front-running**](index.html#req-3-block-front-running).

**\[Q\] Protect against MEV Attacks <a href="index.html#req-3-block-mev" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

<a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> refers to the potential that a block producer can maliciously reorder or suppress transactions, or another participant in a blockchain can propose a transaction or take other action to gain a benefit that was not intended to be available to them.

This requirement entails a careful judgement by the auditor, of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks, and what mitigation strategies are appropriate. Some approaches are discussed further in <a href="index.html#sec-mev-considerations" class="sec-ref">§ 3.7 MEV (Maliciously Extracted Value)</a>.

Many attack types need to be considered, including at least <a href="index.html#dfn-censorship-attacks" class="internalDFN" data-link-type="dfn">Censorship Attacks</a>, <a href="index.html#dfn-future-block-attacks" class="internalDFN" data-link-type="dfn">Future Block Attacks</a>, and <a href="index.html#dfn-timing-attacks" class="internalDFN" data-link-type="dfn">Timing Attacks</a> (<a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, <a href="index.html#dfn-back-running" class="internalDFN" data-link-type="dfn">Back-Running</a>, and <a href="index.html#dfn-sandwich-attacks" class="internalDFN" data-link-type="dfn">Sandwich Attacks</a>).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles), and [**\[Q\] Protect against Front-running**](index.html#req-3-block-front-running).

**\[Q\] Protect Against Governance Takeovers <a href="index.html#req-3-protect-governance" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system *MUST* protect against one external entity taking control via exploit of the governance design.

Governance attacks are specific to the system that is exploited. Depending on the governance proposal system, some areas of vulnerability may include:

- The issued governance token;
- The method of distribution for the governance token;
- The design of the acceptance and execution of governance proposals.

For example, if a staking contract is used to distribute governance tokens as a reward, it is important that the staking contract is not vulnerable to a Flash Loan Attack, where a large amount of tokens are borrowed in a very short-term flash loan, then staked atomically to gain a temporary majority of governance tokens, that are then used to make a governance decision, such as draining all the funds held to an attacker's wallet.

**\[Q\] Process All Inputs <a href="index.html#req-3-all-valid-inputs" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

Code that fails to validate inputs runs the risk of being subverted through maliciously crafted input that can trigger a bug, or behaviour the authors did not anticipate.

See also [SWC-123](https://swcregistry.io/docs/SWC-123) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] which notes that it is important to consider whether input requirements are too strict, as well as too lax, \[<a href="index.html#bib-cwe-573" class="bibref" data-link-type="biblio" title="CWE-573: Improper Following of Specification by Caller">CWE-573</a>\] Improper Following of Specification by Caller, and note that there are several <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> that are specific to particular Solidity compiler versions in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 4.1.4 Compiler Bugs</a>.

**\[Q\] State Changes Trigger Events <a href="index.html#req-3-event-on-state-change" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

Events are convenience interfaces that give an abstraction on top of the EVM's logging functionality. Applications can subscribe and listen to these events through the RPC interface of an Ethereum client. See more at \[<a href="index.html#bib-solidity-events" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Events">solidity-events</a>\].

Events are generally expected to be used for logging all state changes as they are not just useful for off-chain applications but also security monitoring and debugging. Logging all state changes in a contract ensures that any developers interacting with the contract are made aware of every state change as part of the ABI and can understand expected behavior through event annotations, as per [**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate).

**\[Q\] No Private Data <a href="index.html#req-3-no-private-data" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain.

This is a <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> requirement primarily because the question of what is private data often requires careful and thoughtful assessment and a reasoned understanding of context. In general, this is likely to include an assessment of how the data is gathered, and what the providers of data are told about the usage of the information.

Private Data is used in this specification to refer to information that is not intended to be generally available to the public. For example, an individual's home telephone number is generally private data, while a business' customer enquiries telephone number is generally not private data. Similarly, information identifying a person's account is normally private data, but there are circumstances where it is public data. In such cases, that public data can be recorded on-chain in conformance with this requirement.

Warning

PLEASE NOTE: In some cases regulation such as the \[<a href="index.html#bib-gdpr" class="bibref" data-link-type="biblio" title="Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016         on the protection of natural persons with regard to the processing of personal data         and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)         (Text with EEA relevance)">GDPR</a>\] imposes formal legal requirements on some private data. However, performing a test for this requirement results in an expert technical opinion on whether data that the auditor considers private is exposed. A statement about whether <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets this requirement does not represent any form of legal advice or opinion, attorney representation, or the like.

**\[Q\] Intended Replay <a href="index.html#req-3-intended-replay" class="selflink">🔗</a>**
If a signature within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance *MUST* be intended, documented, **and** safe for re-use.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay).

In some rare instances, it may be the intention of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to allow signatures to be replayed. For example, a signature may be used as permission to participate in a whitelist for a given period of time. In these exceptional cases, the replay must be included in documentation as a known allowance. Further, it must be verified that the reuse cannot be exploited.

#### 4.3.1 Documentation requirements<a href="index.html#sec-3-documentation" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> conformance requires a detailed description of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is **intended** to behave. Alongside detailed testing requirements to check that it does behave as described wth regard to specific known vulnerabililies, it is important that the claims made for it are accurate. This requirement helps ensure that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> fulfils claims made for it outside audit-specific documentation.

The combination of these requirements helps ensure there is no malicious code, such as malicious "back doors" or "time bombs" hidden in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Since there are legitimate use cases for code that behaves as e.g. a time bomb, or "phones home", this combination helps ensure that testing focuses on real problems.

The requirements in this section extend the coverage required to meet the <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirement [**\[M\] Document Special Code Use**](index.html#req-2-documented). As with that requirement, there are multiple requirements at this level that require the documentation mandated in this subsection.

**\[Q\] Document Contract Logic <a href="index.html#req-3-documented" class="selflink">🔗</a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

Contract Logic documented in a human-readable format and with enough detail that functional correctness and safety assumptions for special code use can be validated by auditors helps them assess complex code more efficiently and with higher confidence.

It is important to document how the logic protects against potential attacks such as Flash Loan attacks (especially on governance or price manipulation), MEV, and other complex attacks that take advantage of ecosystem features or tokenomics.

**\[Q\] Document System Architecture <a href="index.html#req-3-document-system" class="selflink">🔗</a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

System documentation provides auditor(s) information to understand security assumptions and ensure functional correctness. It is helpful if system documentation is included or referenced in the README file of the code repository, alongside documentation for how the source code can be tested, built and deployed.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Annotate Code with NatSpec**](https://entethalliance.org/specs/ethtrust-sl/v2/req-3-annotate).

**\[Q\] Annotate Code with NatSpec <a href="index.html#req-3-annotate" class="selflink">🔗</a>**
All <a href="index.html#dfn-public-interfaces" class="internalDFN" data-link-type="dfn">Public Interfaces</a> contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

Inline comments are important to ensure that developers and auditors understand the intent behind each function and other code components. Public Interfaces means anything that would be contained in the ABI of the compiled <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>. It is also recommended to use inline comments for private or internal functions that implement sensitive and/or complex logic.

Following the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format allows these inline comments to be understood by the Solidity compiler for extracting them into a machine-readable format that could be used by other third-party tools for security assessments and automatic documentation, including documentation shown to users by wallets that integrate with source code verification tools like [Sourcify](https://sourcify.dev). This could also be used to generate specifications that fully or partially satisfy the Requirement to [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

**\[Q\] Implement as Documented <a href="index.html#req-3-implement-as-documented" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

The requirements at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> to provide documentation are important. However, it is also crucial that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> actually behaves as documented. If it does not, it is possible that this reflects insufficient care and that the code is also vulnerable due to bugs that were missed in implementation. It is also possible that the difference is an attempt to hide malicious code in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

#### 4.3.2 Access Control<a href="index.html#sec-3-access-control" class="self-link" aria-label="§"></a>

**\[Q\] Enforce Least Privilege <a href="index.html#req-3-access-control" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that enables privileged access *MUST* implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct).

There are several common methods to implement access control, such as Role-Based Access Control \[<a href="index.html#bib-rbac" class="bibref" data-link-type="biblio" title="INCITS 359-2012: Information Technology - Role Based Access Control">RBAC</a>\] and \[<a href="index.html#bib-ownable" class="bibref" data-link-type="biblio" title="ERC-173: Contract Ownership Standard">Ownable</a>\], and bespoke access control is often implemented for a given use case. Using industry-standard methods can help simplify the process of auditing, but is not sufficient to determine that there are no risks arising either from errors in implementation or due to a maliciously-crafted contract.

It is important to consider access control at both the protocol operation and deployment levels. If a protocol is deployed in a deterministic manner, for example allowing a multi-chain deployment to have the same address across all chains, it is important to explicitly set an owner rather than defaulting to `msg.sender`, as that may leave a simple factory deployment contract as the insufficent new admin of your protocol.

It is particularly important that appropriate access control applies to payments, as noted in [SWC-105](https://swcregistry.io/docs/SWC-105), but other actions such as overwriting data as described in [SWC-124](https://swcregistry.io/docs/SWC-126), or changing specific access controls, also need to be appropriately protected \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\]. This requirement matches \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\] Improper Access Control.

See also "[Access Restriction](https://fravoll.github.io/solidity-patterns/access_restriction.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\].

**\[Q\] Use Revocable and Transferable Access Control Permissions <a href="index.html#req-3-revocable-permisions" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* implement a mechanism to revoke and transfer those permissions.

Privileged Accounts can perform administrative tasks on the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a>. If those accounts are compromised or responsibility to perform those tasks is assigned to different people, it is important to have a mechanism to revoke and transfer those permissions.

**\[Q\] No Single Admin EOA for Privileged Actions <a href="index.html#req-3-no-single-admin-eoa" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.

Privileged accounts can perform administrative tasks on the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a>. If a single EOA can perform these actions, and that permission cannot be revoked, the risks to a Smart Contract posed by a compromised or lost private key can be existential.

**\[Q\] Verify External Calls <a href="index.html#req-3-external-calls" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

At <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> auditors have a lot of flexibility to offer <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for different uses of External Calls.

This requirement effectively allows a reviewer to declare that the destination of an external call is not a security risk. It is important to note that any such declaration reflects very closely on the reputation of a reviewer.

It is inappropriate to assume that a smart contract is secure just because it is widely used, and it is unacceptable to assume that a smart contract provided by a user in the future will be secure - this is a known vector that has been used for many serious security breaches.

It is also important to consider how any code referenced and declared safe by the reviewer could be vulnerable to attacks based on its use of external calls.

To take a common example, swap contracts that allow a user to provide any pair of token contracts are potentially at risk if one of those contracts is malicious, or simply vulnerable, in a way the swap contract does not anticipate and protect against.

See also the related requirements [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and** [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

**\[Q\] Verify `tx.origin` Usage <a href="index.html#req-3-verify-tx.origin" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

`tx.origin` can be used to enable phishing attacks, tricking a user into interacting with a contract that gains access to all the funds in their account. It is generally the wrong choice for authorization of a caller for which `msg.sender` is the safer choice.

See also <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control), the [section "`tx.origin`"](https://docs.soliditylang.org/en/latest/security-considerations.html?highlight=tx.origin) in Solidity Security Considerations \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], and CWE 284: Improper Access Control \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\].

### 4.4 Recommended Good Practices<a href="index.html#sec-good-practice-recommendations" class="self-link" aria-label="§"></a>

This section describes good practices that require substantial human judgement to evaluate. Testing for, and meeting these requirements does not directly affect conformance to this document. Note however that meeting the Recommended Good Practice [**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible) will in practice mean that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets all the Requirements based on Compiler Bugs, including the majority of Requirements for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>.

**\[GP\] Check For and Address New Security Bugs <a href="index.html#req-R-check-new-bugs" class="selflink">🔗</a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 1 November 2023 and address them.

This version of the specification was finalized late in 2023. New vulnerabilities are discovered from time to time, on an unpredictable schedule. The latest solidity compiler bug accounted for in this version is SOL-2023-3.

Checking for security alerts published too late to be incorporated into the current version of this document is an important technique for maintaining the highest possible security.

There are other sources of information on new security vulnerabilities, from \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\] to following the blogs of many security-oriented organizations such as those that contributed to this specification.

**\[GP\] Meet as Many Requirements as Possible <a href="index.html#req-R-meet-all-possible" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

While meeting some requirements for a higher <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> Security Level makes no change to the formal conformance level of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, each requirement is specified because meeting it provides protection against specific known attacks. If it is possible to meet a particular requirement, even if it is not necessary for conformance at the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> being tested, meeting that requirement will improve the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and is therefore worth doing.

**\[GP\] Use Latest Compiler <a href="index.html#req-R-use-latest-compiler" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable Solidity compiler version.

The Solidity compiler is regularly updated to improve performance but also specifically to fix security vulnerabilities that are discovered. There are many requirements in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 4.1.4 Compiler Bugs</a> that are related to vulnerabilities known at the time this specification was written, as well as enhancements made to provide better security by default. In general, newer Solidity compiler versions improve security, so unless there is a specific known reason not to do so, using the latest Solidity compiler version available will result in better security.

**\[GP\] Write Clear, Legible Solidity Code <a href="index.html#req-R-clean-code" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

There are no strict rules defining how to write clear code. It is important to use sufficiently descriptive names, comment code appropriately, and use structures that are easy to understand without causing the code to become excessively large, because that also makes it difficult to read and understand.

Excessive nesting, unstructured comments, complex looping structures, and the use of very terse names for variables and functions are examples of coding styles that can also make code harder to understand.

It is important to note that in some cases, developers can sacrifice easy reading for other benefits such as reducing gas costs - this can be mitigated somewhat by comments in the code.

Likewise, for complex code involving multiple individual smart contracts, the way source is organised into files can help clarify or obscure what's happening. In particular, naming source code files to match the names of smart contracts they define is a common pattern that eases understanding.

This Good Practice extends somewhat the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Code Linting**](index.html#req-3-linted), but judgements about how to meet it are necessarily more subjective than in the specifics that requirement establishes. Those looking for additional guidance on code styling can refer to the \[<a href="index.html#bib-solidity-style-guide" class="bibref" data-link-type="biblio" title="Solidity Style Guide - Solidity Documentation">Solidity-Style-Guide</a>\].

**\[GP\] Follow Accepted ERC Standards <a href="index.html#req-R-follow-erc-standards" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case.

An ERC is a category of \[<a href="index.html#bib-eip" class="bibref" data-link-type="biblio" title="EIP-1: EIP Purpose and Guidelines">EIP</a>\] (Ethereum Improvement Proposal) that defines application-level standards and conventions, including smart contract standards such as token standards \[<a href="index.html#bib-erc20" class="bibref" data-link-type="biblio" title="EIP-20: Token Standard">ERC20</a>\] and name registries \[<a href="index.html#bib-erc137" class="bibref" data-link-type="biblio" title="ERC-137: Ethereum Domain Name Service - Specification">ERC137</a>\].

While following ERC standards will not inherently make Solidity code secure, they do enable developers to integrate with common interfaces and follow known conventions for expected behavior. If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does claim to follow a given ERC, its functional correctness in conforming to that standard can be verified by auditors.

**\[GP\] Define a Software License <a href="index.html#req-R-define-license" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license

A software license provides legal guidance on how contributors and users can interact with the code, including auditors and whitehats. Because bytecode deployed to public networks can be read by anyone, it is common practice to use an Open-Source license for the Solidity code used to generate it.

It is important to choose a \[<a href="index.html#bib-software-license" class="bibref" data-link-type="biblio" title="Choosing an Open Source License">software-license</a>\] that best addresses the needs of the project, and clearly link to it throughout the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and documentation, e.g. using a prominent LICENSE file in the code repository and referencing it from each source file.

**\[GP\] Disclose New Vulnerabilities Responsibly <a href="index.html#req-R-notify-news" class="selflink">🔗</a>**
Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.

New security vulnerabilities are discovered from time to time. It helps the efforts to revise this specification to ensure the Working Group is aware of new vulnerabilities, or new knowledge regarding existing known vulnerabilities.

The EEA has agreed to manage the specific email address <a href="https://entethalliance.org/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4c3f292f393e25383561222338252f293f0c2922382938242d2020252d222f2962233e2b">[email protected]</a> for such notifications.

**\[GP\] Use Fuzzing <a href="index.html#req-R-fuzzing-in-testing" class="selflink">🔗</a>**
<a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> *SHOULD* be used to probe <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for errors.

Fuzzing is an automated software testing method that repeatedly activates a contract, using a variety of invalid, malformed, or unexpected inputs, to reveal defects and potential security vulnerabilities.

Fuzzing can take days or even weeks: it is better to be patient than to stop it prematurely.

Fuzzing relies on a Corpus - A set of inputs for a fuzzing target. It is important to maintain the Corpus to maximise code coverage, and helpful to prune unnecessary or duplicate inputs for efficiency.

Many tools and input mutation methods can help to build the <a href="index.html#dfn-corpus" class="internalDFN" data-link-type="dfn">Corpus</a> for fuzzing. Good practice is to build on and leverage community resources where possible, always checking licensing restrictions.

Another important part of fuzzing is the set of specification rules that is checked throughout the fuzzing processes. While <a href="index.html#dfn-corpus" class="internalDFN" data-link-type="dfn">Corpus</a> is the set of inputs for fuzzing targets, the specification rules are business logic checks created specifically for fuzzing and are evaluated for each fuzzing input.

For a meaningful and efficient fuzzing campaign, it is not enough to send a large amount of random input to the contracts. This additional set of rules around the contracts should be present, so it gets triggered if fuzzing finds an edge case. The process shouldn't rely on the checks and reverts already within the contracts and the compiler.

<a href="index.html#example-16-fuzzing-specification-with-scribble" class="self-link">Example 16</a>: Fuzzing specification with Scribble

A simple example of a property written using [**Scribble**](https://docs.scribble.codes/tool/instrumented-code), a specification language that turns annotations in Solidity into concrete assertions. The annotation is the comment after "///". The property derived from that annotation that is being checked ensures that if the call to the contract `Foo` and function `add` succeeds, then the state variable `x` has to be equal to its value before the call - `old(x)` - added to the function parameter `y`. Essentially, fuzzing with this property would check whether or not the state's storage gets updated correctly.

``` solidity
      contract Foo {
        int x;
        /// #if_succeeds {:msg "test"} x == old(x) + y;
        function add(int y) public {
            require(y > 0);
            x += y;
        }
    }

```

As shown above, fuzzing rules and properties can be complex and may depend on specific contracts, functions, variables, their values before and/or after execution, and potentially many other things depending on the fuzzing technology and specification language of choice. If any vulnerabilities are discovered in the Solidity compiler by <a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> please [disclose them responsibly](index.html#sec-notifying-new-vulnerabilities).

**\[GP\] Use Formal Verification <a href="index.html#req-R-formal-verification" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* undergo formal verification.

Formal verification is a family of techniques that can mathematically prove functional correctness of smart contracts. It has been used in other applications such as embedded systems. There are many uses for formal verification in smart contracts, such as testing liveness, protocol invariants for safety at a high level, or proving narrower, more specific properties of a program's execution.

In formal verification, a formal (symbolic or mathematical) specification of the expected or desired outcome of a smart contract is created, enabling a formal mathematical proof of a protocol's correctness. The smart contract itself is often translated into a formal language for this purpose.

Several languages and programs exist for creating fromal verification proofs, some with the explicit aim of making formal verification more accessible to casual users and non-mathematicians. Please see \[<a href="index.html#bib-ef-sl" class="bibref" data-link-type="biblio" title="Specification languages for creating formal specifications">EF-SL</a>\] for some examples.

When implemented correctly by a practitioner with experience and skill, formal verification can make guarantees that fuzzing and testing cannot provide. However, that is often difficult to achieve in practice. Formal verification requires substantial manual labor and expertise.

A comprehensive formal verification most likely has a much a higher cost and complexity than unit or integration testing, fuzzing, or other methods. The immutable nature of many smart contracts, and the complexity of upgrading contracts when it is possible, makes formal verification appealing to administrators and stakeholders of protocols.

**\[GP\] Select an Appropriate Threshold for Multisig Wallets <a href="index.html#req-R-multisig-threshold" class="selflink">🔗</a>**
Multisignature requirements for privileged actions *SHOULD* have a sufficient number of signers, and NOT require "1 of N" nor all signatures.

Requiring multiple signatures for administrative actions has become the standard for many teams. When not managed carefully, they can become a source of attack even if the smart contract code is secure.

The problem with "1 of N" setups, that enable a single account to execute transactions, is that it is relatively easy to exploit. "N of N" setups meanwhile mean that if even one signer loses access to their account or will not approve an action, there is no possibility for approval. This can affect necessary operations such as the replacement of one signer with another, for example to ensure operational continuity, which can have a very serious impact.

Choosing a lower number of signatures to meet the requirement allows for quicker response, while a higher value requires stronger majority support. Consider using an "M of N" multisignature where M = (N/2) + 1, in other words, the smallest possible majority of signatures are necessary for approval, as a starting point. However it is important to consider how many potential signers there are, and the specific situations where signatures are needed, to determine a reasonably good value for M in a given case.

**\[GP\] Use TimeLock Delays for Sensitive Operations <a href="index.html#req-R-timelock-for-privileged-actions" class="selflink">🔗</a>**
Sensitive operations that affect all or a majority of users *SHOULD* use \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delays.

Sensitive operations, such as upgrades and \[<a href="index.html#bib-rbac" class="bibref" data-link-type="biblio" title="INCITS 359-2012: Information Technology - Role Based Access Control">RBAC</a>\] changes impact all or a majority of users in the protocol. A \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delay allows users to exit the system if they disagree with the proposed change, and allows developers to react if they detect a suspicious change.

## A. Additional Information<a href="index.html#sec-additional-information" class="self-link" aria-label="§"></a>

### A.1 Defined Terms<a href="index.html#sec-definitions" class="self-link" aria-label="§"></a>

The following is a list of terms defined in this Specification.

- <a href="index.html#dfn-back-running" id="dfnanchor-0">Back-Running</a>
- <a href="index.html#dfn-censorship-attacks" id="dfnanchor-2">Censorship Attacks</a>
- <a href="index.html#dfn-checks-effects-interactions" id="dfnanchor-3">Checks-Effects-Interactions</a>
- <a href="index.html#dfn-corpus" id="dfnanchor-4">Corpus</a>
- <a href="index.html#dfn-ethtrust-certified" id="dfnanchor-5">EEA EthTrust Certification</a>
- <a href="index.html#dfn-evm" id="dfnanchor-6">EVM</a>
- <a href="index.html#dfn-evm-version" id="dfnanchor-7">EVM versions</a>
- <a href="index.html#dfn-execution-contract" id="dfnanchor-8">Execution Contract</a>
- <a href="index.html#dfn-fixed-length-variable" id="dfnanchor-9">Fixed-length Variable</a>
- <a href="index.html#dfn-flash-loan-attack" id="dfnanchor-10">Flash Loan Attack</a>
- <a href="index.html#dfn-free-functions" id="dfnanchor-11">Free Functions</a>
- <a href="index.html#dfn-front-running" id="dfnanchor-12">Front-Running</a>
- <a href="index.html#dfn-future-block-attacks" id="dfnanchor-13">Future Block Attacks</a>
- <a href="index.html#dfn-fuzzing" id="dfnanchor-14">Fuzzing</a>
- <a href="index.html#dfn-gas-griefing" id="dfnanchor-15">Gas Griefing</a>
- <a href="index.html#dfn-gas-siphoning" id="dfnanchor-16">Gas Siphoning</a>
- <a href="index.html#dfn-gas-tokens" id="dfnanchor-17">Gas Tokens</a>
- <a href="index.html#dfn-hash-collisions" id="dfnanchor-18">Hash Collisions</a>
- <a href="index.html#dfn-homoglyph-attacks" id="dfnanchor-19">Homoglyph Attacks</a>
- <a href="index.html#dfn-logic-contract" id="dfnanchor-21">Logic Contract</a>
- <a href="index.html#dfn-low-level-call-functions" id="dfnanchor-22">Low-level Call Functions</a>
- <a href="index.html#dfn-malleable-signatures" id="dfnanchor-23">Malleable Signatures</a>
- <a href="index.html#dfn-metamorphic-upgrade" id="dfnanchor-24">Metamorphic Upgrade</a>
- <a href="index.html#dfn-mev" id="dfnanchor-26">MEV</a>
- <a href="index.html#dfn-hard-fork" id="dfnanchor-27">Network Upgrade</a>
- <a href="index.html#dfn-oracles" id="dfnanchor-28">Oracles</a>
- <a href="index.html#dfn-overriding-requirement" id="dfnanchor-29">Overriding Requirements</a>
- <a href="index.html#dfn-private-data" id="dfnanchor-30">Private Data</a>
- <a href="index.html#dfn-privileged-accounts" id="dfnanchor-31">Privileged Accounts</a>
- <a href="index.html#dfn-proxy-contract" id="dfnanchor-32">Proxy Contract</a>
- <a href="index.html#dfn-public-interfaces" id="dfnanchor-33">Public Interfaces</a>
- <a href="index.html#dfn-re-entrancy-attacks" id="dfnanchor-34">Re-entrancy Attacks</a>
- <a href="index.html#dfn-read-only-re-entrancy-attack" id="dfnanchor-35">Read-only Re-entrancy Attack</a>
- <a href="index.html#dfn-related-requirements" id="dfnanchor-36">Related Requirements</a>
- <a href="index.html#dfn-sandwich-attacks" id="dfnanchor-37">Sandwich Attacks</a>
- <a href="index.html#dfn-security-level-m" id="dfnanchor-38">Security Level [M]</a>
- <a href="index.html#dfn-security-level-q" id="dfnanchor-39">Security Level [Q]</a>
- <a href="index.html#dfn-security-level-s" id="dfnanchor-40">Security Level [S]</a>
- <a href="index.html#dfn-security-levels" id="dfnanchor-41">Security Levels</a>
- <a href="index.html#dfn-set-of-contracts" id="dfnanchor-42">Set Of Contracts</a>
- <a href="index.html#dfn-sets-of-overriding-requirements" id="dfnanchor-43">Set of Overriding Requirements</a>
- <a href="index.html#dfn-tested-code" id="dfnanchor-44">Tested Code</a>
- <a href="index.html#dfn-timing-attacks" id="dfnanchor-45">Timing Attacks</a>
- <a href="index.html#dfn-twap" id="dfnanchor-46">TWAP</a>
- <a href="index.html#dfn-unicode-direction-control-characters" id="dfnanchor-47">Unicode Direction Control Characters</a>
- <a href="index.html#dfn-upgradable-contract" id="dfnanchor-48">Upgradable Contract</a>
- <a href="index.html#dfn-valid-conformance-claim" id="dfnanchor-49">Valid Conformance Claim</a>

### A.2 Summary of Requirements<a href="index.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

This section provides a summary of all requirements and recommended good practices in this Specification.

[**\[S\] Encode Hashes with `chainid`**](index.html#req-1-eip155-chainid) **<a href="index.html#req-1-eip155-chainid" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* create hashes for transactions that incorporate `chainid` values following the recommendation described in \[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\].

[**\[S\] No `CREATE2`**](index.html#req-1-no-create2) **<a href="index.html#req-1-no-create2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction,
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin) **<a href="index.html#req-1-no-tx.origin" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)

[**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check) **<a href="index.html#req-1-exact-balance-check" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check).

[**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict) **<a href="index.html#req-1-inheritance-conflict" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* include more than one variable, or operative function with different code, with the same name
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order).

[**\[S\] No Hashing Consecutive Variable Length Arguments**](index.html#req-1-no-hashing-consecutive-variable-length-args) **<a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

[**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct) **<a href="index.html#req-1-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] No `assembly {}`**](index.html#req-1-no-assembly) **<a href="index.html#req-1-no-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly {}` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in \`assembly {}\`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/)..

[**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo) **<a href="index.html#req-1-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the [Unicode Direction Control Characters](index.html#dfn-unicode-direction-control-characters) `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

[**\[S\] Check External Calls Return**](index.html#req-1-check-return) **<a href="index.html#req-1-check-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call()`, `delegatecall()`, `staticcall()`, `send()`, and `transfer()`) *MUST* check the returned value from each usage to determine whether the call failed,
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return).

[**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i) **<a href="index.html#req-1-use-c-e-i" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall) **<a href="index.html#req-1-delegatecall" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[M\] Protect External Calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow) **<a href="index.html#req-1-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] Compiler Bug SOL-2023-3**](index.html#req-1-compiler-SOL-2023-3) **<a href="index.html#req-1-compiler-SOL-2023-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that includes Yul code and uses the `verbatim` instruction twice, in each case surrounded identical code, *MUST* disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).

[**\[S\] Compiler Bug SOL-2022-6**](index.html#req-1-compiler-SOL-2022-6) **<a href="index.html#req-1-compiler-SOL-2022-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a `struct`, `return` value, or a parameter list) that includes a dynamic component with the ABIEncoderV2, and whose last element is a `calldata` static array of base type `uint` or `bytes32`, *MUST NOT* use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).

[**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push) **<a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a Solidity compiler version older than 0.8.15.

[**\[S\] Compiler Bug SOL-2022-3**](index.html#req-1-compiler-SOL-2022-3) **<a href="index.html#req-1-compiler-SOL-2022-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

[**\[S\] Compiler Bug SOL-2022-2**](index.html#req-1-compiler-SOL-2022-2) **<a href="index.html#req-1-compiler-SOL-2022-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.13 (inclusive).

[**\[S\] Compiler Bug SOL-2022-1**](index.html#req-1-compiler-SOL-2022-1) **<a href="index.html#req-1-compiler-SOL-2022-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use Solidity compiler version 0.8.11 nor 0.8.12.

[**\[S\] Compiler Bug SOL-2021-4**](index.html#req-1-compiler-sol-2021-4) **<a href="index.html#req-1-compiler-sol-2021-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *MUST NOT* use Solidity compiler version 0.8.8.

[**\[S\] Compiler Bug SOL-2021-2**](index.html#req-1-compiler-SOL-2021-2) **<a href="index.html#req-1-compiler-SOL-2021-2" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory` *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).

[**\[S\] Compiler Bug SOL-2021-1**](index.html#req-1-compiler-SOL-2021-1) **<a href="index.html#req-1-compiler-SOL-2021-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the Optimizer with a Solidity compiler version older than 0.8.3.

[**\[S\] Compiler Bug SOL-2020-11-push**](index.html#req-1-compiler-SOL-2020-11-push) **<a href="index.html#req-1-compiler-SOL-2020-11-push" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array using `push()` *MUST NOT* use a Solidity compiler version older than 0.7.4.

[**\[S\] Compiler Bug SOL-2020-10**](index.html#req-1-compiler-SOL-2020-10) **<a href="index.html#req-1-compiler-SOL-2020-10" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an array of types shorter than 16 bytes to a longer array *MUST NOT* use a Solidity compiler version older than 0.7.3.

[**\[S\] Compiler Bug SOL-2020-9**](index.html#req-1-compiler-SOL-2020-9) **<a href="index.html#req-1-compiler-SOL-2020-9" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> *MUST NOT* use Solidity compiler version 0.7.1.

[**\[S\] Compiler Bug SOL-2020-8**](index.html#req-1-compiler-SOL-2020-8) **<a href="index.html#req-1-compiler-SOL-2020-8" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls internal library functions with `calldata` parameters called via `using for` *MUST NOT* use Solidity compiler version 0.6.9.

[**\[S\] Compiler Bug SOL-2020-6**](index.html#req-1-compiler-SOL-2020-6) **<a href="index.html#req-1-compiler-SOL-2020-6" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that accesses an array slice using an expression for the starting index that can evaluate to a value other than zero *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.6.0 and 0.6.7 (inclusive).

[**\[S\] Compiler Bug SOL-2020-7**](index.html#req-1-compiler-SOL-2020-7) **<a href="index.html#req-1-compiler-SOL-2020-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that passes a string literal containing two consecutive backslash ("\\) characters to an encoding function or an external call *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.5.14 and 0.6.7 (inclusive).

[**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5) **<a href="index.html#req-1-compiler-SOL-2020-5" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines a contract that does not include a constructor, but has a base contract that defines a constructor not defined as `payable` *MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive), **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor).

[**\[S\] Compiler Bug SOL-2020-4**](index.html#req-1-compiler-SOL-2020-4) **<a href="index.html#req-1-compiler-SOL-2020-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes assignments to tuples tha

- have nested tuples, **or**
- include a pointer to an external function, **or**
- reference a dynamically sized `calldata` array

*MUST NOT* use a Solidity compiler version older than 0.6.4.

[**\[S\] Compiler Bug SOL-2020-3**](index.html#req-1-compiler-SOL-2020-3) **<a href="index.html#req-1-compiler-SOL-2020-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares arrays of size larger than 2^256-1 *MUST NOT* use a Solidity compiler version older than 0.6.5.

[**\[S\] Compiler Bug SOL-2020-1**](index.html#req-1-compiler-SOL-2020-1) **<a href="index.html#req-1-compiler-SOL-2020-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares variables inside a `for` loop that contains a `break` or `continue` statement *MUST NOT* use the Yul Optimizer with Solidity compiler version 0.6.0 nor a Solidity compiler version between 0.5.8 and 0.5.15 (inclusive).

[**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060) **<a href="index.html#req-1-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

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

[**\[S\] No Ancient Compilers**](index.html#req-1-no-ancient-compilers) **<a href="index.html#req-1-no-ancient-compilers" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.3.

[**\[M\] Pass Security Level \[S\]**](index.html#req-2-pass-l1) **<a href="index.html#req-2-pass-l1" class="selflink">🔗</a>**
To be eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">§ 4.1 Security Level [S]</a>.

[**\[M\] Explicitly Disambiguate Evaluation Order**](index.html#req-2-enforce-eval-order) **<a href="index.html#req-2-enforce-eval-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain statements where variable evaluation order can result in different outcomes

[**\[M\] No Failing `assert()` Statements**](index.html#req-2-no-failing-asserts) **<a href="index.html#req-2-no-failing-asserts" class="selflink">🔗</a>**
`assert()` statements in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* fail.

[**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check) **<a href="index.html#req-2-verify-exact-balance-check" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that checks whether the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable. *MUST* protect itself against transfers affecting the balance tested.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check).

[**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo) **<a href="index.html#req-2-unicode-bdo" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

[**\[M\] No Homoglyph-style Attack**](index.html#req-2-no-homoglyph-attack) **<a href="index.html#req-2-no-homoglyph-attack" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks, if the impact is misleading.

[**\[M\] Protect External Calls**](index.html#req-2-external-calls) **<a href="index.html#req-2-external-calls" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls:

- all addresses called by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* correspond to the exact code of the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> tested, **and**
- all contracts called *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, **and**
- all contracts called *MUST* be controlled by the same entity, **and**
- the protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

[**\[M\] Avoid Read-only Re-entrancy Attacks**](index.html#req-2-avoid-readonly-reentrancy) **<a href="index.html#req-2-avoid-readonly-reentrancy" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.

[**\[M\] Handle External Call Returns**](index.html#req-2-handle-return) **<a href="index.html#req-2-handle-return" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Check External Calls Return**](index.html#req-1-check-return).

[**\[M\] Document Special Code Use**](index.html#req-2-documented) **<a href="index.html#req-2-documented" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* document the need for each instance of:

- `CREATE2`,
- `assembly {}`,
- `selfdestruct()` or its deprecated alias `suicide()`,
- external calls,
- `delegatecall()`,
- code that can cause an overflow or underflow,
- `block.number` or `block.timestamp`, **or**
- Use of oracles and pseudo-randomness,

**and** *MUST* describe how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, **and** the documentation *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of

- [**\[S\] No `CREATE2`**](index.html#req-1-no-create2),
- [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct),
- [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly),
- [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i),
- [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow), and
- [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall).

[**\[M\] Ensure Proper Rounding of Computations Affecting Value**](index.html#req-2-check-rounding) **<a href="index.html#req-2-check-rounding" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* identify and protect against exploiting rounding errors:

- The possible range of error introduced by such rounding *MUST* be documented.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* unintentionally create or lose value through rounding.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.

[**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct) **<a href="index.html#req-2-self-destruct" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct).

[**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly) **<a href="index.html#req-2-safe-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly {}` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2) **<a href="index.html#req-2-protect-create2" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses the `CREATE2` instruction, any contract to be deployed using `CREATE2`

- *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* use any `selfdestruct()`, `delegatecall()` nor `callcode()` instructions, **and**
- *MUST* be fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

[**\[M\] No Overflow/Underflow**](index.html#req-2-overflow-underflow) **<a href="index.html#req-2-overflow-underflow" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow).

[**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order) **<a href="index.html#req-2-safe-inheritance-order" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* clearly document the order of inheritance for each function or variable that shares a name with another function or variable.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict).

[**\[M\] Sources of Randomness**](index.html#req-2-random-enough) **<a href="index.html#req-2-random-enough" class="selflink">🔗</a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

[**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse) **<a href="index.html#req-2-block-data-misuse" class="selflink">🔗</a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

[**\[M\] Proper Signature Verification**](index.html#req-2-signature-verification) **<a href="index.html#req-2-signature-verification" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* use proper signature verification to ensure authenticity of messages that were signed off-chain, e.g. by using `ecrecover()`.

[**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay) **<a href="index.html#req-2-malleable-signatures-for-replay" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST* ensure that signatures cannot be reused:

- In the same function to verify the same message,
- In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>,
- In more than one contract address to verify the same message, in which the same account(s) may be signing messages, **and**
- In the same contract address across multiple chains.

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Intended Replay**](index.html#req-3-intended-replay). Additionally, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

[**\[M\] Solidity Compiler Bug 2023-1**](index.html#req-2-compiler-SOL-2023-1) **<a href="index.html#req-2-compiler-SOL-2023-1" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses `.selector` *MUST* use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.

[**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7) **<a href="index.html#req-2-compiler-SOL-2022-7" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing `return()` or `stop()` instructions *MUST NOT* use a Solidity compiler version between 0.8.13 and 0.8.17 inclusive.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly) **<a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an `assembly {}` instruction that reads that data without explicitly matching the length that was copied, *MUST NOT* use a Solidity compiler version older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4) **<a href="index.html#req-2-compiler-SOL-2022-4" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly {}` instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, and code in a another `assembly {}` instruction refers to that memory, *MUST NOT* use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3) **<a href="index.html#req-2-compiler-SOL-2021-3" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly {}` instruction *MUST NOT* use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor) **<a href="index.html#req-2-compiler-check-payable-constructor" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is

- defined in a base contract, **and**
- used by default in another contract without an explicit constructor, **and**
- not explicity marked `payable`,

*MUST NOT* use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5).

[**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060) **<a href="index.html#req-2-compiler-060" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[M\] Compiler Bug SOL-2020-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2),
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly),
- [**\[M\] Compiler Bug Check Identity Calls**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls),
- [**\[M\] Validate `ecrecover()` input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input),
- [**\[M\] Compiler Bug No Zero Ether Send**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send), and
- [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage).

[**\[Q\] Pass Security Level \[M\]**](index.html#req-3-pass-l2) **<a href="index.html#req-3-pass-l2" class="selflink">🔗</a>**
To be eligible for <a href="index.html#dfn-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">§ 4.2 Security Level [M]</a>.

[**\[Q\] Code Linting**](index.html#req-3-linted) **<a href="index.html#req-3-linted" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert()` statements, **and**
- *MUST NOT* contain a function that has the same name as the smart contract **unless** it is explicitly declared as a constructor using the `constructor` keyword, **and**
- *MUST* explicitly declare the visibility of all functions and variables.

[**\[Q\] Manage Gas Use Increases**](index.html#req-3-enough-gas) **<a href="index.html#req-3-enough-gas" class="selflink">🔗</a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

[**\[Q\] Protect Gas Usage**](index.html#req-3-protect-gas) **<a href="index.html#req-3-protect-gas" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect against malicious actors stealing or wasting gas.

[**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles) **<a href="index.html#req-3-check-oracles" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect itself against malfunctions in <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> it relies on.

[**\[Q\] Protect against Front-Running**](index.html#req-3-block-front-running) **<a href="index.html#req-3-block-front-running" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* require information in a form that can be used to enable a <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attack.

[**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev) **<a href="index.html#req-3-block-mev" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

[**\[Q\] Protect Against Governance Takeovers**](index.html#req-3-protect-governance) **<a href="index.html#req-3-protect-governance" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system *MUST* protect against one external entity taking control via exploit of the governance design.

[**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs) **<a href="index.html#req-3-all-valid-inputs" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

[**\[Q\] State Changes Trigger Events**](index.html#req-3-event-on-state-change) **<a href="index.html#req-3-event-on-state-change" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

[**\[Q\] No Private Data**](index.html#req-3-no-private-data) **<a href="index.html#req-3-no-private-data" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain.

[**\[Q\] Intended Replay**](index.html#req-3-intended-replay) **<a href="index.html#req-3-intended-replay" class="selflink">🔗</a>**
If a signature within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance *MUST* be intended, documented, **and** safe for re-use.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay).

[**\[Q\] Document Contract Logic**](index.html#req-3-documented) **<a href="index.html#req-3-documented" class="selflink">🔗</a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

[**\[Q\] Document System Architecture**](index.html#req-3-document-system) **<a href="index.html#req-3-document-system" class="selflink">🔗</a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

[**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate) **<a href="index.html#req-3-annotate" class="selflink">🔗</a>**
All <a href="index.html#dfn-public-interfaces" class="internalDFN" data-link-type="dfn">Public Interfaces</a> contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

[**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented) **<a href="index.html#req-3-implement-as-documented" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

[**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control) **<a href="index.html#req-3-access-control" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that enables privileged access *MUST* implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct).

[**\[Q\] Use Revocable and Transferable Access Control Permissions**](index.html#req-3-revocable-permisions) **<a href="index.html#req-3-revocable-permisions" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* implement a mechanism to revoke and transfer those permissions.

[**\[Q\] No Single Admin EOA for Privileged Actions**](index.html#req-3-no-single-admin-eoa) **<a href="index.html#req-3-no-single-admin-eoa" class="selflink">🔗</a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.

[**\[Q\] Verify External Calls**](index.html#req-3-external-calls) **<a href="index.html#req-3-external-calls" class="selflink">🔗</a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin) **<a href="index.html#req-3-verify-tx.origin" class="selflink">🔗</a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

[**\[GP\] Check For and Address New Security Bugs**](index.html#req-R-check-new-bugs) **<a href="index.html#req-R-check-new-bugs" class="selflink">🔗</a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 1 November 2023 and address them.

[**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible) **<a href="index.html#req-R-meet-all-possible" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

[**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) **<a href="index.html#req-R-use-latest-compiler" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable Solidity compiler version.

[**\[GP\] Write Clear, Legible Solidity Code**](index.html#req-R-clean-code) **<a href="index.html#req-R-clean-code" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

[**\[GP\] Follow Accepted ERC Standards**](index.html#req-R-follow-erc-standards) **<a href="index.html#req-R-follow-erc-standards" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case.

[**\[GP\] Define a Software License**](index.html#req-R-define-license) **<a href="index.html#req-R-define-license" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license

[**\[GP\] Disclose New Vulnerabilities Responsibly**](index.html#req-R-notify-news) **<a href="index.html#req-R-notify-news" class="selflink">🔗</a>**
Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.

[**\[GP\] Use Fuzzing**](index.html#req-R-fuzzing-in-testing) **<a href="index.html#req-R-fuzzing-in-testing" class="selflink">🔗</a>**
<a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> *SHOULD* be used to probe <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for errors.

[**\[GP\] Use Formal Verification**](index.html#req-R-formal-verification) **<a href="index.html#req-R-formal-verification" class="selflink">🔗</a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* undergo formal verification.

[**\[GP\] Select an Appropriate Threshold for Multisig Wallets**](index.html#req-R-multisig-threshold) **<a href="index.html#req-R-multisig-threshold" class="selflink">🔗</a>**
Multisignature requirements for privileged actions *SHOULD* have a sufficient number of signers, and NOT require "1 of N" nor all signatures.

[**\[GP\] Use TimeLock Delays for Sensitive Operations**](index.html#req-R-timelock-for-privileged-actions) **<a href="index.html#req-R-timelock-for-privileged-actions" class="selflink">🔗</a>**
Sensitive operations that affect all or a majority of users *SHOULD* use \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delays.

### A.3 Acknowledgments<a href="index.html#sec-acknowledgments" class="self-link" aria-label="§"></a>

The EEA acknowledges and thanks the many people who contributed to the development of this version of the specification. Please advise us of any errors or omissions.

We are grateful to the entire community who develops Ethereum, for their work and their ongoing collaboration.

In particular we would like to thank the contributors to the [previous version of this specification](https://entethalliance.org/specs/ethtrust-sl/v1/), Co-chairs Christopher Cordi and Opal Graham as well as previous co-chairs David Tarditi and Jaye Herrell the maintainers of the Solidity Compiler and those who write Solidity Security Alerts \[<a href="index.html#bib-solidity-alerts" class="bibref" data-link-type="biblio" title="Solidity Blog - Security Alerts">solidity-alerts</a>\], the community who developed and maintained the Smart Contract Weakness Classification \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], the Machine Consultancy for publishing the TMIO Best Practices \[<a href="index.html#bib-tmio-bp" class="bibref" data-link-type="biblio" title="Best Practices for Smart Contracts (privately made available to EEA members)">tmio-bp</a>\], and judges and participants in the [Underhanded Solidity](https://underhanded.soliditylang.org/) competitions that have taken place. They have all been very important sources of information and inspiration to the broader community as well as to us in developing this specification.

Security principles have also been developed over many years by many individuals, far too numerous to individually thank for contributions that have helped us to write the present specification. We are grateful to the many people on whose work we build.

### A.4 Changes<a href="index.html#sec-changes" class="self-link" aria-label="§"></a>

This section outlines substantive changes made to the specification since version 1:

#### A.4.1 New Requirements<a href="index.html#new-requirements" class="self-link" aria-label="§"></a>

The following requirements have been added to the specification since the previous release:

- [**\[S\] Encode hashes with `chainid`**](index.html#req-1-eip155-chainid),
- [**\[S\] Compiler Bug SOL-2023-3**](index.html#req-1-compiler-SOL-2023-3),
- [**\[S\] Compiler Bug SOL-2022-6**](index.html#req-1-compiler-SOL-2022-6),
- [**\[S\] Use a modern Compiler**](index.html#req-1-compiler-060),
- [**\[M\] Explicitly Disambiguate Evaluation Order**](index.html#req-2-enforce-eval-order),
- [**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check) as an Overriding Requirement for [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check),
- [**\[M\] Avoid Read-only Re-entrancy Attacks**](index.html#req-2-avoid-readonly-reentrancy)
- [**\[M\] Ensure Proper Rounding Of Computations Affecting Value**](index.html#req-2-check-rounding),
- [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7),
- [**\[M\] Solidity Compiler Bug 2023-1**](index.html#req-2-compiler-SOL-2023-1),
- [**\[M\] Use a modern Compiler**](index.html#req-2-compiler-060),
- [**\[Q\] Protect Gas Usage**](index.html#req-3-protect-gas),
- [**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles),
- [**\[Q\] Protect Against Governance Takeovers**](index.html#req-3-protect-governance),
- [**\[Q\] Intended Replay**](index.html#req-3-intended-replay),
- [**\[Q\] Access control permissions must be both revocable and transferable**](index.html#req-3-revocable-permisions), and
- [**\[Q\] No single Admin EOA for privileged actions**](index.html#req-3-no-single-admin-eoa).

The following <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a> have also been added

- [**\[GP\] Use Fuzzing As Part Of Testing**](index.html#req-R-fuzzing-in-testing),
- [**\[GP\] Select an appropiate threshold for multisig wallets**](index.html#req-R-multisig-threshold), and
- [**\[GP\] Use TimeLock delays for sensitive operations**](index.html#req-R-timelock-for-privileged-actions).

#### A.4.2 Updated Requirements<a href="index.html#updated-requirements" class="self-link" aria-label="§"></a>

The following requirements have been changed in some way since the previous release:

- update [**\[S\] Check External Calls Return**](index.html#req-1-check-return) to allow [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return) as an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>,
- Rename **\[S\] No Conflicting Inheritance** to [**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict),
- update [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall) to require [**\[M\] Document Special Code Use**](index.html#req-2-documented) as an additional <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> at Level \[M\],
- Make [**\[S\] Compiler Bug SOL-2020-4** also apply to Solidity compiler version 0.6.5,](index.html#req-1-compiler-SOL-2020-4)
- Add a requirement to document use of `delegatecall()` to [**\[Q\] Document Special Code Use**](index.html#req-2-documented),
- Explicitly require checking that contract addresses match assumptions in [**\[M\] Protect External Calls**](index.html#req-2-external-calls),
- **\[Q\] Implement Access Control** renamed to [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control) clarifying that it requires providing least privilege, when the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> enables privileged access,
- [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev) lists in the explanatory text a minimum set of attack types that need consideration,
- [**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate) describes an additional use case,
- Clarify that as part of [**\[Q\] Document Contract Logic**](index.html#req-3-documented) documentation is expected to cover tokenomics, protection against MEV and flashloan attacks, and the like,
- [**\[Q\] Code Linting**](index.html#req-3-linted) includes an additional requirement to check that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> uses explicitly labeled constructors. Formerly the requirements for this were at lower levels, but the potential security impact does not justify the lower level requirements, and
- Explicitly state that [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control) is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct).

The following <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 4.4 Recommended Good Practices</a> have also been updated

- [**\[GP\] Check For and Address New Security Bugs**](https://entethalliance.org/specs/ethtrust-sl/v2/req-R-check-new-bugs) updated because this specification accounts for Solidity Compiler Bugs up to and including SOL-2023-2,
- [**\[GP\] Follow Accepted ERC Standards**](https://entethalliance.org/specs/ethtrust-sl/v2/req-R-follow-erc-standards) edited for clarity, and
- [**\[GP\] Define a Software License**](https://entethalliance.org/specs/ethtrust-sl/v2/req-R-define-license) edited for clarity and better explanation.

#### A.4.3 Requirements removed<a href="index.html#requirements-removed" class="self-link" aria-label="§"></a>

- The requirement to check usage of `transfer()` was removed from [\[S\] Check External Calls Return](index.html#req-1-check-return) because it isn't one of the low-level functions: It reverts on failure.
- The statements of Requirement **\[S\] Explicit Constructors**, and **\[M\] Declare Explicit Constructors**, were removed, but the checks remain, moved into [**\[Q\] Code Linting**](index.html#req-3-linted).
- Many Compiler bugs for old Solidity Compiler versions, instead using the [version 1 specification](https://entethalliance.org/specs/ethtrust-sl/v1) to provide them as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> in the rare cases they are necessary and applicable:
  - **\[S\] Explicit Storage** and its overriding requirement **\[M\] Declare `storage` Explicitly**,
  - **\[S\] Compiler Bug SOL-2020-11-length**,
  - **\[S\] Compiler Bug SOL-2019-10**,
  - **\[S\] Compiler Bugs SOL-2019-3,6,7,9**,
  - **\[S\] Compiler Bug SOL-2019-8**,
  - **\[S\] Compiler Bug SOL-2019-5**,
  - **\[S\] Compiler Bug SOL-2019-4**,
  - **\[S\] Compiler Bug SOL-2019-2**,
  - **\[S\] Compiler Bug SOL-2019-1**,
  - **\[S\] Compiler Bug SOL-2018-4**,
  - **\[S\] Compiler Bug SOL-2018-3**,
  - **\[S\] Compiler Bug SOL-2018-2**,
  - **\[S\] Compiler Bug SOL-2018-1**,
  - **\[S\] Compiler Bug SOL-2017-5**,
  - **\[S\] Compiler Bug SOL-2017-4**,
  - **\[S\] Compiler Bug SOL-2017-3**,
  - **\[S\] Compiler Bug SOL-2017-2**,
  - **\[S\] Compiler Bug SOL-2017-1**,
  - **\[S\] Compiler Bug SOL-2016-11**,
  - **\[S\] Compiler Bug SOL-2016-10**,
  - **\[S\] Compiler Bug SOL-2016-9**,
  - **\[S\] Compiler Bug SOL-2016-8**,
  - **\[S\] Compiler Bug SOL-2016-7**,
  - **\[S\] Compiler Bug SOL-2016-6**,
  - **\[S\] Compiler Bug SOL-2016-5**,
  - **\[S\] Compiler Bug SOL-2016-4**,
  - **\[S\] Compiler Bug SOL-2016-3**,
  - **\[S\] Compiler Bug SOL-2016-2**,
  - **\[M\] Compiler Bug SOL-2020-2**,
  - **\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**,
  - **\[M\] Compiler Bug Check Identity Calls**,
  - **\[M\] Validate `ecrecover()` input**, and
  - **\[M\] Compiler Bug No Zero Ether Send**.

## B. References<a href="index.html#references" class="self-link" aria-label="§"></a>

### B.1 Normative references<a href="index.html#normative-references" class="self-link" aria-label="§"></a>

\[c-e-i\]
[Security Considerations - Solidity Documentation. Section 'Use the Checks-Effects-Interactions Pattern'](https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern>

\[CVE-2021-42574\]
[National Vulnerability Database CVE-2021-42574](https://nvd.nist.gov/vuln/detail/CVE-2021-42574). The National Institute of Standards (US Department of Commerce). URL: <https://nvd.nist.gov/vuln/detail/CVE-2021-42574>

\[CWE\]
[Common Weakness Enumeration](https://cwe.mitre.org/index.html). MITRE. URL: <https://cwe.mitre.org/index.html>

\[CWE-1339\]
[CWE-1339: Insufficient Precision or Accuracy of a Real Number](https://cwe.mitre.org/data/definitions/1339.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/1339.html>

\[CWE-252\]
[CWE-252: Unchecked Return Value](https://cwe.mitre.org/data/definitions/252.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/252.html>

\[CWE-284\]
[CWE-284: Improper Access Control](https://cwe.mitre.org/data/definitions/284.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/284.html>

\[CWE-573\]
[CWE-573: Improper Following of Specification by Caller](https://cwe.mitre.org/data/definitions/573.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/573.html>

\[CWE-667\]
[CWE-667: Improper Locking](https://cwe.mitre.org/data/definitions/667.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/667.html>

\[CWE-670\]
[CWE-670: Always-Incorrect Control Flow Implementation](https://cwe.mitre.org/data/definitions/670.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/670.html>

\[CWE-94\]
[CWE-94: Improper Control of Generation of Code ('Code Injection')](https://cwe.mitre.org/data/definitions/94.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/94.html>

\[DevCon-rounding\]
[Tackling Rounding Errors with Precision Analysis](https://archive.devcon.org/archive/watch/6/tackling-rounding-errors-with-precision-analysis/?tab=YouTube). Raoul Schaffranek. Ethereum Foundation. URL: <https://archive.devcon.org/archive/watch/6/tackling-rounding-errors-with-precision-analysis/?tab=YouTube>

\[DevCon-siphoning\]
[The Gas Siphon Attack: How it Happened and How to Protect Yourself](https://archive.devcon.org/archive/watch/5/the-gas-siphon-attack-how-it-happened-and-how-to-protect-yourself/?tab=YouTube). Shane Fontaine. Ethereum Foundation. URL: <https://archive.devcon.org/archive/watch/5/the-gas-siphon-attack-how-it-happened-and-how-to-protect-yourself/?tab=YouTube>

\[EF-SL\]
[Specification languages for creating formal specifications](https://ethereum.org/en/developers/docs/smart-contracts/formal-verification/#specification-languages). Ethereum Foundation. URL: <https://ethereum.org/en/developers/docs/smart-contracts/formal-verification/#specification-languages>

\[EIP\]
[EIP-1: EIP Purpose and Guidelines](https://eips.ethereum.org/EIPS/eip-1). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-1>

\[EIP-155\]
[Simple Replay Attack Protection](https://eips.ethereum.org/EIPS/eip-155). Vitalik Buterin. Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-155>

\[EIP-6049\]
[Deprecate SELFDESTRUCT](https://eips.ethereum.org/EIPS/eip-6049). William Entriken. Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-6049>

\[ERC\]
[ERC Final - Ethereum Improvement Proposals](https://eips.ethereum.org/erc). Ethereum Foundation. URL: <https://eips.ethereum.org/erc>

\[ERC137\]
[ERC-137: Ethereum Domain Name Service - Specification](https://eips.ethereum.org/EIPS/eip-137). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-137>

\[ERC20\]
[EIP-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-20>

\[ERC721\]
[ERC 721: Non-fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721/). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-721/>

\[error-handling\]
[Control Structures - Solidity Documentation. Section 'Error handling: Assert, Require, Revert and Exceptions'](https://docs.soliditylang.org/en/v0.8.14/control-structures.html#error-handling-assert-require-revert-and-exceptions). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/v0.8.14/control-structures.html#error-handling-assert-require-revert-and-exceptions>

\[EthTrust-sl-v1\]
[EEA EthTrust Security Levels Specification. Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/). Enterprise Ethereum Alliance. URL: <https://entethalliance.org/specs/ethtrust-sl/v1/>

\[EVM-version\]
[Using the Compiler - Solidity Documentation. (§Targets)](https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options>

\[freipi\]
[You're writing require statements wrong](https://www.nascent.xyz/idea/youre-writing-require-statements-wrong). Brock Elmore. Nascent. URL: <https://www.nascent.xyz/idea/youre-writing-require-statements-wrong>

\[GDPR\]
[Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) (Text with EEA relevance)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679). The European Union. URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679>

\[hash-commit\]
[Commitment scheme - WikiPedia](https://en.wikipedia.org/wiki/Commitment_scheme). WikiMedia Foundation. URL: <https://en.wikipedia.org/wiki/Commitment_scheme>

\[Ivanov\]
[Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts](https://arxiv.org/pdf/2105.00132.pdf#subsection.4.2). Nikolay Ivanov; Jianzhi Lou; Ting Chen; Jin Li; Qiben Yan. URL: <https://arxiv.org/pdf/2105.00132.pdf#subsection.4.2>

\[NatSpec\]
[NatSpec Format - Solidity Documentation](https://docs.soliditylang.org/en/latest/natspec-format.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/natspec-format.html>

\[Ownable\]
[ERC-173: Contract Ownership Standard](https://eips.ethereum.org/EIPS/eip-173). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-173>

\[RBAC\]
[INCITS 359-2012: Information Technology - Role Based Access Control](http://www.techstreet.com/products/1837530). InterNational Committee for Information Technology Standards. URL: <http://www.techstreet.com/products/1837530>

\[RFC2119\]
[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

\[RFC8174\]
[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

\[rounding-errors\]
[Formal Specification of Constant Product (x × y = k) Market Maker Model and Implementation](https://github.com/runtimeverification/verified-smart-contracts/blob/uniswap/uniswap/x-y-k.pdf). Runtime Verification. URL: <https://github.com/runtimeverification/verified-smart-contracts/blob/uniswap/uniswap/x-y-k.pdf>

\[SHA3-256\]
[FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions](http://dx.doi.org/10.6028/NIST.FIPS.202). The National Institute of Standards (US Department of Commerce). URL: <http://dx.doi.org/10.6028/NIST.FIPS.202>

\[software-license\]
[Choosing an Open Source License](https://choosealicense.com/). GitHub. URL: <https://choosealicense.com/>

\[solidity-alerts\]
[Solidity Blog - Security Alerts](https://blog.soliditylang.org/category/security-alerts/). Ethereum Foundation. URL: <https://blog.soliditylang.org/category/security-alerts/>

\[solidity-bugs\]
[List of Known Bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst>

\[solidity-bugs-json\]
[A JSON-formatted list of some known security-relevant Solidity bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.json). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.json>

\[solidity-cheatsheet\]
[Solidity Documentation: Cheatsheet - Order Of Precedence Of Operators](https://docs.soliditylang.org/en/latest/cheatsheet.html#order-of-precedence-of-operators). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/cheatsheet.html#order-of-precedence-of-operators>

\[solidity-events\]
[Solidity Documentation: Contracts - Events](https://docs.soliditylang.org/en/latest/contracts.html#events). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/contracts.html#events>

\[solidity-functions\]
[Solidity Documentation: Contracts - Functions](https://docs.soliditylang.org/en/latest/contracts.html#functions). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/contracts.html#functions>

\[solidity-patterns\]
[Solidity Patterns](https://fravoll.github.io/solidity-patterns/). Franz Volland. URL: <https://fravoll.github.io/solidity-patterns/>

\[solidity-release-818\]
[Solidity 0.8.18 Release Announcement](https://soliditylang.org/blog/2023/02/01/solidity-0.8.18-release-announcement/). Ethereum Foundation. 2023-02-01. URL: <https://soliditylang.org/blog/2023/02/01/solidity-0.8.18-release-announcement/>

\[solidity-security\]
[Security Considerations - Solidity Documentation.](https://docs.soliditylang.org/en/latest/security-considerations.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/security-considerations.html>

\[Solidity-Style-Guide\]
[Solidity Style Guide - Solidity Documentation](https://docs.soliditylang.org/en/latest/style-guide.html). URL: <https://docs.soliditylang.org/en/latest/style-guide.html>

\[richards2022\]
[Solidity Underhanded Contest 2022. Submission 9 - Tynan Richards](https://github.com/ethereum/solidity-underhanded-contest/tree/master/2022/submissions_2022/submission9_TynanRichards). Ethereum Foundation. URL: <https://github.com/ethereum/solidity-underhanded-contest/tree/master/2022/submissions_2022/submission9_TynanRichards>

\[swcregistry\]
[Smart Contract Weakness Classification Registry](https://swcregistry.io). ConsenSys Diligence. URL: <https://swcregistry.io>

\[TimeLock\]
[Protect Your Users With Smart Contract Timelocks](https://blog.openzeppelin.com/protect-your-users-with-smart-contract-timelocks/). OpenZeppelin. URL: <https://blog.openzeppelin.com/protect-your-users-with-smart-contract-timelocks/>

\[tmio-bp\]
[Best Practices for Smart Contracts (privately made available to EEA members)](https://github.com/EntEthAlliance/eta-registry/blob/master/working-docs/tmio-bp.md). TMIO. URL: <https://github.com/EntEthAlliance/eta-registry/blob/master/working-docs/tmio-bp.md>

\[token-standards\]
[Ethereum Development Documentation - Token Standards](https://ethereum.org/en/developers/docs/standards/tokens/). Ethereum Foundation. URL: <https://ethereum.org/en/developers/docs/standards/tokens/>

\[unicode-bdo\]
[How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls). W3C Internationalization. 10 March 2016. URL: <https://www.w3.org/International/questions/qa-bidi-unicode-controls>

\[unicode-blocks\]
[Blocks-14.0.0.txt](https://www.unicode.org/Public/UNIDATA/Blocks.txt). Unicode®, Inc. 22 January 2021. URL: <https://www.unicode.org/Public/UNIDATA/Blocks.txt>

### B.2 Informative references<a href="index.html#informative-references" class="self-link" aria-label="§"></a>

\[ASVS\]
[OWASP Application Security Verification Standard](https://github.com/OWASP/ASVS). The OWASP Foundation. URL: <https://github.com/OWASP/ASVS>

\[chase\]
[Malleable Signatures: New Definitions and Delegatable Anonymous Credentials](https://smeiklej.com/files/csf14.pdf). Melissa Chase; Markulf Kohlweiss; Anna Lysyanskaya; Sarah Meiklejohn. URL: <https://smeiklej.com/files/csf14.pdf>

\[EEA-clients\]
[Enterprise Ethereum Client Specification - Editors' draft](https://entethalliance.github.io/client-spec/spec.html). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.github.io/client-spec/spec.html>

\[EEA-L2\]
[Introduction to Ethereum Layer 2](https://entethalliance.org/eea-primers/entry/5696/). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.org/eea-primers/entry/5696/>

\[EF-MEV\]
[Maximal Extractable Value (MEV)](https://ethereum.org/en/developers/docs/mev/). Ethereum Foundation. URL: <https://ethereum.org/en/developers/docs/mev/>

\[futureblock\]
[Future-block MEV in Proof of Stake](https://archive.devcon.org/archive/watch/6/future-block-mev-in-proof-of-stake/?tab=YouTube). Ethereum Foundation. URL: <https://archive.devcon.org/archive/watch/6/future-block-mev-in-proof-of-stake/?tab=YouTube>

\[License\]
[Apache license version 2.0](http://www.apache.org/licenses/LICENSE-2.0). The Apache Software Foundation. URL: <http://www.apache.org/licenses/LICENSE-2.0>

\[postmerge-mev\]
[Why is Oracle Manipulation after the Merge so cheap? Multi-Block MEV](https://chainsecurity.com/oracle-manipulation-after-merge/). ChainSecurity. URL: <https://chainsecurity.com/oracle-manipulation-after-merge/>

\[solidity-reports\]
[Reporting a Vulnerability, in Security Policy](https://github.com/ethereum/solidity/security/policy#reporting-a-vulnerability). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/security/policy#reporting-a-vulnerability>

[↑](index.html#title)
