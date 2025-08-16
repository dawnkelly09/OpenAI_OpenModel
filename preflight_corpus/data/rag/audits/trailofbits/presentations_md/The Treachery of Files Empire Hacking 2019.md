# The Treachery of Files and Two New Tools that Tame It

Evan Sultanik

The Treachery of Files
A Tragedy in Two Acts
Act I
Files Have No Intrinsic Meaning
Goal: Convince you that these funky
ﬁles aren’t just nifty parlor tricks
Act II
PolyFile and PolyTracker!
Goal: Introduce two new tools to help you reverse engineer ﬁles and the parsers that process them

`whoami`

`whoami`

`whoami`
! iTerm

$ md5sum ESultanikResume.pdf affab1eda8e9b6d8a80e940f20cb3b3b  ESultanikResume.pdf

$ md5sum ESultanikResume.pdf affab1eda8e9b6d8a80e940f20cb3b3b  ESultanikResume.pdf
$ unzip -l ESultanikResume.pdf
Archive:  ESultanikResume.pdf
  Length      Date    Time    Name
---------  ---------- -----   ---- 0  09-17-2019 14:47   ESultanikResume/ 638270  06-07-2019 10:35   ESultanikResume/PDFGitPolyglot.pdf
---------                     ------- 638270                     2 files

$ file ESultanikResume.pdf
ESultanikResume.pdf: NES ROM image (iNES): 8x16k PRG, 2x8k
CHR [V-mirror] [SRAM] [Trainer]
$ md5sum ESultanikResume.pdf affab1eda8e9b6d8a80e940f20cb3b3b  ESultanikResume.pdf
$ unzip -l ESultanikResume.pdf
Archive:  ESultanikResume.pdf
  Length      Date    Time    Name
---------  ---------- -----   ---- 0  09-17-2019 14:47   ESultanikResume/ 638270  06-07-2019 10:35   ESultanikResume/PDFGitPolyglot.pdf
---------                     ------- 638270                     2 files

$ file ESultanikResume.pdf
ESultanikResume.pdf: NES ROM image (iNES): 8x16k PRG, 2x8k
CHR [V-mirror] [SRAM] [Trainer]
$ nestopia ESultanikResume.pdf
$ md5sum ESultanikResume.pdf affab1eda8e9b6d8a80e940f20cb3b3b  ESultanikResume.pdf
$ unzip -l ESultanikResume.pdf
Archive:  ESultanikResume.pdf
  Length      Date    Time    Name
---------  ---------- -----   ---- 0  09-17-2019 14:47   ESultanikResume/ 638270  06-07-2019 10:35   ESultanikResume/PDFGitPolyglot.pdf
---------                     ------- 638270                     2 files

Act I
Files Have No Intrinsic Meaning

   PoC||GTFO https://sultanik.com/pocorgtfo/

   PoC||GTFO
Proof of Concept
(Pictures of Cats)
or
“It looks great on a shelf, and if you read PoC||GTFO on public transportation, people stay away from you.”
—Hackaday Review
Roughly quarterly journal, in the tradition of Phrack and Uninformed
Oﬀensive security research and stunt hacking
First released on paper at a conference, later released digitally
Each digital release is a Polyglot https://sultanik.com/pocorgtfo/

   PoC||GTFO
Proof of Concept
(Pictures of Cats)
or
“It looks great on a shelf, and if you read PoC||GTFO on public transportation, people stay away from you.”
—Hackaday Review
Roughly quarterly journal, in the tradition of Phrack and Uninformed
Oﬀensive security research and stunt hacking
First released on paper at a conference, later released digitally
Each digital release is a Polyglot https://sultanik.com/pocorgtfo/

   PoC||GTFO
Proof of Concept
(Pictures of Cats)
or
“It looks great on a shelf, and if you read PoC||GTFO on public transportation, people stay away from you.”
—Hackaday Review
Roughly quarterly journal, in the tradition of Phrack and Uninformed
Oﬀensive security research and stunt hacking
First released on paper at a conference, later released digitally
Each digital release is a Polyglot https://sultanik.com/pocorgtfo/

The Book of PoC||GTFO https://www.nostarch.com/gtfo

The Book of PoC||GTFO
“…a ﬁle has no intrinsic meaning. The meaning of a ﬁle—its type, its validity, its contents— can be diﬀerent for each parser or interpreter”
—PoC||GTFO 7:6 by Ange Albertini https://www.nostarch.com/gtfo

Example: Android
APK (zip)/Dex Polyglot

Example: Android
APK (zip)/Dex Polyglot

Example: Android
APK (zip)/Dex Polyglot
July, 2017

Example: Android
APK (zip)/Dex Polyglot
June, 2016
July, 2017

What’s Wrong Here?
$ tar xvf totally_not_malware.tar.gz

What’s Wrong Here?
$ tar xvf totally_not_malware.tar.gz
Note: We didn’t provide the z option!
Modern versions of tar automagically detect that the archive is compressed based on magic bytes!
(The actual ﬁle extension is ignored.)

