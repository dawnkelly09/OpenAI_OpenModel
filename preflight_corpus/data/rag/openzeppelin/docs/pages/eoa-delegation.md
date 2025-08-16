<div id="header">

# EOA Delegation

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) introduces a new transaction type (`0x4`) that grants [Externally Owned Accounts (EOAs)](https://ethereum.org/en/developers/docs/accounts/) the ability to delegate execution to an smart contract. This is particularly useful to enable traditional EVM accounts to:

</div>

<div class="ulist">

- Batch multiple operations in a single transaction (e.g. [`approve`](api:token/ERC20.html#IERC20-approve-address-uint256-) + [`transfer`](api:token/ERC20.html#IERC20-transfer-address-uint256-), yey!)

- Sponsoring transactions for other users.

- Implementing privilege de-escalation (e.g., sub-keys with limited permissions)

</div>

<div class="paragraph">

This section walks you through the process of delegating an EOA to a contract following [ERC-7702](https://eips.ethereum.org/EIPS/eip-7702). This allows you to use your EOA’s private key to sign and execute operations with custom execution logic. Combined with [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) infrastructure, users can achieve gas sponsoring through [paymasters](https://docs.openzeppelin.com/community-contracts/paymasters).

</div>

</div>

</div>

<div class="sect1">

## Delegating execution

<div class="sectionbody">

<div class="paragraph">

EIP-7702 enables EOAs to delegate their execution capabilities to smart contracts, effectively bridging the gap between traditional and [Smart Accounts](accounts.html). The [`SignerERC7702`](api:utils/cryptography.html) utility facilitates this delegation by verifying signatures against the EOA’s address (`address(this)`), making it easier to implement EIP-7702 in smart contract accounts.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$account/MyAccountERC7702.sol[role=include]
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
<td class="content">Users can delegate to an instance of <a href="api:account.html#ERC7821"><code>ERC-7821</code></a> for a minimal batch executor that does not use ERC-4337 related code.</td>
</tr>
</tbody>
</table>

</div>

<div class="sect2">

### Signing Authorization

<div class="paragraph">

To authorize delegation, the EOA owner signs a message containing the chain ID, nonce, delegation address, and signature components (i.e. `[chain_id, address, nonce, y_parity, r, s]`). This signed authorization serves two purposes: it restricts execution to only the delegate contract and prevents replay attacks.

</div>

<div class="paragraph">

The EOA maintains a delegation designator for each authorized address on each chain, which points to the contract whose code will be executed in the EOA’s context to handle delegated operations.

</div>

<div class="paragraph">

Here’s how to construct an authorization with [viem](https://viem.sh/):

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Remember not to hardcode your private key!
const eoa = privateKeyToAccount('<YOUR_PRIVATE_KEY>');
const eoaClient = createWalletClient({
  account: eoa,
  chain: publicClient.chain,
  transport: http(),
});

const walletClient = createWalletClient({
  account, // See Viem's `privateKeyToAccount`
  chain, // import { ... } from 'viem/chains';
  transport: http(),
})

const authorization = await eoaClient.signAuthorization({
  account: walletClient.account.address,
  contractAddress: '0x<YOUR_DELEGATE_CONTRACT_ADDRESS>',
  // Use instead of `account` if your
  // walletClient's account is the one sending the transaction
  // executor: "self",
});
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
<td class="content">When implementing delegate contracts, ensure they require signatures that avoid replayability (e.g. a domain separator, nonce). A poorly implemented delegate can allow a malicious actor to take near complete control over a signer’s EOA.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Send a Set Code Transaction

<div class="paragraph">

After signing the authorization, you need to send a `SET_CODE_TX_TYPE` (0x04) transaction to write the delegation designator (i.e. `0xef0100 || address`) to your EOA’s code, which tells the EVM to load and execute code from the specified address when operations are performed on your EOA.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Send the `authorization` along with `data`
const receipt = await walletClient
  .sendTransaction({
    authorizationList: [authorization],
    data: '0x<CALLDATA_TO_EXECUTE_IN_THE_ACCOUNT>',
    to: eoa.address,
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

<div class="paragraph">

To remove the delegation and restore your EOA to its original state, you can send a `SET_CODE_TX_TYPE` transaction with an authorization tuple that points to the zero address (`0x0000000000000000000000000000000000000000`). This will clear the account’s code and reset its code hash to the empty hash, however, be aware that it will not automatically clean the EOA storage.

</div>

<div class="paragraph">

When changing an account’s delegation, ensure the newly delegated code is purposely designed and tested as an upgrade to the old one. To ensure safe migration between delegate contracts, namespaced storage that avoid accidental collisions following ERC-7201.

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
<td class="content">Updating the delegation designator may render your EOA unusable due to potential storage collisions. We recommend following similar practices to those of <a href="https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable">writing upgradeable smart contracts</a>.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="sect1">

## Using with ERC-4337

<div class="sectionbody">

<div class="paragraph">

The ability to set code to execute logic on an EOA allows users to leverage ERC-4337 infrastructure to process user operations. Developers only need to combine an [`Account`](api:account.html#Account) contract with an [`SignerERC7702`](api:utils/cryptography.html#SignerERC7702) to accomplish ERC-4337 compliance out of the box.

</div>

<div class="sect2">

### Sending a UserOp

<div class="paragraph">

Once your EOA is delegated to an ERC-4337 compatible account, you can send user operations through the entry point contract. The user operation includes all the necessary fields for execution, including gas limits, fees, and the actual call data to execute. The entry point will validate the operation and execute it in the context of your delegated account.

</div>

<div class="paragraph">

Similar to how [sending a UserOp](accounts.html#bundle_a_useroperation) is achieved for factory accounts, here’s how you can construct a UserOp for an EOA who’s delegated to an [`Account`](api:account.html#Account) contract.

</div>

<div class="listingblock">

<div class="content">

``` highlight
const userOp = {
  sender: eoa.address,
  nonce: await entrypoint.read.getNonce([eoa.address, 0n]),
  initCode: "0x" as Hex,
  callData: '0x<CALLDATA_TO_EXECUTE_IN_THE_ACCOUNT>',
  accountGasLimits: encodePacked(
    ["uint128", "uint128"],
    [
      100_000n, // verificationGas
      300_000n, // callGas
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

const userOpHash = await entrypoint.read.getUserOpHash([userOp]);
userOp.signature = await eoa.sign({ hash: userOpHash });

const userOpReceipt = await eoaClient
  .writeContract({
    abi: EntrypointV08Abi,
    address: entrypoint.address,
    authorizationList: [authorization],
    functionName: "handleOps",
    args: [[userOp], eoa.address],
  })
  .then((txHash) =>
    publicClient.waitForTransactionReceipt({
      hash: txHash,
    })
  );

console.log(userOpReceipt);
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
<td class="content">When using sponsored transaction relayers, be aware that the authorized account can cause relayers to spend gas without being reimbursed by either invalidating the authorization (increasing the account’s nonce) or by sweeping the relevant assets out of the account. Relayers may implement safeguards like requiring a bond or using a reputation system.</td>
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
