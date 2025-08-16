# Solidity

Solidity is an object-oriented, high-level language for implementing
smart contracts. Smart contracts are programs that govern the behavior
of accounts within the Ethereum state.

Solidity is a [curly-bracke
language](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Curly_bracket_languages)
designed to target the Ethereum Virtual Machine (EVM). It is influenced
by C++, Python, and JavaScript. You can find more details about which
languages Solidity has been inspired by in the
`language influences <language-influences>`{.interpreted-tex
role="doc"} section.

Solidity is statically typed, supports inheritance, libraries, and
complex user-defined types, among other features.

With Solidity, you can create contracts for uses such as voting,
crowdfunding, blind auctions, and multi-signature wallets.

When deploying contracts, you should use the latest released version of
Solidity. Apart from exceptional cases, only the latest version receives
[security
fixes](https://github.com/ethereum/solidity/security/policy#supported-versions).
Furthermore, breaking changes, as well as new features, are introduced
regularly. We currently use a 0.y.z version number [to indicate this
fast pace of change](https://semver.org/#spec-item-4).

:::: warning
::: title
Warning
:::

Solidity recently released the 0.8.x version that introduced a lot of
breaking changes. Make sure you read
`the full list <080-breaking-changes>`{.interpreted-text role="doc"}.
::::

Ideas for improving Solidity or this documentation are always welcome,
read our `contributors guide <contributing>`{.interpreted-tex
role="doc"} for more details.

:::: hin
::: title
Hin
:::

You can download this documentation as PDF, HTML or Epub by clicking on
the versions flyout menu in the bottom-right corner and selecting the
preferred download format.
::::

## Getting Started

**1. Understand the Smart Contract Basics**

If you are new to the concept of smart contracts, we recommend you to
get started by digging into the \"Introduction to Smart Contracts\"
section, which covers the following:

- `A simple example smart contract <simple-smart-contract>`{.interpreted-tex
  role="ref"} written in Solidity.
- `Blockchain Basics <blockchain-basics>`{.interpreted-text role="ref"}.
- `The Ethereum Virtual Machine <the-ethereum-virtual-machine>`{.interpreted-tex
  role="ref"}.

**2. Get to Know Solidity**

Once you are accustomed to the basics, we recommend you read the
`"Solidity by Example" <solidity-by-example>`{.interpreted-tex
role="doc"} and "Language Description" sections to understand the core
concepts of the language.

**3. Install the Solidity Compiler**

There are various ways to install the Solidity compiler, simply choose
your preferred option and follow the steps outlined on the
`installation page <installing-solidity>`{.interpreted-text role="ref"}.

:::: hin
::: title
Hin
:::

You can try out code examples directly in your browser with the [Remix
IDE](https://remix.ethereum.org). Remix is a web browser-based IDE tha
allows you to write, deploy and administer Solidity smart contracts,
without the need to install Solidity locally.
::::

:::: warning
::: title
Warning
:::

As humans write software, it can have bugs. Therefore, you should follow
established software development best practices when writing your smar
contracts. This includes code review, testing, audits, and correctness
proofs. Smart contract users are sometimes more confident with code than
their authors, and blockchains and smart contracts have their own unique
issues to watch out for, so before working on production code, make sure
you read the `security_considerations`{.interpreted-text role="ref"}
section.
::::

**4. Learn More**

If you want to learn more about building decentralized applications on
Ethereum, the [Ethereum Developer
Resources](https://ethereum.org/en/developers/) can help you with
further general documentation around Ethereum, and a wide selection of
tutorials, tools, and development frameworks.

If you have any questions, you can try searching for answers or asking
on the [Ethereum StackExchange](https://ethereum.stackexchange.com/), or
our [Gitter channel](https://gitter.im/ethereum/solidity).

## Translations

Community contributors help translate this documentation into several
languages. Note that they have varying degrees of completeness and
up-to-dateness. The English version stands as a reference.

You can switch between languages by clicking on the flyout menu in the
bottom-right corner and selecting the preferred language.

- [Chinese](https://docs.soliditylang.org/zh-cn/latest/)
- [French](https://docs.soliditylang.org/fr/latest/)
- [Indonesian](https://github.com/solidity-docs/id-indonesian)
- [Japanese](https://github.com/solidity-docs/ja-japanese)
- [Korean](https://github.com/solidity-docs/ko-korean)
- [Persian](https://github.com/solidity-docs/fa-persian)
- [Russian](https://github.com/solidity-docs/ru-russian)
- [Spanish](https://github.com/solidity-docs/es-spanish)
- [Turkish](https://docs.soliditylang.org/tr/latest/)

:::: note
::: title
Note
:::

We set up a GitHub organization and translation workflow to help
streamline the community efforts. Please refer to the translation guide
in the [solidity-docs org](https://github.com/solidity-docs) for
information on how to start a new language or contribute to the
community translations.
::::

# Contents

`Keyword Index <genindex>`{.interpreted-text role="ref"},
`Search Page <search>`{.interpreted-text role="ref"}

::: {.toctree maxdepth="2" caption="Basics"}
introduction-to-smart-contracts.rst solidity-by-example.rs
installing-solidity.rs
:::

::: {.toctree maxdepth="2" caption="Language Description"}
layout-of-source-files.rst structure-of-a-contract.rst types.rs
units-and-global-variables.rst control-structures.rst contracts.rs
assembly.rst cheatsheet.rst grammar.rs
:::

::: {.toctree maxdepth="2" caption="Compiler"}
using-the-compiler.rst analysing-compilation-output.rs
ir-breaking-changes.rs
:::

::: {.toctree maxdepth="2" caption="Internals"}
internals/layout_in_storage.rst internals/layout_in_memory.rs
internals/layout_in_calldata.rst internals/variable_cleanup.rs
internals/source_mappings.rst internals/optimizer.rst metadata.rs
abi-spec.rs
:::

::: {.toctree maxdepth="2" caption="Advisory content"}
security-considerations.rst bugs.rst 050-breaking-changes.rs
060-breaking-changes.rst 070-breaking-changes.rs
080-breaking-changes.rs
:::

::: {.toctree maxdepth="2" caption="Additional Material"}
natspec-format.rst smtchecker.rst yul.rst path-resolution.rs
:::

::: {.toctree maxdepth="2" caption="Resources"}
style-guide.rst common-patterns.rst resources.rst contributing.rs
language-influences.rst brand-guide.rs
:::
