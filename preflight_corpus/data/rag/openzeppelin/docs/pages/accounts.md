<div id="header">

# Smart Accounts

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

OpenZeppelin provides a simple [`Account`](api:account.html#Account) implementation including only the basic logic to handle user operations in compliance with ERC-4337. Developers who want to build their own account can leverage it to bootstrap custom implementations.

</div>

<div class="paragraph">

User operations are validated using an [`AbstractSigner`](api:utils.html#AbstractSigner), which requires to implement the internal [`_rawSignatureValidation`](api:utils.html#AbstractSigner-_rawSignatureValidation-bytes32-bytes-) function, of which we offer a set of implementations to cover a wide customization range. This is the lowest-level signature validation layer and is used to wrap other validation methods like the Account’s [`validateUserOp`](api:account.html#Account-validateUserOp-struct-PackedUserOperation-bytes32-uint256-).

</div>

</div>

</div>

<div class="sect1">

## Setting up an account

<div class="sectionbody">

<div class="paragraph">

To setup an account, you can either start configuring it using our Wizard and selecting a predefined validation scheme, or bring your own logic and start by inheriting [`Account`](api:account.html#Account) from scratch.

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
<td class="content">Accounts don’t support <a href="erc721.html">ERC-721</a> and <a href="erc1155.html">ERC-1155</a> tokens natively since these require the receiving address to implement an acceptance check. It is recommended to inherit <a href="api:token/ERC721.html#ERC721Holder">ERC721Holder</a>, <a href="api:token/ERC1155.html#ERC1155Holder">ERC1155Holder</a> to include these checks in your account.</td>
</tr>
</tbody>
</table>

</div>

<div class="sect2">

### Selecting a signer

<div class="paragraph">

Since the minimum requirement of [`Account`](api:account.html#Account) is to provide an implementation of [`_rawSignatureValidation`](api:utils/cryptography.html#AbstractSigner-_rawSignatureValidation-bytes32-bytes-), the library includes specializations of the `AbstractSigner` contract that use custom digital signature verification algorithms. Some examples that you can select from include:

</div>

<div class="ulist">

- [`SignerECDSA`](api:utils/cryptography.html#SignerECDSA): Verifies signatures produced by regular EVM Externally Owned Accounts (EOAs).

- [`SignerP256`](api:utils/cryptography.html#SignerP256): Validates signatures using the secp256r1 curve, common for World Wide Web Consortium (W3C) standards such as FIDO keys, passkeys or secure enclaves.

- [`SignerRSA`](api:utils/cryptography.html#SignerRSA): Verifies signatures of traditional PKI systems and X.509 certificates.

- [`SignerERC7702`](api:utils/cryptography.html#SignerERC7702): Checks EOA signatures delegated to this signer using [EIP-7702 authorizations](https://eips.ethereum.org/EIPS/eip-7702#set-code-transaction)

- [`SignerERC7913`](api:utils/cryptography.html#SignerERC7913): Verifies generalized signatures following [ERC-7913](https://eips.ethereum.org/EIPS/eip-7913).

- [`SignerZKEmail`](https://docs.openzeppelin.com/community-contracts/0.0.1/api/utils#SignerZKEmail): Enables email-based authentication for smart contracts using zero knowledge proofs of email authority signatures.

- [`MultiSignerERC7913`](api:utils/cryptography.html#MultiSignerERC7913): Allows using multiple ERC-7913 signers with a threshold-based signature verification system.

- [`MultiSignerERC7913Weighted`](api:utils/cryptography.html#MultiSignerERC7913Weighted): Overrides the threshold mechanism of [`MultiSignerERC7913`](api:utils/cryptography.html#MultiSignerERC7913), offering different weights per signer.

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
<td class="content">Given <a href="api:utils/cryptography.html#SignerERC7913"><code>SignerERC7913</code></a> provides a generalized standard for signature validation, you don’t need to implement your own <a href="api:utils/cryptography.html#AbstractSigner"><code>AbstractSigner</code></a> for different signature schemes, consider bringing your own ERC-7913 verifier instead.</td>
</tr>
</tbody>
</table>

</div>

<div class="sect3">

#### Accounts factory

<div class="paragraph">

The first time you send an user operation, your account will be created deterministically (i.e. its code and address can be predicted) using the the `initCode` field in the UserOperation. This field contains both the address of a smart contract (the factory) and the data required to call it and create your smart account.

</div>

<div class="paragraph">

Suggestively, you can create your own account factory using the [Clones library](api:proxy.html#Clones), taking advantage of decreased deployment costs and account address predictability.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$account/MyFactoryAccount.sol[role=include]
```

</div>

</div>

<div class="paragraph">

Account factories should be carefully implemented to ensure the account address is deterministically tied to the initial owners. This prevents frontrunning attacks where a malicious actor could deploy the account with their own owners before the intended owner does. The factory should include the owner’s address in the salt used for address calculation.

</div>

</div>

<div class="sect3">

#### Handling initialization

<div class="paragraph">

Most smart accounts are deployed by a factory, the best practice is to create [minimal clones](api:proxy.html#minimal_clones) of initializable contracts. These signer implementations provide an initializable design by default so that the factory can interact with the account to set it up right after deployment in a single transaction.

</div>

<div class="listingblock">

<div class="content">

``` highlight
import {Account} from "@openzeppelin/community-contracts/account/Account.sol";
import {Initializable} from "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import {SignerECDSA} from "@openzeppelin/community-contracts/utils/cryptography/SignerECDSA.sol";

contract MyAccount is Initializable, Account, SignerECDSA, ... {
    // ...

    function initializeECDSA(address signer) public initializer {
        _setSigner(signer);
    }
}
```

</div>

</div>

<div class="paragraph">

Note that some account implementations may be deployed directly and therefore, won’t require a factory.

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

</div>

<div class="sect2">

### Signature validation

<div class="paragraph">

Regularly, accounts implement [ERC-1271](https://eips.ethereum.org/EIPS/eip-1271) to enable smart contract signature verification given its wide adoption. To be compliant means that smart contract exposes an [`isValidSignature(bytes32 hash, bytes memory signature)`](api:interfaces.html#IERC1271-isValidSignature-bytes32-bytes-) method that returns `0x1626ba7e` to identify whether the signature is valid.

</div>

<div class="paragraph">

The benefit of this standard is that it allows to receive any format of `signature` for a given `hash`. This generalized mechanism fits very well with the account abstraction principle of *bringing your own validation mechanism*.

</div>

<div class="paragraph">

This is how you enable ERC-1271 using an [`AbstractSigner`](api:utils/cryptography.html#AbstractSigner):

</div>

<div class="listingblock">

<div class="content">

``` highlight
function isValidSignature(bytes32 hash, bytes calldata signature) public view override returns (bytes4) {
    return _rawSignatureValidation(hash, signature) ? IERC1271.isValidSignature.selector : bytes4(0xffffffff);
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
<td class="content">We recommend using <a href="api:utils/cryptography.html#ERC7739">ERC7739</a> to avoid replayability across accounts. This defensive rehashing mechanism that prevents signatures for this account to be replayed in another account controlled by the same signer. See <a href="#erc_7739_signatures">ERC-7739 signatures</a>.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Batched execution

<div class="paragraph">

Batched execution allows accounts to execute multiple calls in a single transaction, which is particularly useful for bundling operations that need to be atomic. This is especially valuable in the context of account abstraction where you want to minimize the number of user operations and associated gas costs. [`ERC-7821`](api:account.html#ERC7821) standard provides a minimal interface for batched execution.

</div>

<div class="paragraph">

The library implementation supports a single batch mode (`0x01000000000000000000`) and allows accounts to execute multiple calls atomically. The standard includes access control through the [`_erc7821AuthorizedExecutor`](api:account.html#ERC7821-_erc7821AuthorizedExecutor-address-bytes32-bytes-) function, which by default only allows the contract itself to execute batches.

</div>

<div class="paragraph">

Here’s an example of how to use batched execution using EIP-7702:

</div>

<div class="listingblock">

<div class="content">

``` highlight
import {Account} from "@openzeppelin/community-contracts/account/Account.sol";
import {ERC7821} from "@openzeppelin/community-contracts/account/extensions/draft-ERC7821.sol";
import {SignerERC7702} from "@openzeppelin/community-contracts/utils/cryptography/SignerERC7702.sol";

contract MyAccount is Account, SignerERC7702, ERC7821 {
    // Override to allow the entrypoint to execute batches
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

The batched execution data follows a specific format that includes the calls to be executed. This format follows the same format as [ERC-7579 execution](https://eips.ethereum.org/EIPS/eip-7579#execution-behavior) but only supports `0x01` call type (i.e. batched `call`) and default execution type (i.e. reverts if at least one subcall does).

</div>

<div class="paragraph">

To encode an ERC-7821 batch, you can use [viem](https://viem.sh/)'s utilities:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// CALL_TYPE_BATCH, EXEC_TYPE_DEFAULT, ..., selector, payload
const mode = encodePacked(
  ["bytes1", "bytes1", "bytes4", "bytes4", "bytes22"],
  ["0x01", "0x00", "0x00000000", "0x00000000", "0x00000000000000000000000000000000000000000000"]
);

const entries = [
  {
    target: "0x000...0001",
    value: 0n,
    data: "0x000...000",
  },
  {
    target: "0x000...0002",
    value: 0n,
    data: "0x000...000",
  }
];

const batch = encodeAbiParameters(
  [parseAbiParameter("(address,uint256,bytes)[]")],
  [
    entries.map<[Address, bigint, Hex]>((entry) =>
      [entry.target, entry.value ?? 0n, entry.data ?? "0x"]
    ),
  ]
);

const userOpData = encodeFunctionData({
    abi: account.abi,
    functionName: "execute",
    args: [mode, batch]
});
```

</div>

</div>

</div>

</div>

</div>

<div class="sect1">

## Bundle a `UserOperation`

<div class="sectionbody">

<div class="paragraph">

[UserOperations](account-abstraction.html#useroperation) are a powerful abstraction layer that enable more sophisticated transaction capabilities compared to traditional Ethereum transactions. To get started, you’ll need to an account, which you can get by [deploying a factory](#accounts_factory) for your implementation.

</div>

<div class="sect2">

### Preparing a UserOp

<div class="paragraph">

A UserOperation is a struct that contains all the necessary information for the EntryPoint to execute your transaction. You’ll need the `sender`, `nonce`, `accountGasLimits` and `callData` fields to construct a `PackedUserOperation` that can be signed later (to populate the `signature` field).

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
<td class="content">Specify <code>paymasterAndData</code> with the address of a paymaster contract concatenated to <code>data</code> that will be passed to the paymaster’s validatePaymasterUserOp function to support sponsorship as part of your user operation.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Here’s how to prepare one using [viem](https://viem.sh/):

</div>

<div class="listingblock">

<div class="content">

``` highlight
import { getContract, createWalletClient, http, Hex } from 'viem';

const walletClient = createWalletClient({
  account, // See Viem's `privateKeyToAccount`
  chain, // import { ... } from 'viem/chains';
  transport: http(),
})

const entrypoint = getContract({
  abi: [/* ENTRYPOINT ABI */],
  address: '0x<ENTRYPOINT_ADDRESS>',
  client: walletClient,
});

const userOp = {
  sender: '0x<YOUR_ACCOUNT_ADDRESS>',
  nonce: await entrypoint.read.getNonce([sender, 0n]),
  initCode: "0x" as Hex,
  callData: '0x<CALLDATA_TO_EXECUTE_IN_THE_ACCOUNT>',
  accountGasLimits: encodePacked(
    ["uint128", "uint128"],
    [
      100_000n, // verificationGasLimit
      300_000n, // callGasLimit
    ]
  ),
  preVerificationGas: 50_000n,
  gasFees: encodePacked(
    ["uint128", "uint128"],
    [
      0n, // maxPriorityFeePerGas
      0n, // maxFeePerGas
    ]
  ),
  paymasterAndData: "0x" as Hex,
  signature: "0x" as Hex,
};
```

</div>

</div>

<div class="paragraph">

In case your account hasn’t been deployed yet, make sure to provide the `initCode` field as `abi.encodePacked(factory, factoryData)` to deploy the account within the same UserOp:

</div>

<div class="listingblock">

<div class="content">

``` highlight
const deployed = await publicClient.getCode({ address: predictedAddress });

if (!deployed) {
  userOp.initCode = encodePacked(
    ["address", "bytes"],
    [
      '0x<ACCOUNT_FACTORY_ADDRESS>',
      encodeFunctionData({
        abi: [/* ACCOUNT ABI */],
        functionName: "<FUNCTION NAME>",
        args: [...],
      }),
    ]
  );
}
```

</div>

</div>

<div class="sect3">

#### Estimating gas

<div class="paragraph">

To calculate gas parameters of a `UserOperation`, developers should carefully consider the following fields:

</div>

<div class="ulist">

- `verificationGasLimit`: This covers the gas costs for signature verification, paymaster validation (if used), and account validation logic. While a typical value is around 100,000 gas units, this can vary significantly based on the complexity of your signature validation scheme in both the account and paymaster contracts.

- `callGasLimit`: This parameter accounts for the actual execution of your account’s logic. It’s recommended to use `eth_estimateGas` for each subcall and add additional buffer for computational overhead.

- `preVerificationGas`: This compensates for the EntryPoint’s execution overhead. While 50,000 gas is a reasonable starting point, you may need to increase this value based on your UserOperation’s size and specific bundler requirements.

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
<td class="content">The <code>maxFeePerGas</code> and <code>maxPriorityFeePerGas</code> values are typically provided by your bundler service, either through their SDK or a custom RPC method.</td>
</tr>
</tbody>
</table>

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
<td class="content">A penalty of 10% (<code>UNUSED_GAS_PENALTY_PERCENT</code>) is applied on the amounts of <code>callGasLimit</code> and <code>paymasterPostOpGasLimit</code> gas that remains unused if the amount of remaining unused gas is greater than or equal to 40,000 (<code>PENALTY_GAS_THRESHOLD</code>).</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect2">

### Signing the UserOp

<div class="paragraph">

To sign a UserOperation, you’ll need to first calculate its hash as an EIP-712 typed data structure using the EntryPoint’s domain, then sign this hash using your account’s signature scheme, and finally encode the resulting signature in the format that your account contract expects for verification.

</div>

<div class="listingblock">

<div class="content">

``` highlight
import { signTypedData } from 'viem/actions';

// EntryPoint v0.8 EIP-712 domain
const domain = {
  name: 'ERC4337',
  version: '1',
  chainId: 1, // Your target chain ID
  verifyingContract: '0x4337084D9E255Ff0702461CF8895CE9E3b5Ff108', // v08
};

// EIP-712 types for PackedUserOperation
const types = {
  PackedUserOperation: [
    { name: 'sender', type: 'address' },
    { name: 'nonce', type: 'uint256' },
    { name: 'initCode', type: 'bytes' },
    { name: 'callData', type: 'bytes' },
    { name: 'accountGasLimits', type: 'bytes32' },
    { name: 'preVerificationGas', type: 'uint256' },
    { name: 'gasFees', type: 'bytes32' },
    { name: 'paymasterAndData', type: 'bytes' },
  ],
} as const;

// Sign the UserOperation using EIP-712
userOp.signature = await eoa.signTypedData({
  domain,
  types,
  primaryType: 'PackedUserOperation',
  message: {
    sender: userOp.sender,
    nonce: userOp.nonce,
    initCode: userOp.initCode,
    callData: userOp.callData,
    accountGasLimits: userOp.accountGasLimits,
    preVerificationGas: userOp.preVerificationGas,
    gasFees: userOp.gasFees,
    paymasterAndData: userOp.paymasterAndData,
  },
});
```

</div>

</div>

<div class="paragraph">

Alternatively, developers can get the raw user operation hash by using the Entrypoint’s `getUserOpHash` function:

</div>

<div class="listingblock">

<div class="content">

``` highlight
const userOpHash = await entrypoint.read.getUserOpHash([userOp]);
userOp.signature = await eoa.sign({ hash: userOpHash });
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
<td class="content">Using <code>getUserOpHash</code> directly may provide a poorer user experience as users see an opaque hash rather than structured transaction data. In many cases, offchain signers won’t have an option to sign a raw hash.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Sending the UserOp

<div class="paragraph">

Finally, to send the user operation you can call `handleOps` on the Entrypoint contract and set yourself as the `beneficiary`.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Send the UserOperation
const userOpReceipt = await walletClient
  .writeContract({
    abi: [/* ENTRYPOINT ABI */],
    address: '0x<ENTRYPOINT_ADDRESS>',
    functionName: "handleOps",
    args: [[userOp], eoa.address],
  })
  .then((txHash) =>
    publicClient.waitForTransactionReceipt({
      hash: txHash,
    })
  );

// Print receipt
console.log(userOpReceipt);
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
<td class="content">Since you’re bundling your user operations yourself, you can safely specify <code>preVerificationGas</code> and <code>maxFeePerGas</code> in 0.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Using a Bundler

<div class="paragraph">

For better reliability, consider using a bundler service. Bundlers provide several key benefits: they automatically handle gas estimation, manage transaction ordering, support bundling multiple operations together, and generally offer higher transaction success rates compared to self-bundling.

</div>

</div>

</div>

</div>

<div class="sect1">

## Further notes

<div class="sectionbody">

<div class="sect2">

### ERC-7739 Signatures

<div class="paragraph">

A common security practice to prevent user operation [replayability across smart contract accounts controlled by the same private key](https://mirror.xyz/curiousapple.eth/pFqAdW2LiJ-6S4sg_u1z08k4vK6BCJ33LcyXpnNb8yU) (i.e. multiple accounts for the same signer) is to link the signature to the `address` and `chainId` of the account. This can be done by asking the user to sign a hash that includes these values.

</div>

<div class="paragraph">

The problem with this approach is that the user might be prompted by the wallet provider to sign an [obfuscated message](https://x.com/howydev/status/1780353754333634738), which is a phishing vector that may lead to a user losing its assets.

</div>

<div class="paragraph">

To prevent this, developers may use [`ERC7739Signer`](api:account.html#ERC7739Signer), a utility that implements [`IERC1271`](api:interfaces.html#IERC1271) for smart contract signatures with a defensive rehashing mechanism based on a [nested EIP-712 approach](https://github.com/frangio/eip712-wrapper-for-eip1271) to wrap the signature request in a context where there’s clearer information for the end user.

</div>

</div>

<div class="sect2">

### EIP-7702 Delegation

<div class="paragraph">

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) lets EOAs delegate to smart contracts while keeping their original signing key. This creates a hybrid account that works like an EOA for signing but has smart contract features. Protocols don’t need major changes to support EIP-7702 since they already handle both EOAs and smart contracts (see [SignatureChecker](api:utils/cryptography.html#SignatureChecker)).

</div>

<div class="paragraph">

The signature verification stays compatible: delegated EOAs are treated as contracts using ERC-1271, making it easy to redelegate to a contract with ERC-1271 support with little overhead by reusing the validation mechanism of the account.

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
<td class="content">Learn more about delegating to an ERC-7702 account in our <a href="eoa-delegation.html">EOA Delegation</a> section.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### ERC-7579 Modules

<div class="paragraph">

Smart accounts have evolved to embrace modularity as a design principle, with popular implementations like [Safe, Pimlico, Rhinestone, Etherspot and many others](https://erc7579.com/#supporters) agreeing on ERC-7579 as the standard for module interoperability. This standardization enables accounts to extend their functionality through external contracts while maintaining compatibility across different implementations.

</div>

<div class="paragraph">

OpenZeppelin Contracts provides both the building blocks for creating ERC-7579-compliant modules and an [`AccountERC7579`](api:account.html#AccountERC7579) implementation that supports installing and managing these modules.

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
<td class="content">Learn more in our <a href="https://docs.openzeppelin.com/community-contracts/0.0.1/account-modules">account modules</a> section.</td>
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
