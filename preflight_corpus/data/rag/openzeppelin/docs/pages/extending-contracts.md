<div id="header">

# Extending Contracts

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

Most of the OpenZeppelin Contracts are expected to be used via [inheritance](https://solidity.readthedocs.io/en/latest/contracts.html#inheritance): you will *inherit* from them when writing your own contracts.

</div>

<div class="paragraph">

This is the commonly found `is` syntax, like in `contract MyToken is ERC20`.

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
<td class="content"><div class="paragraph">
<p>Unlike <code>contract</code>s, Solidity <code>library</code>s are not inherited from and instead rely on the <a href="https://solidity.readthedocs.io/en/latest/contracts.html#using-for"><code>using for</code></a> syntax.</p>
</div>
<div class="paragraph">
<p>OpenZeppelin Contracts has some <code>library</code>s: most are in the <a href="api:utils.html">Utils</a> directory.</p>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect1">

## Overriding

<div class="sectionbody">

<div class="paragraph">

Inheritance is often used to add the parent contract’s functionality to your own contract, but that’s not all it can do. You can also *change* how some parts of the parent behave using *overrides*.

</div>

<div class="paragraph">

For example, imagine you want to change [`AccessControl`](api:access.html#AccessControl) so that [`revokeRole`](api:access.html#AccessControl-revokeRole-bytes32-address-) can no longer be called. This can be achieved using overrides:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessControlModified.sol[role=include]
```

</div>

</div>

<div class="paragraph">

The old `revokeRole` is then replaced by our override, and any calls to it will immediately revert. We cannot *remove* the function from the contract, but reverting on all calls is good enough.

</div>

<div class="sect2">

### Calling `super`

<div class="paragraph">

Sometimes you want to *extend* a parent’s behavior, instead of outright changing it to something else. This is where `super` comes in.

</div>

<div class="paragraph">

The `super` keyword will let you call functions defined in a parent contract, even if they are overridden. This mechanism can be used to add additional checks to a function, emit events, or otherwise add functionality as you see fit.

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
<td class="content">For more information on how overrides work, head over to the <a href="https://solidity.readthedocs.io/en/latest/contracts.html#index-17">official Solidity documentation</a>.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Here is a modified version of [`AccessControl`](api:access.html#AccessControl) where [`revokeRole`](api:access.html#AccessControl-revokeRole-bytes32-address-) cannot be used to revoke the `DEFAULT_ADMIN_ROLE`:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessControlNonRevokableAdmin.sol[role=include]
```

</div>

</div>

<div class="paragraph">

The `super.revokeRole` statement at the end will invoke `AccessControl`'s original version of `revokeRole`, the same code that would’ve run if there were no overrides in place.

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
<td class="content">The same rule is implemented and extended in <a href="api:access.html#AccessControlDefaultAdminRules"><code>AccessControlDefaultAdminRules</code></a>, an extension that also adds enforced security measures for the <code>DEFAULT_ADMIN_ROLE</code>.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="sect1">

## Security

<div class="sectionbody">

<div class="paragraph">

The maintainers of OpenZeppelin Contracts are mainly concerned with the correctness and security of the code as published in the library, and the combinations of base contracts with the official extensions from the library.

</div>

<div class="paragraph">

Custom overrides, especially to hooks, can disrupt important assumptions and may introduce security risks in the code that was previously secure. While we try to ensure the contracts remain secure in the face of a wide range of potential customizations, this is done in a best-effort manner. While we try to document all important assumptions, this should not be relied upon. Custom overrides should be carefully reviewed and checked against the source code of the contract they are customizing to fully understand their impact and guarantee their security.

</div>

<div class="paragraph">

The way functions interact internally should not be assumed to stay stable across releases of the library. For example, a function that is used in one context in a particular release may not be used in the same context in the next release. Contracts that override functions should revalidate their assumptions when updating the version of OpenZeppelin Contracts they are built on.

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
