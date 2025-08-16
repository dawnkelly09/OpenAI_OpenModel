<a href="checklist.html" class="logo"><img src="https://entethalliance.org/wp-content/uploads/2024/10/EEALogo360x140.png" id="eea-logo" width="240" height="97" alt="EEA" /></a>

# Checklist for EEA EthTrust Security Levels version 3

## EEA Publication @@ March 2025

This version
[https://entethalliance.org/specs/ethtrust-sl/v3/checklist.html](checklist.html)

Latest editor's draft:
<https://entethalliance.github.io/eta-registry/checklist.html>

Copyright © 2023 - 2025 [Enterprise Ethereum Alliance](https://entethalliance.org/).

------------------------------------------------------------------------

## Status of This Documen

*This section describes the status of this document at the time of its publication. Newer documents may supersede this document.*

This document is licensed by the Enterprise Ethereum Alliance, Inc. (EEA) under the terms of the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) \[<a href="checklist.html#bib-license" class="bibref" data-link-type="biblio" title="Apache license version 2.0">License</a>\]. Unless otherwise explicitly authorised in writing by the EEA, you can only use this document in accordance with those terms.

Unless required by applicable law or agreed to in writing, this document is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

This checklist is a companion document for the [EEA EthTrust Security Levels Specification, version 3](index.html), provided as a convenience. In case of any discrepancy between this document and the [published Specification](index.html), the text in the [Specification](index.html) is the authorative version. The content of this document has been reviewed by the EEA Board and approved for publication.

The Working Group *expects* at time of publication to maintain this checklist alongside the Editor's draft for the next version of the Specification.

Please send any comments to the editor at [Editor EEA](https://entethalliance.org/cdn-cgi/l/email-protection#b3d6d7dac7dcc1f3d6ddc7d6c7dbd2dfdfdad2ddd0d69ddcc1d4), or as issues via the [EthTrust-public GitHub repository](https://github.com/EntEthAlliance/EthTrust-pibluc/issues/)

.

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

This companion document is the Editors' Draft of a checklist for \[<a href="checklist.html#bib-ethtrust-sl-v1" class="bibref" data-link-type="biblio" title="EEA EthTrust Security Levels Specification. Version 1">EthTrust-sl-v1</a>\], the EEA EthTrust Security Levels Specification. It lists the requirements for granting <a href="checklist.html#dfn-eea-ethtrust-certification" class="externalDFN" data-link-type="dfn">EEA EthTrust Certification</a> to a smart contract written in Solidity as a convenience for security reviewers, developers, or others, who are familiar with the EEA EthTrust Security Levels Specification, and want an *aide memoire*.

In case of any discrepancy between this checklist, and the relevant version of the EEA EthTrust Security Levels Specification, readers can assume that this document is in error, and the definitive version is the text in the specification.

<a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> is a claim by a security reviewer that the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> is not vulnerable to a number of known attacks or failures to operate as expected, based on the reviewer's assessment against those specific requirements.

<a href="checklist.html#dfn-eea-ethtrust-certification" class="externalDFN" data-link-type="dfn">EEA EthTrust Certification</a> **does not and cannot** ensure that the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> is completely secure from any attack.

#### 1.1.2 Typographic Conventions<a href="checklist.html#sec-typographic-conventions" class="self-link" aria-label="§"></a>

Definitions of terms are formatted Like this. Most of the terms are defined in the main specification document. Some definitions are repeated in this document. References to defined terms are rendered as links <a href="index.html#dfn-like-this" class="externalDFN" data-link-type="dfn">Like This</a>.

References to other documents are links to the relevant entry in the <a href="checklist.html#references" class="sec-ref">§ B. References</a> section, within square brackets, such as: \[<a href="checklist.html#bib-cwe" class="bibref" data-link-type="biblio" title="Common Weakness Enumeration">CWE</a>\].

Links to requirements begin with a <a href="index.html#dfn-security-levels" class="externalDFN" data-link-type="dfn">Security Level</a>: **\[S\]**, **\[M\]** or **\[Q\]**, and recommended good practices begin with **\[GP\]**. They then include the requirement or good practice name. They are rendered as links in bold type, for example:

Example of a link to [**\[M\] Document Special Code Use**](checklist.html#req-2-documented).

Variables, introduced to be described further on in a statement or requirement, are formatted as `var`.

## 2. Conformance<a href="checklist.html#conformance" class="self-link" aria-label="§"></a>

The key words *MAY*, *MUST*, *MUST NOT*, *RECOMMENDED*, and *SHOULD* in this document are to be interpreted as described in [BCP 14](https://tools.ietf.org/html/bcp14) \[<a href="checklist.html#bib-rfc2119" class="bibref" data-link-type="biblio" title="Key words for use in RFCs to Indicate Requirement Levels">RFC2119</a>\] \[<a href="checklist.html#bib-rfc8174" class="bibref" data-link-type="biblio" title="Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words">RFC8174</a>\] when, and only when, they appear in all capitals, as shown here.

### 2.1 Conformance Claims<a href="checklist.html#sec-conformance-claims" class="self-link" aria-label="§"></a>

To grant <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> EEA EthTrust Certification, an auditor provides a <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>, that the <a href="checklist.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> meets the requirements of the <a href="index.html#dfn-security-levels" class="externalDFN" data-link-type="dfn">Security Level</a> for which it is certified.

A Valid Conformance Claim *MUST* include:

- The date on which the certification was issued, in 'YYYY-MM-DD' format.
- The <a href="index.html#dfn-evm-version" class="externalDFN" data-link-type="dfn">EVM version(s)</a> (of those listed at \[<a href="checklist.html#bib-evm-version" class="bibref" data-link-type="biblio" title="Using the Compiler - Solidity Documentation. (§Targets)">EVM-version</a>\]) for which the certification is valid.
- The version of the EEA EthTrust Security Levels specification for which the contract is certified.
- A name and a URL for the organisation or software issuing the certification.
- The <a href="index.html#dfn-security-levels" class="externalDFN" data-link-type="dfn">Security Level</a> ("**\[S\]**", "**\[M\]**", or "**\[Q\]**") that the <a href="checklist.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> claims.
- A list of the requirements which were tested and a statement for each one, noting whether the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> meets the requirement. This *MAY* include further information.
- An explicit notice stating that <a href="checklist.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> does not provide any warranty or formal guarantee
  - of the overall security of the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>, nor
  - that the project is free from bugs or vulnerabilities. This notice *SHOULD* state that <a href="checklist.html#dfn-eea-ethtrust-certified" class="internalDFN" data-link-type="dfn">EEA EthTrust Certification</a> represents the best efforts of the issuer to detect and identify certain known vulnerabilities that can affect Smart Contracts.
- For conformance claims where certification is granted because the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> met an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> or a <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>, the conformance claim *MUST* include the results for the <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement(s)</a> met, and *MAY* omit the results for the requirement(s) whose results were thus unnecessary to determine conformance.

The following items *MUST* be part of a <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a>. A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* make them available as a link to the relevant documentation, in which case the Conformance Claim *MUST* also include a \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of all documents linked for this purpose:

- The compiler options applied for each compilation.
- The contract metadata generated by the compiler.

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> for <a href="index.html#dfn-security-level-q" class="externalDFN" data-link-type="dfn">Security Level [Q]</a> *MUST* include:

- a \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the documentation provided to meet [**\[Q\] Document Contract Logic**](index.html#req-3-documented), [, and](index.html#req-3-document-threats) [**\[Q\] Document System Architecture**](index.html#req-3-document-system), and
- A bounded range of Solidity Compiler Versions for which the certification is valid. Note that this range *MAY* differ from the range declared in `pragama` directives present in the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>.

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *SHOULD* include:

- A contact address for feedback such as questions about or challenges to the certification.
- Descriptions of conformance to the good practices described in <a href="checklist.html#sec-good-practice-recommendations" class="sec-ref">§ 5.4 Recommended Good Practices</a>.

A <a href="checklist.html#dfn-valid-conformance-claim" class="internalDFN" data-link-type="dfn">Valid Conformance Claim</a> *MAY* include:

- An address where a \[<a href="checklist.html#bib-sha3-256" class="bibref" data-link-type="biblio" title="FIPS 202 - SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions">SHA3-256</a>\] hash of the conformance claim has been recorded on an identified network, e.g. Ethereum Mainnet.
- An address of the contract deployed on an identified network, e.g. Ethereum Mainnet.

### 2.2 Security Level Requirements<a href="checklist.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Requirement</th>
<th>Status</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="index.html#req-1-eip155-chainid"><strong>[S] Encode Hashes with <code>chainid</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> create hashes for transactions that incorporate <code>chainid</code> values following the recommendation described in [<a href="checklist.html#bib-eip-155" class="bibref" data-link-type="biblio" title="Simple Replay Attack Protection">EIP-155</a>]</td>
<td>Not Tested Passes Not Applicable (Passes) Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-no-create2"><strong>[S] No <code>CREATE2</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain a <code>CREATE2</code> instruction.<br />
<strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>
<ul>
<li><a href="checklist.html#summ-req-2-protect-create2"><strong>[M] Protect <code>CREATE2</code> Calls</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-2-documented"><strong>[M] Document Special Code Use</strong></a>,</li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-no-tx.origin"><strong>[S] No <code>tx.origin</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain a <code>tx.origin</code> instruction<br />
<strong>unless</strong> it meets the <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> <a href="checklist.html#summ-req-3-verify-tx.origin"><strong>[Q] Verify <code>tx.origin</code> Usage</strong></a></p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-exact-balance-check"><strong>[S] No Exact Balance Check<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> test that the balance of an account is exactly equal to (i.e. <code>==</code>) a specified amount or the value of a variable<br />
<strong>unless</strong> it meets the Overriding Requirement <a href="checklist.html#req-2-verify-exact-balance-check"><strong>[M] Verify Exact Balance Checks</strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-no-hashing-consecutive-variable-length-args"><strong>[S] No Hashing Consecutive Variable Length Arguments<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> use <code>abi.encodePacked()</code> with consecutive variable length arguments.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-self-destruct"><strong>[S] No <code>selfdestruct()</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain the <code>selfdestruct()</code> instruction or its now-deprecated alias <code>suicide()</code><br />
<strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>
<ul>
<li><a href="checklist.html#summ-req-2-self-destruct"><strong>[M] Protect Self-destruction</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-2-documented"><strong>[M] Document Special Code Use</strong></a>.</li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-no-assembly"><strong>[S] No <code>assembly {}</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> contain the <code>assembly {}</code> instruction<br />
<strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>
<ul>
<li><a href="checklist.html#req-2-safe-assembly"><strong>[M] Avoid Common <code>assembly {}</code> Attack Vectors</strong></a>,</li>
<li><a href="checklist.html#req-2-documented"><strong>[M] Document Special Code Use</strong></a>,</li>
<li><a href="checklist.html#req-2-compiler-SOL-2022-5-assembly"><strong>[M] Compiler Bug SOL-2022-5 in <code>assembly {}</code></strong></a>,</li>
<li><a href="checklist.html#req-2-compiler-SOL-2022-7"><strong>[M] Compiler Bug SOL-2022-7</strong></a>,</li>
<li><a href="checklist.html#req-2-compiler-SOL-2022-4"><strong>[M] Compiler Bug SOL-2022-4</strong></a>,</li>
<li><a href="checklist.html#req-2-compiler-SOL-2021-3"><strong>[M] Compiler Bug SOL-2021-3</strong></a>, <strong>and</strong></li>
<li>if using Solidity compiler version 0.5.5 or 0.5.6, <a href="https://entethalliance.org/specs/ethtrust-sl/v1#req-2-compiler-SOL-2019-2-assembly"><strong>[M] Compiler Bug SOL-2019-2 in `assembly {}`</strong></a> in <a href="https://entethalliance.org/specs/ethtrust-sl/v1/">EEA EthTrust Security Levels Specification Version 1</a>.</li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-unicode-bdo"><strong>[S] No Unicode Direction Control Characters<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain any of the <a href="index.html#dfn-unicode-direction-control-characters">Unicode Direction Control Characters</a> <code>U+2066</code>, <code>U+2067</code>, <code>U+2068</code>, <code>U+2029</code>, <code>U+202A</code>, <code>U+202B</code>, <code>U+202C</code>, <code>U+202D</code>, or <code>U+202E</code><br />
<strong>unless</strong> it meets the <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> <a href="checklist.html#summ-req-2-unicode-bdo"><strong>[M] No Unnecessary Unicode Controls</strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-check-return"><strong>[S] Check External Calls Return<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that makes external calls using the <a href="index.html#dfn-low-level-call-functions" class="externalDFN" data-link-type="dfn">Low-level Call Functions</a> (i.e. <code>call()</code>, <code>delegatecall()</code>, <code>staticcall()</code>, and <code>send()</code>) <em>MUST</em> check the returned value from each usage to determine whether the call failed,<br />
<strong>unless</strong> it meets the Overriding Requirement <a href="checklist.html#summ-req-2-handle-return"><strong>[M] Handle External Call Returns</strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-use-c-e-i"><strong>[S] Use Check-Effects-Interaction<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that makes external calls <em>MUST</em> use the <a href="index.html#dfn-checks-effects-interactions" class="externalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern to protect against <a href="index.html#dfn-re-entrancy-attacks" class="externalDFN" data-link-type="dfn">Re-entrancy Attacks</a><br />
<strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>
<ul>
<li><a href="checklist.html#summ-req-2-external-calls"><strong>[M] Protect External Calls</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-2-documented"><strong>[M] Document Special Code Use</strong></a></li>
</ul>
<p><strong>or</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a></p>
<ul>
<li><a href="checklist.html#summ-req-3-external-calls"><strong>[Q] Verify External Calls</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-documented"><strong>[Q] Document Contract Logic</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-document-system"><strong>[Q] Document System Architecture</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-3-implement-as-documented"><strong>[Q] Implement as Documented</strong></a>.</li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-delegatecall"><strong>[S] No <code>delegatecall()</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> contain the <code>delegatecall()</code> instruction<br />
<strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:</p>
<ul>
<li><a href="checklist.html#summ-req-2-external-calls"><strong>[M] Protect External Calls</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-2-documented"><strong>[M] Document Special Code Use</strong></a>.</li>
</ul>
<p><strong>or</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a>:</p>
<ul>
<li><a href="checklist.html#summ-req-3-external-calls"><strong>[Q] Verify External Calls</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-documented"><strong>[Q] Document Contract Logic</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-document-system"><strong>[Q] Document System Architecture</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-3-implement-as-documented"><strong>[Q] Implement as Documented</strong></a>.</li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-compiler-SOL-2023-3"><strong>[S] Compiler Bug SOL-2023-3<span class="selflink"></span></strong><br />
</a>Tested code that includes Yul code and uses the <code>verbatim</code> instruction twice, in each case surrounded by identical code, MUST disable the Block Deduplicator when using a Solidity compiler version between 0.8.5 and 0.8.22 (inclusive).</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-compiler-SOL-2022-6"><strong>[S] Compiler Bug SOL-2022-6<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that ABI-encodes a tuple (including a <code>struct</code>, <code>return</code> value, or paramater list) with the ABIEncoderV2, that includes a dynamic component and whose last element is a <code>calldata</code> static array of base type <code>uint</code> or <code>bytes32</code> <em>MUST NOT</em> use a Solidity compiler version between 0.5.8 and 0.8.15 (inclusive).</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-SOL-2022-5-push"><strong>[S] Compiler Bug SOL-2022-5 with <code>.push()</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> tha
<ul>
<li>copies <code>bytes</code> arrays from <code>calldata</code> or <code>memory</code> whose size is not a multiple of 32 bytes, <strong>and</strong></li>
<li>has an empty <code>.push()</code> instruction that writes to the resulting array,</li>
</ul>
<p><em>MUST NOT</em> use a Solidity compiler version older than 0.8.15.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-SOL-2022-3"><strong>[S] Compiler Bug SOL-2022-3<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> tha
<ul>
<li>uses <code>memory</code> and <code>calldata</code> pointers for the same function, <strong>and</strong></li>
<li>changes the data location of a function during inheritance, <strong>and</strong></li>
<li>performs an internal call at a location that is only aware of the original function signature from the base contract</li>
</ul>
<p><em>MUST NOT</em> use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-SOL-2022-2"><strong>[S] Compiler Bug SOL-2022-2<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> with a nested array tha
<ul>
<li>passes it to an external function, <strong>or</strong></li>
<li>passes it as input to <code>abi.encode()</code>, <strong>or</strong></li>
<li>uses it in an event</li>
</ul>
<p><em>MUST NOT</em> use a Solidity compiler version between 0.6.9 and 0.8.12 (inclusive).</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-SOL-2022-1"><strong>[S] Compiler Bug SOL-2022-1<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> tha
<ul>
<li>uses Number literals for a <a href="index.html#dfn-bytesnn" class="externalDFN" data-link-type="dfn"><code>bytesNN</code></a> type shorter than 32 bytes, <strong>or</strong></li>
<li>uses String literals for any <a href="index.html#dfn-bytesnn" class="externalDFN" data-link-type="dfn"><code>bytesNN</code></a> type,</li>
</ul>
<p><strong>and</strong> passes such literals to <code>abi.encodeCall()</code> as the first parameter, <em>MUST NOT</em> use Solidity compiler version 0.8.11 nor 0.8.12.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-compiler-sol-2021-4"><strong>[S] Compiler Bug SOL-2021-4<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that uses custom value types shorter than 32 bytes <em>MUST NOT</em> use Solidity compiler version 0.8.8.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-compiler-SOL-2021-2"><strong>[S] Compiler Bug SOL-2021-2<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that uses <code>abi.decode()</code> on byte arrays as <code>memory</code> <em>MUST NOT</em> use the ABIEncoderV2 with a Solidity compiler version between 0.4.16 and 0.8.3 (inclusive).</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-SOL-2021-1"><strong>[S] Compiler Bug SOL-2021-1<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that has 2 or more occurrences of an instruction <code>keccak(</code><var>mem</var><code>,</code><var>length</var><code>)</code> where
<ul>
<li>the values of <var>mem</var> are equal, <strong>and</strong></li>
<li>the values of <var>length</var> are unequal, <strong>and</strong></li>
<li>the values of <var>length</var> are not multiples of 32,</li>
</ul>
<p><em>MUST NOT</em> use the Optimizer with a Solidity compiler version older than 0.8.3.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-1-compiler-060"><strong>[S] Use a Modern Compiler<span class="selflink"></span></strong><br />
</a>
<p><strong>[S] Use a Modern Compiler</strong><br />
<a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use a Solidity compiler version older than 0.8.0, <strong>unless</strong> it meets all the following requirements from the <a href="https://entethalliance.org/specs/ethtrust-sl/v2/">EEA EthTrust Security Levels Specification Version 2</a>, as <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirements</a>:</p>
<ul>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-overflow-underflow"><strong>[S] No Overflow/Underflow</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-11-push"><strong>[S] Compiler Bug SOL-2020-11-push</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-10"><strong>[S] Compiler Bug SOL-2020-10</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-9"><strong>[S] Compiler Bug SOL-2020-9</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-8"><strong>[S] Compiler Bug SOL-2020-8</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-6"><strong>[S] Compiler Bug SOL-2020-6</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-7"><strong>[S] Compiler Bug SOL-2020-7</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-5"><strong>[S] Compiler Bug SOL-2020-5</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-1-compiler-SOL-2020-4"><strong>[S] Compiler Bug SOL-2020-4</strong></a></li>
</ul>
<p><strong>AND</strong></p>
<p><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use a Solidity compiler version older than 0.6.0, <strong>unless</strong> it meets all the following requirements from the <a href="https://entethalliance.org/specs/ethtrust-sl/v1/">EEA EthTrust Security Levels Specification Version 1</a>, as <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirements</a>:</p>
<ul>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2020-11-length"><strong>[S] Compiler Bug SOL-2020-11-length</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-10"><strong>[S] Compiler Bug SOL-2019-10</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-3679"><strong>[S] Compiler Bugs SOL-2019-3,6,7,9</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-8"><strong>[S] Compiler Bug SOL-2019-8</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-5"><strong>[S] Compiler Bug SOL-2019-5</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-4"><strong>[S] Compiler Bug SOL-2019-4</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-2"><strong>[S] Compiler Bug SOL-2019-2</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2019-1"><strong>[S] Compiler Bug SOL-2019-1</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-explicit-storage"><strong>[S] Explicit Storage</strong></a> (including through its overriding requirement <a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage"><strong>[M] Declare <code>storage</code> Explicitly</strong></a> if appropriate)</li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-4"><strong>[S] Compiler Bug SOL-2018-4</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-3"><strong>[S] Compiler Bug SOL-2018-3</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-2"><strong>[S] Compiler Bug SOL-2018-2</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2018-1"><strong>[S] Compiler Bug SOL-2018-1</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-5"><strong>[S] Compiler Bug SOL-2017-5</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-4"><strong>[S] Compiler Bug SOL-2017-4</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-3"><strong>[S] Compiler Bug SOL-2017-3</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-2"><strong>[S] Compiler Bug SOL-2017-2</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2017-1"><strong>[S] Compiler Bug SOL-2017-1</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-11"><strong>[S] Compiler Bug SOL-2016-11</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-10"><strong>[S] Compiler Bug SOL-2016-10</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-9"><strong>[S] Compiler Bug SOL-2016-9</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-8"><strong>[S] Compiler Bug SOL-2016-8</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-7"><strong>[S] Compiler Bug SOL-2016-7</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-6"><strong>[S] Compiler Bug SOL-2016-6</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-5"><strong>[S] Compiler Bug SOL-2016-5</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-4"><strong>[S] Compiler Bug SOL-2016-4</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-1-compiler-SOL-2016-3"><strong>[S] Compiler Bug SOL-2016-3</strong></a></li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-1-no-ancient-compilers"><strong>[S] No Ancient Compilers<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use a Solidity compiler version older than 0.3.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-pass-l1"><strong>[M] Pass Security Level [S]<span class="selflink"></span></strong><br />
To be eligible for</a> <a href="checklist.html#dfn-eea-ethtrust-certification" class="internalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-m" class="externalDFN" data-link-type="dfn">Security Level [M]</a>, <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> meet the requirements for <a href="index.html#dfn-security-level-s" class="externalDFN" data-link-type="dfn">Security Level [S]</a>.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-enforce-eval-order"><strong>[M] Explicitly Disambiguate Evaluation Order<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain statements where variable evaluation order can result in different outcomes</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-verify-exact-balance-check"><strong>[M] Verify Exact Balance Checks<span class="selflink"></span></strong><br />
</a>Tested code that checks whether the balance of an account is exactly equal to (i.e. <code>==</code>) a specified amount or the value of a variable MUST protect itself against transfers affecting the balance tested.<br />
This is an Overriding Requirement for <a href="checklist.html#req-1-exact-balance-check"><strong>[S] No Exact Balance Check</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-unicode-bdo"><strong>[M] No Unnecessary Unicode Controls<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use <a href="index.html#dfn-unicode-direction-control-characters" class="externalDFN" data-link-type="dfn">Unicode direction control characters</a> <strong>unless</strong> they are necessary to render text appropriately, and the resulting text does not mislead readers.<br />
This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-1-unicode-bdo"><strong>[S] No Unicode Direction Control Characters</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-no-homoglyph-attack"><strong>[M] No Homoglyph-style Attack<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> not use homoglyphs, Unicode control characters, combining characters, or characters from multiple Unicode blocks if the impact is misleading.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-external-calls"><strong>[M] Protect External Calls<span class="selflink"></span></strong><br />
For</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that makes external calls:
<ul>
<li>all addresses called by the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a>, <em>MUST</em> correspond to the exact code of the contracts tested <strong>and</strong></li>
<li>all contracts called <em>MUST</em> be within the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a>, <strong>and</strong></li>
<li>all contracts called <em>MUST</em> be controlled by the same entity, <strong>and</strong></li>
<li>the protection against <a href="index.html#dfn-re-entrancy-attacks" class="externalDFN" data-link-type="dfn">Re-entrancy Attacks</a> for the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> be equivalent to what the <a href="index.html#dfn-checks-effects-interactions" class="externalDFN" data-link-type="dfn">Checks-Effects-Interactions</a> pattern offers,</li>
</ul>
<p><strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a></p>
<ul>
<li><a href="checklist.html#summ-req-3-external-calls"><strong>[Q] Verify External Calls</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-documented"><strong>[Q] Document Contract Logic</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-document-system"><strong>[Q] Document System Architecture</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-3-implement-as-documented"><strong>[Q] Implement as Documented</strong></a>.</li>
</ul>
<p>This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-1-use-c-e-i"><strong>[S] Use Check-Effects-Interaction</strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-avoid-readonly-reentrancy"><strong>[M] Avoid Read-only Re-entrancy Attacks<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that makes external calls <em>MUST</em> protect itself against <a href="index.html#dfn-read-only-re-entrancy-attack" class="externalDFN" data-link-type="dfn">Read-only Re-entrancy Attacks</a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-handle-return"><strong>[M] Handle External Call Returns<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that makes external calls <em>MUST</em> reasonably handle possible errors.<br />
This is an Overriding Requirement for <a href="checklist.html#summ-req-1-check-return"><strong>[S] Check External Calls Return</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-documented"><strong>[M] Document Special Code Use<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> document the need for each instance of:
<ul>
<li><code>CREATE2</code>,</li>
<li><code>assembly {}</code>,</li>
<li><code>selfdestruct()</code> or its deprecated alias <code>suicide()</code>,</li>
<li>external calls,</li>
<li><code>delegatecall()</code>,</li>
<li>code that can cause an overflow or underflow,</li>
</ul>
use of <code>block.number</code> or <code>block.timestamp</code>, <strong>or</strong>
use of oracles and pseudo-randomness,
<p><strong>and</strong> <em>MUST</em> describe how the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> protects against misuse or errors in these cases, <strong>and</strong> the documentation <em>MUST</em> be available to anyone who can call the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>.</p>
<p>This is part of several <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Sets of Overriding Requirements</a>, one for each of</p>
<ul>
<li><a href="checklist.html#summ-req-1-no-create2"><strong>[S] No <code>CREATE2</code></strong></a>,</li>
<li><a href="checklist.html#summ-req-1-self-destruct"><strong>[S] No <code>selfdestruct()</code></strong></a>,</li>
<li><a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>,</li>
<li><a href="checklist.html#summ-req-1-use-c-e-i"><strong>[S] Use Check-Effects-Interaction</strong></a>, and</li>
<li><a href="checklist.html#summ-req-1-no-delegatecall"><strong>[S] No <code>delegatecall()</code></strong></a>.</li>
</ul></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-check-rounding"><strong>[M] Ensure Proper Rounding of Computations Affecting Value<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> identify and protect against exploiting rounding errors:
<ul>
<li>The possible range of error introduced by such rounding <em>MUST</em> be documented.</li>
<li><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> unintentionally create or lose value through rounding.</li>
<li><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> apply rounding in a way that does not allow round-trips "creating" value to repeat causing unexpectedly large transfers.</li>
</ul></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-self-destruct"><strong>[M] Protect Self-destruction<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that contains the <code>selfdestruct()</code> or <code>suicide()</code> instructions <em>MUST</em>
<ul>
<li>ensure that only authorised parties can call the method, <strong>and</strong></li>
<li><em>MUST</em> protect those calls in a way that is fully compatible with the claims of the contract author,</li>
</ul>
<p><strong>unless</strong> it meets the <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a><a href="checklist.html#req-3-access-control"><strong>[Q] Enforce Least Privilege</strong></a></p>
<p>This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-1-self-destruct"><strong>[S] No <code>selfdestruct()</code></strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-safe-assembly"><strong>[M] Avoid Common <code>assembly {}</code> Attack Vectors<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> use the <code>assembly {}</code> instruction to change a variable <strong>unless</strong> the code cannot:
<ul>
<li>create storage pointer collisions, <strong>nor</strong></li>
<li>allow arbitrary values to be assigned to variables of type <code>function</code>.</li>
</ul>
<p>This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-protect-create2"><strong>[M] Protect <code>CREATE2</code> Calls<span class="selflink"></span></strong><br />
For</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that uses the <code>CREATE2</code> instruction, any contract to be deployed using <code>CREATE2</code>
<ul>
<li><em>MUST</em> be within the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>, <strong>and</strong></li>
<li><em>MUST NOT</em> use any <code>selfdestruct()</code>, <code>delegatecall()</code> nor <code>callcode()</code> instructions, <strong>and</strong></li>
<li><em>MUST</em> be fully compatible with the claims of the contract author,</li>
</ul>
<p><strong>unless</strong> it meets the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a></p>
<ul>
<li><a href="checklist.html#summ-req-3-external-calls"><strong>[Q] Verify External Calls</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-documented"><strong>[Q] Document Contract Logic</strong></a>,</li>
<li><a href="checklist.html#summ-req-3-document-system"><strong>[Q] Document System Architecture</strong></a>, <strong>and</strong></li>
<li><a href="checklist.html#summ-req-3-implement-as-documented"><strong>[Q] Implement as Documented</strong></a>.</li>
</ul>
<p>This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-create2"><strong>[S] No <code>CREATE2</code></strong></a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirements Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-overflow-underflow"><strong>[M] Safe Overflow/Underflow<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> contain calculations that can overflow or underflow <strong>unless</strong>
<ul>
<li>there is a demonstrated need (e.g. for use in a modulo operation) and</li>
<li>there are guards around any calculations, if necessary, to ensure behavior consistent with the claims of the contract author.</li>
</ul></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-random-enough"><strong>[M] Sources of Randomness<span class="selflink"></span></strong><br />
Sources of randomness used in</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> be sufficiently resistant to prediction that their purpose is met.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-block-data-misuse"><strong>[M] Don't Misuse Block Data<span class="selflink"></span></strong><br />
Block numbers and timestamps used in</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> introduce vulnerabilities to <a href="index.html#dfn-mev" class="externalDFN" data-link-type="dfn">MEV</a> or similar attacks.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-signature-verification"><strong>[M] Proper Signature Verification<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> use proper signature verification to ensure authenticity of messages that were signed off-chain.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-malleable-signatures-for-replay"><strong>[M] No Improper Usage of Signatures for Replay Attack Protection<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> using signatures to prevent replay attacks <em>MUST</em> ensure that signatures cannot be reused:
<ul>
<li>In the same function to verify the same message, <strong>nor</strong></li>
<li>In more than one function to verify the same message within the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>, <strong>nor</strong></li>
<li>In more than one contract address to verify the same message, in which the same account(s) may be signing messages, <strong>nor</strong></li>
<li>In the same contract address across multiple chains,</li>
</ul>
<p><strong>unless</strong> it meets the <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> <a href="checklist.html#summ-req-3-intended-replay"><strong>[Q] Intended Replay</strong></a>. Additionally, <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> verify that multiple signatures cannot be created for the same message, as is the case with <a href="index.html#dfn-malleable-signatures" class="externalDFN" data-link-type="dfn">Malleable Signatures</a>.</p></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-compiler-SOL-2023-1"><strong>[M] Solidity Compiler Bug 2023-1<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that contains a compound expression with side effects that uses <code>.selector</code> <em>MUST</em> use the viaIR option with Solidity compiler versions between 0.6.2 and 0.8.20 inclusive.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-compiler-SOL-2022-7"><strong>[M] Compiler Bug SOL-2022-7<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that has storage writes followed by conditional early terminations from inline assembly functions containing <code>return()</code> or <code>stop()</code> instructions, <em>MUST NOT</em> not use a Solidity compiler version between 0.8.13 and 0.8.16 inclusive.<br />
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-compiler-SOL-2022-5-assembly"><strong>[M] Compiler Bug SOL-2022-5 in <code>assembly {}</code><span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that</p>
<ul>
<li>copies <code>bytes</code> arrays from calldata or memory whose size is not a multiple of 32 bytes, <strong>and</strong></li>
<li>has an <code>assembly {}</code> instruction that reads that data without explicitly matching the length that was copied,</li>
</ul>
<p><em>MUST NOT</em> use a Solidity compiler version older than 0.8.15.<br />
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-compiler-SOL-2022-4"><strong>[M] Compiler Bug SOL-2022-4<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that</p>
<ul>
<li>has at least two <code>assembly {}</code> instructions, such that one writes to memory e.g. by storing a value in a variable, but does not access that memory again, <strong>and</strong></li>
<li>code in a another <code>assembly {}</code> instruction refers to that memory,</li>
</ul>
<p><em>MUST NOT</em> use the yulOptimizer with Solidity compiler versions 0.8.13 or 0.8.14.<br />
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-2-compiler-SOL-2021-3"><strong>[M] Compiler Bug SOL-2021-3<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that reads an <code>immutable</code> signed integer of a <code>type</code> shorter than 256 bits within an <code>assembly {}</code> instruction <em>MUST NOT</em> use a Solidity compiler version between 0.6.5 and 0.8.8 (inclusive).<br />
This is part of the <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-no-assembly"><strong>[S] No <code>assembly {}</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-compiler-check-payable-constructor"><strong>[M] Compiler Bug Check Constructor Payment<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that allows payment to a constructor function that is
<ul>
<li>defined in a base contract, <strong>and</strong></li>
<li>used by default in another contract without an explicit constructor, <strong>and</strong></li>
<li>not explicity marked <code>payable</code>,</li>
</ul>
<p><em>MUST NOT</em> use a Solidity compiler version between 0.4.5 and 0.6.7 (inclusive).<br />
This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-1-compiler-SOL-2020-5"><strong>[S] Compiler Bug SOL-2020-5</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-2-compiler-060"><strong>[M] Use a Modern Compiler<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use a Solidity compiler version older than 0.8.0, <strong>unless</strong> it meets the requirement <a href="https://entethalliance.org/specs/ethtrust-sl/v2/#req-2-compiler-check-payable-constructor"><strong>[M] Compiler Bug Check Constructor Payment</strong></a> from the <a href="https://entethalliance.org/specs/ethtrust-sl/v2/">EEA EthTrust Security Levels Specification Version 2</a>, as an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a>,
<p><strong>AND</strong></p>
<p><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> use a Solidity compiler version older than 0.6.0, <strong>unless</strong> it meets all the following requirements from the <a href="https://entethalliance.org/specs/ethtrust-sl/v1/">EEA EthTrust Security Levels Specification Version 1</a>, as <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirements</a>:</p>
<ul>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2020-2"><strong>[M] Compiler Bug SOL-2020-2</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-SOL-2019-2-assembly"><strong>[M] Compiler Bug SOL-2019-2 in <code>assembly {}</code></strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-check-identity-calls"><strong>[M] Compiler Bug Check Identity Calls</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-validate-ecrecover-input"><strong>[M] Validate <code>ecrecover()</code> input</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-compiler-no-zero-ether-send"><strong>[M] Compiler Bug No Zero Ether Send</strong></a></li>
<li><a href="https://entethalliance.org/specs/ethtrust-sl/v1/#req-2-explicit-storage"><strong>[M] Declare <code>storage</code> Explicitly</strong></a></li>
</ul></td>
<td>Not Tested Passes Passes Overriding Requirement Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-pass-l2"><strong>[Q] Pass Security Level [M]<span class="selflink"></span></strong><br />
To be eligible for</a> <a href="checklist.html#dfn-eea-ethtrust-certification" class="externalDFN" data-link-type="dfn">EEA EthTrust certification</a> at <a href="index.html#dfn-security-level-q" class="externalDFN" data-link-type="dfn">Security Level [Q]</a>, <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> meet the requirements for <a href="index.html#dfn-security-level-m" class="externalDFN" data-link-type="dfn">Security Level [M]</a>.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-timelock-for-privileged-actions"><strong>[Q] Use TimeLock delays for sensitive operations<span class="selflink"></span></strong><br />
Sensitive operations that affect all or a majority of users <em>MUST</em> use [</a><a href="checklist.html#bib-timelock" class="bibref" data-link-type="biblio" title="Protect Your Users With Smart Contract Timelocks">TimeLock</a>] delays.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-3-linted"><strong>[Q] Code Linting<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a>
<ul>
<li><em>MUST NOT</em> create unnecessary variables, <strong>and</strong></li>
<li><em>MUST NOT</em> use the same name for functions, variables or other tokens that can occur within the same scope, <strong>and</strong></li>
<li><em>MUST NOT</em> include <code>assert()</code> statements that fail in normal operation, <strong>and</strong></li>
<li><em>MUST NOT</em> include code that cannot be reached in execution<br />
<strong>except</strong> for code explicitly intended to manage unexpected errors, such as <code>assert()</code> statements, <strong>and</strong></li>
<li><em>MUST NOT</em> contain a function that has the same name as the smart contract <strong>unless</strong> it is explicitly declared as a constructor using the <code>constructor</code> keyword, <strong>and</strong></li>
<li><em>MUST</em> explicitly declare the visibility of all functions and variables, <strong>and</strong></li>
<li><em>MUST</em> specify one or more Solidity compiler versions in its <code>pragma</code> directive.</li>
</ul></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-enough-gas"><strong>[Q] Manage Gas Use Increases<span class="selflink"></span></strong><br />
Sufficient Gas <em>MUST</em> be available to work with data structures in the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that grow over time, in accordance with descriptions provided for <a href="checklist.html#req-3-documented"><strong>[Q] Document Contract Logic</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-protect-gas"><strong>[Q] Protect Gas Usage<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> protect against malicious actors stealing or wasting gas.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-check-oracles"><strong>[Q] Protect against Oracle Failure<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> protect itself against malfunctions in <a href="index.html#dfn-oracles" class="externalDFN" data-link-type="dfn">Oracles</a> it relies on.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-block-front-running"><strong>[Q] Protect against Ordering Attacks<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST NOT</em> require information in a form that can be used to enable <a href="index.html#dfn-ordering-attacks" class="externalDFN" data-link-type="dfn">Ordering Attacks</a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-block-mev"><strong>[Q] Protect against MEV Attacks<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that is susceptible to <a href="index.html#dfn-mev" class="externalDFN" data-link-type="dfn">MEV</a> attacks <em>MUST</em> follow appropriate design patterns to mitigate this risk.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-protect-governance"><strong>[Q] Protect against Governance Takeovers<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> which includes a governance system <em>MUST</em> protect against malicious exploitation of the governance design.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-all-valid-inputs"><strong>[Q] Process All Inputs<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>MUST</em> validate inputs, and function correctly whether the input is as designed or malformed.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-event-on-state-change"><strong>[Q] State Changes Trigger Events<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> emit a contract event for all transactions that cause state changes.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-no-private-data"><strong>[Q] No Private Data<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST NOT</em> store <a href="index.html#dfn-private-data" class="externalDFN" data-link-type="dfn">Private Data</a> on the blockchain</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-intended-replay"><strong>[Q] Intended Replay<span class="selflink"></span></strong><br />
If a signature within the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> can be reused, the replay instance <em>MUST</em> be intended, documented, <strong>and</strong> safe for re-use.<br />
<br />
This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-2-malleable-signatures-for-replay"><strong>[M] No Improper Usage of Signatures for Replay Attack Protection</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-documented"><strong>[Q] Document Contract Logic<span class="selflink"></span></strong><br />
A specification of the business logic that the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> functionality is intended to implement <em>MUST</em> be available to anyone who can call the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-document-system"><strong>[Q] Document System Architecture<span class="selflink"></span></strong><br />
Documentation of the system architecture for the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> be provided that conveys the overrall system design, privileged roles, security assumptions and intended usage.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="https://entethalliance.org/specs/ethtrust-sl/v3/security-levels-spec.html#req-3-document-threats"><strong>[Q] Document Threat Models<span class="selflink"></span></strong><br />
Documentation of Threat Models considered for the</a> <a href="https://entethalliance.org/specs/ethtrust-sl/v3/security-levels-spec.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> be provided, that describes the threat, security assumptions and expected responses and outcomes.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-annotate"><strong>[Q] Annotate Code with NatSpec<span class="selflink"></span></strong><br />
All public interfaces contained in the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> be annotated with inline comments according to the [<a href="checklist.html#bib-natspec" class="bibref" data-link-type="biblio" title="NatSpec Format - Solidity Documentation.">NatSpec</a>] format that explain the intent behind each function, parameter, event, and return variable, along with developer notes for safe usage.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-implement-as-documented"><strong>[Q] Implement as Documented<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> <em>MUST</em> behave as described in the documentation provided for <a href="checklist.html#req-3-documented"><strong>[Q] Document Contract Logic</strong></a>, <strong>and</strong> <a href="checklist.html#req-3-document-system"><strong>[Q] Document System Architecture</strong></a>.</p></td>
<td>Not Tested Passes Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-access-control"><strong>[Q] Enforce Least Privilege<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> that enables privileged access <em>MUST</em> implement appropriate access control mechanisms that provide the least privilege necessary for those interactions, based on the documentation provided for <a href="checklist.html#req-3-documented"><strong>[Q] Document Contract Logic</strong></a>.<br />
This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-2-self-destruct"><strong>[S] Protect Self-destruction</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-revocable-permisions"><strong>[Q] Use Revocable and Transferable Access Control Permissions<span class="selflink"></span></strong><br />
If the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it <em>MUST</em> implement a mechanism to revoke and transfer those permissions.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-no-single-admin-eoa"><strong>[Q] No Single Admin EOA for Privileged Actions<span class="selflink"></span></strong><br />
If the</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested code</a> makes uses of Access Control for privileged actions, it <em>MUST</em> ensure that all critical administrative tasks require multiple signatures to be executed, unless there is a multisg admin that has greater privileges and can revoke permissions in case of a compromised or rogue EOA and reverse any adverse action the EOA has taken.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-3-external-calls"><strong>[Q] Verify External Calls<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that contains external calls
<ul>
<li><em>MUST</em> document the need for them, <strong>and</strong></li>
<li><em>MUST</em> protect them in a way that is fully compatible with the claims of the contract author.</li>
</ul>
<p>This is part of a <a href="index.html#dfn-sets-of-overriding-requirements" class="externalDFN" data-link-type="dfn">Set of Overriding Requirements</a> for <a href="checklist.html#summ-req-1-use-c-e-i"><strong>[S] Use Check-Effects-Interaction</strong></a>, and for <a href="checklist.html#summ-req-2-external-calls"><strong>[M] Protect External Calls</strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><a href="index.html#req-3-verify-tx.origin"><strong>[Q] Verify <code>tx.origin</code> Usage<span class="selflink"></span></strong><br />
For</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> that uses <code>tx.origin</code>, each instance
<ul>
<li><em>MUST</em> be consistent with the stated security and functionality objectives of the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>, <strong>and</strong></li>
<li><em>MUST NOT</em> allow assertions about contract functionality made for <a href="checklist.html#req-3-documented"><strong>[Q] Document Contract Logic</strong></a> or <a href="checklist.html#req-3-document-system"><strong>[Q] Document System Architecture</strong></a> to be violated by another contract, even where that contract is called by a user authorized to interact directly with the <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a>.</li>
</ul>
<p>This is an <a href="index.html#dfn-overriding-requirement" class="externalDFN" data-link-type="dfn">Overriding Requirement</a> for <a href="checklist.html#summ-req-1-no-tx.origin"><strong>[S] No <code>tx.origin</code></strong></a>.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-3-consistent-solidity-output"><strong>[Q] Specify Solidity Compiler Versions to Produce Consistent Output<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> MUST specify a range of Solidity versions in its <code>pragma</code> directive(s) that produce the same Bytecode given the same compilation options.</p></td>
<td>Not Tested Passes Not Applicable (Passes) Partial, Incomplete (Fails) Fails</td>
<td></td>
</tr>
</tbody>
</table>

### 2.3 Recommended Good Practices<a href="checklist.html#sec-summary-of-requirements" class="self-link" aria-label="§"></a>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Recommended Practice</th>
<th>Status</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="index.html#req-R-check-new-bugs"><strong>[GP] Check For and Address New Security Bugs<span class="selflink"></span></strong><br />
Check [</a><a href="checklist.html#bib-solidity-bugs-json" class="bibref" data-link-type="biblio" title="A JSON-formatted list of some known security-relevant Solidity bugs">solidity-bugs-json</a>] and other sources for bugs announced after 1 November 2023 and address them.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-meet-all-possible"><strong>[GP] Meet As Many Requirements As Possible<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> meet as many requirements of this specification as possible at Security Levels above the Security Level for which it is certified.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-use-latest-compiler"><strong>[GP] Use Latest Compiler<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> use the latest available stable Solidity compiler version.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-clean-code"><strong>[GP] Write clear, legible Solidity code<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> be written for easy understanding.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-follow-erc-standards"><strong>[GP] Follow Accepted ERC Standards<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> conform to finalized [<a href="checklist.html#bib-erc" class="bibref" data-link-type="biblio" title="ERC Final - Ethereum Improvement Proposals">ERC</a>] standards when it is reasonably capable of doing so for its use-case.</p></td>
<td>Not Tested Implemented Not Applicable Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-define-license"><strong>[GP] Define a Software License<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> define a software license.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-notify-news"><strong>[GP] Disclose New Vulnerabilities Responsibly<span class="selflink"></span></strong><br />
Security vulnerabilities that are not addressed by this specification <em>SHOULD</em> be brought to the attention of the Working Group and others through responsible disclosure as described in</a> <a href="index.html#sec-notifying-new-vulnerabilities" class="sec-ref">§ 1.4 Feedback and new vulnerabilities</a>.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-fuzzing-in-testing"><strong>[GP] Use Fuzzing<span class="selflink"></span></strong><br />
</a><a href="index.html#dfn-fuzzing" class="externalDFN" data-link-type="dfn">Fuzzing</a> <em>SHOULD</em> be used to probe <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> for errors.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-mutation-testing"><strong>[GP] Use Mutation Testing</strong></a><a href="checklist.html#req-R-mutation-testing" class="selflink"></a><br />
<a href="index.html#dfn-mutation-testing" class="externalDFN" data-link-type="dfn">Mutation Testing</a> <em>SHOULD</em>em&gt; be used to evaluate and improve the quality of test suites for smart contracts.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><p><a href="index.html#req-R-formal-verification"><strong>[GP] Use Formal Verification<span class="selflink"></span></strong><br />
The</a> <a href="index.html#dfn-tested-code" class="externalDFN" data-link-type="dfn">Tested Code</a> <em>SHOULD</em> undergo formal verification.</p></td>
<td>Not Tested Implemented Not Implemented</td>
<td></td>
</tr>
<tr>
<td><strong>[GP] Select an appropriate threshold for multisig wallets<a href="checklist.html#req-R-multisig-threshold" class="selflink"></a></strong><br />
Multisignature requirements for privileged actions <em>SHOULD</em> have a sufficient number of signers, and NOT require "1 of N" nor all signatures.</td>
<td>Not Tested Implemented Not Applicable Not Implemented</td>
<td></td>
</tr>
</tbody>
</table>

## A. Additional Information<a href="checklist.html#sec-additional-information" class="self-link" aria-label="§"></a>

### A.1 Defined Terms<a href="checklist.html#sec-definitions" class="self-link" aria-label="§"></a>

Definitions of the following terms, copied from the [EEA EthTrust Security Levels Specification](index.html), are given in this document:

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
- <a href="index.html#dfn-ordering-attacks" id="dfnanchor-27">Ordering Attacks</a>
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
[EEA EthTrust Security Levels Specification. Version 2](https://entethalliance.org/specs/ethtrust-sl/v1/). Enterprise Ethereum Alliance. URL: <https://entethalliance.org/specs/ethtrust-sl/v1/>

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
