<div id="header">

# Contracts

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

**A library for secure smart contract development.** Build on a solid foundation of community-vetted code.

</div>

<div class="ulist">

- Implementations of standards like [ERC20](erc20.html) and [ERC721](erc721.html).

- Flexible [role-based permissioning](access-control.html) scheme.

- Reusable [Solidity components](utilities.html) to build custom contracts and complex decentralized systems.

</div>

<div class="admonitionblock important">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Important
</div></td>
<td class="content">OpenZeppelin Contracts uses semantic versioning to communicate backwards compatibility of its API and storage layout. For upgradeable contracts, the storage layout of different major versions should be assumed incompatible, for example, it is unsafe to upgrade from 4.9.3 to 5.0.0. Learn more at <a href="backwards-compatibility.html">Backwards Compatibility</a>.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect1">

## Overview

<div class="sectionbody">

<div class="sect2">

### Installation

<div class="sect3">

#### Hardhat (npm)

<div class="listingblock">

<div class="content">

``` highlight
$ npm install @openzeppelin/contracts
```

</div>

</div>

</div>

<div class="sect3">

#### Foundry (git)

<div class="admonitionblock warning">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Warning
</div></td>
<td class="content">When installing via git, it is a common error to use the <code>master</code> branch. This is a development branch that should be avoided in favor of tagged releases. The release process involves security measures that the <code>master</code> branch does not guarantee.</td>
</tr>
</tbody>
</table>

</div>

<div class="admonitionblock warning">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Warning
</div></td>
<td class="content">Foundry installs the latest version initially, but subsequent <code>forge update</code> commands will use the <code>master</code> branch.</td>
</tr>
</tbody>
</table>

</div>

<div class="listingblock">

<div class="content">

``` highlight
$ forge install OpenZeppelin/openzeppelin-contracts
```

</div>

</div>

<div class="paragraph">

Add `@openzeppelin/contracts/=lib/openzeppelin-contracts/contracts/` in `remappings.txt.`

</div>

</div>

</div>

<div class="sect2">

### Usage

<div class="paragraph">

Once installed, you can use the contracts in the library by importing them:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$MyNFT.sol[role=include]
```

</div>

</div>

<div class="admonitionblock tip">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Tip
</div></td>
<td class="content">If you’re new to smart contract development, head to <a href="learn::developing-smart-contracts.html">Developing Smart Contracts</a> to learn about creating a new project and compiling your contracts.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

To keep your system secure, you should **always** use the installed code as-is, and neither copy-paste it from online sources, nor modify it yourself. The library is designed so that only the contracts and functions you use are deployed, so you don’t need to worry about it needlessly increasing gas costs.

</div>

</div>

</div>

</div>

<div class="sect1">

## Security

<div class="sectionbody">

<div class="paragraph">

Please report any security issues you find via our [bug bounty program on Immunefi](https://www.immunefi.com/bounty/openzeppelin) or directly to <security@openzeppelin.org>.

</div>

<div class="paragraph">

The [Security Center](https://contracts.openzeppelin.com/security) contains more details about the secure development process.

</div>

</div>

</div>

<div class="sect1">

## Learn More

<div class="sectionbody">

<div class="paragraph">

The guides in the sidebar will teach about different concepts, and how to use the related contracts that OpenZeppelin Contracts provides:

</div>

<div class="ulist">

- [Access Control](access-control.html): decide who can perform each of the actions on your system.

- [Tokens](tokens.html): create tradable assets or collectibles, like the well known [ERC20](erc20.html) and [ERC721](erc721.html) standards.

- [Utilities](utilities.html): generic useful tools, including non-overflowing math, signature verification, and trustless paying systems.

</div>

<div class="paragraph">

The [full API](api:token/ERC20.html) is also thoroughly documented, and serves as a great reference when developing your smart contract application. You can also ask for help or follow Contracts' development in the [community forum](https://forum.openzeppelin.com).

</div>

<div class="paragraph">

The following articles provide great background reading, though please note, some of the referenced tools have changed as the tooling in the ecosystem continues to rapidly evolve.

</div>

<div class="ulist">

- [The Hitchhiker’s Guide to Smart Contracts in Ethereum](https://blog.openzeppelin.com/the-hitchhikers-guide-to-smart-contracts-in-ethereum-848f08001f05) will help you get an overview of the various tools available for smart contract development, and help you set up your environment.

- [A Gentle Introduction to Ethereum Programming, Part 1](https://blog.openzeppelin.com/a-gentle-introduction-to-ethereum-programming-part-1-783cc7796094) provides very useful information on an introductory level, including many basic concepts from the Ethereum platform.

- For a more in-depth dive, you may read the guide [Designing the architecture for your Ethereum application](https://blog.openzeppelin.com/designing-the-architecture-for-your-ethereum-application-9cec086f8317), which discusses how to better structure your application and its relationship to the real world.

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
