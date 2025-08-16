<div id="header">

# Access Control

</div>


Access control—that is, "who is allowed to do this thing"—is incredibly important in the world of smart contracts. The access control of your contract may govern who can mint tokens, vote on proposals, freeze transfers, and many other things. It is therefore **critical** to understand how you implement it, lest someone else [steals your whole system](https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7).

</div>

</div>

</div>

<div class="sect1">

## Ownership and `Ownable`

<div class="sectionbody">

<div class="paragraph">

The most common and basic form of access control is the concept of *ownership*: there’s an account that is the `owner` of a contract and can do administrative tasks on it. This approach is perfectly reasonable for contracts that have a single administrative user.

</div>

<div class="paragraph">

OpenZeppelin Contracts provides [`Ownable`](api:access.html#Ownable) for implementing ownership in your contracts.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/MyContractOwnable.sol[role=include]
```

</div>

</div>

<div class="paragraph">

At deployment, the [`owner`](api:access.html#Ownable-owner--) of an `Ownable` contract is set to the provided `initialOwner` parameter.

</div>

<div class="paragraph">

Ownable also lets you:

</div>

<div class="ulist">

- [`transferOwnership`](api:access.html#Ownable-transferOwnership-address-) from the owner account to a new one, and

- [`renounceOwnership`](api:access.html#Ownable-renounceOwnership--) for the owner to relinquish this administrative privilege, a common pattern after an initial stage with centralized administration is over.

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
<td class="content">Removing the owner altogether will mean that administrative tasks that are protected by <code>onlyOwner</code> will no longer be callable!</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Ownable is a simple and effective way to implement access control, but you should be mindful of the dangers associated with transferring the ownership to an incorrect account that can’t interact with this contract anymore. An alternative to this problem is using [`Ownable2Step`](api:access.html#Ownable2Step); a variant of Ownable that requires the new owner to explicitly accept the ownership transfer by calling [`acceptOwnership`](api:access.html#Ownable2Step-acceptOwnership--).

</div>

<div class="paragraph">

Note that **a contract can also be the owner of another one**! This opens the door to using, for example, a [Gnosis Safe](https://safe.global), an [Aragon DAO](https://aragon.org), or a totally custom contract that *you* create.

</div>

<div class="paragraph">

In this way, you can use *composability* to add additional layers of access control complexity to your contracts. Instead of having a single regular Ethereum account (Externally Owned Account, or EOA) as the owner, you could use a 2-of-3 multisig run by your project leads, for example. Prominent projects in the space, such as [MakerDAO](https://makerdao.com), use systems similar to this one.

</div>

</div>

</div>

<div class="sect1">

## Role-Based Access Control

<div class="sectionbody">

<div class="paragraph">

While the simplicity of *ownership* can be useful for simple systems or quick prototyping, different levels of authorization are often needed. You may want for an account to have permission to ban users from a system, but not create new tokens. [*Role-Based Access Control (RBAC)*](https://en.wikipedia.org/wiki/Role-based_access_control) offers flexibility in this regard.

</div>

<div class="paragraph">

In essence, we will be defining multiple *roles*, each allowed to perform different sets of actions. An account may have, for example, 'moderator', 'minter' or 'admin' roles, which you will then check for instead of simply using `onlyOwner`. This check can be enforced through the `onlyRole` modifier. Separately, you will be able to define rules for how accounts can be granted a role, have it revoked, and more.

</div>

<div class="paragraph">

Most software uses access control systems that are role-based: some users are regular users, some may be supervisors or managers, and a few will often have administrative privileges.

</div>

<div class="sect2">

### Using `AccessControl`

<div class="paragraph">

OpenZeppelin Contracts provides [`AccessControl`](api:access.html#AccessControl) for implementing role-based access control. Its usage is straightforward: for each role that you want to define, you will create a new *role identifier* that is used to grant, revoke, and check if an account has that role.

</div>

<div class="paragraph">

Here’s a simple example of using `AccessControl` in an [ERC-20 token](erc20.html) to define a 'minter' role, which allows accounts that have it create new tokens:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessControlERC20MintBase.sol[role=include]
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
<td class="content">Make sure you fully understand how <a href="api:access.html#AccessControl"><code>AccessControl</code></a> works before using it on your system, or copy-pasting the examples from this guide.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

While clear and explicit, this isn’t anything we wouldn’t have been able to achieve with `Ownable`. Indeed, where `AccessControl` shines is in scenarios where granular permissions are required, which can be implemented by defining *multiple* roles.

</div>

<div class="paragraph">

Let’s augment our ERC-20 token example by also defining a 'burner' role, which lets accounts destroy tokens, and by using the `onlyRole` modifier:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessControlERC20MintOnlyRole.sol[role=include]
```

</div>

</div>

<div class="paragraph">

So clean! By splitting concerns this way, more granular levels of permission may be implemented than were possible with the simpler *ownership* approach to access control. Limiting what each component of a system is able to do is known as the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), and is a good security practice. Note that each account may still have more than one role, if so desired.

