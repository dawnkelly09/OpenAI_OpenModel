# 1

Ethereum Security
Dan Guido (@dguido)

Trail of Bits
High-end security research with a real -world attacker mentality
●
Security research & development ﬁrm specializing in:
○
High-assurance software Development
○
Low-level software security Assessments
○
Applied software security Research
● 42 people with oﬃces in NYC, San Diego, LA, Austin, and Toronto
●
Founded in 2012 by 3 expert hackers w/ no investment capital

3
What is Ethereum?

4
Ethereum
●
It’s a “cryptocurrency” (ether)
●
It’s a virtual machine that runs smart contracts
●
It’s the 2nd largest cryptocurrency by valuation

5
Ethereum entities
People with Wallets
● balance
“Contract Account”
● balance
● code

6
Solidity
●
JavaScript-inspired high-level language for smart contracts
●
Compiles to EVM, a native machine code for Ethereum
●
Is the source of nearly all of Ethereum’s issues

7
Solidity enables mistakes
●
Integer overﬂow/underﬂow
●
Incomplete initialization
●
Uninitialized variables
●
Callbacks / re-entrancy
●
Variable name shadowing
●
Type inference (var keyword)
●
Array.length
●
Inline Assembly
●
Divide by zero
●
Race conditions / replay attacks
●
Bad random number generation
●
Time sensitivity
●
Using blockchain as random

8
Consequences

9
Breaking Smart Contracts

10
Step 1: Sort by Value

11
Step 2: Choose literally any contract

12
Step 3: Read the warnings

13
Step 4: Write an exploit

14
Security Tools & Techniques

Not So Smart Contracts https://github.com/trailofbits/not-so-smart-contracts

Slither: Smart contract static analysis
Features
●
Solidity vulnerability detection with low false positives
●
Detection of all major smart contract vulnerabilities
●
Easily integrated into CI pipeline
●
Integrates with Etherscan to obtain contract source
Detections
●
Extensive list of existing vulnerability detectors:
○
Re-entrancy (DAO hack)
○
Missing constructor (Parity MultiSig Hack #1)
○
Uninitialized variables (Parity MultiSig Hack #2)
○
Variable shadowing (most honey pots)
○
Unimplemented functions (missed by solc)
○
Unsafe mapping deletion (missed by solc)
●
Detection of poor coding practices
●
Detector Python API supports writing custom analysis
Inputs
●
Solidity source code
Outputs
●
Static analysis errors and warnings
●
Inheritance graph and contract summary
Slither is available to clients of Trail of Bits https://github.com/trailofbits/slither

Echidna: Smart contract testing
Features
●
Uses smart fuzzing and input generation to:
○
Generates and execute many contract inputs
○
Generate intelligent, grammar-based inputs
○
Seamlessly integrate into developer workﬂows
○
Run thousands of generated inputs per second
○
Automatically generate minimal testcases
●
Highly extensible via Haskell API
Inputs
●
Solidity smart contract
●
Simple Solidity tests
Outputs
●
List of invariants that Echidna was able to violate
●
Minimal call sequences to trigger discovered violations
Echidna is open source!
https://github.com/trailofbits/echidna

Manticore: Smart contract veriﬁer
Features
●
Uses symbolic execution of EVM to:
○
Deeply explore possible contract states across multiple transactions and contracts
○
Discover functions directly from bytecode
○
Detect contract ﬂaws like int overﬂows, uninitialized memory/storage usage, and more
○
Verify customized program assertions
●
Highly scriptable and extensible via Python API
Inputs
●
Solidity smart contract (optional)
●
Ethereum Virtual Machine (EVM) bytecode
Outputs
●
List of detected ﬂaws and inputs to reach them
●
Transactions that trigger all discovered paths
●
Execution traces of discovered paths
●
Code coverage obtained by analysis
Manticore is open source!
https://github.com/trailofbits/manticore

19
Key Takeaways

20
Key takeaways 1.
Ethereum enables automated ﬁnance bots
○
Languages and tooling for them are early stage
○
Many eﬀorts to use them have resulted in hacks 2.
Hacking smart contracts is easy
○
Solidity leaves room for many potential ﬂaws
○
Anyone can send input to any contract 3.
This is a greenﬁeld to apply research
○
Unforgiving smart contracts create demand for it
○
We set the bar for the ﬁrst generation of tools
Contact
Dan Guido, Founder & CEO dan@trailofbits.com
Follow us on Twitter:
@trailofbits
@dguido www.trailofbits.com github.com/trailofbits blog.trailofbits.com