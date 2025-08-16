# Peeling back the "Shlayers" of macOS malware

Erika Noerenberg
Carbon Black
Josh Watson
Trail of Bits
|
| 1 June 2019

Who we are
Erika Noerenberg
Senior Threat Researcher,
Carbon Black
@gutterchurl
Josh Watson
Senior Security Engineer,
Trail of Bits
@josh_watson

Agenda 1. How it all started 2. Shlayer Overview and Technical Analysis 3. Reversing Objective-C 4. Objective-C in Binary Ninja 5. Questions & Answers

How it all started

Monday, November 12, 2018
Go here

Friday, January 4th

Friday, January 4th

Monday, January 7th
●Philip Stokes, SentinelOne Researcher - https://www.sentinelone.com/blog/how-malware-bypass-macos-gatekeeper/
●Down the rabbit hole…

Monday, January 7th

Monday, January 7th

DubbelIPA?

DubbelIPA?

DubbelIPA?

Shlayer Overview and Technical Analysis

What is Shlayer?
●Initially discovered by Intego researchers in January 2018 https://www.intego.com/mac-security-blog/osxshlayer-new-mac-malware-comes
-out-of-its-shell/
●Carbon Black researchers discovered and began tracking an ongoing campaign in November of 2018
○At that time, the family was undetermined
●Saw uptick of infections in February 2019 and dug deeper
●Discovered unique privilege escalation technique not identified in the MITRE
ATT&CK framework

Sample Collection
●
Developed script to scrape known sites serving Shlayer
●
Selenium script automated detection and download of
Shlayer samples
●
Malware authors got smarter and started putting mitigations in place

Sample Collection
●
Developed script to scrape known sites serving Shlayer
●
Selenium script automated detection and download of
Shlayer samples
●
Malware authors got smarter and started putting mitigations in place

Shlayer Distribution
●Initial discovery on hijacked homebrewing site
●Hijacked expired domains to serve ads
●Mostly fake Adobe Flash update installers and browser extensions
○Commonly DMG, PKG, ISO, or zip files
●Also found in weaponized torrents for cracked software

Sample Identification and Collection
Mac links are valid!

Sample Identification and Collection

Sample Identification and Collection

Sample Identification and Collection

Sample Identification and Collection
Some samples had bundled cryptomining component

Sample Shlayer Variant Execution
●
Once DMG mounted and executed, runs hidden .command script
●
First script decodes and decrypts and additional encoded script
●
Second script decodes another embedded script
●
The third decoded script attempts to download and execute the next stage payload using curl and other system tools
●
Privileges are escalated for downloaded payload with sudo
●
Payloads are signed with valid Apple Developer IDs

First encoded script
Execution
Artifacts (CB
Response)

Second script

Third script

URL Components
Sample URL:
hxxp://api.resultsformat[.]com/sd/?c=C2NybQ==&u=$machine_id&s=$session_guid&o=$os_version&b=58310 30393
Identifier
Sample Data
Description c=
C2NybQ
Possible Campaign Identifier, not unique u= 564DB6C2-671E-6AE7-E4D2-D7C3B281EF34
Unique ID for victim system based on IOPlatformUUID s=
E7B274DC-2E66-45B1-A57B-29865A3DE435
Session ID from uuidgen o= 10.12.5 macOS version b= 5831030393
Encryption key, hardcoded per sample

Apple Developer IDs
Downloads second stage with unique system information hxxp://api.xxxxxxxxxx.com/sd/?c=C2NybQ==&u=$machine_id&s=$session_guid&o=$os_version&b=5831030393
Possible Campaign
Identifier
Unique ID based on
IOPlatformUUID
Session ID from uuidgen macOS version
Encryption key from .command script, hardcoded per sample

Apple Developer IDs
Downloads second stage with unique system information hxxp://api.xxxxxxxxxx.com/sd/?c=C2NybQ==&u=$machine_id&s=$session_guid&o=$os_version&b=5831030393
Possible Campaign
Identifier
Unique ID based on
IOPlatformUUID
Session ID from uuidgen macOS version
Encryption key from .command script, hardcoded per sample

Privilege Escalation
●Once second stage executed, attempts privilege execution
●Runs sudo and invokes /usr/libexec/security_authtrampoline
●

AuthorizationExecuteWithPrivileges()
https://speakerdeck.com/patrickwardle/defcon-2017-death-by-1000-installers-its-all-broken?slide=8 https://www.youtube.com/watch?v=mBwXkqJ4Z6c

