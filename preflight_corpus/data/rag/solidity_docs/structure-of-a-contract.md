::: index
contract, state variable, function, event, struct, enum,
function;modifier
:::

# Structure of a Contract {#contract_structure}

Contracts in Solidity are similar to classes in object-oriented
languages. Each contract can contain declarations of
`structure-state-variables`{.interpreted-text role="ref"},
`structure-functions`{.interpreted-text role="ref"},
`structure-function-modifiers`{.interpreted-text role="ref"},
`structure-events`{.interpreted-text role="ref"},
`structure-errors`{.interpreted-text role="ref"},
`structure-struct-types`{.interpreted-text role="ref"} and
`structure-enum-types`{.interpreted-text role="ref"}. Furthermore,
contracts can inherit from other contracts.

There are also special kinds of contracts called
`libraries<libraries>`{.interpreted-text role="ref"} and
`interfaces<interfaces>`{.interpreted-text role="ref"}.

The section about `contracts<contracts>`{.interpreted-text role="ref"}
contains more details than this section, which serves to provide a quick
overview.

## State Variables {#structure-state-variables}

State variables are variables whose values are either permanently stored
in contract storage or, alternatively, temporarily stored in transien
storage which is cleaned at the end of each transaction. See
`data locations <locations>`{.interpreted-text role="ref"} for more
details.

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract SimpleStorage {
    uint storedData; // State variable
    // ...
}
```

See the `types`{.interpreted-text role="ref"} section for valid state
variable types and `visibility-and-getters`{.interpreted-tex
role="ref"} for possible choices for visibility.

## Functions {#structure-functions}

Functions are the executable units of code. Functions are usually
defined inside a contract, but they can also be defined outside of
contracts.

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.1 <0.9.0;

contract SimpleAuction {
    function bid() public payable { // Function
        // ...
    }
}

// Helper function defined outside of a contrac
function helper(uint x) pure returns (uint) {
    return x * 2;
}
```

`function-calls`{.interpreted-text role="ref"} can happen internally or
externally and have different levels of
`visibility<visibility-and-getters>`{.interpreted-text role="ref"}
towards other contracts. `Functions<functions>`{.interpreted-tex
role="ref"} accep
`parameters and return variables<function-parameters-return-variables>`{.interpreted-tex
role="ref"} to pass parameters and values between them.

## Function Modifiers {#structure-function-modifiers}

Function modifiers can be used to amend the semantics of functions in a
declarative way (see `modifiers`{.interpreted-text role="ref"} in the
contracts section).

Overloading, that is, having the same modifier name with differen
parameters, is not possible.

Like functions, modifiers can be
`overridden <modifier-overriding>`{.interpreted-text role="ref"}.

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract Purchase {
    address public seller;

    modifier onlySeller() { // Modifier
        require(
            msg.sender == seller,
            "Only seller can call this."
        );
        _;
    }

    function abort() public view onlySeller { // Modifier usage
        // ...
    }
}
```

## Events {#structure-events}

Events are convenience interfaces with the EVM logging facilities.

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.22;

event HighestBidIncreased(address bidder, uint amount); // Even

contract SimpleAuction {
    function bid() public payable {
        // ...
        emit HighestBidIncreased(msg.sender, msg.value); // Triggering even
    }
}
```

See `events`{.interpreted-text role="ref"} in contracts section for
information on how events are declared and can be used from within a
dapp.

## Errors {#structure-errors}

Errors allow you to define descriptive names and data for failure
situations. Errors can be used in
`revert statements <revert-statement>`{.interpreted-text role="ref"}. In
comparison to string descriptions, errors are much cheaper and allow you
to encode additional data. You can use NatSpec to describe the error to
the user.

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

/// Not enough funds for transfer. Requested `requested`,
/// but only `available` available.
error NotEnoughFunds(uint requested, uint available);

contract Token {
    mapping(address => uint) balances;
    function transfer(address to, uint amount) public {
        uint balance = balances[msg.sender];
        if (balance < amount)
            revert NotEnoughFunds(amount, balance);
        balances[msg.sender] -= amount;
        balances[to] += amount;
        // ...
    }
}
```

See `errors`{.interpreted-text role="ref"} in the contracts section for
more information.

## Struct Types {#structure-struct-types}

Structs are custom defined types that can group several variables (see
`structs`{.interpreted-text role="ref"} in types section).

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract Ballot {
    struct Voter { // Struc
        uint weight;
        bool voted;
        address delegate;
        uint vote;
    }
}
```

## Enum Types {#structure-enum-types}

Enums can be used to create custom types with a finite set of \'constan
values\' (see `enums`{.interpreted-text role="ref"} in types section).

``` solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract Purchase {
    enum State { Created, Locked, Inactive } // Enum
}
```
