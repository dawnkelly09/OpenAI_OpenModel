# CYBER

  GRAND
  CHALLENGE
  
Ryan
  Stortz
  
Trail of
  Bits
  
12
  August 2015
  

CAPTURE
  THE
  FLAG
  

Capture the
  Flag
  
•  Capture the
  Flag is a compe22on that tests a variety of computer
  
security-­‐related skills.
  

  
•  Challenge areas include:
  
–  Cryptanalysis
  
–  Forensics
  
–  Network
  Analysis
  
–  Network and
  Applica2on
  Exploita2on
  
–  Programming
  
–  Reverse
  Engineering
  
–  Trivia
  

CTF
  Compe22on
  Format
  
Blue
  Team
  
Red
  Team
  
Full
  Spectrum
  

Blue
  Team
  
•  Focused on
  IT
  Security
  
– Collegiate
  Cyber
  Defense
  Compe22on
  (CCDC)
  
– CyberPatriot
  
•  Largely
  IT security compe22ons
  
– Some2mes described as
  “Patch and
  Pray”
  
•  Embraces the term
  “Cyber”
  

Red
  Team
  
•  Scoreboard-­‐driven compe22ons
  
– Ghost in the
  Shellcode
  
– PlaidCTF
  
– CSAW
  CTF
  
•  By far the most popular
  
– Interna2onal scores are tracked
  @
  
www.cQ2me.org
  
  

Full
  Spectrum
  
•  ARack-­‐Defense
  
–  DEFCON
  CTF
  
–  RuCTFe
  
•  Most dynamic of the three formats
  
–  Basically unrestricted cyber war in a single room
  
•  Teams host and patch custom vulnerable
  
services, while aRacking the same services run by
  
other teams.
  

Why does this maRer?
  
• 
Many people believe
  CTF is the best crucible for tool
  & strategy development
  
– 
Speciﬁcally
  Full
  Spectrum compe22ons
  

  
• 
HatesIrony made custom tools for:
  
– 
Reverse
  Engineering
  
– 
Packet
  Analysis
  
– 
Automated
  Network
  Exploita2on
  
– 
Key/Flag
  Submission
  
– 
Run2me
  Applica2on
  Defenses
  
– 
Network
  De-­‐anonymiza2onTools
  
• 
...and we threw them out each year as the game evolved
  
hRps://binary.ninja/
  
  

THE
  CYBER
  GRAND
  CHALLENGE
  

ARPANET
  
1969
  
Siri
  
2003
  
Grand
  Challenge
  
2004
  

CTF
  Nerds
  +
  DARPA
  

Cyber
  Grand
  Challenge
  
“Cyber
  Grand
  Challenge
  (CGC)
  is a contest to
  
build high-­‐performance computers capable of
  
playing in a
  Capture-­‐the-­‐Flag style cyber-­‐security
  
compe22on.”
  

  

  

Humans
  >
  Robots
  
*
  Yes, even at soiware
  

Compe22on
  Setup
  
•  Teams build
  “Cyber
  Reasoning
  Systems”
  
–  Fully autonomous systems
  
•  Given a bundle of
  Challenge
  Binaries
  (CBs)
  
–  CB
  :=
  “Pwnables”
  
•  Teams create
  Proof of
  Vulnerabili2es
  (PoV)
  
–  PoVs are inputs that trigger vulnerable code paths
  (via
  
a crash)
  
•  CRSs will compete against each other
  

DECREE
  
•  OS:
  DECREE
  
–  DARPA
  Experimental
  Cyber
  Research
  Evalua2on
  
Environment
  
–  Similar to
  Linux x86
  
–  Executables are sta2cally-­‐linked
  ELFs
  
–  Implemented as a new binfmt
  
•  Removes complexity
  
•  Very clever implementa2on
  
#
  
Syscall
  
Linux
  Eq.
  
1
  
_terminate
  
exit
  
2
  
transmit
  
send
  
3
  
receive
  
  
recv
  
4
  
fdwait
  
select
  
5
  
allocate
  
mmap
  
6
  
deallocate
  
munmap
  
7
  
random
  
n/a
  

Example
  Challenge
  
Example
  Challenge:
  CADET_0001
  

