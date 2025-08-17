---
source_id: 1005 # ID for parent source from sources.csv
source_url: "https://entethalliance.org/specs/ethtrust-sl/v3/"   # Canonical URL for parent source
item_id: "1004-2025-03-31-ethtrust-v3-index"  # source_id-ISOdate-stable slug (i.e: "1020-2023-06-07-uniswap-v3-limit-orders") 
title: "EEA EthTrust Security Levels Specification v3"  # Human-readable title
author_or_org: ["Enterprise Ethereum Alliance"] # Who created this file?
item_source_url: "https://entethalliance.org/specs/ethtrust-sl/v3/"   # Canonical URL for this file
local_path: "preflight_corpus/data/rag/ethtrust/v3/index.md"   # Path inside repo
type: "standard"
intended_use: "RAG" # How this file is used
license: "Apache 2.0"     # SPDX or short label
date_last_updated: "2025-03-31"  # ISO dates only
source_family: "ethtrust"
tags: ["Standards","EthTrust","Security","Conformance"]       # 2–5 controlled tags
status: "draft"  # Only for standards/specs
language: "en"              # Language code

# Optional crosswalk mappings
x:
  crosswalk:
    ethtrust: []
    scwe: []
    swc: []
---

# EEA EthTrust Security Levels Specification Version 3

## EEA Specification March 2025

