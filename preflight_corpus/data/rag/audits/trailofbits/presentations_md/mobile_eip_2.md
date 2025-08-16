# Dan

  Guido,
  Trail of
  Bits
  
Mike
  Arpaia, iSEC
  Partners
  

  
ShakaCon, 06/21/2012
  
Mobile Exploit Intelligence Project

2
Mobile Device Security Thesis
  Mobile devices are loading up with data
  
  E-­‐mail, line of business apps, login credentials…
  
  Lots of possibilities to compromise mobile devices
  
  Insecure data storage, app-­‐to-­‐app,
  NFC,
  TEMPEST,
  …
  
  Very few vectors explored in actual attacks
  
  Why is that?
  What motivates attackers?
  Isn’t it easy?
  
  What attacks do
  I need to defend against now?
  
  Actual vs
  Probable vs
  Possible
  
  How will things change
  (or not)
  tomorrow?
  

3
Attack
  Vector
  
Exploits
  
Millions of Mobile Attacks
Platform
  
* Android and iOS, 2011-2012

What are we doing wrong?

5
Your Defense Lacks Intelligence
X
X
X
X
Attackers choose the least cost path to their objective
  
ßStunt hacking
  
ßProbable
  
ßActual attacks
  
ßFUD
  

6
Attacker Math 101
  Cost(Attack)
  <
  Potential
  Revenue
  
  Attacks must be
  ﬁnancially proﬁtable
  
  Attacks must scale according to resources
  
  Cost(Attack)
  =
  Cost(Vector)
  +
  Cost(Escalation)
  
  What we know from
  Mobile
  OS architectures
  
Cost of
  Attack
  
  Ease
  
  Enforcement
  
  Established
  Process
  
Potential
  Revenue
  
  # of
  Targets
  
  Value of
  Data
  
  Ability to
  Monetize
  

Mobile Malware
How does it work?
  

8
Mobile Malware – The Setup 2.
  Add malware to many applications
  
1.
  Develop malware
  
3.
  Put malware online
  

9
Drive Installs

10
Mobile Malware – The Heist 5.
  Access data outside the app sandbox
  
6.
  Send stolen data to a remote location
  
7.
  Abuse the data somehow to make money
  

11
Intrusion Kill Chains
  Systematic process that an intrusion must follow
  
  Deﬁciency in one step will disrupt the process
  
  Evolves response beyond point of compromise
  
  Prevents myopic focus on vulnerabilities or malware
  
  Identiﬁes attacker reuse of tools and infrastructure
  
  Guides our analysis and implementation of defenses
  
  Align defenses to speciﬁc processes an attacker takes
  
  Force attackers to make diﬃcult strategic adjustments
  
Mike
  Cloppert
  -­‐
  Security
  Intelligence:
  Deﬁning
  APT
  Campaigns
  

12
There’s Not Much a Spy Can Do
MalwareDev
  
AppDev
  
Expose
  
Installs
  
Escalate
  
C&C
  
Actions
  
Thousands of modiﬁed apps
  
Hundreds of malwares
  
Thousands of advertisements
  
Millions of installs
  
Tens of escalation exploits
  
Hundreds of domains
  
Cyber
  Pompeii
  
App
  Store
  Policies
  –
  Vendor
  Controlled
  
Platform
  Security
  –
  Vendor
  Controlled
  
Blacklists
  
Platform
  Security
  –
  Vendor
  Controlled
  
Platform
  Security
  –
  Vendor
  Controlled
  
Blacklists
  
Abuse
  Monitoring
  

13
Why Did This Chain Form?
X
X
X
X
Drive-­‐By
  Exploits
  
Infection over
  Sync
  
<-­‐
  Wireless
  Attacks
  
<-­‐
  Exploit
  Sandbox
  
Request
  Privileges
  -­‐>
  
Website
  Lures
  -­‐>
  

14
Discrepancies
  Is the security industry lying to us?
  
  Assumptions that mobile threat
  == desktop threat
  
  Fascination with new attack vectors
  
  Myopic focus on ease of attack and malware
  
  We have no idea how attackers actually work
  
  Always more possibilities than probable attacks
  
  Attacker economics are diﬀerent on mobile
  
  Use economics and adversarial characterization!
  
  Why don’t we
  / why won’t we see certain attacks?
  

Where are Mobile Drive-Bys?
Mobile
  Town
  
Desktop
  City
  

16
Not Enough Mobile Targets
~8% of total web traﬃc
  
comes from mobile devices
  
Breakdown by version
  / features
  
(+ varying rates of feature support)
  

17
Lack of Ads Limits Targeting Potential
Normal
  Website
  
Mobile
  Website
  
Mobile
  App
  

18
Mobile Browser Exploits are Harder
Kernel
Drivers
Internet
 
