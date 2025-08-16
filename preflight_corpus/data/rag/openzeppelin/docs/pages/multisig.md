<div id="header">

# Multisig Account

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

A multi-signature (multisig) account is a smart account that requires multiple authorized signers to approve operations before execution. Unlike traditional accounts controlled by a single private key, multisigs distribute control among multiple parties, eliminating single points of failure. For example, a 2-of-3 multisig requires signatures from at least 2 out of 3 possible signers.

</div>

<div class="paragraph">

Popular implementations like [Safe](https://safe.global/) (formerly Gnosis Safe) have become the standard for securing valuable assets. Multisigs provide enhanced security through collective authorization, customizable controls for ownership and thresholds, and the ability to rotate signers without changing the account address.

</div>

</div>

</div>

<div class="sect1">

## Beyond Standard Signature Verification

<div class="sectionbody">

<div class="paragraph">

As discussed in the [accounts section](accounts.html#signature_validation), the standard approach for smart contracts to verify signatures is [ERC-1271](https://eips.ethereum.org/EIPS/eip-1271), which defines an `isValidSignature(hash, signature)`. However, it is limited in two important ways:

</div>

<div class="olist arabic">

1.  It assumes the signer has an EVM address

2.  It treats the signer as a single identity

</div>

<div class="paragraph">

This becomes problematic when implementing multisig accounts where:

</div>

<div class="ulist">

- You may want to use signers that don’t have EVM addresses (like keys from hardware devices)

- Each signer needs to be individually verified rather than treated as a collective identity

- You need a threshold system to determine when enough valid signatures are present

</div>

<div class="paragraph">

The [SignatureChecker](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/SignatureChecker.sol) library is useful for verifying EOA and ERC-1271 signatures, but it’s not designed for more complex arrangements like threshold-based multisigs.

</div>

</div>

</div>

<div class="sect1">

## ERC-7913 Signers

<div class="sectionbody">

<div class="paragraph">

[ERC-7913](https://eips.ethereum.org/EIPS/eip-7913) extends the concept of signer representation to include keys that don’t have EVM addresses, addressing this limitation. OpenZeppelin implements this standard through three contracts:

</div>

<div class="sect2">

### SignerERC7913

<div class="paragraph">

The [`SignerERC7913`](api:utils.html#SignerERC7913) contract allows a single ERC-7913 formatted signer to control an account. The signer is represented as a `bytes` object that concatenates a verifier address and a key: `verifier || key`.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// contracts/MyAccountERC7913.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.24;

import {Account} from "@openzeppelin/community-contracts/account/Account.sol";
import {EIP712} from "@openzeppelin/contracts/utils/cryptography/EIP712.sol";
import {ERC721Holder} from "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import {ERC1155Holder} from "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";
import {ERC7739} from "@openzeppelin/community-contracts/utils/cryptography/signers/ERC7739.sol";
import {ERC7821} from "@openzeppelin/community-contracts/account/extensions/ERC7821.sol";
import {Initializable} from "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import {SignerERC7913} from "@openzeppelin/community-contracts/utils/cryptography/signers/SignerERC7913.sol";

contract MyAccountERC7913 is Account, SignerERC7913, ERC7739, ERC7821, ERC721Holder, ERC1155Holder, Initializable {
    constructor() EIP712("MyAccount7913", "1") {}

    function initialize(bytes memory signer) public initializer {
        _setSigner(signer);
    }

    function setSigner(bytes memory signer) public onlyEntryPointOrSelf {
        _setSigner(signer);
    }

    /// @dev Allows the entry point as an authorized executor.
    function _erc7821AuthorizedExecutor(
        address caller,
        bytes32 mode,
        bytes calldata executionData
    ) internal view virtual override returns (bool) {
        return caller == address(entryPoint()) || super._erc7821AuthorizedExecutor(caller, mode, executionData);
    }
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
<td class="content">Leaving an account uninitialized may leave it unusable since no public key was associated with it.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### MultiSignerERC7913

<div class="paragraph">

The [`MultiSignerERC7913`](api:utils/cryptography.html#MultiSignerERC7913) contract extends this concept to support multiple signers with a threshold-based signature verification system.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// contracts/MyAccountMultiSigner.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.27;

import {Account} from "@openzeppelin/community-contracts/account/Account.sol";
import {EIP712} from "@openzeppelin/contracts/utils/cryptography/EIP712.sol";
import {ERC721Holder} from "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import {ERC1155Holder} from "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";
import {ERC7739} from "@openzeppelin/community-contracts/utils/cryptography/signers/ERC7739.sol";
import {ERC7821} from "@openzeppelin/community-contracts/account/extensions/ERC7821.sol";
import {Initializable} from "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import {MultiSignerERC7913} from "@openzeppelin/community-contracts/utils/cryptography/signers/MultiSignerERC7913.sol";

contract MyAccountMultiSigner is
    Account,
    MultiSignerERC7913,
    ERC7739,
    ERC7821,
    ERC721Holder,
    ERC1155Holder,
    Initializable
{
    constructor() EIP712("MyAccountMultiSigner", "1") {}

    function initialize(bytes[] memory signers, uint256 threshold) public initializer {
        _addSigners(signers);
        _setThreshold(threshold);
    }

    function addSigners(bytes[] memory signers) public onlyEntryPointOrSelf {
        _addSigners(signers);
    }

    function removeSigners(bytes[] memory signers) public onlyEntryPointOrSelf {
        _removeSigners(signers);
    }

    function setThreshold(uint256 threshold) public onlyEntryPointOrSelf {
        _setThreshold(threshold);
    }

    /// @dev Allows the entry point as an authorized executor.
    function _erc7821AuthorizedExecutor(
        address caller,
        bytes32 mode,
        bytes calldata executionData
    ) internal view virtual override returns (bool) {
        return caller == address(entryPoint()) || super._erc7821AuthorizedExecutor(caller, mode, executionData);
    }
}
```

</div>

</div>

<div class="paragraph">

This implementation is ideal for standard multisig setups where each signer has equal authority, and a fixed number of approvals is required.

</div>

<div class="paragraph">

The `MultiSignerERC7913` contract provides several key features for managing multi-signature accounts. It maintains a set of authorized signers and implements a threshold-based system that requires a minimum number of signatures to approve operations. The contract includes an internal interface for managing signers, allowing for the addition and removal of authorized parties.

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
<td class="content"><code>MultiSignerERC7913</code> safeguards to ensure that the threshold remains achievable based on the current number of active signers, preventing situations where operations could become impossible to execute.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

The contract also provides public functions for querying signer information: [`isSigner(bytes memory signer)`](api:utils/cryptography.html#MultiSignerERC7913-isSigner-bytes-) to check if a given signer is authorized, [`getSigners(uint64 start, uint64 end)`](api:utils/cryptography.html#MultiSignerERC7913-getSigners-uint64-uint64-) to retrieve a paginated list of authorized signers, and [`getSignerCount()`](api:utils/cryptography.html#MultiSignerERC7913-getSignerCount) to get the total number of signers. These functions are useful when validating signatures, implementing customized access control logic, or building user interfaces that need to display signer information.

</div>

</div>

<div class="sect2">

### MultiSignerERC7913Weighted

<div class="paragraph">

For more sophisticated governance structures, the [`MultiSignerERC7913Weighted`](api:utils/cryptography.html#MultiSignerERC7913Weighted) contract extends `MultiSignerERC7913` by assigning different weights to each signer.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// contracts/MyAccountMultiSignerWeighted.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.27;

import {Account} from "@openzeppelin/community-contracts/account/Account.sol";
import {EIP712} from "@openzeppelin/contracts/utils/cryptography/EIP712.sol";
import {ERC721Holder} from "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import {ERC1155Holder} from "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";
import {ERC7739} from "@openzeppelin/community-contracts/utils/cryptography/signers/ERC7739.sol";
import {ERC7821} from "@openzeppelin/community-contracts/account/extensions/ERC7821.sol";
import {Initializable} from "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import {MultiSignerERC7913Weighted} from "@openzeppelin/community-contracts/utils/cryptography/signers/MultiSignerERC7913Weighted.sol";

contract MyAccountMultiSignerWeighted is
    Account,
    MultiSignerERC7913Weighted,
    ERC7739,
    ERC7821,
    ERC721Holder,
    ERC1155Holder,
    Initializable
{
    constructor() EIP712("MyAccountMultiSignerWeighted", "1") {}

    function initialize(bytes[] memory signers, uint256[] memory weights, uint256 threshold) public initializer {
        _addSigners(signers);
        _setSignerWeights(signers, weights);
        _setThreshold(threshold);
    }

    function addSigners(bytes[] memory signers) public onlyEntryPointOrSelf {
        _addSigners(signers);
    }

    function removeSigners(bytes[] memory signers) public onlyEntryPointOrSelf {
        _removeSigners(signers);
    }

    function setThreshold(uint256 threshold) public onlyEntryPointOrSelf {
        _setThreshold(threshold);
    }

    function setSignerWeights(bytes[] memory signers, uint256[] memory weights) public onlyEntryPointOrSelf {
        _setSignerWeights(signers, weights);
    }

    /// @dev Allows the entry point as an authorized executor.
    function _erc7821AuthorizedExecutor(
        address caller,
        bytes32 mode,
        bytes calldata executionData
    ) internal view virtual override returns (bool) {
        return caller == address(entryPoint()) || super._erc7821AuthorizedExecutor(caller, mode, executionData);
    }
}
```

</div>

</div>

<div class="paragraph">

This implementation is perfect for scenarios where different signers should have varying levels of authority, such as:

</div>

<div class="ulist">

- Board members with different voting powers

- Organizational structures with hierarchical decision-making

- Hybrid governance systems combining core team and community members

- Execution setups like "social recovery" where you trust particular guardians more than others

</div>

<div class="paragraph">

The `MultiSignerERC7913Weighted` contract extends `MultiSignerERC7913` with a weighting system. Each signer can have a custom weight, and operations require the total weight of signing participants to meet or exceed the threshold. Signers without explicit weights default to a weight of 1.

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
<td class="content">When setting up a weighted multisig, ensure the threshold value matches the scale used for signer weights. For example, if signers have weights like 1, 2, or 3, then a threshold of 4 would require at least two signers (e.g., one with weight 1 and one with weight 3).</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="sect1">

## Setting Up a Multisig Account

<div class="sectionbody">

<div class="paragraph">

To create a multisig account, you need to:

</div>

<div class="olist arabic">

1.  Define your signers

2.  Determine your threshold

3.  Initialize your account with these parameters

</div>

<div class="paragraph">

The example below demonstrates setting up a 2-of-3 multisig account with different types of signers:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Example setup code
function setupMultisigAccount() external {
    // Create signers using different types of keys
    bytes memory ecdsaSigner = alice; // EOA address (20 bytes)

    // P256 signer with format: verifier || pubKey
    bytes memory p256Signer = abi.encodePacked(
        p256Verifier,
        bobP256PublicKeyX,
        bobP256PublicKeyY
    );

    // RSA signer with format: verifier || pubKey
    bytes memory rsaSigner = abi.encodePacked(
        rsaVerifier,
        abi.encode(charlieRSAPublicKeyE, charlieRSAPublicKeyN)
    );

    // Create array of signers
    bytes[] memory signers = new bytes[](3);
    signers[0] = ecdsaSigner;
    signers[1] = p256Signer;
    signers[2] = rsaSigner;

    // Set threshold to 2 (2-of-3 multisig)
    uint256 threshold = 2;

    // Initialize the account
    myMultisigAccount.initialize(signers, threshold);
}
```

</div>

</div>

<div class="paragraph">

For a weighted multisig, you would also specify weights:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Example setup for weighted multisig
function setupWeightedMultisigAccount() external {
    // Create array of signers (same as above)
    bytes[] memory signers = new bytes[](3);
    signers[0] = ecdsaSigner;
    signers[1] = p256Signer;
    signers[2] = rsaSigner;

    // Assign weights to signers (Alice:1, Bob:2, Charlie:3)
    uint256[] memory weights = new uint256[](3);
    weights[0] = 1;
    weights[1] = 2;
    weights[2] = 3;

    // Set threshold to 4 (requires at least Bob+Charlie or all three)
    uint256 threshold = 4;

    // Initialize the weighted account
    myWeightedMultisigAccount.initialize(signers, weights, threshold);
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
<td class="content">The <a href="api:utils/cryptography.html#MultiSignerERC7913-_validateReachableThreshold--"><code>_validateReachableThreshold</code></a> function ensures that the sum of weights for all active signers meets or exceeds the threshold. Any customization built on top of the multisigner contracts must ensure the threshold is always reachable.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

For multisig accounts, the signature is a complex structure that contains both the signers and their individual signatures. The format follows ERC-7913’s specification and must be properly encoded.

</div>

<div class="sect2">

### Signature Format

<div class="paragraph">

The multisig signature is encoded as:

</div>

<div class="listingblock">

<div class="content">

``` highlight
abi.encode(
    bytes[] signers,   // Array of signers sorted by `keccak256`
    bytes[] signatures // Array of signatures corresponding to each signer
)
```

</div>

</div>

<div class="paragraph">

Where:

</div>

<div class="ulist">

- `signers` is an array of the signers participating in this particular signature

- `signatures` is an array of the individual signatures corresponding to each signer

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
<p>To avoid duplicate signers, the contract uses <code>keccak256</code> to generate a unique id for each signer. When providing a multisignature, the <code>signers</code> array should be sorted in ascending order by <code>keccak256</code>, and the <code>signatures</code> array must match the order of their corresponding signers.</p>
</div></td>
</tr>
</tbody>
</table>

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