</div>

</div>

<div class="sect2">

### Granting and Revoking Roles

<div class="paragraph">

The ERC-20 token example above uses `_grantRole`, an `internal` function that is useful when programmatically assigning roles (such as during construction). But what if we later want to grant the 'minter' role to additional accounts?

</div>

<div class="paragraph">

By default, **accounts with a role cannot grant it or revoke it from other accounts**: all having a role does is making the `hasRole` check pass. To grant and revoke roles dynamically, you will need help from the *role’s admin*.

</div>

<div class="paragraph">

Every role has an associated admin role, which grants permission to call the `grantRole` and `revokeRole` functions. A role can be granted or revoked by using these if the calling account has the corresponding admin role. Multiple roles may have the same admin role to make management easier. A role’s admin can even be the same role itself, which would cause accounts with that role to be able to also grant and revoke it.

</div>

<div class="paragraph">

This mechanism can be used to create complex permissioning structures resembling organizational charts, but it also provides an easy way to manage simpler applications. `AccessControl` includes a special role, called `DEFAULT_ADMIN_ROLE`, which acts as the **default admin role for all roles**. An account with this role will be able to manage any other role, unless `_setRoleAdmin` is used to select a new admin role.

</div>

<div class="paragraph">

Since it is the admin for all roles by default, and in fact it is also its own admin, this role carries significant risk. To mitigate this risk we provide [`AccessControlDefaultAdminRules`](api:access.html#AccessControlDefaultAdminRules), a recommended extension of `AccessControl` that adds a number of enforced security measures for this role: the admin is restricted to a single account, with a 2-step transfer procedure with a delay in between steps.

</div>

<div class="paragraph">

Let’s take a look at the ERC-20 token example, this time taking advantage of the default admin role:

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessControlERC20MintMissing.sol[role=include]
```

</div>

</div>

<div class="paragraph">

Note that, unlike the previous examples, no accounts are granted the 'minter' or 'burner' roles. However, because those roles' admin role is the default admin role, and *that* role was granted to `msg.sender`, that same account can call `grantRole` to give minting or burning permission, and `revokeRole` to remove it.

</div>

<div class="paragraph">

Dynamic role allocation is often a desirable property, for example in systems where trust in a participant may vary over time. It can also be used to support use cases such as [KYC](https://en.wikipedia.org/wiki/Know_your_customer), where the list of role-bearers may not be known up-front, or may be prohibitively expensive to include in a single transaction.

</div>

</div>

<div class="sect2">

### Querying Privileged Accounts

<div class="paragraph">

Because accounts might [grant and revoke roles](#granting-and-revoking) dynamically, it is not always possible to determine which accounts hold a particular role. This is important as it allows proving certain properties about a system, such as that an administrative account is a multisig or a DAO, or that a certain role has been removed from all users, effectively disabling any associated functionality.

</div>

<div class="paragraph">

Under the hood, `AccessControl` uses `EnumerableSet`, a more powerful variant of Solidity’s `mapping` type, which allows for key enumeration. `getRoleMemberCount` can be used to retrieve the number of accounts that have a particular role, and `getRoleMember` can then be called to get the address of each of these accounts.

</div>

<div class="listingblock">

<div class="content">

``` highlight
const minterCount = await myToken.getRoleMemberCount(MINTER_ROLE);

const members = [];
for (let i = 0; i < minterCount; ++i) {
    members.push(await myToken.getRoleMember(MINTER_ROLE, i));
}
```

</div>

</div>

</div>

</div>

</div>

<div class="sect1">

## Delayed operation

<div class="sectionbody">

<div class="paragraph">

Access control is essential to prevent unauthorized access to critical functions. These functions may be used to mint tokens, freeze transfers or perform an upgrade that completely changes the smart contract logic. While [`Ownable`](api:access.html#Ownable) and [`AccessControl`](api:access.html#AccessControl) can prevent unauthorized access, they do not address the issue of a misbehaving administrator attacking their own system to the prejudice of their users.

</div>

<div class="paragraph">

This is the issue the [`TimelockController`](api:governance.html#TimelockController) is addressing.

</div>

<div class="paragraph">

The [`TimelockController`](api:governance.html#TimelockController) is a proxy that is governed by proposers and executors. When set as the owner/admin/controller of a smart contract, it ensures that whichever maintenance operation is ordered by the proposers is subject to a delay. This delay protects the users of the smart contract by giving them time to review the maintenance operation and exit the system if they consider it is in their best interest to do so.

</div>

<div class="sect2">

### Using `TimelockController`

<div class="paragraph">

By default, the address that deployed the [`TimelockController`](api:governance.html#TimelockController) gets administration privileges over the timelock. This role grants the right to assign proposers, executors, and other administrators.

</div>

<div class="paragraph">

The first step in configuring the [`TimelockController`](api:governance.html#TimelockController) is to assign at least one proposer and one executor. These can be assigned during construction or later by anyone with the administrator role. These roles are not exclusive, meaning an account can have both roles.

</div>

<div class="paragraph">

Roles are managed using the [`AccessControl`](api:access.html#AccessControl) interface and the `bytes32` values for each role are accessible through the `ADMIN_ROLE`, `PROPOSER_ROLE` and `EXECUTOR_ROLE` constants.

</div>

<div class="paragraph">

There is an additional feature built on top of `AccessControl`: giving the executor role to `address(0)` opens access to anyone to execute a proposal once the timelock has expired. This feature, while useful, should be used with caution.

</div>

<div class="paragraph">

At this point, with both a proposer and an executor assigned, the timelock can perform operations.

</div>

<div class="paragraph">

An optional next step is for the deployer to renounce its administrative privileges and leave the timelock self-administered. If the deployer decides to do so, all further maintenance, including assigning new proposers/schedulers or changing the timelock duration will have to follow the timelock workflow. This links the governance of the timelock to the governance of contracts attached to the timelock, and enforce a delay on timelock maintenance operations.

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
<td class="content">If the deployer renounces administrative rights in favour of timelock itself, assigning new proposers or executors will require a timelocked operation. This means that if the accounts in charge of any of these two roles become unavailable, then the entire contract (and any contract it controls) becomes locked indefinitely.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

With both the proposer and executor roles assigned and the timelock in charge of its own administration, you can now transfer the ownership/control of any contract to the timelock.

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
<td class="content">A recommended configuration is to grant both roles to a secure governance contract such as a DAO or a multisig, and to additionally grant the executor role to a few EOAs held by people in charge of helping with the maintenance operations. These wallets cannot take over control of the timelock but they can help smoothen the workflow.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Minimum delay

<div class="paragraph">

Operations executed by the [`TimelockController`](api:governance.html#TimelockController) are not subject to a fixed delay but rather a minimum delay. Some major updates might call for a longer delay. For example, if a delay of just a few days might be sufficient for users to audit a minting operation, it makes sense to use a delay of a few weeks, or even a few months, when scheduling a smart contract upgrade.

</div>

<div class="paragraph">

The minimum delay (accessible through the [`getMinDelay`](api:governance.html#TimelockController-getMinDelay--) method) can be updated by calling the [`updateDelay`](api:governance.html#TimelockController-updateDelay-uint256-) function. Bear in mind that access to this function is only accessible by the timelock itself, meaning this maintenance operation has to go through the timelock itself.

</div>

</div>

</div>

</div>

<div class="sect1">

## Access Management

<div class="sectionbody">

<div class="paragraph">

For a system of contracts, better integrated role management can be achieved with an [`AccessManager`](api:access.html#AccessManager) instance. Instead of managing each contract’s permission separately, AccessManager stores all the permissions in a single contract, making your protocol easier to audit and maintain.

</div>

<div class="paragraph">

Although [`AccessControl`](api:access.html#AccessControl) offers a more dynamic solution for adding permissions to your contracts than Ownable, decentralized protocols tend to become more complex after integrating new contract instances and requires you to keep track of permissions separately in each contract. This increases the complexity of permissions management and monitoring across the system.

</div>

<div class="imageblock">

<div class="content">

![Access Control multiple](access-control-multiple.svg)

</div>

</div>

<div class="paragraph">

Protocols managing permissions in production systems often require more integrated alternatives to fragmented permissions through multiple `AccessControl` instances.

</div>

<div class="imageblock">

<div class="content">

![AccessManager](access-manager.svg)

</div>

</div>

<div class="paragraph">

The AccessManager is designed around the concept of role and target functions:

</div>

<div class="ulist">

- Roles are granted to accounts (addresses) following a many-to-many approach for flexibility. This means that each user can have one or multiple roles and multiple users can have the same role.

- Access to a restricted target function is limited to one role. A target function is defined by one [function selector](https://docs.soliditylang.org/en/v0.8.20/abi-spec.html#function-selector) on one contract (called target).

</div>

<div class="paragraph">

For a call to be authorized, the caller must bear the role that is assigned to the current target function (contract address + function selector).

</div>

<div class="imageblock">

<div class="content">

![AccessManager functions](access-manager-functions.svg)

</div>

</div>

<div class="sect2">

### Using `AccessManager`

<div class="paragraph">

OpenZeppelin Contracts provides [`AccessManager`](api:access.html#AccessManager) for managing roles across any number of contracts. The `AccessManager` itself is a contract that can be deployed and used out of the box. It sets an initial admin in the constructor who will be allowed to perform management operations.

</div>

<div class="paragraph">

In order to restrict access to some functions of your contract, you should inherit from the [`AccessManaged`](api:access.html#AccessManaged) contract provided along with the manager. This provides the `restricted` modifier that can be used to protect any externally facing function. Note that you will have to specify the address of the AccessManager instance ([`initialAuthority`](api:access.html#AccessManaged-constructor-address-)) in the constructor so the `restricted` modifier knows which manager to use for checking permissions.

</div>

<div class="paragraph">

Here’s a simple example of an [ERC-20 token](tokens.html#ERC20) that defines a `mint` function that is restricted by an [`AccessManager`](api:access.html#AccessManager):

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$access-control/AccessManagedERC20MintBase.sol[role=include]
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
<td class="content">Make sure you fully understand how <a href="api:access.html#AccessManager"><code>AccessManager</code></a> works before using it or copy-pasting the examples from this guide.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

Once the managed contract has been deployed, it is now under the manager’s control. The initial admin can then assign the minter role to an address and also allow the role to call the `mint` function. For example, this is demonstrated in the following Javascript code using Ethers.js:

</div>

<div class="listingblock">

<div class="content">

``` highlight
// const target = ...;
// const user = ...;
const MINTER = 42n; // Roles are uint64 (0 is reserved for the ADMIN_ROLE)

// Grant the minter role with no execution delay
await manager.grantRole(MINTER, user, 0);

// Allow the minter role to call the function selector
// corresponding to the mint function
await manager.setTargetFunctionRole(
    target,
    ['0x40c10f19'], // bytes4(keccak256('mint(address,uint256)'))
    MINTER
);
```

</div>

</div>

<div class="paragraph">

Even though each role has its own list of function permissions, each role member (`address`) has an execution delay that will dictate how long the account should wait to execute a function that requires its role. Delayed operations must have the [`schedule`](api:access.html#AccessManager-schedule-address-bytes-uint48-) function called on them first in the AccessManager before they can be executed, either by calling to the target function or using the AccessManager’s [`execute`](api:access.html#AccessManager-execute-address-bytes-) function.

</div>

<div class="paragraph">

Additionally, roles can have a granting delay that prevents adding members immediately. The AccessManager admins can set this grant delay as follows:

</div>

<div class="listingblock">

<div class="content">

``` highlight
const HOUR = 60 * 60;

const GRANT_DELAY = 24 * HOUR;
const EXECUTION_DELAY = 5 * HOUR;
const ACCOUNT = "0x...";

await manager.connect(initialAdmin).setGrantDelay(MINTER, GRANT_DELAY);

// The role will go into effect after the GRANT_DELAY passes
await manager.connect(initialAdmin).grantRole(MINTER, ACCOUNT, EXECUTION_DELAY);
```

</div>

</div>

<div class="paragraph">

Note that roles do not define a name. As opposed to the [`AccessControl`](api:access.html#AccessControl) case, roles are identified as numeric values instead of being hardcoded in the contract as `bytes32` values. It is still possible to allow for tooling discovery (e.g. for role exploration) using role labeling with the [`labelRole`](api:access.html#AccessManager-labelRole-uint64-string-) function.

</div>

<div class="listingblock">

<div class="content">

``` highlight
await manager.labelRole(MINTER, "MINTER");
```

</div>

</div>

<div class="paragraph">

Given the admins of the `AccessManaged` can modify all of its permissions, it’s recommended to keep only a single admin address secured under a multisig or governance layer. To achieve this, it is possible for the initial admin to set up all the required permissions, targets, and functions, assign a new admin, and finally renounce its admin role.

</div>

<div class="paragraph">

For improved incident response coordination, the manager includes a mode where administrators can completely close a target contract. When closed, all calls to restricted target functions in a target contract will revert.

</div>

<div class="paragraph">

Closing and opening contracts don’t alter any of their settings, neither permissions nor delays. Particularly, the roles required for calling specific target functions are not modified.

</div>

<div class="paragraph">

This mode is useful for incident response operations that require temporarily shutting down a contract in order to evaluate emergencies and reconfigure permissions.

</div>

<div class="listingblock">

<div class="content">

``` highlight
const target = await myToken.getAddress();

// Token's `restricted` functions closed
await manager.setTargetClosed(target, true);

// Token's `restricted` functions open
await manager.setTargetClosed(target, false);
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
<td class="content">Even if an <code>AccessManager</code> defines permissions for a target function, these won’t be applied if the managed contract instance is not using the <a href="api:access.html#AccessManaged-restricted--"><code>restricted</code></a> modifier for that function, or if its manager is a different one.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Role Admins and Guardians

<div class="paragraph">

An important aspect of the AccessControl contract is that roles aren’t granted nor revoked by role members. Instead, it relies on the concept of a role admin for granting and revoking.

</div>

<div class="paragraph">

In the case of the `AccessManager`, the same rule applies and only the role’s admins are able to call [grant](api:access.html#AccessManager-grantRole-uint64-address-uint32-) and [revoke](api:access.html#AccessManager-revokeRole-uint64-address-) functions. Note that calling these functions will be subject to the execution delay that the executing role admin has.

</div>

<div class="paragraph">

Additionally, the `AccessManager` stores a *guardian* as an extra protection for each role. This guardian has the ability to cancel operations that have been scheduled by any role member with an execution delay. Consider that a role will have its initial admin and guardian default to the `ADMIN_ROLE` (`0`).

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
<td class="content">Be careful with the members of <code>ADMIN_ROLE</code>, since it acts as the default admin and guardian for every role. A misbehaved guardian can cancel operations at will, affecting the AccessManager’s operation.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Manager configuration

<div class="paragraph">

The `AccessManager` provides a built-in interface for configuring permission settings that can be accessed by its `ADMIN_ROLE` members.

</div>

<div class="paragraph">

This configuration interface includes the following functions:

</div>

<div class="ulist">

- Add a label to a role using the [`labelRole`](api:access.html#AccessManager-labelRole-uint64-string-) function.

- Assign the admin and guardian of a role with [`setRoleAdmin`](api:access.html#AccessManager-setRoleAdmin-uint64-uint64-) and [`setRoleGuardian`](api:access.html#AccessManager-setRoleGuardian-uint64-uint64-).

- Set each role’s grant delay via [`setGrantDelay`](api:access.html#AccessManager-setGrantDelay-uint64-uint32-).

</div>

<div class="paragraph">

As an admin, some actions will require a delay. Similar to each member’s execution delay, some admin operations require waiting for execution and should follow the [`schedule`](api:access.html#AccessManager-schedule-address-bytes-uint48-) and [`execute`](api:access.html#AccessManager-execute-address-bytes-) workflow.

</div>

<div class="paragraph">

More specifically, these delayed functions are those for configuring the settings of a specific target contract. The delay applied to these functions can be adjusted by the manager admins with [`setTargetAdminDelay`](api:access.html#AccessManager-setTargetAdminDelay-address-uint32-).

</div>

<div class="paragraph">

The delayed admin actions are:

</div>

<div class="ulist">

- Updating an `AccessManaged` contract [authority](api:access.html#AccessManaged-authority--) using [`updateAuthority`](api:access.html#AccessManager-updateAuthority-address-address-).

- Closing or opening a target via [`setTargetClosed`](api:access.html#AccessManager-setTargetClosed-address-bool-).

- Changing permissions of whether a role can call a target function with [`setTargetFunctionRole`](api:access.html#AccessManager-setTargetFunctionRole-address-bytes4---uint64-).

</div>

</div>

<div class="sect2">

### Using with Ownable

<div class="paragraph">

Contracts already inheriting from [`Ownable`](api:access.html#Ownable) can migrate to AccessManager by transferring ownership to the manager. After that, all calls to functions with the `onlyOwner` modifier should be called through the manager’s [`execute`](api:access.html#AccessManager-execute-address-bytes-) function, even if the caller doesn’t require a delay.

</div>

<div class="listingblock">

<div class="content">

``` highlight
await ownable.connect(owner).transferOwnership(accessManager);
```

</div>

</div>

</div>

<div class="sect2">

### Using with AccessControl

<div class="paragraph">

For systems already using [`AccessControl`](api:access.html#AccessControl), the `DEFAULT_ADMIN_ROLE` can be granted to the `AccessManager` after revoking every other role. Subsequent calls should be made through the manager’s [`execute`](api:access.html#AccessManager-execute-address-bytes-) method, similar to the Ownable case.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// Revoke old roles
await accessControl.connect(admin).revokeRole(MINTER_ROLE, account);

// Grant the admin role to the access manager
await accessControl.connect(admin).grantRole(DEFAULT_ADMIN_ROLE, accessManager);

await accessControl.connect(admin).renounceRole(DEFAULT_ADMIN_ROLE, admin);
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
