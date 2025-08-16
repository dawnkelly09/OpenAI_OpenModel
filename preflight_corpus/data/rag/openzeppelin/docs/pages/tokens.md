<div id="header">

# Tokens

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

Ah, the "token": blockchain’s most powerful and most misunderstood tool.

</div>

<div class="paragraph">

A token is a *representation of something in the blockchain*. This something can be money, time, services, shares in a company, a virtual pet, anything. By representing things as tokens, we can allow smart contracts to interact with them, exchange them, create or destroy them.

</div>

</div>

</div>

<div class="sect1">

## But First, <span class="strikethrough">Coffee</span> a Primer on Token Contracts

<div class="sectionbody">

<div class="paragraph">

Much of the confusion surrounding tokens comes from two concepts getting mixed up: *token contracts* and the actual *tokens*.

</div>

<div class="paragraph">

A *token contract* is simply an Ethereum smart contract. "Sending tokens" actually means "calling a method on a smart contract that someone wrote and deployed". At the end of the day, a token contract is not much more than a mapping of addresses to balances, plus some methods to add and subtract from those balances.

</div>

<div class="paragraph">

It is these balances that represent the *tokens* themselves. Someone "has tokens" when their balance in the token contract is non-zero. That’s it! These balances could be considered money, experience points in a game, deeds of ownership, or voting rights, and each of these tokens would be stored in different token contracts.

</div>

</div>

</div>

<div class="sect1">

## Different Kinds of Tokens

<div class="sectionbody">

<div class="paragraph">

Note that there’s a big difference between having two voting rights and two deeds of ownership: each vote is equal to all others, but houses usually are not! This is called [fungibility](https://en.wikipedia.org/wiki/Fungibility). *Fungible goods* are equivalent and interchangeable, like Ether, fiat currencies, and voting rights. *Non-fungible* goods are unique and distinct, like deeds of ownership, or collectibles.

</div>

<div class="paragraph">

In a nutshell, when dealing with non-fungibles (like your house) you care about *which ones* you have, while in fungible assets (like your bank account statement) what matters is *how much* you have.

</div>

</div>

</div>

<div class="sect1">

## Standards

<div class="sectionbody">

<div class="paragraph">

Even though the concept of a token is simple, they have a variety of complexities in the implementation. Because everything in Ethereum is just a smart contract, and there are no rules about what smart contracts have to do, the community has developed a variety of **standards** (called EIPs or ERCs) for documenting how a contract can interoperate with other contracts.

</div>

<div class="paragraph">

You’ve probably heard of the ERC-20 or ERC-721 token standards, and that’s why you’re here. Head to our specialized guides to learn more about these:

</div>

<div class="ulist">

- [ERC-20](erc20.html): the most widespread token standard for fungible assets, albeit somewhat limited by its simplicity.

- [ERC-721](erc721.html): the de-facto solution for non-fungible tokens, often used for collectibles and games.

- [ERC-1155](erc1155.html): a novel standard for multi-tokens, allowing for a single contract to represent multiple fungible and non-fungible tokens, along with batched operations for increased gas efficiency.

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