.INTERNET
  
 
.ACCESS_FINE_LOCATION
  
 
.ACCESS_COARSE_LOCATION
  
 
.ACCESS_FINE_LOCATION
  
 
.ACCESS_DOWNLOAD_MANAGER
  
 
.ACCESS_NETWORK_STATE
  
 
.ACCESS_WIFI_STATE
  
 
.SET_WALLPAPER
  
 
.WAKE_LOCK
  
 
.WRITE_EXTERNAL_STORAGE
  
 
.SEND_DOWNLOAD_COMPLETED_INTENTS
  
Browser
  Permissions

19
Vendor App Stores
App stores look like a great value proposition!
  
Incentives
  
Browser
  Exploits
  
Malicious
  Apps
  
# of
  Targets
  
Minimal
  
All
  Devices
  (300 mil+)
  
Ability to
  Target
  
Ads
  
App
  Store
  SEO,
  Lures
  
Ease of
  Exploit
  
Multiple
  Exploits
  
Single
  Exploit
  
Enforcement
  
Anonymous
  
Anonymous?
  

20
Mobile Drive-by Takeaway
  10-­‐20x less potential targets than desktops
  
  Not many mobile browsers, split between platforms
  
  Mobile websites commonly won’t have ads
  

  
  Increased costs to exploit relative to desktops
  
  Harder to target due to feature disparities, lack of
  ﬂash
  
  Multiple exploits required for browser
  + jailbreak
  
  However, anonymity comes easier
  
  Possible, but incentives are stacked against it
  
  Zero identiﬁed cases in the data
  
  Cost not likely to change but
  Potential
  Revenue could…
  
Sidenote:
  Why remotely attack individual
  Apps when even the browser isn’t viable yet?
  

Scaling the Setup 2.
  Add malware to many applications
  
1.
  Develop malware
  
3.
  Put malware online
  

22
Scaling Malicious App Submission
Malicious
  App
  
Developed
  
Use
  New
  IP
  
Submit
  Credit
  
Card
  Payment
  
App on
  
Google
  Play
  
Pass
  Security
  
Review
  
  
Receive
  SMS
  
Submit
  App
  
(Dynamic
  OK)
  
Automated Controls
Apps Can Change
Security Review
Less Effective
Jon
  Oberheide and
  Charlie
  Miller
  -­‐
  Dissecting the
  Android
  Bouncer
  
Signup
  Cost
  
Review
  Cost
  

23
Think Different
  Automate new
  CC/SMS/IPs
  <
  Automate new
  LLCs
  
  Forces malware authors to scale with humans
  
  Enforces accountability along with ban on dynamic code
  
  More diﬃcult to recover from bans
  

24
Scaling Malicious App Submission
Malicious
  App
  
Developed
  
Unknown
  Fraud
  
Controls
  +
  CC#
  
Pass
  Content
  
Review
  
Verify
  Identity
  
Submit
  App
  
(No
  Dynamic
  
Code)
  
App on
  
iOS
  App
  Store
  
Pass
  Security
  
Review
  
  
Human
  Review
  
Automated
  Controls
  
Signup
  Cost
  
Review
  Cost
  

25
Apple Enforces Accountability iOS
  App
  Store
  
Google
  Play
  
Sign
  Up
  
Fraud
  Controls
  
Fraud
  Controls
  
Identiﬁcation
  
Drivers
  License
  
Articles of
  Incorporation
  
IP/SMS/CC#
  
App
  Review
  
Unknown
  Analysis
  
Bouncer
  
Architecture
  
No runtime modiﬁcation
  
Runtime modiﬁcation
  

26
Apple
  App
  Store
  
Google
  Marketplace
  
Malicious App Campaigns
“Say what you will about police states, but they have very little crime.”
  

Scaling the Heist 5.
  Access data outside the app sandbox
  
6.
  Send stolen data to a remote location
  
7.
  Abuse the data somehow to make money
  

28
Which Exploits Get Used?
Exploit
  Scenario
  
Cost of
  Attack
  
Value of
  Data
  
# of
  Targets
  
Universal
  Jailbreak
  
High?
  
High
  (all data)
  
High
  (all)
  
Request
  SMS
  
Free
  
High
  (2FA)
  
Medium
  (2FA users)
  
Handset
  Jailbreak
  
Limited
  Availability
  
High
  (all data)
  
Low
  
App-­‐to-­‐App
  
Limited
  Availability
  
Low
  (limited data)
  
Low
  
  Both platforms have active jailbreaker communities
  
  Android:
  26 jailbreaks from 10 diﬀerent authors
  
  iOS:
  25 jailbreaks from
  ~4 main groups
  

29
Android Jailbreaks by Target 0
  
2
  
4
  
6
  
8
  
10
  
12
  
Stealth
  
Scott
  Walker
  
