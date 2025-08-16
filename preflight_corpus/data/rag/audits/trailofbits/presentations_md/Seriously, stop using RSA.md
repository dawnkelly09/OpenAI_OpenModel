# Fuck RSA

Summercon 2019
Ben Perez

Fuck RSA

Lizard Person

Cancelled

Biologist

RSA invented 1977

Rivest
Shamir
Adleman
Elvis 18 23 16 21 78    +     4096     -     2920    =    1254
RSA Key
Size 2019

1254 / 2    +    39    = 6  6  6

RSA Primer

What is RSA 13

What is RSA 14

Parameter Selection

Parameter Selection 16

Primes 17
If Alice reuses p for another
RSA modulus pq’, attacker can factor using GCD

Primes 18
If Alice reuses p for another
RSA modulus pq’, attacker can factor using GCD
If p and q share approximately half of their upper bits, then pq can be factored using Fermat’s method

Primes 19
If Alice reuses p for another
RSA modulus pq’, attacker can factor using GCD
If p and q share approximately half of their upper bits, then pq can be factored using Fermat’s method
If either p or q contains too many contiguous zero bits, then pq can be factored using Coppersmith’s method

Primes 20
If Alice reuses p for another
RSA modulus pq’, attacker can factor using GCD
If p and q share approximately half of their upper bits, then pq can be factored using Fermat’s method
If either p or q contains too many contiguous zero bits, then pq can be factored using Coppersmith’s method
If p-1 or q-1 has small prime factors, then can use Pollard p-1 to factor pq

Primes 21
If Alice reuses p for another
RSA modulus pq’, attacker can factor using GCD
If p and q share approximately half of their upper bits, then pq can be factored using Fermat’s method
If either p or q contains too many contiguous zero bits, then pq can be factored using Coppersmith’s method
If p-1 or q-1 has small prime factors, then can use Pollard p-1 to factor pq

Private Exponent 22
●
Small private exponent speeds up decryption

Private Exponent 23
●
Small private exponent speeds up decryption
●
If d < ∜pq, then Eve can recover private key using continued fractions

Private Exponent 24
●
Small private exponent speeds up decryption
●
If d < ∜pq, then Eve can recover private key using continued fractions
●
Can use Chinese remainder theorem to speed up decryption instead of picking small d - vulnerable to fault attacks.

Public Exponent 25
●
Common to use e = 3, 17, 65537
● e = 3 is very bad
●
Related messages can be decrypted
●
Partial key exposure attack
●
Signature forgery

How Bad is This IRL?
26

How Bad is This IRL?
27

How Bad is This IRL?
28
Developers should not need to understand algebraic number theory to build secure software

Padding Attacks

RSA Requires Padding 30
Nuclear launch site
President

RSA Requires Padding 31
Nuclear launch site
President
“Don’t fire”
Eve

RSA Requires Padding 32
Nuclear launch site
President
“Don’t fire”
Eve

RSA Requires Padding 33
Nuclear launch site
President
“Don’t fire”
Eve
“Fire”

RSA Requires Padding 34
Nuclear launch site
President
“Don’t fire”
Eve
“Fire”

RSA Requires Padding 35
Nuclear launch site
President
“Don’t fire”
Eve

Forgery Attack 36

Forgery Attack 37

Forgery Attack 38
If e = 3, can forge signatures

Forgery Attack 39
If e = 3, can forge signatures

Padding Oracle Attacks 40

Padding Oracle Attacks 41
Padded message

Padding Oracle Attacks 42
Padded message
“Ok!”

Padding Oracle Attacks 43
Padded message
Invalid padding
X
Random junk

Padding Oracle Attacks 44
Invalid padding
Padded message X
Random junk

Padding Oracle Attacks 45
Invalid padding
Padded message X
Random junk

Padding Oracle Attacks 46
Invalid padding
Padded message X
Random junk

Padding Oracle Attacks 47
Invalid padding
Padded message X
Random junk

Padding Oracle Attacks 48
Ok!
Padded message X
Random junk

How Bad is This IRL?
49

How Bad is This IRL?
50

How Bad is This IRL?
51

How Bad is This IRL?
52

How Bad is This IRL?
53

What Should I Use Instead?

What Should I Use Instead 55

What Should I Use Instead?
56
Curve25519
X25519
Ed25519

What Should I Use Instead?
57

Final Thoughts

RSA Timeline 59 1977 - RSA invented 2019 - This talk 2005 - Suite B 2014 - libsodium

RSA Timeline 60

Wrapping Up 61
Devs talking about their custom RSA implementation
Their RSA implementation

Wrapping Up 62

Wrapping Up 63

Wrapping Up 64

Wrapping Up 65

Wrapping Up 66
“Using crypto in your application shouldn't have to feel like juggling chainsaws in the dark.” - Tink Documentation

Thanks!

Trail of Bits   |   Empire Hacking  |  02.12.2019
Contact
Ben Perez
Security Engineer benjamin.perez@trailofbits.com
@blperez_ 68