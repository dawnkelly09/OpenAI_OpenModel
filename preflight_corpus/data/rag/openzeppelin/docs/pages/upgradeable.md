<div id="header">

# Using with Upgrades

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

If your contract is going to be deployed with upgradeability, such as using the [OpenZeppelin Upgrades Plugins](upgrades-plugins::index.html), you will need to use the Upgradeable variant of OpenZeppelin Contracts.

</div>

<div class="paragraph">

This variant is available as a separate package called `@openzeppelin/contracts-upgradeable`, which is hosted in the repository [OpenZeppelin/openzeppelin-contracts-upgradeable](https://github.com/OpenZeppelin/openzeppelin-contracts-upgradeable). It uses `@openzeppelin/contracts` as a peer dependency.

</div>

<div class="paragraph">

It follows all of the rules for [Writing Upgradeable Contracts](upgrades-plugins::writing-upgradeable.html): constructors are replaced by initializer functions, state variables are initialized in initializer functions, and we additionally check for storage incompatibilities across minor versions.

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
<td class="content">OpenZeppelin provides a full suite of tools for deploying and securing upgradeable smart contracts. <a href="openzeppelin::upgrades.html">Check out the full list of resources</a>.</td>
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

<div class="listingblock">

<div class="content">

``` highlight
$ npm install @openzeppelin/contracts-upgradeable @openzeppelin/contracts
```

</div>

</div>

</div>

<div class="sect2">

### Usage

<div class="paragraph">

The Upgradeable package replicates the structure of the main OpenZeppelin Contracts package, but every file and contract has the suffix `Upgradeable`.

</div>

<div class="listingblock">

<div class="content">

``` highlight
-import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
+import {ERC721Upgradeable} from "@openzeppelin/contracts-upgradeable/token/ERC721/ERC721Upgradeable.sol";

-contract MyCollectible is ERC721 {
+contract MyCollectible is ERC721Upgradeable {
```

</div>

</div>

<div class="admonitionblock note">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Note
</div></td>
<td class="content">Interfaces and libraries are not included in the Upgradeable package, but are instead imported from the main OpenZeppelin Contracts package.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Constructors are replaced by internal initializer functions following the naming convention `__{ContractName}_init`. Since these are internal, you must always define your own public initializer function and call the parent initializer of the contract you extend.

</div>

<div class="listingblock">

<div class="content">

``` highlight
-    constructor() ERC721("MyCollectible", "MCO") public {
+    function initialize() initializer public {
+        __ERC721_init("MyCollectible", "MCO");
     }
```

</div>

</div>

<div class="admonitionblock caution">

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="icon"><div class="title">
Caution
</div></td>
<td class="content">Use with multiple inheritance requires special attention. See the section below titled <a href="#multiple-inheritance">Multiple Inheritance</a>.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Once this contract is set up and compiled, you can deploy it using the [Upgrades Plugins](upgrades-plugins::index.html). The following snippet shows an example deployment script using Hardhat.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// scripts/deploy-my-collectible.js
const { ethers, upgrades } = require("hardhat");

async function main() {
  const MyCollectible = await ethers.getContractFactory("MyCollectible");

  const mc = await upgrades.deployProxy(MyCollectible);

  await mc.waitForDeployment();
  console.log("MyCollectible deployed to:", await mc.getAddress());
}

main();
```

</div>

</div>

</div>

</div>

</div>

<div class="sect1">

## Further Notes

<div class="sectionbody">

<div class="sect2">

### Multiple Inheritance

<div class="paragraph">

Initializer functions are not linearized by the compiler like constructors. Because of this, each `__{ContractName}_init` function embeds the linearized calls to all parent initializers. As a consequence, calling two of these `init` functions can potentially initialize the same contract twice.

</div>

<div class="paragraph">

The function `__{ContractName}_init_unchained` found in every contract is the initializer function minus the calls to parent initializers, and can be used to avoid the double initialization problem, but doing this manually is not recommended. We hope to be able to implement safety checks for this in future versions of the Upgrades Plugins.

</div>

</div>

<div class="sect2">

### Namespaced Storage

<div class="paragraph">

You may notice that contracts use a struct with the `@custom:storage-location erc7201:<NAMESPACE_ID>` annotation to store the contract’s state variables. This follows the [ERC-7201: Namespaced Storage Layout](https://eips.ethereum.org/EIPS/eip-7201) pattern, where each contract has its own storage layout in a namespace that is separate from other contracts in the inheritance chain.

</div>

<div class="paragraph">

Without namespaced storage, it isn’t safe to simply add a state variable because it "shifts down" all of the state variables below in the inheritance chain. This makes the storage layouts incompatible, as explained in [Writing Upgradeable Contracts](upgrades-plugins::writing-upgradeable.html#modifying-your-contracts).

</div>

<div class="paragraph">

The namespaced storage pattern used in the Upgradeable package allows us to freely add new state variables in the future without compromising the storage compatibility with existing deployments. It also allows changing the inheritance order with no impact on the resulting storage layout, as long as all inherited contracts use namespaced storage.

</div>

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
