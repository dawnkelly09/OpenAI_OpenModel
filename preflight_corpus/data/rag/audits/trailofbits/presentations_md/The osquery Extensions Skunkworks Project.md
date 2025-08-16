# The osquery Extensions

Skunkworks Project
Unconventional Uses for Osquery
Mike Myers
Principal Security Engineer @ Trail of Bits

2 osquery extensions
Extensions are the way to develop custom functionality in a separate component that extends (via virtual tables) or overrides (via plugins)
the osquery core behavior.
Extensions compile and run as separate executables. They communicate with the osquery core process using the Thrift RPC protocol.

3
Terminology: Plugins vs. Extensions
Extensions
Plugins
●
User-overridable implementations of particular key features
●
Query configuration
(filesystem or TLS server)
●
Logging (filesystem, TLS, syslog or windows_event_log, kinesis, firehose, kafka)
●
An extension can implement a plugin
●
More commonly, it implements custom
(sometimes proprietary)
virtual tables

4 osquery extensions extension2.ext osqueryd
(osquery core)
UNIX domain socket socket extension1.ext socket
Thrift Protocol
Plugin a
Plugin c
Plugin b osqueryi --extension /path/to/extension1.ext --extension /path/to/extension2.ext osqueryd --extension_autoload /path/to/list_of_all_extensions.txt.load
OR cat --disable_extensions=false > /etc/osquery/osquery.flags
THEN

5
Building an osquery extension (C++)
1.
Statically link the core code 2.
#include <osquery/sdk.h> 3.
Inherit from TablePlugin and implement appropriate methods 4.
Register the table or plugin 5.
Initialize osquery worker threads 6.
startExtension() to connect to osquery core 7.
Symlink your build directory into osquery’s 8.
make externals

6
Building an osquery extension (Python)
https://github.com/osquery/osquery-python 1.
> pip install osquery 2.
import osquery 3.
@osquery.register_plugin 4.
class MyTablePlugin(osquery.TablePlugin)
5.
def name(), def columns(), def generate()
6.
osquery.start_extension(name="my_ex", version="1.0.0")
osqueryi --extension path_to_my_table_plugin.py

7
Building an osquery extension (Go)
https://github.com/kolide/osquery-go 1.
install the Kolide library in your GOPATH 2.
import("github.com/kolide/osquery-go")
3.
server := osquery.NewExtensionManagerServer()
4.
server.RegisterPlugin(table.NewPlugin(
"foobar", FoobarColumns(), FoobarGenerate))
5.
define the foobar methods to return stuff.
go build -o my_table_plugin my_table_plugin.go osqueryi --extension /path/to/my_table_plugin

osquery extensions enable new horizons

9
Why create extensions?
osquery extensions allow you to:
●try “dangerous” features
●...without the risk of crashing osquery
(worker/watchdogs)
●develop with autonomy, outside of core
●...without maintaining your own fork
●protect secret-sauce ideas

10
What is not allowed in osquery core?
1. Don't pry into users’ data 2. Don't create network traffic to third parties 3. Don't change the state of the system 4. Don’t use undocumented APIs or private interfaces 5. Don’t use external dependencies 6. Do not fork a new process

Audience exercise: write down an osquery feature idea that would never be accepted in “core”

12
Trail of Bits’ extensions repository https://github.com/trailofbits/osquery-extensions
Skunkworks Project: any small group working on radical ideas outside of standard procedures & constraints.
Contributing engineers at Trail of Bits:
-
Alessandro Gario
-
Garret Reece

13
Remotely query NTFS metadata
●
Metadata valuable in incident response
○
Additional timestamp entries, file security descriptors, whether a file has Alternate Data
Streams (ADS).
●
NTFS filesystem forensics
○
Index entries for directory indices, including entries that are deallocated
●
Accelerated response
○
Remote investigations with the free osquery that you’ve already deployed
Extension highlight: NTFS forensics

