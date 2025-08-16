# Your Mitigations are My

Opportunities
Yarden Shafir

About Me
◦
Sr. Security Engineer at Trail of Bits
◦
Previously Sr. Software Engineer at CrowdStrike and
SentinelOne
◦
Instructor of Windows Internals classes
◦
Circus artist
◦
Former pastry chef
◦
Author of articles and tools at windows-internals.com
▫
CET internals, extension host hooking, I/O ring exploitation, kernel exploit mitigations, heap backed pool internals
◦
@yarden_shafir

State of Windows Exploitation
◦
New features and mitigations kill entire bug classes or exploitation techniques
▫
CET, CastGuard, KASAN…
◦
But…
▫
Some require new hardware
▫
Or require recompilation of software
▫
Many are disabled by default
◦
Code Integrity Policies limit unsigned software
◦
Win32k rewrite in rust could remove the biggest source of kernel vulnerabilities

Introducing CET
◦
CET creates a shadow stack that stores return addresses
▫
Attacker can’t modify the shadow stack without an additional vulnerability
◦
On every “ret” instruction, the return address is compared with the top address in the shadow stack
▫
Mismatch will generate INT21: Control Protection Fault
▫
Windows implements CET support for both user-mode and kernel-mode targets

Data
Data
Return Address 1
Data
Data
Data
Return Address 2
Data
Return Address 3
Return Address 1
Return Address 2
Return Address 3
Stack
Shadow Stack call ret
Jump to return address

Data
Data
Return Address 1
Data
Data
Data
Return Address 2
Data
Return Address 3
Return Address 1
Return Address 2
Return Address 3
Stack
Shadow Stack call ret
INT 21
Fake Address
Exploit

CET – the Windows Implementation
◦
Kernel doesn’t immediately crash the process on Control
Protection fault
▫
Processes where CET is disabled / in audit mode are exempt
▫
Return to modules compiled without CET is allowed
▫
Returning to any address in the shadow stack is allowed
◦
Additional logic to handle APCs, SetThreadContext, exceptions
◦
The kernel has CET too (KCET) implemented by VTL1
▫
Also allows returning to any address in the shadow stack

The Bypass
◦
Returning to any address in the shadow stack is allowed
▫
We can create a type confusion by returning to a valid address with a different register state
▫
More stack frames == More type confusion choices
The Bypass

s = FuncB(); s->Table[1]();
FuncA
FuncC(); s = new MyClass(); s.Table[1] = Foo; return s;
FuncB return 7;
FuncC
…
Foo
Normal Case

s = FuncB(); s->Table[1]();
FuncA
FuncC(); s = new MyClass(); s.Table[1] = Foo; return s;
FuncB
_retaddr = FuncA + 8; b = new BadClass(); b[0] = “AAAAAAAA”; b[1] = MaliciousFunc; b[2] = “BBBBBBBB”; return b;
FuncC
…
MaliciousFunc
The Bypass

Demo

Getting to the Kernel
◦
BYOVD! (Bring Your Own Vulnerable Driver)
◦
HVCI block list blocks some vulnerable drivers
▫
But many drivers are still allowed to load
▫
Loldrivers.io has over 600 vulnerable drivers – over 170 aren’t blocked by HVCI block list
▫
Some blocked drivers have new unblocked builds too that are sometimes still vulnerable
■
New version of dbutil_2_3.sys is identical – but now requires admin rights to trigger vulns

The Problem With EDRs
◦
Most EDRs use drivers to monitor the system and block/ kill processes detected as malicious
◦
Many EDR user-mode processes are hard to kill because they run as a Protected Process Light (PPL)
▫
Run with a special level protecting them from other processes
■
Yes, even admin processes
●
Well, sort of
▫
Only other protected processes can read/write/suspend/ terminate
▫
Requires an ELAM driver

How Can We Neutralize EDRs?
◦
HVCI has undocumented features that can be configured through the registry
▫
HKLM\System\CurrentControlSet\Control\CI
◦
HvciAuditMode (regular/full) allows receiving ETW messages for HVCI events without any blocking
▫
UMCIAuditMode is the same for user mode CI events
◦
HVCIDisallowedImages allows registering an array of driver names to be blocked by HVCI (requires reboot)
▫
Only blocks by driver file name on disk
▫
Great for blocking EDR drivers (except WdFilter.sys )

