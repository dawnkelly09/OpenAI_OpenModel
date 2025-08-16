<div id="header">

# Backwards Compatibility

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

OpenZeppelin Contracts uses semantic versioning to communicate backwards compatibility of its API and storage layout. Patch and minor updates will generally be backwards compatible, with rare exceptions as detailed below. Major updates should be assumed incompatible with previous releases. On this page, we provide details about these guarantees.

</div>

</div>

</div>

<div class="sect1">

## API

<div class="sectionbody">

<div class="paragraph">

In backwards compatible releases, all changes should be either additions or modifications to internal implementation details. Most code should continue to compile and behave as expected. The exceptions to this rule are listed below.

</div>

<div class="sect2">

### Security

<div class="paragraph">

Infrequently a patch or minor update will remove or change an API in a breaking way, but only if the previous API is considered insecure. These breaking changes will be noted in the changelog and release notes, and published along with a security advisory.

</div>

</div>

<div class="sect2">

### Draft or Pre-Final ERCs

<div class="paragraph">

ERCs that are not Final can change in incompatible ways. For this reason, we avoid shipping implementations of ERCs before they are Final. Some exceptions are made for ERCs that have been published for a long time and seem unlikely to change. Implementations for ERCs that may have breaking changes are published in files named `draft-*.sol` to make that condition explicit. There is no backwards compatibility guarantee for content in files prefixed with `draft`.

</div>

<div class="paragraph">

Standards that have achieved widespread adoption with strong backwards compatibility expectations from the community may be treated as de-facto finalized and published without the `draft-` prefix, as extensive ecosystem reliance makes breaking changes highly unlikely.

</div>

</div>

<div class="sect2">

### Virtual & Overrides

<div class="paragraph">

Almost all functions in this library are virtual with some exceptions, but this does not mean that overrides are encouraged. There is a subset of functions that are designed to be overridden. By defining overrides outside of this subset you are potentially relying on internal implementation details. We make efforts to preserve backwards compatibility even in these cases but it is extremely difficult and easy to accidentally break. Caution is advised.

</div>

<div class="paragraph">

Additionally, some minor updates may result in new compilation errors of the kind "two or more base classes define function with same name and parameter types" or "need to specify overridden contract", due to what Solidity considers ambiguity in inherited functions. This should be resolved by adding an override that invokes the function via `super`.

</div>

<div class="paragraph">

See [Extending Contracts](extending-contracts.html) for more about virtual and overrides.

</div>

</div>

<div class="sect2">

### Structs

<div class="paragraph">

Struct members with an underscore prefix should be considered "private" and may break in minor versions. Struct data should only be accessed and modified through library functions.

</div>

</div>

<div class="sect2">

### Errors

<div class="paragraph">

The specific error format and data that is included with reverts should not be assumed stable unless otherwise specified.

</div>

</div>

<div class="sect2">

### Major Releases

<div class="paragraph">

Major releases should be assumed incompatible. Nevertheless, the external interfaces of contracts will remain compatible if they are standardized, or if the maintainers judge that changing them would cause significant strain on the ecosystem.

</div>

<div class="paragraph">

An important aspect that major releases may break is "upgrade compatibility", in particular storage layout compatibility. It will never be safe for a live contract to upgrade from one major release to another.

</div>

</div>

</div>

</div>

<div class="sect1">

## Storage Layout

<div class="sectionbody">

<div class="paragraph">

Minor and patch updates always preserve storage layout compatibility. This means that a live contract can be upgraded from one minor to another without corrupting the storage layout. In some cases it may be necessary to initialize new state variables when upgrading, although we expect this to be infrequent.

</div>

<div class="paragraph">

We recommend using [OpenZeppelin Upgrades Plugins or CLI](upgrades-plugins::index.html) to ensure storage layout safety of upgrades.

</div>

</div>

</div>

<div class="sect1">

## Solidity Version

<div class="sectionbody">

<div class="paragraph">

The minimum Solidity version required to compile the contracts will remain unchanged in minor and patch updates. New contracts introduced in minor releases may make use of newer Solidity features and require a more recent version of the compiler.

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
