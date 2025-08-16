# 1

Joy of Pwning
Sophia d’Antoine
October 26th, 2017

2 whoami

3
Hacker Training
The World of Wargame & CTFs

7
Hacking Competition
- Wargames
-
Several weeks
-
Individual
-
FLARE Reversing Challenges (FLARE team @ FireEye)
- CTFs: 24-36 hours (no sleep)
- 24-36 hours (no sleep!)
-
Team sport
-
CSAW CTF (Hosted @ NYU)
-
CyberSeed ($50,000 in prizes)
- Why? Internet points and hacker fame (also skillz)
Further information: “Automatic Exploit Generation, an Odyssey”, CanSecWest 2016

pwnable.kr fail ...
input argv[1]
3 checks
... 15 more functions ...
memcpy fail ...

9
Current Status: CTF Field Guide https://trailofbits.github.io/ctf/

10
Security Engineering & Tooling
Why do it if you can make a program do it

11
Post Graduation: Jobs
- Pentesting/ RE/ VR/ Forensics/ IT Sec/ ...
-
Growing Field!
-
Specialization
- Public/ Private Sector
-
Private sector trends
- Security Engineering & Research
-
Tool development to better aid in security
-
Find bugs and exploit automatically
-
ML to detect Network anomalies
-
Static, Dynamic analysis
-
LLVM/ Clang compiler based research <3
Further information: “Be a Binary Rockstar, an Intro to Program Analysis with Binary Ninja”, Infiltrate 2017

12
Example: Pintool
- Binary Level
-
Inject incrementer code after each instruction
- Still Brute Force :<
-
Return total instructions for fuzzed input
-
Only true for that 1 executed path (the possible CFG space may be very large)
Further information: “Be a Binary Rockstar, an Intro to Program Analysis with Binary Ninja”, Infiltrate 2017

Software Program Analysis!

14
Symbolic/ Concolic Execution

[SYMBOL] a, b, c
[INT] x, y, z = 0; fun( int a, b, c ){ if (a) { x = -2;
} if (b < 5) { if (!a && c) { y = 1;
} z = 2;
} assert(x+y+z!=3) }
. . .
fun( 0, 3, 1 );
. . .
Old Method:
Try all inputs until assert
[WARNING] inputs unbounded!

16
Current Status: Manticore (Symbolic, Concolic)

17
Interdisciplinary Research
Security research applies to everything

18

19
Smart Contracts are Literal Programs!
●
●
○
○
○
●
○
○
●
○
Ethereum Smart Contracts

20
Room for New Security Research & Tooling

21 ethersplay

[INT OVERFLOW] Solidity contract Overflow { uint private sellerBalance = 0;

    function add(uint value) returns (bool){ sellerBalance += value; // possible overflow
        // possible auditor assert
        // assert(sellerBalance >= value);
    } function safe_add(uint value) returns (bool){ require(value + sellerBalance >= sellerBalance); sellerBalance += value;
    }
}

23
Current Status: Ongoing

High-end security research with a real-world attacker mentality
●
Security Research & Development firm specializing in:
○
High-assurance software Development
○
Low-level software security Assessments
○
Applied software security Research
● 26 people with offices in NYC, Chicago, Austin, and Toronto
● 10 people with US government security clearances
●
Founded in 2012 by 3 expert hackers, no investment capital taken to date
Trail of Bits Overview

25
Any Questions?
IRC: quend email: sophia@trailofbits.com website: www.sophia.re