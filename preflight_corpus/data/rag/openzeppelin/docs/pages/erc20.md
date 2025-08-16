<div id="header">

# ERC-20

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

An ERC-20 token contract keeps track of [*fungible* tokens](tokens.html#different-kinds-of-tokens): any one token is exactly equal to any other token; no tokens have special rights or behavior associated with them. This makes ERC-20 tokens useful for things like a **medium of exchange currency**, **voting rights**, **staking**, and more.

</div>

<div class="paragraph">

OpenZeppelin Contracts provides many ERC20-related contracts. On the [`API reference`](api:token/ERC20.html) you’ll find detailed information on their properties and usage.

</div>

</div>

</div>

<div class="sect1">

## Constructing an ERC-20 Token Contract

<div class="sectionbody">

<div class="paragraph">

Using Contracts, we can easily create our own ERC-20 token contract, which will be used to track *Gold* (GLD), an internal currency in a hypothetical game.

</div>

<div class="paragraph">

Here’s what our GLD token might look like.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$token/ERC20/GLDToken.sol[role=include]
```

</div>

</div>

<div class="paragraph">

Our contracts are often used via [inheritance](https://solidity.readthedocs.io/en/latest/contracts.html#inheritance), and here we’re reusing [`ERC20`](api:token/ERC20.html#erc20) for both the basic standard implementation and the [`name`](api:token/ERC20.html#ERC20-name--), [`symbol`](api:token/ERC20.html#ERC20-symbol--), and [`decimals`](api:token/ERC20.html#ERC20-decimals--) optional extensions. Additionally, we’re creating an `initialSupply` of tokens, which will be assigned to the address that deploys the contract.

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
<td class="content">For a more complete discussion of ERC-20 supply mechanisms, see <a href="erc20-supply.html">Creating ERC-20 Supply</a>.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

That’s it! Once deployed, we will be able to query the deployer’s balance:

</div>

<div class="listingblock">

<div class="content">

``` highlight
> GLDToken.balanceOf(deployerAddress)
1000000000000000000000
```

</div>

</div>

<div class="paragraph">

We can also [transfer](api:token/ERC20.html#IERC20-transfer-address-uint256-) these tokens to other accounts:

</div>

<div class="listingblock">

<div class="content">

``` highlight
> GLDToken.transfer(otherAddress, 300000000000000000000)
> GLDToken.balanceOf(otherAddress)
300000000000000000000
> GLDToken.balanceOf(deployerAddress)
700000000000000000000
```

</div>

</div>

</div>

</div>

<div class="sect1">

## A Note on `decimals`

<div class="sectionbody">

<div class="paragraph">

Often, you’ll want to be able to divide your tokens into arbitrary amounts: say, if you own `5 GLD`, you may want to send `1.5 GLD` to a friend, and keep `3.5 GLD` to yourself. Unfortunately, Solidity and the EVM do not support this behavior: only integer (whole) numbers can be used, which poses an issue. You may send `1` or `2` tokens, but not `1.5`.

</div>

<div class="paragraph">

To work around this, [`ERC20`](api:token/ERC20.html#ERC20) provides a [`decimals`](api:token/ERC20.html#ERC20-decimals--) field, which is used to specify how many decimal places a token has. To be able to transfer `1.5 GLD`, `decimals` must be at least `1`, since that number has a single decimal place.

</div>

<div class="paragraph">

How can this be achieved? It’s actually very simple: a token contract can use larger integer values, so that a balance of `50` will represent `5 GLD`, a transfer of `15` will correspond to `1.5 GLD` being sent, and so on.

</div>

<div class="paragraph">

It is important to understand that `decimals` is *only used for display purposes*. All arithmetic inside the contract is still performed on integers, and it is the different user interfaces (wallets, exchanges, etc.) that must adjust the displayed values according to `decimals`. The total token supply and balance of each account are not specified in `GLD`: you need to divide by `10 ** decimals` to get the actual `GLD` amount.

</div>

<div class="paragraph">

You’ll probably want to use a `decimals` value of `18`, just like Ether and most ERC-20 token contracts in use, unless you have a very special reason not to. When minting tokens or transferring them around, you will be actually sending the number `num GLD * (10 ** decimals)`.

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
<td class="content">By default, <code>ERC20</code> uses a value of <code>18</code> for <code>decimals</code>. To use a different value, you will need to override the <code>decimals()</code> function in your contract.</td>
</tr>
</tbody>
</table>

</div>

<div class="listingblock">

<div class="content">

``` highlight
function decimals() public view virtual override returns (uint8) {
  return 16;
}
```

</div>

</div>

<div class="paragraph">

So if you want to send `5` tokens using a token contract with 18 decimals, the method to call will actually be:

</div>

<div class="listingblock">

<div class="content">

``` highlight
transfer(recipient, 5 * (10 ** 18));
```

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
