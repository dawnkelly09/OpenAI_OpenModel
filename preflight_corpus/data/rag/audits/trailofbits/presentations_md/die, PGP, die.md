# 1


2 die, PGP, die 🔪
William Woodruff
Trail of Bits

3 hello i am:
● william woodruff (@8x5clPW2)
● senior security engineer @ Trail of Bits
○
LLVM, applied cryptography, open source engineering agenda:
●
PGP is bad
○ real bad
●
“i can ﬁx him”
○ no you can’t
● what to do and to use instead
○ tl;dr signal & age & sigstore (soon!)

4
“Pretty” “”Good”” “””Privacy””” good for:
● email encryption (not really)
● authenticated channels (not really)
● digital signing (not really)
key features:
●
“web of trust”
● historical museum of bad crypto
“standardized” in RFC 4880 your 5 second refresher on PGP

5 let’s talk about cryptography

6
PGP is from 1991

7
RFC 4880: your new best friend the original PGP RFC, describing the message format and baseline algorithms
● public key: RSA, ElGamal, DSA (lol)
● symmetric:
○
IDEA (weird obsolete 90s replacement for DES)
○ 3DES (your bank loves this one)
○
CAST5 (the oﬃcial block cipher of 󰎟)
○
Blowﬁsh (broken)
○
Twoﬁsh (okay? maybe? who knows?)
○
AES (good, but marked as optional)
● extended by 5581 (Camellia) and 6637 (ECC)
○ better(?), but both optional! the baseline is still 4880!

8 want a sane mode of operation? too bad, you only get PGP’s weird custom CFB psst: it’s not authenticated who needs GCM?
statements dreamed up by the utterly deranged

9
RSA (throwback!)

10

11
ElGamal is weird circa 1985 (the before times)
selected because of minimal legal encumbrance, not ideal cryptographic properties (seeing a pattern?)
in particular:
● malleability (CCA)
● you need to understand groups to achieve semantic security (like RSA)
● big ol’ keys for smol bit security (like
RSA)
● essentially RSA but with discrete log instead of prime factorization

12
ElGamal is weird did i mention that there’s no actual standard for ElGamal?
RFC4880 cites Taher’s original paper:
PGP implementations implement prime generation in different ways!
you are here

13 forward secrecy
“compromises in long term keys do not compromise short-lived sessions” key compromise should not allow an adversary to decrypt passively captured historical traffic!
users expect this when communicating in a post-Heartbleed world!!
PGP cannot provide forward secrecy. there are no session keys.
key compromise in PGP means total compromise of all messages.
this is a completely solved problem in modern protocols (TLS 1.3, SSH,
Noise)!!!

14 this is so fucking broken i’m not going to ﬁll this slide in google “PGP MDC” authenticated encryption

15
“web of trust” remember key signing parties?

16
“the strong set” the set of keys such that each pair of keys has a path between them in theory:
● strong set continuously grows over time, strengthening the WoT
● more interconnections = more trust, amirite??
in practice:
● shaky/nonexist mechanisms for revocation/compromise
“Poisoned certificates are already on the SKS keyserver network. There is no reason to believe the attacker will stop at just poisoning two certificates. Further, given the ease of the attack and the highly publicized success of the attack, it is prudent to believe other certificates will soon be poisoned.”

17 let’s talk about email and
PGP

18 how it started how it’s going

19 real heads know

20

21
PGP lures you into a false sense of security even if you do everything right, PGP will not save you from:
● unencrypted metadata (including your recipients and subject line)
● people helpfully replying in cleartext
● nonrepudiation (maybe you didn’t mean to send that particular email with a permanent global identiﬁer for yourself?)

22
“i can ﬁx him”

23 no, you can’t you have two options in the PGP ecosystem:
● accept (and generate) all kinds of crap required by the RFCs
● do your own thing and use nonstandard ciphers
○ in eﬀect, a GnuPG monoculture. why not simply use something better to begin with?
we’ve only scratched the surface here. i’m going easy by not talking about the CLI.
JUST USE SOMETHING ELSE!!!!