This Release version:
[https://entethalliance.org/specs/ethtrust-sl/v3/](index.html)

Checklist for this version:
[https://entethalliance.org/specs/ethtrust-sl/v3/checklist.html](checklist.html)

Latest editor's draft:
<https://entethalliance.github.io/eta-registry/security-levels-spec.html>

Editor:
<a href="https://entethalliance.org/cdn-cgi/l/email-protection#a2c7c6cbd6cdd0e2c7ccd6c7d6cac3cececbc3ccc1c78ccdd0c5" class="ed_mailto u-email email p-name">EEA Editor</a>

Latest release URL:
<https://entethalliance.org/specs/ethtrust-sl/>

Contributors to this version:
As well as all those who contributed to the previous versions that this version extends, the following people made specific contributions to this version of the specification:
Chaals Neville, Anish Agrawal (Olympix), Kenan Bešić (ChainSecurity), Daniel Burnett, Valerian Callens, Luke Ciattaglia (Hacken), Christopher Cordi, Ignacio Freire (Olympix), Aminadav Glickshtein (EY), Opal Graham (CertiK), Channi Greenwall (Olympix), James Harsh, Sebastian Holler, George Kobakhidze (Diligence), Michael Lewellen (OpenZeppelin), Luis Lubeck (Hacken), Dominik Muhs, Anton Permenev (ChainSecurity), Juliano Rizzo (Coinspect), Gernot Salzer, Clara Schneidewinde, Tobias Vogel (Diligence), Morgan Weaver (OpenZeppelin)

Copyright © 2020-2025 [Enterprise Ethereum Alliance](https://entethalliance.org/).

------------------------------------------------------------------------

## Abstrac

This document defines the requirements for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, a set of certifications that a smart contract has been reviewed and found not to have a defined set of security vulnerabilities.

## Status of This Documen

*This section describes the status of this document at the time of its publication. Newer documents may supersede this document.*

This document is the [EEA EthTrust Security Levels Specification Version 3](https://entethalliance.org/specs/ethtrust-sl/v2/), developed by the [EthTrust Security Levels Working Group](https://entethalliance.org/groups/EthTrust) and published by the Enterprise Ethereum Alliance, Inc.

The content of this draft has been approved for publication by the EEA.

The Working Group expects, at the time of publication, to continue work and produce a new version to supersede this document, likely to be finalized and published in the second half of 2026.

This specification is licensed by the Enterprise Ethereum Alliance, Inc. (EEA) under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) \[<a href="index.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\] Unless otherwise explicitly authorised in writing by the EEA, you can only use this specification in accordance with those terms.

Unless required by applicable law or agreed to in writing, this specification is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

Feedback on this specification can be sent directly to the editor at [EEA Editor](https://entethalliance.org/cdn-cgi/l/email-protection#b2d7d6dbc6ddc0f2d7dcc6d7c6dad3dededbd3dcd1d79cddc0d5), or raised as issues in the [EthTrust-public GitHub repository](https://github.com/entethalliance/EthTrust-public).

[GitHub Issues](https://github.com/EntEthAlliance/EthTrust-public/issues/) are preferred for discussion of this specification.

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
    8.  <a href="index.html#sec-ordering-considerations" class="tocxref">3.8 Ordering Attacks</a>
    9.  <a href="index.html#sec-source-compiler-considerations" class="tocxref">3.9 Source code, pragma, and compilers</a>
    10. <a href="index.html#sec-deployment-considerations" class="tocxref">3.10 Contract Deployment</a>
    11. <a href="index.html#sec-realtime-monitoring-considerations" class="tocxref">3.11 Post-deployment Monitoring</a>
    12. <a href="index.html#sec-netupgrades-considerations" class="tocxref">3.12 Network Upgrades</a>
    13. <a href="index.html#sec-organizational-security" class="tocxref">3.13 Organizational and Off-Chain Security Posture</a>
    14. <a href="index.html#sec-adversarial-simulation" class="tocxref">3.14 Preempting On-Chain Adversarial Conditions</a>
4.  <a href="index.html#sec-testing-methods" class="tocxref">4. Testing Methodologies</a>
    1.  <a href="index.html#sec-testing-unit" class="tocxref">4.1 Unit Testing</a>
    2.  <a href="index.html#sec-testing-static" class="tocxref">4.2 Static Analysis</a>
    3.  <a href="index.html#sec-testing-fuzzing" class="tocxref">4.3 Fuzzing</a>
    4.  <a href="index.html#sec-testing-mutation" class="tocxref">4.4 Mutation Testing</a>
    5.  <a href="index.html#sec-testing-symbolic" class="tocxref">4.5 Symbolic Execution</a>
    6.  <a href="index.html#sec-testing-formal" class="tocxref">4.6 Formal Verification</a>
    7.  <a href="index.html#sec-testing-properties" class="tocxref">4.7 Properties and Invariants</a>
    8.  <a href="index.html#sec-testing-testnets" class="tocxref">4.8 Testnet Deployment</a>
5.  <a href="index.html#sec-levels" class="tocxref">5. EEA EthTrust Security Levels</a>
    1.  <a href="index.html#sec-levels-one" class="tocxref">5.1 Security Level [S]</a>
        1.  <a href="index.html#sec-1-unicode" class="tocxref">5.1.1 Text and homoglyphs</a>
        2.  <a href="index.html#sec-1-external-calls" class="tocxref">5.1.2 External Calls</a>
        3.  <a href="index.html#sec-1-compiler-bugs" class="tocxref">5.1.3 Compiler Bugs </a>
    2.  <a href="index.html#sec-levels-two" class="tocxref">5.2 Security Level [M]</a>
        1.  <a href="index.html#sec-2-unicode" class="tocxref">5.2.1 Text and homoglyph attacks</a>
        2.  <a href="index.html#sec-2-external-calls" class="tocxref">5.2.2 External Calls</a>
        3.  <a href="index.html#sec-2-special-code" class="tocxref">5.2.3 Documented Defensive Coding</a>
        4.  <a href="index.html#sec-2-signature-requirements" class="tocxref">5.2.4 Signature Management</a>
        5.  <a href="index.html#sec-level-2-compiler-bugs" class="tocxref">5.2.5 Security Level [M] Compiler Bugs and Overriding Requirements</a>
    3.  <a href="index.html#sec-levels-three" class="tocxref">5.3 Security Level [Q]</a>
        1.  <a href="index.html#sec-3-documentation" class="tocxref">5.3.1 Documentation requirements</a>
        2.  <a href="index.html#sec-3-access-control" class="tocxref">5.3.2 Access Control</a>
    4.  <a href="index.html#sec-good-practice-recommendations" class="tocxref">5.4 Recommended Good Practices</a>
6.  <a href="index.html#sec-additional-information" class="tocxref">A. Additional Information</a>
    1.  <a href="index.html#sec-definitions" class="tocxref">A.1 Defined Terms</a>
    2.  <a href="index.html#sec-summary-of-requirements" class="tocxref">A.2 Summary of Requirements</a>
    3.  <a href="index.html#sec-acknowledgments" class="tocxref">A.3 Acknowledgments</a>
    4.  <a href="index.html#sec-changes" class="tocxref">A.4 Changes</a>
        1.  <a href="index.html#sec-change-new" class="tocxref">A.4.1 New Requirements and Recommended Good Practices</a>
        2.  <a href="index.html#sec-change-update" class="tocxref">A.4.2 Updated Requirements</a>
        3.  <a href="index.html#sec-change-removed" class="tocxref">A.4.3 Requirements removed</a>
    5.  <a href="index.html#requirements-removed-from-previous-versions" class="tocxref">A.5 Requirements removed from previous versions</a>
7.  <a href="index.html#references" class="tocxref">B. References</a>
    1.  <a href="index.html#normative-references" class="tocxref">B.1 Normative references</a>
    2.  <a href="index.html#informative-references" class="tocxref">B.2 Informative references</a>

## 1. Introduction<a href="index.html#sec-introduction" class="self-link" aria-label="§"></a>

*This section is non-normative.*

This defines the requirements for granting <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> to a smart contract written in Solidity.

<a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is a claim by a security reviewer that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is not vulnerable to a number of known attacks or failures to operate as expected, based on the reviewer's assessment against those specific requirements.

No amount of security review can guarantee that a smart contract is secure against **all possible** vulnerabilities, as further explained in <a href="index.html#sec-security-considerations" class="sec-ref">§ 3. Security Considerations</a>. However reviewing a smart contract according to the requirements in this specification provides assurance that it is not vulnerable to a known setof potential attacks.

This assurance is backed not only by the reputation of the reviewer, but by the collective reputations of the multiple experts in security from many competing organizations, who collaborated within the EEA to ensure this specification defines protections against a real and significant set of known vulnerabilities.

### 1.1 How to read this specification<a href="index.html#sec-reading-the-spec" class="self-link" aria-label="§"></a>

This section describes how to understand this specification, including the conventions used for examples and requirements, core concepts, references, informative sections, etc.

#### 1.1.1 Overview of this Document<a href="index.html#sec-document-overview" class="self-link" aria-label="§"></a>

Broadly, the document is structured as follows:

Front matter
Basic information about the document - authors, copyright, etc.

Conformance section
What it means and looks like to claim conformance to this specification.

Security Considerations
A general introduction to key security concepts relevant to Smart Contracts.

Testing Methodologies
A general introduction to some different approaches to Testing that are relevant to this specification.

EthTrust Security Levels
The core of the document. Requirements that security reviews should meet, grouped by levels and then thematically.

Additional Information
- A glossary of terms defined.
- A summary of requirements and recommended good practices.
- Acknowledgements
- A summary of substantial changes made since the previous release version.
- A list of requirements that were in published version, but have already been removed in earlier versions.

References
Further reading, including normative references necessary to the requirements and informative references that expand on topics described in the specification.

This specification is accompanied by a [**Checklist**](checklist.html), that lists the requirements in a handy table. That checklist can be used to help developers or reviewers familiar with the specification to quickly remind themselves of each individual requirement and track whether they have tested it. In case of any discrepancy, the normative text is in this specification document.

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

Definitions of terms are formatted Like This and subsequent references to defined terms are rendered as links to that definition <a href="index.html#dfn-like-this" class="internalDFN" data-link-type="dfn">Like This</a>.

References to other documents are given as links to the relevant entry in the section <a href="index.html#references" class="sec-ref">§ B. References</a>, within square brackets: \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\].

Links to requirements begin with a <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a>: **\[S\]**, **\[M\]** or **\[Q\]**, and links to recommended good practices begin with **\[GP\]**. They then include the requirement or good practice name. They are rendered as links in bold type:

<a href="index.html#example-3" class="self-link">Example 3</a>

Example of a link to [**\[M\] Document Special Code Use**](index.html#req-2-documented).

Variables, introduced to be described further on in a statement or requirement, are formatted as `var`.

Occasional explanatory notes, presented as follows, are not normative and do not specify formal requirements.

Note: Notes are explanatory

The content of a Note is meant to be useful, but does not form a requirement.

#### 1.1.3 How to Read a Requirement<a href="index.html#sec-reading-requirements" class="self-link" aria-label="§"></a>

The core of this document is the requirements, that collectively define <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

Requirements have

- a [Security Level](index.html#sec-levels) that is one of "[**\[S\]**](index.html#sec-levels-one)", "[**\[M\]**](index.html#sec-levels-two)", or "[**\[Q\]**](index.html#sec-levels-three)",
- a name,
- a link (identified with "🔗") to its URL, and
- a statement of what *MUST* be achieved to meet the requirement.

The group intends that the URL for a requirement in this Editors' Draft always points to the latest version of the requirement in the group's Editors' Draft. Note that this possibly represents incomplete work in progress.

Some requirements at the same <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> are grouped in a subsection, because they are related to a particular theme or area of potential attacks.

Requirements are followed by explanation, that can include why the requirement is important, how to test for it, links to <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>, test cases, and links to other useful information.

As well as requirements, this document includes some <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a>, that are formatted similarly with an apparent Security Level of "**\[GP\]**". It is not necessary to implement these in order to conform to the specification, but if carefully implemented they can improve the security of smart contracts.

The following requirement:

<a href="index.html#example-4-a-simple-requirement" class="self-link">Example 4</a>: A simple requiremen

**\[S\] Compiler Bug SOL-2022-5 with `.push()` [🔗](index.html#req-1-compiler-SOL-2022-5-push)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, **and**
- has an empty `.push()` instruction that writes to the resulting array,

*MUST NOT* use a Solidity compiler version older than 0.8.15.

Until Solidity compiler version 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using code through `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly).

is a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, as denoted by the "**\[S\]**" before its name. Its name is **Compiler Bug SOL-2022-5 with `.push()`**. (Its URL **in the editor's draft** as linked from the " 🔗 " character) is <https://entethalliance.github.io/eta-registry/security-levels-spec.html#req-1-compiler-SOL-2022-5-push>.

The statement of requirement is

> <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha
>
> - copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, **and**
> - has an empty `.push()` instruction that writes to the resulting array,
>
> *MUST NOT* use a Solidity compiler version older than 0.8.15.

Following the requirement is a brief explanation of the relevant vulnerability, and links to further discussion.

Note

Good Practices are formatted the same way as Requirements, with an apparent level of **\[GP\]**. However, as explained in <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a> meeting them is not necessary and does not in itself change conformance to this specification.

##### 1.1.3.1 Overriding Requirements<a href="index.html#sec-overriding-requirements" class="self-link" aria-label="§"></a>

For some requirements, the statement will include an alternative condition, introduced with the keyword **unless**, that identifies one or more Overriding Requirements. These are requirements at a higher Security Level, that can be satisfied to achieve conformance if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet the lower-level requirement as stated. In some cases it is necessary to meet more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> to meet the requirement they override. In this case, the requirements are described as a Set of Overriding Requirements. It is necessary to meet all the requirements in a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> in order to meet the requirement that is overriden.

In a number of cases, there will be more than one <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> that can be met in order to satisfy a given requirement. For example, it is sometimes possible to meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> Requirement either by directly fulfilling it, **or** by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, **or** by meeting a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>.

<a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> enable simpler testing for common simple cases. For more complex <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, that uses features which need to be handled with extra care to avoid introducing vulnerabilities, they ensure such usage is appropriately checked.

In a typical case of a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement, an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> will apply in relatively unusual cases or where automated systems are generally unable to verify that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. Further verification of the applicable <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> can determine that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is using a feature appropriately, and therefore passes the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement.

If there is not an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for a requirement that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> does not meet, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is not eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. However, even for such cases, note the Recommended Good Practice [**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible); meeting any requirements in this specification will improve the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

In the following requirement:

- the Security Level is "**\[S\]**",

- the name is "**No `tx.origin`**", and

- the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> is "[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)".

  <a href="index.html#example-5-example-a-requirement-with-an-overriding-requirement" class="self-link">Example 5</a>: Example: A requirement with an Overriding Requiremen
  **\[S\] No `tx.origin` [🔗](index.html#req-1-no-tx.origin)**
  <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not contain a `tx.origin` instruction
  **unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin).

The requirement that the tested code does not contain a `tx.origin` instruction is automatically verifiable.

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that meets the Security Level \[Q\] <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin) conforms to this Security Level \[S\] requirement.

Requirements that are an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for another, or are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, expicitly mention that:

<a href="index.html#example-6-example-overriding-requirement" class="self-link">Example 6</a>: Example: Overriding Requiremen

**\[M\] No Unnecessary Unicode Controls [🔗](index.html#req-2-unicode-bdo)**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* not use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirement</a> for [\[S\] No Unicode Direction Control Characters](index.html#req-1-unicode-bdo).

##### 1.1.3.2 Related Requirements<a href="index.html#sec-related-requirements" class="self-link" aria-label="§"></a>

Many requirements have Related Requirements, which are requirements that address thematically related issues.

The links to them are provided as useful information. Unlike <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>, meeting Related Requirements does not substitute for meeting a specific requirement in order to achieve conformance.

### 1.2 Why Certify Contracts?<a href="index.html#sec-intro-why-certify-contracts" class="self-link" aria-label="§"></a>

*This section is non-normative.*

A number of smart contracts that power decentralized applications on Ethereum have been found to contain security issues, and today it is often difficult or impossible in practice to see how secure an address or contract is before initiating a transaction. The Defi space in particular has exploded with a flurry of activity, with individuals and organizations approving transactions in token contracts, swapping tokens, and adding liquidity to pools in quick succession, sometimes without stopping to check security. For Ethereum to be trusted as a transaction layer, enterprises storing critical data or financial institutions moving large amounts of capital need a clear signal that a contract has had appropriate security audits.

Reviewing early, in particular before production deployment, is especially important in the context of blockchain development because the costs in time, effort, funds, and/or credibility, of attempting to update or patch a smart contract after deployment are generally much higher than in other software development contexts.

This smart contract security standard is designed to increase confidence in the quality of security audits for smart contracts, and thus to raise trust in the Ethereum ecosystem as a global settlement layer for all types of transactions across all types of industry sectors, for the benefit of the entire Ethereum ecosystem.

Certification also provides value to the actual or potential users of a smart contract, and others who could be affected by the use or abuse of a particular smart contract but are not themselves direct users. By limiting exposure to certain known weaknesses through <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, these stakeholders benefit from reduced risk and increased confidence in the security of assets held in or managed by the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This assurance is not complete; for example it relies on the competence and integrity of the auditor issuing the certification. That is generally not completely knowable. Professional reputations can change based on subsequent performance of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. This is especially so if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> becomes sufficiently high-profile to motivate exploitation of weaknesses remaining after certification.

Finally, smart contract developers and ecosystem stakeholders receive value when others (including direct competitors) complete the certification process, because it means those other contracts are less likely to generate exploitation-related headlines which can lead to negative perceptions of Ethereum technology as insecure or high risk by the general public including business leaders, prospective customers/users, regulators, and investors.

The value of smart contract security certification is in some ways analogous to the certification processes applicable to aircraft parts. Most directly, it helps reduce risks for part manufacturers and the integrators who use those parts as components of a more complex structure, by providing assurance of a minimum level of quality. Less directly, these processes significantly reduce aviation accidents and crashes, saving lives and earning the trust of both regulators and customers who consider the safety and risk of the industry and its supporting technology as a whole. Many safety certification processes began as voluntary procedures created by a manufacturer, or specified and required by a consortium of customers representing a significant fraction of the total market. Having proven their value, some of these certification processes are now required by law, to protect the public.

We hope the value of the certification process motivates frequent use, and furthers development of automated tools that can make the evaluation process easier and cheaper.

As new security vulnerabilities, issues in this specification, and challenges in implementation are discovered, we hope they will lead to both feedback and increased participation in the [Enterprise Ethereum Alliance](https://entethalliance.org)'s [EthTrust Security Levels Working Group](https://entethalliance.org/groups/EthTrust/) or its successors, responsible for developing and maintaining this specification.

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

EEA members are encouraged to provide feedback through joining the Working Group. Anyone can also provide feedback through the [Ethtrust-public Github repository](https://github.com/entethalliance/EthTrust-public), or by emailing the Editor at [EEA Editor](https://entethalliance.org/cdn-cgi/l/email-protection#fb9e9f928f9489bb9e958f9e8f939a9797929a95989ed594899c) and it will be forwarded to the Working Group as appropriate.

We expect that new vulnerabilities will be discovered after this specification is published. To ensure that we consider them for inclusion in a revised version, we welcome notification of them. EEA has created a specific email address to let us know about new security vulnerabilities: [\[email protected\]](https://entethalliance.org/cdn-cgi/l/email-protection#a1d2c4c2d4d3c8d5d88ccfced5c8c2c4d2e1c4cfd5c4d5c9c0cdcdc8c0cfc2c48fced3c6). Information sent to this address *SHOULD* be sufficient to identify and rectify the problem described, and *SHOULD* include references to other discussions of the problem. It will be assessed by EEA staff, and then forwarded to the Working Group to address the issue.

When these vulnerabilities affect the Solidity compiler, or suggest modifications to the compiler that would help mitigate the problem, the Solidity Development community *SHOULD* be notified, as described in \[<a href="index.html#bib-solidity-reports" class="bibref" data-link-type="biblio" title="Reporting a Vulnerability, in Security Policy">solidity-reports</a>\].

## 2. Conformance<a href="index.html#conformance" class="self-link" aria-label="§"></a>

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) \[<a href="index.html#bib-rfc2119" class="bibref" data-link-type="biblio" title="Key words for use in RFCs to Indicate Requirement Levels">RFC2119</a>\] \[<a href="index.html#bib-rfc8174" class="bibref" data-link-type="biblio" title="Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words">RFC8174</a>\] when, and only when, they appear in all capitals, as shown here.

This specification defines a number of requirements. As described in <a href="index.html#sec-reading-requirements" class="sec-ref">§ 1.1.3 How to Read a Requirement</a>, each requirement has a Security Level (**\[S\]**, **\[M\]**, or **\[Q\]**), and a statement of the requirement that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet.

In order to achieve <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at a specific Security Level, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* meet **all the requirements for that Security Level**, including all the requirements for lower Security Levels. Some requirements can either be met directly, or by meeting one or more <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding requirements</a> that mean the requirement is considered met.

This document does not create an affirmative duty of compliance on any party, though requirements to comply with it could be created by contract negotiations or other processes with prospective customers or investors.

Section <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a>, contains further recommendations. Although they are formatted similarly to requirements, they begin with a "level" marker **\[GP\]**. There is no requirement to test for these; however careful implementation and testing is *RECOMMENDED*.

Note that good implementation of the <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a> can enhance security, but in some cases incomplete or low-quality implementation could **reduce** security.

### 2.1 Conformance Claims<a href="index.html#sec-conformance-claims" class="self-link" aria-label="§"></a>

To grant <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> EEA EthTrust Certification, an auditor provides a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>, that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirements of the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> for which it is certified.

There is no required format for a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid conformance claim</a> for Version 1 or Version 2 of this specification, beyond being legible and containing the required information as specified in this section.

Note: Machine-readable formats

The Working Group believes that a standard machine-readable format for Conformance Claims would be useful, and seeks feedback on this question as well as concrete proposals for such a format, which *MAY* be adopted in a subsequent version.

A Valid Conformance Claim *MUST* include:

- The date on which the certification was issued, in 'YYYY-MM-DD' format.
- The <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> (of those listed at \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]) for which the certification is valid.
- The version of the EEA EthTrust Security Levels specification for which the contract is certified.
- A name and a URL for the organisation or software issuing the certification.
- The <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> ("**\[S\]**", "**\[M\]**", or "**\[Q\]**") that the <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> claims.
- A list of the requirements which were tested and a statement for each one, noting whether the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. This *MAY* include further information.
- An explicit notice stating that <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> does not provide any warranty or formal guarantee
  - of the overall security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, nor
  - that the project is free from bugs or vulnerabilities. This notice *SHOULD* state that <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> represents the best efforts of the issuer to detect and identify certain known vulnerabilities that can affect Smart Contracts.
- For conformance claims where certification is granted because the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> met an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> or a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, the conformance claim *MUST* include the results for the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a> met, and *MAY* omit the results for the requirement(s) whose results were thus unnecessary to determine conformance.

The following items *MUST* be part of a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>. A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* make them available as a link to the relevant documentation, in which case the Conformance Claim *MUST* also include a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of all documents linked for this purpose:

- The compiler options applied for each compilation.
- The contract metadata generated by the compiler.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> for <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> *MUST* include:

- a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the documentation provided to meet [**\[Q\] Document Contract Logic**](index.html#req-3-documented) and [**\[Q\] Document System Architecture**](index.html#req-3-document-system), and
- A bounded range of Solidity Compiler Versions for which the certification is valid. Note that this range *MAY* differ from the range declared in `pragama` directives present in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *SHOULD* include:

- A contact address for feedback such as questions about or challenges to the certification.
- Descriptions of conformance to the good practices described in <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a>.

A <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* include:

- An address where a \[<a href="index.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the conformance claim has been recorded on an identified network, e.g. Ethereum Mainnet.
- An address of the contract deployed on an identified network, e.g. Ethereum Mainnet.

Valid values of EVM versions are those listed in the Solidity documentation \[<a href="index.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]. At the date of publication the two most recent are `cancun` (the current default) and `prague` (an experimental version).

### 2.2 Who can offer EEA EthTrust Certification?<a href="index.html#who-can-audit" class="self-link" aria-label="§"></a>

*This section is non-normative.*

This version of the specification does not make any restrictions on who can perform an audit and provide <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. There is no certification process defined for auditors or tools who grant certification. This means that reviewers' claims of performing accurate tests are made by themselves. There is always a possibility of fraud, misrepresentation, or incompetence on the part of anyone who offers <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for Version 2.

Note

In principle anyone can submit a smart contract for verification. However submitters need to be aware of any restrictions on usage arising from copyright conditions or the like. In addition, meeting certain requirements can be more difficult to demonstrate in a situation of limited control over the development of the smart contract.

The Working Group expects its own members, who wrote the specification, to behave to a high standard of integrity and to know the specification well, and notes that there are many others who also do so.

The Working Group or EEA *MAY* seek to develop an auditor certification program for subsequent versions of the EEA EthTrust Security Levels Specification.

### 2.3 Identifying what is certified<a href="index.html#sec-source-and-contracts" class="self-link" aria-label="§"></a>

An EEA EthTrust evaluation is performed on Tested Code, which means the Solidity source code for a smart contract or several related smart contracts, along with the bytecode generated by compiling the code with specified parameters.

If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is divided into more than one smart contract, deployable at different addresses, it is referred to as a Set Of Contracts.

## 3. Security Considerations<a href="index.html#sec-security-considerations" class="self-link" aria-label="§"></a>

*This section is non-normative.*

Security of information systems is a major field of work. There are risks inherent in any system of even moderate complexity.

This specification describes testing for security problems in Ethereum smart contracts. However there is no such thing as perfect security. EEA EthTrust Certification means that at least a defined minimum set of checks has been performed on a smart contract. **This does not mean the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> definitely has no security vulnerabilities**. From time to time new security vulnerabilities are identified. Manual auditing procedures require skill and judgement. This means there is always a possibility that a vulnerability is not noticed in review.

### 3.1 Smart Contracts in context - broader considerations<a href="index.html#sec-eth-broader-considerations" class="self-link" aria-label="§"></a>

Ethereum is based on a model of account holders authorising transactions between accounts. It is very difficult to stop a malicious actor with a privileged key from using that to cause undesirable or otherwise bad outcomes.

Likewise, in practice users often interact with smart contracts through a "Ðapp" or "distributed app", whose user interface is a Web Application. Web Application Security is its own extensive area of research and development, beyond the scope of this specification.

### 3.2 Upgradable Contracts<a href="index.html#sec-proxy-contract-considerations" class="self-link" aria-label="§"></a>

Smart contracts in Ethereum are immutable by default. However, for some scenarios, it is desirable to modify them, for example to add new features or fix bugs. An Upgradable Contract is any type of contract that fulfills these needs by enabling changes to the code executed via calls to a fixed address.

Some common patterns for Upgradable Contracts use a Proxy Contract: a simple wrapper that users interact with directly that is in charge of forwarding transactions to and from another contract (called the Execution Contract in this document, but also known as a Logic Contract), which contains the code that actually implements the Smart Contract's behaviour.

The <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be replaced while the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>, acting as the access point, is never changed. Both contracts are still immutable in the sense that their code cannot be changed, but one <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can be swapped out with another. The <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> can thus point to a different implementation and in doing so, the software is "upgraded".

This means that a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> that follow this pattern to make an <a href="index.html#dfn-upgradable-contract" class="internalDFN" data-link-type="dfn">Upgradable Contract</a> generally cannot be considered immutable, as the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> itself could redirect calls to a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a>, which could be insecure or malicous. By meeting the requirements for [access control](index.html#sec-3-access-control) in this specification to restrict upgrade capabilities enabling new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contracts</a> to be deployed, and by documenting upgrade patterns and following that documentation per [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), deployers of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can demonstrate reliability. In general, <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> of a <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a> does not apply to the internal logic of an Upgradable Contract, so a new <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> needs to be certified before upgrading to it through the <a href="index.html#dfn-proxy-contract" class="internalDFN" data-link-type="dfn">Proxy Contract</a>.

There are several possible variations on this core structure, for example having a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> that includes multiple <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contracts</a>. In the attack known as Metamorphic Upgrades, a series of Smart Contracts are used to convince people (e.g. voters in a DAO) to approve a certain piece of code for deployment, but one of the proxy contracts in the chain is updated to deploy different, malicious, code.

Other patterns rely on using the `CREATE2` instruction to deploy a Smart Contract at a known address. It is currently possible to remove the code at that address using the `selfdestruct()` method, and then deploy new code to that address. This possibility is sometimes used to save Gas Fees, but it is also used in Metamorphic Upgrade attacks.

### 3.3 Oracles<a href="index.html#sec-oracle-considerations" class="self-link" aria-label="§"></a>

A common feature of Ethereum networks is the use of Oracles: functions that can provide information sourced from on-chain or off-chain data. Oracles solve a range of problems, from providing random number generation to asset data, managing the operation of liquidity pools, and enabling access to weather, sports, or other special-interest information. Oracles are used heavily in DeFi and gaming, where asset data and randomization are central to protocol design.

This specification contains requirements to check that smart contracts are sufficiently robust to deal appropriately with whatever information is returned, including the possibility of malformed data that can be deliberately crafted for oracle-specific attacks.

While some aspects of <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are within the scope of this specification, it is still possible that an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> provides misinformation or even actively produces harmful disinformation.

The two key considerations are the risk of corrupted or manipulated data, and the risk of oracle failure. Vulnerabilities related to these considerations - excessive reliance on <a href="index.html#dfn-twap" class="internalDFN" data-link-type="dfn">TWAP</a>, and unsafe management of oracle failure - have occurred repeatedly leading to the loss of millions of dollars of value on various DeFi protocols.

While many high-quality and trusted <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are available, it is possible to suffer an attack even with legitimate data. When calling on an Oracle, data received needs to be checked for staleness to avoid <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-running</a> attacks. Even in non-DeFi scenarios, such as a source of randomness, it is often important to reset the data source for each transaction, to avoid arbitrage on the next transaction.

A common strategy for pricing Oracles is to provide a time-weighted average price (known as TWAP). This provides some level of security against sudden spikes such as those created by a Flashloan attack, but at the cost of providing stale information.

It is important to choose time windows carefully: when a time window is too wide, it won't reflect volatile asset prices, leaking opportunities to arbitrageurs. However the "instantaneous" price of an asset is often not a good data point: It is the most manipulable piece of Oracle data, and in any event it will almost always be stale by the time a transaction is executed.

Oracles that collate a wide variety of source data, clean outliers from their data, and are well-regarded by the community, are more likely to be reliable. If an Oracle is off-chain, whether it reflects stale on-chain data or reliable and accurate data that is truly off-chain is an important consideration.

Even an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> using a well-chosen <a href="index.html#dfn-twap" class="internalDFN" data-link-type="dfn">TWAP</a> can enable a liquidity pool or other DeFi structure to be manipulated, especially by taking advantage of flashloans and flashswaps to cheaply raise funds. If an asset targeted for manipulation has insufficient liquidity this can render it vulnerable to large price swings by an attacker holding only a relatively small amount of liquidity.

The second important consideration when using <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> is that of a graceful failure scenario. What happens if an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> no longer returns data, or suddenly returns an unlikely value? At least one protocol has suffered losses due to 'hanging' on a minimum value in the rare event of a price crash rather than truly dropping to zero, with traders who accumulated large amounts of a near zero-priced asset able to sell it back to the protocol. Hardcoding a minimum or maximum value can lead to problems reflecting reality.

### 3.4 External Interactions and Re-entrancy Attacks<a href="index.html#sec-reentrancy-considerations" class="self-link" aria-label="§"></a>

Code that relies on external code can introduce multiple attack vectors. This includes cases where an external dependency contains malicious code or has been subject to malicious manipulation through security vulnerabilities. However, failure to adequately manage the possible outcomes of an external call can also introduce security vulnerabilities.

One of the most commonly cited vulnerabilities in Ethereum Smart Contracts is Re-entrancy Attacks. These attacks allow malicious contracts to make a call back into the contract that called it before the originating contract's function call has been completed. This effect causes the calling contract to complete its processing in unintended ways, for example, by making unexpected changes to its state variables.

While the \[c-e-i\] implementation pattern provides crucial protection, emerging cross-contract interaction patterns may require additional safeguards. Regular review of interaction patterns can help identify new reentrancy vectors.

A Read-only Re-entrancy Attack arises when a view function reads a state that will subsequently be changed. These are a particular additional danger because such functions often lack safeguards since they don't modify the contract's state. However, if the state is inconsistent, incorrect values could be reported. This deception can mislead other protocols into reading inaccurate state values, potentially leading to unintended actions or outcomes.

This issue can affect other contracts that rely on the accurate reporting of state from these view functions, as well as the contract itself being re-entered. Consequently, third parties that call a Smart Contract, and protocols that are composed of a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a> are potentially vulnerable to Read-only Re-entrancy.

<a href="index.html#example-7-rari-a-read-only-re-entrancy-attack" class="self-link">Example 7</a>: Rari: a read-only re-entrancy attack

In the Rari hack a large flashloaned deposit was made in order to borrow ETH from the cETH contract. During the borrow call, `exitMarket()` was called within the Comptroller, which reads the state of the cETH contract, performing read-only re-entrancy of cETH. Since the cETH contract’s state had not yet recorded the borrow, the attacker was able to redeem their initial deposit while keeping their borrowed funds. For more information on the hack, see \[<a href="index.html#bib-certik-rari" class="bibref" data-link-type="biblio" title="Fei Protocol Incident Analysis">certik-rari</a>\].

### 3.5 Signature Mechanisms<a href="index.html#sec-signature-considerations" class="self-link" aria-label="§"></a>

Some requirements in the document refer to Malleable Signatures. These are signatures created according to a scheme constructed so that, given a message and a signature, it is possible to efficiently compute the signature of a different message - usually one that has been transformed in specific ways. While there are valuable use cases that such signature schemes allow, if not used carefully they can lead to vulnerabilities, which is why this specification seeks to constrain their use appropriately. In a similar vein, Hash Collisions could occur for hashed messages where the input used is malleable, allowing the same signature to be used for two distinct messages.

Other requirements in the document are related to exploits which take advantage of ambiguity in the input used to created the signed message. When a signed message does not include enough identifying information concerning where, when, and how many times it is intended to be used, the message signature could be used (or reused) in unintended functions, contracts, chains, or at unintended times.

For more information on this topic, and the potential for exploitation, see also \[<a href="index.html#bib-chase" class="bibref" data-link-type="biblio" title="Malleable Signatures: New Definitions and Delegatable Anonymous Credentials">chase</a>\].

### 3.6 Gas and Gas Prices<a href="index.html#sec-gas-considerations" class="self-link" aria-label="§"></a>

Gas Griefing is the deliberate abuse of the Gas mechanism that Ethereum uses to regulate the consumption of computing power, to protect against unexpected or adverse outcome such as a Denial of Service attack. Because Ethereum is designed with the Gas mechanism as a regulating feature, it is insufficient to simply check that a transaction has enough Gas; checking for Gas Griefing needs to take into account the goals and business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements.

Gas Siphoning is another abuse of the Gas mechanism that Ethereum uses to regulate the consumption of computing power, where attackers steal Gas from vulnerable contracts either to deny service or for their own gain (e.g. to mint <a href="index.html#dfn-gas-tokens" class="internalDFN" data-link-type="dfn">Gas Tokens</a>). Similar to Gas Griefing, checking for Gas Siphoning requires careful consideration of the goals and business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements.

Gas Tokens use Gas when minted and free slightly less Gas when burned, provided the EVM refunds a sufficient quantity of Gas for clearing the state. Gas Tokens minted when Gas prices are low can be burned to subsidize Ethereum transactions when Gas prices are high. On Ethereum's main chain, Gas refunds were removed with the London hard fork that deployed \[<a href="index.html#bib-eip-3529" class="bibref" data-link-type="biblio" title="Reduction in Refunds">EIP-3529</a>\] in August 2021, effectively disabling Gas Tokens.

In addition, a common feature of Ethereum network upgrades is to change the Gas Price of specific operations. <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> only applies for the <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version(s)</a> specified; it is not valid for other <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>. Thus it is important to recheck code to ensure its security properties remain the same across network upgrades, or take remedial action.

### 3.7 MEV (Maliciously Extracted Value)<a href="index.html#sec-mev-considerations" class="self-link" aria-label="§"></a>

MEV, used in this document to mean "Maliciously Extracted Value", refers to the potential for block producers or other paticipants in a blockchain to extract value that is not intentionally given to them, in other words to steal it, by maliciously reordering transactions, as in <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>, or suppressing them.

<a href="index.html#example-8-an-mev-attack" class="self-link">Example 8</a>: An MEV attack

A Smart Contract promises an award for the first transaction that answers a question. A block producer can steal the answer from another transaction, then drop all other transactions with the answer from the block.

Note

The term MEV is commonly expanded as "Miner Extracted Value", and sometimes "Maximum Extractable Value". Often, as in the example above, block producers can take best advantage of a vulnerability.

However MEV can be exploited by other participants who do not produce blocks themselves.

In addition, some extraction of value is essentially block producers taking expected advantage of known arbitrage opportunities in order to provide a more predictably efficient market.

Some MEV attacks can be prevented by careful consideration of the information that is included in a transaction, including the parameters required by a contract.

Other mitigation strategies include those that protect against <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>.

The Ethereum Foundation maintains a set of information resources regarding MEV \[<a href="index.html#bib-ef-mev" class="bibref" data-link-type="biblio" title="Maximal Extractable Value (MEV)">EF-MEV</a>\].

### 3.8 Ordering Attacks<a href="index.html#sec-ordering-considerations" class="self-link" aria-label="§"></a>

Various attacks are related to a malicious rearrangement of transactions in a block,for example by reordering, censoring, or inserting particular transactions. While a primary motivation for this attack class is to facilitate <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks, they can also be used to set up conditions for other types of attack.

Warning

<a href="index.html#example-9-ordering-attacks" class="self-link">Example 9</a>: Ordering Attacks

The setup period of a voting contract can sometimes be exploited by maliciously suppressing or front-running voting option proposals to limit the number of candidates eligible in the voting stage. A block proposer can maliciously schedule such a voting initialization period when they know they will produce a sequence of blocks.

There are various types of Ordering Attacks:

Censorship Attacks
A block processor actively suppresses a proposed transaction, for their own benefit.

Front-Running
Based on transactions that are visible before they are added to a block, allowing a malicious participant to submit an alternative transaction, frustrating the aim of the original transaction.

<a href="index.html#example-10-front-running-attack-strategy" class="self-link">Example 10</a>: Front Running Attack strategy

In a system designed to attest original authorship, a malicious participant uses the information in a claim of authorship to create a rival claim, and adds their claim to a block first providing grounds for them to falsely claim to be the author.

Implemented on a repeated basis this is an effective Denial of Service (DoS) attack against the service itself.

Back-Running
Similar to <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-Running</a>, except the attacker places their transactions after the one they are attacking.

Sandwich Attacks
An attacker places a victim's transaction undesirably between two other transactions.

<a href="index.html#example-11-sandwich-attack-strategy" class="self-link">Example 11</a>: Sandwich Attack strategy

An attacker creates a swap transaction to buy a particular token, insert it block before a victim's buy transaction, artificially driving the price up for the victim, and insert a corresponding sell transaction at the increased valuation, providing no-risk profit for the attacker at the victim's expense.

### 3.9 Source code, pragma, and compilers<a href="index.html#sec-source-compiler-considerations" class="self-link" aria-label="§"></a>

This version of the specification requires the compiled bytecode as well as the Solidity Source Code that together constitute the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Solidity is by a large measure the most common programming language for Ethereum smart contracts, and benefits of requiring source code in Solidity include that it simplifies a number of tests, and that there is substantial security research done on Solidity source code.

Solidity allows the source code to specify the Solidity compiler version used with a `pragma` statement. This specification does not require any particular Solidity compiler version, so long as it is no older than 0.3.0, but at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> it only allows <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for a bounded set of Solidity compiler versions, where it is known that those Solidity compiler versions produce identical bytecode from the given source code if compiled with the same options.

There are some drawbacks to requiring Solidity Source code. The most obvious is that some code that is not written in Solidity. Different languages have different features and often support different coding styles.

Perhaps more important, it means that a deployed contract written in Solidity cannot be tested directly without someone making the source code available.

Another important limitation introduced by reading source code is that it is subject to <a href="index.html#dfn-homoglyph-attacks" class="internalDFN" data-link-type="dfn">Homoglyph Attacks</a>, where characters that look the same but are different such as Latin "p" and Cyrillic "р", can deceive people visually reading the source code, to disguise malicious behaviour. There are related attacks that use features such as <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode Direction Control Characters</a> or take advantage of inconsistent normalisation of combining characters to achieve the same type of deceptions.

### 3.10 Contract Deployment<a href="index.html#sec-deployment-considerations" class="self-link" aria-label="§"></a>

This specification primarily addresses vulnerabilities that arise in Smart Contract code. However it is important to note that the deployment of a smart contract is often a crucial element of protocol operation. Some aspects of smart contract security primarily depend on how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> gets deployed. Even audited protocols can be easily exploited if deployed naively.

Code written for a specific blockchain might depend on features available in that blockchain. When the code is deployed to a different chain that is compatible, the difference in features can expose a vulnerability. For any contract deployed to a blockchain or parachain that uses a patched fork of the EVM, common security assumptions might no longer apply at the VM level. It is valuable to deploy <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certified</a> contracts to a testnet for each chain first, and undergo thorough penetration testing.

Of particular concern is the issue of <a href="index.html#dfn-upgradable-contract" class="internalDFN" data-link-type="dfn">Upgradable Contracts</a>, and any contract with an initializer function in deployment. Many protocols have been hacked due to accidentally leaving their initializer functions unprotected, or using a non-atomic deployment in which the initializing function is not called in the same transaction as the contract deployment. This scenario is ripe for <a href="index.html#dfn-front-running" class="internalDFN" data-link-type="dfn">Front-running</a> attacks, and can result in protocol takeover by malicious parties, and theft or loss of funds. Initializing a contract in the same transaction as its deployment reduces the risk that a malicious actor takes control of the contract.

Moreover, the deployment implications of assigning access roles to `msg.sender` or other variables in constructors and initializers need careful consideration. This is discussed further in <a href="index.html#sec-3-access-control" class="sec-ref">§ 5.3.2 Access Control</a> requirements.

Several libraries and tools exist specifically for safe proxy usage and safe contract deployment. From command-line tools to libraries to sophisticated UI-based deployment tools, many solutions exist to prevent unsafe proxy deployments and upgrades.

Using access control for a given contract's initializer, and limiting the number of times an initializer can be called on or after deployment, can enhance safety and transparency for the protocol itself and its users. Furthermore, a function that disables the ability to re-initialize an <a href="index.html#dfn-execution-contract" class="internalDFN" data-link-type="dfn">Execution Contract</a> can prevent any future initializer calls after deployment, preventing later attacks or accidents.

Although this specification does not require that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> has been deployed, some requirements are more easily tested when code has been deployed to a blockchain, or possibly in some cases can only be thoroughly tested "*in situ*".

### 3.11 Post-deployment Monitoring<a href="index.html#sec-realtime-monitoring-considerations" class="self-link" aria-label="§"></a>

While monitoring Smart Contracts after deployment is beyond the formal scope of this specification, it is an important consideration for Smart Contract security. New attack techniques arise from time to time, and some attacks can only be prevented by active measures implemented in real time. Monitoring of on-chain activity can help detect attacks before it is too late to stop them.

Monitoring, backed by an automated dataset, can enable identifying an attack that has occurred elsewhere, even on other blockchains.

Automated monitoring can facilitate rapid response, producing alerts or automatically initiating action, improving the security of contracts that might be compromised when security responses are delayed by even a few blocks.

However, it can be difficult to determine the difference between an attack and anamolous behaviour on the part of individuals. Relying purely on automated monitoring can expose a blockchain to the risk that a malicious actor deliberately triggers an automated security response to damage a blockchain or project, analogous to a Denial of Service attack.

### 3.12 Network Upgrades<a href="index.html#sec-netupgrades-considerations" class="self-link" aria-label="§"></a>

The EVM, or Ethereum Virtual Machine, acts as a distributed state machine for the Ethereum network, computing state changes resulting from transactions. The EVM maintains the network state for simple transfers of Ether, as well as more complex Smart Contract interactions. In other words, it is the "computer" (although in fact it is software) that runs the code of Smart Contracts.

From time to time the Ethereum community implements a Network Upgrade, sometimes also called a Hard Fork. This is a change to Ethereum that is backwards-incompatible. Because they *typically* change the EVM, Ethereum Mainnet <a href="index.html#dfn-network-upgrade" class="internalDFN" data-link-type="dfn">Network Upgrades</a> generally correspond to <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>.

A <a href="index.html#dfn-network-upgrade" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can affect more or less any aspect of Ethereum, including changing EVM opcodes or their Gas price, changing how blocks are added, or how rewards are paid, among many possibilities.

Because <a href="index.html#dfn-network-upgrade" class="internalDFN" data-link-type="dfn">Network Upgrades</a> are not guaranteed to be backwards compatible, a newer <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM version</a> can process bytecode in unanticipated ways. If a <a href="index.html#dfn-network-upgrade" class="internalDFN" data-link-type="dfn">Network Upgrade</a> changes the EVM to fix a security problem, it is important to consider that change, and it is a good practice to follow that upgrade.

Because claims of conformance to this specification are only valid for specific <a href="index.html#dfn-evm-version" class="internalDFN" data-link-type="dfn">EVM versions</a>, a <a href="index.html#dfn-network-upgrade" class="internalDFN" data-link-type="dfn">Network Upgrade</a> can mean an updated audit is needed to maintain valid <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for a current Ethereum network.

Network Upgrades typically only impact a few features. This helps limit the effort necessary to audit code after an upgrade: often there will be no changes that affect the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, or review of a small proportion that is the only part affected by a Network Upgrade will be sufficient to renew <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>.

### 3.13 Organizational and Off-Chain Security Posture<a href="index.html#sec-organizational-security" class="self-link" aria-label="§"></a>

Smart contract security extends beyond code to encompass organizational processes and off-chain infrastructure. A comprehensive security strategy needs to address both technical and operational aspects of protocol management.

Operational Security Measures
- Hardware security modules (HSMs) for critical key storage
- Multi-signature schemes with distributed key holders
- Regular security training for all team members
- Secure development environment protocols

Infrastructure Security
- Protected deployment infrastructure
- Secure communication channels
- Access control systems
- Network security monitoring

Monitoring and Response
- Real-time transaction monitoring
- Automated alerting systems
- Incident response procedures
- Emergency shutdown capabilities

Organizations aiming to follow best practices will implement:

- Regular security assessments of both on-chain and off-chain systems
- Documented incident response plans with clear roles and responsibilities
- Periodic penetration testing of infrastructure
- Security awareness training programs
- Access control reviews and updates

<a href="index.html#example-12-security-operations-example" class="self-link">Example 12</a>: Security Operations Example

A robust security operations center (SOC) will monitor for:

- Unusual transaction patterns
- Suspicious administrative actions
- Infrastructure security alerts
- Smart contract anomalies

Note: Continuous Security

Security is an ongoing process requiring regular assessment and updates to match evolving threats and organizational changes. Regular drills and updates to security procedures help maintain operational readiness.

### 3.14 Preempting On-Chain Adversarial Conditions<a href="index.html#sec-adversarial-simulation" class="self-link" aria-label="§"></a>

Smart contracts operate in a highly adversarial environment where network conditions, external data sources, and economic incentives can be manipulated by malicious actors. Simulating these attack scenarios during pre-deployment is crucial for identifying vulnerabilities that may not manifest under standard testing conditions.

Key adversarial scenarios to simulate include:

Network Manipulation
- Extreme gas price fluctuations
- Deliberate network congestion
- Strategic transaction ordering by miners
- Block timestamp manipulation

Oracle Attacks
- Price feed manipulation through flash loans
- Delayed or stale data scenarios
- Multiple oracle failure modes
- Cross-chain oracle inconsistencies

Economic Warfare
- Extreme asset price volatility
- Liquidity pool manipulation
- Token economic attacks
- Arbitrage exploitation

Governance Exploitation
- Token voting manipulation
- Proposal flooding attacks
- Timing attacks on voting periods
- Malicious parameter updates

Standard testing environments often fail to capture the complex interactions between these adversarial conditions. Protocols that appear secure under controlled testing may harbor critical vulnerabilities that only emerge when multiple attack vectors are combined or when economic incentives are sufficiently large.

Note: Dynamic Testing Environmen

Testing these scenarios requires dynamic environments that can simulate complex market conditions and actor behaviors. Simple unit tests or static analysis tools cannot adequately model these adversarial situations.

By modeling these scenarios during pre-deployment, developers can:

- Identify edge cases in economic models
- Validate circuit breaker mechanisms
- Test emergency shutdown procedures
- Verify governance safeguards
- Assess protocol resilience under stress

## 4. Testing Methodologies<a href="index.html#sec-testing-methods" class="self-link" aria-label="§"></a>

*This section is non-normative.*

There are a number of common approaches to testing security. This specification anticipates multiple approaches being used, but in general does not explicitly require any specific testing style. However, a thorough security evaluation will cover different approaches. While these methods will be used to assess <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>, they can also be used by developers to ensure their code does not contain known vulnerabilities. Doing so can produce higher-quality code, and contribute to a reduced cost for security review, or ensure that the expertise of security reviewers is focused on complex issues that are hard to identify, significantly improving the value of the review.

Some common testing methods:

### 4.1 Unit Testing<a href="index.html#sec-testing-unit" class="self-link" aria-label="§"></a>

The practice of Unit Testing is based on many individual tests, each testing a specific requirement. This approach can be incorporated into Test-driven Development, where tests are written alongside the development of code, and added to a set of unit tests, to ensure that changes do not introduce problems that had previously been considered resolved or had not existed.

An important factor in the value of Unit Testing is Test Coverage: ensuring that there are enough Unit Tests to cover the range of possibilities being tested for. In many cases, this means not just ensuring each requirement has a test, but that each way of triggering a requirement has a test. For example, it is possible to include a `tx.origin` statement directly in smart contract code, but it is also possible to include it using `assembly {}`. Unless a single test covers both cases, there is not sufficient <a href="index.html#dfn-test-coverage" class="internalDFN" data-link-type="dfn">Test Coverage</a> of the specific requirement not to use `tx.origin`

Unit Testing is regularly automated by building a test harness that ensures the Unit Tests are run whenever something is changed, whether smart contract code, or the environment in which it is operating, including integration with new services or systems.

### 4.2 Static Analysis<a href="index.html#sec-testing-static" class="self-link" aria-label="§"></a>

Static Analysis is examining the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> directly to identify potential issues, and determine whether they need to be addressed. In this specification, all issues at <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> are believed to be discoverable using automated Static Analysis, and a number of software tools exist that will assess various aspects of smart contracts.

The EEA's EthTrust Security Levels Working Group, producer of this specification, has begun to collect information about such tools, as well as test cases that can be used to determine whether they accurately detect different aspects of a particular requirement.

Static Analysis is also regularly performed manually. This approach takes advantage of the experience and creativity of an expert to identify potential issues arising from the way code is written. The Working Group believes that manual Static Analysis is sufficient to determine whether <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets requirements at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> in this specification.

### 4.3 Fuzzing<a href="index.html#sec-testing-fuzzing" class="self-link" aria-label="§"></a>

Fuzzing is an automated software testing method that repeatedly activates a contract, with a variety of inputs to reveal defects and potential security vulnerabilities.

Fuzzing relies on a Corpus - A set of inputs for a fuzzing target. The value of fuzzing ultimately depends in large part on the quality of the Corpus. It is important to maintain the Corpus to maximise code coverage, and helpful to prune unnecessary or duplicate inputs for efficiency.

Different Fuzzing styles are often described according how the Corpus is adapted specifically to the codebase, and to generally known and expected usage patterns:

Black-Box Fuzzing:

White-Box Fuzzing:
Leverage full visibility into the source code and execution paths, using symbolic execution or test instrumentation to guide input generation. White-box fuzzing can more effectively pinpoint intricate logic flaws and subtle state-dependent vulnerabilities.

Gray-Box Fuzzing
Combine elements of both black-box and white-box methodologies, using limited instrumentation or lightweight heuristics to guide test input generation. This often strikes a balance between thoroughness and efficiency, uncovering a wide range of potential issues without the complexity of full white-box methods.

### 4.4 Mutation Testing<a href="index.html#sec-testing-mutation" class="self-link" aria-label="§"></a>

Mutation Testing is a fault-based testing technique that introduces artificial defects (mutations) into the source code to evaluate the effectiveness of test cases. If the test suite detects the mutation, it is considered "killed"; otherwise, the mutation "survives," indicating potential gaps in test coverage.

There are various categories of Mutation that can be useful for testing smart contracts, including:

State Variable Mutations:
Modifying state variable declarations and operations.

Arithmetic Mutations:
Altering arithmetic operations to test numerical calculations. examples include:

- Replacing operators (+, -, \*, /)
- Modifying boundary conditions
- Introducing overflow/underflow conditions

Control Flow Mutations:
Changing execution paths, for example:

- Inverting conditional statements
- Modifying loop conditions
- Altering function modifiers

Access Control Mutations:
Varying security-critical permission checks, such as:

- Removing ownership checks
- Altering role-based permissions
- Modifying authentication logic

Mutation testing relies on a Mutation Score - the ratio of killed mutations to the total number of non-equivalent mutations. It is important to maintain high mutation scores for critical contract components, though achieving 100% can be impractical due to equivalent mutations and implementation constraints.

Many tools and mutation operators can help to implement mutation testing effectively. A good practice to leverage and build on public resources where possible, always checking licensing restrictions.

Another important part of Mutation Testing is the set of equivalence rules that help identify mutations that don't meaningfully change the contract behavior. These rules help reduce the testing effort by eliminating mutations that cannot reveal defects. This approach complements <a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> by providing a different perspective on test suite quality.

### 4.5 Symbolic Execution<a href="index.html#sec-testing-symbolic" class="self-link" aria-label="§"></a>

Symbolic Execution analyzes a program by tracking symbolic rather than actual values (much like using a variable whose value is unknown in algebra instead of a specific number). The results are a set of constraints on possible outcomes, that can be tested to check for possible vulnerabilities. The procedure can also identify code that is never called, variables that are unused, etc.

For more information on Symbolic Execution, see \[<a href="index.html#bib-wse" class="bibref" data-link-type="biblio" title="Symbolic Execution">WSE</a>\]

### 4.6 Formal Verification<a href="index.html#sec-testing-formal" class="self-link" aria-label="§"></a>

Formal Verification is a family of techniques that mathematically prove certain properties of code. It has been used in applications such as embedded systems. There are many uses for formal verification in smart contracts, such as testing liveness, protocol invariants for safety at a high level, or proving narrower, more specific properties of a program's execution.

In formal verification, a formal (symbolic or mathematical) specification of the expected or desired outcome of a smart contract is created, enabling a formal mathematical proof of a protocol's correctness. The smart contract itself is often translated into another language for this purpose.

Several languages and programs exist for creating formal verification proofs, some with the explicit aim of making formal verification more accessible to casual users and non-mathematicians. Please see \[<a href="index.html#bib-ef-sl" class="bibref" data-link-type="biblio" title="Specification languages for creating formal specifications">EF-SL</a>\] for some examples.

When done correctly, formal verification can make guarantees that methods such as <a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> and <a href="index.html#dfn-static-analysis" class="internalDFN" data-link-type="dfn">Static Analysis</a> cannot. However, its accuracy depends on correctly modelling the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, and selecting appropriate properties to test. This task usually needs substantial expertise, and if the model does not accurately reflect the properties of the original <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> the results derived might likewise not apply.

The immutable nature of many smart contracts makes formal verification appealing.

### 4.7 Properties and Invariants<a href="index.html#sec-testing-properties" class="self-link" aria-label="§"></a>

Property-Based Testing is a common approach used in concert with multiple methodologies, where test cases are generated based on properties or invariants that should hold true for the system, allowing for automated exploration of a wide range of inputs and scenarios.

Invariant Testing is a subset of <a href="index.html#dfn-property-based-testing" class="internalDFN" data-link-type="dfn">Property-Based Testing</a>, that tests whether assumptions about Invariants hold true. Invariants are specific properties that are expected to remain true in all circumstances.

### 4.8 Testnet Deployment<a href="index.html#sec-testing-testnets" class="self-link" aria-label="§"></a>

Aside from <a href="index.html#dfn-static-analysis" class="internalDFN" data-link-type="dfn">Static Analysis</a>, many test methodologies rely on being able to execute <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Rather than deploying code directly to a blockchain where it is exposed, and may be used unintentionally with undesirable outcomes, a common practice is to deploy code on a Testnet, a blockchain that is created exclusively for testing, which is known to include smart contracts that can contain security vulnerabilities, and where the underlying cryptocurrencyand thus gas have a zero or negligible cost.

## 5. EEA EthTrust Security Levels<a href="index.html#sec-levels" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is available at three Security Levels. The Security Levels describe minimum requirements for certifications at each Security Level: **\[S\]**, **\[M\]**, and **\[Q\]**. These Security Levels provide successively stronger assurance that a smart contract does not have specific security vulnerabilities.

- [Security Level \[S\]](index.html#sec-levels-one) is designed so that for most cases, where common features of Solidity are used following well-known patterns, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be certified by an automated "static analysis" tool.
- [Security Level \[M\]](index.html#sec-levels-two) mandates a stricter static analysis. It includes requirements where a human auditor is expected to determine whether use of a feature is necessary, or whether a claim about the security properties of code is justified.
- [Security Level \[Q\]](index.html#sec-levels-three) provides analysis of the business logic the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> implements, and that the code not only does not exhibit known security vulnerabilities, but also correctly implements what it claims to do.

The optional <a href="index.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a>, correctly implemented, further enhance the Security of smart contracts. However it is not necessary to test them to conform to this specification.

Note

This scheme has been compared to the conformance approach used in the "OWASP Application Security Verification Standard" specification family \[<a href="index.html#bib-asvs" class="bibref" data-link-type="biblio" title="OWASP Application Security Verification Standard">ASVS</a>\]. There are some clear differences, largely resulting from the differences between the general applicability ASVS aims to achieve, and this specification's very precise focus on testing the security of Ethereum smart contracts written in Solidity.

The vulnerabilities addressed by this specification come from a number of sources, including Solidity Security Alerts \[<a href="index.html#bib-solidity-alerts" class="bibref" data-link-type="biblio" title="Solidity Blog - Security Alerts">solidity-alerts</a>\], the Smart Contract Weakness Classification \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], TMIO Best practices \[<a href="index.html#bib-tmio-bp" class="bibref" data-link-type="biblio" title="Best Practices for Smart Contracts (privately made available to EEA members)">tmio-bp</a>\], various sources of Security Advisory Notices, discussions in the Ethereum community and researchers presenting newly discovered vulnerabilities, and the extensive practical experience of participants in the Working Group.

### 5.1 Security Level \[S\]<a href="index.html#sec-levels-one" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> is intended to allow an unguided automated tool to analyze most contracts' bytecode and source code, and determine whether they meet the requirements. The requirements of <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> are designed to be testable using automated <a href="index.html#dfn-static-analysis" class="internalDFN" data-link-type="dfn">Static Analysis</a>. As of this version of the specification, the Working Group has begun to maintain a (registry of tools)\[\] that claim to provide coverage of specific requirements, as well as test cases and the results of running them in those tools. For more information see \[<a href="index.html#bib-et-tools" class="bibref" data-link-type="biblio" title="EEA EthTrust Tool Implementation Registry">ET-tools</a>\].

For some situations that are difficut to verify automatically, there are higher-level <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> that can be fulfilled instead to meet a requirement for this Security Level.

To be eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for Security Level \[S\], <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* fulfil all <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements, **unless** it meets the applicable **<a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement(s)</a>** for each <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement it does not meet directly.

**\[S\] Encode Hashes with `chainid`<a href="index.html#req-1-eip155-chainid" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* create hashes for transactions that incorporate `chainid` values following the recommendation described in \[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\]

\[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\] describes an enhanced hashing rule, incorporating a chain identifier in the hash. While this only provides a guarantee against replay attacks if there is a unique chain identifier, using the mechanism described provides a certain level of robustness and makes it much more difficult to execute a replay attack.

**\[S\] No `CREATE2`<a href="index.html#req-1-no-create2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction.
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

The `CREATE2` opcode provides the ability to interact with addresses that do not exist yet on-chain but could possibly eventually contain code. While this can be useful for deployments and counterfactual interactions with contracts, it can allow external calls to code that is not yet known or can be altered, and could turn out to be malicous or insecure due to errors or weak protections.

**\[S\] No `tx.origin`<a href="index.html#req-1-no-tx.origin" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)

`tx.origin` is a global variable in Solidity which returns the address of the account that sent the transaction. A contract using `tx.origin` can allow an authorized account to call into a malicious contract, enabling the malicious contract to pass authorization checks in unintended cases. It is better to use `msg.sender` for authorization instead of `tx.origin`.

See also [SWC-115](https://swcregistry.io/docs/SWC-115) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] for examples.

**\[S\] No Exact Balance Check<a href="index.html#req-1-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check).

Testing the balance of an account as a basis for some action has risks associated with unexpected receipt of ether or another token, including tokens deliberately transfered to cause such tests to fail as an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev), subsection <a href="index.html#sec-mev-considerations" class="sec-ref">§ 3.7 MEV (Maliciously Extracted Value)</a> of the Security Considerations for this specification, [SWC-132](https://swcregistry.io/docs/SWC-132) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] for examples, and improper locking as described in \[<a href="index.html#bib-cwe-667" class="bibref" data-link-type="biblio" title="CWE-667: Improper Locking">CWE-667</a>\].

**\[S\] No Hashing Consecutive Variable Length Arguments<a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

The elements of each variable-length argument to `abi.encodePacked()` are packed in order prior to hashing. <a href="index.html#dfn-hash-collisions" class="internalDFN" data-link-type="dfn">Hash Collisions</a> are possible by rearranging the elements between consecutive, variable length arguments while maintaining that their concatenated order is the same.

**\[S\] No `selfdestruct()`<a href="index.html#req-1-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, sending any Ether held by the contract, thus potentially stealing it. It is also possible to use it in combination with `CREATE2` to change the code at a particular address. This feature can break immutability and trustless guarantees to introduce numerous security issues. In addition, once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

`selfdestruct()` is officially deprecated, its usage discouraged, since Solidity compiler version 0.8.18 \[<a href="index.html#bib-solidity-release-818" class="bibref" data-link-type="biblio" title="Solidity 0.8.18 Release Announcement">solidity-release-818</a>\].

See also [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], \[<a href="index.html#bib-eip-6049" class="bibref" data-link-type="biblio" title="Deprecate SELFDESTRUCT">EIP-6049</a>\].

**\[S\] No `assembly {}`<a href="index.html#req-1-no-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly {}` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

The `assembly {}` instruction allows lower-level code to be included. This give the authors much stronger control over the bytecode that is generated, which can be used for example to optimise gas usage. However, it also potentially exposes a number of vulnerabilites and bugs that are additional attack surfaces, and there are a number of ways to use `assembly {}` to introduce deliberately malicious code that is difficult to detect.

#### 5.1.1 Text and homoglyphs<a href="index.html#sec-1-unicode" class="self-link" aria-label="§"></a>

**\[S\] No Unicode Direction Control Characters<a href="index.html#req-1-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the Unicode Direction Control Characters `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

Changing the apparent order of characters through the use of invisible <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> can mask malicious code, even in viewing source code, to deceive human auditors.

More information on <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> is available in the W3C note [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls) \[<a href="index.html#bib-unicode-bdo" class="bibref" data-link-type="biblio" title="How to use Unicode controls for bidi text">unicode-bdo</a>\].

#### 5.1.2 External Calls<a href="index.html#sec-1-external-calls" class="self-link" aria-label="§"></a>

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[M\] Protect External Calls**](index.html#req-2-external-calls), and [**\[Q\] Verify External Calls**](index.html#req-3-external-calls).

**\[S\] Check External Calls Return<a href="index.html#req-1-check-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call()`, `delegatecall()`, `staticcall()`, and `send()`) *MUST* check the returned value from each usage to determine whether the call failed,
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return).

Normally, exceptions in calls cause a revert. This will "bubble up", unless it is handled in a `try`/`catch`. However Solidity defines a set of Low-level Call Functions:

- `call()`,
- `delegatecall()`,
- `staticcall()`, and
- `send()`.

Calls using these functions behave differently. Instead of reverting on failure they return a boolean indicating whether the call completed successfully. Not testing explicitly for the return value could lead to unexpected behavior in the caller contract. Relying on these calls reverting on failure will lead to unexpected behaviour when they are not successful.

See also [SWC-104](https://swcregistry.io/docs/SWC-104) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], error handling documentation in \[<a href="index.html#bib-error-handling" class="bibref" data-link-type="biblio" title="Control Structures - Solidity Documentation. Section &#39;Error handling: Assert, Require, Revert and Exceptions&#39;">error-handling</a>\], unchecked return value as described in \[<a href="index.html#bib-cwe-252" class="bibref" data-link-type="biblio" title="CWE-252: Unchecked Return Value">CWE-252</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a>: [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return), and [**\[Q\] Verify External Calls**](index.html#req-3-external-calls).

**\[S\] Use Check-Effects-Interaction<a href="index.html#req-1-use-c-e-i" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The Checks-Effects-Interactions pattern is

- Validate all preconditions before making any state changes, and **only then**
- Complete all state updates before external interactions, and **only then**
- Execute external calls

Designing contracts this way significantly reduces the scope for <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>.

As well as checking the particular contract effects, it is possible as part of this pattern to test protocol invariants, to provide a further assurance that a request doesn't produce an unsafe outcome.

See also <a href="index.html#sec-reentrancy-considerations" class="sec-ref">§ 3.4 External Interactions and Re-entrancy Attacks</a>, the explanation of "Checks-Effects-Interactions" \[<a href="index.html#bib-c-e-i" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation. Section &#39;Use the Checks-Effects-Interactions Pattern&#39;">c-e-i</a>\] in "Solidity Security Considerations" \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], "[Checks Effects Interactions](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\], and \[<a href="index.html#bib-freipi" class="bibref" data-link-type="biblio" title="You&#39;re writing require statements wrong">freipi</a>\].

**\[S\] No `delegatecall()`<a href="index.html#req-1-delegatecall" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[M\] Protect External Calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

The `delegatecall()` instruction enables an external contract to manipulate the state of a contract that calls it, because the code is run with the caller's balance, storage, and address.

#### 5.1.3 Compiler Bugs <a href="index.html#sec-1-compiler-bugs" class="self-link" aria-label="§"></a>

There are a number of known security bugs in different Solidity compiler versions. The requirements in this subsection ensure that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not trigger these bugs. The name of the requirement includes the `uid` first recorded for the bug in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\], as a key that can be used to find more information about the bug. \[<a href="index.html#bib-solidity-bugs" class="bibref" data-link-type="biblio" title="List of Known Bugs">solidity-bugs</a>\] describes the conventions used for the JSON-formatted list of bugs.

The requirements in this subsection are ordered according to the latest Solidity compiler versions that are vulnerable.

Note

Implementing the Recommended Good Practice [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes all requirements in this subsection.

Some compiler-related bugs are in the <a href="index.html#sec-level-2-compiler-bugs" class="sec-ref">§ 5.2.5 Security Level [M] Compiler Bugs and Overriding Requirements</a> as <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirements, either because they are <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for requirements in this subsection, or because they are part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirements that already ensure that the bug cannot be triggered.

Some bugs were introduced in known Solidity compiler versions, while others are known or assumed to have existed in all Solidity compiler versions until they were fixed.

**\[S\] Compiler Bug SOL-2023-3<a href="index.html#req-1-compiler-SOL-2023-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that includes Yul code and uses the `verbatim` instruction twice, in each case surrounded by identical code, *MUST* disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).

From Solidity compiler version 0.8.5 until 0.8.22, the block deduplicator incorrectly processed `verbatim` items, meaning that sometimes it conflated two items based on the code surrounding them instead of comparing them properly.

See also the [8 November 2023 security alert](https://soliditylang.org/blog/2023/11/08/verbatim-invalid-deduplication-bug/).

**\[S\] Compiler Bug SOL-2022-6<a href="index.html#req-1-compiler-SOL-2022-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a `struct`, `return` value, or a parameter list) that includes a dynamic component with the ABIEncoderV2, and whose last element is a `calldata` static array of base type `uint` or `bytes32`, *MUST NOT* use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).

From Solidity compiler version 0.5.8 until 0.8.15, ABI encoding a tuple whose final component is a `calldata` static array of base type `uint` or `bytes32` with the ABIEncoderV2 could result in corrupted data.

See also the [8 August 2022 security alert](https://blog.soliditylang.org/2022/08/08/calldata-tuple-reencoding-head-overflow-bug/).

**\[S\] Compiler Bug SOL-2022-5 with `.push()`<a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, **and**
- has an empty `.push()` instruction that writes to the resulting array,

*MUST NOT* use a Solidity compiler version older than 0.8.15.

Until Solidity compiler version 0.8.15 copying memory or calldata whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using code through `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly).

**\[S\] Compiler Bug SOL-2022-3<a href="index.html#req-1-compiler-SOL-2022-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).

Solidity compiler versions from 0.6.9 until it was fixed in 0.8.13 had a bug that incorrectly allowed internal or public calls to use a simpification only valid for external calls, treating `memory` and `calldata` as equivalent pointers.

See also the [17 May 2022 security alert](https://blog.soliditylang.org/2022/05/17/data-location-inheritance-bug/).

**\[S\] Compiler Bug SOL-2022-2<a href="index.html#req-1-compiler-SOL-2022-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).

Solidity compiler versions from 0.5.8 until it was fixed in 0.8.13 had a bug that meant a single-pass encoding and decoding of a nested array could read data beyond the `calldatasize()`.

See also the [17 May 2022 security alert](https://blog.soliditylang.org/2022/05/17/calldata-reencode-size-check-bug/).

**\[S\] Compiler Bug SOL-2022-1<a href="index.html#req-1-compiler-SOL-2022-1" class="selflink"></a>**
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

See also the [16 March 2022 security alert](https://blog.soliditylang.org/2022/03/16/encodecall-bug/).

**\[S\] Compiler Bug SOL-2021-4<a href="index.html#req-1-compiler-sol-2021-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *MUST NOT* use Solidity compiler version 0.8.8.

Solidity compiler version 0.8.8 had a bug that assigned a full 32 bytes of storage to custom types that did not need it. This can be misused to enable reading arbitrary storage, as well as causing errors if the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> contains code compiled using different Solidity compiler versions.

See also the [29 September 2021 security alert](https://blog.soliditylang.org/2021/09/29/user-defined-value-types-bug/)

**\[S\] Compiler Bug SOL-2021-2<a href="index.html#req-1-compiler-SOL-2021-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory` *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).

Solidity compiler version 0.4.16 introduced a bug, fixed in 0.8.4, that meant the ABIEncoderV2 incorrectly validated pointers when reading `memory` byte arrays, which could result in reading data beyond the array area due to an overflow error in calculating pointers.

See also the [21 April 2021 security alert](https://blog.soliditylang.org/2021/04/21/decoding-from-memory-bug/).

**\[S\] Compiler Bug SOL-2021-1<a href="index.html#req-1-compiler-SOL-2021-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the Optimizer with a Solidity compiler version older than 0.8.3.

Solidity compiler versions before 0.8.3 had an Optimizer bug that meant keccak hashes, calculated for the same content but different lengths that were not multiples of 32 bytes, incorrectly used the first value from cache instead of recalculating.

See also the [23 March 2021 security alert](https://blog.soliditylang.org/2021/03/23/keccak-optimizer-bug/).

**\[S\] Use a Modern Compiler<a href="index.html#req-1-compiler-060" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 2](https://entethalliance.org/specs/ethtrust-sl/v2/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[S\] No Overflow/Underflow**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-overflow-underflow)
- [**\[S\] Compiler Bug SOL-2020-11-push**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-11-push)
- [**\[S\] Compiler Bug SOL-2020-10**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-10)
- [**\[S\] Compiler Bug SOL-2020-9**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-9)
- [**\[S\] Compiler Bug SOL-2020-8**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-8)
- [**\[S\] Compiler Bug SOL-2020-6**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-6)
- [**\[S\] Compiler Bug SOL-2020-7**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-7)
- [**\[S\] Compiler Bug SOL-2020-5**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-5)
- [**\[S\] Compiler Bug SOL-2020-4**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-4)

**AND**

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

It is a good practice to use a modern Solidity Compiler Version. In the rare cases where it is not possible to use a Solidity Compiler Version later than 0.6.0, it is possible to achieve <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> by conforming to the relevant <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> that were defined in version 1 of this specification \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060), covering Solidity Compiler bugs that require review for <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>.

**\[S\] No Ancient Compilers<a href="index.html#req-1-no-ancient-compilers" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.3.

Compiler bugs are not tracked for compiler Solidity compiler versions older than 0.3. There is therefore a risk that unknown bugs create unexpected problems.

See also "SOL-2016-1" in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\].

### 5.2 Security Level \[M\]<a href="index.html#sec-levels-two" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[M\] means that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> has been carefully reviewed by a human auditor or team, doing a manual analysis, and important security issues have been addressed to their satisfaction.

This level includes a number of <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> for cases when <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet a <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement directly, because it uses an uncommon feature that introduces higher risk, or because in certain circumstsances testing that the requirement has been met requires human judgement. Passing the relevant <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> tests that the feature has been implemented sufficiently well to satisfy the auditor that it does not expose the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to the known vulnerabilities identified in this Security Level.

**\[M\] Pass Security Level \[S\]<a href="index.html#req-2-pass-l1" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">§ 5.1 Security Level [S]</a>.

**\[M\] Explicitly Disambiguate Evaluation Order<a href="index.html#req-2-enforce-eval-order" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain statements where variable evaluation order can result in different outcomes

The evaluation order of functions is not entirely deterministic in Solidity, and is not guaranteed to be consistent across Solidity compiler versions. This means that the outcome of a statement calling multiple functions that each have side effects on shared stateful objects can lead to different outcomes if the order that the called functions were evaluated varies.

Also, the evaluation order in events and the instructions `addmod` and `modmul` generally does not follow the **usual** pattern, meaning that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using those instructions could produce unexpected outcomes.

Warning

<a href="index.html#example-13-variant-evaluation-order" class="self-link">Example 13</a>: variant evaluation order

If functions `g` and `h` change the state of any variable that the result of a function `f` depends on, a call such as `f(g(x), h(y))` cannot be guaranteed to return repeatable results.

A common approach to addressing this vulnerability is the use of temporary results, to ensure evaluation order will be the same.

<a href="index.html#example-14-using-temporary-values-to-enforce-evaluation-order" class="self-link">Example 14</a>: Using temporary values to enforce evaluation order

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

See also \[<a href="index.html#bib-solidity-underhanded-richards2022" class="bibref" data-link-type="biblio" title="Solidity Underhanded Contest 2022. Submission 9 - Tynan Richards">solidity-underhanded-richards2022</a>\], \[<a href="index.html#bib-solidity-cheatsheet" class="bibref" data-link-type="biblio" title="Solidity Documentation: Cheatsheet - Order Of Precedence Of Operators">solidity-cheatsheet</a>\], and the [19 July 2023 Solidity Compiler Security Bug notification](https://blog.soliditylang.org/2023/07/19/full-inliner-non-expression-split-argument-evaluation-order-bug/) for Solidity Compiler Security Bug 2023-2, noted in \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\].

**\[M\] Verify Exact Balance Checks<a href="index.html#req-2-verify-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that checks whether the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable. *MUST* protect itself against transfers affecting the balance tested.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check).

If a Smart Contract checks that an account balance is some particular exact value at some point during its execution, it is potentially vulnerable to an attack, where a transfer to the account can be used to change the balance of the account causing unexpected results such as a transaction reverting. If such checks are used it is important that they are protected against this possibility.

#### 5.2.1 Text and homoglyph attacks<a href="index.html#sec-2-unicode" class="self-link" aria-label="§"></a>

The requirements in this section are related to the security advisory \[<a href="index.html#bib-cve-2021-42574" class="bibref" data-link-type="biblio" title="National Vulnerability Database CVE-2021-42574">CVE-2021-42574</a>\] and \[<a href="index.html#bib-cwe-94" class="bibref" data-link-type="biblio" title="CWE-94: Improper Control of Generation of Code (&#39;Code Injection&#39;)">CWE-94</a>\], "Improper Control of Generation of Code", also called "Code Injection".

**\[M\] No Unnecessary Unicode Controls<a href="index.html#req-2-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

<a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> permits the use of <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> in text strings, subject to analysis of whether they are necessary.

**\[M\] No Homoglyph-style Attack<a href="index.html#req-2-no-homoglyph-attack" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks, if the impact is misleading.

Substituting characters from different alphabets or that can be hard to distinguish, or using direction control characters or combining characters, can be used to mask malicious code, for example by presenting variables or function names designed to mislead auditors. These attacks are known as Homoglyph Attacks. Several approaches to successfully exploiting this issue are described in \[<a href="index.html#bib-ivanov" class="bibref" data-link-type="biblio" title="Targeting the Weakest Link: Social Engineering Attacks in Ethereum Smart Contracts">Ivanov</a>\].

In the rare case when there is a valid use of characters from multiple Unicode blocks (see \[<a href="index.html#bib-unicode-blocks" class="bibref" data-link-type="biblio" title="Blocks-14.0.0.txt">unicode-blocks</a>\]) in a variable name or label (most likely to be mixing two languages in a name), this requirement allows them to achieve <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> so long as they do not mislead or confuse.

This level requires checking for homoglyph attacks including those within a single character set, such as the use of "í" in place of "i" or "ì", "ت" for "ث", or "1" for "l", as well as across character sets such as e.g. Latin "a" and Cyrillic "а" or the Mathematical character "𝚒" and latin "i". If the reviewer judges that the result is unnecessarily misleading or confusing, the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does not meet this requirement.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a>: [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

#### 5.2.2 External Calls<a href="index.html#sec-2-external-calls" class="self-link" aria-label="§"></a>

**\[M\] Protect External Calls<a href="index.html#req-2-external-calls" class="selflink"></a>**
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

<a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> allows calling within a <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">set of contracts</a> that form part of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. This ensures all contracts called are audited together at this Security Level.

If a contract calls a well-known external contract that is not audited as part of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, it is possible to certify conformance to this requirement through the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>, which allow the certifier to claim on their own judgement that the contracts called provide appropriate security. The extended requirements around documentation of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that apply when claiming conformance through implementation of the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> in this case reflect the potential for very high risk if the external contracts are simply assumed by a reviewer to be secure because they have been widely used.

Unless the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> deploys contracts itself, and retrieves their address accurately for calling, it is necessary to check that the contracts are really deployed at the addresses assumed in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

The same level of protection against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a> has to be provided to the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> overall as for the <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a> requirement [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i). Contracts using reentrancy guards can still be vulnerable if they don't follow \[c-e-i\]. Cross-function reentrancy attacks have succeeded where separate functions sharing the same state caused state changes after external calls.

**\[M\] Avoid Read-only Re-entrancy Attacks<a href="index.html#req-2-avoid-readonly-reentrancy" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.

As described in <a href="index.html#sec-reentrancy-considerations" class="sec-ref">§ 3.4 External Interactions and Re-entrancy Attacks</a>, code that reads information from a function can end up reading inconsistent or incorrect information. When the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> calls a function in which this possibility arises, the calling code needs an appropriate mechanism to avoid it happening.

One potential mechanism is for view functions to have a modifier that checks whether the data is currently in an inconsistent state, in the manner of a lock function. This enables calling code to explicitly avoid viewing inconsistent data.

Warning

<a href="index.html#example-15-insecure-approach-relaying-on-values-of-view-functions-that-can-be-reentered" class="self-link">Example 15</a>: INSECURE approach: relaying on values of view functions that can be reentered

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

**\[M\] Handle External Call Returns<a href="index.html#req-2-handle-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Check External Calls Return**](index.html#req-1-check-return).

It is important that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> works as expected, to the satisfaction of the auditor, when the return value is the result of a possible error, such as if a call to a non-existent function triggers a fallback function instead of simply reverting, or an external call using a <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Function</a> does not revert.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a>: [**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs).

#### 5.2.3 Documented Defensive Coding<a href="index.html#sec-2-special-code" class="self-link" aria-label="§"></a>

**\[M\] Document Special Code Use<a href="index.html#req-2-documented" class="selflink"></a>**
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
- [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), **and**
- [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall).

There are legitimate uses for all of these coding patterns, but they are also potential causes of security vulnerabilities. <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> therefore requires testing that the use of these patterns is explained and justified, and that they are used in a manner that does not introduce known vulnerabilities.

The requirement to document the use of external calls applies to **all** external calls in the tested code, whether or not they meet the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related requirements</a>: [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented), [**\[Q\] Verify External Calls**](index.html#req-3-external-calls), [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

**\[M\] Ensure Proper Rounding of Computations Affecting Value<a href="index.html#req-2-check-rounding" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* identify and protect against exploiting rounding errors:

- The possible range of error introduced by such rounding *MUST* be documented.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* unintentionally create or lose value through rounding.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.

Smart Contracts typically implement mathematical formulas over real numbers using integer arithmetic. Such code can introduce rounding errors because integers and rational numbers whose size is bounded cannot precisely represent all real numbers in the same range.

If a procedure that uses rounding results in a predictable amount of error, that increases the value produced by the round-trip, it is possible to exploit that difference by repeating the procedure to cumulatively siphon a large sum.

Warning

<a href="index.html#example-16-insecure-approach-rounding-can-create-value" class="self-link">Example 16</a>: INSECURE approach: rounding can create value

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

<a href="index.html#example-17-rounding-with-the-keep-the-change-approach" class="self-link">Example 17</a>: Rounding with the 'Keep the Change' approach

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

**\[M\] Protect Self-destruction<a href="index.html#req-2-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct).

If the `selfdestruct()` instruction (or its deprecated alternative `suicide()`) is not carefully protected, malicious code can call it and destroy a contract, and potentially steal any Ether held by the contract. In addition, this can disrupt other users of the contract since once the contract has been destroyed any Ether sent is simply lost, unlike when a contract is disabled which causes a transaction sending Ether to revert.

See also [SWC-106](https://swcregistry.io/docs/SWC-106) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

<a href="index.html#example-18-unprotected-self-destruction" class="self-link">Example 18</a>: Unprotected Self-destruction

This vulnerability led to the [Parity MultiSig Wallet Failure](https://www.parity.io/blog/parity-technologies-multi-sig-wallet-issue-update/) that blocked around 1/2 Million Ether on mainnet in 2017.

**\[M\] Avoid Common `assembly {}` Attack Vectors<a href="index.html#req-2-safe-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly {}` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

The `assembly {}` instruction provides a low-level method for developers to produce code in smart contracts. Using this approach provides great flexibility and control, for example to reduce gas cost. However it also exposes some possible attack surfaces where a malicious coder could introduce attacks that are hard to detect. This requirement ensures that two such attack surfaces that are well-known are not exposed.

See also [SWC-124](https://swcregistry.io/docs/SWC-124) and [SWC-127](https://swcregistry.io/docs/SWC-127) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), and if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

**\[M\] Protect `CREATE2` Calls<a href="index.html#req-2-protect-create2" class="selflink"></a>**
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

**\[M\] Safe Overflow/Underflow<a href="index.html#req-2-overflow-underflow" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

There are a few rare use cases where arithmetic overflow or underflow is intended, or expected behaviour. It is important such cases are protected appropriately.

Note that Solidity compiler version 0.8.0 introduced overflow protection that causes transactions to revert.

See also [SWC-101](https://swcregistry.io/docs/SWC-101) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

**\[M\] Sources of Randomness<a href="index.html#req-2-random-enough" class="selflink"></a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

This requirement involves careful evaluation for each specific contract and case. Some uses of randomness rely on no prediction being more accurate than any other. For such cases, values that can be guessed at with some accuracy or controlled by miners or validators, like block difficulty, timestamps, and/or block numbers, introduces a vulnerability. Thus a "strong" source of randomness like an oracle service is necessary.

Other uses are resistant to "good guesses" because using something that is close but wrong provides no more likelihood of gaining an advantage than any other guess.

Warning

<a href="index.html#example-19-don-t-do-this-randomness-vulnerable-to-approximate-guessing" class="self-link">Example 19</a>: Don't do this: Randomness vulnerable to approximate guessing

A competition to guess the block number of a chain at a specific time, that rewards the answer closest to the correct answer is using a source of "randomness" that is vulnerable to approximate guessing.

<a href="index.html#example-20-randomness-resistant-to-approximation" class="self-link">Example 20</a>: Randomness resistant to approximation

A lottery that will only pay if a number is submitted that exactly matches a winning entry in an offchain lottery to be held in the future, offers no advantage in being able to approximate the answer.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[M\] Don't Misuse Block Data<a href="index.html#req-2-block-data-misuse" class="selflink"></a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

Block numbers are vulnerable to approximate prediction, although they are generally not reliably precise indicators of elapsed time. `block.timestamp` is subject to manipulation by malicious actors. It is therefore important that these data are not trusted by <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to function as if they were highly reliable or random information.

The description of [SWC-116](https://swcregistry.io/docs/SWC-116) in \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] includes some code examples for techniques to avoid, for example using `block.number / 14` as a proxy for elapsed seconds, or relying on `block.timestamp` to indicate a precise time has passed.

For probabilitsitic low precision use, such as "about 1/2 an hour has passed", an expression like `(block.number / 14 > 1800)` can be sufficiently robust on main net, or a blockchain with a similar regular block period of around 14 seconds. But using this approach to determine that e.g. "exactly 36 seconds" have elapsed fails the requirement.

Warning

A contract that relies on a specific block period can introduce serious risks if it is deployed on a blockchain with a very different block frequency.

Likewise, because block.timestamp depends on settings that can be manipulated by a malicious node operator, in cases likes Ethereum mainnet it is suitable for use as a coarse-grained approximation (on a scale of minutes) but the same code on a different blockchain can be vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks.

Note that this is related to the use of <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a>, which can also provide inaccurate information.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

#### 5.2.4 Signature Management<a href="index.html#sec-2-signature-requirements" class="self-link" aria-label="§"></a>

**\[M\] Proper Signature Verification<a href="index.html#req-2-signature-verification" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* properly verify signatures to ensure authenticity of messages that were signed off-chain.

Some smart contracts process messages that were signed off-chain to increase flexibility, while maintaining authenticity. Smart contracts performing their own signature verification need to verify such messages' authenticity.

Using `ecrecover()` for signature verification, it is important to validate the address returned against the expected outcome. In particular, a return value of `address(0)` represents a failure to provide a valid signature.

See also [SWC-122](https://swcregistry.io/docs/SWC-122) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\].

For code that does use `ecrecover()` and a Solidity compiler version older than 0.4.14, see the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060), specifically [**\[M\] Validate `ecrecover()` Input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input) in \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\]

**\[M\] No Improper Usage of Signatures for Replay Attack Protection<a href="index.html#req-2-malleable-signatures-for-replay" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST* ensure that signatures cannot be reused:

- In the same function to verify the same message, **nor**
- In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **nor**
- In more than one contract address to verify the same message, in which the same account(s) may be signing messages, **nor**
- In the same contract address across multiple chains,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Intended Replay**](index.html#req-3-intended-replay). Additionally, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

In Replay Attacks, an attacker replays correctly signed messages to exploit a system. The signed message needs to include enough identifying information so that its intended setting is well-defined.

<a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a> allow an attacker to create a new signature for the same message. Smart contracts that check against hashes of signatures to ensure that a message has only been processed once could be vulnerable to replay attacks if malleable signatures are used.

#### 5.2.5 Security Level \[M\] Compiler Bugs and Overriding Requirements<a href="index.html#sec-level-2-compiler-bugs" class="self-link" aria-label="§"></a>

Some solidity compiler bugs described in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 5.1.3 Compiler Bugs </a> have <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, and some have trigger conditions that are not readily detectable in software.

Note

Implementing the Recommended Good Practice [**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler) means that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> passes all requirements in this subsection.

**\[M\] Solidity Compiler Bug 2023-1<a href="index.html#req-2-compiler-SOL-2023-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses `.selector` *MUST* use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.

A bug introduced in Solidity compiler version 0.6.2 and fixed in Solidity compiler version 0.8.21 meant that when compound expressions accessed the `.selector` member, the expression would not be evaluated, unless the viaIR pipeline was used. Thus any side effects caused by the expression would not occur.

See also the [19 July 2023 security alert](https://blog.soliditylang.org/2023/07/19/missing-side-effects-on-selector-access-bug/).

**\[M\] Compiler Bug SOL-2022-7<a href="index.html#req-2-compiler-SOL-2022-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing `return()` or `stop()` instructions *MUST NOT* use a Solidity compiler version between 0.8.13 and 0.8.16 inclusive.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

A bug fixed in Solidity compiler version 0.8.17 meant that storage writes followed by conditional early terminations from inline assembly functions would sometimes be erroneously dropped during optimization.

See also the [5 September 2022 security alert](https://blog.soliditylang.org/2022/09/08/storage-write-removal-before-conditional-termination/).

**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`<a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, **and**
- has an `assembly {}` instruction that reads that data without explicitly matching the length that was copied,

*MUST NOT* use a Solidity compiler version older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Until Solidity compiler version 0.8.15 copying `memory` or `calldata` whose length is not a multiple of 32 bytes could expose data beyond the data copied, which could be observable using `assembly {}`.

See also the [15 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push), [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Compiler Bug SOL-2022-4<a href="index.html#req-2-compiler-SOL-2022-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly {}` instructions, such tha

- one writes to memory e.g. by storing a value in a variable, but does not access that memory again, **and**
- code in a another `assembly {}` instruction refers to that memory,

*MUST NOT* use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Solidity compiler version 0.8.13 introduced a yulOptimizer bug, fixed in Solidity compiler version 0.8.15, where memory created in an `assembly {}` instruction but only read in a different `assembly {}` instruction was discarded.

See also the [17 June 2022 security alert](https://blog.soliditylang.org/2022/06/15/inline-assembly-memory-side-effects-bug/) and <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), and [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3).

**\[M\] Compiler Bug SOL-2021-3<a href="index.html#req-2-compiler-SOL-2021-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly {}` instruction *MUST NOT* use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

Solidity compiler version 0.6.8 introduced a bug, fixed in Solidity compiler version 0.8.9, that meant immutable signed integer types shorter than 256 bits could be read incorrectly in inline `assembly {}` instructions.

See also the [29 September 2021 security alert](https://blog.soliditylang.org/2021/09/29/signed-immutables-bug/), and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">related requirements</a> [**\[M\] Safe Use of `assembly {}`**](index.html#req-2-safe-assembly), [**\[M\] Document Special Code Use**](index.html#req-2-documented), [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), and [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4).

**\[M\] Use a Modern Compiler<a href="index.html#req-2-compiler-060" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0, **unless** it meets the requirement [**\[M\] Compiler Bug Check Constructor Payment**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-2-compiler-check-payable-constructor) from the [EEA EthTrust Security Levels Specification Version 2](https://entethalliance.org/specs/ethtrust-sl/v2/), as an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>,

**AND**

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[M\] Compiler Bug SOL-2020-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2),
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly),
- [**\[M\] Compiler Bug Check Identity Calls**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls),
- [**\[M\] Validate `ecrecover()` input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input),
- [**\[M\] Compiler Bug No Zero Ether Send**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send), and
- [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage).

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060), covering Solidity Compiler bugs that require review for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>.

### 5.3 Security Level \[Q\]<a href="index.html#sec-levels-three" class="self-link" aria-label="§"></a>

In addition to automatable static testing verification (<a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>), and a manual audit (<a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>), <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at Security Level \[Q\] means checking that the intended functionality of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> is sufficiently well documented that its functional correctness can be verified, that the code and documentation has been thoroughly reviewed by a human auditor or audit team to ensure that they are both internally coherent and consistent with each other, carefully enough to identify complex security vulnerabilities.

This level of review is especially relevant for tokens using ERC20 \[<a href="index.html#bib-erc20" class="bibref" data-link-type="biblio" title="EIP-20: Token Standard">ERC20</a>\], ERC721 \[<a href="index.html#bib-erc721" class="bibref" data-link-type="biblio" title="ERC 721: Non-fungible Token Standard">ERC721</a>\], and others; \[<a href="index.html#bib-token-standards" class="bibref" data-link-type="biblio" title="Ethereum Development Documentation - Token Standards">token-standards</a>\] identifies a number of other standards that can define tokens.

At this Security Level there are also checks to ensure the code does not contain errors that do not directly impact security, but do impact code quality. Code is often copied, so <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> requires code to be as well-written as possible. The risk being addressed is that it is easy, and not uncommon, to introduce weaknesses after copying existing code as a starting point.

**\[Q\] Pass Security Level \[M\]<a href="index.html#req-3-pass-l2" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">§ 5.2 Security Level [M]</a>.

**\[Q\] Use TimeLock Delays for Sensitive Operations<a href="index.html#req-3-timelock-for-privileged-actions" class="selflink"></a>**
Sensitive operations that affect all or a majority of users *MUST* use \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delays.

Sensitive operations, such as Smart Contract upgrades and \[<a href="index.html#bib-rbac" class="bibref" data-link-type="biblio" title="INCITS 359-2012: Information Technology - Role Based Access Control">RBAC</a>\] changes impact all or a majority of users in the protocol. A \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delay allows users to exit the system if they disagree with the proposed change, and allows developers to react if they detect a suspicious change.

**\[Q\] Code Linting<a href="index.html#req-3-linted" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* use the same name for functions, variables or other tokens that can occur within the same scope, **and**
- *MUST NOT* include `assert()` statements that fail in normal operation, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert()` statements, **and**
- *MUST NOT* contain a function that has the same name as the smart contract **unless** it is explicitly declared as a constructor using the `constructor` keyword, **and**
- *MUST* explicitly declare the visibility of all functions and variables, **and**
- *MUST* specify one or more Solidity compiler versions in its `pragma` directive.

Code is often copied from "good examples" as a starting point for development. Code that has achieved <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is meant to be high quality, so it is important to ensure that copying it does not encourage bad habits. It is also easier to review <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that does not contain pointless code.

Code that has the same names for functions and variables is generally harder to read. If those items can overlap in scope, compilation will disambiguate them, but they will often require significant work on the part of reviewers to mentally separate. Using i,j as counters in multiple non-overlapping loops is fine, but having a variable in an "outer scope" whose name is replicated in an "inner scope" by some other variable or function increases the effort required to follow the execution patterns.

Code designed to trap unexpected errors, such as `assert()` instructions, is explicitly allowed, because it would be very unfortunate if defensively written code that successfully eliminates the possibility of triggering a particular error could not achieve <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a>. `assert()` statements are meant for invariants, not as a generic error-handling mechanism. If an `assert()` statement fails in routine operation because it is being used as a mechanism to catch errors, it is better to replace it with a `require()` statement or similar mechanism explicitly designed for the use case. If it fails due to a coding bug, that needs to be fixed.

The requirement on `assert()` statements is based on \[<a href="index.html#bib-cwe-670" class="bibref" data-link-type="biblio" title="CWE-670: Always-Incorrect Control Flow Implementation">CWE-670</a>\] Always-Incorrect Control Flow Implementation.

**\[Q\] Manage Gas Use Increases<a href="index.html#req-3-enough-gas" class="selflink"></a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

Some structures such as arrays can grow, and the value of variables is (by design) variable. Iterating over a structure whose size is not clear in advance, whether an array that grows, a bound that changes, or something determined by an external value, can result in significant increases in gas usage.

What is reasonable growth to expect needs to be considered in the context of the business logic intended, and how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> protects against <a href="index.html#dfn-gas-griefing" class="internalDFN" data-link-type="dfn">Gas Griefing</a> attacks, where malicious actors or errors result in values occurring beyond the expected reasonable range(s).

See also [SWC-126](https://swcregistry.io/docs/SWC-126), [SWC-128](https://swcregistry.io/docs/SWC-128) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] and the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> in <a href="index.html#sec-3-documentation" class="sec-ref">§ 5.3.1 Documentation requirements</a>.

**\[Q\] Protect Gas Usage<a href="index.html#req-3-protect-gas" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect against malicious actors stealing or wasting gas.

Smart contracts allowing "gasless" transactions enable users to submit transactions without having to supply their own gas. They need to be carefully implemented to prevent Denial of Service from <a href="index.html#dfn-gas-griefing" class="internalDFN" data-link-type="dfn">Gas Griefing</a> and <a href="index.html#dfn-gas-siphoning" class="internalDFN" data-link-type="dfn">Gas Siphoning</a> attacks.

See also [The Gas Siphon Attack: How it Happened and How to Protect Yourself](https://archive.devcon.org/archive/watch/5/the-gas-siphon-attack-how-it-happened-and-how-to-protect-yourself/) from the DevCon 2019 talk \[<a href="index.html#bib-devcon-siphoning" class="bibref" data-link-type="biblio" title="The Gas Siphon Attack: How it Happened and How to Protect Yourself">DevCon-siphoning</a>\].

**\[Q\] Protect against Oracle Failure<a href="index.html#req-3-check-oracles" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect itself against malfunctions in <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> it relies on.

Some <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> are known to be vulnerable to manipulation, for example because they derive the information they provide from information vulnerable to <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>, or manipulation of prices through the use of flashloans to enable an <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attack, among other well-known attacks.

In addition, as networked software <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> can potentially suffer problems ranging from latency issues to outright failure, or being discontinued.

It is important to check the mechanism used by an <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> to generate the information it provides, and the potential exposure of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that relies on that <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracle</a> to the effects of it failing, or of malicious actors manipulating its inputs or code to enable attacks.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[Q\] Protect against Ordering Attacks**](index.html#req-3-block-front-running), and [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[Q\] Protect against Ordering Attacks<a href="index.html#req-3-block-front-running" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* manage information in such a way that it protects against <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>.

In <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>, an attacker places their transaction in a beneficial position compared to that of a victim's. This can be done by a malicious block producer or by an attacker monitoring the mempool, and preempting susceptible transactions by broadcasting their own transactions with higher transaction fees. Removing incentives generally means applying mitigations such as hash commitment schemes \[<a href="index.html#bib-hash-commit" class="bibref" data-link-type="biblio" title="Commitment scheme - WikiPedia">hash-commit</a>\] or batch execution.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev).

**\[Q\] Protect against MEV Attacks<a href="index.html#req-3-block-mev" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

<a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> refers to the potential that a block producer can maliciously reorder or suppress transactions, or another participant in a blockchain can propose a transaction or take other action to gain a benefit that was not intended to be available to them.

This requirement entails a careful judgement by the auditor, of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is vulnerable to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks, and what mitigation strategies are appropriate. Some approaches are discussed further in <a href="index.html#sec-mev-considerations" class="sec-ref">§ 3.7 MEV (Maliciously Extracted Value)</a>.

Many attack types need to be considered, including <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check), [**\[M\] Sources of Randomness**](index.html#req-2-random-enough), [**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse), and [**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles), and [**\[Q\] Protect against Ordering Attacks**](index.html#req-3-block-front-running).

**\[Q\] Protect Against Governance Takeovers<a href="index.html#req-3-protect-governance" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system *MUST* protect against malicious exploitation of the governance design.

"Malicious exploitation" is hard to define precisely, because it depends on the stated goals of the system - for example those described in [**\[Q\] Document Contract Logic**](index.html#req-3-documented). Broadly, this requirement is to check that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is robust against efforts by malicious entities to gain governance control that is expected to be vested either in specified trusted entities, or decentralized and distributed widely enough to provide a sense of security that governance decisions and actions taken are widely supported.

Governance attacks are specific to the system that is exploited. Depending on the governance proposal system, some areas of vulnerability may include:

- The issued governance token;
- The method of distribution for the governance token;
- The design of the acceptance and execution of governance proposals.

For example, if a staking contract is used to distribute governance tokens as a reward, it is important that the staking contract is not vulnerable to a Flash Loan Attack, where a large amount of tokens are borrowed in a very short-term flash loan, and staked atomically to gain a temporary majority of governance tokens that are then used to make a governance decision, such as draining all the funds held to an attacker's wallet.

See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Protect against Ordering Attacks**](index.html#req-3-block-front-running).

**\[Q\] Process All Inputs<a href="index.html#req-3-all-valid-inputs" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

Code that fails to validate inputs runs the risk of being subverted through maliciously crafted input that can trigger a bug, or behaviour the authors did not anticipate.

See also [SWC-123](https://swcregistry.io/docs/SWC-123) \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\] which notes that it is important to consider whether input requirements are too strict, as well as too lax, \[<a href="index.html#bib-cwe-573" class="bibref" data-link-type="biblio" title="CWE-573: Improper Following of Specification by Caller">CWE-573</a>\] Improper Following of Specification by Caller, and note that there are several <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> that are specific to particular Solidity compiler versions in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 5.1.3 Compiler Bugs </a>.

**\[Q\] State Changes Trigger Events<a href="index.html#req-3-event-on-state-change" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

Events are convenience interfaces that give an abstraction on top of the EVM's logging functionality. Applications can subscribe and listen to these events through the RPC interface of an Ethereum client. See more at \[<a href="index.html#bib-solidity-events" class="bibref" data-link-type="biblio" title="Solidity Documentation: Contracts - Events">solidity-events</a>\].

Events are generally expected to be used for logging all state changes as they are not just useful for off-chain applications but also security monitoring and debugging. Logging all state changes in a contract ensures that any developers interacting with the contract are made aware of every state change as part of the ABI and can understand expected behavior through event annotations, as per [**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate).

**\[Q\] No Private Data<a href="index.html#req-3-no-private-data" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain.

This is a <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> requirement primarily because the question of what is private data often requires careful and thoughtful assessment and a reasoned understanding of context. In general, this is likely to include an assessment of how the data is gathered, and what the providers of data are told about the usage of the information.

Private Data is used in this specification to refer to information that is not intended to be generally available to the public. For example, an individual's home telephone number is generally private data, while a business' customer enquiries telephone number is generally not private data. Similarly, information identifying a person's account is normally private data, but there are circumstances where it is public data. In such cases, that public data can be recorded on-chain in conformance with this requirement.

Warning

PLEASE NOTE: In some cases regulation such as the \[<a href="index.html#bib-gdpr" class="bibref" data-link-type="biblio" title="Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016         on the protection of natural persons with regard to the processing of personal data         and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)         (Text with EEA relevance)">GDPR</a>\] imposes formal legal requirements on some private data. However, performing a test for this requirement results in an expert technical opinion on whether data that the auditor considers private is exposed. A statement about whether <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets this requirement does not represent any form of legal advice or opinion, attorney representation, or the like.

**\[Q\] Intended Replay<a href="index.html#req-3-intended-replay" class="selflink"></a>**
If a signature within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance *MUST* be intended, documented, **and** safe for re-use.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay).

In some rare instances, it may be the intention of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to allow signatures to be replayed. For example, a signature may be used as permission to participate in a whitelist for a given period of time. In these exceptional cases, the replay must be included in documentation as a known allowance. Further, it must be verified that the reuse cannot be maliciously exploited.

#### 5.3.1 Documentation requirements<a href="index.html#sec-3-documentation" class="self-link" aria-label="§"></a>

<a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> conformance requires a detailed description of how the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is **intended** to behave. Alongside detailed testing requirements to check that it does behave as described wth regard to specific known vulnerabililies, it is important that the claims made for it are accurate. This requirement helps ensure that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> fulfils claims made for it outside audit-specific documentation.

The combination of these requirements helps ensure there is no malicious code, such as malicious "back doors" or "time bombs" hidden in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Since there are legitimate use cases for code that behaves as a "time bomb", "phones home", or the like, this combination helps ensure that testing focuses on real problems.

The requirements in this section extend the coverage required to meet the <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a> requirement [**\[M\] Document Special Code Use**](index.html#req-2-documented). As with that requirement, there are multiple requirements at this level that require the documentation mandated in this subsection.

**\[Q\] Document Contract Logic<a href="index.html#req-3-documented" class="selflink"></a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

Contract Logic documented in a human-readable format and with enough detail that functional correctness and safety assumptions for special code use can be validated by auditors helps them assess complex code more efficiently and with higher confidence.

It is important to document how the logic protects against potential attacks such as <a href="index.html#dfn-flash-loan-attack" class="internalDFN" data-link-type="dfn">Flash Loan Attacks</a> (especially on governance or price manipulation), MEV, and other complex attacks that take advantage of ecosystem features or tokenomics.

**\[Q\] Document System Architecture<a href="index.html#req-3-document-system" class="selflink"></a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

System documentation provides auditor(s) information to understand security assumptions and ensure functional correctness. It is helpful if system documentation is included or referenced in a README file of the code repository, alongside documentation for how the source code can be tested, built and deployed.

The management of variables and more complex data structures over time is an important part of this documentation. That aspect of this requirement is likely to be met through work to meet the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Manage Gas Use Increases**](index.html#req-3-enough-gas). See also the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate).

**\[Q\] Document Threat Models<a href="index.html#req-3-document-threats" class="selflink"></a>**
Documented Threat Models for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided, describing each threat, security assumptions, expected responses, and expected outcomes.

A Threat Model is a tool to help prepare for a variety of attacks that might be raised, either indivudally or in concert, providing a set of hypothetical but possible scenarios, in order to ensure the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can adequately withstand them.

A good Threat Model will cover a range of possiblities, including

- Emergence of previously unknown attack vectors
- Network Manipulation
- Economic Warfare
- Governance Exploitation
- Oracle Attacks

And other scenarios as well as combinations of such scenarios that could overwhelm the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>'s defenses against them.

**\[Q\] Annotate Code with NatSpec<a href="index.html#req-3-annotate" class="selflink"></a>**
All <a href="index.html#dfn-public-interfaces" class="internalDFN" data-link-type="dfn">Public Interfaces</a> contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

Inline comments are important to ensure that developers and auditors understand the intent behind each function and other code components. Public Interfaces means anything that would be contained in the ABI of the compiled <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>. It is also recommended to use inline comments for private or internal functions that implement sensitive and/or complex logic.

Following the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format allows these inline comments to be understood by the Solidity compiler for extracting them into a machine-readable format that could be used by other third-party tools for security assessments and automatic documentation, including documentation shown to users by wallets that integrate with source code verification tools like [Sourcify](https://sourcify.dev). This could also be used to generate specifications that fully or partially satisfy the Requirement to [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

**\[Q\] Implement as Documented<a href="index.html#req-3-implement-as-documented" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

The requirements at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> to provide documentation are important. However, it is also crucial that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> actually behaves as documented. If it does not, it is possible that this reflects insufficient care and that the code is also vulnerable due to bugs that were missed in implementation. It is also possible that the difference is an attempt to hide malicious code in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

#### 5.3.2 Access Control<a href="index.html#sec-3-access-control" class="self-link" aria-label="§"></a>

**\[Q\] Enforce Least Privilege<a href="index.html#req-3-access-control" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that enables privileged access *MUST* implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct).

There are several common methods to implement access control, such as Role-Based Access Control \[<a href="index.html#bib-rbac" class="bibref" data-link-type="biblio" title="INCITS 359-2012: Information Technology - Role Based Access Control">RBAC</a>\] and \[<a href="index.html#bib-ownable" class="bibref" data-link-type="biblio" title="ERC-173: Contract Ownership Standard">Ownable</a>\], and bespoke access control is often implemented for a given use case. Using industry-standard methods can help simplify the process of auditing, but is not sufficient to determine that there are no risks arising either from errors in implementation or due to a maliciously-crafted contract.

It is important to consider access control at both the protocol operation and deployment levels. If a protocol is deployed in a deterministic manner, for example allowing a multi-chain deployment to have the same address across all chains, it is important to explicitly set an owner rather than defaulting to `msg.sender`, as that may leave a simple factory deployment contract as the insufficent new admininstrator of your protocol.

It is particularly important that appropriate access control applies to payments, as noted in [SWC-105](https://swcregistry.io/docs/SWC-105), but other actions such as overwriting data as described in [SWC-124](https://swcregistry.io/docs/SWC-126), or changing specific access controls, also need to be appropriately protected \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\]. This requirement matches \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\] Improper Access Control.

See also "[Access Restriction](https://fravoll.github.io/solidity-patterns/access_restriction.html)" in \[<a href="index.html#bib-solidity-patterns" class="bibref" data-link-type="biblio" title="Solidity Patterns">solidity-patterns</a>\].

**\[Q\] Use Revocable and Transferable Access Control Permissions<a href="index.html#req-3-revocable-permisions" class="selflink"></a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* implement a mechanism to revoke and transfer those permissions.

Privileged Accounts can perform administrative tasks on the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a>. If those accounts are compromised or responsibility to perform those tasks is assigned to different people, it is important to have a mechanism to revoke and transfer those permissions.

**\[Q\] No Single Admin EOA for Privileged Actions<a href="index.html#req-3-no-single-admin-eoa" class="selflink"></a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.

Privileged accounts can perform administrative tasks on the <a href="index.html#dfn-set-of-contracts" class="internalDFN" data-link-type="dfn">Set of Contracts</a>. If a single EOA can perform these actions, and that permission cannot be revoked, the risks to a Smart Contract posed by a compromised or lost private key can be existential.

**\[Q\] Verify External Calls<a href="index.html#req-3-external-calls" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

At <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a> auditors have a lot of flexibility to offer <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> for different uses of External Calls.

This requirement effectively allows a reviewer to declare that the destination of an external call is not a security risk. It is important to note that any such declaration reflects very closely on the reputation of a reviewer.

It is inappropriate to assume that a smart contract is secure just because it is widely used, and it is unacceptable to assume that a smart contract provided by a user in the future will be secure - this is a known vector that has been used for many serious security breaches.

It is also important to consider how any code referenced and declared safe by the reviewer could be vulnerable to attacks based on its use of external calls.

To take a common example, swap contracts that allow a user to provide any pair of token contracts are potentially at risk if one of those contracts is malicious, or simply vulnerable, in a way the swap contract does not anticipate and protect against.

See also the related requirements [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and** [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

**\[Q\] Verify `tx.origin` Usage<a href="index.html#req-3-verify-tx.origin" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

`tx.origin` can be used to enable phishing attacks, tricking a user into interacting with a contract that gains access to all the funds in their account. It is generally the wrong choice for authorization of a caller for which `msg.sender` is the safer choice.

See also <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirements</a> [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control), the [section "`tx.origin`"](https://docs.soliditylang.org/en/latest/security-considerations.html?highlight=tx.origin) in Solidity Security Considerations \[<a href="index.html#bib-solidity-security" class="bibref" data-link-type="biblio" title="Security Considerations - Solidity Documentation.">solidity-security</a>\], and CWE 284: Improper Access Control \[<a href="index.html#bib-cwe-284" class="bibref" data-link-type="biblio" title="CWE-284: Improper Access Control">CWE-284</a>\].

**\[Q\] Specify Solidity Compiler Versions to Produce Consistent Output<a href="index.html#req-3-consistent-solidity-output" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* specify a range of Solidity versions in its `pragma` directive(s) that produce the same Bytecode given the same compilation options.

Different compiler versions can have different security vulnerabilities and introduce unexpected behavior. While compiler upgrades *almost* always improve security characteristics, there is no possible way to guarantee this is the case for any given change made in the future.

For this reason, if the bytecode that is produced by compliling the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> changes, this specification requires a new assessment to achieve <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>.

Explicitly specifying an exact Solidity version ensures consistency between development, auditing, and deployment by preventing compilation with other versions. Specifying a range of Solidity Compiler Versions such that compiling the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> with any of the Soldity compiler versions within that range using the same settings produces the same Bytecode, means that <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA Ethtrust Certification</a> of <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> is valid for as long as it is known there is no change to the compiler that necessitates a new analysis.

Note

The wording of this requirement allows for the specification of an open-ended range in `pragma` directives, such as

<a href="index.html#example-20" class="self-link">Example</a>

      pragma solidity >=0.8.14;

However <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> requires specifying a specific range of Solidity Compiler Versions for which it is valid, in case a future version of the Solidity Compiler compiles the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> to produce different Bytecode.

This is intended to ensure that where an upgrade to the compiler does not result in any change to the Bytecode produced, re-certification of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for a newer Solidity compiler version needs very little work.

Note that even with a specific pragma directive, different compiler implementations claiming to be the same version, optimization settings, and other build configuration parameters can all influence the Bytecode produced.

### 5.4 Recommended Good Practices<a href="index.html#sec-good-practice-recommendations" class="self-link" aria-label="§"></a>

This section describes good practices that require substantial human judgement to evaluate, where there isn't a clear way to determine if it has been done or not, or where a poor implementation can reduce rather than increase the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>. Testing for, and meeting these requirements does not directly affect conformance to this document. Note however that meeting the Recommended Good Practice [**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible) will in practice mean that <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> meets all the Requirements based on Compiler Bugs, including the majority of Requirements for <a href="index.html#dfn-security-level-s" class="internalDFN" data-link-type="dfn">Security Level [S]</a>.

**\[GP\] Check For and Address New Security Bugs<a href="index.html#req-R-check-new-bugs" class="selflink"></a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 1 November 2023 and address them.

This version of the specification was finalized late in 2023. New vulnerabilities are discovered from time to time, on an unpredictable schedule. The latest solidity compiler bug accounted for in this version is SOL-2023-3.

Checking for security alerts published too late to be incorporated into the current version of this document is an important technique for maintaining the highest possible security.

There are other sources of information on new security vulnerabilities, from \[<a href="index.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\] to following the blogs of many security-oriented organizations such as those that contributed to this specification.

**\[GP\] Meet as Many Requirements as Possible<a href="index.html#req-R-meet-all-possible" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

While meeting some requirements for a higher <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> Security Level makes no change to the formal conformance level of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, each requirement is specified because meeting it provides protection against specific known attacks. If it is possible to meet a particular requirement, even if it is not necessary for conformance at the <a href="index.html#dfn-security-levels" class="internalDFN" data-link-type="dfn">Security Level</a> being tested, meeting that requirement will improve the security of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and is therefore worth doing.

**\[GP\] Use Latest Compiler<a href="index.html#req-R-use-latest-compiler" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable Solidity compiler version.

The Solidity compiler is regularly updated to improve performance but also specifically to fix security vulnerabilities that are discovered. There are many requirements in <a href="index.html#sec-1-compiler-bugs" class="sec-ref">§ 5.1.3 Compiler Bugs </a> that are related to vulnerabilities known at the time this specification was written, as well as enhancements made to provide better security by default. In general, newer Solidity compiler versions improve security. Unless there is a specific known reason not to do so, using the latest Solidity compiler version available will result in better security.

**\[GP\] Write Clear, Legible Solidity Code<a href="index.html#req-R-clean-code" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

There are no strict rules defining how to write clear code. It is important to use sufficiently descriptive names, comment code appropriately, and use structures that are easy to understand without causing the code to become excessively large, because that also makes it difficult to read and understand.

Excessive nesting, unstructured comments, complex looping structures, and the use of very terse names for variables and functions are examples of coding styles that can also make code harder to understand.

It is important to note that in some cases, developers can sacrifice easy reading for other benefits such as reducing gas costs - this can be mitigated somewhat by well-documented code.

Likewise, for complex code involving multiple individual smart contracts, the way source is organised into files can help clarify or obscure what's happening. In particular, naming source code files to match the names of smart contracts they define is a common pattern that eases understanding.

This Good Practice extends somewhat the <a href="index.html#dfn-related-requirements" class="internalDFN" data-link-type="dfn">Related Requirement</a> [**\[Q\] Code Linting**](index.html#req-3-linted), but judgements about how to meet it are necessarily more subjective than in the specifics that requirement establishes. Those looking for additional guidance on code styling can refer to the \[<a href="index.html#bib-solidity-style-guide" class="bibref" data-link-type="biblio" title="Solidity Style Guide - Solidity Documentation">Solidity-Style-Guide</a>\].

**\[GP\] Follow Accepted ERC Standards<a href="index.html#req-R-follow-erc-standards" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case.

An ERC is a category of \[<a href="index.html#bib-eip" class="bibref" data-link-type="biblio" title="EIP-1: EIP Purpose and Guidelines">EIP</a>\] (Ethereum Improvement Proposal) that defines application-level standards and conventions, including smart contract standards such as token standards \[<a href="index.html#bib-erc20" class="bibref" data-link-type="biblio" title="EIP-20: Token Standard">ERC20</a>\] and name registries \[<a href="index.html#bib-erc137" class="bibref" data-link-type="biblio" title="ERC-137: Ethereum Domain Name Service - Specification">ERC137</a>\].

While following ERC standards will not inherently make Solidity code secure, they do enable developers to integrate with common interfaces and follow known conventions for expected behavior. If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> does claim to follow a given ERC, its functional correctness in conforming to that standard can be verified by auditors.

**\[GP\] Define a Software License<a href="index.html#req-R-define-license" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license

A software license provides legal guidance on how contributors and users can interact with the code, including auditors and whitehats. Because bytecode deployed to public networks can be read by anyone, it is common practice to use an Open-Source license for the Solidity code used to generate it.

It is important to choose a \[<a href="index.html#bib-software-license" class="bibref" data-link-type="biblio" title="Choosing an Open Source License">software-license</a>\] that best addresses the needs of the project, and clearly link to it throughout the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> and documentation, e.g. using a prominent LICENSE file in the code repository and referencing it from each source file.

**\[GP\] Disclose New Vulnerabilities Responsibly<a href="index.html#req-R-notify-news" class="selflink"></a>**
Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.

New security vulnerabilities are discovered from time to time. It helps the efforts to revise this specification to ensure the Working Group is aware of new vulnerabilities, or new knowledge regarding existing known vulnerabilities.

The EEA has agreed to manage a specific email address for such notifications - and if that changes, to update this specification accordingly.

**\[GP\] Use Fuzzing<a href="index.html#req-R-fuzzing-in-testing" class="selflink"></a>**
<a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> *SHOULD* be used to probe <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for errors.

Effective Fuzzing can take days or even weeks: it is better to be patient than to stop it prematurely.

Because Fuzzing relies on a <a href="index.html#dfn-corpus" class="internalDFN" data-link-type="dfn">Corpus</a>, it is important to maintain that Corpus to maximise code coverage, and helpful to prune unnecessary or duplicate inputs for efficiency.

<a href="index.html#example-21-fuzzing-specification-with-scribble" class="self-link">Example 21</a>: Fuzzing specification with Scribble

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

Fuzzing rules and properties can be complex and depend on specific contracts, functions, variables, their values before and/or after execution, and potentially many other things. If any vulnerabilities are discovered in the Solidity compiler version by <a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> please [disclose them responsibly](index.html#sec-notifying-new-vulnerabilities).

**\[GP\] Use Mutation Testing<a href="index.html#req-R-mutation-testing" class="selflink"></a>**
<a href="index.html#dfn-mutation-testing" class="internalDFN" data-link-type="dfn">Mutation Testing</a> *SHOULD* be used to evaluate and improve the quality of test suites for smart contracts.

<a href="index.html#dfn-mutation-testing" class="internalDFN" data-link-type="dfn">Mutation Testing</a> is a fault-based testing technique that introduces artificial defects (mutations) into the source code to find potential gaps in test coverage.

There are several categories of Mutation Operators specifically relevant to smart contracts:

<a href="index.html#dfn-state-variable-mutations" class="internalDFN" data-link-type="dfn">State Variable Mutations</a>:
Modify state variable declarations and operations, including:

- Changing visibility modifiers (`public`/`private`)
- Altering constant values
- Modifying storage locations

<a href="index.html#dfn-arithmetic-mutations" class="internalDFN" data-link-type="dfn">Arithmetic Mutations</a>:
Alter arithmetic operations to test numerical calculations:

- Replacing operators (+, -, \*, /)
- Modifying boundary conditions
- Introducing overflow/underflow conditions

<a href="index.html#dfn-control-flow-mutations" class="internalDFN" data-link-type="dfn">Control Flow Mutations</a>:
Change the execution paths through the contract:

- Inverting conditional statements
- Modifying loop conditions
- Altering function modifiers

<a href="index.html#dfn-access-control-mutations" class="internalDFN" data-link-type="dfn">Access Control Mutations</a>:
Security-critical permission checks:

- Removing ownership checks
- Altering role-based permissions
- Modifying authentication logic

It can be helpful to integrate <a href="index.html#dfn-mutation-testing" class="internalDFN" data-link-type="dfn">Mutation Testing</a> into the CI/CD pipeline, with appropriate performance benchmarks (e.g., minimum mutation score thresholds, test timeout limits), and exit criteria (e.g., critical path mutation coverage, required mutation operators).

**\[GP\] Use Formal Verification<a href="index.html#req-R-formal-verification" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* undergo formal verification.

Formal verification is a family of techniques that can mathematically prove functional correctness of smart contracts. It has been used in other applications such as embedded systems. There are many uses for formal verification in smart contracts, such as testing liveness, protocol invariants for safety at a high level, or proving narrower, more specific properties of a program's execution.

In formal verification, a formal (symbolic or mathematical) specification of the expected or desired outcome of a smart contract is created, enabling a formal mathematical proof of a protocol's correctness. The smart contract itself is often translated into a formal language for this purpose.

Several languages and programs exist for creating fromal verification proofs, some with the explicit aim of making formal verification more accessible to casual users and non-mathematicians. Please see \[<a href="index.html#bib-ef-sl" class="bibref" data-link-type="biblio" title="Specification languages for creating formal specifications">EF-SL</a>\] for some examples.

When implemented correctly by a practitioner with experience and skill, formal verification can make guarantees that fuzzing and testing cannot provide. However, that is often difficult to achieve in practice. Formal verification requires substantial manual labor and expertise.

A comprehensive formal verification most likely has a much a higher cost and complexity than unit or integration testing, fuzzing, or other methods. The immutable nature of many smart contracts, and the complexity of upgrading contracts when it is possible, makes formal verification appealing to administrators and stakeholders of protocols.

**\[GP\] Select an Appropriate Threshold for Multisig Wallets<a href="index.html#req-R-multisig-threshold" class="selflink"></a>**
Multisignature requirements for privileged actions *SHOULD* have a sufficient number of signers, and NOT require "1 of N" nor all signatures.

Requiring multiple signatures for administrative actions has become the standard for many teams. When not managed carefully, they can become a source of attack even if the smart contract code is secure.

The problem with "1 of N" setups, that enable a single account to execute transactions, is that it is relatively easy to exploit. "N of N" setups meanwhile mean that if even one signer loses access to their account or will not approve an action, there is no possibility for approval. This can affect necessary operations such as the replacement of one signer with another, for example to ensure operational continuity, which can have a very serious impact.

Choosing a lower number of signatures to meet the requirement allows for quicker response, while a higher value requires stronger majority support. Consider using an "M of N" multisignature where M = (N/2) + 1, in other words, the smallest possible majority of signatures are necessary for approval, as a starting point. However it is important to consider how many potential signers there are, and the specific situations where signatures are needed, to determine a reasonably good value for M in a given case.

## A. Additional Information<a href="index.html#sec-additional-information" class="self-link" aria-label="§"></a>

### A.1 Defined Terms<a href="index.html#sec-definitions" class="self-link" aria-label="§"></a>

The following is a list of terms defined in this Specification.

- <a href="index.html#dfn-access-control-mutations" id="dfnanchor-0">Access Control Mutations</a>
- <a href="index.html#dfn-arithmetic-mutations" id="dfnanchor-1">Arithmetic Mutations</a>
- <a href="index.html#dfn-back-running" id="dfnanchor-2">Back-Running</a>
- <a href="index.html#dfn-black-box-fuzzing" id="dfnanchor-3">Black-Box Fuzzing</a>
- <a href="index.html#dfn-censorship-attacks" id="dfnanchor-5">Censorship Attacks</a>
- <a href="index.html#dfn-checks-effects-interactions" id="dfnanchor-6">Checks-Effects-Interactions</a>
- <a href="index.html#dfn-control-flow-mutations" id="dfnanchor-7">Control Flow Mutations</a>
- <a href="index.html#dfn-corpus" id="dfnanchor-8">Corpus</a>
- <a href="index.html#dfn-economic-warfare" id="dfnanchor-9">Economic Warfare</a>
- <a href="index.html#dfn-eea-ethtrust-certified" id="dfnanchor-10">EEA EthTrust Certification</a>
- <a href="index.html#dfn-evm" id="dfnanchor-11">EVM</a>
- <a href="index.html#dfn-evm-version" id="dfnanchor-12">EVM versions</a>
- <a href="index.html#dfn-execution-contract" id="dfnanchor-13">Execution Contract</a>
- <a href="index.html#dfn-fixed-length-variable" id="dfnanchor-14">Fixed-length Variable</a>
- <a href="index.html#dfn-flash-loan-attack" id="dfnanchor-15">Flash Loan Attack</a>
- <a href="index.html#dfn-formal-verification" id="dfnanchor-16">Formal Verification</a>
- <a href="index.html#dfn-front-running" id="dfnanchor-17">Front-Running</a>
- <a href="index.html#dfn-fuzzing" id="dfnanchor-18">Fuzzing</a>
- <a href="index.html#dfn-gas-griefing" id="dfnanchor-19">Gas Griefing</a>
- <a href="index.html#dfn-gas-siphoning" id="dfnanchor-20">Gas Siphoning</a>
- <a href="index.html#dfn-gas-tokens" id="dfnanchor-21">Gas Tokens</a>
- <a href="index.html#dfn-governance-exploitation" id="dfnanchor-22">Governance Exploitation</a>
- <a href="index.html#dfn-gray-box-fuzzing" id="dfnanchor-23">Gray-Box Fuzzing</a>
- <a href="index.html#dfn-hard-fork" id="dfnanchor-24">Hard Fork</a>
- <a href="index.html#dfn-hash-collisions" id="dfnanchor-25">Hash Collisions</a>
- <a href="index.html#dfn-homoglyph-attacks" id="dfnanchor-26">Homoglyph Attacks</a>
- <a href="index.html#dfn-infrastructure-security" id="dfnanchor-27">Infrastructure Security</a>
- <a href="index.html#dfn-invariant-testing" id="dfnanchor-28">Invariant Testing</a>
- <a href="index.html#dfn-invariants" id="dfnanchor-29">Invariants</a>
- <a href="index.html#dfn-like-this" id="dfnanchor-30">Like This</a>
- <a href="index.html#dfn-logic-contract" id="dfnanchor-31">Logic Contract</a>
- <a href="index.html#dfn-low-level-call-functions" id="dfnanchor-32">Low-level Call Functions</a>
- <a href="index.html#dfn-malleable-signatures" id="dfnanchor-33">Malleable Signatures</a>
- <a href="index.html#dfn-metamorphic-upgrade" id="dfnanchor-34">Metamorphic Upgrade</a>
- <a href="index.html#dfn-metamorphic-upgrades" id="dfnanchor-35">Metamorphic Upgrades</a>
- <a href="index.html#dfn-mev" id="dfnanchor-36">MEV</a>
- <a href="index.html#dfn-monitoring-and-response" id="dfnanchor-37">Monitoring and Response</a>
- <a href="index.html#dfn-mutation-score" id="dfnanchor-38">Mutation Score</a>
- <a href="index.html#dfn-mutation-testing" id="dfnanchor-39">Mutation Testing</a>
- <a href="index.html#dfn-network-manipulation" id="dfnanchor-40">Network Manipulation</a>
- <a href="index.html#dfn-network-upgrade" id="dfnanchor-41">Network Upgrade</a>
- <a href="index.html#dfn-operational-security-measures" id="dfnanchor-42">Operational Security Measures</a>
- <a href="index.html#dfn-oracle-attacks" id="dfnanchor-43">Oracle Attacks</a>
- <a href="index.html#dfn-oracles" id="dfnanchor-44">Oracles</a>
- <a href="index.html#dfn-ordering-attacks" id="dfnanchor-45">Ordering Attacks</a>
- <a href="index.html#dfn-overriding-requirement" id="dfnanchor-46">Overriding Requirements</a>
- <a href="index.html#dfn-private-data" id="dfnanchor-47">Private Data</a>
- <a href="index.html#dfn-privileged-accounts" id="dfnanchor-48">Privileged Accounts</a>
- <a href="index.html#dfn-property-based-testing" id="dfnanchor-49">Property-Based Testing</a>
- <a href="index.html#dfn-proxy-contract" id="dfnanchor-50">Proxy Contract</a>
- <a href="index.html#dfn-public-interfaces" id="dfnanchor-51">Public Interfaces</a>
- <a href="index.html#dfn-re-entrancy-attacks" id="dfnanchor-52">Re-entrancy Attacks</a>
- <a href="index.html#dfn-read-only-re-entrancy-attack" id="dfnanchor-53">Read-only Re-entrancy Attack</a>
- <a href="index.html#dfn-related-requirements" id="dfnanchor-54">Related Requirements</a>
- <a href="index.html#dfn-sandwich-attacks" id="dfnanchor-55">Sandwich Attacks</a>
- <a href="index.html#dfn-security-level-m" id="dfnanchor-56">Security Level [M]</a>
- <a href="index.html#dfn-security-level-q" id="dfnanchor-57">Security Level [Q]</a>
- <a href="index.html#dfn-security-level-s" id="dfnanchor-58">Security Level [S]</a>
- <a href="index.html#dfn-security-levels" id="dfnanchor-59">Security Levels</a>
- <a href="index.html#dfn-set-of-contracts" id="dfnanchor-60">Set Of Contracts</a>
- <a href="index.html#dfn-sets-of-overriding-requirements" id="dfnanchor-61">Set of Overriding Requirements</a>
- <a href="index.html#dfn-state-variable-mutations" id="dfnanchor-62">State Variable Mutations</a>
- <a href="index.html#dfn-static-analysis" id="dfnanchor-63">Static Analysis</a>
- <a href="index.html#dfn-symbolic-execution" id="dfnanchor-64">Symbolic Execution</a>
- <a href="index.html#dfn-test-coverage" id="dfnanchor-65">Test Coverage</a>
- <a href="index.html#dfn-test-driven-development" id="dfnanchor-66">Test-driven Development</a>
- <a href="index.html#dfn-tested-code" id="dfnanchor-67">Tested Code</a>
- <a href="index.html#dfn-testnet" id="dfnanchor-68">Testnet</a>
- <a href="index.html#dfn-threat-model" id="dfnanchor-69">Threat Model</a>
- <a href="index.html#dfn-twap" id="dfnanchor-70">TWAP</a>
- <a href="index.html#dfn-unicode-direction-control-characters" id="dfnanchor-71">Unicode Direction Control Characters</a>
- <a href="index.html#dfn-unit-testing" id="dfnanchor-72">Unit Testing</a>
- <a href="index.html#dfn-upgradable-contract" id="dfnanchor-73">Upgradable Contract</a>
- <a href="index.html#dfn-valid-conformance-claim" id="dfnanchor-74">Valid Conformance Claim</a>
- <a href="index.html#dfn-white-box-fuzzing" id="dfnanchor-75">White-Box Fuzzing</a>

### A.2 Summary of Requirements<a href="index.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

This section provides a summary of all requirements and Recommended Good Practices in this Specification.

[**\[S\] Encode Hashes with `chainid`**](index.html#req-1-eip155-chainid)**<a href="index.html#req-1-eip155-chainid" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* create hashes for transactions that incorporate `chainid` values following the recommendation described in \[<a href="index.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>\]

[**\[S\] No `CREATE2`**](index.html#req-1-no-create2)**<a href="index.html#req-1-no-create2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `CREATE2` instruction.
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

[**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin)**<a href="index.html#req-1-no-tx.origin" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain a `tx.origin` instruction
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)

[**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check)**<a href="index.html#req-1-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* test that the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check).

[**\[S\] No Hashing Consecutive Variable Length Arguments**](index.html#req-1-no-hashing-consecutive-variable-length-args)**<a href="index.html#req-1-no-hashing-consecutive-variable-length-args" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use `abi.encodePacked()` with consecutive variable length arguments.

[**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct)**<a href="index.html#req-1-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain the `selfdestruct()` instruction or its now-deprecated alias `suicide()`
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented).

[**\[S\] No `assembly {}`**](index.html#req-1-no-assembly)**<a href="index.html#req-1-no-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `assembly {}` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly),
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),
- [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly),
- [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7),
- [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4),
- [**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3), **and**
- if using Solidity compiler version 0.5.5 or 0.5.6, [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly) in \[<a href="index.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\].

[**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo)**<a href="index.html#req-1-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain any of the [Unicode Direction Control Characters](index.html#dfn-unicode-direction-control-characters) `U+2066`, `U+2067`, `U+2068`, `U+2029`, `U+202A`, `U+202B`, `U+202C`, `U+202D`, or `U+202E`
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo).

[**\[S\] Check External Calls Return**](index.html#req-1-check-return)**<a href="index.html#req-1-check-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="internalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. `call()`, `delegatecall()`, `staticcall()`, and `send()`) *MUST* check the returned value from each usage to determine whether the call failed,
**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[M\] Handle External Call Returns**](index.html#req-2-handle-return).

[**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i)**<a href="index.html#req-1-use-c-e-i" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that makes external calls *MUST* use the <a href="index.html#dfn-checks-effects-interactions" class="internalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="internalDFN" data-link-type="dfn">Re-entrancy Attacks</a>
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[M\] Protect external calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall)**<a href="index.html#req-1-delegatecall" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* contain the `delegatecall()` instruction
**unless** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:

- [**\[M\] Protect External Calls**](index.html#req-2-external-calls), **and**
- [**\[M\] Document Special Code Use**](index.html#req-2-documented),

**or** it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a>

- [**\[Q\] Verify External Calls**](index.html#req-3-external-calls),
- [**\[Q\] Document Contract Logic**](index.html#req-3-documented),
- [**\[Q\] Document System Architecture**](index.html#req-3-document-system), **and**
- [**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented).

[**\[S\] Compiler Bug SOL-2023-3**](index.html#req-1-compiler-SOL-2023-3)**<a href="index.html#req-1-compiler-SOL-2023-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that includes Yul code and uses the `verbatim` instruction twice, in each case surrounded by identical code, *MUST* disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).

[**\[S\] Compiler Bug SOL-2022-6**](index.html#req-1-compiler-SOL-2022-6)**<a href="index.html#req-1-compiler-SOL-2022-6" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a `struct`, `return` value, or a parameter list) that includes a dynamic component with the ABIEncoderV2, and whose last element is a `calldata` static array of base type `uint` or `bytes32`, *MUST NOT* use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).

[**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push)**<a href="index.html#req-1-compiler-SOL-2022-5-push" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- copies `bytes` arrays from `calldata` or `memory` whose size is not a multiple of 32 bytes, **and**
- has an empty `.push()` instruction that writes to the resulting array,

*MUST NOT* use a Solidity compiler version older than 0.8.15.

[**\[S\] Compiler Bug SOL-2022-3**](index.html#req-1-compiler-SOL-2022-3)**<a href="index.html#req-1-compiler-SOL-2022-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses `memory` and `calldata` pointers for the same function, **and**
- changes the data location of a function during inheritance, **and**
- performs an internal call at a location that is only aware of the original function signature from the base contrac

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).

[**\[S\] Compiler Bug SOL-2022-2**](index.html#req-1-compiler-SOL-2022-2)**<a href="index.html#req-1-compiler-SOL-2022-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> with a nested array tha

- passes it to an external function, **or**
- passes it as input to `abi.encode()`, **or**
- uses it in an even

*MUST NOT* use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).

[**\[S\] Compiler Bug SOL-2022-1**](index.html#req-1-compiler-SOL-2022-1)**<a href="index.html#req-1-compiler-SOL-2022-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- uses Number literals for a <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, **or**
- uses String literals for any <a href="index.html#dfn-bytesnn" class="internalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,

**and** passes such literals to `abi.encodeCall()` as the first parameter, *MUST NOT* use Solidity compiler version 0.8.11 nor 0.8.12.

[**\[S\] Compiler Bug SOL-2021-4**](index.html#req-1-compiler-sol-2021-4)**<a href="index.html#req-1-compiler-sol-2021-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes *MUST NOT* use Solidity compiler version 0.8.8.

[**\[S\] Compiler Bug SOL-2021-2**](index.html#req-1-compiler-SOL-2021-2)**<a href="index.html#req-1-compiler-SOL-2021-2" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that uses `abi.decode()` on byte arrays as `memory` *MUST NOT* use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).

[**\[S\] Compiler Bug SOL-2021-1**](index.html#req-1-compiler-SOL-2021-1)**<a href="index.html#req-1-compiler-SOL-2021-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction `keccak(``mem``,``length``)` where

- the values of `mem` are equal, **and**
- the values of `length` are unequal, **and**
- the values of `length` are not multiples of 32,

*MUST NOT* use the Optimizer with a Solidity compiler version older than 0.8.3.

[**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060)**<a href="index.html#req-1-compiler-060" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 2](https://entethalliance.org/specs/ethtrust-sl/v2/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[S\] No Overflow/Underflow**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-overflow-underflow)
- [**\[S\] Compiler Bug SOL-2020-11-push**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-11-push)
- [**\[S\] Compiler Bug SOL-2020-10**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-10)
- [**\[S\] Compiler Bug SOL-2020-9**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-9)
- [**\[S\] Compiler Bug SOL-2020-8**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-8)
- [**\[S\] Compiler Bug SOL-2020-6**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-6)
- [**\[S\] Compiler Bug SOL-2020-7**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-7)
- [**\[S\] Compiler Bug SOL-2020-5**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-5)
- [**\[S\] Compiler Bug SOL-2020-4**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-4)

**AND**

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

[**\[S\] No Ancient Compilers**](index.html#req-1-no-ancient-compilers)**<a href="index.html#req-1-no-ancient-compilers" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.3.

[**\[M\] Pass Security Level \[S\]**](index.html#req-2-pass-l1)**<a href="index.html#req-2-pass-l1" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="internalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-one" class="sec-ref">§ 5.1 Security Level [S]</a>.

[**\[M\] Explicitly Disambiguate Evaluation Order**](index.html#req-2-enforce-eval-order)**<a href="index.html#req-2-enforce-eval-order" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain statements where variable evaluation order can result in different outcomes

[**\[M\] Verify Exact Balance Checks**](index.html#req-2-verify-exact-balance-check)**<a href="index.html#req-2-verify-exact-balance-check" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that checks whether the balance of an account is exactly equal to (i.e. `==`) a specified amount or the value of a variable. *MUST* protect itself against transfers affecting the balance tested.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Exact Balance Check**](index.html#req-1-exact-balance-check).

[**\[M\] No Unnecessary Unicode Controls**](index.html#req-2-unicode-bdo)**<a href="index.html#req-2-unicode-bdo" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use <a href="index.html#dfn-unicode-direction-control-characters" class="internalDFN" data-link-type="dfn">Unicode direction control characters</a> **unless** they are necessary to render text appropriately, and the resulting text does not mislead readers.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No Unicode Direction Control Characters**](index.html#req-1-unicode-bdo).

[**\[M\] No Homoglyph-style Attack**](index.html#req-2-no-homoglyph-attack)**<a href="index.html#req-2-no-homoglyph-attack" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks, if the impact is misleading.

[**\[M\] Protect External Calls**](index.html#req-2-external-calls)**<a href="index.html#req-2-external-calls" class="selflink"></a>**
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

[**\[M\] Avoid Read-only Re-entrancy Attacks**](index.html#req-2-avoid-readonly-reentrancy)**<a href="index.html#req-2-avoid-readonly-reentrancy" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="internalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.

[**\[M\] Handle External Call Returns**](index.html#req-2-handle-return)**<a href="index.html#req-2-handle-return" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that makes external calls *MUST* reasonably handle possible errors.
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] Check External Calls Return**](index.html#req-1-check-return).

[**\[M\] Document Special Code Use**](index.html#req-2-documented)**<a href="index.html#req-2-documented" class="selflink"></a>**
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
- [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), **and**
- [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall).

[**\[M\] Ensure Proper Rounding of Computations Affecting Value**](index.html#req-2-check-rounding)**<a href="index.html#req-2-check-rounding" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* identify and protect against exploiting rounding errors:

- The possible range of error introduced by such rounding *MUST* be documented.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* unintentionally create or lose value through rounding.
- <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.

[**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct)**<a href="index.html#req-2-self-destruct" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains the `selfdestruct()` or `suicide()` instructions *MUST*

- ensure that only authorised parties can call the method, **and**
- *MUST* protect those calls in a way that is fully compatible with the claims of the contract author,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control).

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `selfdestruct()`**](index.html#req-1-self-destruct).

[**\[M\] Avoid Common `assembly {}` Attack Vectors**](index.html#req-2-safe-assembly)**<a href="index.html#req-2-safe-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* use the `assembly {}` instruction to change a variable **unless** the code cannot:

- create storage pointer collisions, **nor**
- allow arbitrary values to be assigned to variables of type `function`.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Protect `CREATE2` Calls**](index.html#req-2-protect-create2)**<a href="index.html#req-2-protect-create2" class="selflink"></a>**
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

[**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow)**<a href="index.html#req-2-overflow-underflow" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* contain calculations that can overflow or underflow **unless**

- there is a demonstrated need (e.g. for use in a modulo operation) and
- there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.

[**\[M\] Sources of Randomness**](index.html#req-2-random-enough)**<a href="index.html#req-2-random-enough" class="selflink"></a>**
Sources of randomness used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* be sufficiently resistant to prediction that their purpose is met.

[**\[M\] Don't Misuse Block Data**](index.html#req-2-block-data-misuse)**<a href="index.html#req-2-block-data-misuse" class="selflink"></a>**
Block numbers and timestamps used in <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST NOT* introduce vulnerabilities to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> or similar attacks.

[**\[M\] Proper Signature Verification**](index.html#req-2-signature-verification)**<a href="index.html#req-2-signature-verification" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* properly verify signatures to ensure authenticity of messages that were signed off-chain.

[**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay)**<a href="index.html#req-2-malleable-signatures-for-replay" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks *MUST* ensure that signatures cannot be reused:

- In the same function to verify the same message, **nor**
- In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **nor**
- In more than one contract address to verify the same message, in which the same account(s) may be signing messages, **nor**
- In the same contract address across multiple chains,

**unless** it meets the <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> [**\[Q\] Intended Replay**](index.html#req-3-intended-replay). Additionally, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="internalDFN" data-link-type="dfn">Malleable Signatures</a>.

[**\[M\] Solidity Compiler Bug 2023-1**](index.html#req-2-compiler-SOL-2023-1)**<a href="index.html#req-2-compiler-SOL-2023-1" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses `.selector` *MUST* use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.

[**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7)**<a href="index.html#req-2-compiler-SOL-2022-7" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing `return()` or `stop()` instructions *MUST NOT* use a Solidity compiler version between 0.8.13 and 0.8.16 inclusive.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly)**<a href="index.html#req-2-compiler-SOL-2022-5-assembly" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> tha

- copies `bytes` arrays from calldata or memory whose size is not a multiple of 32 bytes, **and**
- has an `assembly {}` instruction that reads that data without explicitly matching the length that was copied,

*MUST NOT* use a Solidity compiler version older than 0.8.15.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4)**<a href="index.html#req-2-compiler-SOL-2022-4" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that has at least two `assembly {}` instructions, such tha

- one writes to memory e.g. by storing a value in a variable, but does not access that memory again, **and**
- code in a another `assembly {}` instruction refers to that memory,

*MUST NOT* use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Compiler Bug SOL-2021-3**](index.html#req-2-compiler-SOL-2021-3)**<a href="index.html#req-2-compiler-SOL-2021-3" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that reads an `immutable` signed integer of a `type` shorter than 256 bits within an `assembly {}` instruction *MUST NOT* use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] No `assembly {}`**](index.html#req-1-no-assembly).

[**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060)**<a href="index.html#req-2-compiler-060" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.8.0, **unless** it meets the requirement [**\[M\] Compiler Bug Check Constructor Payment**](https://entethalliance.org/specs/ethtrust-sl/v2/#req-2-compiler-check-payable-constructor) from the [EEA EthTrust Security Levels Specification Version 2](https://entethalliance.org/specs/ethtrust-sl/v2/), as an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a>,

**AND**

<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* use a Solidity compiler version older than 0.6.0, **unless** it meets all the following requirements from the [EEA EthTrust Security Levels Specification Version 1](https://entethalliance.org/specs/ethtrust-sl/v1/), as <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirements</a>:

- [**\[M\] Compiler Bug SOL-2020-2**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2),
- [**\[M\] Compiler Bug SOL-2019-2 in `assembly {}`**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly),
- [**\[M\] Compiler Bug Check Identity Calls**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls),
- [**\[M\] Validate `ecrecover()` input**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input),
- [**\[M\] Compiler Bug No Zero Ether Send**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send), and
- [**\[M\] Declare `storage` Explicitly**](https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage).

[**\[Q\] Pass Security Level \[M\]**](index.html#req-3-pass-l2)**<a href="index.html#req-3-pass-l2" class="selflink"></a>**
To be eligible for <a href="index.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> at <a href="index.html#dfn-security-level-q" class="internalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* meet the requirements for <a href="index.html#sec-levels-two" class="sec-ref">§ 5.2 Security Level [M]</a>.

[**\[Q\] Use TimeLock Delays for Sensitive Operations**](index.html#req-3-timelock-for-privileged-actions)**<a href="index.html#req-3-timelock-for-privileged-actions" class="selflink"></a>**
Sensitive operations that affect all or a majority of users *MUST* use \[<a href="index.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>\] delays.

[**\[Q\] Code Linting**](index.html#req-3-linted)**<a href="index.html#req-3-linted" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a>

- *MUST NOT* create unnecessary variables, **and**
- *MUST NOT* use the same name for functions, variables or other tokens that can occur within the same scope, **and**
- *MUST NOT* include `assert()` statements that fail in normal operation, **and**
- *MUST NOT* include code that cannot be reached in execution
  **except** for code explicitly intended to manage unexpected errors, such as `assert()` statements, **and**
- *MUST NOT* contain a function that has the same name as the smart contract **unless** it is explicitly declared as a constructor using the `constructor` keyword, **and**
- *MUST* explicitly declare the visibility of all functions and variables, **and**
- *MUST* specify one or more Solidity compiler versions in its `pragma` directive.

[**\[Q\] Manage Gas Use Increases**](index.html#req-3-enough-gas)**<a href="index.html#req-3-enough-gas" class="selflink"></a>**
Sufficient Gas *MUST* be available to work with data structures in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).

[**\[Q\] Protect Gas Usage**](index.html#req-3-protect-gas)**<a href="index.html#req-3-protect-gas" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect against malicious actors stealing or wasting gas.

[**\[Q\] Protect against Oracle Failure**](index.html#req-3-check-oracles)**<a href="index.html#req-3-check-oracles" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* protect itself against malfunctions in <a href="index.html#dfn-oracles" class="internalDFN" data-link-type="dfn">Oracles</a> it relies on.

[**\[Q\] Protect against Ordering Attacks**](index.html#req-3-block-front-running)**<a href="index.html#req-3-block-front-running" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* manage information in such a way that it protects against <a href="index.html#dfn-ordering-attacks" class="internalDFN" data-link-type="dfn">Ordering Attacks</a>.

[**\[Q\] Protect against MEV Attacks**](index.html#req-3-block-mev)**<a href="index.html#req-3-block-mev" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="internalDFN" data-link-type="dfn">MEV</a> attacks *MUST* follow appropriate design patterns to mitigate this risk.

[**\[Q\] Protect Against Governance Takeovers**](index.html#req-3-protect-governance)**<a href="index.html#req-3-protect-governance" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system *MUST* protect against malicious exploitation of the governance design.

[**\[Q\] Process All Inputs**](index.html#req-3-all-valid-inputs)**<a href="index.html#req-3-all-valid-inputs" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* validate inputs, and function correctly whether the input is as designed or malformed.

[**\[Q\] State Changes Trigger Events**](index.html#req-3-event-on-state-change)**<a href="index.html#req-3-event-on-state-change" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* emit a contract event for all transactions that cause state changes.

[**\[Q\] No Private Data**](index.html#req-3-no-private-data)**<a href="index.html#req-3-no-private-data" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST NOT* store <a href="index.html#dfn-private-data" class="internalDFN" data-link-type="dfn">Private Data</a> on the blockchain.

[**\[Q\] Intended Replay**](index.html#req-3-intended-replay)**<a href="index.html#req-3-intended-replay" class="selflink"></a>**
If a signature within the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance *MUST* be intended, documented, **and** safe for re-use.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay).

[**\[Q\] Document Contract Logic**](index.html#req-3-documented)**<a href="index.html#req-3-documented" class="selflink"></a>**
A specification of the business logic that the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement *MUST* be available to anyone who can call the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

[**\[Q\] Document System Architecture**](index.html#req-3-document-system)**<a href="index.html#req-3-document-system" class="selflink"></a>**
Documentation of the system architecture for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.

[**\[Q\] Document Threat Models**](index.html#req-3-document-threats)**<a href="index.html#req-3-document-threats" class="selflink"></a>**
Documented Threat Models for the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be provided, describing each threat, security assumptions, expected responses, and expected outcomes.

[**\[Q\] Annotate Code with NatSpec**](index.html#req-3-annotate)**<a href="index.html#req-3-annotate" class="selflink"></a>**
All <a href="index.html#dfn-public-interfaces" class="internalDFN" data-link-type="dfn">Public Interfaces</a> contained in the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* be annotated with inline comments according to the \[<a href="index.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation">NatSpec</a>\] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.

[**\[Q\] Implement as Documented**](index.html#req-3-implement-as-documented)**<a href="index.html#req-3-implement-as-documented" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> *MUST* behave as described in the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented), **and** [**\[Q\] Document System Architecture**](index.html#req-3-document-system).

[**\[Q\] Enforce Least Privilege**](index.html#req-3-access-control)**<a href="index.html#req-3-access-control" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> that enables privileged access *MUST* implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for [**\[Q\] Document Contract Logic**](index.html#req-3-documented).
This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[M\] Protect Self-destruction**](index.html#req-2-self-destruct).

[**\[Q\] Use Revocable and Transferable Access Control Permissions**](index.html#req-3-revocable-permisions)**<a href="index.html#req-3-revocable-permisions" class="selflink"></a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* implement a mechanism to revoke and transfer those permissions.

[**\[Q\] No Single Admin EOA for Privileged Actions**](index.html#req-3-no-single-admin-eoa)**<a href="index.html#req-3-no-single-admin-eoa" class="selflink"></a>**
If the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it *MUST* ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.

[**\[Q\] Verify External Calls**](index.html#req-3-external-calls)**<a href="index.html#req-3-external-calls" class="selflink"></a>**
<a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that contains external calls

- *MUST* document the need for them, **and**
- *MUST* protect them in a way that is fully compatible with the claims of the contract author.

This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="internalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for [**\[S\] Use Check-Effects-Interaction**](index.html#req-1-use-c-e-i), and for [**\[M\] Protect External Calls**](index.html#req-2-external-calls).

[**\[Q\] Verify `tx.origin` Usage**](index.html#req-3-verify-tx.origin)**<a href="index.html#req-3-verify-tx.origin" class="selflink"></a>**
For <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> that uses `tx.origin`, each instance

- *MUST* be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>, **and**
- *MUST NOT* allow assertions about contract functionality made for [**\[Q\] Document Contract Logic**](index.html#req-3-documented) or [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a>.

This is an <a href="index.html#dfn-overriding-requirement" class="internalDFN" data-link-type="dfn">Overriding Requirement</a> for [**\[S\] No `tx.origin`**](index.html#req-1-no-tx.origin).

[**\[Q\] Specify Solidity Compiler Versions to Produce Consistent Output**](index.html#req-3-consistent-solidity-output)**<a href="index.html#req-3-consistent-solidity-output" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *MUST* specify a range of Solidity versions in its `pragma` directive(s) that produce the same Bytecode given the same compilation options.

[**\[GP\] Check For and Address New Security Bugs**](index.html#req-R-check-new-bugs)**<a href="index.html#req-R-check-new-bugs" class="selflink"></a>**
Check \[<a href="index.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>\] and other sources for bugs announced after 1 November 2023 and address them.

[**\[GP\] Meet as Many Requirements as Possible**](index.html#req-R-meet-all-possible)**<a href="index.html#req-R-meet-all-possible" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.

[**\[GP\] Use Latest Compiler**](index.html#req-R-use-latest-compiler)**<a href="index.html#req-R-use-latest-compiler" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* use the latest available stable Solidity compiler version.

[**\[GP\] Write Clear, Legible Solidity Code**](index.html#req-R-clean-code)**<a href="index.html#req-R-clean-code" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* be written for easy understanding.

[**\[GP\] Follow Accepted ERC Standards**](index.html#req-R-follow-erc-standards)**<a href="index.html#req-R-follow-erc-standards" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* conform to finalized \[<a href="index.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>\] standards when it is reasonably capable of doing so for its use-case.

[**\[GP\] Define a Software License**](index.html#req-R-define-license)**<a href="index.html#req-R-define-license" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* define a software license

[**\[GP\] Disclose New Vulnerabilities Responsibly**](index.html#req-R-notify-news)**<a href="index.html#req-R-notify-news" class="selflink"></a>**
Security vulnerabilities that are not addressed by this specification *SHOULD* be brought to the attention of the Working Group and others through responsible disclosure as described in <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.

[**\[GP\] Use Fuzzing**](index.html#req-R-fuzzing-in-testing)**<a href="index.html#req-R-fuzzing-in-testing" class="selflink"></a>**
<a href="index.html#dfn-fuzzing" class="internalDFN" data-link-type="dfn">Fuzzing</a> *SHOULD* be used to probe <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> for errors.

[**\[GP\] Use Mutation Testing**](index.html#req-R-mutation-testing)**<a href="index.html#req-R-mutation-testing" class="selflink"></a>**
<a href="index.html#dfn-mutation-testing" class="internalDFN" data-link-type="dfn">Mutation Testing</a> *SHOULD* be used to evaluate and improve the quality of test suites for smart contracts.

[**\[GP\] Use Formal Verification**](index.html#req-R-formal-verification)**<a href="index.html#req-R-formal-verification" class="selflink"></a>**
The <a href="index.html#dfn-tested-code" class="internalDFN" data-link-type="dfn">Tested Code</a> *SHOULD* undergo formal verification.

[**\[GP\] Select an Appropriate Threshold for Multisig Wallets**](index.html#req-R-multisig-threshold)**<a href="index.html#req-R-multisig-threshold" class="selflink"></a>**
Multisignature requirements for privileged actions *SHOULD* have a sufficient number of signers, and NOT require "1 of N" nor all signatures.

### A.3 Acknowledgments<a href="index.html#sec-acknowledgments" class="self-link" aria-label="§"></a>

The EEA acknowledges and thanks the many people who contributed to the development of this version of the specification. Please advise us of any errors or omissions.

We are grateful to the entire community who develops Ethereum, for their work and their ongoing collaboration.

In particular we would like to thank the contributors to the [previous version of this specification](https://entethalliance.org/specs/ethtrust-sl/v1/), Co-chairs Christopher Cordi and Opal Graham as well as previous co-chairs David Tarditi and Jaye Herrell the maintainers of the Solidity Compiler and those who write Solidity Security Alerts \[<a href="index.html#bib-solidity-alerts" class="bibref" data-link-type="biblio" title="Solidity Blog - Security Alerts">solidity-alerts</a>\], the community who developed and maintained the Smart Contract Weakness Classification \[<a href="index.html#bib-swcregistry" class="bibref" data-link-type="biblio" title="Smart Contract Weakness Classification Registry">swcregistry</a>\], the Machine Consultancy for publishing the TMIO Best Practices \[<a href="index.html#bib-tmio-bp" class="bibref" data-link-type="biblio" title="Best Practices for Smart Contracts (privately made available to EEA members)">tmio-bp</a>\], and judges and participants in the [Underhanded Solidity](https://underhanded.soliditylang.org/) competitions that have taken place. They have all been very important sources of information and inspiration to the broader community as well as to us in developing this specification.

Security principles have also been developed over many years by many individuals, far too numerous to individually thank for contributions that have helped us to write the present specification. We are grateful to the many people on whose work we build.

### A.4 Changes<a href="index.html#sec-changes" class="self-link" aria-label="§"></a>

Full details of all changes since the version 2 release of this Specification are available to EEA members via the [GitHub repository for this Specification](https://github.com/entethalliance/eta-registry).

This section outlines substantive changes made to the specification since version 2:

A new informative section was added, <a href="index.html#sec-testing-methods" class="sec-ref">§ 4. Testing Methodologies</a>.

#### A.4.1 New Requirements and Recommended Good Practices<a href="index.html#sec-change-new" class="self-link" aria-label="§"></a>

- Add level **\[Q\]** Requirement [**\[Q\] Document Threat Models**](index.html#req-3-document-threats),
- Move the Recommended Good Practice to Use Timelock Delays to a level **\[Q\]** Requirement: [**\[Q\] Use TimeLock Delays for Sensitive Operations**](index.html#req-3-timelock-for-privileged-actions),
- Add level **\[Q\]** Requirement [**\[Q\] Specify Solidity Compiler Versions to Produce Consistent Output**](index.html#req-3-consistent-solidity-output)
- Added Recommended Good Practice [**\[GP\] Use Mutation Testing**](index.html#req-R-mutation-testing)

#### A.4.2 Updated Requirements<a href="index.html#sec-change-update" class="self-link" aria-label="§"></a>

The following requirements have been changed in some way since version 2 of this Specification:

- The requirements for a <a href="index.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> were slightly simplified, and clarified, to make them easier to manage
- Update
  - [**\[S\] No `delegatecall()`**](index.html#req-1-delegatecall),
  - [**\[S\] Compiler Bug SOL-2022-5 with `.push()`**](index.html#req-1-compiler-SOL-2022-5-push),
  - [**\[M\] No Improper Usage of Signatures for Replay Attack Protection**](index.html#req-2-malleable-signatures-for-replay),
  - [**\[M\] Compiler Bug SOL-2022-5 in `assembly {}`**](index.html#req-2-compiler-SOL-2022-5-assembly), and
  - [**\[M\] Compiler Bug SOL-2022-4**](index.html#req-2-compiler-SOL-2022-4)

  to fix grammatical errors and provide clearer formatting
- Update [**\[S\] Compiler Bug SOL-2022-3**](index.html#req-1-compiler-SOL-2022-3) and [**\[S\] Compiler Bug SOL-2022-2**](https://entethalliance.org/specs/ethtrust-sl/v3/req-1-sol-2022-2) to be clear that it is not necessary to test these when using Solidity Compiler version 0.8.13
- Rename **\[M\] No Overflow/Underflow** to [**\[M\] Safe Overflow/Underflow**](index.html#req-2-overflow-underflow)
- Update [**\[M\] Compiler Bug SOL-2022-7**](index.html#req-2-compiler-SOL-2022-7) to be clear that it is not necessary to test this when using Solidity Compiler version 0.8.17
- Rename and Update [**\[Q\] Protect against Front-Running**](index.html#req-3-block-front-running) to [**\[Q\] Protect against Ordering Attacks**](index.html#req-3-block-front-running) to cover a broader class of attacks.
- Update [**\[Q\] Code Linting**](index.html#req-3-linted)
  - to contain the requirements formerly in
    - [**\[M\] No Failing `assert()` Statements**](index.html#req-2-no-failing-asserts), and
    - [**\[S\] No Conflicting Names**](index.html#req-1-inheritance-conflict)
  - and to include a requirement for a `pragma` directive that specifies a range of Solidity Compiler Versions
- Update [**\[Q\] Protect Against Governance Takeovers**](https://entethalliance.org/specs/ethtrust-sl/v3/req-3-protect-governance) and its explanation to clarify the intent of protecting against malicious actors.
- Update [**\[Q\] Document System Architecture**](index.html#req-3-document-system) to explicitly mention variable and data structure sizes, and the related requirement [**\[Q\] Manage Gas Usage**](index.html#req-3-enough-gas)

#### A.4.3 Requirements removed<a href="index.html#sec-change-removed" class="self-link" aria-label="§"></a>

- The requirements
  - **\[S\] No Conflicting Names** and
  - **\[M\] No Failing `assert()` Statements**

  were removed with the functional requirements moved into [**\[Q\] Code Linting**](index.html#req-3-linted).

- **\[M\] Document Name Conflicts**.

- The following requirements that depend on Solidity compiler versions

  - **\[S\] No Overflow/Underflow**
  - **\[S\] Compiler Bug SOL-2020-11-push**
  - **\[S\] Compiler Bug SOL-2020-10**
  - **\[S\] Compiler Bug SOL-2020-9**
  - **\[S\] Compiler Bug SOL-2020-8**
  - **\[S\] Compiler Bug SOL-2020-6**
  - **\[S\] Compiler Bug SOL-2020-7**
  - **\[S\] Compiler Bug SOL-2020-5**
  - **\[S\] Compiler Bug SOL-2020-4**

  were removed, with the functional requirements being covered as necessary via references to Version 2 of the Specification, in [**\[S\] Use a Modern Compiler**](index.html#req-1-compiler-060).

- The requirement **\[M\] Compiler Bug Check Constructor Payment** was removed, with the functional requirement being covered via references to Version 2 of the Specification, in [**\[M\] Use a Modern Compiler**](index.html#req-2-compiler-060).

### A.5 Requirements removed from previous versions<a href="index.html#requirements-removed-from-previous-versions" class="self-link" aria-label="§"></a>

The following requirements, present in Version 1 of this specification, were [removed in Version 2](https://entethalliance.org/specs/ethtrust-sl/v2/#requirements-removed):

- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-explicit-storage" id="req-1-explicit-storage" class="removed"><strong>[S] Explicit Storage</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2020-11-length" id="req-1-compiler-SOL-2020-11-length" class="removed"><strong>[S] Compiler Bug SOL-2020-11-length</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-10" id="req-1-compiler-SOL-2019-10" class="removed"><strong>[S] Compiler Bug SOL-2019-10</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-3679" id="req-1-compiler-SOL-2019-3679" class="removed"><strong>[S] Compiler Bugs SOL-2019-3,6,7,9</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-8" id="req-1-compiler-SOL-2019-8" class="removed"><strong>[S] Compiler Bug SOL-2019-8</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-5" id="req-1-compiler-SOL-2019-5" class="removed"><strong>[S] Compiler Bug SOL-2019-5</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-4" id="req-1-compiler-SOL-2019-4" class="removed"><strong>[S] Compiler Bug SOL-2019-4</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-2" id="req-1-compiler-SOL-2019-2" class="removed"><strong>[S] Compiler Bug SOL-2019-2</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-1" id="req-1-compiler-SOL-2019-1" class="removed"><strong>[S] Compiler Bug SOL-2019-1</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-4" id="req-1-compiler-SOL-2018-4" class="removed"><strong>[S] Compiler Bug SOL-2018-4</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-3" id="req-1-compiler-SOL-2018-3" class="removed"><strong>[S] Compiler Bug SOL-2018-3</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-2" id="req-1-compiler-SOL-2018-2" class="removed"><strong>[S] Compiler Bug SOL-2018-2</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-1" id="req-1-compiler-SOL-2018-1" class="removed"><strong>[S] Compiler Bug SOL-2018-1</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-5" id="req-1-compiler-SOL-2017-5" class="removed"><strong>[S] Compiler Bug SOL-2017-5</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-4" id="req-1-compiler-SOL-2017-4" class="removed"><strong>[S] Compiler Bug SOL-2017-4</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-3" id="req-1-compiler-SOL-2017-3" class="removed"><strong>[S] Compiler Bug SOL-2017-3</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-2" id="req-1-compiler-SOL-2017-2" class="removed"><strong>[S] Compiler Bug SOL-2017-2</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-1" id="req-1-compiler-SOL-2017-1" class="removed"><strong>[S] Compiler Bug SOL-2017-1</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-11" id="req-1-compiler-SOL-2016-11" class="removed"><strong>[S] Compiler Bug SOL-2016-11</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-10" id="req-1-compiler-SOL-2016-10" class="removed"><strong>[S] Compiler Bug SOL-2016-10</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-9" id="req-1-compiler-SOL-2016-9" class="removed"><strong>[S] Compiler Bug SOL-2016-9</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-8" id="req-1-compiler-SOL-2016-8" class="removed"><strong>[S] Compiler Bug SOL-2016-8</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-7" id="req-1-compiler-SOL-2016-7" class="removed"><strong>[S] Compiler Bug SOL-2016-7</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-6" id="req-1-compiler-SOL-2016-6" class="removed"><strong>[S] Compiler Bug SOL-2016-6</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-5" id="req-1-compiler-SOL-2016-5" class="removed"><strong>[S] Compiler Bug SOL-2016-5</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-4" id="req-1-compiler-SOL-2016-4" class="removed"><strong>[S] Compiler Bug SOL-2016-4</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-3" id="req-1-compiler-SOL-2016-3" class="removed"><strong>[S] Compiler Bug SOL-2016-3</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage" id="req-2-explicit-storage" class="removed"><strong>[M] Declare <code>storage</code> Explicitly</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2" id="req-2-compiler-SOL-2020-2" class="removed"><strong>[M] Compiler Bug SOL-2020-2</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly" id="req-2-compiler-SOL-2019-2-assembly" class="removed"><strong>[M] Compiler Bug SOL-2019-2 in <code>assembly {}</code></strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls" id="req-2-compiler-check-identity-calls" class="removed"><strong>[M] Compiler Bug Check Identity Calls</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input" id="req-2-validate-ecrecover-input" class="removed"><strong>[M] Validate <code>ecrecover()</code> input</strong></a>
- <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send" id="req-2-compiler-no-zero-ether-send" class="removed"><strong>[M] Compiler Bug No Zero Ether Send</strong></a>

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

\[ET-tools\]
[EEA EthTrust Tool Implementation Registry](https://github.com/EntEthAlliance/ethtrust-tool-registry/). EEA. URL: <https://github.com/EntEthAlliance/ethtrust-tool-registry/>

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

\[solidity-patterns\]
[Solidity Patterns](https://fravoll.github.io/solidity-patterns/). Franz Volland. URL: <https://fravoll.github.io/solidity-patterns/>

\[solidity-release-818\]
[Solidity 0.8.18 Release Announcement](https://soliditylang.org/blog/2023/02/01/solidity-0.8.18-release-announcement/). Ethereum Foundation. 2023-02-01. URL: <https://soliditylang.org/blog/2023/02/01/solidity-0.8.18-release-announcement/>

\[solidity-security\]
[Security Considerations - Solidity Documentation.](https://docs.soliditylang.org/en/latest/security-considerations.html). Ethereum Foundation. URL: <https://docs.soliditylang.org/en/latest/security-considerations.html>

\[Solidity-Style-Guide\]
[Solidity Style Guide - Solidity Documentation](https://docs.soliditylang.org/en/latest/style-guide.html). URL: <https://docs.soliditylang.org/en/latest/style-guide.html>

\[solidity-underhanded-richards2022\]
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

\[certik-rari\]
[Fei Protocol Incident Analysis](https://certik.medium.com/fei-protocol-incident-analysis-8527440696cc). CertiK. URL: <https://certik.medium.com/fei-protocol-incident-analysis-8527440696cc>

\[chase\]
[Malleable Signatures: New Definitions and Delegatable Anonymous Credentials](https://smeiklej.com/files/csf14.pdf). Melissa Chase; Markulf Kohlweiss; Anna Lysyanskaya; Sarah Meiklejohn. URL: <https://smeiklej.com/files/csf14.pdf>

\[EEA-L2\]
[Introduction to Ethereum Layer 2](https://entethalliance.org/eea-primers/entry/5696/). Enterprise Ethereum Alliance, Inc. URL: <https://entethalliance.org/eea-primers/entry/5696/>

\[EF-MEV\]
[Maximal Extractable Value (MEV)](https://ethereum.org/en/developers/docs/mev/). Ethereum Foundation. URL: <https://ethereum.org/en/developers/docs/mev/>

\[EIP-3529\]
[Reduction in Refunds](https://eips.ethereum.org/EIPS/eip-3529). Ethereum Foundation. URL: <https://eips.ethereum.org/EIPS/eip-3529>

\[futureblock\]
[Future-block MEV in Proof of Stake](https://archive.devcon.org/archive/watch/6/future-block-mev-in-proof-of-stake/?tab=YouTube). Ethereum Foundation. URL: <https://archive.devcon.org/archive/watch/6/future-block-mev-in-proof-of-stake/?tab=YouTube>

\[License\]
[Apache license version 2.0](http://www.apache.org/licenses/LICENSE-2.0). The Apache Software Foundation. URL: <http://www.apache.org/licenses/LICENSE-2.0>

\[postmerge-mev\]
[Why is Oracle Manipulation after the Merge so cheap? Multi-Block MEV](https://chainsecurity.com/oracle-manipulation-after-merge/). ChainSecurity. URL: <https://chainsecurity.com/oracle-manipulation-after-merge/>

\[solidity-reports\]
[Reporting a Vulnerability, in Security Policy](https://github.com/ethereum/solidity/security/policy#reporting-a-vulnerability). Ethereum Foundation. URL: <https://github.com/ethereum/solidity/security/policy#reporting-a-vulnerability>

\[WSE\]
[Symbolic Execution](https://en.wikipedia.org/wiki/Symbolic_execution). WikiPedia. URL: <https://en.wikipedia.org/wiki/Symbolic_execution>

[↑](index.html#title)
