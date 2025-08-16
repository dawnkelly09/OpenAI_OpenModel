# Differential fuzzing, or: how to ﬁnd bugs when (ground) truth isn’t real

William Woodruff
OSIRIS Lab

Hi
●
Me
○
𝓼𝓮𝓷𝓲𝓸𝓻 security engineer (certiﬁed good at computers)
○
R&D: program analysis research (mostly LLVM)
○
Engineering: open-source C, C++, Rust, Ruby, Python
●
Trail of Bits
○
About 60 people, ~30% in NYC, rest remote
○
Research, engineering, assurance
○
Very good
○
Summer and winter internships 2

Today’s agenda
●
Finding bugs
●
Finding bugs with fuzzing
●
Normal fuzzing can’t ﬁnd some bugs :(
○
We don’t even know what bugs are, actually
●
Spicy (diﬀerential) fuzzing to ﬁnd those bugs
●
Example case: x86_64 decoding
○
Demo!!!
3

Finding bugs
●
Why? We want to...
○ write reliable, safe code (cred)
○ embarrass our coworkers (more cred)
○ embarrass help our clients (money)
●
How?
○
Manual code review
■
Expensive (money & time), fallible (goto fail)
○
Static analysis, formal methods, symbolic execution
■
Cheap-ish (compute heavy), sometimes eﬀective, often indefeasible (luv 2 explode state)
○
Fuzzing 4

Finding bugs with fuzzing
●
The TL;DR of fuzzing: feed garbage into the program until it crashes
●
Inexpensive, shockingly good at discovering (exploitable) bugs
●
Problem: random inputs won’t explore the program much
○
Intuition: Most random inputs don’t resemble HTML, ZIP streams, PNGs…
●
Solution: Use a feedback mechanism to guide inputs
○
“If it <runs longer/calls more functions/has more coverage>, try similar inputs” 5

Not all bugs are easily fuzzable
●
Not all bugs…
○ cause easy-to-observe crashes (segfaults, aborts, non-zero exits, &c)
○ are memory corruptions (logic errors, permission errors, DoS, &c)
●
If we have a speciﬁcation, we can instrument the program to turn non-crashing errors into discoverable crashes 7

What’s a bug without a speciﬁcation?
●
Not everything has a real speciﬁcation
●
Lots of things have “speciﬁcations” that are basically ignored
●
The real spec is generally-agreed-upon behavior
○
“What does Adobe Acrobat do? Make our program do that”
●
Lots of things are written in memory safe languages
○
== no memory corruption == no crashes on “bugs”
○
+ no speciﬁcation == no easy instrumentation approach :( 8

Another perspective: ground truth and oracles
●
Restate the problem: instead of bugs, we want an oracle
●
Oracle supplies some notion of “ground truth”
○ a yes or no answer for whether some behavior is correct
●
Diﬀerent oracles:
○
C and C++: segfaults, assertions, non-zero exits
○
Memory safe languages: exceptions, assertions, contract violations
●
Still no oracle if a “bug” doesn’t cause any of these!
○
Back where we started :( 9

Constructing ground truth from difference
●
Observation: lots of things have multiple implementations
○
Multiple PDF parsers, ZIP extractors, HTTP header parsers
●
Observation: lots of programs copy ideas and features from competitors
○
“Acrobat can do $X so our program needs to be able to do $X!”
●
Observation: copying features without a speciﬁcation means underspeciﬁcation + lots of variation on unexpected inputs
●
What if we compared diﬀerent implementations?
○
What if we deﬁne “bug” == “diﬀerence between impls”?
10

Differential fuzzing: we can’t all be right 11 input pdf1.exe pdf2.exe pdf3.exe
●
Three programs, two diﬀerent results (     and      , italic vs. bold)
●
Not clear which is “right”, but both probably aren’t
●
No crashes needed!
●
What if this but automated?
Foo bar
Foo bar
Foo bar

Differential fuzzing: applications
●
Any complex, popular format with competing implementations
○
PDF, Word, media container formats (MKV, MP4)
●
Crypto primitives (hashing, digital signatures)
○
Prior work: Wycheproof (Google), CDF (Kudelski)
●
Competing hardware implementations of ISAs
○ x86_64: sandsifter
●
Competing software decoders for ISAs
○
ARM: MC-Hammer
○ x86_64: mishegos (us!)
12

Case study: x86_64 decoding
●
Ideal target for diﬀerential fuzzing:
○
Large, messy ISA with thousands of unique instructions
○
Complex encoding format with >50 years of backwards compatibility
○
Variable-length instructions, unlike ARM! Up to 15 bytes!!!
○
Two major vendors with totally independent implementations: Intel, AMD
○
Lots of popular, open source decoders to compare:
■
Capstone (mostly LLVM), zydis, XED (Intel), libopcodes (GNU)
○
High-interest/impact bugs:
■
Mess up debuggers, RE platforms, static analysis tools, ...
13

Case study: x86_64 decoding
The basic idea:
●
Spawn a bunch of workers that wrap diﬀerent decoder impls.
●
Blast “random” inputs at the workers
○
Not really random: use x86_64’s structure to inform our choices
■
Legacy preﬁxes, SIB byte, &c
●
Record what each worker claims each input decodes to
●
Compare and contrast
●
?? Bugs ??
14

Mishegos: differential fuzzing for x86 decoders 15

Mishegos: making sense of the noise 16
●
Results: ~tens of millions of results per hour
○
Depends on the number of workers, system load, …
●
Need an automated strategy for ﬁltering the interesting results
●
Observation: we want a list (or DAG?) of ﬁlters to run, biggest ﬁrst
●
Implemented as “passes” (think LLVM) on transformed (JSON) output
●
Boils down to this pipeline:

Contact Slide
William Woodruff
Senior Security Engineer william@trailofbits.com
@8x5clPW2  |  github.com/woodruffw 17