T???? - Privilege Escalation
“Death by 1000 installers”

Reversing Objective-C

Reversing Objective-C
@interface Test : NSObject
- (void)none;
- (void)param: (int)x;
- (void)params: (int)a : (int)b : (int)c : (int)d : (int)e : (int)f : (int)g;
- (int)retval;
- (struct x)stret;
@property NSString *propertyString;
@end
@implementation Test
- (id)init
{ fprintf(stderr, "in init method, self is %p\n", self); return self;
}
/* ... */
@end

Reversing Objective-C
Test *t = [[Test alloc] init]; struct x y = [t stret];
[t none];
[t param: 9999];
[t params: 1 : 2 : 3 : 4 : 5 : 6 : 7]; fprintf(stderr, "retval gave us %d\n", [t retval]);
[t setPropertyString:@"test"];

Reversing Objective-C mov rdi, obj_ptr mov esi, 1 call cls::my_method mov edx, 1 mov rsi, my_method_sel mov rdi, obj_ptr call objc_msgSend

Objective-C in Binary Ninja

ObjCGraphView

Objective-C Sections

Parsing a Mach-O binary: structure recovery class_t class_ro_t ivar_list_t property_list_t

Classes class_t class_t *isa class_t *superclass struct cache class_ro_t *vtable class_ro_t uint32_t flags uint32_t instanceStart uint32_t instanceSize uint32_t reserved uint8_t* ivarLayout char const* name method_list_t* baseMethods protocol_list_t* baseProtocols ivar_list_t* ivars uint8_t* weakIvarLayout property_list_t* baseProperties

Classes class_t class_t *isa class_t *superclass struct cache class_ro_t *vtable class_ro_t uint32_t flags uint32_t instanceStart uint32_t instanceSize uint32_t reserved uint8_t* ivarLayout char const* name method_list_t* baseMethods protocol_list_t* baseProtocols ivar_list_t* ivars uint8_t* weakIvarLayout property_list_t* baseProperties

Classes class_t class_t *isa class_t *superclass struct cache class_ro_t *vtable class_ro_t uint32_t flags uint32_t instanceStart uint32_t instanceSize uint32_t reserved uint8_t* ivarLayout char const* name method_list_t* baseMethods protocol_list_t* baseProtocols ivar_list_t* ivars uint8_t* weakIvarLayout property_list_t* baseProperties

Classes class_t class_t *isa class_t *superclass struct cache class_ro_t *vtable class_ro_t uint32_t flags uint32_t instanceStart uint32_t instanceSize uint32_t reserved uint8_t* ivarLayout char const* name method_list_t* baseMethods protocol_list_t* baseProtocols ivar_list_t* ivars uint8_t* weakIvarLayout property_list_t* baseProperties

Classes method_list_t uint32_t entsize uint32_t count method_t first[]
SEL name char* types void* imp
SEL name char* types void* imp

Classes method_list_t uint32_t entsize uint32_t count method_t first[]
SEL name char* types void* imp
SEL name char* types void* imp

Parsing a Mach-O binary: methods and typing
Types and Methods
All objc classes and methods are parsed from the Mach-O headers and added to Binary Ninja objc_msgSend calls to method calls objc_msgSend calls are replaced with the method they actually call in the
ObjCGraphView adding xrefs
Methods are cross-referenced with the objc_msgSend calls rather than just their structures in the objc sections

Future
DataRenderer for classes, properties, and protocols
More objc_* methods handled
Integration with my proof-of-concept MLIL decompiler
...your pull requests!
https://github.com/trailofbits/ObjCGraphView

Demo: Calculator

Demo: Shlayer?

WindTail overview
●
Taha Karim (Dark Matter) - Hack in the
Box Singapore presentation "In the Trails of WINDSHIFT APT" revealed malware targeting Middle East
●
Authors used unique exploitation technique leveraging custom URL schemes
●
Creates Login item for persistence
●
Hardcoded AES key - Base64 encoded and AES 256 encrypted strings

Demo: WindTail
Sample/Analysis (Objective-See):
https://objective-see.com/blog/blog_0x3B.html

Questions?
Erika Noerenberg
Carbon Black enoerenberg@carbonblack.com
@gutterchurl
Josh Watson
Trail of Bits josh@trailofbits.com
@josh_watson https://twitch.tv/syrillian