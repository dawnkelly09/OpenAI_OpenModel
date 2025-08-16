# cURL

 Threat Model
 December 13, 2022
 Prepared for:
 Daniel Stenberg,  cURL
 Open Source Security Foundation (OpenSSF)
 Open Source Technology Improvement Fund
 Prepared by:  Alex Useche and  Anders Helsing

 About Trail of Bits
 Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high- end security research with a real -world attacker mentality to reduce risk and fortify code. With 80+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
 We maintain an exhaustive list of publications at  https://github.com/trailofbits/publications , with links to papers, presentations, public audit reports, and podcast appearances.
 In recent years, Trail of Bits consultants have showcased cutting-edge research through presentations at CanSecWest, HCSS, Devcon, Empire Hacking, GrrCon, LangSec, NorthSec, the O’Reilly Security Conference, PyCon, REcon, Security BSides, and SummerCon.
 We specialize in software testing and code review projects, supporting client organizations in the technology, defense, and ﬁnance industries, as well as government entities. Notable clients include HashiCorp, Google, Microsoft, Western Digital, and Zoom.
 Trail of Bits also operates a center of excellence with regard to blockchain security. Notable projects include audits of Algorand, Bitcoin SV, Chainlink, Compound, Ethereum 2.0,
 MakerDAO, Matic, Uniswap, Web3, and Zcash.
 To keep up to date with our latest news and announcements, please follow  @trailofbits  on
 Twitter and explore our public repositories at  https://github.com/trailofbits .  To engage us directly, visit our “Contact” page at  https://www.trailofbits.com/contact ,  or email us at info@trailofbits.com .
 Trail of Bits, Inc.
 228 Park Ave S #80688
 New York, NY 10003 https://www.trailofbits.com info@trailofbits.com
 Trail of Bits 1

 Notices and Remarks
 Copyright and Distribution
 © 2022 by Trail of Bits, Inc.
 All rights reserved. Trail of Bits hereby asserts its right to be identiﬁed as the creator of this report in the United Kingdom.
 This report is considered by Trail of Bits to be public information;  it is licensed to Linux
 Foundation under the terms of the project statement of work and has been made public at
 Linux Foundation’s request.  Material within this report  may not be reproduced or distributed in part or in whole without the express written permission of Trail of Bits.
 Analysis Coverage Disclaimer
 All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and mutually agreed upon project plan.
 Security assessment projects are time-boxed and often reliant on information that may be provided by a client, its aﬃliates, or its partners. As such, the ﬁndings documented in this report should not be considered a comprehensive list of security issues, ﬂaws, or defects in the target system or codebase.
 Trail of Bits 2

 Table of Contents
 About Trail of Bits 1
 Notices and Remarks 2
 Table of Contents 2
 Executive Summary 5
 Project Summary 6
 Project Coverage 7
 System Diagrams 8
 High-Level Data Flow 8
 Binary Data Flow 9
 Components 10
 High-Level Breakdown 10
 Binary Breakdown 11
 Trust Zones 14
 Trust Zone Connections 15
 Connection Type and Authentication Breakdown 17
 Threat Actors 19
 Threat Actor Paths 20
 Possible Attack Vectors 21
 Summary of Recommendations 22
 Summary of Findings 23
 Detailed Findings 24 1. Proxy credentials are cached without encryption 24
 Trail of Bits 3

 2. Lack of support for MQTT over TLS 25 3. No warnings when TLS connection attempts fail with the --ssl ﬂag 26 4. Contributing guidelines lack recommendations against using insecure C functions 27 5. cURL treats localhost as secure by default 28 6. Insuﬃcient input validation strategy 29 7. Lack of documentation on supported protocol features and RFC compliance 30
 A. Methodology 31
 B. Security Controls and Rating Criteria 32
 C. CVE Analysis 35
 High-Level Analysis 39
 CIA Triad Impact 39
 Common CWEs 39
 Common Concerns 40
 D. Fix Review Results 41
 Detailed Fix Review Results 42
 Trail of Bits 4

 Executive Summary
 Engagement Overview
 The Linux Foundation, via OpenSSF and strategic partner Open Source Technology
 Improvement Fund, engaged Trail of Bits to conduct a component-focused threat model of its cURL. From September 6 to October 7, 2022, a team of two consultants conducted a threat model of cURL and libcurl. Details of the project’s timeline, test targets, and coverage are provided in subsequent sections of this report.
 Project Scope
 Our assessment focused on the identiﬁcation of security control ﬂaws that could result in a compromise of conﬁdentiality, integrity, or availability of the target system, especially with respect to the controls noted in the category breakdown table  below. An exhaustive list of security control types and their deﬁnitions can be found in  Appendix B .
 Summary of Findings
 The audit uncovered one design-level issue that could lead to vulnerabilities that compromise conﬁdentiality, integrity, or availability of users and data handled by the system under audit.
 FINDINGS BY SEVERITY
 Severity
 Count
 High 1
 Medium 3
 Informational 3
 FINDINGS BY CONTROL TYPE
 Category
 Count
 System and Information
 Integrity 1
 Awareness and Training 3
 System and
 Communications Protection 1
 Audit and Accountability 1
 Conﬁguration Management 1
 Trail of Bits 5

 Project Summary
 Contact Information
 The following managers were associated with this project:
 Dan Guido , Account Manager
 Mary O’Brien , Project  Manager dan@trailofbits.com mary.obrien@trailofbits.com
 Derek Zimmer , Program Manager  Amir Montazery , Program  Manager derek@ostif.org amir@ostif.org
 The following engineers were associated with this project:
 Alex Useche , Consultant
 Anders Helsing ,  Consultant alex.useche@trailofbits.com anders.helsing@trailofbits.com
 Project Timeline
 The signiﬁcant events and milestones of the project are listed below.
 Date
 Event
 September 2, 2022
 Pre-project kickoﬀ call
 September 13, 2022
 Status meeting #1
 September 16, 2022
 Interview meeting
 September 20, 2022
 Status meeting #2
 September 27, 2022
 Delivery of preliminary ﬁnal  report
 October 11, 2022
 Delivery of ﬁnal report draft
 December 13, 2022
 Delivery of ﬁnal report with ﬁx  review
 Trail of Bits 6

 Project Coverage
 During a threat modeling assessment, engineers generally aim to cover the entire target system as a coherent whole. In some cases, however, certain components may be either unnecessary to examine, or impossible to review thoroughly.
 Security Controls
 The following security controls were used to evaluate the project targets during threat modeling exercises. Further information regarding security controls can be observed within
 Appendix B .
 ●  Access Controls
 ●  Audit and Accountability
 ●  Awareness and Training
 ●  Conﬁguration Management
 ●  Cryptography
 ●  Denial of Service
 ●  Identiﬁcation and Authentication
 ●  Risk Assessment
 ●  System and Communications Protection
 ●  System and Information Integrity
 Limitations
 Because of the time-boxed nature of testing work, it is common to encounter coverage limitations. During this project, we focused on considering threats to cURL, including the command-line utility and libcurl. However, because cURL supports a long list of protocols, we chose not to treat each protocol implementation as a discrete component. As a result, our review considers support for various protocols at a high level while focusing on core components of cURL such as parsing, ﬁle input, output operations, and polling of connections.
 Trail of Bits 7

 System Diagrams
 The following diagrams depict the relationships between the target system’s various components and trust zones, as well as the potential paths of threat actors within them.
 High-Level Data Flow
 Trail of Bits 8

 Binary Data Flow
 Trail of Bits 9

 Components cURL is a command-line utility and C library for data transfers with upstream servers over several supported protocols. The following tables describe the various components of cURL considered for the threat model.
 High-Level Breakdown
 Component
 Description cURL Binary
 The binary uses libcurl and is compiled with a TLS library. This includes either cURL, the command line utility, or any application built with libcurl.
 Upstream Server
 The server with which cURL communicates (e.g., an HTTPS or FTP server).
 Can be located either on the internet or an intranet. May redirect communication to another upstream server.
 Proxy
 A proxy, either on the internet or an intranet, with which cURL is conﬁgured for making requests to the upstream server.
 Memory storage cURL uses in-process memory storage to save connections, TLS sessions,
 DNS responses, and other data.
 Local ﬁle system cURL uses the local ﬁle system to store and retrieve cookies, alternative service (alt-svc) information, HSTS entries, TLS certiﬁcates, logging output, environment variables, and other data. It can also load conﬁguration ﬁles with options to use cURL.
 libcurl
 The core library on top of which cURL is built.
 DNS server
 Domain name resolution, with which cURL communicates for translating domain names to IP addresses and vice versa.
 Local socker
 Unix socket with which cURL can communicate via the  --unix-socket
 ﬂag.
 CA Store
 Used by the TLS library with which cURL is compiled. For some libraries
 (such as OpenSSL), cURL is responsible for iterating through the ﬁles in a
 CA store.
 Trail of Bits 10

 Binary Breakdown
 Component
 Description
 Protocols cURL supports several protocols that allow for two-way data transfers, most of which support URI schemes. We list protocols supported under the ﬁve categories listed below.
 File Transfer
 SCP, FILE, FTP, FTPS, SFTP, TFTP, SMB, SMBS
 Mail
 IMAP, IMAPS, POP3, POP3S, SMTP, SMTPS
 HTTP
 HTTP, HTTPS, WS, WSS
 Streaming
 RTSP, RTMP, RTMPS
 IoT
 MQTT
 Other / Legacy
 GOPHER, GOPHERS, LDAP, LDAPS, DICT, TELNET
 SSL/TLS
 Logic for handling in-transit encryption
 TLS Connectors
 TLS logic within the libcurl responsible for interacting with TLS libraries
 TLS library
 The TLS library with which cURL was compiled. cURL supports the following libraries: AmiSSL, BearSSL, BoringSSL, GnuTLS, libressl, mbedTLS, NSS, OpenSSL, rustls, Schannel, Secure Transport, and WolfSSL.
 File I/O
 Operations in cURL responsible for loading working with ﬁles stored on the system hard drive.
 Cookie Engine
 The cURL cookie engine keeps track of cookies for HTTP and HTTPS requests and uses the ﬁle system to load cookies and store cookie changes.
 Alt-svc
 Similar to the cookie engine, altsvc.c keeps track of atl-svc headers and loads them from local ﬁle storage.
 HSTS
 Similar to the cookie engine, hsts.c keeps track of HSTS header values and
 Trail of Bits 11

 loads them from local ﬁle storage.
 Other cURL can also read environment ﬁles from memory, as well as other ﬁles for various operations, including
 ● etags
 ●
 TLS certiﬁcates
 ●
 Conﬁguration ﬁles such as  .netrc and  .curlrc
 Networking
 Logic responsible for establishing and maintaining connections to the various protocols.
 PINGPONG
 Generic back-and-forth support functions for certain protocols (e.g., FTP,
 IMAP, POP3, and SMTP).
 Connection Reuse
 The functionality for connection reuse via the connection cache.
 Proxy communication
 Logic for communicating via proxies.
 DNS logic
 Logic responsible for name resolution via ﬂags like  --dns-servers and
 --doh-url  .
 Local socket communication
 Logic responsible for communicating with local sockets via
 --unix-socket  .
 Parsing
 Logic used by cURL to parse request and response data.
 Parsers
 Parser logic in various APIs that are part of libcurl. For instance, the header API parses various request and response headers, and the URL
 API parses URLs used for various requests.
 Encoders &
 Decoders cURL’s logic for encoding and decoding various data types, such as HTTP content types (deﬂate, gzip, zstd, and br) and chunked HTTP requests.
 C Logic
 Any other logic dealing in the cURL codebase that could lead to potential vulnerabilities, including unrestricted recursions and memory bugs.
 Memory operations
 Operations such as memory and buﬀer allocations.
 Concurrency / Async
 Operations responsible for calling operations asynchronously (e.g., making requests in a non-blocking manner).
 Trail of Bits 12

 Rate limiting
 Operations that limit request rates.
 Other C programming logic
 Any other logic that could lead to bugs in the application.
 Trail of Bits 13

 Trust Zones
 Systems include logical “trust boundaries” or “zones” in which components may have diﬀerent criticality or sensitivity. Therefore, to further analyze a system, we decompose components into zones based on shared criticality rather than physical placement in the system. Trust zones capture logical boundaries where controls should or could be enforced by the system and allow designers to implement interstitial controls and policies between zones of components as needed.
 Zone
 Description
 Included Components
 Internet
 The externally facing, wider internet zone. Components in this zone are untrusted.
 ●
 Upstream server
 ●
 Proxy
 ●
 DNS server
 Intranet
 Local network hosting the system running the cURL binary.
 ●
 Upstream server
 ●
 Optional proxy
 Local system
 The local system running the cURL binary.
 ● cURL binary:
 Protocols, SSL/TLS,
 File I/O, Networking,
 Parsing, C logic, etc
 ●
 Files
 ●
 CA Store
 ●
 Memory storage
 Trail of Bits 14

 Trust Zone Connections
 At a design level, trust zones are delineated by the security controls that enforce the diﬀering levels of trust within each zone. As such, it is necessary to ensure that data cannot move between trust zones without ﬁrst satisfying the intended trust requirements of its destination. We enumerate such connections between trust zones below.
 Originating
 Zone
 Destination
 Zone
 Data Description
 Connection
 Type
 Authentication
 Type
 Local system
 Internet
 User data submitted via protocol speciﬁcations to the upstream server.
 Optionally, connection to proxy between server and cURL binary.
 See  Connection
 Type
 Breakdown
 DNS for name resolution
 ●
 Proxy authentication
 ●
 See
 Connection
 Type
 Breakdown
 Local
 System
 Intranet
 User data submitted via protocol speciﬁcations to the upstream server.
 Optional connection to proxy between server and cURL binary.
 See  Connection Type Breakdown
 Local
 System
 Local
 System cURL can make requests to Unix sockets using
 GET and POST requests.
 cURL can generate C code by specifying a cURL command and using the  --libcurl
 ﬂag.
 N/A
 Local ﬁle IO for various tasks (see components table for a list), including conﬁguration ﬁle reads.
 Environment variables
 Trail of Bits 15

 are read by cURL, which could change its behavior. Environmental variables are read from memory and include settings that can in many cases be speciﬁed in conﬁguration ﬁles instead.
 Local
 Network
 Local
 System
 Upstream servers on the local network with which cURL has established a connection will return data to a local system.
 Connections could be proxied via external or internal proxy servers.
 See  Connection Type Breakdown
 Local
 Network
 Internet
 Proxy located in the intranet that sends data to an upstream server located on the internet.
 Data that was originally sent to a server in the intranet, but was redirected (fully or partially) to a server on the internet.
 Trail of Bits 16

 Connection Type and Authentication Breakdown
 The following table lists additional details regarding connection types and authentication methods available for supported protocols. For many protocols such as SMB, users can authenticate by sending credentials as part of the URI or request headers. However, we list only authentication types supported when cURL has a speciﬁc ﬂag that users can pass to specify username and password and authentication types.
 Protocol
 Stateful
 Stateless
 TCP
 UDP
 Authentication
 WS / WSS
 X
 X
 -
 RTSP
 X
 X
 -
 RTMP / RTMPS
 X
 X
 X
 -
 MQTT
 X
 X
 ●
 Username and password
 IMAP / IMAPS
 X
 X
 ●
 Username and password
 POP3 / POP3S
 X
 X
 ●
 Username and password
 SMTP / SMTPS
 X
 X
 ●
 Username and password
 SCP
 X
 X
 ●
 Certiﬁcate authentication
 ●
 Username and password
 FTP /  FTPS / SFTP
 X
 X
 ●
 Username and password
 ●
 Certiﬁcate authentication ( for
 SFTP)
 ●
 Kerberos4 (for FTP)
 ● kerberos5/GSSAPI (for
 FTP)
 Trail of Bits 17

 SMB / SMBS
 X
 X
 ●
 Username and password
 LDAP /  LDAPS
 X
 X
 X
 ●
 Basic
 ●
 NTLM
 ●
 Digest
 TELNET
 X
 X
 -
 HTTP / HTTPS
 X
 X
 ●
 Basic
 ●
 Digest
 ●
 NTLM
 ●
 Negotiate
 ●
 Bearer
 FILE
 X
 X
 -
 TFTP
 X
 X
 -
 GOPHER / GOPHERS
 X
 X
 -
 DICT
 X
 X
 -
 FILE
 N/A
 N/A
 N/A
 N/A
 -
 Trail of Bits 18

 Threat Actors
 Similarly to establishing trust zones, deﬁning malicious actors when conducting a threat model is useful in determining which protections, if any, are necessary to mitigate or remediate a vulnerability. We will use these actors in all subsequent ﬁndings from the threat model. Additionally, we deﬁne other “users” of the system who may be impacted by, or induced to undertake, an attack. For example, in a confused deputy attack such as cross-site request forgery, a normal user would be both the victim and the potential direct attacker, even though that user would be induced to undertake the action by a secondary attacker.
 Actor
 Description
 External attacker
 An attacker on the internet. They can control servers and proxies on the internet, eavesdrop, and create Man-in-the-Middle (MitM)
 connections in the internet space.
 Internal attacker
 An attacker on the intranet. They can eavesdrop and create MitM connections on the intranet. They cannot control either servers or proxies on the intranet.
 Local attacker
 An attacker sitting on the same machine where cURL application is being run. Has the same or lower level of privileges as the end user.
 End user
 A user who runs a built cURL binary.
 libcurl user
 Integrates libcurl in custom-developed applications.
 Contributor
 Regular contributor to the project.
 Maintainer
 A gatekeeper controlling additions to the project.
 Malicious dependency developer
 A source code dependency of curl that has been compromised.
 Trail of Bits 19

 Threat Actor Paths
 Deﬁning attackers’ paths through the various zones is useful when analyzing potential controls, remediations, and mitigations that exist in the current architecture.
 Originating
 Zone
 Destination
 Zone
 Actor
 Description
 Internet
 Internet
 Malicious dependency developer
 Attackers can introduce malicious code in dependencies used in the cURL codebase, compromising users of the libcurl application and the cURL command line.
 Internet
 Intranet
 External
 Attacker
 Attackers will try to leak sensitive data intended only for intranet components. Similarly, they could target internal proxies used by cURL.
 Internet
 Local system
 External
 Attacker
 Attackers will attempt to manipulate data handled by cURL applications to gain access to the local system (e.g., by exploiting memory corruption bugs), to perform DoS attacks on the local system, or to inﬁltrate the system's internal network (e.g., via attacks similar to server-side request forgery).
 Intranet
 Intranet
 Internal Attacker
 Attackers will attempt to ﬁnd and exploit bugs in cURL’s network protocol implementations in order to bypass the protocols’ security controls. Examples include dropping encryption from connections, downgrading protocol versions, impersonating authenticated connections, injecting data into established connections, and impersonating servers.
 Trail of Bits 20

 Local system
 Local system
 Local attacker
 Attackers with access to a system running cURL will attempt local privilege escalation attacks by manipulating the local environment
 (variables, ﬁles, conﬁgurations, etc.)
 prior to end users' usage of the cURL application.
 Possible Attack Vectors
 At a high level, we consider the following non-exhaustive list of potential attack vectors based on the above analysis, in addition to the information gathered in our CVE analysis in
 Appendix C . Note that this list does not indicate  there are vulnerabilities in each listed area; rather, it describes possible attack areas where attackers may look for points of failures and vulnerabilities to take advantage of.
 ●  Invalid usage of libcurl by third-party application developers
 ●  Flaws in protocols implementations, including:
 ○  Proxy communication
 ○  Non-conformance with protocol standards
 ○  Stateful vs. stateless protocol treatments
 ○  Authentication correctness issues
 ●  Connection reuse ﬂaws leading to issues such as  CVE-2022-22576  and
 CVE-2022-27782
 ●  Unexpected default behavior
 ●  Flawed cross-endpoint transfers such as insuﬃcient Same Origin Policy correctness and insecure HTTP redirects
 ●  Flawed cross-protocol communication logic (e.g., redirects to other protocols, HTTP version changes, HTTP connection upgrades)
 ●  Data transformations such as parsing, serialization, encoding, and data validation
 ●  Memory safety issues
 ●  Interaction with local system
 ●  Insecure interaction with the kernel via networking interfaces or Unix sockets
 ●  Incorrect or insecure DNS usage
 ●  Race conditions and other concurrency bugs
 ●  vTLS and TLS integration issues such as ﬂaws in HSTS parsing or handling of certiﬁcates
 Trail of Bits 21

 Summary of Recommendations
 Throughout the engagement, Trail of Bits identiﬁed a number of threat scenarios that may introduce risk within cURL. Trail of Bits recommends that the Linux Foundation address the
 ﬁndings detailed in this report and take the following additional steps to further build upon threat modeling exercises:
 ●  Document deviations from RFCs and invariants for the various supported protocols, as a way to both inform cURL users of such deviations and document features that can be implemented or improved upon by cURL contributors. This can also drive property-based testing eﬀorts.
 ●  Consider implementing a property-based testing strategy driven by requirements speciﬁed by the RFCs for the various protocols supported by cURL.
 ●  Devise a centralized input validation that relies on allowlists rather than denylists for checking against certain illegal characters per RFC speciﬁcations such as  RFC 1738 .
 ●  Consider using tools such as  weggli  that allow you  to write custom static analysis rules to run checks against potential issues, including non-conformance to RFC speciﬁcation, insecure use of C functions such as  malloc  , and use of other insecure functions. These checks should run before merging pull requests into the codebase.
 ●  Always default to secure settings for any operations that cURL performs. Implement terminal ﬂags (such as  -k for skipping certiﬁcate  validation) to force users to tell cURL to skip or bypass secure defaults. See the recommendations in  TOB-CURLTM-4 for a speciﬁc example.
 Trail of Bits 22

 Summary of Findings
 The table below summarizes the ﬁndings of the review, including type and severity details.
 ID
 Title
 Type
 Severity 1
 Proxy credentials are cached without encryption
 System and
 Information
 Integrity
 Medium 2
 Lack of support for MQTT over TLS
 System and
 Communications
 Protection
 Medium 3
 No warnings when TLS connection attempts fail with the --ssl ﬂag
 Audit and
 Accountability
 Informational 4
 Contributing guidelines lack recommendations against using insecure C functions
 Awareness and
 Training
 Medium 5 cURL treats localhost as secure by default
 Conﬁguration
 Management
 Informational 6
 Insuﬃcient input validation strategy
 Awareness and
 Training
 High 7
 Lack of documentation on supported protocol features and RFC compliance
 Awareness and
 Training
 Informational
 Trail of Bits 23

 Detailed Findings 1. Proxy credentials are cached without encryption
 Severity:  Medium
 Diﬃculty:  High
 Type: System and Information Integrity
 Finding ID: TOB-CURLTM-1
 Target:  cURL
 Description
 Users are able to conﬁgure cURL to communicate with the upstream server using a proxy they specify. cURL caches credentials for proxies provided by users in memory, so they can be reused for subsequent connections. These credentials are stored in memory in plaintext.
 Threat Scenario
 An attacker with access to the system running cURL uses a utility to dump heap memory used by cURL. The attacker then lists the credentials that the proxy uses to connect to the proxy and re-uses them to authenticate to it.
 Justiﬁcation
 The severity is medium. Access to proxy credentials could allow the attacker to compromise the proxy.
 The diﬃculty is high. Access to the system running cURL is required. Furthermore, the attacker would need to be able to run a utility to dump process memory from cURL.
 Recommendations
 Short term, consider encrypting proxy credentials in memory and clearing them as soon as they are no longer needed.
 Trail of Bits 24

 2. Lack of support for MQTT over TLS
 Severity:  Medium
 Diﬃculty:  High
 Type: System and Communications
 Protection
 Finding ID: TOB-CURLTM-2
 Target: cURL, libcurl
 Description cURL supports data transfers and communication over the MQTT protocol. This protocol allows a client, such as a cURL, to communicate with an MQTT and subscribe to events for user-deﬁned topics. However, communications with MQTT that are brokered over TLS
 (MQTTS) are not supported by cURL.
 Threat Scenario
 Eve decides to use cURL for data transfers over MQTT. She realizes that cURL does not support MQTTS, so she decides to instead communicate with the non-TLS MQTT broker.
 Her communications with the broker are now intercepted by an attacker in the network, resulting in a loss of conﬁdentiality.
 Justiﬁcation
 The severity is medium. Attackers with an MitM position will be able to read MQTT communications in plaintext.
 The diﬃculty is high. Attackers would need to position themselves in the network and be able to capture communications between cURL and the upstream server. Furthermore, users are likely to use other utilities when they need to communicate with MQTTS servers.
 Recommendations
 Short term, extend cURL to support MQTT over TLS.
 Trail of Bits 25

 3. No warnings when TLS connection attempts fail with the  --ssl  ﬂag
 Severity:  Informational
 Diﬃculty:  High
 Type: Audit and Accountability
 Finding ID: TOB-CURLTM-3
 Target: cURL
 Description cURL supports enabling TLS for  various protocols  with  the  --ssl ﬂag. This ﬂag tells cURL to communicate with the upstream server over TLS if the server supports it. In cases where cURL is unable to connect over TLS, data transfers will continue over plaintext or non-TLS connections without warning the user that the connection was not upgraded to TLS. Note that users can force the use of SSL by specifying the  --ssl-reqd ﬂag.
 Threat Scenario
 A user uses cURL to communicate with a server and speciﬁes  --ssl  . The connection upgrade fails, and due to the lack of warning, the user believes the connection was established over TLS.
 Recommendations
 Short term, add a warning to STDOUT to notify users when connection upgrades fail.
 Consider adding a ﬂag to allow users to ignore such warnings if they wish.
 Trail of Bits 26

 4. Contributing guidelines lack recommendations against using insecure C functions
 Severity:  Medium
 Diﬃculty:  Medium
 Type: Awareness and Training
 Finding ID: TOB-CURLTM-4
 Target: cURL, libcurl
 Description
 The cURL website includes documentation on  contribution  guidelines  and a  C style guide .
 However, neither document includes guidelines mandating or recommending secure C coding practices and standards, such as discouraging the use of insecure functions like strcpy  ,  atoi  , and  fscanf  . Although cURL uses  scripts/checksrc.pl to disallow the use of certain functions, guidelines should exist that recommend secure C coding standards for contributors, particularly as some functions such as  strcpy are not disallowed by the same script.
 Threat Scenario
 A developer pushes insecure code to cURL that is not caught by automated scripts or PR reviewers, introducing new vulnerabilities into the application or library.
 Justiﬁcation
 The severity is medium. Insecure code and functions such as  atoi and  strcpy pushed to the codebase can introduce undeﬁned behavior and other bugs that could lead to vulnerabilities such as code execution.
 The diﬃculty is medium. The  scripts/checksrc.pl script checks against the use of a list of banned functions listed in  docs/CHECKSRC.md  . Pull  request requirements also reduce the likelihood that insecure code may be introduced.
 Recommendations
 Short term, include secure C coding guidelines in either the contribution guidelines or the C style guide. Either document should list the banned function that  scripts/checksrc.pl checks against. If functions such as  scripts/checksrc.pl continue to be avoidable by using non-standard libraries, the same document should describe how these functions should be used.
 Trail of Bits 27

 5. cURL treats localhost as secure by default
 Severity:  Informational
 Diﬃculty:  High
 Type: Conﬁguration Management
 Finding ID: TOB-CURLTM-5
 Target: cURL, libcurl
 Description
 By default, cURL assumes that connection requests to  localhos  t,  127.0.0.  1, and  [::1]
 are secure and disables relevant security features, such as accepting the use of the  secure cookie ﬂag for insecure connections to  localhost and cURL skipping name resolution checks. This may mislead cURL users into believing that their connections to  localhost are secure.
 Threat Scenario
 A web developer uses cURL to make requests against a site they are developing and running on  http://localhost:8080  . Since cURL accepts  and honors secure cookies from an insecure  localhost  , the developer assumes  the application's behavior in localhost will match when it is deployed to production  and makes assumptions about how the cookie ﬂags will be treated when deploying to production.
 Recommendations
 Short term, explicitly document how cURL treats requests to  localhost diﬀerently than requests to upstream servers.
 Long term, update cURL so that it treats  localhosts securely by default, and introduce a
 ﬂag that users can use when calling cURL to turn oﬀ insecure behavior, such as disallowing cookies with the secure ﬂag to be sent to  localhost endpoints. This ﬂag can work similarly to  -k  , which users can use when leveraging  self-signed certiﬁcates to bypass validation.
 Trail of Bits 28

 6. InsuĆcient input validation strategy
 Severity:  High
 Diﬃculty:  Medium
 Type: Conﬁguration Management
 Finding ID: TOB-CURLTM-6
 Target: cURL, libcurl
 Description cURL performs input sanitization using a denylist of characters rather than strongly validating characters against an allowlist, regex, or similar. For instance, cURL allows potentially unsafe characters into cookie jar ﬁles, which could lead to broken functionality.
 This behavior deviates from relevant RFC speciﬁcations such as  RFC 1738 , which deﬁnes a set of permitted characters for URIs and disallows all others.
 Threat Scenario
 A zero-day exploit that takes advantage of weak URI validation is used against applications that rely on libcurl. Attackers leverage the exploit to compromise the conﬁdentiality, integrity, or availability of user data and services that rely on such applications.
 Justiﬁcation
 The severity is high. Because validation relies in many cases on denylists, it is diﬃcult to account for future attacks that could make cURL vulnerable to attacks allowing malicious actors to compromise users, perform privilege escalation, or use cURL to run custom code remotely.
 The diﬃculty is medium. There are no immediate concerns regarding allowed characters which cURL may not account for in their deny lists. However,  deny lists are diﬃcult to maintain and provide little protection against potential zero-day attacks, as new exploits may rely on the use of characters such as ‘  \t  ‘, which  cURL may not verify against.
 Recommendations
 Short term, default to using allow lists for sanitization and validation strategies for the various parsing tasks that cURL performs, such as cookie and URI parsing routines.
 Long term, review RFCs for the various protocols and strings that cURL works with and parses and assure that the code conforms to the expectations outlined in such documents.
 Additionally, follow recommendations for  TOB-CURLTM-6 .
 Trail of Bits 29

 7. Lack of documentation on supported protocol features and RFC compliance
 Severity:  Informational
 Diﬃculty:  High
 Type: Awareness and Training
 Finding ID: TOB-CURLTM-7
 Target: cURL, libcurl
 Description cURL supports communications with upstream servers that rely on multiple protocols such as those listed in the  Components table  of this document.  Data communications with each protocol must conform to the RFC documentation that is publicly available for each protocol. In some cases, conformance to RFC requirements is not strictly enforced by cURL for each protocol. Although upstream servers with which cURL communicates should enforce data conformance to applicable RFC requirements, attackers could take advantage of cURL’s non-strict conformance to the same RFC for various attacks. Moreover, users of cURL, including application developers relying on libcurl, may incorrectly assume full compliance with the various protocol RFCs.
 Threat Scenario
 A developer makes assumptions about cURLs compliance to RFCs and implements a feature insecurely. An attacker notices this non-compliance and takes advantage of it to craft new attacks.
 Recommendations
 Short term, document deviations from RFCs and make it easily available for users of cURL so they understand where cURL stops data validation against RFC standards and when the responsibility is placed on upstream servers, developers, and users of cURL.
 Long term, implement a property-based testing strategy that relies on testing speciﬁc properties deﬁned in the RFC documents for every supported protocol.
 Trail of Bits 30

 A. Methodology
 Trail of Bits’s threat modeling assessments are intended to provide a detailed analysis of the risks facing an application at a structural and operational level, assessing the security of its design as opposed to its implementation details. During these assessments, engineers rely heavily on frequent meetings with the client’s developers, paired with extensive readings of any and all documentation the client can make available. Code review and dynamic testing are not an integral part of threat modeling assessments, although engineers may occasionally consult the codebase or a live instance to verify speciﬁc assumptions about the system’s design.
 Engineers begin a threat modeling assessment by identifying the safeguards and guarantees that are critical to maintaining the target system’s conﬁdentiality, integrity, and availability. These  security controls  dictate the  assessment’s overarching scope, and are determined based on the speciﬁc requirements of the target system, which may include technical and reputational concerns, legal liability, regulatory compliance, and so on.
 With these security controls in mind, engineers then divide the system into logical components —discrete elements that perform speciﬁc  tasks—and establish  trust zones around groups of components that lie within a common trust boundary. They identify the types of data handled by the system, enumerating the points at which data is sent, received, or stored by each component, as well as within and across trust boundaries.
 Having established a detailed map of the target system’s structure and data ﬂows, engineers then identify  threat actors —anyone who might  threaten the target’s security, whether a malicious external attacker, a naive insider, or otherwise. Based on each threat actor’s initial privileges and knowledge,  threat actor  paths  are then traced out through the system, establishing which controls and data a threat actor might be able to improperly access, as well as which safeguards stand in the way of such compromise. Any viable attack path discovered in this way constitutes a  ﬁnding ,  which will also be paired with design recommendations by which such gaps in the system’s defenses can be remediated.
 After enumerating a list of ﬁndings, engineers rate the strength of each security control, indicating the general robustness of that type of defense against the full spectrum of possible attacks.
 Trail of Bits 31

 B. Security Controls and Rating Criteria
 The following tables describe the security controls and rating criteria used in this report.
 Security Controls for Threat Modeling assessment
 Category
 Description
 Access Controls
 Authorization (including entitlement, access controls), session management, separation of duties, API and interfaces security, etc.
 Audit and
 Accountability
 Logging, non-repudiation, monitoring, analysis, reporting, etc.
 Awareness and
 Training
 Controls related to policies, procedures, and related capabilities
 Conﬁguration
 Management
 Inventory, secure baselines, conﬁguration management & change control
 Cryptography
 The cryptographic controls implemented at rest, in transit, and in-process
 Denial of Service
 The controls to defend against diﬀerent types of denial-of-service attacks impacting availability
 Identiﬁcation and
 Authentication
 User and system identiﬁcation and authentication controls
 Risk Assessment
 Risk assessment policies, vulnerability scanning capabilities, and risk management solutions.
 System and
 Communications
 Protection
 Network level controls to protect data, network security, component security, and hardening, vendors’ solutions and their integration, security of elements build internally
 System and
 Information
 Integrity
 Software integrity, malicious code protection, monitoring, information handling, and related controls
 Rating Criteria
 Rating
 Description
 Trail of Bits 32

 Strong
 The security control was reviewed and no concerns were found.
 Satisfactory
 The security control had only minor issues; though it may lack certain non-critical operational procedures or security measures, their absence does not expose users to a signiﬁcant degree of risk. Remediation in this area is suggested, but is not urgent.
 Moderate
 The security control had several issues or an impactful issue which may expose users  to some degree of risk, albeit not to a severe degree.
 Remediation in this area is desired.
 Weak
 The security control had several signiﬁcant issues which are likely to expose users to a substantial amount of risk. Remediation in this area should be prioritized.
 Missing
 The security control was found to be nonexistent or totally ineﬀective for its intended purpose, despite being necessary for the system’s security.
 The implementation of this control should be prioritized.
 Not Applicable
 The security control is not applicable to this review.
 Not Considered
 The security control was not considered in this review.
 Further
 Investigation
 Required
 Further investigation is required to reach a meaningful conclusion.
 Severity Levels
 Severity
 Description
 Informational
 The issue does not pose an immediate risk but is relevant to security best practices.
 Undetermined
 The extent of the risk was not determined during this engagement.
 Low
 The risk is small or is not one the client has indicated is important.
 Medium
 User information is at risk; exploitation could pose reputational, legal, or moderate ﬁnancial risks.
 High
 The ﬂaw could aﬀect numerous users and have serious reputational, legal, or ﬁnancial implications.
 Diﬃculty Levels
 Trail of Bits 33

 Diﬃculty
 Description
 Undetermined
 The diﬃculty of exploitation was not determined during this engagement.
 Low
 The threat is well known or common; an attacker can exploit it without signiﬁcant eﬀort or specialized knowledge.
 Medium
 An attacker must acquire in-depth knowledge of the system or expend a non-trivial amount of eﬀort in order to exploit this issue.
 High
 An attacker must acquire complex insider knowledge or privileged access to the system in order to exploit this issue.
 Trail of Bits 34

 C. CVE Analysis
 We analyzed the last CVEs (33) reported for cURL over the past three years. For each CVE, we examined the CWE to determine the key root cause and which aspects of the CIA triad were aﬀected. Next, we determined which key components were aﬀected by each CVE. This allowed us to better understand common attack paths from a historical perspective and to determine commonly aﬀected components and root causes.
 CVE
 CWE
 Root Cause
 Impact
 Component
 CVE-2022-35252:
 control code in cookie denial of service 1286
 Input validation (invalid server cookie accepted)
 Availability
 HTTP
 CVE-2022-32208:
 FTP-KRB bad message veriﬁcation 924
 Data injection (injecting mitm data into error msg)
 Integrity
 FTP or KRB
 CVE-2022-32207:
 Unpreserved ﬁle permissions 281
 File permission problem
 (overwrite does not retain rights)
 Conﬁdentiality
 “cookie.c”
 CVE-2022-32206:
 HTTP compression denial of service 770
 Unbounded compression chain from server
 Availability
 HTTP
 CVE-2022-32205:
 Set-Cookie denial of service 770
 Input validation (invalid server set-cookie:)
 Availability
 HTTP
 CVE-2022-30115:
 HSTS bypass via trailing dot 319
 Data validation (trailing dot can bypass HSTS)
 Conﬁdentiality
 HSTS
 CVE-2022-27782:
 TLS and SSH connection too eager reuse 295 840
 Improper certiﬁcate Validation  Integrity
 CONNECTION
 POOL
 CVE-2022-27781:
 835
 Uncontrolled resource
 Availability
 URL, NSS
 Trail of Bits 35

 CERTINFO never-ending busy-loop 400
 Consumption
 CVE-2022-27780:
 percent-encoded path separator in
 URL host 918 177
 Improper handling of URL encoding
 Integrity
 URL
 CVE-2022-27779:
 cookie for trailing dot TLD 668 201
 Insertion of sensitive information into sent data
 Conﬁdentiality
 URL
 CVE-2022-27778:
 curl removes wrong
 ﬁle on error 706
 Use of incorrectly-resolved name or reference
 Integrity Availability
 TOOL
 CVE-2022-27776:
 Auth/cookie leak on redirect 522
 Insuﬃciently protected credentials
 Conﬁdentiality
 HTTP
 CVE-2022-27775:
 Bad local IPv6 connection reuse 200
 Exposure of sensitive information to an unauthorized actor
 Conﬁdentiality
 CONNECTION
 POOL
 CVE-2022-27774:
 Credential leak on redirect 522
 Insuﬃciently protected credentials
 Conﬁdentiality
 HTTP
 CVE-2022-22576:
 OAUTH2 bearer bypass in connection re-use 287
 Improper authentication
 Conﬁdentiality Integrity
 CONNECTION
 POOL
 CVE-2021-22947:
 STARTTLS protocol injection via MITM 345 310
 Insuﬃcient veriﬁcation of data
 Authenticity / cryptographic
 Issues
 Integrity
 PINGPONG
 (used for several protocols)
 CVE-2021-22946:
 Protocol downgrade required TLS bypassed 319 325
 Missing cryptographic step
 Conﬁdentiality
 PINGPONG
 (IMAP, POP3,
 FTP)
 Trail of Bits 36

 CVE-2021-22945:
 UAF and double-free in MQTT sending 415
 Double free
 Conﬁdentiality
 MQTT
 CVE-2021-22926:
 CURLOPT_SSLCERT mixup with Secure
 Transport 295
 Improper certiﬁcate validation
 Availability
 “DARWIN TLS”
 CVE-2021-22925:
 TELNET stack contents disclosure again 457
 Use of uninitialized variable
 Conﬁdentiality
 TELNET
 CVE-2021-22924:
 Bad connection reuse due to ﬂawed path name checks 295
 Improper certiﬁcate validation
 Conﬁdentiality
 CONNECTION
 POOL
 CVE-2021-22923:
 Metalink download sends credentials 522
 Insuﬃciently protected credentials
 Conﬁdentiality
 TOOL
 CVE-2021-22922:
 Wrong content via metalink not discarded 20
 Improper input validation
 Integrity
 TOOL
 CVE-2021-22901:
 TLS session caching disaster 416
 Use after free
 Availability
 Integrity
 Conﬁdentiality
 CONNECTION
 POOL
 CVE-2021-22898:
 TELNET stack contents disclosure 457
 Use of uninitialized variable
 Conﬁdentiality
 TELNET
 CVE-2021-22897:
 schannel cipher selection surprise 488
 Exposure of data element to wrong session
 Conﬁdentiality
 SCHANNEL
 CVE-2021-22890:
 TLS 1.3 session ticket proxy host 290
 Authentication bypass by spooﬁng
 Integrity
 PROXY or VTLS
 Trail of Bits 37

 mixup
 CVE-2021-22876:
 Automatic referer leaks credentials 359
 Exposure of private personal information to an unauthorized actor
 Conﬁdentiality
 HTTP
 CVE-2020-8286:
 Inferior OCSP veriﬁcation 299
 Improper check for certiﬁcate revocation
 Integrity
 OPENSSL
 CVE-2020-8285: FTP wildcard stack overﬂow 674
 Uncontrolled recursion
 Availability
 FTP
 CVE-2020-8284:
 trusting FTP PASV responses 200
 Exposure of sensitive information to an unauthorized actor
 Conﬁdentiality
 FTP
 CVE-2020-8231:
 wrong connect-only connection 825
 Expired pointer dereference
 Conﬁdentiality
 CONNECTION
 POOL
 CVE-2020-8177: curl overwrite local ﬁle with -J 641
 Improper restriction of names for ﬁles and other resources
 Conﬁdentiality
 TOOL
 CVE-2020-8169:
 Partial password leak over DNS on
 HTTP redirect 200
 Exposure of sensitive information to an unauthorized actor
 Conﬁdentiality
 HTTP
 Trail of Bits 38

 High-Level Analysis
 CIA Triad Impact
 Figure C.1. CIA triad impact
 Common CWEs
 Count
 CWE
 Title 3 200
 Exposure of Sensitive Information to an Unauthorized
 Actor 3 295
 Improper Certiﬁcate Validation 3 522
 Insuﬃciently Protected Credentials 2 319
 Data validation (trailing dot can bypass HSTS)
 2 457
 Use of Uninitialized Variable 2 770
 Allocation of Resources Without Limits or Throttling
 Trail of Bits 39

 Common Concerns
 ●  Mishandling or ineﬀective use of TLS
 ●  Revealing sensitive data in URL concerns by using TLS libraries ineﬀectively or incorrectly
 ●  Caching of sensitive data via cookies (it is unclear how cURL  handles cookies in requests and whether those are or can be cached)
 ●  Uncontrolled recursions or inﬁnite loops that cause code to hang
 Trail of Bits 40

 D. Fix Review Results
 On December 6, 2022, Trail of Bits reviewed the ﬁxes and mitigations implemented by the
 Linux Foundation, via OpenSSF and strategic partner Open Source Technology
 Improvement Fund  team, to resolve the issues identiﬁed  in this report. OpenSSF delivered
 ﬁxes for some of the ﬁndings in this report, with associated pull requests when applicable.
 In summary, Linux Foundation has suﬃciently addressed one of the issues described in this report, partially resolved one, has not resolved two, and stated that they will not take action on three issues.
 We reviewed each ﬁx to determine its eﬀectiveness in resolving the associated issue. For additional information, please see the Detailed Fix Log.
 ID
 Title
 Severity
 Status 1
 Proxy credentials are cached without encryption
 Medium
 Unresolved 2
 Lack of support for MQTT over TLS
 Medium
 Unresolved 3
 No warnings when TLS connection attempts fail with the --ssl ﬂag
 Informational
 Resolved 4
 Contributing guidelines lack recommendations against using insecure C functions
 Medium
 Unresolved 5 cURL treats localhost as secure by default
 Informational
 Partially resolved 6
 Insuﬃcient input validation strategy
 High
 Unresolved 7
 Lack of documentation on supported protocol features and RFC compliance
 Informational
 Unresolved
 Trail of Bits 41

 Detailed Fix Review Results
 TOB-CURLTM-1: Proxy credentials are cached without encryption
 Unresolved. No changes were made at the time of this ﬁx review.
 TOB-CURLTM-2: Lack of support for MQTT over TLS
 Unresolved. No changes were made at the time of this ﬁx review.
 TOB-CURLTM-3: No warnings when TLS connection attempts fail with the  --ssl ﬂag
 Resolved. The cURL team added a warning to cURL as recommended in the reported
 ﬁnding ( PR# 9519 ).
 TOB-CURLTM-4: Contributing guidelines lack recommendations against using insecure C functions
 Unresolved. The cURL team stated they will not be accepting the recommendation in the report.
 TOB-CURLTM-5: cURL treats  localhost as secure by default
 Undetermined. The cURL team stated that they consider  localhost to be secure.
 However, they added documentation to  docs/HTTP-COOKIES.md to explicitly state how localhost is treated as secure by default by cURL  ( PR# 9938 ).
 TOB-CURLTM-6: Insuﬃcient input validation strategy
 Unresolved. The cURL team stated they cannot fully accept the recommendation in the report, citing existing levels of strictness in testing parsers, including with fuzzers. The
 ﬁnding is unresolved as the input validation strategy continues to rely on denylists.
 TOB-CURLTM-7: Lack of documentation on supported protocol features and RFC compliance
 Unresolved. The cURL team stated that they will not address the recommendations provided for this ﬁnding and mentioned that all supported features are documented in depth, with details and examples. They also noted the infeasibility of documenting compliance with RFCs.
 Trail of Bits 42