# Automatically Detecting

Variability Bugs Through Hybrid
Control and Data Flow Analysis
Kelly Kaoudis, Henrik Brodin, Evan Sultanik
LangSec Workshop at IEEE S&P, 25 May 2023

Variability bug: run-to-run (over the same input) software execution divergence due to build conﬁguration or environment

Goal: detect and correctly diagnose runtime
C and C++ variability bugs
(with multiple causes)

“That should be easy to ﬁgure out with UBSan, right?”
●
UBSan helps detect some but not all types of UB
●
UBSan cannot detect all types of variability bug
●
Detection != correct diagnosis
●
Tells you there is a bug (detection) and roughly where, but does not help with further diagnosis actions
●
May not help at all, due to build conﬁguration

$ clang++ -Wall -o toy -std=c++20
-DPRODUCTION -O2 toy.cpp
$ ./toy 63
$ echo $?
0
$ clang++ -Wall -o toy0 -std=c++20 -O0 toy.cpp
$ ./toy0 63 toy0: toy.cpp:11: int main(int, char **):
Assertion `shift > 0 && shift < 32' failed.
[1]    500225 abort      ./toy0 63
D
E
B
U
G
P
R
O
D

$ clang++ -Wall -o toy0 -std=c++20 -O0 toy.cpp
$ ./toy0 63 toy0: toy.cpp:11: int main(int, char **):
Assertion `shift > 0 && shift < 32' failed.
[1]    500225 abort      ./toy0 63
$ clang++ -Wall -o toy0 -std=c++20 -O0
-fsanitize=undefined toy.cpp
$ ./toy0 63 toy0: toy.cpp:11: int main(int, char **):
Assertion `shift > 0 && shift < 32' failed.
[1]    500413 abort      ./toy0 63
D
E
B
U
G
U
B
S
A
N
🤔

$ clang++ -Wall -o toy0 -std=c++20 -O0
-fsanitize=undefined toy.cpp
$ ./toy0 63 toy0: toy.cpp:11: int main(int, char **):
Assertion `shift > 0 && shift < 32' failed.
[1]    500413 abort      ./toy0 63
$ clang++ -Wall -o toy -std=c++20 -O2
-DPRODUCTION -fsanitize=undefined toy.cpp
$ ./toy 63 toy.cpp:12:21: runtime error: shift exponent 63 is too large for 32-bit type
'int'
SUMMARY: UndefinedBehaviorSanitizer:
undefined-behavior toy.cpp:12:21
D
E
B
U
G
P
R
O
D

↓ This would be awesome ↓
        DEBUG  | fn | PROD 1| {0,1,2,3}   | f0 | {0,1,2,3} 2| {8,9,10,11} | f1 | {8,9,10,11} 3| {8,9,10,11} | f2 | 4| {8,9,10,11} | f2 | 5|             | f0 | {8,9,10,11}

        DEBUG  |       function symbol            | PROD 1| {0,1,2,3}   | int main(int argc, char* argv[]) | {0,1,2,3} 2| {8,9,10,11} | int std::atoi(const char* str)   | {8,9,10,11} 3| {8,9,10,11} | void assert(int expression)      | 4| {8,9,10,11} | void assert(int expression)      | 5|             | int main(int argc, char* argv[]) | {8,9,10,11}
↓ This would be *really* awesome ↓
        DEBUG  | fn | PROD 1| {0,1,2,3}   | f0 | {0,1,2,3} 2| {8,9,10,11} | f1 | {8,9,10,11} 3| {8,9,10,11} | f2 | 4| {8,9,10,11} | f2 | 5|             | f0 | {8,9,10,11}

↓ This would be *really* awesome ↓
?
?
        DEBUG  | fn | PROD 1| {0,1,2,3}   | f0 | {0,1,2,3} 2| {8,9,10,11} | f1 | {8,9,10,11} 3| {8,9,10,11} | f2 | 4| {8,9,10,11} | f2 | 5|             | f0 | {8,9,10,11}
        DEBUG  |       function symbol            |  PROD 1| {0,1,2,3}   | int main(int argc, char* argv[]) | {0,1,2,3} 2| {8,9,10,11} | int std::atoi(const char* str)   | {8,9,10,11} 3| {8,9,10,11} | void assert(int expression)      | 4| {8,9,10,11} | void assert(int expression)      | 5|             | int main(int argc, char* argv[]) | {8,9,10,11}