How Can We Disable a PPL?
◦
Common method is to terminate, suspend or close the handles of a PPL through a driver
▫
KProcessHacker.sys, ProcExp.sys
◦
Defender ATP installs a “KseSec” shim to hook APIs in drivers known to be used for PPL suspension/termination
▫
Hooks ZwTerminateProcess, PsSuspendProcess, NtClose, etc
▫
Also hooks drivers/functions that allow mapping physical memory
▫
Will block requests or log them to Microsoft-Windows-Sec
■
Depends on configuration received from user mode agent

MsSecFlt.sys and MsSecCore.sys
◦
MsSecFlt.sys – Microsoft Security Events Component file system filter driver
▫
Responsible for logging events to the Microsoft-Windows-Sec
ETW channel
▫
Provides security-related events to security tools
■
Process must be an AM PPL or above to subscribe
◦
MsSecCore.sys – Microsoft Security Core Boot Driver
▫
Recently added driver that works as an extension of
MsSecFlt.sys

MsSecCore.sys
MsSecFlt.sys
SecBindHost(..)
Function Table
SecRegisterKernelShimProvider(
SecKseShimInformation)
ntoskrnl
Register shims
Shimmed
Driver
ZwTerminateProcess
SecKseZwTerminateProcess
SecKseZwTerminateProcess
MsSense.exe
Send shim configuration over filter port
\MicrosoftSecFilterControlPort

MsSecCore.sys

MsSecFlt.sys

Time for Plan B
◦
MsMpEng.exe is a PPL – hard to suspend/terminate
▫
WdFilter.sys can terminate the process but only
MsMpEng.exe can send it commands
◦
WdFilter.sys has a “Panic Mode”
▫
Enabled when MsMpEng.exe times out on multiple file scans
▫
Opens a “back door” that allows any process to sent certain commands to the driver
▫
Sending a FSCTL with code 0x902EB will enter
MpFsCtlDispatcher: a private IOCTL interface
■
Allows setting internal flags, resetting cache and terminating
MsMpEng.exe

Windows Defender Backdoor FSCTL
◦
Timeout is determined by MpData->LocalTimeout
▫
Default is 4 minutes for local files and 6 for network files
▫
After 4 timeouts WdFilter.sys will go into panic mode
■
Also set in MpData together with the number of times it entered panic mode
■
FSCTL 0x902EB with code 9 will terminate MsMpEng.exe f = win32file.CreateFile("c:\\temp\\test.txt", win32file.GENERIC_READ, win32file.FILE_SHARE_READ, None, win32file.OPEN_EXISTING, 0)
win32file.DeviceIoControl(f, 0x902eb, b'\x09\x00\x00\x00',
None, None)

Demo

Hiding in the Kernel
◦
Drivers are visible to anyone who is looking
▫
And user<->kernel communication mechanisms are too
▫
Many kernel structures are protected or monitored so they can’t be hooked or tampered with anymore
◦
But we can live off the land in the kernel
▫
MsSecCore.sys shim functions call the registered functions in
MsSecFlt.sys – this interface isn’t protected
◦
Build private comms mechanism by hooking callback routines and invoking hooked APIs from the UM process to send messages to the driver

User Mode
Process
MsSecCore.sys
Shimmed
Driver
Rootkit.sys
Request process suspension
Call shim function
Call evaluation routine ntoskrnl
PsSuspendProcess

Summary
◦
Bypass CET by returning to a different address from the shadow stack
▫
Works against KCET too
◦
Reach the kernel through a vulnerable driver
▫
Even if HVCI block list is enabled
◦
Neutralize EDRs with HVCI features or built-in backdoors
▫
Or vulnerable drivers
◦
Live off the land in the kernel by hooking and abusing existing internal mechanisms

References
◦
Protected Processes:
▫ http://publications.alex- ionescu.com/NoSuchCon/NoSuchCon%202014%20-
%20Unreal%20Mode%20-%20Breaking%20Protected%20Processes.pdf
▫ https://googleprojectzero.blogspot.com/2018/10/injecting-code-into- windows-protected.html
▫ https://drive.google.com/file/d/1Pj7hSvsj0qvegdIUvABa9KUEKOrLzu2p/vi ew + https://github.com/gabriellandau/PPLFault
◦
Kernel Shim Engine:
▫ https://www.youtube.com/watch?v=qCa9icMqBNM

Questions?