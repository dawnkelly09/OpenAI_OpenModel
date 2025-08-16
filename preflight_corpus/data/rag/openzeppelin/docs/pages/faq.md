<div id="header">

# Frequently Asked Questions

</div>

<div id="content">

<div class="sect1">

## Can I restrict a function to EOAs only?

<div class="sectionbody">

<div class="paragraph">

When calling external addresses from your contract it is unsafe to assume that an address is an externally-owned account (EOA) and not a contract. Attempting to prevent calls from contracts is highly discouraged. It breaks composability, breaks support for smart wallets like Gnosis Safe, and does not provide security since it can be circumvented by calling from a contract constructor.

</div>

<div class="paragraph">

Although checking that the address has code, `address.code.length > 0`, may seem to differentiate contracts from EOAs, it can only say that an address is currently a contract, and its negation (that an address is not currently a contract) does not imply that the address is an EOA. Some counterexamples are:

</div>

<div class="ulist">

- address of a contract in construction

- address where a contract will be created

- address where a contract lived, but was destroyed

</div>

<div class="paragraph">

Furthermore, an address will be considered a contract within the same transaction where it is scheduled for destruction by `SELFDESTRUCT`, which only has an effect at the end of the entire transaction.

</div>

</div>

</div>

</div>

<div id="footer">

<div id="footer-text">

Last updated 2025-08-16 13:05:30 -0400

</div>

</div>
