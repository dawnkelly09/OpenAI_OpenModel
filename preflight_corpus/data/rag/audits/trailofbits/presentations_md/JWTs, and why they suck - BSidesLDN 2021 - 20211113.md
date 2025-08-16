# 1


2
JWTs, and why they suck

3 who?
1.
Rory Mackie / @roddux
●
AppSec at Trail of Bits
A.
Development -> DevSecOps -> Sec Eng -> Pentesting/websec
❖
Purveyor of awful opinions (facts)
1)
bad at lists this guy

4 what?
JWTs are JSON Web Tokens       (more like Janky Worthless Tokens haha gottem)
Actually a group noun referring to JWSs and JWEs — we’re talking about JWSs.
The header is known as ‘JOSE’, which uses algorithms deﬁned in the JWA standard, because ACRONYMS
Used (badly) for authentication and authorization
Popularised by SAAS companies that sell authentication products apparently pronounced ‘jot’3 which tells you everything really
RFC 7519

5 why?
To convince you all why you should stop using JWTs for sessions, by:
-
Teaching you the bad bits
-
Making you question whether you need JWTs                     (spoiler: you don’t)
-
Giving you some more sensible options

6 how do i JWT
<base64-encoded JSON blob> . <base64-encoded JSON blob> . <signature>
( starts with eyJhb[..] because that’s what {“alg” looks like in base64 )
<HEADER>.<CLAIMS>.<SIGNATURE>

Circle of shame

7
I GOT 99 PROBLEMS and they’re all JWTs

8
Problem 1: Irrevocable
Once issued there exists no means to revoke a JWT (builtin)
If you track state for each token you may as well have a database    :^)
Having an expiry is not the same thing as being able to revoke a token

9
Problem 2: JSON
JSON is a not a strong format
-
Field ordering
-
Duplicate ﬁelds
-
Field data types
Inconsistencies in the above between different libraries/langs 1

10
Problem 3: YOU DON’T NEED IT
YAGNI — You Aren’t Gonna Need It.
You’re not Facebook
You are also not Google
Just use a database, or memcached/Redis
$£ sponsor me pls redis £$

11
Problem 4: Too ﬂexible
Too many options
Thirteen different alg types 2 s, and that’s just for JWS
Seventeen types for JWEs
Too many ways to misconﬁgure those options, leading to ...

12
Problem 5: Footguns alg: none mixing symmetric and asymmetric parsing untrusted data token can specify which key is used for validation

13
Problems 6—99: You gotta parse ‘em
You have to decode and parse RANDOM USER-SUPPLIED DATA in order to validate the token
Hope your Base64/JOSE/JSON/JWS parsing libraries are all
~~~absolutely~~~ bulletproof    :^)
(spoilers: they are not)   (~121 CVEs in JWT/JOSE/JWS libraries)

14
Problem 7: Offline attacks against your keys
Attackers can literally spend as long as they need to break your key signature algorithm. ECDSA is not bulletproof, and lots of crypto algos have had problems in the past that allow for privkey recovery.
Using JWTs allows attackers to try any attack they want (and any new, secret attack) to break your signatures

15
Bad implementations
List of high-proﬁle JWT-related issues https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-librarie s/ https://insomniasec.com/blog/auth0-jwt-validation-bypass https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=JWT

16
Why you think you need JWTs
“muh stateless”  — stop
“b-but muh interoperability” — use protobufs
“everyone else is doing it!” — doesn’t mean it’s a good idea
“derp derp it protect me against CSRF” — JWTs are not a security control, don’t treat them as one. Also, other   s u p e r i o r   controls exist

17
What to use instead
Honest-to-goodness COOKIES with session IDs
HttpOnly, Secure, Sec-Fetch-Mode, SameSite...
why throw away hard-won security controls? for what?
congrats, XSS bugs are now a problem again

18 but what if i JWT inside my cookies?
don’t talk to me or my son ever again

19
TL;DW:

20 20
REJECT MODERNITY
EMBRACE TRADITION
❌ bad standard
❌ dumb logo
❌ khafkaesque nightmare
❌ doesn’t care about you
❌ not ﬂexible
❌ will leave you for next big thing
❌ did i mention alg:none?
✅ tasty snack
✅ everybody loves him
✅ cares about you
✅ not fussy
✅ been around forever
✅ gets on with your friends

21 1.
An exploration of JSON interoperability vulnerabilities,
Bishop Fox 2.
JWA RFC — JWT algorithm list 3.
JWT RFC 4.
Thomas Ptacek blogpost 5.
Sec/Crypto/W.e podcast
- some other links here lol
- sample text
References

22
Questions!
( and maybe answers )
@roddux