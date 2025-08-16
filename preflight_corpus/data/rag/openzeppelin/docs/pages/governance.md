<div id="header">

# How to set up on-chain governance

</div>

<div id="content">

<div id="preamble">

<div class="sectionbody">

<div class="paragraph">

In this guide we will learn how OpenZeppelin’s Governor contract works, how to set it up, and how to use it to create proposals, vote for them, and execute them, using tools provided by Ethers.js and Tally.

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
<td class="content">Find detailed contract documentation at <a href="api:governance.html">Governance API</a>.</td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="sect1">

## Introduction

<div class="sectionbody">

<div class="paragraph">

Decentralized protocols are in constant evolution from the moment they are publicly released. Often, the initial team retains control of this evolution in the first stages, but eventually delegates it to a community of stakeholders. The process by which this community makes decisions is called on-chain governance, and it has become a central component of decentralized protocols, fueling varied decisions such as parameter tweaking, smart contract upgrades, integrations with other protocols, treasury management, grants, etc.

</div>

<div class="paragraph">

This governance protocol is generally implemented in a special-purpose contract called “Governor”. The GovernorAlpha and GovernorBravo contracts designed by Compound have been very successful and popular so far, with the downside that projects with different requirements have had to fork the code to customize it for their needs, which can pose a high risk of introducing security issues. For OpenZeppelin Contracts, we set out to build a modular system of Governor contracts so that forking is not needed, and different requirements can be accommodated by writing small modules using Solidity inheritance. You will find the most common requirements out of the box in OpenZeppelin Contracts, but writing additional ones is simple, and we will be adding new features as requested by the community in future releases. Additionally, the design of OpenZeppelin Governor requires minimal use of storage and results in more gas efficient operation.

</div>

</div>

</div>

<div class="sect1">

## Compatibility

<div class="sectionbody">

<div class="paragraph">

OpenZeppelin’s Governor system was designed with a concern for compatibility with existing systems that were based on Compound’s GovernorAlpha and GovernorBravo. Because of this, you will find that many modules are presented in two variants, one of which is built for compatibility with those systems.

</div>

<div class="sect2">

### ERC20Votes & ERC20VotesComp

<div class="paragraph">

The ERC-20 extension to keep track of votes and vote delegation is one such case. The shorter one is the more generic version because it can support token supplies greater than 2^96, while the “Comp” variant is limited in that regard, but exactly fits the interface of the COMP token that is used by GovernorAlpha and Bravo. Both contract variants share the same events, so they are fully compatible when looking at events only.

</div>

</div>

<div class="sect2">

### Governor & GovernorStorage

<div class="paragraph">

An OpenZeppelin Governor contract is not interface-compatible with Compound’s GovernorAlpha or Bravo. Even though events are fully compatible, proposal lifecycle functions (creation, execution, etc.) have different signatures that are meant to optimize storage use. Other functions from GovernorAlpha and Bravo are likewise not available. It’s possible to opt in some Bravo-like behavior by inheriting from the GovernorStorage module. This module provides proposal enumerability and alternate versions of the `queue`, `execute` and `cancel` function that only take the proposal id. This module reduces the calldata needed by some operations in exchange for an increased storage footprint. This might be a good trade-off for some L2 chains. It also provides primitives for indexer-free frontends.

</div>

<div class="paragraph">

Note that even with the use of this module, one important difference with Compound’s GovernorBravo is the way that \`proposalId\`s are calculated. Governor uses the hash of the proposal parameters with the purpose of keeping its data off-chain by event indexing, while the original Bravo implementation uses sequential \`proposalId\`s.

</div>

</div>

<div class="sect2">

### GovernorTimelockControl & GovernorTimelockCompound

<div class="paragraph">

When using a timelock with your Governor contract, you can use either OpenZeppelin’s TimelockController or Compound’s Timelock. Based on the choice of timelock, you should choose the corresponding Governor module: GovernorTimelockControl or GovernorTimelockCompound respectively. This allows you to migrate an existing GovernorAlpha instance to an OpenZeppelin-based Governor without changing the timelock in use.

</div>

</div>

<div class="sect2">

### Tally

<div class="paragraph">

[Tally](https://www.tally.xyz) is a full-fledged application for user owned on-chain governance. It comprises a voting dashboard, proposal creation wizard, real time research and analysis, and educational content.

</div>

<div class="paragraph">

For all of these options, the Governor will be compatible with Tally: users will be able to create proposals, see voting periods and delays following [IERC6372](api:interfaces.html#IERC6372), visualize voting power and advocates, navigate proposals, and cast votes. For proposal creation in particular, projects can also use [Defender Transaction Proposals](https://docs.openzeppelin.com/defender/module/actions#transaction-proposals-reference) as an alternative interface.

</div>

<div class="paragraph">

In the rest of this guide, we will focus on a fresh deploy of the vanilla OpenZeppelin Governor features without concern for compatibility with GovernorAlpha or Bravo.

</div>

</div>

</div>

</div>

<div class="sect1">

## Setup

<div class="sectionbody">

<div class="sect2">

### Token

<div class="paragraph">

The voting power of each account in our governance setup will be determined by an ERC-20 token. The token has to implement the ERC20Votes extension. This extension will keep track of historical balances so that voting power is retrieved from past snapshots rather than current balance, which is an important protection that prevents double voting.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$governance/MyToken.sol[role=include]
```

