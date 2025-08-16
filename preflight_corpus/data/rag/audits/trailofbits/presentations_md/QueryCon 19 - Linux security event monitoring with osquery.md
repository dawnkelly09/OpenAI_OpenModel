# Linux security event monitoring with osquery

QueryCon 2019

Alessandro Gario
Senior Security Engineer alessandro.gario@trailofbits.com www.trailofbits.com 2

Overview 1. Event-based tables on Linux 2. Audit 101 3. The next big thing 4. What’s eBPF 5. Journey from zero to process_events
Disclaimer: I like Spaceballs 3

State of the event-based tables

hardware_events, syslog_events
Awesome!
●Low memory usage
●Not many events to process
●Low CPU usage 5

ﬁle_events
Kind of annoying:
●Watchers have to be updated as events come in
●Relies on (globbing) existing ﬁles
●Prone to losing events
●No way to know if events were lost 6

How to break ﬁle_events
Example
$ cd /monitored
$ mkdir -p 1/2/3/4/5 && \ date > 1/2/3/4/5/hidden_file 7

How to make ﬁle_events lose changes 8 inotify
WE BRAKE FOR NOBODY

Audit tables
Interesting:
●Good insight on each event
●Can monitor most things
Not perfect:
●Uses a lot of memory
●Consumes a lot of CPU 9

Can we do better?
Data sources alone determine the fate of the table’s quality, not the actual code:
●How much memory is used?
●How much processing is required?
●Can events be trusted?
10

Audit 101

A system tracing utility
●Syscalls
●System events
Used by most event-based tables:
●process_events
●socket_events
●user_events
●selinux_events
●process_ﬁle_events
What is Audit?
12

NOTHING!
Teddy and I wrote it
If you don’t like it, you are
WRONG
What is wrong with Audit?
13

●Only one Audit consumer*
●Text-based
●Multiple records need to be a aggregated to create event context
●High memory footprint
●High CPU usage
What is actually wrong with Audit?
14

The next big thing

Finding the next big thing
What would we like?
●Event tracing
●Syscall tracing
●Context information for each event
●Binary data instead of text walls 16

I’ve heard about a thing called eBPF
AMAZING
●Tracepoints!
●More tracepoints! Kprobes! Uprobes!
●Not much context information!
●Binary data! Finally!
eBPF looks like a good candidate!
17

What’s eBPF

eBPF 101
A technology to load arbitrary programs and have them run when a speciﬁc event occurs:

●Tracepoints: manually deﬁned in the source, stable interface
●kprobes: basically code hooking
More data sources exist, but we are only interested in the ﬁrst two 19

eBPF 102
●eBPF programs are:
○compiled into bytecode
○Sandboxed
○Veriﬁed kernel-side upon load
Can be built:
●Manually, with raw BPF opcodes
●Ofﬁcial toolchain 20

BPF Compiler Collection (BCC)
21
A toolkit for creating and compiling eBPF programs:
●developed by  IOVisor,
●offers kernel instrumentation in C,
●has front-ends in Python and Lua,
●built on top of LLVM and Clang

Journey from zero to process_events

What’s inside process_events anyway?
23
Many ﬁelds, but let’s start with the following ones:
●pid
●path
●cmdline

Our initial implementation 24
#include <uapi/linux/ptrace.h>
#include <uapi/linux/limits.h> typedef struct { u32 pid; char filename[NAME_MAX]; // 256 bytes
} ExecveData;
BPF_PERF_OUTPUT(events); int sys_enter_execve(struct tracepoint__syscalls__sys_enter_execve *args)
{
  ExecveData execve_data = {}; execve_data.pid = (u32) (bpf_get_current_pid_tgid() >> 32);
  // We can't directly access user memory bpf_probe_read(&execve_data.filename, sizeof(execve_data.filename), args->filename); events.perf_submit(args, &execve_data, sizeof(ExecveData)); return 0;
};

Our initial implementation 25
#include <uapi/linux/ptrace.h>
#include <uapi/linux/limits.h> typedef struct { u32 pid; char filename[NAME_MAX]; // 256 bytes
} ExecveData;
BPF_PERF_OUTPUT(events); int sys_enter_execve(struct tracepoint__syscalls__sys_enter_execve *args)
{
  ExecveData execve_data = {}; execve_data.pid = (u32) (bpf_get_current_pid_tgid() >> 32);
  // We can't directly access user memory bpf_probe_read(&execve_data.filename, sizeof(execve_data.filename), args->filename); events.perf_submit(args, &execve_data, sizeof(ExecveData)); return 0;
};

Our initial implementation 26
#include <uapi/linux/ptrace.h>
#include <uapi/linux/limits.h> typedef struct { u32 pid; char filename[NAME_MAX]; // 256 bytes
} ExecveData;
BPF_PERF_OUTPUT(events); int sys_enter_execve(struct tracepoint__syscalls__sys_enter_execve *args)
{
  ExecveData execve_data = {}; // Declare a new struct on stack execve_data.pid = (u32) (bpf_get_current_pid_tgid() >> 32);
  // We can't directly access user memory bpf_probe_read(&execve_data.filename, sizeof(execve_data.filename), args->filename); events.perf_submit(args, &execve_data, sizeof(ExecveData)); return 0;
};

Our initial implementation 27
#include <uapi/linux/ptrace.h>
#include <uapi/linux/limits.h> typedef struct { u32 pid; char filename[NAME_MAX]; // 256 bytes
} ExecveData;
BPF_PERF_OUTPUT(events); int sys_enter_execve(struct tracepoint__syscalls__sys_enter_execve *args)
{
  ExecveData execve_data = {}; execve_data.pid = (u32) (bpf_get_current_pid_tgid() >> 32);
  // We can't directly access user memory bpf_probe_read(&execve_data.filename, sizeof(execve_data.filename), args->filename); events.perf_submit(args, &execve_data, sizeof(ExecveData)); return 0;
};

First challenge 28
The ﬁlename parameter is truncated at 256 bytes.
You COULD increase the array size, but here’s the thing: stack is limited to 512 bytes.
Can we do better?

First workaround: PER-CPU maps to the rescue!
29
BPF_PERCPU_ARRAY(temp_execve_data,
                 ExecveData, 1);
...
int index = 0;
// Make sure to check for NULL values!
ExecveData *execve_data_ptr = temp_execve_data.lookup(&index);

Second challenge: other parameters?
30
We only have the binary name!
What about program arguments?
Let’s take a look at two possible workarounds:
●Use a bigger map
●Create additional maps

Second workaround/a: Using bigger maps 31
Too much space across perf_events. Will make it easy to lose events.
typedef struct { u32 pid; char filename[512]; char param1[512]; char param2[512]; char param3[512];
  ...
} ExecveData;

Second workaround/b: Using additional maps
Step two: index map
Step one: data map
Step three: event object typedef struct { char bytes[2048];
} StringBuffer;
PER_CPU_ARRAY( string_data,
  StringBuffer, 1000
);
PER_CPU_ARRAY( string_data_index, int, 1
); typedef struct { u32 pid; char filename[512]; int parameters[20];
} ExecveData; 32

Challenge 3 33
We are still only getting N parameters!
String size is still limited!

Workaround 3 34
NONE :(
Additional eBPF limitations
●Jumps can only go forward
●Only 4096 instructions per program

Different approaches 35
●Dedicated tracepoints
●Deeper inspection with kprobes

Conclusions

●Audit is not that bad!
●eBPF is hard
●Using eBPF like we use Audit doesn’t work
●Teddy is a super hero
Conclusions 37