OUR
  CYBER
  REASONING
  SYSTEM
  

Bug
  Finding
  
•  Fuzzing
  
•  Symbolic
  Execu2on
  
•  Concolic
  Execu2on
  
– Concrete
  +
  Symbolic….get it?
  Ha ha…
  

FUZZING
  

Fuzzing
  
•  Fuzzing is a technique where you take valid
  
inputs, corrupt them slightly, feed them
  
through an applica2on, and hope for a crash.
  

  
•  Extremely eﬀec2ve for many
  ﬁle formats
  
•  Requires good input data to be truly eﬀec2ve
  

Granary
  -­‐
  Binary
  Transla2on
  
•  Persistent
  Code
  Cache
  
•  Code
  Coverage
  
•  No
  System
  IO
  
– Granary emulated all of it
  
•  One instance
  = 400,000 test cases/hour
  
– We had
  ~10,000 instances for the qualiﬁer
  

Minset
  
•  Collects the
  “Minimum
  Set” of inputs to cause
  
the maximum amount of path coverage.
  
80%
  
17%
  
3%
  
33%
  
33%
  
33%
  

SYMBOLIC
  EXECUTION
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
-­‐
  
Y
  
RV
  
-­‐
  
-­‐
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
0
  
Y
  
RV
  
0
  
-­‐
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
0
  
Y
  
RV
  
0
  
-­‐
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
0
  
Y
  
RV
  
0
  
-­‐
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
0
  
Y
  
RV
  
1
  
-­‐
  

  ExecuNon
  :
  Symbolic
  Execu2on
  ::
  ArithmeNc
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
5
  
12
  
0
  
Y
  
RV
  
1
  
1
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
-­‐
  
Y
  
RV
  
-­‐
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
0
  
Y
  
RV
  
0
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
0
  
Y
  
RV
  
0
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
2∧(a==2)
  
Y
  
RV
  
0
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
2∧(a==2)
  
Y
  
RV
  
0
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
2∧(a==2)
  
Y
  
RV
  
1∧(b>10)
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
2∧(a==2)
  
Y
  
RV
  
1∧(b>10)∨b∧(b≤10)
  
-­‐
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
A
  
B
  
X
  
?
  
?
  
2∧(a==2)
  
Y
  
RV
  
1∧(b>10)∨b∧(b≤10)
  
2∧(a==2)
  + 1∧(b>10)∨b∧(b≤10)
  

  Execu2on
  :
  Symbolic
  ExecuNon
  ::
  Arithme2c
  :
  Algebra
  

  
  1 int ex(int a, int b)
  

  
  2
  {
  

  
  3
  
  
  
  
  int x
  = 0, y
  = 0;
  

  
  4
  

  
  5
  
  
  
  
  if
  (a
  == 2)
  {
  

  
  6
  
  
  
  
  
  
  
  
  x
  = 2;
  

  
  7
  
  
  
  
  }
  

  
  8
  

  
  9
  
  
  
  
  if
  (b
  > 10)
  {
  

  10
  
  
  
  
  
  
  
  
  y
  = 1;
  

  11
  
  
  
  
  } else
  {
  

  12
  
  
  
  
  
  
  
  
  y
  = b;
  

  13
  
  
  
  
  }
  

  14
  

  15
  
  
  
  
  return x
  + y;
  

  16
  }
  
a=2
  

  b=?
  
a=?
  

  b>10
  
a=?
  

  b≤10
  
#
  
A
  
B
  
1
  
==2
  
>10
  
2
  
==2
  
≤10
  
3
  
!=2
  
>10
  
4
  
!=2
  
≤10
  

Input genera2on with
  SMT-­‐LIB
  
(declare-­‐fun
  V_4
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_5
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_6
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_7
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_12
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_1
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_2
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_3
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  MEM
  ()
  (Array
  (_
  BitVec 32)
  (_
  BitVec 8)))
  
(declare-­‐fun
  V_10
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_11
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_8
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  V_9
  ()
  (_
  BitVec 32))
  
(declare-­‐fun
  RECEIVE
  ()
  (Array
  (_
  BitVec 32)
  (_
  BitVec 8)))
  
(declare-­‐fun
  V
  ()
  (_
  BitVec 32))
  
