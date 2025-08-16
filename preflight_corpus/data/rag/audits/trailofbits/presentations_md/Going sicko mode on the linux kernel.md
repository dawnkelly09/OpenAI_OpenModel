# Going sicko mode on the linux kernel

Empire Hacking 2/12/19
William Woodruff

●
○
○
■
■
○
■
■
■ 2
Hi

Faults
●
●
● read() write()
malloc()
●
●
● errno
GetLastError 3

int main(void) { chdir(getenv(“TMPDIR”)); int fd = open(“hello”, O_WRONLY); write(fd, “hello tmpdir\n”, 13); lseek(fd, 6, SEEK_SET);
  do_more(fd); return 0;
} 4
How many potential faults?
●
Each of these calls can fail!
●
If just one fails, each after is likely to fail
(or do the wrong thing):
○ chdir() fails: open() either fails or creates the file in the wrong place
○ write() fails: lseek() now has an invalid offset (fd unchanged)
Faults are not limited to elementary calls like these!
???

Faults as a vulnerability class?
●
●
●
●
● 5

Faults as a vulnerability class?
{ char *buf = malloc(4096); // sprayed buffer read(fd, buf, 4095);      // EFOOBAR, buf unmodified
  // ...
  yaml_parse(buf);          // arbitrary deserialization
} 6

●
○
●
○
○
LD_PRELOAD
○
■
Fault injection 7

First approach: linkage fiddling 8
A contrived* dynamic linkage scenario

First approach: linkage fiddling 9
A contrived* dynamic linkage scenario, with LD_PRELOAD

●
●
●
●
●
●
Fault injection for software resiliency 10

●
○
●
○
○
●
Fault injection for software resiliency 11

●
●
●
●
●
● read()
● malloc()
Fault injection for vulnerability research 12

●
○
■
●
○
○
■
■
■
○
Practical fault exploitation 13

●
LD_PRELOAD
○
LD_PRELOAD
○ read()
write()
LD_PRELOAD
■ open(3)
openat(2) fork(3)
vfork(3)
clone(2)
■ syscall(SYS_read, …)
○
LD_PRELOAD
LD_PRELOAD
__attribute__((constructor))
●
○
Exploitation blockers 14

●
○
■
○ int 80h syscall
■
○ ptrace(2)
■
SECCOMP_RET_TRACE
■
○
Reliable syscall faulting 15

●
○
■ bpf_probe_write_user
■
SECCOMP_RET_ERRNO
■
○
■
■
●
Reliable syscall faulting 16

● sys_call_table
__NR_<syscall>
○ errno
●
○
●
○ memcpy()
Futzing with the syscall table 17

asmlinkage long wrap_sys_read(...) { return (some_check() ? sys_read(...) : -EFAULT);
} module_init() { sys_call_table = kallsyms_lookup_name(“sys_call_table”); sys_call_table[__NR_read] = (void*)&wrap_sys_read;
}
Futzing with the syscall table 18

Syscall targeting options
●
○ current_uid() current_gid()
○
○
● personality(2)
○
■
PER_BSD PER_SUNOS PER_XENIX
○ personality(2)
exec
● 19

Tying it all together
●
○
○
○ krfexec krfctl 20

KRF’s wrapping/interception mechanism 21

krfexec and krfctl
● personality(2)
○ krfexec curl http://example.com
●
○
■ sudo krfctl -F read,write,open,close # fault just these 4 syscalls
■ sudo krfctl -P net                   # fault all networking syscalls
■ sudo krfctl -c                       # clear all faulty syscalls
○
■ sudo krfctl -p 100      # 1/100 calls on average will fail
■ sudo krfctl -r 0        # set the RNG state to 0 22

24 24

Demo

References/Links
LD_PRELOAD is super fun. And easy!
26
Kernel tracing with eBPF
Intercepting and Emulating Linux System Calls with Ptrace
How to write a rootkit without really trying
SECure COMPuting with filters

References/Links
KRF 27
Hooking the Linux System Call Table
Linux on-the-fly kernel patching without LKM

Contact
William Woodruff
Security Engineer william@trailofbits.com www.trailofbits.com 28