14
Track and manage application whitelisting on macOS
●
See applications that tried to run
○
See how Santa enforces its whitelist or blacklist of allowed executions.
●
Illustrates writeable tables PR #4094
○
Not only reads Santa events log, but can also update Santa rules.
●
No longer need separate server
○
Reduced operating overhead. Single interface: osquery.
Extension highlight: manage Santa whitelist

15
Simple, cross-platform interface to endpoints’ host-based firewalls
●
Block hosts or check blocked hosts
○
Turns /etc/hosts into a virtual table.
○
Again, illustrates PR #4094
●
Block ports or check blocked ports
○
These common firewall management tasks are now simple SQL syntax.
Extension highlight: manage the OS firewall
●
Single interface across macOS / Linux / Windows
○
Accelerate incident response
○
Ensure policy compliance

16
Windows objects: mutants, semaphores, and ‘events’
●
Useful in incident response
○
Malware infection markers
●
Vaccination via mutant squatting
○
Threat intelligence → vaccinate
Extension highlight: synchronization objects
●
Edge browser tabs
○
Edge browser creates named mutants for every cross-site domain you’re currently browsing (find XSS and iFrames)

17
Improving extension performance
●PR #4335 (tagged 3.3.0)
●Extension must call new add_osquery_extension_ex() function
●Reduced overhead from Thrift
●Fewer processes running
●Will enable bundling extensions with, e.g., Kolide
Launcher

18
Who else is creating extensions?
Organization
Extension functionality
Availability
Facebook tables that implement proprietary detection strategies
Proprietary
Kolide adds Go language support bridge for the osquery SDK; others bundled with Launcher
Open-source
PolyLogyx traditional and event-driven tables; includes a kernel driver
Closed-source but free
SpellSecurity
Labs traditional and event-driven tables; includes a kernel driver. Also implements an osquery software update mechanism.
Commercial
Trail of Bits new category of management-capable tables; integration with other open-source endpoint security tools and libraries
Open-source

19
Attack detection and response timelines
Security
Orchestration
Manage rules
& settings
Control Santa, firewall, etc.

OS instrumentation osquery core
SELECT *
FROM settings

Monitoring
Event-driven
Auditing, eventing, maybe eBPF
(tracing)

Forensics
Leverage 3rd party code
Memory capture/ forensics, filesystem metadata

“
”
Q&A

Challenges & Opportunities

22
Extension limitations & caveats
Thrift overhead
Lack of pub/sub
No integration with event pub/sub in osquery core.
This means a lack of the cache (backing store)
provided by RocksDB, and no support for certain CLI controls. Your extension must implement its own database (easy in Go, not as easy in C++). Also, no expiry
(event expiration).
If transferring a large quantity of table data, the
Thrift serialization/ deserialization causes performance degradation
(poor event-driven table performance in extensions).
You can mitigate this by throttling events.
No result streaming
Extensions don't have a keepalive mechanism while busy generating table data, so osquery core is prone to complaining about timeouts on queries of tables implemented in extensions.
Annoyance, not a stopper?

23
Stretching the SQL table metaphor
Inherent Challenges:
●Translating complex rule data to tabular format
●Cannot always flatten hierarchical data
●Mutant table: each object has different properties
Writable Tables Challenges:
●Translating back from SQL format to update rule-driven configuration files
●Synchronizing state (no reusing row IDs)

24
Call to action
Make a pull request
Develop your idea
Do you have an idea for an osquery extension? File an issue on our GitHub repo for it. Or, develop it yourself using the osquery SDK.
Get our feedback on your extension. If we think it’s great and you want it featured, we can add it to our growing repo of extensions.
You can hire us
Contact us to discuss an estimate for implementing your idea. We work in the open, engage with the community, and stay in regular contact with our customers.

25
Contact Us
Dan Guido
CEO dan@trailofbits.com 516.359.3208
Mike Myers
Principal Security Engineer mike.myers@trailofbits.com 708.374.7853 on Signal