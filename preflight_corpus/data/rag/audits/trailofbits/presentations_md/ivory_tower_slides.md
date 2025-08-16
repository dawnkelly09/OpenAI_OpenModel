# From One Ivory Tower to Another:

Wish Listing for Filling the Gaps in
Information (In)Security
Vincenzo Iozzo
Director of Security Engineering
Trail of Bits, Inc

My ivory tower

The security community is fixated on persistence

The mantra: “whoever scores is right”

Technical elegance is highly valued

Essentially: results trump (almost) everything

This happens a lot..
..while reading academic papers

The NSA and your ivory tower

The NSA says..

Is this it?

How do we make the relationship better?

Note

Given the audience we will mostly focus on
FUD (or “the future” if you prefer)

Problem

Most of the problems we deal with are either intractable or undecidable in the general case

Small, overlooked fact
 Exploitation is successful due to specificity

Thesis/Solution

 Get specific, get practical

Mostly two topics

Vulnerability discovery

Exploitation

Vulnerability Discovery

Success stories

HAVOC/HAVOC-LITE (Julien Vanegue et al)

Bochspwn (Jurczyk et al)

Chucky (Fabian Yamaguchi et al)

HAVOC-LITE
Check reference counting issues in COM interfaces

Solution: Add a ghost property to the model of the object to check for QueryInterface correctness

Bochspwn
Ring0/Ring3 Race conditions in Windows

Solution: Instrument a Windows machine with
Bochs to log memory access. Enhance the analysis by:
 1) only analyzing reads > 1 byte 2) same-size consecutive reads 3)  remove known useless patterns 4) more stuff..

Chucky
Find missing checks

Solution: Automate the natural “pattern matching” work that bug-hunters do through anomaly detection based on other instances of similar code snippets inside the application

So.. What to focus on?

Novel (this goes without saying, right?)

Hard

Driven by real world-data

Practical

What’s hard?
Bugs dependent on precise heap modeling

Concurrency

Logic bugs

Some data - Chrome

IE

Linux kernel

Some data from MS

Real world.. Stuxnet

 3 out of 4 bugs used were logic bugs

Exploit kits

        Java.

Practical

Not: How do I find use-after-free bugs?

But

How do I find a specific type of use-after-free bug in IE/Chrome?

Future
Will automatic bug-hunting technique converge to AI in the future?

Can machines discover new bug patterns?

Exploitation

Quick recap(generic mitigations)
2000
NX
(PAGEEXEC)
2001
ASLR 2004
Stack
Canaries/ heap hardening 2011-2013
New stuff coming

Fact

Writing an exploit in 2013 is theoretically no different than writing one in 2005

Another fact

To date the lower bound on the number of bugs needed to compromise an application
(sandboxes excluded) is almost always between 1 and 2

This shows
Exploitation becomes fundamentally application-specific above a certain number of kLOC

Hot Stuff

“Eternal War in Memory”
Laszlo Szekeres, Mathias Payer, Tao Wei, Dawn Song

Again, get specific.. CFI

Vtguard/Vtable protection in Chrome

SEHOP/ Stack canaries

EMET

Some more, memory safety

DOM Objects “heap partition”:
https://code.google.com/p/chromium/ issues/detail?id=246860

LFH allocation order randomization

UDEREF (PaX)

Future

Adaptive exploits/Probabilistic exploits

Data-only exploits

AEG?

Adaptive exploits

Information leaks become more and more important

Timing attacks become relevant as well (i.e.
Dion Blazakis and pakt  “Leaking addresses with vulnerabilities that can't read good”)

Timing attacks

Problem: what can we tell about the program and heap states before we perform tasks that can crash the application?

Timing attacks - defense
Can we make operations on data structures have the same best, worst and average case complexity?

And heap allocators?

How about Garbage collectors with no noticeable slowdowns?

 etc etc

Data-only attacks

Given a program state p and a memory corruption bug what data can I change to reach a ‘privileged’ state s ?

Note: solving this problem also helps a lot in solving its dual

Conclusion

First
Look for real-world data

Do your own offensive research

Develop intuition through practice

Each large size application is a research topic of its own (sad but true)

Second
Seek collaboration with the industry

Collaborate in funded projects (EU FP, DARPA
CGC, etc.) with industry researchers

Integrate industry-led research in your curricula

 Thanks!

     Questions?

        vincenzo@trailofbits.com