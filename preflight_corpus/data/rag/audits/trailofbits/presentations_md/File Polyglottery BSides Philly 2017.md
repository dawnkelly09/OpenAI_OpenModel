# File Polyglottery or, This Proof of Concept is Also a Picture of Cats

Evan Sultanik https://www.sultanik.com/
@ESultanik

`whoami`

   PoC||GTFO
Proof of Concept
(Pictures of Cats)
or
“It looks great on a shelf, and if you read PoC||GTFO on public transportation, people stay away from you.”
—Hackaday Review
Roughly quarterly journal, in the tradition of Phrack and Uninformed
Oﬀensive security research and stunt hacking
Issue 0x17 will be released at CCC
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
Issue 0x17 will be released at CCC
First released on paper at a conference, later released digitally
Each digital release is a Polyglot https://sultanik.com/pocorgtfo/

The Book of PoC||GTFO
“…a ﬁle has no intrinsic meaning. The meaning of a ﬁle—its type, its validity, its contents— can be diﬀerent for each parser or interpreter”
—PoC||GTFO 7:6 by Ange Albertini https://www.nostarch.com/gtfo

It’s Slide 4 and I Haven’t Even
Told You What this Talk is About!
• Each issue of PoC||GTFO is a polyglot: a ﬁle that can be interpreted multiple ways depending on how it is parsed
• Usually crafted by Ange Albertini,
Philippe Teuwen, myself, or some subset of the three of us
• This talk is about the ones I’ve contributed to
• Goal: Convince you that polyglots aren’t just a nifty parlor trick

Example: Android
APK (zip)/Dex Polyglot

Example: Android
APK (zip)/Dex Polyglot
June, 2016
July, 2017

Before we get to more PoC||GTFO…
Time to drop some 0-day!
$ tar xvf totally_not_malware.tar.gz

Before we get to more PoC||GTFO…
Time to drop some 0-day!
$ tar xvf totally_not_malware.tar.gz
Note: We didn’t provide the z option!
Modern versions of tar automagically detect that the archive is compressed based on magic bytes!
(The actual ﬁle extension is ignored.)

Before we get to more PoC||GTFO…
Time to drop some 0-day!
$ tar xvf totally_not_malware.tar.gz
Note: We didn’t provide the z option!
Modern versions of tar automagically detect that the archive is compressed based on magic bytes!
(The actual ﬁle extension is ignored.)
!
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
PostScript created by
Weev!
Producing a Positively Provocative
PDF/PostScript Polyglot

Don’t print
PostScript created by
Weev!
Producing a Positively Provocative
PDF/PostScript Polyglot

PoC||GTFO 0x13
PDF
PostScript

• The PDF format is a subset of the PostScript language, meaning that we need to devise a way to get a PDF interpreter to ignore the
PostScript code, and vice versa
• It’s almost impossible to ﬁnd a PostScript interpreter that doesn’t also support PDF

• The PDF format is a subset of the PostScript language, meaning that we need to devise a way to get a PDF interpreter to ignore the
PostScript code, and vice versa
• It’s almost impossible to ﬁnd a PostScript interpreter that doesn’t also support PDF
It would have been suﬃcient to just start the polyglot with an opening parenthesis, but we can’t do that because Adobe has blacklisted all PDFs that start with a parenthesis.
Why? Because “Adobe,” that’s why!

How do we tell the PostScript interpreter to stop interpreting?
⋮
%%EndDocument
 @endspecial 0 TeXcolorgray 0 TeXcolorgray eop end
%%Trailer userdict /end-hook known{end-hook}if
%%EOF stop