What’s Wrong Here?
$ tar xvf totally_not_malware.tar.gz
Note: We didn’t provide the z option!
Modern versions of tar automagically detect that the archive is compressed based on magic bytes!
(The actual ﬁle extension is ignored.)
"
What if we created a ﬁle that is both a valid .tar and a valid .tar.gz?

totally_not_malware.tar totally_not_malware.tar

totally_not_malware y_not_malware.tar

Why are PDFs
Particularly Polyglottable?
• Because “Adobe,” that’s why!
• It’s been around for a long time
• Parsers built to be resilient to all sorts of errors and incompatibilities
• Can insert arbitrary length binary blobs almost anywhere in the ﬁle
• Almost all parsers ignore everything before the header lol, put whatever you want here!
%PDF-1.5
%<D0><D4><C5><D8>
⋮ 9999 0 obj
<<
/Length # bytes in the blob
>> stream lol, put whatever you want here!
endstream endobj

Hey,
I’ve been trying to get my résumé to so-and-so in HR, but we’ve had problems with E-mail. Can you please print out the attached copy and give it to them?
Thanks! —Alice Hackerman

Hey,
I’ve been trying to get my résumé to so-and-so in HR, but we’ve had problems with E-mail. Can you please print out the attached copy and give it to them?
Thanks! —Alice Hackerman
Looks legit!
(AV doesn’t typically scan for MIPS
ﬁrmware!)

Corporate
LAN lolololololololololol
PostScript/PJL (Cui & Stolfo, 2011)

Don’t print
PostScript created by Evan!
Producing a Positively Provocative
PDF/PostScript Polyglot

Don’t print
PostScript created by Evan!
Producing a Positively Provocative
PDF/PostScript Polyglot

PoC||GTFO 0x13
PDF
PostScript

HTTP Quine

HTTP Quine
$ ruby pocorgtfo11.pdf
Listening for connections on port 8080.
To listen on a different port, re-run with the desired port as a command-line argument.

HTTP Quine
$ ruby pocorgtfo11.pdf
Listening for connections on port 8080.
To listen on a different port, re-run with the desired port as a command-line argument.
Feelies automagically parsed from the ZIP!

$ ln -s pocorgtfo11.pdf pocorgtfo11.html
But Wait, There’s More!

$ ln -s pocorgtfo11.pdf pocorgtfo11.html
But Wait, There’s More!

$ ln -s pocorgtfo11.pdf pocorgtfo11.html
But Wait, There’s More!

In which an HTML page is also a PDF
Which is also a ZIP
Which is also a Ruby script
Which is an HTTP Quine or, The Treachery of Files
Ceci n’est pas une PoC!

1949–2014 3,000,000 Square Feet
(almost 2x the size of the
Tesla Gigafactory)

PDF/Git Polyglot
$ git bundle

argv_array_pushl(&pack_objects.args,
                     "pack-objects", "--all-progress-implied",
                     "--compression=0",
                     "--stdout", "--thin", "--delta-base-offset",
NULL); bundle.c
$ export PATH=/path/to/patched/git:$PATH
$ git init
$ git add article.pdf
$ git commit article.pdf -m "added"
$ git bundle create PDFGitPolyglot.pdf —all https://github.com/ESultanik/PDFGitPolyglot

PDF/Git Polyglot

$ git clone PDFGitPolyglot.pdf foo
Cloning into ’foo’...
Receiving objects: 100% (174/174), 103.48 KiB | 0 bytes/s, done.
Resolving deltas: 100% (100/100), done.
$ cd foo
$ ls
PDFGitPolyglot.pdf PDFGitPolyglot.tex
PDF/Git Polyglot

Act II
Introducing PolyFile and PolyTracker!
SafeDocs TA1

Act II
Introducing PolyFile and PolyTracker!
Automated Lexical Annotation and Navigation of Parsers
SafeDocs TA1

Act II
Introducing PolyFile and PolyTracker!
Automated Lexical Annotation and Navigation of Parsers
SafeDocs TA1
The ALAN Parsers Project

#
High Level Goals
Create semantic map of the functions in a parser
$
%
???

#
High Level Goals
Create semantic map of the functions in a parser
$ parser_function1
↳byte 0, 10, 50
  Object Stream parser_function2
↳byte 10, 74
  Xref parser_function3
↳byte 20
  JFIF

#
High Level Goals
Create semantic map of the functions in a parser
$ parser_function1
↳byte 0, 10, 50
  Object Stream parser_function2
↳byte 10, 74
  Xref parser_function3
↳byte 20
  JFIF
Ultimate Goal: Automatically extract a minimal grammar specifying the ﬁles accepted by a parser
Hypothesis: The majority of the potential for maliciousness and schizophrenia will exist in the symmetric diﬀerence of the grammars accepted by a format’s parser implementations