</div>

</div>

<div class="paragraph">

If your project already has a live token that does not include ERC20Votes and is not upgradeable, you can wrap it in a governance token by using ERC20Wrapper. This will allow token holders to participate in governance by wrapping their tokens 1-to-1.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$governance/MyTokenWrapped.sol[role=include]
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
<td class="content">The only other source of voting power available in OpenZeppelin Contracts currently is <a href="api:token/ERC721.html#ERC721Votes"><code>ERC721Votes</code></a>. ERC-721 tokens that don’t provide this functionality can be wrapped into a voting tokens using a combination of <a href="api:token/ERC721.html#ERC721Votes"><code>ERC721Votes</code></a> and <a href="api:token/ERC721.html#ERC721Wrapper"><code>ERC721Wrapper</code></a>.</td>
</tr>
</tbody>
</table>

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
<td class="content">The internal clock used by the token to store voting balances will dictate the operating mode of the Governor contract attached to it. By default, block numbers are used. Since v4.9, developers can override the <a href="api:interfaces.html#IERC6372">IERC6372</a> clock to use timestamps instead of block numbers.</td>
</tr>
</tbody>
</table>

</div>

</div>

<div class="sect2">

### Governor

<div class="paragraph">

Initially, we will build a Governor without a timelock. The core logic is given by the Governor contract, but we still need to choose: 1) how voting power is determined, 2) how many votes are needed for quorum, 3) what options people have when casting a vote and how those votes are counted, and 4) what type of token should be used to vote. Each of these aspects is customizable by writing your own module, or more easily choosing one from OpenZeppelin Contracts.

</div>

<div class="paragraph">

For 1) we will use the GovernorVotes module, which hooks to an IVotes instance to determine the voting power of an account based on the token balance they hold when a proposal becomes active. This module requires as a constructor parameter the address of the token. This module also discovers the clock mode (ERC-6372) used by the token and applies it to the Governor.

</div>

<div class="paragraph">

For 2) we will use GovernorVotesQuorumFraction which works together with ERC20Votes to define quorum as a percentage of the total supply at the block a proposal’s voting power is retrieved. This requires a constructor parameter to set the percentage. Most Governors nowadays use 4%, so we will initialize the module with parameter 4 (this indicates the percentage, resulting in 4%).

</div>

<div class="paragraph">

For 3) we will use GovernorCountingSimple, a module that offers 3 options to voters: For, Against, and Abstain, and where only For and Abstain votes are counted towards quorum.

</div>

<div class="paragraph">

Besides these modules, Governor itself has some parameters we must set.

</div>

<div class="paragraph">

votingDelay: How long after a proposal is created should voting power be fixed. A large voting delay gives users time to unstake tokens if necessary.

</div>

<div class="paragraph">

votingPeriod: How long does a proposal remain open to votes.

</div>

<div class="paragraph">

These parameters are specified in the unit defined in the token’s clock. Assuming the token uses block numbers, and assuming block time of around 12 seconds, we will have set votingDelay = 1 day = 7200 blocks, and votingPeriod = 1 week = 50400 blocks.

</div>

<div class="paragraph">

