<div id="header">

# Utilities

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

The OpenZeppelin Contracts provide a ton of useful utilities that you can use in your project. For a complete list, check out the [API Reference](api:utils.html). Here are some of the more popular ones.

</div>

</div>

</div>

<div class="sect1">

## Cryptography

<div class="sectionbody">

<div class="sect2">

### Checking Signatures On-Chain

<div class="paragraph">

At a high level, signatures are a set of cryptographic algorithms that allow for a *signer* to prove himself owner of a *private key* used to authorize a piece of information (generally a transaction or `UserOperation`). Natively, the EVM supports the Elliptic Curve Digital Signature Algorithm ([ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)) using the secp256k1 curve, however other signature algorithms such as P256 and RSA are supported.

</div>

<div class="sect3">

#### Ethereum Signatures (secp256k1)

<div class="paragraph">

[`ECDSA`](api:utils/cryptography.html#ECDSA) provides functions for recovering and managing Ethereum account ECDSA signatures. These are often generated via [`web3.eth.sign`](https://web3js.readthedocs.io/en/v1.7.3/web3-eth.html#sign), and form a 65-byte array (of type `bytes` in Solidity) arranged the following way: `[[v (1)], [r (32)], [s (32)]]`.

</div>

<div class="paragraph">

The data signer can be recovered with [`ECDSA.recover`](api:utils/cryptography.html#ECDSA-recover-bytes32-bytes-), and its address compared to verify the signature. Most wallets will hash the data to sign and add the prefix `\x19Ethereum Signed Message:\n`, so when attempting to recover the signer of an Ethereum signed message hash, you’ll want to use [`toEthSignedMessageHash`](api:utils/cryptography.html#MessageHashUtils-toEthSignedMessageHash-bytes32-).

</div>

<div class="listingblock">

<div class="content">

``` highlight
using ECDSA for bytes32;
using MessageHashUtils for bytes32;

function _verify(bytes32 data, bytes memory signature, address account) internal pure returns (bool) {
    return data
        .toEthSignedMessageHash()
        .recover(signature) == account;
}
```

</div>

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
<td class="content">Getting signature verification right is not trivial: make sure you fully read and understand <a href="api:utils/cryptography.html#MessageHashUtils"><code>MessageHashUtils</code></a>'s and <a href="api:utils/cryptography.html#ECDSA"><code>ECDSA</code></a>'s documentation.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect3">

#### P256 Signatures (secp256r1)

<div class="paragraph">

P256, also known as secp256r1, is one of the most used signature schemes. P256 signatures are standardized by the National Institute of Standards and Technology (NIST) and they are widely available in consumer hardware and software.

</div>

<div class="paragraph">

These signatures are different from regular Ethereum Signatures (secp256k1) in that they use a different elliptic curve to perform operations but have similar security guarantees.

</div>

<div class="listingblock">

<div class="content">

``` highlight
using P256 for bytes32;

function _verify(
    bytes32 data,
    bytes32 r,
    bytes32 s,
    bytes32 qx,
    bytes32 qy
) internal pure returns (bool) {
    return data.verify(data, r, s, qx, qy);
}
```

</div>

</div>

<div class="paragraph">

By default, the `verify` function will try calling the [RIP-7212](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md) precompile at address `0x100` and will fallback to an implementation in Solidity if not available. We encourage you to use `verifyNative` if you know the precompile is available on the chain you’re working on and on any other chain on which you intend to use the same bytecode in the future. In case of any doubts regarding the implementation roadmap of the native precompile `P256` of potential future target chains, please consider using `verifySolidity`.

</div>

<div class="listingblock">

<div class="content">

``` highlight
using P256 for bytes32;

function _verify(
    bytes32 data,
    bytes32 r,
    bytes32 s,
    bytes32 qx,
    bytes32 qy
) internal pure returns (bool) {
    // Will only call the precompile at address(0x100)
    return data.verifyNative(data, r, s, qx, qy);
}
```

</div>

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
<td class="content">The P256 library only allows for <code>s</code> values in the lower order of the curve (i.e. <code>s ⇐ N/2</code>) to prevent malleability. In case your tooling produces signatures in both sides of the curve, consider flipping the <code>s</code> value to keep compatibility.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect3">

#### RSA

<div class="paragraph">

RSA is a public-key cryptosystem that was popularized by corporate and governmental public key infrastructures ([PKIs](https://en.wikipedia.org/wiki/Public_key_infrastructure)) and [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions).

</div>

<div class="paragraph">

This cryptosystem consists of using a private key that’s the product of 2 large prime numbers. The message is signed by applying a modular exponentiation to its hash (commonly SHA256), where both the exponent and modulus compose the public key of the signer.

</div>

<div class="paragraph">

RSA signatures are known for being less efficient than elliptic curve signatures given the size of the keys, which are big compared to ECDSA keys with the same security level. Using plain RSA is considered unsafe, this is why the implementation uses the `EMSA-PKCS1-v1_5` encoding method from [RFC8017](https://datatracker.ietf.org/doc/html/rfc8017) to include padding to the signature.

</div>

<div class="paragraph">

To verify a signature using RSA, you can leverage the [`RSA`](api:utils/cryptography.html#RSA) library that exposes a method for verifying RSA with the PKCS 1.5 standard:

</div>

<div class="listingblock">

<div class="content">

``` highlight
using RSA for bytes32;

function _verify(
    bytes32 data,
    bytes memory signature,
    bytes memory e,
    bytes memory n
) internal pure returns (bool) {
    return data.pkcs1Sha256(signature, e, n);
}
```

</div>

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
<td class="content">Always use keys of at least 2048 bits. Additionally, be aware that PKCS#1 v1.5 allows for replayability due to the possibility of arbitrary optional parameters. To prevent replay attacks, consider including an onchain nonce or unique identifier in the message.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect2">

### Signature Verification

<div class="paragraph">

The [`SignatureChecker`](api:utils/cryptography.html#SignatureChecker) library provides a unified interface for verifying signatures from different sources. It seamlessly supports:

</div>

<div class="ulist">

- ECDSA signatures from externally owned accounts (EOAs)

- ERC-1271 signatures from smart contract wallets like Argent and Safe Wallet

- ERC-7913 signatures from keys that don’t have their own Ethereum address

</div>

<div class="paragraph">

This allows developers to write signature verification code once and have it work across all these different signature types.

</div>

<div class="sect3">

#### Basic Signature Verification

<div class="paragraph">

For standard signature verification that supports both EOAs and ERC-1271 contracts:

</div>

<div class="listingblock">

<div class="content">

``` highlight
using SignatureChecker for address;

function _verifySignature(address signer, bytes32 hash, bytes memory signature) internal view returns (bool) {
    return SignatureChecker.isValidSignatureNow(signer, hash, signature);
}
```

</div>

</div>

<div class="paragraph">

The library automatically detects whether the signer is an EOA or a contract and uses the appropriate verification method.

</div>

</div>

<div class="sect3">

#### ERC-1271 Contract Signatures

<div class="paragraph">

For smart contract wallets that implement ERC-1271, you can explicitly use:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function _verifyContractSignature(address signer, bytes32 hash, bytes memory signature) internal view returns (bool) {
    return SignatureChecker.isValidERC1271SignatureNow(signer, hash, signature);
}
```

</div>

</div>

</div>

<div class="sect3">

#### ERC-7913 Extended Signatures

<div class="paragraph">

ERC-7913 extends signature verification to support keys that don’t have their own Ethereum address. This is useful for integrating non-Ethereum cryptographic curves, hardware devices, or other identity systems.

</div>

<div class="paragraph">

A signer is represented as a `bytes` object that concatenates a verifier address and a key: `verifier || key`.

</div>

<div class="listingblock">

<div class="content">

``` highlight
function _verifyERC7913Signature(bytes memory signer, bytes32 hash, bytes memory signature) internal view returns (bool) {
    return SignatureChecker.isValidSignatureNow(signer, hash, signature);
}
```

</div>

</div>

<div class="paragraph">

The verification process works as follows:

</div>

<div class="ulist">

- If `signer.length < 20`: verification fails

- If `signer.length == 20`: verification is done using standard signature checking

- Otherwise: verification is done using an ERC-7913 verifier

</div>

</div>

<div class="sect3">

#### Batch Verification

<div class="paragraph">

For verifying multiple ERC-7913 signatures at once:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function _verifyMultipleSignatures(
    bytes32 hash,
    bytes[] memory signers,
    bytes[] memory signatures
) internal view returns (bool) {
    return SignatureChecker.areValidSignaturesNow(hash, signers, signatures);
}
```

</div>

</div>

<div class="paragraph">

This function will reject inputs that contain duplicated signers. Sorting the signers by their `keccak256` hash is recommended to minimize the gas cost.

</div>

<div class="paragraph">

This unified approach allows smart contracts to accept signatures from any supported source without needing to implement different verification logic for each type.

</div>

</div>

</div>

<div class="sect2">

### Verifying Merkle Proofs

<div class="paragraph">

Developers can build a Merkle Tree off-chain, which allows for verifying that an element (leaf) is part of a set by using a Merkle Proof. This technique is widely used for creating whitelists (e.g., for airdrops) and other advanced use cases.

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
<td class="content">OpenZeppelin Contracts provides a <a href="https://github.com/OpenZeppelin/merkle-tree">JavaScript library</a> for building trees off-chain and generating proofs.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

[`MerkleProof`](api:utils/cryptography.html#MerkleProof) provides:

</div>

<div class="ulist">

- [`verify`](api:utils/cryptography.html#MerkleProof-verify-bytes32---bytes32-bytes32-) - can prove that some value is part of a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree).

- [`multiProofVerify`](api:utils/cryptography.html#MerkleProof-multiProofVerify-bytes32-bytes32---bytes32---bool---) - can prove multiple values are part of a Merkle tree.

</div>

<div class="paragraph">

For an on-chain Merkle Tree, see the [`MerkleTree`](api:utils.html#MerkleTree) library.

</div>

</div>

</div>

</div>

<div class="sect1">

## Introspection

<div class="sectionbody">

<div class="paragraph">

In Solidity, it’s frequently helpful to know whether or not a contract supports an interface you’d like to use. ERC-165 is a standard that helps do runtime interface detection. Contracts provide helpers both for implementing ERC-165 in your contracts and querying other contracts:

</div>

<div class="ulist">

- [`IERC165`](api:utils.html#IERC165) — this is the ERC-165 interface that defines [`supportsInterface`](api:utils.html#IERC165-supportsInterface-bytes4-). When implementing ERC-165, you’ll conform to this interface.

- [`ERC165`](api:utils.html#ERC165) — inherit this contract if you’d like to support interface detection using a lookup table in contract storage. You can register interfaces using [`_registerInterface(bytes4)`](api:utils.html#ERC165-_registerInterface-bytes4-): check out example usage as part of the ERC-721 implementation.

- [`ERC165Checker`](api:utils.html#ERC165Checker) — ERC165Checker simplifies the process of checking whether or not a contract supports an interface you care about.

- include with `using ERC165Checker for address;`

- [`myAddress._supportsInterface(bytes4)`](api:utils.html#ERC165Checker-_supportsInterface-address-bytes4-)

- [`myAddress._supportsAllInterfaces(bytes4[])`](api:utils.html#ERC165Checker-_supportsAllInterfaces-address-bytes4---)

</div>

<div class="listingblock">

<div class="content">

``` highlight
contract MyContract {
    using ERC165Checker for address;

    bytes4 private InterfaceId_ERC721 = 0x80ac58cd;

    /**
     * @dev transfer an ERC-721 token from this contract to someone else
     */
    function transferERC721(
        address token,
        address to,
        uint256 tokenId
    )
        public
    {
        require(token.supportsInterface(InterfaceId_ERC721), "IS_NOT_721_TOKEN");
        IERC721(token).transferFrom(address(this), to, tokenId);
    }
}
```

</div>

</div>

</div>

</div>

<div class="sect1">

## Math

<div class="sectionbody">

<div class="paragraph">

Although Solidity already provides math operators (i.e. `+`, `-`, etc.), Contracts includes [`Math`](api:utils.html#Math); a set of utilities for dealing with mathematical operators, with support for extra operations (e.g., [`average`](api:utils.html#Math-average-uint256-uint256-)) and [`SignedMath`](api:utils.html#SignedMath); a library specialized in signed math operations.

</div>

<div class="paragraph">

Include these contracts with `using Math for uint256` or `using SignedMath for int256` and then use their functions in your code:

</div>

<div class="listingblock">

<div class="content">

``` highlight
contract MyContract {
    using Math for uint256;
    using SignedMath for int256;

    function tryOperations(uint256 a, uint256 b) internal pure {
        (bool succeededAdd, uint256 resultAdd) = x.tryAdd(y);
        (bool succeededSub, uint256 resultSub) = x.trySub(y);
        (bool succeededMul, uint256 resultMul) = x.tryMul(y);
        (bool succeededDiv, uint256 resultDiv) = x.tryDiv(y);
        // ...
    }

    function unsignedAverage(int256 a, int256 b) {
        int256 avg = a.average(b);
        // ...
    }
}
```

</div>

</div>

<div class="paragraph">

Easy!

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
<td class="content">While working with different data types that might require casting, you can use <a href="api:utils.html#SafeCast"><code>SafeCast</code></a> for type casting with added overflow checks.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect1">

## Structures

<div class="sectionbody">

<div class="paragraph">

Some use cases require more powerful data structures than arrays and mappings offered natively in Solidity. Contracts provides these libraries for enhanced data structure management:

</div>

<div class="ulist">

- [`BitMaps`](api:utils.html#BitMaps): Store packed booleans in storage.

- [`Checkpoints`](api:utils.html#Checkpoints): Checkpoint values with built-in lookups.

- [`DoubleEndedQueue`](api:utils.html#DoubleEndedQueue): Store items in a queue with `pop()` and `queue()` constant time operations.

- [`EnumerableSet`](api:utils.html#EnumerableSet): A [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) with enumeration capabilities.

- [`EnumerableMap`](api:utils.html#EnumerableMap): A `mapping` variant with enumeration capabilities.

- [`MerkleTree`](api:utils.html#MerkleTree): An on-chain [Merkle Tree](https://wikipedia.org/wiki/Merkle_Tree) with helper functions.

- [`Heap`](api:utils.html#Heap.sol): A [binary heap](https://en.wikipedia.org/wiki/Binary_heap) to store elements with priority defined by a compartor function.

</div>

<div class="paragraph">

The `Enumerable*` structures are similar to mappings in that they store and remove elements in constant time and don’t allow for repeated entries, but they also support *enumeration*, which means you can easily query all stored entries both on and off-chain.

</div>

<div class="sect2">

### Building a Merkle Tree

<div class="paragraph">

Building an on-chain Merkle Tree allows developers to keep track of the history of roots in a decentralized manner. For these cases, the [`MerkleTree`](api:utils.html#MerkleTree) includes a predefined structure with functions to manipulate the tree (e.g. pushing values or resetting the tree).

</div>

<div class="paragraph">

The Merkle Tree does not keep track of the roots intentionally, so that developers can choose their tracking mechanism. Setting up and using a Merkle Tree in Solidity is as simple as follows:

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
<td class="content">Functions are exposed without access control for demonstration purposes</td>
</tr>
</tbody>
</table>

</div>

<div class="listingblock">

<div class="content">

``` highlight
using MerkleTree for MerkleTree.Bytes32PushTree;
MerkleTree.Bytes32PushTree private _tree;

function setup(uint8 _depth, bytes32 _zero) public /* onlyOwner */ {
    root = _tree.setup(_depth, _zero);
}

function push(bytes32 leaf) public /* onlyOwner */ {
    (uint256 leafIndex, bytes32 currentRoot) = _tree.push(leaf);
    // Store the new root.
}
```

</div>

</div>

<div class="paragraph">

The library also supports custom hashing functions, which can be passed as an extra parameter to the [`push`](api:utils.html#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-) and [`setup`](api:utils.html#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-) functions.

</div>

<div class="paragraph">

Using custom hashing functions is a sensitive operation. After setup, it requires to keep using the same hashing function for every new value pushed to the tree to avoid corrupting the tree. For this reason, it’s a good practice to keep your hashing function static in your implementation contract as follows:

</div>

<div class="listingblock">

<div class="content">

``` highlight
using MerkleTree for MerkleTree.Bytes32PushTree;
MerkleTree.Bytes32PushTree private _tree;

function setup(uint8 _depth, bytes32 _zero) public /* onlyOwner */ {
    root = _tree.setup(_depth, _zero, _hashFn);
}

function push(bytes32 leaf) public /* onlyOwner */ {
    (uint256 leafIndex, bytes32 currentRoot) = _tree.push(leaf, _hashFn);
    // Store the new root.
}

function _hashFn(bytes32 a, bytes32 b) internal view returns(bytes32) {
    // Custom hash function implementation
    // Kept as an internal implementation detail to
    // guarantee the same function is always used
}
```

</div>

</div>

</div>

<div class="sect2">

### Using a Heap

<div class="paragraph">

A [binary heap](https://en.wikipedia.org/wiki/Binary_heap) is a data structure that always stores the most important element at its peak and it can be used as a priority queue.

</div>

<div class="paragraph">

To define what is most important in a heap, these frequently take comparator functions that tell the binary heap whether a value has more relevance than another.

</div>

<div class="paragraph">

OpenZeppelin Contracts implements a Heap data structure with the properties of a binary heap. The heap uses the [`lt`](api:utils.html#Comparators-lt-uint256-uint256-) function by default but allows to customize its comparator.

</div>

<div class="paragraph">

When using a custom comparator, it’s recommended to wrap your function to avoid the possibility of mistakenly using a different comparator function:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function pop(Uint256Heap storage self) internal returns (uint256) {
    return pop(self, Comparators.gt);
}

function insert(Uint256Heap storage self, uint256 value) internal {
    insert(self, value, Comparators.gt);
}

function replace(Uint256Heap storage self, uint256 newValue) internal returns (uint256) {
    return replace(self, newValue, Comparators.gt);
}
```

</div>

</div>

</div>

</div>

</div>

<div class="sect1">

## Misc

<div class="sectionbody">

<div class="sect2">

### Packing

<div class="paragraph">

The storage in the EVM is shaped in chunks of 32 bytes, each of this chunks is known as a *slot*, and can hold multiple values together as long as these values don’t exceed its size. These properties of the storage allow for a technique known as *packing*, that consists of placing values together on a single storage slot to reduce the costs associated to reading and writing to multiple slots instead of just one.

</div>

<div class="paragraph">

Commonly, developers pack values using structs that place values together so they fit better in storage. However, this approach requires to load such struct from either calldata or memory. Although sometimes necessary, it may be useful to pack values in a single slot and treat it as a packed value without involving calldata or memory.

</div>

<div class="paragraph">

The [`Packing`](api:utils.html#Packing) library is a set of utilities for packing values that fit in 32 bytes. The library includes 3 main functionalities:

</div>

<div class="ulist">

- Packing 2 `bytesXX` values

- Extracting a packed `bytesXX` value from a `bytesYY`

- Replacing a packed `bytesXX` value from a `bytesYY`

</div>

<div class="paragraph">

With these primitives, one can build custom functions to create custom packed types. For example, suppose you need to pack an `address` of 20 bytes with a `bytes4` selector and an `uint64` time period:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function _pack(address account, bytes4 selector, uint64 period) external pure returns (bytes32) {
    bytes12 subpack = Packing.pack_4_8(selector, bytes8(period));
    return Packing.pack_20_12(bytes20(account), subpack);
}

function _unpack(bytes32 pack) external pure returns (address, bytes4, uint64) {
    return (
        address(Packing.extract_32_20(pack, 0)),
        Packing.extract_32_4(pack, 20),
        uint64(Packing.extract_32_8(pack, 24))
    );
}
```

</div>

</div>

</div>

<div class="sect2">

### Storage Slots

<div class="paragraph">

Solidity allocates a storage pointer for each variable declared in a contract. However, there are cases when it’s required to access storage pointers that can’t be derived by using regular Solidity. For those cases, the [`StorageSlot`](api:utils.html#StorageSlot) library allows for manipulating storage slots directly.

</div>

<div class="listingblock">

<div class="content">

``` highlight
bytes32 internal constant _IMPLEMENTATION_SLOT = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;

function _getImplementation() internal view returns (address) {
    return StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value;
}

function _setImplementation(address newImplementation) internal {
    require(newImplementation.code.length > 0);
    StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value = newImplementation;
}
```

</div>

</div>

<div class="paragraph">

The [`TransientSlot`](api:utils.html#TransientSlot) library supports transient storage through user defined value types ([UDVTs](https://docs.soliditylang.org/en/latest/types.html#user-defined-value-types)), which enables the same value types as in Solidity.

</div>

<div class="listingblock">

<div class="content">

``` highlight
bytes32 internal constant _LOCK_SLOT = 0xf4678858b2b588224636b8522b729e7722d32fc491da849ed75b3fdf3c84f542;

function _getTransientLock() internal view returns (bool) {
    return _LOCK_SLOT.asBoolean().tload();
}

function _setTransientLock(bool lock) internal {
    _LOCK_SLOT.asBoolean().tstore(lock);
}
```

</div>

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
<td class="content">Manipulating storage slots directly is an advanced practice. Developers MUST make sure that the storage pointer is not colliding with other variables.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

One of the most common use cases for writing directly to storage slots is ERC-7201 for namespaced storage, which is guaranteed to not collide with other storage slots derived by Solidity.

</div>

<div class="paragraph">

Users can leverage this standard using the [`SlotDerivation`](api:utils.html#SlotDerivation) library.

</div>

<div class="listingblock">

<div class="content">

``` highlight
using SlotDerivation for bytes32;
string private constant _NAMESPACE = "<namespace>" // eg. example.main

function erc7201Pointer() internal view returns (bytes32) {
    return _NAMESPACE.erc7201Slot();
}
```

</div>

</div>

</div>

<div class="sect2">

### Base64

<div class="paragraph">

[`Base64`](api:utils.html#Base64) util allows you to transform `bytes32` data into its Base64 `string` representation.

</div>

<div class="paragraph">

This is especially useful for building URL-safe tokenURIs for both [`ERC-721`](api:token/ERC721.html#IERC721Metadata-tokenURI-uint256-) or [`ERC-1155`](api:token/ERC1155.html#IERC1155MetadataURI-uri-uint256-). This library provides a clever way to serve URL-safe [Data URI](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs/) compliant strings to serve on-chain data structures.

</div>

<div class="paragraph">

Here is an example to send JSON Metadata through a Base64 Data URI using an ERC-721:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$utilities/Base64NFT.sol[role=include]
```

</div>

</div>

</div>

<div class="sect2">

### Multicall

<div class="paragraph">

The `Multicall` abstract contract comes with a `multicall` function that bundles together multiple calls in a single external call. With it, external accounts may perform atomic operations comprising several function calls. This is not only useful for EOAs to make multiple calls in a single transaction, it’s also a way to revert a previous call if a later one fails.

</div>

<div class="paragraph">

Consider this dummy contract:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$utilities/Multicall.sol[role=include]
```

</div>

</div>

<div class="paragraph">

This is how to call the `multicall` function using Ethers.js, allowing `foo` and `bar` to be called in a single transaction:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// scripts/foobar.js

const instance = await ethers.deployContract("Box");

await instance.multicall([
    instance.interface.encodeFunctionData("foo"),
    instance.interface.encodeFunctionData("bar")
]);
```

</div>

</div>

</div>

<div class="sect2">

### Memory

<div class="paragraph">

The [`Memory`](api:utils.html#Memory) library provides functions for advanced use cases that require granular memory management. A common use case is to avoid unnecessary memory expansion costs when performing repeated operations that allocate memory in a loop. Consider the following example:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function processMultipleItems(uint256[] memory items) internal {
  for (uint256 i = 0; i < items.length; i++) {
    bytes memory tempData = abi.encode(items[i], block.timestamp);
    // Process tempData...
  }
}
```

</div>

</div>

<div class="paragraph">

Note that each iteration allocates new memory for `tempData`, causing the memory to expand continuously. This can be optimized by resetting the memory pointer between iterations:

</div>

<div class="listingblock">

<div class="content">

``` highlight
function processMultipleItems(uint256[] memory items) internal {
  Memory.Pointer ptr = Memory.getFreeMemoryPointer(); // Cache pointer
  for (uint256 i = 0; i < items.length; i++) {
    bytes memory tempData = abi.encode(items[i], block.timestamp);
    // Process tempData...
    Memory.setFreeMemoryPointer(ptr); // Reset pointer for reuse
  }
}
```

</div>

</div>

<div class="paragraph">

This way, memory allocated for `tempData` in each iteration is reused, significantly reducing memory expansion costs when processing many items.

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
<td class="content">Only use these functions after carefully confirming they’re necessary. By default, Solidity handles memory safely. Using this library without understanding memory layout and safety may be dangerous. See the <a href="https://docs.soliditylang.org/en/v0.8.20/internals/layout_in_memory.html">memory layout</a> and <a href="https://docs.soliditylang.org/en/v0.8.20/assembly.html#memory-safety">memory safety</a> documentation for details.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Historical Block Hashes

<div class="paragraph">

[`Blockhash`](api:utils.html#Blockhash) provides L2 protocol developers with extended access to historical block hashes beyond Ethereum’s native 256-block limit. By leveraging [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)'s history storage contract, the library enables access to block hashes up to 8,191 blocks in the past, making it invaluable for L2 fraud proofs and state verification systems.

</div>

<div class="paragraph">

The library seamlessly combines native `BLOCKHASH` opcode access for recent blocks (≤256) with EIP-2935 history storage queries for older blocks (257-8,191). It handles edge cases gracefully by returning zero for future blocks or those beyond the history window, matching the EVM’s behavior. The implementation uses gas-efficient assembly for static calls to the history storage contract.

</div>

<div class="listingblock">

<div class="content">

``` highlight
contract L1Inbox {
    using Blockhash for uint256;

    function verifyBlockHash(uint256 blockNumber, bytes32 expectedHash) public view returns (bool) {
        return blockNumber.blockHash() == expectedHash;
    }
}
```

</div>

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
<td class="content">After EIP-2935 activation, it takes 8,191 blocks to completely fill the history storage. Before that, only block hashes since the fork block will be available.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Time

<div class="paragraph">

The [`Time`](api:utils.html#Time) library provides helpers for manipulating time-related objects in a type-safe manner. It uses `uint48` for timepoints and `uint32` for durations, helping to reduce gas costs while providing adequate precision.

</div>

<div class="paragraph">

One of its key features is the `Delay` type, which represents a duration that can automatically change its value at a specified point in the future while maintaining delay guarantees. For example, when reducing a delay value (e.g., from 7 days to 1 day), the change only takes effect after the difference between the old and new delay (i.e. a 6 days) or a minimum setback period, preventing an attacker who gains admin access from immediately reducing security timeouts and executing sensitive operations. This is particularly useful for governance and security mechanisms where timelock periods need to be enforced.

</div>

<div class="paragraph">

Consider this example for using and safely updating Delays:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {Time} from "contracts/utils/types/Time.sol";

contract MyDelayedContract {
    using Time for *;

    Time.Delay private _delay;

    constructor() {
        _delay = Time.toDelay(3 days);
    }

    function schedule(bytes32 operationId) external {
        // Get the current `_delay` value, respecting any pending delay changes if they've taken effect
        uint32 currentDelay = _delay.get();
        uint48 executionTime = Time.timestamp() + currentDelay;

        // ... schedule the operation at `executionTime`
    }

    function execute(bytes32 operationId) external {
        uint48 executionTime = getExecutionTime(operationId);
        require(executionTime > 0, "Operation not scheduled");
        require(Time.timestamp() >= executionTime, "Delay not elapsed yet");

        // ... execute the operation
    }

    // Update the delay with `Time`'s safety mechanism
    function updateDelay(uint32 newDelay) external {
        (Time.Delay updatedDelay, uint48 effect) = _delay.withUpdate(
            newDelay,    // The new delay value
            5 days       // Minimum setback if reducing the delay
        );

        _delay = updatedDelay;

        // ... emit events
    }

    // Get complete delay details including pending changes
    function getDelayDetails() external view returns (
        uint32 currentValue, // The current delay value
        uint32 pendingValue, // The pending delay value
        uint48 effectTime    // The timepoint when the pending delay change takes effect
    ) {
        return _delay.getFull();
    }
}
```

</div>

</div>

<div class="paragraph">

This pattern is used extensively in OpenZeppelin’s [AccessManager](api:access.html#AccessManager) for implementing secure time-based access control. For example, when changing an admin delay:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// From AccessManager.sol
function _setTargetAdminDelay(address target, uint32 newDelay) internal virtual {
    uint48 effect;
    (_targets[target].adminDelay, effect) = _targets[target].adminDelay.withUpdate(
        newDelay,
        minSetback()
    );

    emit TargetAdminDelayUpdated(target, newDelay, effect);
}
```

</div>

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
