# Safely Integrating ERC20 Tokens to

Your DeFi Application

●
●
○
○
■
■
■ 2

●
●
● 3

General considerations

●
●
●
●
● 5

●
●
●
●
●
● 6

ERC conformity

8
● 1.
function get(ERC20 token) internal returns(uint, uint8){ 2.
   uint8 decimals = token.decimals(); 3.
   uint balance = token.balanceOf(address(this)); 4.
   return balance, decimals; 5.
}

9

● 10

●
●
● 11

●
●
●
● require(token.transfer(..,..)); 12

●
●
●
●
●
● 13

●
●
●
●
●
●
●
● 14

15

Extensions Risks

●
●
● 1.
function withdraw(ERC20 token) internal{ 2.
   require(token.transfer(msg.sender, balance[msg.sender])); 3.
   balance[msg.sender] = 0; 4.
} 17

● 1.
function add(uint value) internal{ 2.
   require(token.transferFrom(msg.sender, address(this), value)); 3.
   balance[msg.sender] += value; 4.
} 18

●
●
●
●
●
● 19

Contract Composition

●
●
● 21

●
●
● 22

23

●
●
●
● 24

Testing Basic Properties

●
●
●
●
●
●
●
●
● 26

Owner privileges

●
●
●
●
●
● 28

●
●
●
● 29

●
● 30

Token scarcity

●
●
●
●
●
● 32

●
●
●
● 33

Summary

●
●
○
○ 35