Revolutionary
  
Oberheide
  /
  Larimer
  
sc2k
  
unrevoked
  
Ken
  Millington
  
Justin
  Case
  
Dan
  Rosenberg
  
Malware
  Authors
  
Aﬀects
  Android
  
Aﬀects
  Particular
  Handset
  
0

30
Universal Android Exploits
Exploit
  Name
  
Last
  Aﬀected
  Version
  
Abused?
  
Exploid
  
2.1
  
Malware
  
RageAgainstTheCage
  
2.2.1
  
Malware
  
Zimperlich
  
2.2.1
  
No
  
KillingInTheNameOf
  
2.2.2
  
No
  
Psneuter
  
2.2.2
  
No
  
GingerBreak
  
2.3.4
  
Malware
  
zergRush
  
2.3.5
  
No
  (conﬁg per device)
  
Levitator
  
2.3.5
  
No
  (low
  # of devices?)
  
mempodroid
  
4.0.3
  
No
  (conﬁg per device)
  

31
What to do?
  Jailbreaks are a certainty after enough popularity
  

  

  
  How we do prevent malicious use of jailbreaks?
  
1. 
Slow jailbreak development by increasing costs
  
2. 
Discourage app-­‐accessible jailbreaks
  
3. 
Decrease potential revenue by patching quickly
  
 
Make less to react to, then react quickly
  
 
Probably some kind of
  Tao proverb that says this better
  

  
“My
  Gingerbreak works, but
  I wont release it before
  
a couple of devices are in the wild so the issue is not
  
ﬁxed before it can become useful.”
  
-­‐-­‐ stealth
  (prior to releasing
  Gingerbreak)
  

32
Factors Influencing JB Availability
Mitigation
  
iOS
  
Android
  
Code
  Injection
  
Code
  Signing
  
No-­‐Execute
  
Randomization
  
Strong
  ASLR
  
ASLR*
  
Containment
  
Seatbelt
  
UNIX
  Permissions
  
Shell
  Available?
  
No
  
Yes
  
1. 
Code
  Signing is signiﬁcantly stronger than
  NX
  (Partial vs
  Full
  ROP)
  
2. 
Does
  ASLR in
  Android 4.0.4+ matter if less than 7% are running it?
  
3. 
Android app permissions don’t make privilege escalation harder
  
4. 
Shell access makes jailbreak development easier on
  Android
  

33
Android Jailbreak Equivalents
  Android
  Private
  Signing
  Keys
  
  jSMSHider:
  http://goo.gl/vPzjg
  
  Aﬀects custom
  ROMs only
  
  Have the user do it
  (no joke)
  -­‐-­‐-­‐-­‐-­‐-­‐-­‐-­‐-­‐-­‐>
  
  Lena:
  http://goo.gl/eiTBA
  

  
  Request
  Device
  Admin
  API
  Privs
  
  DroidLive:
  http://goo.gl/c3EET
  
  Request
  SMS privileges
  
  Almost 100% of non-­‐privesc malware
  
  They’re less eﬀective
  (user interaction), less used, but still work
  

34
Android Maximizes Potential Revenue
Platform
  
Codename
  
03/12/2012
  
4/18/2012
  
06/04/2012
  
1.x
  
Cupcake
  /
  Donut
  
1.2%
  
1.0%
  
0.9%
  
2.1
  
Eclair
  
6.6%
  
6.0%
  
5.2%
  
2.2
  
Froyo
  
25.3%
  
23.1%
  
19.1%
  
2.3
  
Gingerbread
  
62.0%
  
63.7%
  
65.0%
  
3.x
  
Honeycomb
  
3.3%
  
3.3%
  
2.7%
  
4.x
  
Ice
  Cream
  Sandwich
  
1.6%
  
2.9%
  
7.1%
  
Android
  Exploit
  
Time to
  Patch 50%
  
Exploid
  (2.1)
  
294 days
  
RageAgainstTheCage
  (2.2.1)
  
> 240 days
  
http://blog.mylookout.com/blog/2011/08/04/inside-­‐the-­‐android-­‐security-­‐patch-­‐lifecycle/
  

35 iOS Limits Potential Revenue
Vulnerability
  
Exploit
  
Patch
  Availability
  
Malformed
  CFF
  
Star
  (JailbreakMe 2.0)
  
10 days
  
T1
  Font
  Int
  Overﬂow
  
Saﬀron
  (JailbreakMe 3.0)
  
9 days
  
http://david-­‐smith.org/blog/2012/03/10/ios-­‐5-­‐dot-­‐1-­‐upgrade-­‐stats/index.html
  

36
Privilege Escalation Takeaways
  Malware authors have no ability to write exploits
  
  The only exploits abused are public jailbreak exploits
  
  Cost to exploit
  Android is signiﬁcantly lower than iOS
  
  App sandbox is weak against privilege escalation
  
  Platform has many alternate escalation scenarios
  
  Implemented mitigations are weaker than on iOS
  
  Android patches have little eﬀect on problem
  
  Google has no ability to force carriers
  /
  OEMs to react
  
  Even if they could, it’s too easy to write new exploits
  
If you can install an app, you can take over
  Android
  

Where this leads us
X
X
X
X
Drive-­‐By
  Exploits
  
Infection over
  Sync
  
<-­‐
  Wireless
  Attacks
  
<-­‐
  Exploit
  Sandbox
  
Request
  Privileges
  -­‐>
  
Website
  Lures
  -­‐>
  

38
Android Mitigation Outlook
  Chrome for
  Android
  
  Makes browser exploits hard
  
  Not an exploited vector now
  
  No eﬀect on current
  Android malware
  
  SEAndroid
  
  Kills userspace jailbreaks, but not kernel!
  
  Kernel exploits demonstrated on iOS
  
  What handsets will use it?
  
  ASLR in
  Ice
  Cream
  Sandwich 4.x
  
  Little to no eﬀect on privilege escalations
  
  Useful to make browser exploits diﬃcult
  
  Can’t help 300+ million existing devices
  
Google is ahead of threats that don’t exist yet, but far behind on ones that do
  

39
Mobile Malware Predictions
  Malware continues to be
  App and
  Android-­‐centric
  
  “The
  Setup” is getting harder, but not by enough
  
  It’s still worth it to get malware into
  Google
  Play
  
  “The
  Heist” scales extremely well on
  Android
  
  Not likely to change any time soon
  
  Innovation will revolve around
  Driving
  Installs
  
  Ex.
  NotCompatible only diﬀers in how it drives installs
  
  Upcoming
  Android mitigations incorrectly focused
  
  Bouncer,
  Chrome,
  ASLR have limited impact
  
  Changes in 4.0
  / 4.1 don’t signiﬁcantly aﬀect problem
  

40
Mobile Malware Predictions
  Browser,
  NFC,
  Ads
  (incl.
  mobile)
  are not as attractive
  
  Higher costs than app-­‐centric strategy
  
  # of targets still too low
  
  Lack of established process impedes growth
  

  
  iOS will steer clear of similar attacks for now
  
  Real-­‐world veriﬁcation trumps all the technical attacks
  
  Mitigations slow jailbreaks, quick patches reduce value
  
  Attackers are resource-­‐constrained and rational
  

41
App Development Strategies
  Not all keychains are created equal
  
  Android only stores keys.
  No keygen, no data storage.
  
  Try not to shoot yourself in the foot!
  
  Jailbreak means exposure of
  Android keystore
  
  iOS
  DP
  API is
  HW-­‐backed, signiﬁcantly limits exposure
  
  Limit accessible data and implement a circuit breaker
  
  Apps shouldn’t request an entire
  DB of content
  
  Alert
  / modify access after a threshold
  – circuit breaker
  
  Determine accessible data by context
  
  Why is your mobile device downloading
  AutoCAD
  ﬁles?
  
* http://www.trailo{its.com/resources/#ios-­‐eval
  

42
Enterprise BYOD Strategies
  Mobile groupware must follow app security strategy
  
  Limit accessible data, implement a circuit breaker
  
  Ask your vendor these questions!
  
  Assume that
  BYOD devices are compromised
  
  Less likely on iOS, a certainty on
  Android
  
  Existing jailbreak detection is fallible
  
  Malicious attackers aren’t connecting to
  Cydia
  
  If
  Android users can install their own apps, they will be
  
compromised by accident
  
  Restrict access to internal
  App
  Catalogue if possible
  

43
References
 
Attacker
  Math 101,
  Dino
  Dai
  Zovi
  
  www.trailo{its.com/research/#attackermath
  
 iOS
  Security
  Evaluation,
  Dino
  Dai
  Zovi
  
  www.trailo{its.com/research/#ios-­‐eval
  
 
Exploit
  Intelligence
  Project,
  Dan
  Guido
  
  www.trailo{its.com/research/#eip
  
 
Lookout
  Security
  Mobile
  Threat
  Report
  
  https://www.mylookout.com/mobile-­‐threat-­‐report
  
 
Contagio
  Mini
  Dump,
  Mila
  
  http://contagiominidump.blogspot.com/
  
 
Dissecting
  Android
  Malware,
  Yajin
  Zhou,
  Xuxian
  Jiang
  
  http://goo.gl/AOrCJ
  
 
Androguard,
  Anthony
  Desnos
  
  https://code.google.com/p/androguard/
  
 
Dissecting the
  Android
  Bouncer,
  Jon
  Oberheide and
  Charlie
  Miller
  
  
  http://goo.gl/BK82s