24 what should you use?
texting friends/buying drugs? use Signal.
emailing anyone? stop LARPing*.
encrypting ﬁles? use age. online? use tarsnap.
signing commits? use ssh (hurry up, GitHub)

25 the future: keyless codesigning with sigstore when is the last time you veriﬁed a Python package’s PGP signature?
when is the last time you published a PGP signature for your code?
● hint: your linux package manager’s signatures does not count sigstore is the future here:
● signers use their identities (established through OIDC) instead of keys
○ short lived signing certs + CT logging ensures auditability and transparency
●
Trail of Bits is working on this future
○ sigstore-python + PyPI support for OIDC

26 conclusion: PGP delenda est

27 send me PGP hate mail:
william@yossarian.net
-----BEGIN PGP PUBLIC KEY BLOCK----- mQINBFVkpc4BEACj1sixEQcfbaMqs4jeI2gdZ
PUetr1W8Yf2aBfmlIXUntvzpqxyj6l56YzL
XGJG/0a+UpN88ZE+H/G0HbkmDx9rqWJw0iRQs wUxr4oncejLP9Fe/LCbdramD6jpFsT8SVXLco 5DGbaOYKTdIWyOMIoEZ5TpnIXHRP5jnvSiKJG fq68V0jSAyw6E0kgjAYnxvdwp9h+xHUAYiegI eKlgXis4qyZ8g/yR7o5T9oRafbNoGWY+fSPJM 8dy0oirescLRguPtAGeuFA1saOWY76AJuAF+d
Qu/46ClorhsrhybUmibbYPInNk0C9fR0uFVTw 9jUkF7/l3Pui7D7tS5iEoExGaw+OXo3UzT4G2
OyAFvdLg6PUQLlyouLyyusLbBoYPEs0YBdo5I jeeqZ/S3GmWaIWOAV+b3bfQgLYVYCBOESEbCX sq0G37KrgC3KV1w68k+lC6FvjHyIvmMftZ80B cIvmCJa3i5kVxnQS4SdR7+vwmYEKkLXYMTs5G hwwpi4Gipr9MdY9SyRSWLqpUxOHKdeB8d38vD o6W/y1/uJ/GK3cfkLZL5AWvzoZKlILuSgKqlG kRu2CYejVOMTj5A9gUMJ0hv/evlf7DTTQCXLA
JNrMSjU+youGA4gB4v2S132lrB8Pe3SAZzHZJ
TbyhCpiZN3fdn4kXcUu91gr7yu90q6zL/QARA
QABtCtrZXliYXNlLmlvL3lvc3NhcmlhbiA8eW 9zc2FyaWFuQGtleWJhc2UuaW8+iQI+BBMBAgA oBQJVZKXOAhsjBQkSzAMABgsJCAcDAgYVCAIJ
CgsEFgIDAQIeAQIXgAAKCRCFrgDFBIM7PKtsE
ACYY0zPqQtw3wPvHn8WeFO8lKUry6V4hhzqi4

28 cribbed material
●
“SKS Keyserver Network Under Attack”, Hansen, GitHub Gist 2019
●
“Fuck RSA”, Ben Perez, SummerCon 2019
●
“On the (In)security of ElGamal in OpenPGP”, Feo et al., RWC 2022
●
“Efail: Breaking S/MIME and OpenPGP Email Encryption using Exﬁltration Channels”,
Poddebniak et al., USENIX 2018
●
“This World of Ours”, James Mickens, ;login January 2014
●
“Stop Using Encrypted Email”, Latacora, February 2020
●
“The PGP Problem”, Latacora, July 2019
●
"Giving up on long term PGP", Filippo Valsorda, December 2016 thanks
● ryan stortz (@withzombies)
● josh hoﬁng