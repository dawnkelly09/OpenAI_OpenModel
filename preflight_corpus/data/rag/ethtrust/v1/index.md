<a href="https://entethalliance.org" class="logo"><img src="eea_logo.svg" id="eea-logo" width="180" height="90" alt="EEA" /></a>

# EEA EthTrust Security Levels Specification v1

## EEA Specification 22 August 2022

SUPERSEDED VERSION

This version of the specification was SUPERSEDED on 13 December 2023 by the [**EEA EthTrust Security Levels Specification Version 2**](https://entethalliance.org/specs/ethtrust-sl/v2/), available at <https://entethalliance.org/specs/ethtrust-sl/v2/>

This Version
[https://entethalliance.org/specs/ethtrust-sl/v1/](index.html)

Latest editor's draft:
<https://entethalliance.github.io/eta-registry/security-levels-spec.html>

Editor:
<a href="https://entethalliance.org/cdn-cgi/l/email-protection#2c4f444d4d405f6c4942584958444d4040454d424f4902435e4b" class="ed_mailto u-email email p-name">Chaals Nevile</a> (Enterprise Ethereum Alliance)

Contributors to this version:
Andrew Anderson (OpenZeppelin), Horacio Mijail Antón Quiles (ConsenSys), Imran Bashir (JPMorgan Chase), Yevhenii Bezuhlyi - Євгеній Безуглий (Hacken), Yevheniia Broshevan - Євгенія Брошеван (Hacken), Benjamin Bukari (Abbacio), Mark Carney (Santander), Michael Colburn (Trail of Bits), Christopher Cordi (Splunk), Cory Dickson (NVISO), Shayan Eskandari (ConsenSys), Joanne Fuller (ConsenSys), William Izzo (DTCC), Aminadav Glickshtein (EY), Dan Guido (Trail of Bits), Michael Lewellen (OpenZeppelin), Tom Lindeman (Runtime Verification / ConsenSys), Melanie Marsoller (Splunk), Pierre-Alain Mouy (NVISO), Dominik Muhs (ConsenSys Diligence), Luis Naranjo (Microsoft), Jyotirmayee Ponnapalli (DTCC), Jonathan Prince (NVISO), Przemek Siemion (Santander), Gonçalo Sá (ConsenSys), Grant Southey (ConsenSys), Michael Theriault (DTCC), Antoine Toulmé (TMIO), Ben Towne (SAE)

Copyright © 2020-2022 [Enterprise Ethereum Alliance](https://entethalliance.org/).

------------------------------------------------------------------------

## Abstrac

This document defines the requirements for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, a set of certifications that a smart contract has been reviewed and found not to have a defined set of security vulnerabilities.

## Status of This Documen

*This section describes the status of this document at the time of its publication. Newer documents may supersede this document.*

This specification is licensed by the Enterprise Ethereum Alliance, Inc. (EEA) under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) \[<a href="index.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\] Unless otherwise explicitly authorised in writing by the EEA, you can only use this specification in accordance with those terms.

Unless required by applicable law or agreed to in writing, this specification is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the \[<a href="index.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\] for the specific language governing permissions and limitations.

This is version 1 of the EEA EthTrust Security Levels Specification. The EEA Board has reviewed this document and authorised publication as an EEA Specification as requested by the EEA EthTrust Security Levels Working Group.

The Working Group *expects* at time of writing that an update to this Specification will be published some time in the next 6 to 18 months

Please send any comments to the EEA at <https://entethalliance.org/contact/>.

## Table of Contents

1.  <a href="index.html#sec-introduction" class="tocxref">1. Introduction</a>
    1.  <a href="index.html#sec-reading-the-spec" class="tocxref">1.1 How to read this specification</a>
        1.  <a href="index.html#sec-typographic-conventions" class="tocxref">1.1.1 Typographic Conventions</a>
        2.  <a href="index.html#sec-reading-requirements" class="tocxref">1.1.2 How to Read a Requirement</a>
            1.  <a href="index.html#sec-overriding-requirements" class="tocxref">1.1.2.1 Overriding Requirements</a>
            2.  <a href="index.html#sec-related-requirements" class="tocxref">1.1.2.2 Related Requirements</a>
    2.  <a href="index.html#sec-intro-why-certify-contracts" class="tocxref">1.2 Why Certify Contracts?</a>
    3.  <a href="index.html#sec-intro-developing-secure-contracts" class="tocxref">1.3 Developing Secure Smart Contracts</a>
    4.  <a href="index.html#sec-notifying-new-vulnerabilities" class="tocxref">1.4 Feedback and new vulnerabilities</a>
2.  <a href="index.html#conformance" class="tocxref">2. Conformance</a>
    1.  <a href="index.html#sec-conformance-claims" class="tocxref">2.1 Conformance Claims</a>
    2.  <a href="index.html#who-can-audit" class="tocxref">2.2 Who can offer EEA EthTrust Certification?</a>
    3.  <a href="index.html#sec-source-and-contracts" class="tocxref">2.3 Identifying what is certified</a>
3.  <a href="index.html#sec-security-considerations" class="tocxref">3. Security Considerations</a>
    1.  <a href="index.html#sec-proxy-contract-considerations" class="tocxref">3.1 Upgradable Contracts</a>
    2.  <a href="index.html#sec-oracle-considerations" class="tocxref">3.2 Oracles</a>
    3.  <a href="index.html#sec-reentrancy-considerations" class="tocxref">3.3 External Calls and Re-entrancy</a>
    4.  <a href="index.html#sec-signature-considerations" class="tocxref">3.4 Signature mechanisms</a>
    5.  <a href="index.html#sec-gas-considerations" class="tocxref">3.5 Gas and Gas Prices</a>
    6.  <a href="index.html#sec-mev-considerations" class="tocxref">3.6 MEV (Maliciously Extracted Value)</a>
    7.  <a href="index.html#sec-source-compiler-considerations" class="tocxref">3.7 Source code, pragma, and compilers</a>
    8.  <a href="index.html#sec-netupgrades-considerations" class="tocxref">3.8 Network Upgrades</a>
4.  <a href="index.html#sec-levels" class="tocxref">4. EEA EthTrust Security Levels</a>
    1.  <a href="index.html#sec-levels-one" class="tocxref">4.1 Security Level [S]</a>
        1.  <a href="index.html#sec-1-unicode" class="tocxref">4.1.1 Text and homoglyphs</a>
        2.  <a href="index.html#sec-1-external-calls" class="tocxref">4.1.2 External Calls</a>
        3.  <a href="index.html#sec-1-compile-improvements" class="tocxref">4.1.3 Improved Compilers</a>
        4.  <a href="index.html#sec-1-compiler-bugs" class="tocxref">4.1.4 Compiler Bugs</a>
    2.  <a href="index.html#sec-levels-two" class="tocxref">4.2 Security Level [M]</a>
        1.  <a href="index.html#sec-2-unicode" class="tocxref">4.2.1 Text and homoglyph attacks</a>
        2.  <a href="index.html#sec-2-external-calls" class="tocxref">4.2.2 External Calls</a>
        3.  <a href="index.html#sec-2-special-code" class="tocxref">4.2.3 Documenting Defensive Coding</a>
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
6.  <a href="index.html#references" class="tocxref">B. References</a>
    1.  <a href="index.html#normative-references" class="tocxref">B.1 Normative references</a>
    2.  <a href="index.html#informative-references" class="tocxref">B.2 Informative references</a>

## 1. Introduction

*This section is non-normative.*

This document, the EEA EthTrust Security Levels Specification, defines the requirements for granting <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> to a smart contract that has undergone a security audit.

No audit can guarantee that a smart contract is secure against **all possible** vulnerabilities, as explained in <a href="index.html#sec-security-considerations" class="sec-ref">3. Security Considerations</a>. However it can provide a certain assurance, backed not only by the reputation of the auditor issuing the certification, but by the collective reputations of the multiple experts in security from many competing organizations, who collaborated within the EEA to ensure this specification defines protections against a real and significant set of known vulnerabilities.

### 1.1 How to read this specification

This section describes how to understand this specification, including the conventions used for examples and requirements, core concepts, references, informative sections, etc.

#### 1.1.1 Typographic Conventions

Definintions of terms are formatted Like this and subsequent references are <a href="index.html#dfn-like-this" class="internalDFN" data-link-type="dfn">Like This</a>.

Bibliographic references e.g. to other documents are links to the relevant entry in the reference section, within square brackets: \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\]

Links to requirements and good practices begin with a Security Level in square brackets "\[\]", and include the requirement name. They are rendered as links in bold type:

[**\[M\] Document Special Code Use**](index.html#req-2-documented)

The formatting of requirements is described in detail in <a href="index.html#sec-reading-requirements" class="sec-ref">1.1.2 How to Read a Requirement</a>

Examples are given in some places. These are not requirements and are not normative. They are distinguished by a background with a border and title, like so:

<a href="index.html#example-1-example-an-example-example" class="self-link">Example 1</a>: Example: An example example

There may be text with `code()` inline in an example, as well as blocks of code:

``` solidity
  // SPDX-License-Identifier: MIT
  pragma solidity 0.8.0;

  contract HelloWorld{
      string public greeting = "Hello World";
  }

```

In a few places a word is used as a variable, for example so it can be described further on in a statement or requirement. These are formatted as `var`.

#### 1.1.2 How to Read a Requiremen

The core of this document is the requirements, that collectively define EEA EthTrust Certification.

Requirements have

- a Level,
- a name,
- a link identified with "🔗" to its URL, and
- a statement of what *MUST* be achieved to meet the requirement.

Some requirements at the same Security Level are grouped in a subsection, because they are related to a particular theme or area of potential attacks.

Most requirements or groups of requirements are followed by some explanation that can include why the requirement is important, how to test for it, links to <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>, test cases, and links to other useful information.

The following requirement:

<a href="index.html#example-2-a-simple-requirement" class="self-link">Example 2</a>: A simple requiremen

**\[S\] No Exact Balance Check [🔗](index.html#req-1-exact-balance-check)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* make tests that ether balance is equal to (i.e. `==`) a specified amount or the value of a variable.

Testing the balance of an account as a basis for some action has risks associated with unexpected receipt of ether or another token, including tokens deliberately transfered to cause such tests to fail, as an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[Q\] Protect against MEV**](index.html#req-3-block-mev), <a href="index.html#sec-mev-considerations" class="sec-ref">3.6 MEV (Maliciously Extracted Value)</a>, [SWC-132](https://swcregistry.io/docs/SWC-132) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and improper locking as described in \[<a href="index.html#bib-cwe-667" class="bibref" data-link-type="biblio" title="CWE-667: Improper Locking">CWE-667</a>\].

is a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, as noted by the "\[S\]" before its name. Its name is **No Unsafe Balance Check**. Its URL as linked from the " 🔗 " character is <https://entethalliance.org/specs/ethtrust-sl/#req-1-exact-balance-check>.

The statement of requirement is tha

> <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* make tests that ether balance is equal to (i.e. `==`) a specified amount or the value of a variable.

Following the requirement is a brief explanation of the relevant vulnerability, a link to further discussion, in this case in the security considerations section and in the "Smart Contract Weakness Classification Registry" \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] that includes test cases, and to the description of a related general vulnerability in the "Common Weakness Enumeration" \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\].

Note

Good Practices are formatted the same way as Requirements, with an apparent level of **\[GP\]**. However, as explained in <a href="index.html#sec-good-practice-recommendations" class="sec-ref">4.4 Recommended Good Practices</a> meeting them is not necessary and does not in itself change conformance to this specification.

##### 1.1.2.1 Overriding Requirements

For some requirements, the statement will include an alternative condition, introduced with the keyword **unless**, that identifies one or more Overriding Requirements. These are requirements at a higher Security Level, that can be satisfied to achieve conformance if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet the lower-level requirement as stated. In some cases it is necessary to meet more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> to meet the requirement they override. In this case, the requirements are described as a Set of Overriding Requirements. It is necessary to meet all the requirements in a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> in order to meet the requirement that is overriden.

In a number of cases, there will be more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> that can be met in order to satisfy a given requirement. For example, it is sometimes possible to meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> Requirement either by directly fulfilling it, or by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, or by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>.

The purpose of <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> is to simplify testing for simple cases that do not use features that need to be handled with extra care to avoid introducing vulnerabilities, while ensuring that more complex <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is appropriately checked.

In a typical case of an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, they apply in relatively unusual cases or where automated systems are generally unable to verify that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. Further manual verification of the applicable <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> can determine that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is using a feature appropriately, and therefore passes the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement.

If there is not an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for a requirement that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> does not meet, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is not eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. However even for such cases, note the Good Practice [**\[GP\] Meet as many requirements as possible**](index.html#req-R-meet-all-possible); meeting any requirements in this specification will improve the security of smart contracts.

In the following requirement:

- the Security Level is "**\[S\]**",
- the name is "**No `tx.origin`**", and
- the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> is "[**\[Q\] Verify `tx.origin` usage**](index.html#req-3-verify-tx.origin)".

<a href="index.html#example-3-example-a-requirement-with-an-overriding-requirement" class="self-link">Example 3</a>: Example: A requirement with an Overriding Requiremen

**\[S\] No `tx.origin` [🔗](index.html#req-1-no-tx.origin)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` usage**](index.html#req-3-verify-tx.origin).

The requirement that the tested code does not contain a `tx.origin` instruction is automatically verifiable.

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that does have a valid use for `tx.origin`, as decided by the auditor, and meets the Security Level \[Q\] <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` usage**](index.html#req-3-verify-tx.origin) conforms to this Security Level \[S\] requirement.

Requirements that are an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for another, or are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, expicitly mention that:

<a href="index.html#example-4-example-overriding-requirement" class="self-link">Example 4</a>: Example: Overriding Requiremen

**\[M\] No Unnecessary Unicode Controls [🔗](index.html#req-2-unicode-bdo)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirement</a> for [\[S\] No Unicode Direction Control Characters](index.html#req-1-unicode-bdo).

##### 1.1.2.2 Related Requirements

Many requirements have Related Requirements, which are requirements that address the same broad issues.

The links to them are provided as useful information. Unlike <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>, meeting Related Requirements does not substitute for meeting a specific requirement in order to achieve conformance.

### 1.2 Why Certify Contracts?

The smart contracts that power decentralized applications on Ethereum have been fraught with security issues, and today there is still no good way to see how secure an address or contract is before initiating a transaction. The Defi space in particular has exploded with a flurry of activity, with individuals and organizations approving transactions in token contracts, swapping tokens, and adding liquidity to pools in quick succession, sometimes without stopping to check security. For Ethereum to be trusted as a transaction layer, enterprises storing critical data or financial institutions moving large amounts of capital need a clear signal that a contract has had appropriate security audits.

Reviewing early, in particular before production deployment, is especially important in the context of blockchain development because the costs in time, effort, funds, and/or credibility, of attempting to update or patch a smart contract after deployment are generally much higher than in other software development contexts.

This smart contract security standard is designed to increase confidence in the quality of security audits for smart contracts, and thus to raise trust in the Ethereum ecosystem as a global settlement layer for all types of transactions across all types of industry sectors, for the benefit of the entire Ethereum ecosystem.

Certification also provides value to the actual or potential users of a smart contract, and others who may be affected by the use or abuse of a particular smart contract but are not themselves direct users. By limiting exposure to certain known weaknesses through <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, these stakeholders benefit from reduced risk and increased confidence in the security of assets held in or managed by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This assurance is not complete; for example it relies on the competence and integrity of the auditor issuing the certification. That may be incompletely knowable, and/or reflected in a professional reputation stemming from subsequently revealed information about the performance of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> they have audited. This is especially so if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> becomes sufficiently high-profile to motivate exploitation of any known weaknesses remaining after certification.

Finally, smart contract developers and ecosystem stakeholders receive value when others (including direct competitors) complete the certification process, because it means those other contracts are less likely to generate exploitation-related headlines which can lead to negative perceptions of Ethereum technology as insecure or high risk, by the general public including business leaders, prospective customers/users, regulators, and investors.

The value of smart contract security certification is in some ways analogous to the certification processes applicable to aircraft parts. Most directly, it helps reduce risks for part manufacturers and the integrators who use those parts as components of a more complex structure, by providing assurance of a minimum level of quality. Less directly, these processes significantly reduce aviation accidents and crashes, saving lives and earning the trust of both regulators and customers who consider the safety and risk of the industry and its supporting technology as a whole. Many safety certification processes began as voluntary procedures created by a manufacturer, or specified and required by a consortium of customers representing a significant fraction of the total market. Having proven their value, some of these certification processes are now required by law, to protect the public (including ground-based bystanders).

This document does not create an affirmative duty of compliance on any party, though requirements to comply with it may be created by contract negotiations or other processes with prospective customers or investors.

We hope the value of the certification process motivates frequent use, and furthers development of automated tools that can make the evaluation process easier and cheaper.

This is the first version of this specification. The Working Group expects that experience with implementing it will lead to revisions in a subsequent version. As issues in the specification and challenges in the implementation are discovered, we hope such discoveries will lead to change requests and increased participation in the [Enterprise Ethereum Alliance](https://entethalliance.org)'s [EthTrust Security Levels Working Group](https://entethalliance.github.io/eta-registry) or its successors, responsible for developing and maintaining this specification.

### 1.3 Developing Secure Smart Contracts

Security issues that this specification calls for checking are not necessarily obvious to smart contract developers, especially relative newcomers in a quickly growing field.

By walking their own code through the certification process, even if no prospective customer requires it, a smart contract developer can discover ways their code is vulnerable to known weaknesses and fix that code prior to deployment.

Developers ought to make their code as secure as possible. Instead of aiming to fulfil only the requirements to conform at a particular Security Level, ensuring that code implements as many requirements of this specification as possible per [**\[GP\] Meet As Many Requirements As Possible**](index.html#req-R-meet-all-possible) helps ensure the developer has considered all the vulnerabilities this specfication addresses.

Aside from the obvious reputational benefit, developers will learn from this process, improving their understanding of potential weaknesses and thus their ability to avoid them completely in their own work.

For an organization developing and deploying smart contracts, this process reduces the risks both to their credibility, and to their assets and other capital.

### 1.4 Feedback and new vulnerabilities

The Working Group seeks feedback on this specification: Implementation experience, suggestions to improve clarity, or questions if a particular section or requirement is difficut to understand.

We also explicitly want feedback about the use of a standard machine-readable format for <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claims</a>, whether being suitable for storing on a blockchain is important for such a format, and for other use cases.

EEA members are encouraged to provide feedback through joining the Working Group. Anyone can also provide feedback through the EEA's contact pages at <https://entethalliance.org/contact/> and it will be forwarded to the Working Group as appropriate.

We expect that new vunerabilities will be discovered after this specification is published. To ensure that we consider them for inclusion in a revised version, we welcome notification of them. EEA has created a specific email address to let us know about new security vulnerabilities: [\[email protected\]](https://entethalliance.org/cdn-cgi/l/email-protection#99eafcfaecebf0ede0b4f7f6edf0fafcead9fcf7edfcedf1f8f5f5f0f8f7fafcb7f6ebfe). Information sent to this address *SHOULD* be sufficient to identify and rectify the problem described, and *SHOULD* include references to other discussions of the problem. It will be assessed by EEA staff, and then forwarded to the Working Group to address the issue.

When these vulnerabilities affect the Solidity compiler, or suggest modifications to the compiler that would help mitigate the problem, the Solidity Development community *SHOULD* be notified, as described in \[solidity-reports\].

## 2. Conformance

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) \[<a href="index.html#bib-rfc2119" class="bibref" data-link-type="biblio" title="Key words for use in RFCs to Indicate Requirement Levels">RFC2119</a>\] \[<a href="index.html#bib-rfc8174" class="bibref" data-link-type="biblio" title="Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words">RFC8174</a>\] when, and only when, they appear in all capitals, as shown here.

This specification defines a number of requirements. As described in <a href="index.html#sec-reading-requirements" class="sec-ref">1.1.2 How to Read a Requirement</a>, each requirement has a Security Level (one, two or three), and a statement of the requirement that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> must meet.

In order to achieve <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at a specific Security Level, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet **all the requirements for that Security Level**, including all the requirements for lower Security Levels. Some requirements can either be met directly, or by meeting one or more <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirements</a> that mean the requirement is considered met.

Section <a href="index.html#sec-good-practice-recommendations" class="sec-ref">4.4 Recommended Good Practices</a>, contains further recommendations. There is no requirement to test for these; however careful implementation and testing is *RECOMMENDED*.

Note that good implementation of the Recommended Good Practices can enhance security, but in some cases incomplete or low-quality implementation could **reduce** security.

### 2.1 Conformance Claims

To grant <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> EEA EthTrust Certification, an auditor provides a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>, that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirements of the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> for which it is certified.

There is no required format for a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid conformance claim</a> for Version 1 of this specification, beyond being legible and containing the required information as specified in this section.

Note: Machine-readable formats

The Working Group believes that a standard machine-readable format for Conformance Claims would be useful, and seeks feedback on this question as well as concrete proposals for such a format, which *MAY* be adopted in a subsequent version.

A Valid Conformance Claim *MUST* include:

- The date on which the certification was issued, in 'YYYY-MM-DD' forma
- The <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> (of those listed at \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]) for which the certification is valid
- The version of the EEA EthTrust Security Levels specification for which the contract is certified (this specification is version 1)
- A name and a URL for the organisation or software issuing the certification
- The <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> ("1", "2", or "3") that the <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> claims.
- A \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the compiled bytecode for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number
- A \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the Solidity source code for each contract in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> certified, sorted ascending by the hash value interpreted as a number
- The compiler options applied for each compilation
- The contract metadata generated by the compiler
- A list of the requirements which were tested and a statement for each one, noting whether the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. This *MAY* include further information.
- For conformance claims where certification is granted because the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> met an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, the conformance claim *MUST* include the results for the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> met, and *MAY* omit the results for the requirement(s) whose results were thus unnecessary to determine conformance.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> for <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> *MUST* contain a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the documentation provided to meet [**\[Q\] Document Contract Logic**](index.html#req-3-documented) and [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *SHOULD* include

- a contact address for questions about or challenges to the certification.
- descriptions of conformance to the "Recommended Good Practices".

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* include:

- An address where a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the conformance claim has been recorded on an identified network, e.g. Ethereum Mainnet.
- An address of the contract deployed on an identified network, e.g. Ethereum Mainnet.

Valid values of EVM versions are those listed in the Solidity documentation \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]. As of July 2022 the two most recent are `london` and `berlin`.

### 2.2 Who can offer EEA EthTrust Certification?

This version of the specification does not make any restrictions on who can perform an audit and provide <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. There is no certification process defined for auditors or tools who grant certification. This means that Auditors' claims of performing accurate tests are made by themselves. There is always a possibility of fraud, misrepresentation, or incompetence on the part of any auditor who offers "EEA EthTrust certification" for Version 1.

Note

In principle anyone can submit a smart contract for verification. However submitters should be aware of any restrictions on usage arising from copyright conditions or the like. In addition, meeting certain requirements can be more difficult to demonstrate in a situation of limited control over the development of the smart contract.

The Working Group expects its own members, who wrote the specification, to behave to a high standard of integrity and to know the specification well, and notes that there are many others who also do so.

The Working Group or EEA *MAY* seek to develop an auditor certification program for subsequent versions of the EEA EthTrust Security Levels Specification.

### 2.3 Identifying what is certified

An EEA EthTrust evaluation is performed on Tested Code, which means the Solidity source code for a smart contract or several related smart contracts, along with the bytecode generated by compiling the code with specified parameters.

If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is divided into more than one smart contract, each deployable at a single address, it is referred to as a Set Of Contracts.

## 3. Security Considerations

*This section is non-normative.*

Security of information systems is a major field of work. There are risks inherent in any system of even moderate complexity.

This specification describes testing for security problems in Ethereum smart contracts. However there is no such thing as perfect security. EEA EthTrust certification means that at least a defined minimum set of checks has been performed on a smart contract. **This does not mean the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> definitely has no security vulnerabilities**. From time to time new security vulnerabilities are identified. Manual auditing procedures require skill and judgement. This means there is always a possibility that a vulnerability is not noticed in review.

Ethereum is based on a model of account holders authorising transactions between accounts. It is very difficult to stop a malicious actor with a privileged key from using that to cause undesirable or otherwise bad outcomes.

### 3.1 Upgradable Contracts

Smart contracts in Ethereum are immutable by default. However, for some scenarios, it is desirable to be able to modify them to add new features or fix bugs. An Upgradable Contract is any type of contract that fulfills these needs by enabling changes to its code while preserving storage and balance at a fixed address.

Some of the most common and useful patterns for Upgradable Contracts utilize a proxy. A Proxy Contract is a simple wrapper or "proxy" which users interact with directly and is in charge of forwarding transactions to and from another contract (called the Execution Contract in this document), which contains the logic. The <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be replaced while the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>, acting as the access point, is never changed. Both contracts are still immutable in the sense that their code cannot be changed, but one <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be swapped out with another. The <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> can thus point to a different implementation and in doing so, the software is "upgraded".

This means that a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> that follow this pattern to make an <a href="index.html#dfn-upgradable-contract" class="internalDFN" data-link-type="dfn">Upgradable Contract</a> generally cannot be considered immutable, as the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> itself could redirect calls to a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a>, which may be insecure or malicous. By meeting the requirements for [access control](index.html#sec-3-access-control) in this specification to restrict upgrade capabilities enabling new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contracts</a> to be deployed, and by documenting upgrade patterns and following that documentation per [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), deployers of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can demonstrate reliability. In general, EthTrust certification of a <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> does not apply to the internal logic of an Upgradable Contract, so a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> needs to be certified before upgrading to it through the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>.

### 3.2 Oracles

A common feature of Ethereum networks is the use of Oracles; functions that can be called to provide information from outside a blockchain, from weather forecasts to random number generation. This specification contains requirements to check that smart contracts are sufficiently robust to deal appropriately with whatever information is returned (including the possibility of mal-formed data, that can potentially be delibrately crafted as an attack). However, determining whether data produced by an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> is actually true is beyond the scope of this specification, and it is possible that an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> provides misinformation or even actively produces harmful disinformation.

### 3.3 External Calls and Re-entrancy

Code that relies on external code can introduce multiple attack vectors. This includes cases where an external dependency contains malicious code or has been subject to malicious manipulation through security vulnerabilities. However, failure to adequately manage the possible outcomes of an external call can also introduce security vulnerabilities.

One of the most commonly cited vulnerabilities in Ethereum Smart Contracts is Re-entrancy Attacks. These attacks allow malicious contracts to make a call back into the contract that called it before the originating contract's function call has been completed. This effect causes the calling contract to complete its processing in unintended ways, for example, by making unexpected changes to its state variables.

### 3.4 Signature mechanisms

Some requirements in the document refer to Malleable Signatures. These are signatures created according to a scheme constructed so that, given a message and a signature, it is possible to efficiently compute the signature of a different message - usually one that has been transformed in specific ways. While there are very valuable use cases that such signature schemes allow, if not used carefully they can lead to vulnerabilites, which is why this specfication seeks to constrain their use appropriately.

For more information on this topic, and the potential for exploitation, see also \[<a href="index.html#bib-chase" class="bibref" data-link-type="biblio" title="Malleable Signatures: New Definitions and Delegatable Anonymous Credentials">chase</a>\].

### 3.5 Gas and Gas Prices

Gas Griefing is the deliberate abuse of the Gas mechanism that Ethereum uses to regulate the consumption of computing power, to cause an unexpected or adverse outcome much in the style of a Denial of Service attack. Because Ethereum is designed with the Gas mechanism as a regulating feature, it is insufficient to simply check that a transaction has enough Gas; checking for Gas Griefing needs to take into account the goals and business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements.

In addition, a common feature of Ethereum network upgrades is to change the Gas Price of specific operations. EEA EthTrust certification only applies for the <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> specified; it is not valid for other versions. Thus it is important to recheck code to ensure its security properties remain the same across network upgrades, or take remedial action.

### 3.6 MEV (Maliciously Extracted Value)

MEV, used in this document to mean "Maliciously Extracted Value" refers to the potential for block producers or other paticipants in a blockchain to extract value that is not intentionally given to them, in other words to steal it, by maliciously reordering transactions, as in <a href="index.html#dfn-timing-attacks" class="internalDFN" data-link-type="dfn">Timing Attacks</a>, or suppressing them.

For example a Smart Contract promises an award to the first transaction that answers a question. A block producer that knows the answer can drop all transactions that send the answer, except for their own in the block.

The term is commonly expanded as "Miner Extracted Value", as in the example above. But MEV can be exploited by other participants, for example duplicating most of a submitted transaction, offering a higher fee so it is processed first. It is also sometimes called "Maximum Extractable Value".

Some MEV attacks can be prevented by requires careful consideration of the information that is included in a transaction, including the parameters required by a contract.

Other strategies include the use of hash commitment schemes \[<a href="index.html#bib-hash-commit" class="bibref" data-link-type="biblio" title="Commitment scheme - WikiPedia">hash-commit</a>\], batch execution, private transactions \[<a href="index.html#bib-eea-clients" class="bibref" data-link-type="biblio" title="Enterprise Ethereum Client Specification - Editors&#39; draft">EEA-clients</a>\], Layer 2 \[<a href="index.html#bib-eea-l2" class="bibref" data-link-type="biblio" title="Introduction to Ethereum Layer 2">EEA-L2</a>\], or an extension to establish the ordering of transactions before releasing sensitive information to all nodes participating in a blockchain.

The Ethereum Foundation curates up to date information on MEV \[EF-MEV\].

Timing Attacks are a class of MEV attacks where an adversary benefits from placing their or a victim's transactions earlier or later in a block. They include <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, <a href="index.html#dfn-back-running" class="internalDFN" data-link-type="dfn">Back-Running</a>, and <a href="index.html#dfn-sandwich-attacks" class="internalDFN" data-link-type="dfn">Sandwich Attacks</a>.

Front-Running is based on the fact that transactions are visible to the participants in the network before they are added to a block. This allows a malicious participant to submit an alternative transaction, frustrating the aim of the original transaction.

In a system designed to attest original authorship, a malicious participant uses the information in a claim of authorship to create a rival claim, and adds their claim to a block first.

Back-Running is similar to <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, except the attacker places their transactions after the one they are attacking.

In Sandwich Attacks, an attacker places a victim's transaction undesirably between two other transactions.

An attacker creates a buy and sell transaction before and after a victim's buy transaction, artificially driving the price up for the victim and providing no-risk profit for the attacker at the victim's expense.

### 3.7 Source code, pragma, and compilers

This version of the specification requires the compiled bytecode as well as the Solidity Source Code that create the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Solidity is by a large measure the most common programming language for Ethereum smart contracts, and benefits of requiring source code in Solidity include

- Having it simplifies a number of tests
- There is substantial security research done that is based on Solidity source code.

Solidity allows the source code to specify the compiler version used. This specification currently has no requirement for a specific pragma, but it is a good practice to ensure that the pragma refers to a bounded set of versions, where it is known that those versions of the compiler produce identical bytecode from the given source code.

There are some drawbacks to requiring Solidity Source code. The most obvious is that some code that is not written in Solidity. Different languages have different features and often support different coding styles.

Perhaps more important, it means that a deployed contract, which may have been written in Solidity, cannot be tested directly without someone making the source code available.

Another important limitation introduced by reading source code is that it is subject to <a href="index.html#dfn-homoglyph-attacks" class="internalDFN" data-link-type="dfn">Homoglyph Attacks</a>, where characters that look the same but are different such as Latin "p" and Cyrillic "р", can deceive people visually reading the source code, to disguise malicious behaviour. There are related attacks that use features such as <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode Direction Control Characters</a> or take advantage of inconsistent normalisation of combining characters to achieve the same type of deceptions.

### 3.8 Network Upgrades

From time to time the Ethereum community implements a Network Upgrade, sometimes also called a **hard fork**. This is a change to Ethereum that is backwards-incompatible. Because they *typically* change the EVM, Ethereum Mainnet <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a> generally correspond to <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>.

A <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can affect more or less any aspect of Ethereum, including changing EVM opcodes or their Gas price, changing how blocks are added, or how rewards are paid, among many possibilities.

Because <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a> are not guaranteed to be backwards compatible, a newer <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version</a> can process bytecode in unanticipated ways. If a <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> changes the EVM to fix a security problem, it is important to consider that change, and it is a good practice to follow that upgrade. Enterprise Ethereum (as defined in \[<a href="index.html#bib-eea-clients" class="bibref" data-link-type="biblio" title="Enterprise Ethereum Client Specification - Editors&#39; draft">EEA-clients</a>\] and \[<a href="index.html#bib-eea-chains" class="bibref" data-link-type="biblio" title="Enterprise Ethereum Alliance Permissioned Blockchains Specification - Editors&#39; draft">EEA-chains</a>\]) follows Ethereum <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrades</a>.

Because claims of conformance to this specification are only valid for specific <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>, a <a href="index.html#dfn-hard-fork" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can mean an updated audit is needed to maintain valid <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for the current Ethereum network. Network Upgrades typically only impact a few features. This helps limit the effort necessary to audit code after an upgrade: often there will be no changes that affect the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, or review of a small proportion that is the only part affected by a Network Upgrade will be sufficient to renew <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

## 4. EEA EthTrust Security Levels

<a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is available at three Security Levels. The Security Levels describe minimum requirements for certifications at each Security Level: \[S\], \[M\], and \[Q\]. These Security Levels provide successively stronger assurance that a smart contract does not have specific security vulnerabilities.

- [Level \[S\]](index.html#sec-levels-one) is designed so that for most cases, where common features of Solidity are used following well-known patterns, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be certified by an automated "static analysis" tool.
- [Level \[M\]](index.html#sec-levels-two) mandates a stricter static analysis. It includes requirements where a human auditor is expected to determine whether use of a feature is necessary, or whether a claim about the security properties of code is justified.
- [Level \[Q\]](index.html#sec-levels-three) provides analysis of the business logic the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements, and that the code not only does not exhibit known security vulnerabilities, but also correctly implements what it claims to do.

The optional [Recommended Good Practices](index.html#sec-good-practice-recommendations), correctly implemented, further enhance the Security of smart contracts. However it is not necessary to test them to conform to this specification.

Note

This scheme has been compared to the conformance approach used in the "OWASP Application Security Verification Standard" specification family \[<a href="index.html#bib-asvs" class="bibref" data-link-type="biblio" title="OWASP Application Security Verification Standard">ASVS</a>\]. There are some clear differences, largely resulting from the differences between the general applicability ASVS aims to achieve, and this specification's very precise focus on the security of Ethereum smart contracts written in Solidity.

The vulnerabilities addressed by this specification come from a number of sources, including Solidity Security Alerts \[<a href="index.html#bib-solidity-alerts" class="bibref" data-link-type="biblio" title="Solidity Blog - Security Alerts">solidity-alerts</a>\], the Smart Contract Weakness Classification \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], TMIO Best practices \[<a href="index.html#bib-tmio-bp" class="bibref" data-link-type="biblio" title="Best Practices for Smart Contracts (privately made available to EEA members)">tmio-bp</a>\], various sources of Security Advisory Notices, and practical tests that auditors perform.

### 4.1 Security Level \[S\]

<a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> is intended to allow an unguided automated tool to analyze most contracts' bytecode and source code, and determine whether they meet the requirements. For some situations that are difficut to verify automatically, usually only likely to arise in a small minority of contracts, there are higher-level <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> that can be fulfilled to meet a requirement for this Security Level.

To be eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for Security Level \[S\], <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* fulfil all <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements, **unless** it meets the applicable **<a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a>** for any <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement it does not meet.

**\[S\] No `CREATE2`<a href="index.html#req-1-no-create2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction.
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

The `CREATE2` opcode provides the ability to interact with addresses that do not exist yet on-chain but could possibly eventually contain code. While this can be useful for deployments and counterfactual interactions with contracts, it may allow external calls to code that is not yet known, and could turn out to be malicous or insecure due to errors or weak protections.

**\[S\] No `tx.origin`<a href="index.html#req-1-no-tx.origin" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` usage**](index.html#req-3-verify-tx.origin)

`tx.origin` is a global variable in Solidity which returns the address of the account that sent the transaction. A contract using `tx.origin` could be made vulnerable if an authorized account calls into a malicious contract, allowing it to pass the authorization check in unintended cases. Use `msg.sender` for authorization instead of `tx.origin`.

See also [SWC-115](https://swcregistry.io/docs/SWC-115) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[S\] No Exact Balance Check<a href="index.html#req-1-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable.

Testing the balance of an account as a basis for some action has risks associated with unexpected receipt of ether or another token, including tokens deliberately transfered to cause such tests to fail as an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), [**\[M\] Don't misuse block data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev), <a href="index.html#sec-mev-considerations" class="sec-ref">3.6 MEV (Maliciously Extracted Value)</a>, [SWC-132](https://swcregistry.io/docs/SWC-132) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and improper locking as described in \[<a href="index.html#bib-cwe-667" class="bibref" data-link-type="biblio" title="CWE-667: Improper Locking">CWE-667</a>\].

**\[S\] No Conflicting Inheritance<a href="index.html#req-1-inheritance-conflict" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* include more than one variable, or operative function with different code, with the same name
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order).

In most programming languages, including Solidity, it is possible to use the same name for variables or functions that have different types or (for functions) input parameters. This can be hard to interpret in the source code, meaning reviewers misunderstand the code or are maliciously misled to do so, analogously to <a href="index.html#dfn-homoglyph-attacks" class="internalDFN" data-link-type="dfn">Homoglyph Attacks</a>.

This requirement means that unless the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> is met, any function or variable name will not be repeated, to eliminate confusion. It does however allow functions to be overridden, e.g. from a Base contract, so long as there is only one version of the function that operates within the code.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2020-2**](index.html#req-2-compiler-SOL-2020-2), and the [documentation of function inheritance](https://docs.soliditylang.org/en/latest/contracts.html#inheritance) in \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\]

**\[S\] No Hashing Consecutive Variable Length Arguments<a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

The elements of each variable-length argument to `abi.encodePacked()` are packed in order prior to hashing. Hash collisions are possible by rearranging the elements between consecutive, variable length arguments while maintaining that their concatenated order is the same.

**\[S\] No Self-destruct<a href="index.html#req-1-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, sending any Ether held by the contract, which may result in stealing it. This feature can often break immutability and trustless guarantees to introduce numerous security issues. In addition, once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

See also [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[S\] No `assembly()`<a href="index.html#req-1-no-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

The `assembly()` instruction allows lower-level code to be included. This give the authors much stronger control over the bytecode that is generated, which can be used for example to optimise gas usage. However, it also potentially exposes a number of vulnerabilites and bugs that are additional attack surfaces, and there are a number of ways to use `assembly()` to introduce deliberately malicious code that is difficult to detect.

#### 4.1.1 Text and homoglyphs

**\[S\] No Unicode Direction Control Characters<a href="index.html#req-1-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the Unicode Direction Control Characters `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

Changing the apparent order of characters through the use of invisible <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> can mask malicious code, even in viewing source code, to deceive human auditors.

More information on <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> is available in the W3C note [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls) \[<a href="index.html#bib-unicode-bdo" class="bibref" data-link-type="biblio" title="How to use Unicode controls for bidi text">unicode-bdo</a>\].

#### 4.1.2 External Calls

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[M\] Protect External Calls**](index.html#req-2-external-calls), [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return), and [**\[Q\] Verify External Calls**](index.html#req-3-external-calls).

**\[S\] Check External Calls Return<a href="index.html#req-1-check-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call`, `delegatecall`, `staticcall`, `send`, and `transfer`) *MUST* check the returned value from each usage to determine whether the call failed.

Normally, exceptions in subcalls "bubble up", unless they are handled in a try/catch. However Solidity defines a set of Low-level Call Functions:

- `call()`,
- `delegatecall()`,
- `staticcall()`,
- `send()`, and
- `transfer()`.

Calls using these functions behave differently. They return a boolean indicating whether the call completed successfully. Not testing explicitly whether these calls fail may lead to unexpected behavior in the caller contract.

See also [SWC-104](https://swcregistry.io/docs/SWC-104) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], error handling documentation in \[<a href="index.html#bib-error-handling" class="bibref" data-link-type="biblio" title="Control Structures - Solidity Documentation. Section &#39;Error handling: Assert, Require, Revert and Exceptions&#39;">error-handling</a>\], unchecked return value as described in \[<a href="index.html#bib-cwe-252" class="bibref" data-link-type="biblio" title="CWE-252: Unchecked Return Value">CWE-252</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return), [**\[Q\] Verify External Calls**](index.html#req-3-external-calls)

**\[S\] Use Check-Effects-Interaction<a href="index.html#req-1-use-c-e-i" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented)

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The Checks-Effects-Interactions pattern ensures that validation of the request, and changes to the state variables of the contract, are performed before any interactions take place with other contracts. When contracts are implemented this way, the scope for <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> is reduced significantly.

See also <a href="index.html#sec-reentrancy-considerations" class="sec-ref">3.3 External Calls and Re-entrancy</a>, the explanation of "Checks-Effects-Interactions" \[<a href="index.html#bib-c-e-i" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation. Section &#39;Use the Checks-Effects-Interactions Pattern&#39;">c-e-i</a>\] in "Solidity Security Considerations" \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], and "[Checks Effects Interactions](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\].

**\[S\] No `delegatecall()`<a href="index.html#req-1-delegatecall" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Protect External Calls**](index.html#req-2-external-calls).
**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The `delegatecall()` instruction enables an external contract to manipulate the state of a contract that calls it, because the code is run with the caller's balance, storage, and address.

#### 4.1.3 Improved Compilers

The requirements in this subsection can be met by using a sufficiently recent version of the Solidity compiler. Otherwise, there are <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> to perform the same testing that the up-to-date compiler checks:

- From 0.8.0 the compiler checks for arithmetic causing overflows and underflows.
- From 0.5.0 storage has to be declared explicitly as `storage` or `memory`.
- From 0.4.22 code does not compile if it uses constructors that are not explicitly declared as `constructor`.

**\[S\] No Overflow/Underflow<a href="index.html#req-1-overflow-underflow" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.8.0
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

Like most programming languages, the EVM and Solidity represent numbers as a set of bytes that by default has a fixed length. This means arithmetic operations on large numbers can "overflow" the size by producing a result that does not fit in the space allocated. This results in corrupted data, and can be used as an attack on code. The \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\] registry of generic code vulnerabilities contains many overflow attacks; it is a well-known vector that is exposed in many systems and has regularly been exploited.

There are many ways to check for overflows, or underflows (where a negative number is large enough in magnitude to trigger the same effect). Since version 0.8.0 Solidity includes built-in protection. <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> compiled with an earlier version needs to check explicitly to mitigate this potential vulnerability.

**\[S\] Explicit Storage<a href="index.html#req-1-explicit-storage" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.5.0
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Declare `storage` Explicitly**](index.html#req-2-explicit-storage).

Versions of Solidity older before 0.5.0 allowed contracts to create uninitialized `storage`, which could be attacked by malicious code.

See the section [Uninitialised Storage Pointers](https://blog.sigmaprime.io/solidity-security.html#storage) in \[<a href="index.html#bib-sigp" class="bibref" data-link-type="biblio" title="Solidity Security: Comprehensive List of Known Attack Vectors and Common Anti-Patterns">sigp</a>\] for further discussion of the vulnerability, and how it has been exploited, and [SWC-109](https://swcregistry.io/docs/SWC-109) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] for some more exammple code.

**\[S\] Explicit Constructors<a href="index.html#req-1-explicit-constructors" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.4.22
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Declare Constructors Explicitly**](index.html#req-2-explicit-constructors).

Versions of Solidity older than 0.4.22 define constructors implicitly, as a function with the same name as a `contract`. If the source code is copied, and the contract's name changed, the function is no longer recognized as a constructor.

#### 4.1.4 Compiler Bugs

There are a number of known security bugs in various versions of the Solidity compiler. The requirements in this subsection ensure that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not trigger these bugs. The name of the requirement includes the `uid` first recorded for the bug in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\], as a key that can be used to find more information about the bug. \[<a href="index.html#bib-solidity-bugs" class="bibref" data-link-type="biblio" title="List of Known Bugs">solidity-bugs</a>\] describes the conventions used for the JSON-formatted list of bugs.

The requirements in this subsection are ordered according to the latest compiler versions that are vulnerable, to slightly simplify assessment given the compiler version in use. Implementing the Good Practice of the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes all requirements in this subsection.

Some compiler-related bugs are in the <a href="index.html#sec-level-2-compiler-bugs" class="sec-ref">4.2.5 Security Level [M] Compiler Bugs and Overriding Requirements</a> as <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirements, either because they are <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for requirements in this subsection, or because they are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements that already ensure that the bug cannot be triggered.

Some bugs were introduced in known versions, while others are assumed to have existed in all versions before they were fixed.

**\[S\] Compiler Bug SOL-2022-5 with `.push()`<a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a version of Solidity older than 0.8.15.

Until 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using code through `assembly()`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly).

**\[S\] Compiler Bug SOL-2022-3<a href="index.html#req-1-compiler-SOL-2022-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a version of Solidity between 0.6.9 and 0.8.13 (inclusive).

Compilers from 0.6.9 until it was fixed in 0.8.13 had a bug that incorrectly allowed internal or public calls to use a simpification only valid for external calls, treating `memory` and `calldata` as equivalent pointers.

See also the 17 May 2022 [security alert](https://blog.soliditylang.org/2022/05/17/data-location-inheritance-bug/).

**\[S\] Compiler Bug SOL-2022-2<a href="index.html#req-1-compiler-SOL-2022-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a version of Solidity between 0.6.9 and 0.8.13 (inclusive).

Compilers from 0.5.8 until it was fixed in 0.8.13 had a bug that meant a single-pass encoding and decoding of a nested array could read data beyond the `calldatasize()`.

See also the 17 May 2022 [security alert](https://blog.soliditylang.org/2022/05/17/calldata-reencode-size-check-bug/).

**\[S\] Compiler Bug SOL-2022-1<a href="index.html#req-1-compiler-SOL-2022-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use version 0.8.11 nor 0.8.12 of Solidity.

Solidity defines a set of types for variables known collectively as `bytesNN` or Fixed-length Variable types, that specify the length of the variable as a fixed number of bytes, following the pattern

- `bytes1`
- `bytes2`
- ...
- `bytes10`
- ...
- `bytes32`

Compilers from 0.8.11 and 0.8.12 had a bug that meant literal parameters were incorrectly encoded by `abi.encodeCall()` in certain circumstances.

See also the 16 March 2022 [security alert](https://blog.soliditylang.org/2022/03/16/encodecall-bug/).

**\[S\] Compiler Bug SOL-2021-4<a href="index.html#req-1-compiler-sol-2021-4" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *SHOULD* not use version 0.8.8 of Solidity.

Compiler version 0.8.8 had a bug that assigned a full 32 bytes of storage to custom types that did not need it. This can be misused to enable reading arbitrary storage, as well as causing errors if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> contains code compiled using different Compiler versions.

See also the 29 September 2021 [security alert](https://blog.soliditylang.org/2021/09/29/user-defined-value-types-bug/)

**\[S\] Compiler Bug SOL-2021-2<a href="index.html#req-1-compiler-SOL-2021-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory`, *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.4.16 and 0.8.3 (inclusive).

Version 0.4.16 introduced a bug, fixed in 0.8.4, that meant the ABIEncoderV2 incorrectly validated pointers when reading `memory` byte arrays, which could result in reading data beyond the array area due to an overflow error in calcuating pointers.

See also the 21 April 2021 [security alert](https://blog.soliditylang.org/2021/04/21/decoding-from-memory-bug/).

**\[S\] Compiler Bug SOL-2021-1<a href="index.html#req-1-compiler-SOL-2021-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the bytecode optimzier with a version of Solidity older than 0.8.3.

Compilers before 0.8.3 had an optimizer bug that meant keccak hashes, calculated for the same content but different lengths that were not multiples of 32 bytes incorrectly used the first value from cache instead of recalculating.

See also the 23 March 2021 [security alert](https://blog.soliditylang.org/2021/03/23/keccak-optimizer-bug/).

**\[S\] Compiler Bug SOL-2020-11-push<a href="index.html#req-1-compiler-SOL-2020-11-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array using `push()` *MUST NOT* a use version of Solidity older than 0.7.4.

Compilers before 0.7.4 had a bug that meant data would be packed after an empty array, and if the length of the array is subsequently extended by `push()`, that data would be readable from the array.

See also the 19 October 2020 [security alert](https://blog.soliditylang.org/2020/10/19/empty-byte-array-copy-bug/).

**\[S\] Compiler Bug SOL-2020-10<a href="index.html#req-1-compiler-SOL-2020-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an array of types shorter than 16 bytes to a longer array *MUST NOT* a use version of Solidity older than 0.7.3.

Compilers before 0.7.3 had a bug that meant when array data for types shorter than 16 bytes are assigned to a longer array, the extra values in that longer array are not correctly reset to zero.

See also the 7 October 2020 [security alert](https://blog.soliditylang.org/2020/10/07/solidity-dynamic-array-cleanup-bug).

**\[S\] Compiler Bug SOL-2020-9<a href="index.html#req-1-compiler-SOL-2020-9" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> *MUST NOT* use version 0.7.1 of Solidity.

Solidity version 0.7.1 introduced Free Functions \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\]: Functions that are defined in the source code of smart contract but outside the scope of the formal contract declaration. <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> have `internal` visibility, and the compiler "inlines" them to the contracts that call them. The solidity documentation explains that they are:

> executed in the context of a contract. They still have access to the variable this, can call other contracts, send them Ether and destroy the contract that called them, among other things. The main difference to functions defined inside a contract is that free functions do not have direct access to storage variables and functions not in their scope.
>
> <https://docs.soliditylang.org/en/latest/contracts.html#functions>

The 0.7.1 compiler did not correctly distinguish overlapping <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Function</a> declarations, meaning that the wrong function could be called.

See examples of a [passing contract](https://entethalliance.github.io/eta-registry/examples/SOL-2020-9-fail.sol) and a [failing contract](https://entethalliance.github.io/eta-registry/examples/SOL-2020-9-fail.sol) for this requirement.

**\[S\] Compiler Bug SOL-2020-8<a href="index.html#req-1-compiler-SOL-2020-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls internal library functions with calldata parameters called via `using for` *MUST NOT* use version 0.6.9 of Solidity.

The 0.6.9 compiler incorrectly copied calldata parameters passed to internal library functions passed with `using for` as if they were calling to external library functions, leading to stack corruption and an incorrect jump destination.

See also a github issue with [code example](https://github.com/ethereum/solidity/issues/9172).

**\[S\] Compiler Bug SOL-2020-6<a href="index.html#req-1-compiler-SOL-2020-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that accesses an array slice using an expression for the starting index that can evaluate to a value other than zero *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.6.0 and 0.6.7 (inclusive).

Compiler version 0.6.0 introduced a bug fixed in 0.6.8 that incorrectly calculated index offsets for the start of array slices, used in dynamic `calldata` types, when using the ABIEncoderV2.

**\[S\] Compiler Bug SOL-2020-7<a href="index.html#req-1-compiler-SOL-2020-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that passes a string literal containing two consecutive backslash ("\\) characters to an encoding function or an external call *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.5.14 and 0.6.7 (inclusive).

Compiler version 0.5.14 introduced a bug fixed in 0.6.8 that incorrectly encoded consecutive backslash characters in string literals when passing them to an external function, or an enncoding function, when using the ABIEncoderV2.

**\[S\] Compiler Bug SOL-2020-5<a href="index.html#req-1-compiler-SOL-2020-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines a contract that does not include a constructor but has a base contract that defines a constructor not defined as `payable` *MUST NOT* use a version of Solidity between 0.4.5 and 0.6.7 (inclusive), **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor).

Solidity version 0.4.5 introduced a check intended to result in contract creation reverting if value is passed to a constructor that is not explicitly marked as `payable`. If the constructor was inherited from a base instead of explicitly defined in the contract, this check did not function properly until version 0.6.8, meaning the creation would not revert as expected.

**\[S\] Compiler Bug SOL-2020-4<a href="index.html#req-1-compiler-SOL-2020-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes assignments to tuples tha

- have nested tuples, **or**
- include a pointer to an external function, **or**
- reference a dynamically sized `calldata` array

*MUST NOT* use a version of Solidity older than 0.6.4.

Solidity version 0.1.6 introduced a bug fixed in 0.6.5 that meant tuple assignments involving nested tuples, pointers to external functions, or references to dynamically sized `calldata` arrays were corrupted due to incorrectly calculating the number of stack slots.

**\[S\] Compiler Bug SOL-2020-3<a href="index.html#req-1-compiler-SOL-2020-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares arrays of size larger than 2^256-1 *MUST NOT* use a version of Solidity older than 0.6.5.

Compiler version 0.2.0 introduced a bug, fixed in version 0.6.5, that meant no overflow check was performed for the creation of very large arrays, meaning in some cases an overflow error would occur that would use result in consuming all gas in a transaction due to the memory handling error introduced in compiling the contract.

**\[S\] Compiler Bug SOL-2020-1<a href="index.html#req-1-compiler-SOL-2020-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares variables inside a `for` loop that contains a `break` or `continue` statement *MUST NOT* use the Yul Optimizer with version 0.6.0 nor a version of Solidity between 0.5.8 and 0.5.15 (inclusive).

A bug in the Yul Optimiser in versions from 0.5.8 to 0.5.15 and in version 0.6.0 meant assignments for variables declared inside a `for` loop that contained a `break` or `continue` statement could be removed.

**\[S\] Compiler Bug SOL-2020-11-length<a href="index.html#req-1-compiler-SOL-2020-11-length" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array by assigning the `length` attribute *MUST NOT* use a version of Solidity older than 0.6.0.

Compilers before 0.6.0 had a bug that meant data would be packed after an empty array, and if the length of the array were then extended by assigning the `length` attribute that data would be readable from the array. From version 0.6.0 it was no longer possible to extend an array by assigning the `length`, which became read-only.

See also the 19 October 2020 [security alert](https://blog.soliditylang.org/2020/10/19/empty-byte-array-copy-bug/), and an example [contract that fails this requirement](https://entethalliance.github.io/eta-registry/examples/SOL-2020-11-length-fail.sol)

**\[S\] Compiler Bug SOL-2019-10<a href="index.html#req-1-compiler-SOL-2019-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use the combination of all of

- the ABIEncoderV2
- the Optimizer
- the yulOptimizer
- version 0.5.14 of Solidity.

A bug in version 0.5.14 that required multiple compiler options to trigger could result in data corruption in storage.

**\[S\] Compiler Bugs SOL-2019-3,6,7,9<a href="index.html#req-1-compiler-SOL-2019-3679" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `struct` **or** arrays *MUST NOT* use the ABIEncoderV2 option with a version of Solidity between 0.4.16 and 0.5.10 (inclusive).

Compiler version 0.5.6 introduced bug SOL-2019-9 fixed in 0.5.11 that meant reading a `struct` through `calldata` which had dyamically encoded members that were statically sized resulted in corrupted data. Bugs SOL-2019-6 and SOL-2019-7 introduced in compiler 0.4.16 and fixed in compiler 0.5.9 and 0.5.10 respectively meant that data encoded in or read from a `struct` could be corrupted. Bug SOL-2019-3 from 0.4.19 to 0.4.25 and from 0.5.0 to 0.5.7 could corrupt data, both in the `struct` and other encoded data, when encoding a `struct`. All of these bugs were triggered by using the ABIEncoderV2.

See also the 26 March 2019 [security alert](https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/), and the 25 June 2019 [security alert](https://blog.soliditylang.org/2019/06/25/solidity-storage-array-bugs/).

**\[S\] Compiler Bug SOL-2019-8<a href="index.html#req-1-compiler-SOL-2019-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that assigns an array of signed integers to an array of a different type *MUST NOT* use a version of Solidity between 0.4.7 and 0.5.9 (inclusive).

Compiler version 0.4.7 introduced a bug fixed in 0.5.10 that meant assigning an array of signed integers to another array of different type corrupted negative values.

See also the 25 June 2019 [security alert](https://blog.soliditylang.org/2019/06/25/solidity-storage-array-bugs/).

**\[S\] Compiler Bug SOL-2019-5<a href="index.html#req-1-compiler-SOL-2019-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls an uninitialized internal function pointer in the constructor *MUST NOT* use a version between 0.4.5 and 0.4.25 (inclusive) nor a version between 0.5.0 and 0.5.7 (inclusive) of Solidity.

A bug in compilers versions 0.4.5 to 0.4.25 and versions 0.5.0 until fixed in 0.5.8 meant calls to unitialized function pointers in constructors did not revert as expected and as they do in deployed code.

**\[S\] Compiler Bug SOL-2019-4<a href="index.html#req-1-compiler-SOL-2019-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses events containing contract types, in libraries, *MUST NOT* use a version of Solitidy between 0.5.0 and 0.5.7.

Compiler version 0.5.0 introduced a bug fixed in 0.5.8 that meant an incorrect hash is logged if library events contain contract types.

**\[S\] Compiler Bug SOL-2019-2<a href="index.html#req-1-compiler-SOL-2019-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes index access to <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> types with a second parameter (not the index) whose compile-time value evaluates to 31 *MUST NOT* use the Optimizer with versions 0.5.5 nor 0.5.6 of Solitidy.

Version 0.5.5 introduced an Optimizer bug fixed in 0.5.7 where a second parameter value of "31" for a `byte` opcode resulted in unexpected values.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[S\] Compiler Bug SOL-2019-1<a href="index.html#req-1-compiler-SOL-2019-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that nests bitwise shifts to produce a total shift of more than 256 bits **and** compiles for the `Constantinople` or later <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version</a> *MUST NOT* use the Optimizer option with version 0.5.5 of Solidity.

Compiler version 0.5.5 introduced a bug fixed in 0.5.6 that meant nested bitwise shifts could be incorrectly optimized.

See also the 26 March 2019 [security alert](https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/).

**\[S\] Compiler Bug SOL-2018-4<a href="index.html#req-1-compiler-SOL-2018-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has a match for the regexp `[^/]\\*\\* *[^/0-9 ]` *MUST NOT* use a version of Solidity older than 0.4.25.

Compilers before 0.4.25 had a bug that meant exponents calculated using `**` with a type that is shorter than 256 bits, not shorter than the type of the base, and containing dirty higher order bits could produce an incorrect result.

See also the 13 September 2018 [security alert](https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/).

**\[S\] Compiler Bug SOL-2018-3<a href="index.html#req-1-compiler-SOL-2018-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a `struct` in events *MUST NOT* use a version of Solidity between 0.4.17 and 0.4.24 (inclusive).

Compilers from 0.4.17 until it was fixed in 0.4.25 had a bug that meant when events used `struct`s, the address of the `struct` was logged instead of the data.

See also the 13 September 2018 [security alert](https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/), and an example [contract that fails this requirement](https://entethalliance.github.io/eta-registry/examples/SOL-2018-3-fail.sol)

**\[S\] Compiler Bug SOL-2018-2<a href="index.html#req-1-compiler-SOL-2018-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls a function matching the regexp `returns[^;{]*\\[\\s*[^\\] \\t\\r\\n\\v\\f][^\\]]*\\]\\s*\\[\\s*[^\\] \\t\\r\\n\\v\\f][^\\]]*\\][^{;]*[;{]` *MUST NOT* use a version of Solidity older than 0.4.22.

Compilers between 0.1.4 and 0.4.21 incorrectly interpreted array values as memory pointers when a function that returns a fixed-size multidimensional array is called.

See also the 13 September 2018 [security alert](https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/).

**\[S\] Compiler Bug SOL-2018-1<a href="index.html#req-1-compiler-SOL-2018-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that both a new-style constructor (using the `constructor` keyword) and an old-style constructor (a function with the same name as the contract), which are not exactly the same *MUST NOT* use version 0.4.22 of Solidity.

Compiler version 0.4.22 had a bug that means it is unclear which constructor function is used.

It is unnecessary to use the old-style constructor in this case, and not using it avoids triggering the bug.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[S\] Explicit Constructors**](index.html#req-1-explicit-constructors) and [**\[M\] Declare Constructors Explicitly**](index.html#req-2-explicit-constructors).

**\[S\] Compiler Bug SOL-2017-5<a href="index.html#req-1-compiler-SOL-2017-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a function that is `payable` whose name consists only of any number of zeros ("0"), and does not have a fallback function, *MUST NOT* use a version of Solidity older than 0.4.18.

Compilers before 0.4.18 had a bug that meant such a function would be called instead of a fallback function if Ether is sent without data.

**\[S\] Compiler Bug SOL-2017-4<a href="index.html#req-1-compiler-SOL-2017-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `delegatecall()` instruction *MUST NOT* use a version of Solidity older than 0.4.15.

Compilers from 0.3.0 to 0.4.14 had a bug that meant if `delegateCall()` returned a value that started with 32 bytes of zeros, it would be read as `false` instead of `true`.

**\[S\] Compiler Bug SOL-2017-3<a href="index.html#req-1-compiler-SOL-2017-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `ecrecover()` pre-compile *MUST NOT* use a version of Solidity older than 0.4.14
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Validate `ecrecover()` Input**](index.html#req-2-validate-ecrecover-input).

Before version 0.4.14 Solidity had a bug that meant malformed input to the `ecrecover()` instruction could cause an unauthorised read of data in memory, without raising an exception or other signal that something had gone wrong.

**\[S\] Compiler Bug SOL-2017-2<a href="index.html#req-1-compiler-SOL-2017-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with functions that accept 2 or more parameters, of which any but the last are of <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type *MUST NOT* use a version of Solidity older than 0.4.12.

Compilers before 0.4.12 had a bug that meant when the empty string `""` was passed as a parameter value for a function that expected a <a href="index.html#dfn-fixed-length-variable" class="internalDFN" data-link-type="dfn">Fixed-length Variable</a>, the encoder simply ignored it, thus assigning subsequent arguments to the wrong parameter and corrupting the function call.

See an example [contractthat fails this requirement](https://entethalliance.github.io/eta-registry/examples/SOL-2017-2-fail.sol).

**\[S\] Compiler Bug SOL-2017-1<a href="index.html#req-1-compiler-SOL-2017-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains any number that **either** begins with `0xff` and ends with `00`, **or** begins with `0x00` and ends with `ff`, twice, **OR** uses such a number in the constructor, *MUST NOT* use the Optimizer with a version of Solidity older than 0.4.11.

The Optimizer for Compilers before 0.4.11 had a bug that meant certain numbers were corrupted by an attempt to optimise gas or constructor size.

See also the 3 May 2017 [security alert](https://blog.soliditylang.org/2017/05/03/solidity-optimizer-bug/).

**\[S\] Compiler Bug SOL-2016-11<a href="index.html#req-1-compiler-SOL-2016-11" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version older than 0.4.7 of Solidity *MUST NOT* call the Identity Contract **UNLESS** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Compiler Bug Check Identity Calls**](index.html#req-2-compiler-check-identity-calls).

Compilers before 0.4.7 had a bug that caused data corruption at jump destinations.

**\[S\] Compiler Bug SOL-2016-10<a href="index.html#req-1-compiler-SOL-2016-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use the Optimizer option with version 0.4.5 of Solidity.

Compiler version 0.4.5 had an Optimizer bug that caused data corruption at jump destinations.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Compiler Bug SOL-2016-4**](index.html#req-1-compiler-SOL-2016-4).

**\[S\] Compiler Bug SOL-2016-9<a href="index.html#req-1-compiler-SOL-2016-9" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that use variables of a type shorter than 17 bytes *MUST NOT* use a version of Solidity older than 0.4.4.

Compilers between 0.1.6 and 0.4.4 packed shorter data types in a way that potentially allowed the overwriting of variables.

See also [SWC-124](https://swcregistry.io/docs/SWC-124) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[S\] Compiler Bug SOL-2016-8<a href="index.html#req-1-compiler-SOL-2016-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `sha3()` instruction *MUST NOT* use the Optimizer option with a version of Solidity older than 0.4.3.

Compilers before 0.4.3 had a bug in the Optimizer that incorrectly cached some `sha3()` hashes. Note that the `sha3()` instruction is disallowed since version 0.5.0, replaced by the `keccak256()` instruction.

**\[S\] Compiler Bug SOL-2016-7<a href="index.html#req-1-compiler-SOL-2016-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `delegatecall()` from a function that can receive Ether to call a Library Function *MUST NOT* use versions 0.4.0 or 0.4.1 of Solidity.

Compilers 0.4.0 and 0.4.1 had a bug that incorrectly rejected Library Function calls made with `delegatecall()` from a function that had received Ether, interpreting it as an attempt to send Ether to the Library Function.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Compiler Bug SOL-2017-4**](index.html#req-1-compiler-SOL-2017-4), and note that meetng that requirement means this requirement will automatically be met.

**\[S\] Compiler Bug SOL-2016-6<a href="index.html#req-1-compiler-SOL-2016-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that sends Ether *MUST NOT* use a version of Solidity older than 0.4.0 **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">overriding requirement</a> [**\[M\] Compiler Bug No Zero Ether Send**](index.html#req-2-compiler-no-zero-ether-send).

Compilers before 0.4.0 had a bug that meant transactions that send Ether but with a zero value fail to provide gas, causing an exception.

**\[S\] Compiler Bug SOL-2016-5<a href="index.html#req-1-compiler-SOL-2016-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that creates a dynamically sized array with a `length` that can be zero *MUST NOT* use a version of Solidity older than 0.3.6.

Compilers before 0.3.6 had a bug that meant dynamically created arrays with a zero length created code that did not terminate, and consumed all gas.

**\[S\] Compiler Bug SOL-2016-4<a href="index.html#req-1-compiler-SOL-2016-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that creates a `Jump Destination` opcode *MUST NOT* use the Optimizer with versions of Solidity older than 0.3.6.

Compilers before 0.3.6 had an Optimizer bug that meant data corruption could occur due to incorrectly computing state at jump destinations.

**\[S\] Compiler Bug SOL-2016-3<a href="index.html#req-1-compiler-SOL-2016-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that compares the values of data of type <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> *MUST NOT* use a version of Solidity older than 0.3.3.

Compilers before 0.3.3 had a bug in the way they compared values of <a href="index.html#dfn-fixed-length-variable" class="internalDFN" data-link-type="dfn">Fixed-Length Variables</a> that meant the comparison would read higher-order bits beyond the size of the variable, and so could produce an incorrect result.

**\[S\] Compiler Bug SOL-2016-2<a href="index.html#req-1-compiler-SOL-2016-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses arrays, with data types whose size is less than 17 bytes *MUST NOT* use a version of Solidity older than 0.3.1.

Compilers before 0.3.1 incorrectly packed <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> shorter than 17 bytes in arrays, leading to data corruption.

**\[S\] No Ancient Compilers<a href="index.html#req-1-no-ancient-compilers" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.3.

Compiler bugs are not tracked for compiler versions older than 0.3. There is therefore a risk that unknown bugs create unexpected problems.

See also "SOL-2016-1" in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\].

### 4.2 Security Level \[M\]

<a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[M\] means that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> has been carefully reviewed by a human auditor or team, doing a "manual analysis", and important security issues have been addressed to their satisfaction.

This level includes a number of <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for cases when <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement directly, e.g. because it uses an uncommon feature that introduces higher risk, or because testing that the requirement has been met generally requires human judgement. Passing the relevant <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> tests that the feature has been implemented sufficiently well to satisfy the auditor that it does not expose the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to the known vulnerabilities identified in this Security Level.

**\[M\] Pass Security Level \[S\]<a href="index.html#req-2-pass-l1" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">4.1 Security Level [S]</a>.

**\[M\] No failing `assert` statements<a href="index.html#req-2-no-failing-asserts" class="selflink"></a>**
`assert()` statements in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* fail.

`assert` statements are meant for invariants, not as a generic error-handling mechanism. If an `assert` statement fails because it is being used as a mechanism to catch errors, it *SHOULD* be replaced with a `require` statement or similar mechanism designed for the use case. If it fails due to a coding bug, that needs to be fixed.

This requirement is based on \[<a href="index.html#bib-cwe-670" class="bibref" data-link-type="biblio" title="CWE-670: Always-Incorrect Control Flow Implementation">CWE-670</a>\] Always-Incorrect Control Flow Implementation.

#### 4.2.1 Text and homoglyph attacks

**\[M\] No Unnecessary Unicode Controls<a href="index.html#req-2-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characterss**](index.html#req-1-unicode-bdo).

<a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> permits the use of <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> in text strings, subject to analysis of whether they are necessary.

**\[M\] No Homoglyph-style Attack<a href="index.html#req-2-no-homoglyph-attack" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks if the impact is misleading.

Techniques such as substituting characters from different alphabets (e.g. Latin "a" and Cyrillic "а" are not the same). This can be used to mask malicious code, for example by presenting variables or function names designed to mislead auditors. These attacks are known as Homoglyph Attacks. Several approaches to successfully exploiting this issue are described in \[<a href="index.html#bib-ivanov" class="bibref" data-link-type="biblio" title="Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts">Ivanov</a>\].

In the rare case there is a valid use of characters from multiple Unicode blocks (see \[<a href="index.html#bib-unicode-blocks" class="bibref" data-link-type="biblio" title="Blocks-14.0.0.txt">unicode-blocks</a>\]) in a variable name or label (most likely to be mixing two languages in a name), requirements at this level allow them to pass EEA EthTrust certification so long as they do not mislead or confuse.

This level requires checking for homoglyph attacks including those within a single character set, such as the use of "í" in place of "i" or "ì", "ت" for "ث", or "1" for "l", and when a reviewer judges that the result is misleading or confusing, the relevant code does not meet the <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirements.

The requirements in this section are related to the security advisory \[<a href="index.html#bib-cve-2021-42574" class="bibref" data-link-type="biblio" title="National Vulnerability Database CVE-2021-42574">CVE-2021-42574</a>\] and \[<a href="index.html#bib-cwe-94" class="bibref" data-link-type="biblio" title="CWE-94: Improper Control of Generation of Code (&#39;Code Injection&#39;)">CWE-94</a>\], "Improper Control of Generation of Code", also called "Code Injection".

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a>: [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

#### 4.2.2 External Calls

**\[M\] Protect External Calls<a href="index.html#req-2-external-calls" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls:

- all contracts called *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, **and**
- all contracts called *MUST* be controlled by the same entity, **and**
- the protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

<a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> allows calling within a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">set of contracts</a> that form part of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. This ensures all contracts called are audited as a group at this Security Level. The same level of protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> is provided to the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> overall as for the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement.

**\[M\] Handle External Call Returns<a href="index.html#req-2-handle-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.

As well as checking that the calls return, it is important that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> "works" - to the satisfaction of the auditor - if the return value is the result of an error.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a>: [**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs), [**\[S\] Check External Calls Return**](index.html#req-1-check-return).

#### 4.2.3 Documenting Defensive Coding

**\[M\] Document Special Code Use<a href="index.html#req-2-documented" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* document the need for each instance of:

- `selfdestruct()` or its deprecated alias `suicide()`,
- `assembly()`,
- `CREATE2`,
- external calls,
- use of `block.number` or `block.timestamp`,
- Use of oracles and pseudo-randomness, **or**
- code that can cause an overflow or underflow,

**and** *MUST* describe how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, **and** the documentation *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of

- [**\[S\] No `Self-destruct`**](index.html#req-1-self-destruct).
- [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).
- [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

There are legitimate uses for all of these coding patterns, but they are also potential causes of security vulnerabilities. Requirements at Security Level M therefore require testing that ensures the use of these patterns is explained and justified, and that they are used in a manner that does not introduce known vulnerabilities.

The requirement to document the use of external calls applies to **all** external calls in the tested code, whether or not they meet the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related requirements</a>: [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), [**\[Q\] Verify External Calls**](index.html#req-3-external-calls), [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[M\] Protect Self-destruction<a href="index.html#req-2-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Self-destruct**](index.html#req-1-self-destruct).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, and steal any Ether held by the contract. In addition, this can disrupt other users of the contract since once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [\[Q\] Implement Access Control](https://entethalliance.github.io/eta-registry/security-levels-spec.html#req-3-access-control), and [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

This vulnerability led to the [Parity MultiSig Wallet Failure](https://www.parity.io/blog/parity-technologies-multi-sig-wallet-issue-update/) that blocked around 1/2 Million Ether on mainnet in 2017.

**\[M\] Avoid Common `assembly()` Attack Vectors<a href="index.html#req-2-safe-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly()` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

The `assembly()` instruction provides a low-level method for developers to produce code in smart contracts. Using this approach provides great flexibility and control, for example to reduce gas cost. However it also exposes some possible attack surfaces where a malicious coder could introduce attacks that are hard to detect. This requirement ensures that two such attack surfaces that are well-known are not exposed.

See also [SWC-124](https://swcregistry.io/docs/SWC-124) and [SWC-127](https://swcregistry.io/docs/SWC-127) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[M\] Protect `CREATE2` Calls<a href="index.html#req-2-protect-create2" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses the `CREATE2` instruction, any contract to be deployed using `CREATE2`

- *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* use any `selfdestruct()`, `delegatecall()` nor `callcode()` instructions, **and**
- *MUST* be fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

The `CREATE2` opcode's ability to interact with addresses whose code does not exist yet on-chain mandates protections to prevent external calls to malicous or insecure contract code that is not yet known.

The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> needs to include any code that can be deployed using `CREATE2` to verify protections are in place and the code behaves as the contract author claims. This includes ensuring opcodes that can change the immutability or forward calls in the contracts deployed with `CREATE2`, such as `selfdestruct()`, `delegatecall()` and `callcode()`, are not present.

If any of these opcodes are present, the additional protections and documentation required by the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> are necessary.

**\[M\] Declare `storage` Explicitly<a href="index.html#req-2-explicit-storage" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.5.0 *MUST* explicitly declare `storage` or `memory` for storage objects, and must justify the need for any `storage` item.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Explicit Storage**](index.html#req-1-explicit-storage).

Solidity's default way of providing uninitialised storage can be and has been exploited \[<a href="index.html#bib-storage-honeypots" class="bibref" data-link-type="biblio" title="Solidity Security: Comprehensive list of known attack vectors and common anti-patterns - section 14: Uninitialised Storage Pointers">storage-honeypots</a>\], because it can enable access to an unnitiatilized pointer \[<a href="index.html#bib-cwe-824" class="bibref" data-link-type="biblio" title="CWE-824: Access of Uninitialized Pointer">CWE-824</a>\]. This was addressed by checking that storage is explicitly declared, from version 0.5.0, but for older compilers it is important to test for this exploit.

**\[M\] No Overflow/Underflow<a href="index.html#req-2-overflow-underflow" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow).

There are a few rare use cases where arithmetic overflow or underflow is intended, or expected behaviour. It is important such cases are protected appropriately. Note that these are harder to implement since version 0.8.0 which introduced overflow protection that causes transactions to revert.

**\[M\] Declare Explicit Constructors<a href="index.html#req-2-explicit-constructors" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.22 *MUST* declare `constructor` methods explicitly.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Explicit Constructors**](index.html#req-1-explicit-constructors).

Versions of Solidity older than 0.4.22 allowed an "implicit" constructor: a function with the same name as the `contract`. Renaming a contract but not the function means that the function is no longer recognised as a constructor. This is an error that has been seen with copied source code.

For more information and examples of code that exploits this see the discussion in the [Constructors with Care](https://github.com/sigp/solidity-security-blog#constructors) section of \[<a href="index.html#bib-sigp" class="bibref" data-link-type="biblio" title="Solidity Security: Comprehensive List of Known Attack Vectors and Common Anti-Patterns">sigp</a>\] or [SWC-118](https://swcregistry.io/docs/SWC-118) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[M\] Document Name Conflicts<a href="index.html#req-2-safe-inheritance-order" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* clearly document the order of inheritance for each function or variable that shares a name with another function or variable.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Conflicting Inheritance**](index.html#req-1-inheritance-conflict).

As noted in [**\[S\] No Conflicting Inheritance**](index.html#req-1-inheritance-conflict). using the same name for different functions or variables can lead to reviewers misundersanding code, either inadvertently or deliberately as an attempt to hide malicious code. Explicitly documenting any occurrences of doing this helps security audits, and makes it clear to others using the code where they need to pay attention to the scope of variable or function declarations.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirement</a> [**\[M\] Compiler Bug SOL-2020-2**](index.html#req-2-compiler-SOL-2020-2), and the [documentation of function inheritance](https://docs.soliditylang.org/en/latest/contracts.html#inheritance) in \[<a href="index.html#bib-solidity-functions" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Functions">solidity-functions</a>\]

**\[M\] Sources of Randomness<a href="index.html#req-2-random-enough" class="selflink"></a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

This requirement involves careful evaluation for each specific contract and case. Some uses of randomness rely on no prediction being more accurate than any other. For such cases, values that can be guessed at with some accuracy or controlled by miners or validators, like block difficulty, timestamps, and/or block numbers, introduces a vulnerability. Thus a "strong" source of randomness like an oracle service is necessary.

Other uses are resistant to "good guesses" because using something that is close but wrong provides no more likelihood of gaining an advantage than any other guess.

For example a competition to guess the block number of a chain at a specific time, that rewards the answer closest to the correct answer is using a source of "randomness" that is vulnerable to approximate guessing.

On the other hand, for a lottery that will only pay if a number is submitted that exactly matches a winning entry in an offchain lottery to be held in the future, there is no advantage in being able to approximate the answer.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Don't misuse block data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[M\] Don't misuse block data<a href="index.html#req-2-block-data-misuse" class="selflink"></a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

Block numbers are vulnerable to approximate prediction, although they are generally not reliably precise indicators of elapsed time. `block.timestamp` is subject to manipulation by malicious actors. It is therefore important that these data are not trusted by <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to function as if they were highly reliable or random information.

The description of [SWC-116](https://swcregistry.io/docs/SWC-116) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] includes some code examples for techniques to avoid, for example using `block.number / 14` as a proxy for elapsed seconds, or relying on `block.timestamp` to indicate a precise time has passed.

For low precision, such as "a few minutes", `block.number / 14 > 1000` can be sufficient on main net, or a blockchain with a similar regular block period of around 14 seconds. But using it to determine that e.g. "exactly 36 seconds" have elapsed fails the requirement. A contract that relies on a specific block period can introduce serious risks if it is deployed on another blockchain with a very different block frequency.

Likewise, because block.timestamp depends on settings that can be manipulated by a malicious node operator, in cases likes Ethereum mainnet it is suitable for use as a coarse-grained approximation (on a scale of minutes) but the same code on a different blockchain can be vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks.

Note that this is related to the use of <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a>, which can also provide inaccurate information.

#### 4.2.4 Signature Managemen

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[M\] Proper Signature Verification<a href="index.html#req-2-signature-verification" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* use proper signature verification to ensure authenticity of messages that were signed off-chain, e.g. by using `ecrecover()`.

Some smart contracts process messages that were signed off-chain to increase flexibility, while maintaining authenticity. Smart contracts performing their own signature verification must ensure that they are correctly verifying message authenticity.

See also [SWC-122](https://swcregistry.io/docs/SWC-122) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

For code that does use `ecrecover()`, see the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] Compiler Bug SOL-2017-3**](index.html#req-1-compiler-SOL-2017-3) and [**\[M\] Validate `ecrecover()` input**](index.html#req-2-validate-ecrecover-input)

**\[M\] No Improper Usage of Malleable Signatures for Replay Attack Protection<a href="index.html#req-2-malleable-signatures-for-replay" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST NOT* rely on <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

In Replay Attacks, an attacker replays correctly signed messages to exploit a system. Malleable signatures allow an attacker to create a new signature for the same message. Smart contracts that check against hashes of signatures to ensure that a message has only been processed once may be vulnerable to replay attacks if malleable signatures are used.

#### 4.2.5 Security Level \[M\] Compiler Bugs and Overriding Requirements

Some solidity compiler bugs have <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>.

**\[M\] Compiler Bug SOL-2022-5 in `assembly()`<a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an `assembly()` instruction that reads that data without explicitly matching the length that was copied, *MUST NOT* use a version of Solidity older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

Until 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using `assembly()`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push), [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[M\] Compiler Bug SOL-2022-4<a href="index.html#req-2-compiler-SOL-2022-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly()` instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, and code in a another `assembly()` instruction refers to that memory, *MUST NOT* use the yulOptimizer with versions 0.8.13 or 0.8.14 of Solidity.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

Version 0.8.13 introduced a yulOptimizer bug fixed 0.8.15 in where memory created in an `assembly()` instruction but only read in a different `assembly()` instruction was discarded.

See also the [17 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/inline-assembly-memory-side-effects-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[M\] Compiler Bug SOL-2021-3<a href="index.html#req-2-compiler-SOL-2021-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly()` instruction *MUST NOT* use a version of Solidity between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

Compiler 0.6.8 introduced a bug, fixed in 0.8.9, that meant immutable signed integer types shorter than 256 bits could be read incorrectly in inline `assembly()` instructions.

See also the [29 September 2021 security alert](https://blog.soliditylang.org/2021/09/29/signed-immutables-bug/), and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Safe Use of `assembly()`**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), and [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

**\[M\] Compiler Bug Check Constructor Payment<a href="index.html#req-2-compiler-check-payable-constructor" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is

- defined in a base contract, **and**
- used by default in another contract without an explicit constructor, **and**
- not explicity marked `payable`,

*MUST NOT* use a version of Solidity between 0.4.5 and 0.6.7 (inclusive).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5).

Solidity versions from 0.4.5 set the expectation that payments to a constructor that was not expicitly denoted as `payable` would revert. But when the constructor is inherited from a base contract, this reversion does not happen in versions before 0.6.8.

**\[M\] Compiler Bug SOL-2020-2<a href="index.html#req-2-compiler-SOL-2020-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares multiple functions with the same name *MUST NOT* use a version of Solidity older than 0.5.17.

Compilers between 0.3.0 and 0.5.17 had a bug that allowed private method declarations to be overridden by declaring another function of the same name.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Conflicting Inheritance**](index.html#req-1-inheritance-conflict) and [**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order).

**\[M\] Compiler Bug SOL-2019-2 in `assembly()`<a href="index.html#req-2-compiler-SOL-2019-2-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the Optimizer with a version 0.5.5 nor 0.5.6 of Solitidy *MUST NOT* contain inline `assembly()` that uses the `byte` instruction with a second parameter whose compile-time value evaluates to 31.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

Version 0.5.5 introduced a bug fixed in 0.5.7 where a second parameter value of "31" for a `byte` opcode resulted in unexpected values.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[S\] Compiler Bug SOL-2019-2**](index.html#req-1-compiler-SOL-2019-2), [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Compiler Bug Check Identity Calls<a href="index.html#req-2-compiler-check-identity-calls" class="selflink"></a>**
In <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.7, calls to the Identity Contract *MUST* explicitly check the return value.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2016-11**](index.html#req-1-compiler-SOL-2016-11).

Calls to the Identity Contract ignored the return value before version 0.4.7.

**\[M\] Validate `ecrecover()` input<a href="index.html#req-2-validate-ecrecover-input" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `ecrecover()` pre-compile in a version of Solidity older than 0.4.14 *MUST* ensure that input is well-formed before making the call.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2017-3**](index.html#req-1-compiler-SOL-2017-3).

Prior to Solidity 0.4.14, bad input to `ecrecover()` could cause it to fail and produce corrupted data, while appearing to succeed.

**\[M\] Compiler Bug No Zero Ether Send<a href="index.html#req-2-compiler-no-zero-ether-send" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.0, *MUST NOT* make Ether transfers that can send a value of zero.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2016-6**](index.html#req-1-compiler-SOL-2016-6).

A bug fixed in Solidity version 0.4.0 meant that transactions that explicity send zero Ether would automatically cause an exception, due to insufficient gas being passed on.

### 4.3 Security Level \[Q\]

In addition to static testing verification (Level \[S\]) and a manual audit (Level \[M\]), <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[Q\] means the intended functionality of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is sufficently well documented that its functional correctness can be verified, and that the code and documentation has been thoroughly reviewed by a human auditor or audit team to ensure that they are both internally coherent and consistent with each other, as well as to eliminate complex security vulnerabilities.

This level of review is especially relevant for tokens, for example using ERC20 \[<a href="index.html#bib-erc20" class="bibref" data-link-type="biblio" title="EIP-20: Token Standard">ERC20</a>\].

At this Security Level there are also checks to ensure the code does not contain errors that do not directly impact security, but do impact code quality. Code is often copied, so <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> code needs to be as well-written as possible. The risk being addressed is that it is easy and not uncommon to introduce weaknesses by copying existing code as a starting point.

**\[Q\] Pass Security Level \[M\]<a href="index.html#req-3-pass-l2" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">4.2 Security Level [M]</a>.

**\[Q\] Code Linting<a href="index.html#req-3-linted" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert` statements, **and**
- *MUST* explicitly declare the visibility of all functions and variables.

Code is often copied from "good examples" as a starting point for development. Code that has achieved <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is meant to be high quality, so it is important to ensure that copying it does not encourage bad habits. It is also helpful for review to remove pointless code.

Code designed to trap unexpected errors, such as `assert()` instructions, are explicitly allowed because it would be very unfortunate if defensively written code that successfully eliminates the possibility of triggering a particular error could not achieve <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

**\[Q\] Manage Gas Use Increases<a href="index.html#req-3-enough-gas" class="selflink"></a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

Some structures such as arrays can grow, and the value of variables is (by design) variable. Iterating over a structure whose size is not clear in advance, whether an array that grows, a bound that changes, or something determined by an external value, can result in significant increases in gas usage.

What is reasonable growth to expect needs to be considered in the context of the business logic intended, and how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against <a href="index.html#dfn-gas-griefing" class="internalDFN" data-link-type="dfn">Gas Griefing</a> attacks, where malicious actors or errors result in values occurring beyond the expected reasonable range(s).

See also [SWC-126](https://swcregistry.io/docs/SWC-126), [SWC-128](https://swcregistry.io/docs/SWC-128) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[Q\] Protect against Front-Running<a href="index.html#req-3-block-front-running" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* require information in a form that can be used to enable a <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attack.

In front-running attacks, an attacker places their transaction in front of a victim's. This can be done by a malicious miner or by an attacker monitoring the mempool and preempting susceptible transactions by broadcasting their own transactions with higher transaction fees. Any smart contracts where an attacker would be incentivized to front-run should apply mitigations such as hash commitment schemes or batch execution.

**\[Q\] Protect against MEV Attacks<a href="index.html#req-3-block-mev" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

<a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> refers to the potential that a block producer can maliciously reorder or suppress transactions, or another participant in a blockchain can propose a transaction or take other action to gain a benefit that was not intended to be available to them.

This requirement entails a careful judgement by the auditor, of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks, and what mitigation strategies are appropriate. Some approaches are discussed further in <a href="index.html#sec-mev-considerations" class="sec-ref">3.6 MEV (Maliciously Extracted Value)</a>.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), and [**\[M\] Don't misuse block data**](index.html#req-2-block-data-misuse).

**\[Q\] Process All Inputs<a href="index.html#req-3-all-valid-inputs" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

Code that fails to validate inputs runs the risk of being subverted through maliciously crafted input that can trigger a bug, or behaviour the authors did not anticipate.

See also [SWC-123](https://swcregistry.io/docs/SWC-123) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] which notes that it is important to consider whether input requirements are too strict, as well as too lax, \[<a href="index.html#bib-cwe-573" class="bibref" data-link-type="biblio" title="CWE-573: Improper Following of Specification by Caller">CWE-573</a>\] Improper Following of Specification by Caller, and note that there are several <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> that are specific to particular compiler versions in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">4.1.4 Compiler Bugs</a>.

**\[Q\] State Changes Trigger Events<a href="index.html#req-3-event-on-state-change" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

Events are convenience interfaces that give an abstraction on top of the EVM's logging functionality. Applications can subscribe and listen to these events through the RPC interface of an Ethereum client. See more at \[<a href="index.html#bib-solidity-events" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Events">solidity-events</a>\].

Events are generally expected to be used for logging all state changes as they are not just useful for off-chain applications but also security monitoring and debugging. Logging all state changes in a contract ensures that any developers interacting with the contract are made aware of every state change as part of the ABI and can understand expected behavior through event annotations, as per [**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate).

**\[Q\] No Private Data<a href="index.html#req-3-no-private-data" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain

This is a <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> requirement primarily because the question of what is private data often requires careful and thoughtful assessment and a reasoned understanding of context. In general, this is likely to include an assessment of how the data is gathered, and what the providers of data are told about the usage of the information.

Private data is used in this specification to refer to information that should not be generally available to the public. For example, an individual's home telephone number is generally private data, while a customer enquiries telephone number is generally not private data. Similarly, information identifying a person's account is normally private data, but there are circumstances where it is public data. In such cases that public data can be recorded on-chain in conformance with this requirement.

Warning

PLEASE NOTE: In some cases regulation such as the \[<a href="index.html#bib-gdpr" class="bibref" data-link-type="biblio" title="Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016         on the protection of natural persons with regard to the processing of personal data         and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)         (Text with EEA relevance)">GDPR</a>\] imposes formal legal requirements on some private data. However, performing a test for this requirement results in an expert technical opinion on whether data that the auditor considers private is exposed. A statement about whether <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets this requirement does not represent any form of legal advice or opinion, attorney representation, or the like.

#### 4.3.1 Documentation requirements

<a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> conformance requires a detailed description of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is **intended** to behave. Alongside detailed testing requirements to check that it does behave as described wth regard to specific known vulnerabililies, it is important that the claims made for it are accurate. This requirement underpins a Good Practice, that it fulfils claims made for it outside audit-specific documentation.

The combination of these requirements helps ensure there is no malicious code, such as malicious "back doors" or "time bombs" hidden in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Since there are legitimate use cases for code that behaves as e.g. a time bomb, or "phones home", this combination helps ensure that testing focuses on real problems.

The requirements in this section extend the coverage required to meet the <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirement [**\[M\] Document Special Code Use**](index.html#req-2-documented). As with that requirement, there are multiple requirements that require the documentation to perform an audit at this level.

**\[Q\] Document Contract Logic<a href="index.html#req-3-documented" class="selflink"></a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

Contract Logic documented in a human-readable format and with enough detail that functional correctness and safety assumptions for special code use can be validated by auditors helps them assess complex code more efficiently and with higher confidence.

**\[Q\] Document System Architecture<a href="index.html#req-3-document-system" class="selflink"></a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

System documentation provides auditor(s) information to understand security assumptions and ensure functional correctness. It is recommended that system documentation be included or referenced in the README file of the code repository alongside documentation for how the source code can be tested, built and deployed.

**\[Q\] Annotate Code with NatSpec<a href="index.html#req-3-annotate" class="selflink"></a>**
All public interfaces contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation.">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

Inline comments are important to ensure that developers and auditors understand the intent behind each function and other code components. Public interfaces should be interpreted as anything that would be contained in the ABI of the compiled <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>. It is also recommended to use inline comments for private or internal functions that implement sensitive and/or complex logic.

Following the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation.">NatSpec</a>\] format allows these inline comments to be understood by the Solidity compiler for extracting them into a machine-readable format that may be used by other third-party tools for security assessments and automatic documentation. This may also be used to generate specifications that fully or partially satisfy the Requirement to [**\[Q\] Document Contract Logic**](index.html#req-3-documented)

**\[Q\] Implement as Documented<a href="index.html#req-3-implement-as-documented" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

The requirements at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> to provide documentation are important. However, it is also crucial that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> actually behaves as documented. If it does not, it is possible that this reflects insufficient care and that the code is also vulnerable due to bugs that were missed in implementation. It is also possible that the difference is an attempt to hide malicious code in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

#### 4.3.2 Access Control

**\[Q\] Implement Access Control<a href="index.html#req-3-access-control" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* implement appropriate access control mechanisms, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

There are several common methods to implement access control, such as Role-Based Access Control \[<a href="index.html#bib-rbac" class="bibref" data-link-type="biblio" title="INCITS 359-2012: Information Technology - Role Based Access Control">RBAC</a>\], and bespoke access control is often implemented for a given use case. Using industry-standard methods can help simplify the process of auditing, But is not sufficient to determine that there are no risks arising either from errors in implementation or due to a maliciously-crafted contract.

It is particularly important that appropriate access control applies to payments, as noted in [SWC-105](https://swcregistry.io/docs/SWC-105), but other actions such as overwriting data as described in [SWC-124](https://swcregistry.io/docs/SWC-126), or changing specific access controls, also need to be appropriately protected \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\]. This requirement matches \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\] Improper Access Control.

See also "[Access Restriction](https://fravoll.github.io/solidity-patterns/access_restriction.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\].

**\[Q\] Verify External Calls<a href="index.html#req-3-external-calls" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

At <a href="index.html#sec-levels-three" class="sec-ref">4.3 Security Level [Q]</a><a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> auditors have a lot of flexibility to offer <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for different uses of External Calls. Because <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> are such a well-known security vulnerability, well-known implementation patterns are generally easier to verify.

See also the related requirements [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and** [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

**\[Q\] Verify `tx.origin` Usage<a href="index.html#req-3-verify-tx.origin" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

`tx.origin` can be used to enable phishing attacks, tricking a user into interacting with a contract that gains access to all the funds in their account. It is generally the wrong choice for authorization of a caller for which `msg.sender` is the safer choice.

See also <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Implement Access Control**](index.html#req-3-access-control), the [section "`tx.origin`"](https://docs.soliditylang.org/en/latest/security-considerations.html?highlight=tx.origin) in Solidity Security Considerations \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], and CWE 284: Improper Access Control \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\].

### 4.4 Recommended Good Practices

This section describes good practices that require substantial human judgement to evaluate, or where a poor implementation can reduce rather than increase the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Testing for, and meeting these requirements does not directly affect conformance.

**\[GP\] Check For and Address New Security Bugs<a href="index.html#req-R-check-new-bugs" class="selflink"></a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 15 July 2022 and address them.

This specification was written between April 2021 and July 2022. New vulnerabilities are discovered from time to time, on an unpredictable schedule.

Checking for security alerts published too late to be incorporated into the current version of this document is an important technique for maintaining the highest possible security.

There are other sources of information on new security vulnerabilities, from \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\] to following the blogs of many security-oriented organizations such as those that contributed to this specification.

**\[GP\] Meet As Many Requirements As Possible<a href="index.html#req-R-meet-all-possible" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

While meeting some requirements for a higher <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> Security Level makes no change to the formal conformance of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, each requirement is specified because meeting it provides protection against specific known attacks. If it is possible to meet a particular requirement that is not necessary for conformance at the Security Level being tested, meeting that requirement will improve the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and is therefore worth doing.

**\[GP\] Use Latest Compiler<a href="index.html#req-R-use-latest-compiler" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable version of the Solidity compiler.

The Solidity compiler is regularly updated to improve performance but also specifically to fix security vulnerabilities that are discovered. There are many requirements in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">4.1.4 Compiler Bugs</a> that are related to vulnerabilities known at the time this specification was written, as well as enhancements made to provide better security by default. In general, newer versions of the compiler improve security, so unless there is a specific known reason not to do so, using the latest version available will result in better security.

**\[GP\] Write clear, legible Solidity code<a href="index.html#req-R-clean-code" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

There are no strict rules defining how to write clear code. It is important to use sufficiently descriptive names, comment code appropriately, and use structures that are easy to understand without causing the code to become excessively large because that also makes it difficult to read and understand.

Excessive nesting, unstructured comments, complex looping structures, and the use of very terse names for variables and functions are examples of coding styles that can also make code harder to understand.

It is important to note that in some cases, developers can sacrifice easy reading for other benefits such as reducing gas costs - this can be mitigated somewhat by comments in the code.

This Good Practice extends somewhat the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Code Linting**](index.html#req-3-linted), but judgements about how to meet it are necessarily more subjective than in the specifics that requirement establishes. Those looking for additional guidance on code styling can refer to the \[<a href="index.html#bib-solidity-style-guide" class="bibref" data-link-type="biblio" title="Solidity Style Guide - Solidity Documentation.">Solidity-Style-Guide</a>\].

**\[GP\] Follow Accepted ERC Standards<a href="index.html#req-R-follow-erc-standards" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case. An ERC is a category of \[<a href="index.html#bib-eip" class="bibref" data-link-type="biblio" title="EIP-1: EIP Purpose and Guidelines">EIP</a>\] (Ethereum Improvement Proposal) that defines application-level standards and conventions, including smart contract standards such as token standards (EIP-20) and name registries (EIP-137).

While following ERC standards will not inherently make Solidity code secure, they do enable developers to integrate with common interfaces and follow known conventions for expected behavior. If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does claim to follow a given ERC, its functional correctness in conforming to that standard can be verified by auditors.

**\[GP\] Define a Software License<a href="index.html#req-R-define-license" class="selflink"></a>** The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license, which is commonly open-source for Solidity code deployed to public networks. A software license provides legal guidance on how contributors and users can interact with the code, including auditors and whitehats.

It is important to choose a \[<a href="index.html#bib-software-license" class="bibref" data-link-type="biblio" title="Choosing an Open Source License">software-license</a>\] that best addresses the needs of the project, and clearly link to it throughout the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and documentation, e.g. using a prominent LICENSE file in the code repository, and referencing it from each source file.

**\[GP\] Disclose New Vulnerabilities Responsibly<a href="index.html#req-R-notify-news" class="selflink"></a>** Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">1.4 Feedback and new vulnerabilities</a>.

New security vulnerabilities are discovered from time to time. It helps the efforts to revise this specification to ensure the Working Group is aware of new vulnerabilities, or new knowledge regarding existing known vulnerabilities.

The EEA has agreed to manage a specific email address for such notifications - and if that changes, to update this specification accordingly.

## A. Additional Information

### A.1 Defined Terms

The following is a list of terms defined in this Specification.

- <a href="index.html#dfn-back-running" id="dfnanchor-0">back-running</a>
- <a href="index.html#dfn-checks-effects-interactions" id="dfnanchor-2">checks-effects-interactions</a>
- <a href="index.html#dfn-eea-ethtrust-certification" id="dfnanchor-3">eea ethtrust certification</a>
- <a href="index.html#dfn-evm-version" id="dfnanchor-4">evm versions</a>
- <a href="index.html#dfn-execution-contract" id="dfnanchor-5">execution contract</a>
- <a href="index.html#dfn-fixed-length-variable" id="dfnanchor-6">fixed-length variable</a>
- <a href="index.html#dfn-free-functions" id="dfnanchor-7">free functions</a>
- <a href="index.html#dfn-front-running" id="dfnanchor-8">front-running</a>
- <a href="index.html#dfn-gas-griefing" id="dfnanchor-9">gas griefing</a>
- <a href="index.html#dfn-homoglyph-attacks" id="dfnanchor-10">homoglyph attacks</a>
- <a href="index.html#dfn-low-level-call-functions" id="dfnanchor-12">low-level call functions</a>
- <a href="index.html#dfn-malleable-signatures" id="dfnanchor-13">malleable signatures</a>
- <a href="index.html#dfn-mev" id="dfnanchor-14">mev</a>
- <a href="index.html#dfn-hard-fork" id="dfnanchor-15">network upgrade</a>
- <a href="index.html#dfn-oracles" id="dfnanchor-16">oracles</a>
- <a href="index.html#dfn-overriding-requirement" id="dfnanchor-17">overriding requirements</a>
- <a href="index.html#dfn-private-data" id="dfnanchor-18">private data</a>
- <a href="index.html#dfn-proxy-contract" id="dfnanchor-19">proxy contract</a>
- <a href="index.html#dfn-re-entrancy-attacks" id="dfnanchor-20">re-entrancy attacks</a>
- <a href="index.html#dfn-related-requirements" id="dfnanchor-21">related requirements</a>
- <a href="index.html#dfn-sandwich-attacks" id="dfnanchor-22">sandwich attacks</a>
- <a href="index.html#dfn-security-level-m" id="dfnanchor-23">security level [m]</a>
- <a href="index.html#dfn-security-level-q" id="dfnanchor-24">security level [q]</a>
- <a href="index.html#dfn-security-level-s" id="dfnanchor-25">security level [s]</a>
- <a href="index.html#dfn-security-levels" id="dfnanchor-26">security levels</a>
- <a href="index.html#dfn-set-of-contracts" id="dfnanchor-27">set of contracts</a>
- <a href="index.html#dfn-sets-of-overriding-requirements" id="dfnanchor-28">set of overriding requirements</a>
- <a href="index.html#dfn-tested-code" id="dfnanchor-29">tested code</a>
- <a href="index.html#dfn-timing-attacks" id="dfnanchor-30">timing attacks</a>
- <a href="index.html#dfn-unicode-direction-control-characters" id="dfnanchor-31">unicode direction control characters</a>
- <a href="index.html#dfn-upgradable-contract" id="dfnanchor-32">upgradable contract</a>
- <a href="index.html#dfn-valid-conformance-claim" id="dfnanchor-33">valid conformance claim</a>

### A.2 Summary of Requirements

This section provides a summary of all requirements in this Specification.

[**\[S\] No `CREATE2`**](index.html#req-1-no-create2)**<a href="index.html#req-1-no-create2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction.
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

[**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin)**<a href="index.html#req-1-no-tx.origin" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` usage**](index.html#req-3-verify-tx.origin)

[**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check)**<a href="index.html#req-1-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable.

[**\[S\] No Conflicting Inheritance**](index.html#req-1-inheritance-conflict)**<a href="index.html#req-1-inheritance-conflict" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* include more than one variable, or operative function with different code, with the same name
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order).

[**\[S\] No Hashing Consecutive Variable Length Arguments**](index.html#req-1-no-hashing-consecutive-variable-length-args)**<a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

[**\[S\] No Self-destruct**](index.html#req-1-self-destruct)**<a href="index.html#req-1-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] No `assembly()`**](index.html#req-1-no-assembly)**<a href="index.html#req-1-no-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly).

[**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo)**<a href="index.html#req-1-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the [Unicode Direction Control Characters](index.html#dfn-unicode-direction-control-characters) `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

[**\[S\] Check External Calls Return**](index.html#req-1-check-return)**<a href="index.html#req-1-check-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call`, `delegatecall`, `staticcall`, `send`, and `transfer`) *MUST* check the returned value from each usage to determine whether the call failed.

[**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i)**<a href="index.html#req-1-use-c-e-i" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented)

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall)**<a href="index.html#req-1-delegatecall" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Protect External Calls**](index.html#req-2-external-calls).
**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow)**<a href="index.html#req-1-overflow-underflow" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.8.0
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] Explicit Storage**](index.html#req-1-explicit-storage)**<a href="index.html#req-1-explicit-storage" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.5.0
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Declare `storage` Explicitly**](index.html#req-2-explicit-storage).

[**\[S\] Explicit Constructors**](index.html#req-1-explicit-constructors)**<a href="index.html#req-1-explicit-constructors" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.4.22
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>: [**\[M\] Declare Constructors Explicitly**](index.html#req-2-explicit-constructors).

[**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push)**<a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an empty `.push()` instruction that writes to the resulting array, *MUST NOT* use a version of Solidity older than 0.8.15.

[**\[S\] Compiler Bug SOL-2022-3**](index.html#req-1-compiler-SOL-2022-3)**<a href="index.html#req-1-compiler-SOL-2022-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a version of Solidity between 0.6.9 and 0.8.13 (inclusive).

[**\[S\] Compiler Bug SOL-2022-2**](index.html#req-1-compiler-SOL-2022-2)**<a href="index.html#req-1-compiler-SOL-2022-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a version of Solidity between 0.6.9 and 0.8.13 (inclusive).

[**\[S\] Compiler Bug SOL-2022-1**](index.html#req-1-compiler-SOL-2022-1)**<a href="index.html#req-1-compiler-SOL-2022-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use version 0.8.11 nor 0.8.12 of Solidity.

[**\[S\] Compiler Bug SOL-2021-4**](index.html#req-1-compiler-sol-2021-4)**<a href="index.html#req-1-compiler-sol-2021-4" class="selflink"></a>** <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *SHOULD* not use version 0.8.8 of Solidity.

[**\[S\] Compiler Bug SOL-2021-2**](index.html#req-1-compiler-SOL-2021-2)**<a href="index.html#req-1-compiler-SOL-2021-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory`, *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.4.16 and 0.8.3 (inclusive).

[**\[S\] Compiler Bug SOL-2021-1**](index.html#req-1-compiler-SOL-2021-1)**<a href="index.html#req-1-compiler-SOL-2021-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the bytecode optimzier with a version of Solidity older than 0.8.3.

[**\[S\] Compiler Bug SOL-2020-11-push**](index.html#req-1-compiler-SOL-2020-11-push)**<a href="index.html#req-1-compiler-SOL-2020-11-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array using `push()` *MUST NOT* a use version of Solidity older than 0.7.4.

[**\[S\] Compiler Bug SOL-2020-10**](index.html#req-1-compiler-SOL-2020-10)**<a href="index.html#req-1-compiler-SOL-2020-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an array of types shorter than 16 bytes to a longer array *MUST NOT* a use version of Solidity older than 0.7.3.

[**\[S\] Compiler Bug SOL-2020-9**](index.html#req-1-compiler-SOL-2020-9)**<a href="index.html#req-1-compiler-SOL-2020-9" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines <a href="index.html#dfn-free-functions" class="internalDFN" data-link-type="dfn">Free Functions</a> *MUST NOT* use version 0.7.1 of Solidity.

[**\[S\] Compiler Bug SOL-2020-8**](index.html#req-1-compiler-SOL-2020-8)**<a href="index.html#req-1-compiler-SOL-2020-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls internal library functions with calldata parameters called via `using for` *MUST NOT* use version 0.6.9 of Solidity.

[**\[S\] Compiler Bug SOL-2020-6**](index.html#req-1-compiler-SOL-2020-6)**<a href="index.html#req-1-compiler-SOL-2020-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that accesses an array slice using an expression for the starting index that can evaluate to a value other than zero *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.6.0 and 0.6.7 (inclusive).

[**\[S\] Compiler Bug SOL-2020-7**](index.html#req-1-compiler-SOL-2020-7)**<a href="index.html#req-1-compiler-SOL-2020-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that passes a string literal containing two consecutive backslash ("\\) characters to an encoding function or an external call *MUST NOT* use the ABIEncoderV2 with a version of Solidity between 0.5.14 and 0.6.7 (inclusive).

[**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5)**<a href="index.html#req-1-compiler-SOL-2020-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that defines a contract that does not include a constructor but has a base contract that defines a constructor not defined as `payable` *MUST NOT* use a version of Solidity between 0.4.5 and 0.6.7 (inclusive), **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor).

[**\[S\] Compiler Bug SOL-2020-4**](index.html#req-1-compiler-SOL-2020-4)**<a href="index.html#req-1-compiler-SOL-2020-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes assignments to tuples tha

- have nested tuples, **or**
- include a pointer to an external function, **or**
- reference a dynamically sized `calldata` array

*MUST NOT* use a version of Solidity older than 0.6.4.

[**\[S\] Compiler Bug SOL-2020-3**](index.html#req-1-compiler-SOL-2020-3)**<a href="index.html#req-1-compiler-SOL-2020-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares arrays of size larger than 2^256-1 *MUST NOT* use a version of Solidity older than 0.6.5.

[**\[S\] Compiler Bug SOL-2020-1**](index.html#req-1-compiler-SOL-2020-1)**<a href="index.html#req-1-compiler-SOL-2020-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares variables inside a `for` loop that contains a `break` or `continue` statement *MUST NOT* use the Yul Optimizer with version 0.6.0 nor a version of Solidity between 0.5.8 and 0.5.15 (inclusive).

[**\[S\] Compiler Bug SOL-2020-11-length**](index.html#req-1-compiler-SOL-2020-11-length)**<a href="index.html#req-1-compiler-SOL-2020-11-length" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies an empty byte array to storage, and subsequently increases the size of the array by assigning the `length` attribute *MUST NOT* use a version of Solidity older than 0.6.0.

[**\[S\] Compiler Bug SOL-2019-10**](index.html#req-1-compiler-SOL-2019-10)**<a href="index.html#req-1-compiler-SOL-2019-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use the combination of all of

- the ABIEncoderV2
- the Optimizer
- the yulOptimizer
- version 0.5.14 of Solidity.

[**\[S\] Compiler Bugs SOL-2019-3,6,7,9**](index.html#req-1-compiler-SOL-2019-3679)**<a href="index.html#req-1-compiler-SOL-2019-3679" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `struct` **or** arrays *MUST NOT* use the ABIEncoderV2 option with a version of Solidity between 0.4.16 and 0.5.10 (inclusive).

[**\[S\] Compiler Bug SOL-2019-8**](index.html#req-1-compiler-SOL-2019-8)**<a href="index.html#req-1-compiler-SOL-2019-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that assigns an array of signed integers to an array of a different type *MUST NOT* use a version of Solidity between 0.4.7 and 0.5.9 (inclusive).

[**\[S\] Compiler Bug SOL-2019-5**](index.html#req-1-compiler-SOL-2019-5)**<a href="index.html#req-1-compiler-SOL-2019-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls an uninitialized internal function pointer in the constructor *MUST NOT* use a version between 0.4.5 and 0.4.25 (inclusive) nor a version between 0.5.0 and 0.5.7 (inclusive) of Solidity.

[**\[S\] Compiler Bug SOL-2019-4**](index.html#req-1-compiler-SOL-2019-4)**<a href="index.html#req-1-compiler-SOL-2019-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses events containing contract types, in libraries, *MUST NOT* use a version of Solitidy between 0.5.0 and 0.5.7.

[**\[S\] Compiler Bug SOL-2019-2**](index.html#req-1-compiler-SOL-2019-2)**<a href="index.html#req-1-compiler-SOL-2019-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes index access to <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> types with a second parameter (not the index) whose compile-time value evaluates to 31 *MUST NOT* use the Optimizer with versions 0.5.5 nor 0.5.6 of Solitidy.

[**\[S\] Compiler Bug SOL-2019-1**](index.html#req-1-compiler-SOL-2019-1)**<a href="index.html#req-1-compiler-SOL-2019-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that nests bitwise shifts to produce a total shift of more than 256 bits **and** compiles for the `Constantinople` or later <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version</a> *MUST NOT* use the Optimizer option with version 0.5.5 of Solidity.

[**\[S\] Compiler Bug SOL-2018-4**](index.html#req-1-compiler-SOL-2018-4)**<a href="index.html#req-1-compiler-SOL-2018-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has a match for the regexp `[^/]\\*\\* *[^/0-9 ]` *MUST NOT* use a version of Solidity older than 0.4.25.

[**\[S\] Compiler Bug SOL-2018-3**](index.html#req-1-compiler-SOL-2018-3)**<a href="index.html#req-1-compiler-SOL-2018-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a `struct` in events *MUST NOT* use a version of Solidity between 0.4.17 and 0.4.24 (inclusive).

[**\[S\] Compiler Bug SOL-2018-2**](index.html#req-1-compiler-SOL-2018-2)**<a href="index.html#req-1-compiler-SOL-2018-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that calls a function matching the regexp `returns[^;{]*\\[\\s*[^\\] \\t\\r\\n\\v\\f][^\\]]*\\]\\s*\\[\\s*[^\\] \\t\\r\\n\\v\\f][^\\]]*\\][^{;]*[;{]` *MUST NOT* use a version of Solidity older than 0.4.22.

[**\[S\] Compiler Bug SOL-2018-1**](index.html#req-1-compiler-SOL-2018-1)**<a href="index.html#req-1-compiler-SOL-2018-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that both a new-style constructor (using the `constructor` keyword) and an old-style constructor (a function with the same name as the contract), which are not exactly the same *MUST NOT* use version 0.4.22 of Solidity.

[**\[S\] Compiler Bug SOL-2017-5**](index.html#req-1-compiler-SOL-2017-5)**<a href="index.html#req-1-compiler-SOL-2017-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a function that is `payable` whose name consists only of any number of zeros ("0"), and does not have a fallback function, *MUST NOT* use a version of Solidity older than 0.4.18.

[**\[S\] Compiler Bug SOL-2017-4**](index.html#req-1-compiler-SOL-2017-4)**<a href="index.html#req-1-compiler-SOL-2017-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `delegatecall()` instruction *MUST NOT* use a version of Solidity older than 0.4.15.

[**\[S\] Compiler Bug SOL-2017-3**](index.html#req-1-compiler-SOL-2017-3)**<a href="index.html#req-1-compiler-SOL-2017-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `ecrecover()` pre-compile *MUST NOT* use a version of Solidity older than 0.4.14
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Validate `ecrecover()` Input**](index.html#req-2-validate-ecrecover-input).

[**\[S\] Compiler Bug SOL-2017-2**](index.html#req-1-compiler-SOL-2017-2)**<a href="index.html#req-1-compiler-SOL-2017-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with functions that accept 2 or more parameters, of which any but the last are of <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type *MUST NOT* use a version of Solidity older than 0.4.12.

[**\[S\] Compiler Bug SOL-2017-1**](index.html#req-1-compiler-SOL-2017-1)**<a href="index.html#req-1-compiler-SOL-2017-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains any number that **either** begins with `0xff` and ends with `00`, **or** begins with `0x00` and ends with `ff`, twice, **OR** uses such a number in the constructor, *MUST NOT* use the Optimizer with a version of Solidity older than 0.4.11.

[**\[S\] Compiler Bug SOL-2016-11**](index.html#req-1-compiler-SOL-2016-11)**<a href="index.html#req-1-compiler-SOL-2016-11" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version older than 0.4.7 of Solidity *MUST NOT* call the Identity Contract **UNLESS** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Compiler Bug Check Identity Calls**](index.html#req-2-compiler-check-identity-calls).

[**\[S\] Compiler Bug SOL-2016-10**](index.html#req-1-compiler-SOL-2016-10)**<a href="index.html#req-1-compiler-SOL-2016-10" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use the Optimizer option with version 0.4.5 of Solidity.

[**\[S\] Compiler Bug SOL-2016-9**](index.html#req-1-compiler-SOL-2016-9)**<a href="index.html#req-1-compiler-SOL-2016-9" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that use variables of a type shorter than 17 bytes *MUST NOT* use a version of Solidity older than 0.4.4.

[**\[S\] Compiler Bug SOL-2016-8**](index.html#req-1-compiler-SOL-2016-8)**<a href="index.html#req-1-compiler-SOL-2016-8" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `sha3()` instruction *MUST NOT* use the Optimizer option with a version of Solidity older than 0.4.3.

[**\[S\] Compiler Bug SOL-2016-7**](index.html#req-1-compiler-SOL-2016-7)**<a href="index.html#req-1-compiler-SOL-2016-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `delegatecall()` from a function that can receive Ether to call a Library Function *MUST NOT* use versions 0.4.0 or 0.4.1 of Solidity.

[**\[S\] Compiler Bug SOL-2016-6**](index.html#req-1-compiler-SOL-2016-6)**<a href="index.html#req-1-compiler-SOL-2016-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that sends Ether *MUST NOT* use a version of Solidity older than 0.4.0 **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">overriding requirement</a> [**\[M\] Compiler Bug No Zero Ether Send**](index.html#req-2-compiler-no-zero-ether-send).

[**\[S\] Compiler Bug SOL-2016-5**](index.html#req-1-compiler-SOL-2016-5)**<a href="index.html#req-1-compiler-SOL-2016-5" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that creates a dynamically sized array with a `length` that can be zero *MUST NOT* use a version of Solidity older than 0.3.6.

[**\[S\] Compiler Bug SOL-2016-4**](index.html#req-1-compiler-SOL-2016-4)**<a href="index.html#req-1-compiler-SOL-2016-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that creates a `Jump Destination` opcode *MUST NOT* use the Optimizer with versions of Solidity older than 0.3.6.

[**\[S\] Compiler Bug SOL-2016-3**](index.html#req-1-compiler-SOL-2016-3)**<a href="index.html#req-1-compiler-SOL-2016-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that compares the values of data of type <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> *MUST NOT* use a version of Solidity older than 0.3.3.

[**\[S\] Compiler Bug SOL-2016-2**](index.html#req-1-compiler-SOL-2016-2)**<a href="index.html#req-1-compiler-SOL-2016-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses arrays, with data types whose size is less than 17 bytes *MUST NOT* use a version of Solidity older than 0.3.1.

[**\[S\] No Ancient Compilers**](index.html#req-1-no-ancient-compilers)**<a href="index.html#req-1-no-ancient-compilers" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a version of Solidity older than 0.3.

[**\[M\] Pass Security Level \[S\]**](index.html#req-2-pass-l1)**<a href="index.html#req-2-pass-l1" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">4.1 Security Level [S]</a>.

[**\[M\] No failing `assert` statements**](index.html#req-2-no-failing-asserts)**<a href="index.html#req-2-no-failing-asserts" class="selflink"></a>**
`assert()` statements in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* fail.

[**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo)**<a href="index.html#req-2-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characterss**](index.html#req-1-unicode-bdo).

[**\[M\] No Homoglyph-style Attack**](index.html#req-2-no-homoglyph-attack)**<a href="index.html#req-2-no-homoglyph-attack" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks if the impact is misleading.

[**\[M\] Protect External Calls**](index.html#req-2-external-calls)**<a href="index.html#req-2-external-calls" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls:

- all contracts called *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>, **and**
- all contracts called *MUST* be controlled by the same entity, **and**
- the protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

[**\[M\] Handle External Call Returns**](index.html#req-2-handle-return)**<a href="index.html#req-2-handle-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.

[**\[M\] Document Special Code Use**](index.html#req-2-documented)**<a href="index.html#req-2-documented" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* document the need for each instance of:

- `selfdestruct()` or its deprecated alias `suicide()`,
- `assembly()`,
- `CREATE2`,
- external calls,
- use of `block.number` or `block.timestamp`,
- Use of oracles and pseudo-randomness, **or**
- code that can cause an overflow or underflow,

**and** *MUST* describe how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, **and** the documentation *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of

- [**\[S\] No `Self-destruct`**](index.html#req-1-self-destruct).
- [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).
- [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

[**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct)**<a href="index.html#req-2-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Self-destruct**](index.html#req-1-self-destruct).

[**\[M\] Avoid Common `assembly()` Attack Vectors**](index.html#req-2-safe-assembly)**<a href="index.html#req-2-safe-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly()` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

[**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2)**<a href="index.html#req-2-protect-create2" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses the `CREATE2` instruction, any contract to be deployed using `CREATE2`

- *MUST* be within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* use any `selfdestruct()`, `delegatecall()` nor `callcode()` instructions, **and**
- *MUST* be fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `CREATE2`**](index.html#req-1-no-create2).

[**\[M\] Declare `storage` Explicitly**](index.html#req-2-explicit-storage)**<a href="index.html#req-2-explicit-storage" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.5.0 *MUST* explicitly declare `storage` or `memory` for storage objects, and must justify the need for any `storage` item.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Explicit Storage**](index.html#req-1-explicit-storage).

[**\[M\] No Overflow/Underflow**](index.html#req-2-overflow-underflow)**<a href="index.html#req-2-overflow-underflow" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Overflow/Underflow**](index.html#req-1-overflow-underflow).

[**\[M\] Declare Explicit Constructors**](index.html#req-2-explicit-constructors)**<a href="index.html#req-2-explicit-constructors" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.22 *MUST* declare `constructor` methods explicitly.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Explicit Constructors**](index.html#req-1-explicit-constructors).

[**\[M\] Document Name Conflicts**](index.html#req-2-safe-inheritance-order)**<a href="index.html#req-2-safe-inheritance-order" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* clearly document the order of inheritance for each function or variable that shares a name with another function or variable.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Conflicting Inheritance**](index.html#req-1-inheritance-conflict).

[**\[M\] Sources of Randomness**](index.html#req-2-random-enough)**<a href="index.html#req-2-random-enough" class="selflink"></a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

[**\[M\] Don't misuse block data**](index.html#req-2-block-data-misuse)**<a href="index.html#req-2-block-data-misuse" class="selflink"></a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

[**\[M\] Proper Signature Verification**](index.html#req-2-signature-verification)**<a href="index.html#req-2-signature-verification" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* use proper signature verification to ensure authenticity of messages that were signed off-chain, e.g. by using `ecrecover()`.

[**\[M\] No Improper Usage of Malleable Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay)**<a href="index.html#req-2-malleable-signatures-for-replay" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST NOT* rely on <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

[**\[M\] Compiler Bug SOL-2022-5 in `assembly()`**](index.html#req-2-compiler-SOL-2022-5-assembly)**<a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, and has an `assembly()` instruction that reads that data without explicitly matching the length that was copied, *MUST NOT* use a version of Solidity older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4)**<a href="index.html#req-2-compiler-SOL-2022-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly()` instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, and code in a another `assembly()` instruction refers to that memory, *MUST NOT* use the yulOptimizer with versions 0.8.13 or 0.8.14 of Solidity.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3)**<a href="index.html#req-2-compiler-SOL-2021-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly()` instruction *MUST NOT* use a version of Solidity between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug Check Constructor Payment**](index.html#req-2-compiler-check-payable-constructor)**<a href="index.html#req-2-compiler-check-payable-constructor" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is

- defined in a base contract, **and**
- used by default in another contract without an explicit constructor, **and**
- not explicity marked `payable`,

*MUST NOT* use a version of Solidity between 0.4.5 and 0.6.7 (inclusive).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2020-5**](index.html#req-1-compiler-SOL-2020-5).

[**\[M\] Compiler Bug SOL-2020-2**](index.html#req-2-compiler-SOL-2020-2)**<a href="index.html#req-2-compiler-SOL-2020-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that declares multiple functions with the same name *MUST NOT* use a version of Solidity older than 0.5.17.

[**\[M\] Compiler Bug SOL-2019-2 in `assembly()`**](index.html#req-2-compiler-SOL-2019-2-assembly)**<a href="index.html#req-2-compiler-SOL-2019-2-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the Optimizer with a version 0.5.5 nor 0.5.6 of Solitidy *MUST NOT* contain inline `assembly()` that uses the `byte` instruction with a second parameter whose compile-time value evaluates to 31.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly()`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug Check Identity Calls**](index.html#req-2-compiler-check-identity-calls)**<a href="index.html#req-2-compiler-check-identity-calls" class="selflink"></a>**
In <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.7, calls to the Identity Contract *MUST* explicitly check the return value.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2016-11**](index.html#req-1-compiler-SOL-2016-11).

[**\[M\] Validate `ecrecover()` input**](index.html#req-2-validate-ecrecover-input)**<a href="index.html#req-2-validate-ecrecover-input" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses the `ecrecover()` pre-compile in a version of Solidity older than 0.4.14 *MUST* ensure that input is well-formed before making the call.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2017-3**](index.html#req-1-compiler-SOL-2017-3).

[**\[M\] Compiler Bug No Zero Ether Send**](index.html#req-2-compiler-no-zero-ether-send)**<a href="index.html#req-2-compiler-no-zero-ether-send" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses a version of Solidity older than 0.4.0, *MUST NOT* make Ether transfers that can send a value of zero.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Compiler Bug SOL-2016-6**](index.html#req-1-compiler-SOL-2016-6).

[**\[Q\] Pass Security Level \[M\]**](index.html#req-3-pass-l2)**<a href="index.html#req-3-pass-l2" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">4.2 Security Level [M]</a>.

[**\[Q\] Code Linting**](index.html#req-3-linted)**<a href="index.html#req-3-linted" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert` statements, **and**
- *MUST* explicitly declare the visibility of all functions and variables.

[**\[Q\] Manage Gas Use Increases**](index.html#req-3-enough-gas)**<a href="index.html#req-3-enough-gas" class="selflink"></a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

[**\[Q\] Protect against Front-Running**](index.html#req-3-block-front-running)**<a href="index.html#req-3-block-front-running" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* require information in a form that can be used to enable a <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a> attack.

[**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev)**<a href="index.html#req-3-block-mev" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

[**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs)**<a href="index.html#req-3-all-valid-inputs" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

[**\[Q\] State Changes Trigger Events**](index.html#req-3-event-on-state-change)**<a href="index.html#req-3-event-on-state-change" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

[**\[Q\] No Private Data**](index.html#req-3-no-private-data)**<a href="index.html#req-3-no-private-data" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain

[**\[Q\] Document Contract Logic**](index.html#req-3-documented)**<a href="index.html#req-3-documented" class="selflink"></a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

[**\[Q\] Document System Architecture**](index.html#req-3-document-system)**<a href="index.html#req-3-document-system" class="selflink"></a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

[**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate)**<a href="index.html#req-3-annotate" class="selflink"></a>**
All public interfaces contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation.">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

[**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented)**<a href="index.html#req-3-implement-as-documented" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

[**\[Q\] Implement Access Control**](index.html#req-3-access-control)**<a href="index.html#req-3-access-control" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* implement appropriate access control mechanisms, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

[**\[Q\] Verify External Calls**](index.html#req-3-external-calls)**<a href="index.html#req-3-external-calls" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirement</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)**<a href="index.html#req-3-verify-tx.origin" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

[**\[GP\] Check For and Address New Security Bugs**](index.html#req-R-check-new-bugs)**<a href="index.html#req-R-check-new-bugs" class="selflink"></a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 15 July 2022 and address them.

[**\[GP\] Meet As Many Requirements As Possible**](index.html#req-R-meet-all-possible)**<a href="index.html#req-R-meet-all-possible" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

[**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler)**<a href="index.html#req-R-use-latest-compiler" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable version of the Solidity compiler.

[**\[GP\] Write clear, legible Solidity code**](index.html#req-R-clean-code)**<a href="index.html#req-R-clean-code" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

[**\[GP\] Follow Accepted ERC Standards**](index.html#req-R-follow-erc-standards)**<a href="index.html#req-R-follow-erc-standards" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case. An ERC is a category of \[<a href="index.html#bib-eip" class="bibref" data-link-type="biblio" title="EIP-1: EIP Purpose and Guidelines">EIP</a>\] (Ethereum Improvement Proposal) that defines application-level standards and conventions, including smart contract standards such as token standards (EIP-20) and name registries (EIP-137).

[**\[GP\] Define a Software License**](index.html#req-R-define-license)**<a href="index.html#req-R-define-license" class="selflink"></a>** The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license, which is commonly open-source for Solidity code deployed to public networks. A software license provides legal guidance on how contributors and users can interact with the code, including auditors and whitehats.

[**\[GP\] Disclose New Vulnerabilities Responsibly**](index.html#req-R-notify-news)**<a href="index.html#req-R-notify-news" class="selflink"></a>** Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">1.4 Feedback and new vulnerabilities</a>.

### A.3 Acknowledgments

The EEA acknowledges and thanks the many people who contributed to the development of this version of the specification. Please advise us of any errors or omissions.

Enterprise Ethereum is built on top of Ethereum, and we are grateful to the entire community who develops Ethereum, for their work and their ongoing collaboration. It helps us maintain as much compatibility as possible with the Ethereum ecosystem.

Security principles have also been developed over many years by many individuals, far too numerous to individually thank for contributions that have helped us to write the present specification. We are grateful to the many people on whose work we build.

## B. References

### B.1 Normative references

\[c-e-i\]
[Security Considerations - Solidity Documentation. Section 'Use the Checks-Effects-Interactions Pattern'](https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern>

\[CVE-2021-42574\]
[National Vulnerability Database CVE-2021-42574](https://nvd.nist.gov/vuln/detail/CVE-2021-42574). The National Institute of Standards (US Department of Commerce). URL: <https://nvd.nist.gov/vuln/detail/CVE-2021-42574>

\[CWE\]
[Common Weakness Enumeration](https://cwe.mitre.org/index.html). MITRE. URL: <https://cwe.mitre.org/index.html>

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

\[CWE-824\]
[CWE-824: Access of Uninitialized Pointer](https://cwe.mitre.org/data/definitions/824.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/824.html>

\[CWE-94\]
[CWE-94: Improper Control of Generation of Code ('Code Injection')](https://cwe.mitre.org/data/definitions/94.html). MITRE. URL: <https://cwe.mitre.org/data/definitions/94.html>

\[EIP\]
[EIP-1: EIP Purpose and Guidelines](https://eips.ethereum.org/EIPS/eip-1). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-1>

\[ERC\]
[ERC Final - Ethereum Improvement Proposals](https://eips.ethereum.org/erc). Ethereum Foundation. URL: <https://eips.ethereum.org/erc>

\[ERC20\]
[EIP-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-20>

\[error-handling\]
[Control Structures - Solidity Documentation. Section 'Error handling: Assert, Require, Revert and Exceptions'](https://docs.soliditylang.org/en/v0.8.14/control-structures.html#error-handling-assert-require-revert-and-exceptions). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/v0.8.14/control-structures.html#error-handling-assert-require-revert-and-exceptions>

\[EVM-version\]
[Using the Compiler - Solidity Documentation. (§Targets)](https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/using-the-compiler.html#target-options>

\[GDPR\]
[Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) (Text with EEA relevance)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679). The European Union. URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679>

\[Ivanov\]
[Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts](https://arxiv.org/pdf/2105.00132.pdf#subsection.4.2). Nikolay Ivanov; Jianzhi Lou; Ting Chen; Jin Li; Qiben Yan. URL: <https://arxiv.org/pdf/2105.00132.pdf#subsection.4.2>

\[NatSpec\]
[NatSpec Format - Solidity Documentation.](https://docs.soliditylang.org/en/latest/natspec-format.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/natspec-format.html>

\[RBAC\]
[INCITS 359-2012: Information Technology - Role Based Access Control](http://www.techstreet.com/products/1837530). InterNational Committee for Information Technology Standards. URL: <http://www.techstreet.com/products/1837530>

\[RFC2119\]
[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

\[RFC8174\]
[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

\[SHA3-256\]
[FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions](http://dx.doi.org/10.6028/NIST.FIPS.202). The National Institute of Standards (US Department of Commerce). URL: <http://dx.doi.org/10.6028/NIST.FIPS.202>

\[sigp\]
[Solidity Security: Comprehensive List of Known Attack Vectors and Common Anti-Patterns](https://blog.sigmaprime.io/solidity-security.html). URL: <https://blog.sigmaprime.io/solidity-security.html>

\[software-license\]
[Choosing an Open Source License](https://choosealicense.com/). GitHub. URL: <https://choosealicense.com/>

\[solidity-alerts\]
[Solidity Blog - Security Alerts](https://blog.soliditylang.org/category/security-alerts/). Ethereum Foundation. URL: <https://blog.soliditylang.org/category/security-alerts/>

\[solidity-bugs\]
[List of Known Bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.rst>

\[solidity-bugs-json\]
[A JSON-formatted list of some known security-relevant Solidity bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.json). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/blob/develop/docs/bugs.json>

\[solidity-events\]
[Solidity Documentation: Contracts - Events](https://docs.soliditylang.org/en/latest/contracts.html#events). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/contracts.html#events>

\[solidity-functions\]
[Solidity Documentation: Contracts - Functions](https://docs.soliditylang.org/en/latest/contracts.html#functions). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/contracts.html#functions>

\[solidity-patterns\]
[Solidity Patterns](https://fravoll.github.io/solidity-patterns/). Franz Volland. URL: <https://fravoll.github.io/solidity-patterns/>

\[solidity-security\]
[Security Considerations - Solidity Documentation.](https://docs.soliditylang.org/en/latest/security-considerations.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/security-considerations.html>

\[Solidity-Style-Guide\]
[Solidity Style Guide - Solidity Documentation.](https://docs.soliditylang.org/en/latest/style-guide.html). URL: <https://docs.soliditylang.org/en/latest/style-guide.html>

\[storage-honeypots\]
[Solidity Security: Comprehensive list of known attack vectors and common anti-patterns - section 14: Uninitialised Storage Pointers](https://blog.sigmaprime.io/solidity-security.html#storage). URL: <https://blog.sigmaprime.io/solidity-security.html#storage>

\[swcregistry\]
[Smart Contract Weakness Classification Registry](https://swcregistry.io). ConsenSys Diligence. URL: <https://swcregistry.io>

\[tmio-bp\]
[Best Practices for Smart Contracts (privately made available to EEA members)](https://github.com/EntEthAlliance/eta-registry/blob/master/working-docs/tmio-bp.md). TMIO. URL: <https://github.com/EntEthAlliance/eta-registry/blob/master/working-docs/tmio-bp.md>

\[unicode-bdo\]
[How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls). W3C Internationalization. 10 March 2016. URL: <https://www.w3.org/International/questions/qa-bidi-unicode-controls>

\[unicode-blocks\]
[Blocks-14.0.0.txt](https://www.unicode.org/Public/UNIDATA/Blocks.txt). Unicode®, Inc. 22 January 2021. URL: <https://www.unicode.org/Public/UNIDATA/Blocks.txt>

### B.2 Informative references

\[ASVS\]
[OWASP Application Security Verification Standard](https://github.com/OWASP/ASVS). The OWASP Foundation. URL: <https://github.com/OWASP/ASVS>

\[chase\]
[Malleable Signatures: New Definitions and Delegatable Anonymous Credentials](https://smeiklej.com/files/csf14.pdf). Melissa Chase; Markulf Kohlweiss; Anna Lysyanskaya; Sarah Meiklejohn. URL: <https://smeiklej.com/files/csf14.pdf>

\[EEA-chains\]
[Enterprise Ethereum Alliance Permissioned Blockchains Specification - Editors' draft](https://entethalliance.github.io/client-spec/chainspec.html). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.github.io/client-spec/chainspec.html>

\[EEA-clients\]
[Enterprise Ethereum Client Specification - Editors' draft](https://entethalliance.github.io/client-spec/spec.html). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.github.io/client-spec/spec.html>

\[EEA-L2\]
[Introduction to Ethereum Layer 2](https://entethalliance.org/eea-primers/entry/5696/). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.org/eea-primers/entry/5696/>

\[hash-commit\]
[Commitment scheme - WikiPedia](https://en.wikipedia.org/wiki/Commitment_scheme). WikiMedia Foundation. URL: <https://en.wikipedia.org/wiki/Commitment_scheme>

\[License\]
[Apache license version 2.0](http://www.apache.org/licenses/LICENSE-2.0). The Apache Software Foundation. URL: <http://www.apache.org/licenses/LICENSE-2.0>

[↑](index.html#title)