We can optionally set a proposal threshold as well. This restricts proposal creation to accounts that have enough voting power.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$governance/MyGovernor.sol[role=include]
```

</div>

</div>

</div>

<div class="sect2">

### Timelock

<div class="paragraph">

It is good practice to add a timelock to governance decisions. This allows users to exit the system if they disagree with a decision before it is executed. We will use OpenZeppelin’s TimelockController in combination with the GovernorTimelockControl module.

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
<td class="content">When using a timelock, it is the timelock that will execute proposals and thus the timelock that should hold any funds, ownership, and access control roles. Before version 4.5 there was no way to recover funds in the Governor contract when using a timelock! Before version 4.3, when using the Compound Timelock, ETH in the timelock was not easily accessible.</td>
</tr>
</tbody>
</table>

</div>

<div class="paragraph">

TimelockController uses an AccessControl setup that we need to understand in order to set up roles.

</div>

<div class="ulist">

- The Proposer role is in charge of queueing operations: this is the role the Governor instance should be granted, and it should likely be the only proposer in the system.

- The Executor role is in charge of executing already available operations: we can assign this role to the special zero address to allow anyone to execute (if operations can be particularly time sensitive, the Governor should be made Executor instead).

- Lastly, there is the Admin role, which can grant and revoke the two previous roles: this is a very sensitive role that will be granted automatically to the timelock itself, and optionally to a second account, which can be used for ease of setup but should promptly renounce the role.

</div>

</div>

</div>

</div>

<div class="sect1">

## Proposal Lifecycle

<div class="sectionbody">

<div class="paragraph">

Let’s walk through how to create and execute a proposal on our newly deployed Governor.

</div>

<div class="paragraph">

A proposal is a sequence of actions that the Governor contract will perform if it passes. Each action consists of a target address, calldata encoding a function call, and an amount of ETH to include. Additionally, a proposal includes a human-readable description.

</div>

<div class="sect2">

### Create a Proposal

<div class="paragraph">

Let’s say we want to create a proposal to give a team a grant, in the form of ERC-20 tokens from the governance treasury. This proposal will consist of a single action where the target is the ERC-20 token, calldata is the encoded function call `transfer(<team wallet>, <grant amount>)`, and with 0 ETH attached.

</div>

<div class="paragraph">

Generally a proposal will be created with the help of an interface such as Tally or [Defender Proposals](https://docs.openzeppelin.com/defender/module/actions#transaction-proposals-reference). Here we will show how to create the proposal using Ethers.js.

</div>

<div class="paragraph">

First we get all the parameters necessary for the proposal action.

</div>

<div class="listingblock">

<div class="content">

``` highlight
const tokenAddress = ...;
const token = await ethers.getContractAt(‘ERC20’, tokenAddress);