Related Work
•Ange’s SBuD
◦
Limited parser support
•Kaitai Struct
◦
No support for PDF
◦
Diﬃcult to specity context sensitive languages
•Valgrind / TaintGrind
◦
Intractably slow; hours of computation to parse a minimal
PDF
•AFL Analyze
◦
Does not associate input byte sequences with the program trace
•LLVM Dataﬂow Sanitizer
◦
Limited to just a few thousand taint labels
◦
Can only track at most one input byte at a time

Approach: Semantic Labeling
Polyglot-Aware
File Identiﬁcation
Resilient Parsing
Hierarchical Labeling
%
???
iNES ROM
PDF
ZIP
Modify parsers for best eﬀort
Instrument to track input byte oﬀsets
Label regions of the input
Produce ground truth iNES [0x0→0x12220]
↳ Magic [0x0→0x3]
   Header [0x4→0xF]
   ⋮
   PRG [0xC210→0x1020F]
   CHR [0x10210→0x12220]
PDF [0x10→0x2EF72F]
↳ Magic [0x10→0x1E]
   Object 1.0 [0x1F→0x12221]
   ↳ Dictionary [0x2A→0x3E]
      Stream [0x3F→0x12219]
      ↳ JFIF Image [0x46→0x1220F]
         ↳ JPEG Segment […]
            ↳ Magic […]
               Marker […]
⋮

Approach: Parser Instrumentation
LLVM
Instrumentation
Taint Tracking
Operate on LLVM/IR
Can work with all open source parsers
Eventually support closed- source binaries by lifting to
LLVM (e.g., with McSEMA or Remill)
Shadow memory inspired by the Data Flow Sanitizer
(dfsan)
Negligible CPU overhead
O(n) memory overhead, where n is the number of instructions executed by the parser
Novel datastructure for eﬃciently storing taint labels dfsan status quo:
훩(1) lookups
훩(n²) storage
TAPP:
O(log n) lookups
O(n) storage

Current
Tooling
Novel ﬁle matching algorithm seeded with over 10,000 ﬁle deﬁnitions from TrID
Kaitai Struct ﬁle deﬁnition parser for automatically labeling based upon KSY deﬁnitions (e.g., JPEG, ZIP, WASM)
Instrumented Didier Stevens’ PDF parser, resilient to malformations and schizophrenia
Interactive ﬁle explorer
Shadow memory inspired by the Data Flow
Sanitizer (dfsan) and Angora
Negligible CPU overhead
O(n) memory overhead, where n is the number of instructions executed by the parser
Currently supports C, C++ (experimental), and any code entirely representable in LLVM/IR.
https://github.com/trailofbits/polyfile https://github.com/trailofbits/polytracker

Demo

Demo

WASM/HTML
Polyglot Detection

WASM/HTML
Polyglot Detection

PolyTracker Instrumentation
{
  "dfs$ensure_solid_xref": [ 2276587, 2276588
  ],
  "dfs$fmt_obj": [ 2465223, 2465224, 2465225, 2465226, 2465227, 2465228, 2465240, 2465241, 2465242, 2465243, 2465244, 2465245, 2465246, 2465258, 2465259, 2465260, 2465261, 2465262
  ]
}

PolyTracker Instrumentation
{
  "dfs$ensure_solid_xref": [ 2276587, 2276588
  ],
  "dfs$fmt_obj": [ 2465223, 2465224, 2465225, 2465226, 2465227, 2465228, 2465240, 2465241, 2465242, 2465243, 2465244, 2465245, 2465246, 2465258, 2465259, 2465260, 2465261, 2465262
  ]
} iNES [0x0→0x12220]
↳ Magic [0x0→0x3]
   Header [0x4→0xF]
   ⋮
   PRG [0xC210→0x1020F]
   CHR [0x10210→0x12220]
PDF [0x10→0x2EF72F]
↳ Magic [0x10→0x1E]
   Object 1.0 [0x1F→0x12221]
   ↳ Dictionary [0x2A→0x3E]
      Stream [0x3F→0x12219]
      ↳ JFIF Image [0x46→0x1220F]
         ↳ JPEG Segment […]
            ↳ Magic […]
               Marker […]
⋮

Why Should You Care?
'!
☣
&
% 010101 010101 010101 010101
☑
☑
☑

Why Should You Care?
Why Should You Care?
'!
☣
&
% 010101 010101 010101 010101
☑
☑
☑

Acknowledgements
Ange Albertini
Sergey Bratus
Travis Goodspeed
Philippe Teuwen
Evan Teran
Jacob Torrey
Ryan Speers
@angealbertini
@sergeybratus
@travisgoodspeed
@doegox
@evan_teran
@JacobTorrey
@rmspeers
Et pl. al.

Thanks!
Evan Sultanik

@ESultanik

Contact Info
Carson Harmon
Brad Larsen
@reyeetengineer
@BradLarsen
Thanks!
Evan Sultanik

@ESultanik https://github.com/trailofbits/polyfile https://github.com/trailofbits/polytracker

This slide is here solely to prevent the slideshow from auto-closing if Evan clicks one too many times!