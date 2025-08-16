# Contract upgrade risks and remediations


Who Am I
●
●
●
● 2

Goals
●
●
●
● 3

Upgradability

Smart contracts
●
● 5

Immutability
●
●
●
●
●
● 6

●
●
●
●
Contract Upgradability 7

Data Separation

Data Separation
●
●
● 9
User
Logic Contract
Data Contract
Call

How to Upgrade
● 10
User
New
Logic Contract
Data Contract
Call
Old
Logic Contract

Data Separation 11 contract Logic{
  Data data; function inc() public{ data.setV(data.v() + 1);
  } function v() public returns(uint){ return data.v();
  } contract Data is Owner { uint public v; function setV(uint new_v) onlyOwner public { v = new_v;
 }
User
Logic Contract
Data Contract
Call

Data Separation: logic alternative
●
● 12
New
Logic Contract
Data Contract
Call
Old
Logic Contract
User
Proxy
Call

Data Separation: Recommendations
●
●
●
●
●
●
● 13

Delegatecall Proxy

EVM Internals
●
●
●
●
●
● 15

delegatecall instruction
●
●
●
●
●
● 16

library Lib { struct Data { uint val; } function set(Data storage self, uint new_val) public { self.val = new_val;
  }
} contract C {
  Lib.Data public myVal; function set(uint new_val) public {
    Lib.set(myVal, new_val);
  }
}
Library 17

delegatecall
●
●
● really 18

Upgradability through delegatecall
●
●
●
● 19
User
Logic Contract
Proxy Contract
(holds data)
delegatecall

Upgradability through delegatecall
●
●
● 20

Delegatecall Example contract Proxy { uint public a; address public pointer;
 ...
 function () public { pointer.delegatecall(..)
 }
} contract MyContract_v1 { uint public a; address public pointer; function set(uint val) public { a = val;
 }
} 21 address pointer uint a uint a
Proxy
MyContract_v1 address pointer

contract Proxy { uint public a; address public pointer;
 ...
 function () public { pointer.delegatecall(..)
 }
} contract MyContract_v1 { uint public a; address public pointer; function set(uint val) public { a = val;
 }
}
Delegatecall Example 22 contract MyContract_v2 { address public pointer; uint public a; function set(uint val) public { a = val;
 }
} address pointer uint a uint a
Proxy address pointer
MyContract_v1

contract Proxy { uint public a; address public pointer;
 ...
 function () public { pointer.delegatecall(..)
 }
} contract MyContract_v1 { uint public a; address public pointer; function set(uint val) public { a = val;
 }
}
Delegatecall Example 23 address pointer uint a
MyContract_v2 address pointer uint a uint a contract MyContract_v2 { address public pointer; uint public a; function set(uint val) public { a = val;
 }
}
Proxy address pointer
MyContract_v1

Examples of incorrect upgrades 24 contract is A, B{
  ….
contract is B, A{
  ….
contract A{ uint a; uint b; contract A{ uint8 a; uint8 b; contract A{ uint a; uint b;
} contract B is A{
...
contract A{ uint a;
} contract B is A{
...

Delegatecall Proxy: Recommendations
●
●
●
●
● 25

Delegatecall Proxy: Recommendations
●
●
●
●
●
● 26

●
●
●
●
Delegatecall Proxy: Recommendations 27

Upgradability: Summary

●
●
●
●
●
●
●
●
●
Upgradability: Summary 29

Upgradability: recommendations
●
●
●
● 30

Alternative?
Contract Migration

Contract Migration
● 32

Why do you need a Migration?
●
●
●
●
●
● 33

●
●
●
How to perform a migration?
34

Migration versus Upgradability
●
●
●
●
●
●
● 35

Migration versus Upgradability
●
●
●
● 36

Takeaway
●
●
●
● 37

●
● 38