const teamAddress = ...;
const grantAmount = ...;
const transferCalldata = token.interface.encodeFunctionData(‘transfer’, [teamAddress, grantAmount]);
```

</div>

</div>

<div class="paragraph">

Now we are ready to call the propose function of the Governor. Note that we don’t pass in one array of actions, but instead three arrays corresponding to the list of targets, the list of values, and the list of calldatas. In this case it’s a single action, so it’s simple:

</div>

<div class="listingblock">

<div class="content">

``` highlight
await governor.propose(
  [tokenAddress],
  [0],
  [transferCalldata],
  “Proposal #1: Give grant to team”,
);
```

</div>

</div>

<div class="paragraph">

This will create a new proposal, with a proposal id that is obtained by hashing together the proposal data, and which will also be found in an event in the logs of the transaction.

</div>

</div>

<div class="sect2">

### Cast a Vote

<div class="paragraph">

Once a proposal is active, delegates can cast their vote. Note that it is delegates who carry voting power: if a token holder wants to participate, they can set a trusted representative as their delegate, or they can become a delegate themselves by self-delegating their voting power.

</div>

<div class="paragraph">

Votes are cast by interacting with the Governor contract through the `castVote` family of functions. Voters would generally invoke this from a governance UI such as Tally.

</div>

<div class="imageblock">

<div class="content">

![Voting in Tally](tally-vote.png)

</div>

</div>

</div>

<div class="sect2">

### Execute the Proposal

<div class="paragraph">

Once the voting period is over, if quorum was reached (enough voting power participated) and the majority voted in favor, the proposal is considered successful and can proceed to be executed. Once a proposal passes, it can be queued and executed from the same place you voted.

</div>

<div class="imageblock">

<div class="content">

![Administration Panel in Tally](tally-exec.png)

</div>

</div>

<div class="paragraph">

We will see now how to do this manually using Ethers.js.

</div>

<div class="paragraph">

If a timelock was set up, the first step to execution is queueing. You will notice that both the queue and execute functions require passing in the entire proposal parameters, as opposed to just the proposal id. This is necessary because this data is not stored on chain, as a measure to save gas. Note that these parameters can always be found in the events emitted by the contract. The only parameter that is not sent in its entirety is the description, since this is only needed in its hashed form to compute the proposal id.

</div>

<div class="paragraph">

To queue, we call the queue function:

</div>

<div class="listingblock">

<div class="content">

``` highlight
const descriptionHash = ethers.utils.id(“Proposal #1: Give grant to team”);

await governor.queue(
  [tokenAddress],
  [0],
  [transferCalldata],
  descriptionHash,
);
```

</div>

</div>

<div class="paragraph">

This will cause the Governor to interact with the timelock contract and queue the actions for execution after the required delay.

</div>

<div class="paragraph">

After enough time has passed (according to the timelock parameters), the proposal can be executed. If there was no timelock to begin with, this step can be ran immediately after the proposal succeeds.

</div>

<div class="listingblock">

<div class="content">

``` highlight
await governor.execute(
  [tokenAddress],
  [0],
  [transferCalldata],
  descriptionHash,
);
```

</div>

</div>

<div class="paragraph">

Executing the proposal will transfer the ERC-20 tokens to the chosen recipient. To wrap up: we set up a system where a treasury is controlled by the collective decision of the token holders of a project, and all actions are executed via proposals enforced by on-chain votes.

</div>

</div>

</div>

</div>

<div class="sect1">

## Timestamp based governance

<div class="sectionbody">

<div class="sect2">

### Motivation

<div class="paragraph">

It is sometimes difficult to deal with durations expressed in number of blocks because of inconsistent or unpredictable time between blocks. This is particularly true of some L2 networks where blocks are produced based on blockchain usage. Using number of blocks can also lead to the governance rules being affected by network upgrades that modify the expected time between blocks.

</div>

<div class="paragraph">

The difficulty of replacing block numbers with timestamps is that the Governor and the token must both use the same format when querying past votes. If a token is designed around block numbers, it is not possible for a Governor to reliably do timestamp based lookups.

</div>

<div class="paragraph">

Therefore, designing a timestamp based voting system starts with the token.

</div>

</div>

<div class="sect2">

### Token

<div class="paragraph">

Since v4.9, all voting contracts (including [`ERC20Votes`](api:token/ERC20.html#ERC20Votes) and [`ERC721Votes`](api:token/ERC721.html#ERC721Votes)) rely on [IERC6372](api:interfaces.html#IERC6372) for clock management. In order to change from operating with block numbers to operating with timestamps, all that is required is to override the `clock()` and `CLOCK_MODE()` functions.

</div>

<div class="listingblock">

<div class="content">

``` highlight
link:api:example$governance/MyTokenTimestampBased.sol[role=include]
```

</div>

</div>

</div>

<div class="sect2">

### Governor

<div class="paragraph">

The Governor will automatically detect the clock mode used by the token and adapt to it. There is no need to override anything in the Governor contract. However, the clock mode does affect how some values are interpreted. It is therefore necessary to set the `votingDelay()` and `votingPeriod()` accordingly.

</div>

<div class="listingblock">

<div class="content">

``` highlight
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Governor} from "@openzeppelin/contracts/governance/Governor.sol";
import {GovernorCountingSimple} from "@openzeppelin/contracts/governance/compatibility/GovernorCountingSimple.sol";
import {GovernorVotes} from "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import {GovernorVotesQuorumFraction} from "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";
import {GovernorTimelockControl} from "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";
import {TimelockController} from "@openzeppelin/contracts/governance/TimelockController.sol";
import {IVotes} from "@openzeppelin/contracts/governance/utils/IVotes.sol";

contract MyGovernor is Governor, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction, GovernorTimelockControl {
    constructor(IVotes _token, TimelockController _timelock)
        Governor("MyGovernor")
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(4)
        GovernorTimelockControl(_timelock)
    {}

    function votingDelay() public pure virtual override returns (uint256) {
        return 1 days;
    }

    function votingPeriod() public pure virtual override returns (uint256) {
        return 1 weeks;
    }

    function proposalThreshold() public pure virtual override returns (uint256) {
        return 0;
    }

    // ...
}
```

</div>

</div>

</div>

<div class="sect2">

### Disclaimer

<div class="paragraph">

Timestamp based voting is a recent feature that was formalized in ERC-6372 and ERC-5805, and introduced in v4.9. At the time this feature is released, some governance tooling may not support it yet. Users can expect invalid reporting of deadlines & durations if the tool is not able to interpret the ERC6372 clock. This invalid reporting by offchain tools does not affect the onchain security and functionality of the governance contract.

</div>

<div class="paragraph">

Governors with timestamp support (v4.9 and above) are compatible with old tokens (before v4.9) and will operate in "block number" mode (which is the mode all old tokens operate on). On the other hand, old Governor instances (before v4.9) are not compatible with new tokens operating using timestamps. If you update your token code to use timestamps, make sure to also update your Governor code.

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