./toy 63

Challenge #1
How to successfully detect?

Parser differential basics input input
Input
Binary A
Binary B
Output A
Output B
SAME

Program output differential basics input input
Input
Binary A
Binary B
Output A
Output B
SAME
X

Challenge #2
Can we “rewind” execution (enough) to correctly diagnose the contributing factors?

PolyTracker’s Data Flow Representation 0 1 2 3 4 5 6 7 0,1 0, 1, 2 0, 1, 2, 3 0, 4 0, 4, 5 0, 4, 5 ,6 5, 7

Avoid FPs and reduce extra detail
●
Start from too much, reduce to helpful representation
●
Control ﬂow (function, BB identiﬁers, …) as waypoints
●
Label all waypoints by nearest function identiﬁer, f()id
●
When data ﬂow passes through a waypoint, create a control-affecting data ﬂow log entry mapped to f()id
●
Map f()ids to human-readable program symbols

Program representation:
Hybrid control and data ﬂow
Control-affecting data ﬂow

Control-Affecting Data Flow
                                                 Data Flow 0f0 4f0 5f2 7f3 0,1f0 0, 1, 2 f1 0, 1, 2, 3f4 5, 7f3 0 1 2 3 4 5 6 7 0,1 0, 1, 2 0, 1, 2, 3 0, 4 0, 4, 5 0, 4, 5 ,6 5, 7 f0, f1, f2, f3, f4, f5, f6, ...
Waypoint (Control Flow) Identiﬁers

Method summary
●
For each program variant, build the program representation
○ 2x llvm dynamic instrumentation passes
■
Before front end optimization (new!)
■
After front end optimization (PolyTracker original)
○
When data ﬂow passes through a waypoint f()id , map f()id to parent input byte(s) bi…bn
○
Can check instrumentation is transparent!!
●
Compare f()ids at matching input byte sets bi…bn
●
Map opaque f()id s to de-mangled symbols (from the pre-opt llvm pass)

Preliminary Evaluation

Example: Nitro
●
Reference parser for public NITF speciﬁcations
○
NITF: visual data (mp4, jpeg, ﬁngerprints, …) + text (captions, …)
in a binary ﬁle format package
○
Implements the mutually incompatible MIL-STD-2500{A, B, C}
○
Bespoke stdlib fn implementations baked into build system
●
Small known-valid and known-invalid input corpus
(148 NITFs) to start with
●
Found and diagnosed 3 bugs in Nitro; more to come!

Result: Nitro
●
Last byte offset affecting control ﬂow before divergence: 756 ‘Y’
●
Nearest identiﬁer: showImages(nitf::Record const&)
●
Last thing Nitro runs: TRY_SHOW(imsub.imageRepresentation());
●
Manual (for now) mapping back of byte offset to NITF speciﬁcation
ﬁelds: IREP (Image Representation)
●
Field value in input: YCbCr601

Future directions :D
●
Evaluate different types of binary ﬁle or image format parsers
●
Better differential metrics - graph similarity clustering
●
More experiments evaluating Nitro, too
●
Integrate other Trail of Bits tools into our analysis
○
Graphtage for improved control-affecting data ﬂow matching up
○
Polyﬁle for mapping back last related input byte offset to spec
○
Maybe: run PolyTracker over an MLIR (from VAST) instead of bitcode?
●
Integrate our analysis into Galois’ Format Analysis Workbench (FAW)?
●
What else would you like to see? We are open to ideas

Summary
Code: github.com/trailofbits/polytracker
Contact: kelly.kaoudis@trailofbits.com, henrik.brodin@trailofbits.com, evan.sultanik@trailofbits.com
Special thanks to our shepherd Sergey, our awesome reviewers, and our colleagues Nathan, Marek, Peter, Dominik, Lisa, Jay, and Michael.
●
Learned the limits of existing compiler-rt sanitizers!
●
New program representation enabling variability bug analysis!
●
We found that following the control ﬂow input bytes exercised helps trace back to to the root(s) of a divergence!
●
Detected and diagnosed variability bugs in real software!
Thank you!