(assert
  (=
  V_11
  (let
  ((a!1
  ((_ extract 31 7)
  

  

  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000000))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000000)))
  

  
  
  
  
  
  
  
  ((_ extract 5 3)
  (select
  RECEIVE
  #x00000000))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 2 2)
  (select
  RECEIVE
  #x00000000)))
  

  
  
  
  
  
  
  
  ((_ extract 1 0)
  (select
  RECEIVE
  #x00000000)))))
  
(assert
  (=
  V_7
  (let
  ((a!1
  ((_ extract 31 3)
  

  
  
  
  
  
  
  
  
  
  
  
  
  (bvadd
  #xbebdbcbc
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (concat
  (select
  RECEIVE
  #x00000003)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000002)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000))))))
  

  
  (concat
  #b000 a!1))))
  
(assert
  (=
  V
  (concat
  ((_ extract 7 7)
  (select
  RECEIVE
  
#x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 5 1)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 1)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000001)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 0)
  (select
  RECEIVE
  #x00000001)))
  

  

  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000)))
  

  
  
  
  
  
  
  V_4)))
  
(assert
  (=
  V_4
  (let
  ((a!1
  ((_ extract 31 1)
  

  
  
  
  
  
  
  
  
  
  
  
  
  (bvadd
  #xbebdbcbc
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (concat
  (select
  RECEIVE
  #x00000003)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000002)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000))))))
  

  
  (concat
  #b0 a!1))))
  
(assert
  (=
  V_9
  (let
  ((a!1
  ((_ extract 31 5)
  

  
  
  
  
  
  
  
  
  
  
  
  
  (bvadd
  #xbebdbcbc
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (concat
  (select
  RECEIVE
  #x00000003)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000002)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000))))))
  

  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000)))
  

  
  
  
  
  
  
  V_4)))
  
(assert
  (=
  V_4
  (let
  ((a!1
  ((_ extract 31 1)
  

  
  
  
  
  
  
  
  
  
  
  
  
  (bvadd
  #xbebdbcbc
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (concat
  (select
  RECEIVE
  #x00000003)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000002)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000))))))
  

  
  (concat
  #b0 a!1))))
  
(assert
  (=
  V_9
  (let
  ((a!1
  ((_ extract 31 5)
  

  
  
  
  
  
  
  
  
  
  
  
  
  (bvadd
  #xbebdbcbc
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (concat
  (select
  RECEIVE
  #x00000003)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000002)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000001)
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  (select
  RECEIVE
  #x00000000))))))
  
(assert
  (=
  V
  (concat
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 5 1)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 1)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000001)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 0)
  (select
  RECEIVE
  #x00000001)))
  
(assert
  (=
  V
  (concat
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 5 1)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 1)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000001))
  
  
  
  
  
  
  
  
  
(bvnot
   (( extract 6 6)
   (select
   RECEIVE
   #x00000001)))
  
(assert
  (=
  V
  (concat
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 5 1)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 1)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000001)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 0)
  (select
  RECEIVE
  #x00000001)))
  
(assert
  (=
  V
  (concat
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 5 1)
  (select
  RECEIVE
  #x00000003))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000003)))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 5 2)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 1 1)
  (select
  RECEIVE
  #x00000002)))
  

  
  
  
  
  
  
  
  ((_ extract 0 0)
  (select
  RECEIVE
  #x00000002))
  

  
  
  
  
  
  
  
  ((_ extract 7 7)
  (select
  RECEIVE
  #x00000001))
  

  
  
  
  
  
  
  
  (bvnot
  ((_ extract 6 6)
  (select
  RECEIVE
  #x00000001)))
  
  
  
  
  
  
  
  
  
((
  
  
  
)
   (
  
  
))
  

PATCHING
  

Automated
  Patching
  
•  We convert
  CBs to
  LLVM
  IR with
  McSema
  
•  We iden2fy all taint input sources
  
•  Locate all tainted loads and stores
  
– In loops only
  (as an op2miza2on)
  
•  Added checks to verify they’re safe
  

How
  Replacement
  Binaries are made
  

Challenge
  
Binary
  
McSema
  
LLVM
  IR
  
Patch
  
Replacement
  
Binary
  

DEMO
  

QUESTIONS?