static int dsc_scan_type(CDSC *dsc)
{ unsigned char *p; unsigned char *line = (unsigned char *)(dsc->data + dsc->data_index); int length = dsc->data_length - dsc->data_index;
    /* Types that should be known:
     *   DSC
     *   EPSF
     *   PJL + any of above
     *   ^D + any of above
     *   DOS EPS
     *   PDF
     *   non-DSC
     */
Plus 164 more lines of complex logic!
Ghostview /psi/dscparse.c

static int dsc_scan_type(CDSC *dsc)
{ unsigned char *p; unsigned char *line = (unsigned char *)(dsc->data + dsc->data_index); int length = dsc->data_length - dsc->data_index;
    /* Types that should be known:
     *   DSC
     *   EPSF
     *   PJL + any of above
     *   ^D + any of above
     *   DOS EPS
     *   PDF
     *   non-DSC
     */
Plus 164 more lines of complex logic!
Ghostview /psi/dscparse.c if (COMPARE(dsc->line, "%!PS-Adobe")) { dsc->dsc = TRUE; dsc->begincomments = DSC_START(dsc); if (dsc->dsc_version == NULL)
        return CDSC_ERROR;  /* no memory */ p = (unsigned char *)dsc->line + 14; while (IS_WHITE(*p))
        p++; if (COMPARE(p, "EPSF-"))
        dsc->epsf = TRUE; dsc->scan_section = scan_comments; return CDSC_PSADOBE;
} if (COMPARE(dsc->line, "%!")) { dsc->scan_section = scan_comments; return CDSC_NOTDSC;
}

static int dsc_scan_type(CDSC *dsc)
{ unsigned char *p; unsigned char *line = (unsigned char *)(dsc->data + dsc->data_index); int length = dsc->data_length - dsc->data_index;
    /* Types that should be known:
     *   DSC
     *   EPSF
     *   PJL + any of above
     *   ^D + any of above
     *   DOS EPS
     *   PDF
     *   non-DSC
     */
Plus 164 more lines of complex logic!
Ghostview /psi/dscparse.c if (COMPARE(dsc->line, "%!PS-Adobe")) { dsc->dsc = TRUE; dsc->begincomments = DSC_START(dsc); if (dsc->dsc_version == NULL)
        return CDSC_ERROR;  /* no memory */ p = (unsigned char *)dsc->line + 14; while (IS_WHITE(*p))
        p++; if (COMPARE(p, "EPSF-"))
        dsc->epsf = TRUE; dsc->scan_section = scan_comments; return CDSC_PSADOBE;
} if (COMPARE(dsc->line, "%!")) { dsc->scan_section = scan_comments; return CDSC_NOTDSC;
}
Interpret the ﬁle as a PDF
Interpret the ﬁle as PostScript

static int dsc_scan_type(CDSC *dsc)
{ unsigned char *p; unsigned char *line = (unsigned char *)(dsc->data + dsc->data_index); int length = dsc->data_length - dsc->data_index;
    /* Types that should be known:
     *   DSC
     *   EPSF
     *   PJL + any of above
     *   ^D + any of above
     *   DOS EPS
     *   PDF
     *   non-DSC
     */
Plus 164 more lines of complex logic!
Ghostview /psi/dscparse.c if (COMPARE(dsc->line, "%!PS-Adobe")) { dsc->dsc = TRUE; dsc->begincomments = DSC_START(dsc); if (dsc->dsc_version == NULL)
        return CDSC_ERROR;  /* no memory */ p = (unsigned char *)dsc->line + 14; while (IS_WHITE(*p))
        p++; if (COMPARE(p, "EPSF-"))
        dsc->epsf = TRUE; dsc->scan_section = scan_comments; return CDSC_PSADOBE;
} if (COMPARE(dsc->line, "%!")) { dsc->scan_section = scan_comments; return CDSC_NOTDSC;
}
%!PS-Adobe ← this must come before
%PDF-1.5 ← this

HTTP Quine

HTTP Quine
$ ruby pocorgtfo11.pdf
Listening for connections on port 8080.
To listen on a different port, re-run with the desired port as a command-line argument.

HTTP Quine
$ ruby pocorgtfo11.pdf
Listening for connections on port 8080.
To listen on a different port, re-run with the desired port as a command-line argument.

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

Minimal PoC require ’socket’ server = TCPServer.new(’’, 8080) loop do socket = server . accept request = socket . gets response = File.open(__FILE__).read socket . print "HTTP/1.1 200 OK\r\n" +
"Content−Type: application/pdf\r\n" +
"Content−Length : #{response . bytesize}\r\n" +
"Connection: close\r\n" socket . print "\r\n" socket . print response socket . close end
__END__
Simply prepend this to any PDF!

But why stop there?
require 'socket' server = TCPServer.new('', 8080)
html = DATA.read().split(/<\/html>/)[0]+"</html>\n" loop do socket = server.accept if socket.gets.split(' ')[1].downcase.end_with? ".pdf" then c = "application/pdf" d = File.open(__FILE__).read n = File.size(__FILE__)
        else c = "text/html" d = html n = html.length end socket.print "HTTP/1.1 200 OK\r\nContent-Type: #{c}\r\nContent-Length: #{n}\r\nConnection: close\r\n\r\n"+d socket.close end
__END__
<html>
  <head>
    <title>An HTTP Quine PoC</title>
  </head>
  <body>
    <a href="pocorgtfo11.pdf">Download pocorgtfo11.pdf!</a>
  </body>
</html>

PDF/NES Polyglot and MD5 Quine

PDF/NES Polyglot and MD5 Quine char md5_part1[33]; char md5_part2[33]; unsigned char read_md5_byte(unsigned char byte) { static unsigned char bit; static uintptr_t offset; static unsigned char ret; ret = 0; for(bit=0; bit<8; ++bit) { ret <<= 1; offset = MD5_OFFSET + 128 * 8 * (uintptr_t)byte + 128*(uintptr_t)bit + MEMORY(MD5_DIFFS_OFFSET + 2 * 8 * byte + 2 * bit); if(MEMORY(offset) == MEMORY(MD5_DIFFS_OFFSET + 2
* 8 * byte + 2 * bit + 1)) { ret |= 1;
        }
    } return ret;
} char nibble_to_char(unsigned char nibble) { if(nibble < 10) { return '0' + nibble;
    } else { return 'A' + nibble - 10;
    }
} void read_md5() { static unsigned char i; for(i=0; i<8; ++i) { unsigned char byte = read_md5_byte(i); md5_part1[i*3] = nibble_to_char(byte >> 4); md5_part1[i*3+1] = nibble_to_char(byte & 0xF); md5_part1[i*3+2] = ' ';
    } md5_part1[32] = '\0'; for(i=0; i<8; ++i) { unsigned char byte = read_md5_byte(8 + i); md5_part2[i*3] = nibble_to_char(byte >> 4); md5_part2[i*3+1] = nibble_to_char(byte & 0xF); md5_part2[i*3+2] = ' ';
    } md5_part2[32] = '\0';
}

NES Architecture
PPU
CPU
APU

NES Architecture
PPU
CPU
APU
CHR
(ROM or RAM)
PRG ROM
Mapper

NES Architecture
PPU
CPU
APU
CHR
(ROM or RAM)
PRG ROM
Mapper

CHR
(ROM or RAM)
PRG ROM
Mapper

iNES Header, including ﬂags for a trainer
%PDF-1.5
%<D0><D4><C5><D8> 9999 0 obj
<< /Length number of bytes remaining in the ROM >> stream zeros for the remainder of the 512 Trainer bytes the remainder of the iNES ROM endstream endobj the remainder of the PDF

Requires 32,768 Bytes!

1949–2014 3,000,000 Square Feet
(almost 2x the size of the
Tesla Gigafactory)

PDF/Git Polyglot
$ git bundle

??????????????

!

Data chunk: encoded uncompressed length followed by zlib-compressed data

Git Plumbing
$ git pull
Is equivalent to
$ git fetch && git merge
Likewise,
$ git bundle delegates to
$ git pack-objects

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

PACK^@^@^@^B^@^@^A°µ¬´^Ax^A^@^S#ìÜ%PDF-1.4
%ÐÔÅØ 6 0 obj
<<
/Length 61337
/Filter /FlateDecode
>> stream
PDF Object endstream endobj
Our Hopes, Deﬂated
Maximum Size of a DEFLATE Block: 65,535 Bytes
Byte Stream 7 0 obj
<<
/Length 1234
/Filter /FlatDecode
>> stream

PACK^@^@^@^B^@^@^A°µ¬´^Ax^A^@^S#ìÜ%PDF-1.4
%ÐÔÅØ 6 0 obj
<<
/Length 61337
/Filter /FlateDecode
>> stream
PDF Object endstream endobj 00 FF FF 00 00
Our Hopes, Deﬂated
Maximum Size of a DEFLATE Block: 65,535 Bytes
Byte Stream 7 0 obj
<<
/Length 1234
/Filter /FlatDecode
>> stream

PACK^@^@^@^B^@^@^A°µ¬´^Ax^A^@^S#ìÜ%PDF-1.4
%ÐÔÅØ 6 0 obj
<<
/Length 61337
/Filter /FlateDecode
>> stream
PDF Object endstream endobj 00 FF FF 00 00
Our Hopes, Deﬂated
Maximum Size of a DEFLATE Block: 65,535 Bytes
Byte Stream 7 0 obj
<<
/Length 1234
/Filter /FlatDecode
>>
%
Remember to update the SHA1 hash!
Breaks xrefs in the inner PDF, but most viewers are resilient!

PDF/Git Polyglot

$ git clone PDFGitPolyglot.pdf foo
Cloning into ’foo’...
Receiving objects: 100% (174/174), 103.48 KiB | 0 bytes/s, done.
Resolving deltas: 100% (100/100), done.
$ cd foo
$ ls
PDFGitPolyglot.pdf PDFGitPolyglot.tex
PDF/Git Polyglot

Conclusions
• Files have no intrinsic meaning
• Polyglots aren’t just a nifty parlor trick
• You can make them, too!
• Open PostScript in a VM
• PDF is broken
Homework
Check out PoC||GTFO 0x16, which helps you reverse engineer itself https://www.sultanik.com/pocorgtfo/

Acknowledgements
Ange Albertini
Sergey Bratus
Travis Goodspeed
Philippe Teuwen
Evan Teran
Jacob Torrey
@angealbertini
@sergeybratus
@travisgoodspeed
@doegox
@evan_teran
@JacobTorrey
Et pl. al.

Thanks!
@ESultanik https://www.sultanik.com/