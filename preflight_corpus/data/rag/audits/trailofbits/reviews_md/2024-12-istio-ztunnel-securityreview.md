# Istio Ztunnel

Security Assessment Summary
March 5, 2025

Prepared for:​
The Istio Project​
Organized by the Open Source Technology Improvement Fund (OSTIF)

Prepared by: Vasco Franco and Sam Alws

Table of Contents
Table of Contents​ 1
Project Summary​ 2
Executive Summary​ 4
Detailed Findings​ 6 1. No automated process for updating vulnerable dependencies​ 6 2. Some code paths that trigger error conditions are not covered by tests​ 7 3. HTTP forwarded header parser not fuzz tested​ 8
A. Vulnerability Categories​ 8
B. cargo audit Output​ 11
C. Integrating Semgrep in CI​ 14
D. Why and How to Use Dylint​ 15
E. Cargo Mutants Report​ 16
F. Fix Review Results​ 28
Detailed Fix Review Results​ 29
G. Fix Review Status Categories​ 30
About Trail of Bits​ 31
Notices and Remarks​ 32

​
        Trail of Bits​ 1​
Istio Ztunnel​
        PUBLIC​
​

Project Summary
Contact Information
The following project manager was associated with this project:
Jeff Braswell, Project Manager jeff.braswell@trailofbits.com
The following engineering director was associated with this project:
Keith Hoodlet, Engineering Director, Application Security keith.hoodlet@trailofbits.com
The following consultants were associated with this project:
​
Vasco Franco, Consultant​ ​
Sam Alws, Consultant
​ vasco.franco@trailofbits.com​ sam.alws@trailofbits.com
Project Timeline
The significant events and milestones of the project are listed below.
Date​
Event
December 9, 2024​
Pre-project kickoff call
December 18, 2024​
Delivery of report draft and report readout
March 5, 2025 ​
Delivery of final summary report

​
        Trail of Bits​ 2​
Istio Ztunnel​
        PUBLIC​
​

Project Targets
The engagement involved a review and testing of the following target.
Ztunnel
Repository ​ https://github.com/istio/ztunnel
Version ​ 029513a4610db851b9544ed423c9965192ef4caa
Type ​
Proxy
Platform ​
Linux

​
        Trail of Bits​ 3​
Istio Ztunnel​
        PUBLIC​
​

Executive Summary
Engagement Overview
OSTIF hired Trail of Bits to review the security of Ztunnel, the node proxy implementation of Istio’s ambient mesh mode, an alternative to the sidecar model. Ztunnel is developed in
Rust, with a narrow and well-defined feature set, and a focus on high performance.
A team of two consultants conducted the review from December 9 to December 13, 2024, for a total of two engineer-weeks of effort. With full access to source code and documentation, we performed static and dynamic testing of Istio Ztunnel using automated and manual processes.
The audit uncovered no significant flaws or defects that could impact system confidentiality or integrity.
Observations and Impact
Compared to the sidecar model, which uses Envoy proxies, Ztunnel reduces the attack surface by having a minimal set of features that rely only on data from the transport layer
(L4), eliminating the need to terminate and parse a user’s HTTP request (L7). Additionally,
Ztunnel is developed in Rust, minimizing the risk of memory corruption issues.
Our best-effort review focused on a manual review of Ztunnel’s most critical code paths, including L4 authorization, inbound request proxying (excluding raw socket code), transport-layer security (TLS), and certificate management code. Additionally, we performed static analysis of the whole repository using Semgrep, Dylint, and Clippy
Pedantic, evaluated Ztunnel’s test quality and coverage, and reviewed the project’s dependency management process. We did not review the code on the Istio repository that interacts with Ztunnel.
We found that the Ztunnel codebase is well-written and structured: the code responsible for different application parts is divided into discrete files and folders, the unsafe tag is used only when necessary, and cryptographic and parsing code is delegated to libraries.
Regarding dependencies, we found that Ztunnel depends on unmaintained dependencies, such as derivative, and others controlled by single developers, which increases the risk of supply-chain attacks. We also found that Ztunnel lacked an automated process for updating vulnerable dependencies (TOB-ZTN-1). Regarding testing, we found that Ztunnel’s tests do not cover some “unhappy paths”—paths that trigger error conditions (TOB-ZTN-2).
​
        Trail of Bits​ 4​
Istio Ztunnel​
        PUBLIC​
​

Recommendation Summary
We recommend that the Ztunnel team improve automated processes in Ztunnel’s CI/CD pipeline:
●​ Add an automated process for updating outdated and vulnerable dependencies.
See TOB-ZTN-1 for more details.
●​ Add additional fuzz tests to the project’s CI/CD pipeline to periodically re-fuzz functions that process untrusted input. See TOB-ZTN-3 for more details.
●​ Consider adding cargo-mutants and necessist to the CI/CD pipeline to identify broken tests and tests where additional or more precise assertions are needed. See
TOB-ZTN-2 for more details.
●​ Ztunnel already uses Clippy to identify security and coding issues in new code.
Consider adding Semgrep and Dylint to the project’s CI/CD pipeline.
○​ Semgrep is a multi-language security scanner with 57 Rust rules and many rules for other languages that may be present in Ztunnel (e.g., Dockerfiles).
See appendix C for a guide on integrating it into Ztunnel’s CI.
○​ Dylint is a Rust linter similar to Clippy with its own lints, such as try_io_result and unnecessary_conversion_for_trait. It also allows developers to create lint rules specific to their project or organization's needs. A simple example of using Dylint would be creating a custom lint to enforce specific naming conventions or to catch common anti-patterns in the codebase. The lints are written in Rust, and both the syntax and semantics of Rust code can be analyzed. See appendix D for more information on Dylint and a guide on integrating it into Ztunnel’s CI.

​
        Trail of Bits​ 5​
Istio Ztunnel​
        PUBLIC​
​

Detailed Findings 1. No automated process for updating vulnerable dependencies
Severity: Medium
Difficulty: Medium
Type: Patching
Finding ID: TOB-ZTN-1
Target: Cargo.toml
Description
Ztunnel has no automated process for updating dependencies; maintainers manually create pull requests to periodically bump Rust dependency versions defined in the
Cargo.toml configuration file. For this reason, Ztunnel depends on outdated, unmaintained, and vulnerable dependencies. The cargo audit command currently reports three unique vulnerabilities and three warnings relating to Ztunnel’s dependencies, as shown in appendix B. We did not fully investigate these findings to determine if they are reachable from Ztunnel.
Recommendations
Short term, update Ztunnel’s vulnerable dependencies, and attempt to replace the unmaintained derivative and instant crates with equivalents that are actively maintained.
Long term, create a system to automatically open pull requests that update dependencies with known vulnerabilities. This could be done by adding this functionality to the istio-testing bot or by using GitHub’s Dependabot.

​
        Trail of Bits​ 6​
Istio Ztunnel​
        PUBLIC​
​

2. Some code paths that trigger error conditions are not covered by tests
Severity: Informational
Difficulty: High
Type: Testing
Finding ID: TOB-ZTN-2
Target: Testing Suite
Description
Our review of Ztunnel’s test coverage revealed that while most functionality is well-tested, some error-handling code paths—known as “unhappy paths”—are not covered by tests; this can mean bugs in error handling code may not be automatically detected. This was determined by manually reviewing a coverage report of Ztunnel’s current tests.
We also used cargo-mutants, a mutation testing tool, to identify weaknesses in Ztunnel’s test suite. This tool systematically introduces small but meaningful changes to the source code—such as replacing equality operators (==) with inequality operators (!=)—and observes whether the test suite detects these mutations. When tests pass despite these introduced changes, it reveals gaps in the test assertions. Even if a piece of code is executed by tests, without proper assertions, bugs in that code could go undetected. Cargo mutants generated 1841 mutants and found that the test suite missed 418. The full results can be found in appendix E.
Additionally, we used necessist, a test harness mutation tool that helps to identify broken tests by removing statements and method calls from tests. If a test passes with a statement or method call removed, it could indicate a problem in the test, or worse, a problem in the tested code. We found no broken tests with necessist.
Exploit Scenario
An attacker finds an instance of incorrect error handling in the Ztunnel codebase and uses this to remotely trigger a panic.
Recommendations
Short term, write “unhappy path” tests, which test that Ztunnel handles errors correctly.
Use test coverage reports to find which lines of error handling need to be tested.
Long term, use cargo-mutants and necessist periodically to highlight broken tests and tests where additional or more precise assertions are needed.

​
        Trail of Bits​ 7​
Istio Ztunnel​
        PUBLIC​
​

3. HTTP forwarded header parser not fuzz tested
Severity: Informational
Difficulty: High
Type: Testing
Finding ID: TOB-ZTN-3
Target: http_types::proxies::Forwarded::parse
Description
The http_types::proxies::Forwarded::parse function parses input from inbound
HBONE requests, but is not fuzz-tested. This function is implemented in the third-party http_types library and is called in src/proxy/inbound.rs in the parse_forwarded_host function. We are not aware of any fuzzing campaign targeting it.
Parsers are excellent targets for fuzzing since they are typically error-prone and easy to provide random inputs to.
Exploit Scenario
Ongoing development introduces a subtle flaw in the parser that can only be triggered in unexpected conditions but does not affect the functionality expected by unit tests. An attacker finds and exploits the bug in the parse_forwarded_host function to make
Ztunnel panic.
Recommendations
Short term, add a fuzzing harness for the http_types::proxies::Forwarded::parse function to the existing OSS-Fuzz tests.
Long term, create a testing policy that requires fuzz testing for all header parsing code.
Document this requirement in contribution guidelines and code review checklists, covering both first-party and third-party parsing components. Make fuzz test coverage a gate for production deployment in CI/CD. Additionally, establish an inventory for header parsing components and their testing coverage. Set up an automated process to identify parsing code that lacks coverage, including changes to existing parsing-related code. As the codebase grows, consider developing reusable, well-tested parsing primitives to ensure consistent security coverage across all header parsing operations.
References
●​ The rustls GitHub Action workflow that runs fuzz tests
●​ Trail of Bits Testing Handbook: cargo-fuzz walkthrough
​
        Trail of Bits​ 8​
Istio Ztunnel​
        PUBLIC​
​

A. Vulnerability Categories
The following tables describe the vulnerability categories, severity levels, and difficulty levels used in this document.
Vulnerability Categories
Category
Description
Access Controls
Insufficient authorization or assessment of rights
Auditing and Logging
Insufficient auditing of actions or logging of problems
Authentication
Improper identification of users
Configuration
Misconfigured servers, devices, or software components
Cryptography
A breach of system confidentiality or integrity
Data Exposure
Exposure of sensitive information
Data Validation
Improper reliance on the structure or values of data
Denial of Service
A system failure with an availability impact
Error Reporting
Insecure or insufficient reporting of error conditions
Patching
Use of an outdated software package or library
Session Management
Improper identification of authenticated users
Testing
Insufficient test methodology or test coverage
Timing
Race conditions or other order-of-operations flaws
Undefined Behavior
Undefined behavior triggered within the system

​
        Trail of Bits​ 9​
Istio Ztunnel​
        PUBLIC​
​

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
User information is at risk; exploitation could pose reputational, legal, or moderate financial risks.
High
The flaw could affect numerous users and have serious reputational, legal, or financial implications.

Difficulty Levels
Difficulty
Description
Undetermined
The difficulty of exploitation was not determined during this engagement.
Low
The flaw is well known; public tools for its exploitation exist or can be scripted.
Medium
An attacker must write an exploit or will need in-depth knowledge of the system.
High
An attacker must have privileged access to the system, may need to know complex technical details, or must discover other weaknesses to exploit this issue.

​
        Trail of Bits​ 10​
Istio Ztunnel​
        PUBLIC​
​

B. cargo audit Output
This appendix shows the output of the cargo audit command when run on the Ztunnel repository; see TOB-ZTN-1.
Crate:     hashbrown
Version:   0.15.0
Title:     Borsh serialization of HashMap is non-canonical
Date:      2024-10-11
ID:        RUSTSEC-2024-0402
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0402
Solution:  Upgrade to >=0.15.1
Dependency tree:
hashbrown 0.15.0
├── lru 0.12.5
│   └── pingora-pool 0.1.1
│       └── ztunnel 0.0.0
│           └── ztunnel 0.0.0
└── indexmap 2.6.0
    ├── serde_yaml 0.9.34+deprecated
    │   └── ztunnel 0.0.0
    ├── petgraph 0.6.5
    │   └── prost-build 0.13.3
    │       ├── ztunnel 0.0.0
    │       └── tonic-build 0.12.3
    │           └── ztunnel 0.0.0
    ├── keyed_priority_queue 0.4.2
    │   └── ztunnel 0.0.0
    └── h2 0.4.6
        ├── ztunnel 0.0.0
        └── hyper 1.4.1
            ├── ztunnel 0.0.0
            ├── hyper-util 0.1.9
            │   ├── ztunnel 0.0.0
            │   └── hyper-rustls 0.27.3
            │       └── ztunnel 0.0.0
            └── hyper-rustls 0.27.3

Crate:     idna
Version:   0.4.0
Title:     `idna` accepts Punycode labels that do not produce any non-ASCII when decoded
Date:      2024-12-09
ID:        RUSTSEC-2024-0421
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0421
Solution:  Upgrade to >=1.0.0
Dependency tree:
idna 0.4.0
└── hickory-proto 0.24.1
    ├── ztunnel 0.0.0
​
        Trail of Bits​ 11​
Istio Ztunnel​
        PUBLIC​
​

    │   └── ztunnel 0.0.0
    ├── hickory-server 0.24.1
    │   └── ztunnel 0.0.0
    ├── hickory-resolver 0.24.1
    │   ├── ztunnel 0.0.0
    │   └── hickory-server 0.24.1
    └── hickory-client 0.24.1
        └── ztunnel 0.0.0

Crate:     idna
Version:   0.5.0
Title:     `idna` accepts Punycode labels that do not produce any non-ASCII when decoded
Date:      2024-12-09
ID:        RUSTSEC-2024-0421
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0421
Solution:  Upgrade to >=1.0.0
Dependency tree:
idna 0.5.0
└── url 2.5.2
    ├── ztunnel 0.0.0
    │   └── ztunnel 0.0.0
    ├── http-types 2.12.0
    │   └── ztunnel 0.0.0
    └── hickory-proto 0.24.1
        ├── ztunnel 0.0.0
        ├── hickory-server 0.24.1
        │   └── ztunnel 0.0.0
        ├── hickory-resolver 0.24.1
        │   ├── ztunnel 0.0.0
        │   └── hickory-server 0.24.1
        └── hickory-client 0.24.1
            └── ztunnel 0.0.0

Crate:     rustls
Version:   0.23.14
Title:     rustls network-reachable panic in `Acceptor::accept`
Date:      2024-11-22
ID:        RUSTSEC-2024-0399
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0399
Solution:  Upgrade to >=0.23.18
Dependency tree:
rustls 0.23.14
├── ztunnel 0.0.0
│   └── ztunnel 0.0.0
├── tokio-rustls 0.26.0
│   ├── ztunnel 0.0.0
│   └── hyper-rustls 0.27.3
│       └── ztunnel 0.0.0
├── hyper-rustls 0.27.3
└── boring-rustls-provider 0.0.1
​
        Trail of Bits​ 12​
Istio Ztunnel​
        PUBLIC​
​

    └── ztunnel 0.0.0

Crate:     derivative
Version:   2.2.0
Warning:   unmaintained
Title:     `derivative` is unmaintained; consider using an alternative
Date:      2024-06-26
ID:        RUSTSEC-2024-0388
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0388
Dependency tree:
derivative 2.2.0
└── ztunnel 0.0.0
    └── ztunnel 0.0.0

Crate:     instant
Version:   0.1.13
Warning:   unmaintained
Title:     `instant` is unmaintained
Date:      2024-09-01
ID:        RUSTSEC-2024-0384
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0384
Dependency tree:
instant 0.1.13
├── fastrand 1.9.0
│   └── futures-lite 1.13.0
│       └── http-types 2.12.0
│           └── ztunnel 0.0.0
│               └── ztunnel 0.0.0
└── backoff 0.4.0
    └── ztunnel 0.0.0

Crate:     pprof
Version:   0.13.0
Warning:   unsound
Title:     Unsound usages of `std::slice::from_raw_parts`
Date:      2024-12-04
ID:        RUSTSEC-2024-0408
URL:       https://rustsec.org/advisories/RUSTSEC-2024-0408
Dependency tree:
pprof 0.13.0
└── ztunnel 0.0.0
    └── ztunnel 0.0.0

error: 4 vulnerabilities found!
warning: 3 allowed warnings found
Figure B.1: The cargo audit command output

​
        Trail of Bits​ 13​
Istio Ztunnel​
        PUBLIC​
​

C. Integrating Semgrep in CI
To integrate Semgrep in Ztunnel’s CI, we recommend using the following approach:
1.​ Schedule a full Semgrep scan on the main branch with a broad set of Semgrep rules
(e.g., p/default).
2.​ Implement a diff-aware scanning approach for pull requests, using a fine-tuned set of rules that yield high confidence and true positive results.
3.​ Once the project’s Semgrep implementation is mature, configure Semgrep to block the PR pipeline if there are unresolved Semgrep findings.
Read the Trail of Bits Testing Handbook section on Semgrep in CI for a complete guide.

​
        Trail of Bits​ 14​
Istio Ztunnel​
        PUBLIC​
​

D. Why and How to Use Dylint
Dylint extends Rust's linting capabilities beyond what's available in Clippy, offering two key advantages:
●​ Extended customization: Teams can create project-specific lint rules to enforce organization-specific coding standards and architectural decisions. This is particularly valuable for implementing custom checks that involve third-party crates or project-specific requirements.
●​ Specialized error detection: By interfacing with rustc’s internal APIs, Dylint can implement complex, context-aware checks that detect subtle bugs and anti-patterns specific to a codebase. This is especially useful for cases where standard lints could produce too many false positives or fail to capture nuanced violations.
These features make Dylint particularly suitable for projects requiring specialized static analysis rules or those dealing with complex, project-specific requirements that standard
Rust lints do not cover.
Dylint can be installed by running the command cargo install cargo-dylint dylint-link. To run it, we added the following content to the project’s Cargo.toml file and then ran the command cargo dylint --all --workspace.
[[workspace.metadata.dylint.libraries]]
git = "https://github.com/trailofbits/dylint" pattern = [
    "examples/general/*",
    "examples/supplementary/*",
]
Figure D.1: Metadata required to run Dylint

​
        Trail of Bits​ 15​
Istio Ztunnel​
        PUBLIC​
​

E. Cargo Mutants Report
This appendix shows the output of the cargo mutants command when run on the
Ztunnel repository; see TOB-ZTN-2.
MISSED   src/state/service.rs:103:9: replace EndpointSet::contains -> bool with true in 21.8s build + 3.3s test
MISSED   src/app.rs:317:5: replace init_inpod_proxy_mgr -> anyhow::Result<std::pin::Pin<Box<dyn std::future::Future<Output =()>+Send +Sync>>> with Ok(Pin::new(Box::new(Default::default()))) in 17.7s build
+ 3.0s test
MISSED   src/test_helpers/tcp.rs:190:59: replace >= with < in handle_stream in 24.6s build + 3.3s test
MISSED   src/proxy/pool.rs:553:9: replace <impl Display for WorkloadKey>::fmt -> fmt::Result with
Ok(Default::default()) in 26.9s build + 3.1s test
MISSED   src/metrics.rs:119:9: replace DefaultedUnknown<T>::inner -> Option<T> with None in 30.0s build + 2.9s test
MISSED   src/inpod/workloadmanager.rs:115:92: replace * with / in WorkloadProxyNetworkHandler::connect in 18.0s build + 3.0s test
MISSED   src/test_helpers.rs:68:5: replace can_run_privilged_test -> bool with false in 49.5s build + 2.9s test
MISSED   src/state/policy.rs:103:9: replace PolicyStore::clear_all_policies with () in 22.8s build + 2.8s test
MISSED   src/test_helpers/tcp.rs:74:29: replace += with *= in run_client in 15.4s build + 2.9s test
MISSED   src/config.rs:547:30: replace - with / in construct_config in 48.1s build + 2.8s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from_iter([Full::new()])) in 30.0s build + 3.7s test
TIMEOUT  src/copy.rs:109:9: replace <impl AsyncWriteBuf for WriteAdapter<T>>::poll_write_buf ->
Poll<std::io::Result<usize>> with Poll::from(Ok(1)) in 36.0s build + 20.0s test
MISSED   src/inpod/admin.rs:146:9: replace <impl AdminHandler for WorkloadManagerAdminHandler>::handle -> anyhow::Result<serde_json::Value> with Ok(Default::default()) in 25.1s build + 2.8s test
MISSED   src/proxy/outbound.rs:434:5: replace baggage -> String with String::new() in 23.9s build + 2.8s test
MISSED   src/copy.rs:364:9: replace <impl ResizeBufRead for BufReader<R>>::resize with () in 23.0s build + 2.7s test
TIMEOUT  src/state.rs:124:19: replace == with != in WorkloadInfo::matches in 21.0s build + 20.0s test
MISSED   src/test_helpers/tcp.rs:60:23: replace < with == in run_client in 20.5s build + 2.8s test
MISSED   src/inpod/statemanager.rs:201:9: replace WorkloadProxyManagerState::reconcile with () in 28.4s build + 2.7s test
MISSED   src/test_helpers/app.rs:127:9: replace TestApp::admin_request_body -> anyhow::Result<Bytes> with
Ok(Default::default()) in 27.6s build + 2.8s test
MISSED   src/state/workload.rs:560:17: replace <impl Deserialize for NetworkAddress>::deserialize::<impl
Visitor for NetworkAddressVisitor>::expecting -> fmt::Result with Ok(Default::default()) in 18.1s build + 2.9s test
MISSED   src/proxy.rs:599:5: replace get_original_src_from_stream -> Option<IpAddr> with None in 23.1s build
+ 2.8s test
MISSED   src/test_helpers/tcp.rs:65:29: replace += with *= in run_client in 26.5s build + 3.0s test
MISSED   src/inpod/workloadmanager.rs:135:9: replace WorkloadProxyManager::verify_syscalls -> anyhow::Result<()> with Ok(()) in 26.8s build + 3.0s test
MISSED   src/rbac.rs:395:9: replace <impl From for Option<StringMatch>>::from -> Self with
Default::default() in 27.7s build + 3.3s test
MISSED   src/xds/client.rs:78:9: replace <impl Display for RejectedConfig>::fmt -> fmt::Result with
Ok(Default::default()) in 53.5s build + 3.2s test
MISSED   src/copy.rs:391:9: replace <impl AsyncWrite for BufReader<R>>::poll_write_vectored ->
Poll<io::Result<usize>> with Poll::from(Ok(1)) in 15.2s build + 3.2s test
TIMEOUT  src/tls/certificate.rs:325:5: replace der_to_pem -> String with String::new() in 30.4s build + 20.0s test
MISSED   src/test_helpers/netns.rs:255:41: replace + with * in NamespaceManager::child in 32.8s build + 2.7s test
MISSED   src/inpod/packet.rs:39:50: replace - with / in bind in 16.3s build + 2.8s test
MISSED   src/inpod/admin.rs:142:9: replace <impl AdminHandler for WorkloadManagerAdminHandler>::key ->
&'static str with "" in 18.9s build + 2.7s test
MISSED   src/cert_fetcher.rs:113:9: replace <impl CertFetcher for CertFetcherImpl>::clear_cert with () in 45.3s build + 2.7s test
MISSED   src/copy.rs:88:9: replace <impl AsyncWriteBuf for &mut T>::poll_write_buf ->
Poll<std::io::Result<usize>> with Poll::from(Ok(1)) in 41.5s build + 2.8s test
MISSED   src/test_helpers.rs:401:41: replace > with < in check_eventually in 17.8s build + 2.7s test
​
        Trail of Bits​ 16​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/proxy/pool.rs:332:9: replace <impl Drop for PoolState>::drop with () in 45.5s build + 2.8s test
MISSED   src/identity/manager.rs:106:9: replace Identity::from_parts -> Identity with Default::default() in 33.2s build + 3.1s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from(Full::from_iter([Default::default()]))) in 26.0s build + 4.5s test
MISSED   src/xds/client.rs:550:56: replace * with / in AdsClient::run_loop in 26.2s build + 2.9s test
MISSED   src/xds.rs:378:55: replace += with *= in <impl Handler for ProxyStateUpdater>::handle in 25.9s build + 2.9s test
MISSED   src/telemetry.rs:431:9: replace testing::assert_contains with () in 25.6s build + 2.9s test
TIMEOUT  src/tls/certificate.rs:299:48: replace + with - in WorkloadCertificate::refresh_at in 24.4s build + 20.0s test
MISSED   src/telemetry.rs:279:9: replace <impl Visit for JsonVisitory<S>>::record_bool with () in 25.7s build + 2.9s test
MISSED   src/admin.rs:239:5: replace handle_pprof -> anyhow::Result<Response<Full<Bytes>>> with
Ok(Response::new(Full::new(Default::default()))) in 42.1s build + 3.0s test
MISSED   src/xds/client.rs:531:21: replace || with && in AdsClient::run_loop in 44.0s build + 2.9s test
MISSED   src/tls/control.rs:116:12: delete ! in <impl ServerCertVerifier for
AltHostnameVerifier>::verify_server_cert in 44.0s build + 3.0s test
MISSED   src/copy.rs:140:47: replace * with / in 15.1s build + 2.8s test
TIMEOUT  src/test_helpers/netns.rs:83:9: replace Ready::set_ready with () in 19.2s build + 20.0s test
MISSED   src/signal.rs:102:9: replace imp::shutdown with () in 14.4s build + 2.7s test
MISSED   src/socket.rs:32:5: replace set_freebind_and_transparent -> io::Result<()> with Ok(()) in 26.2s build + 2.7s test
MISSED   src/test_helpers/ca.rs:88:16: replace * with / in CaServer::spawn in 18.6s build + 2.7s test
MISSED   src/copy.rs:314:45: replace && with || in <impl Future for CopyBuf<'_, R, W>>::poll in 22.8s build
+ 2.7s test
MISSED   src/proxy/pool.rs:522:9: replace ConnClient::is_for_workload -> Result<(), crate::proxy::Error> with Ok(()) in 23.1s build + 2.5s test
TIMEOUT  src/identity/caclient.rs:217:40: replace + with - in mock::CaClient::fetch_certificate in 16.3s build + 20.0s test
TIMEOUT  src/xds/client.rs:139:9: replace <impl RawHandler for HandlerWrapper<T>>::handle -> Result<(),
Vec<RejectedConfig>> with Ok(()) in 26.3s build + 20.0s test
MISSED   src/inpod/netns.rs:100:9: replace <impl PartialEq for InpodNetns>::eq -> bool with true in 15.2s build + 2.9s test
MISSED   src/copy.rs:314:20: replace < with > in <impl Future for CopyBuf<'_, R, W>>::poll in 14.7s build + 2.7s test
MISSED   src/test_helpers/ca.rs:88:16: replace * with + in CaServer::spawn in 17.7s build + 2.7s test
MISSED   src/state/service.rs:232:9: replace Service::contains_endpoint -> bool with true in 17.4s build + 3.7s test
TIMEOUT  src/hyper_util.rs:82:9: replace <impl Executor for TokioExecutor>::execute with () in 19.6s build + 20.0s test
MISSED   src/test_helpers/tcp.rs:77:29: replace += with *= in run_client in 40.5s build + 2.7s test
MISSED   src/state/workload.rs:737:66: replace == with != in WorkloadStore::was_last_identity_on_node in 26.8s build + 2.6s test
MISSED   src/xds/client.rs:533:21: replace || with && in AdsClient::run_loop in 18.0s build + 2.7s test
MISSED   src/tls/workload.rs:101:9: replace <impl ClientCertVerifier for
TrustDomainVerifier>::root_hint_subjects -> &[DistinguishedName] with Vec::leak(Vec::new()) in 18.0s build + 2.6s test
MISSED   src/test_helpers/tcp.rs:56:5: replace run_client -> Result<(), io::Error> with Ok(()) in 21.2s build + 2.7s test
MISSED   src/metrics.rs:188:9: replace <impl From for Option<T>>::from -> Self with Default::default() in 20.5s build + 2.7s test
MISSED   src/test_helpers/app.rs:178:9: replace TestApp::readiness_request -> anyhow::Result<()> with Ok(())
in 14.5s build + 2.7s test
MISSED   src/drain.rs:139:13: replace internal::Signal::closed with () in 14.8s build + 2.8s test
MISSED   src/inpod/config.rs:120:9: replace <impl SocketFactory for
InPodSocketFactory>::ipv6_enabled_localhost -> std::io::Result<bool> with Ok(false) in 20.1s build + 2.7s test
MISSED   src/inpod/statemanager.rs:212:9: replace WorkloadProxyManagerState::drain with () in 28.9s build + 2.7s test
MISSED   src/version.rs:55:9: replace <impl Display for BuildInfo>::fmt -> fmt::Result with
Ok(Default::default()) in 16.6s build + 2.7s test
MISSED   src/proxy/connection_manager.rs:126:9: replace <impl Drop for OutboundConnectionGuard>::drop with
() in 20.1s build + 2.7s test
MISSED   src/state.rs:392:79: replace == with != in ProxyState::load_balance in 20.1s build + 2.6s test
MISSED   src/inpod/packet.rs:31:33: replace | with & in bind in 17.9s build + 2.6s test
MISSED   src/proxy/connection_manager.rs:239:9: replace ConnectionManager::release_outbound with () in 22.1s build + 2.8s test
​
        Trail of Bits​ 17​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/copy.rs:224:25: replace == with != in ignore_shutdown_errors in 20.4s build + 2.7s test
MISSED   src/proxy/h2/client.rs:121:36: replace * with + in spawn_connection in 57.6s build + 2.7s test
MISSED   src/inpod/protocol.rs:56:9: replace WorkloadStreamProcessor::send_nack -> std::io::Result<()> with
Ok(()) in 23.3s build + 2.7s test
TIMEOUT  src/tls/certificate.rs:325:5: replace der_to_pem -> String with "xyzzy".into() in 49.4s build + 20.0s test
MISSED   src/xds/client.rs:293:9: replace Config::build_struct -> Struct with Default::default() in 28.4s build + 2.6s test
MISSED   src/copy.rs:135:48: replace - with + in 51.7s build + 2.7s test
MISSED   src/config.rs:534:35: replace * with / in construct_config in 17.8s build + 2.7s test
MISSED   src/drain.rs:186:13: replace internal::<impl Debug for Watch>::fmt -> std::fmt::Result with
Ok(Default::default()) in 14.5s build + 2.8s test
MISSED   src/proxy/metrics.rs:247:9: replace OnDemandDnsLabels::with_destination -> Self with
Default::default() in 19.4s build + 2.7s test
MISSED   src/tls/workload.rs:223:9: replace <impl Debug for DebugAsDisplay<T>>::fmt -> std::fmt::Result with
Ok(Default::default()) in 17.2s build + 2.7s test
MISSED   src/xds/client.rs:516:66: replace * with / in AdsClient::run_loop in 20.0s build + 2.7s test
MISSED   src/test_helpers/namespaced.rs:128:5: replace write_to_stderr -> io::Result<()> with Ok(()) in 19.5s build + 2.7s test
MISSED   src/dns/metrics.rs:187:9: replace <impl Recorder for Metrics>::record with () in 23.4s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:60:23: replace < with > in run_client in 22.7s build + 2.8s test
MISSED   src/identity/auth.rs:30:9: replace AuthSource::insert_headers -> anyhow::Result<()> with Ok(()) in 23.3s build + 2.6s test
MISSED   src/test_helpers.rs:165:5: replace localhost_error_message -> String with "xyzzy".into() in 25.2s build + 2.6s test
MISSED   src/config.rs:534:35: replace * with + in construct_config in 25.7s build + 2.8s test
MISSED   src/inpod/statemanager.rs:377:68: delete - in WorkloadProxyManagerState::update_proxy_count_metrics in 16.4s build + 2.6s test
MISSED   src/config.rs:327:5: replace parse_proxy_config -> Result<ProxyConfig, Error> with
Ok(Default::default()) in 30.3s build + 2.7s test
MISSED   src/state.rs:899:9: replace DemandProxyState::fetch_on_demand with () in 28.6s build + 2.8s test
MISSED   src/test_helpers/dns.rs:318:9: replace <impl Forwarder for TestDnsServer>::search_domains ->
Vec<Name> with vec![] in 29.2s build + 2.8s test
MISSED   src/xds/client.rs:532:25: replace && with || in AdsClient::run_loop in 20.4s build + 2.6s test
MISSED   src/identity/caclient.rs:96:46: replace > with == in CaClient::fetch_certificate in 20.3s build + 3.8s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new(Full::from_iter([Default::default()]))) in 22.4s build + 2.7s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from_iter([Full::new(Default::default())])) in 14.1s build + 2.7s test
MISSED   src/signal.rs:110:9: replace imp::watch_signal with () in 14.2s build + 2.8s test
MISSED   src/dns/metrics.rs:139:9: replace <impl Recorder for Metrics>::record with () in 22.8s build + 2.7s test
MISSED   src/admin.rs:120:9: replace Service::add_handler with () in 30.5s build + 2.7s test
MISSED   src/metrics.rs:146:9: replace <impl From for DefaultedUnknown<RichStrng>>::from -> Self with
Default::default() in 17.3s build + 2.7s test
MISSED   src/telemetry.rs:179:9: replace <impl Visit for Visitor<'_>>::record_str with () in 19.3s build + 2.8s test
MISSED   src/test_helpers/app.rs:201:9: replace TestApp::ready with () in 18.5s build + 2.7s test
MISSED   src/test_helpers.rs:518:9: replace MpscAckSender<T>::wait_forever -> anyhow::Result<()> with Ok(())
in 39.5s build + 2.7s test
MISSED   src/app.rs:305:5: replace mock_secret_manager -> Arc<SecretManager> with
Arc::new(Default::default()) in 18.9s build + 2.8s test
MISSED   src/xds/client.rs:577:32: replace += with *= in AdsClient::run in 21.1s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:206:21: replace > with < in handle_stream in 18.2s build + 2.8s test
MISSED   src/config.rs:317:5: replace parse_args -> String with String::new() in 22.8s build + 2.7s test
MISSED   src/state/workload.rs:528:9: replace <impl Display for NamespacedHostname>::fmt -> fmt::Result with
Ok(Default::default()) in 20.8s build + 2.7s test
TIMEOUT  src/state.rs:684:9: replace DemandProxyState::find_by_info -> Option<Arc<Workload>> with None in 17.5s build + 20.0s test
TIMEOUT  src/identity/manager.rs:245:9: replace Worker::has_id -> bool with false in 19.7s build + 20.0s test
TIMEOUT  src/tls/certificate.rs:117:9: replace Certificate::as_pem -> String with "xyzzy".into() in 26.0s build + 20.0s test
MISSED   src/proxy/outbound.rs:434:5: replace baggage -> String with "xyzzy".into() in 19.9s build + 2.7s test
​
        Trail of Bits​ 18​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/proxy/connection_manager.rs:106:9: replace ConnectionGuard::release with () in 20.1s build + 2.8s test
TIMEOUT  src/proxy/h2.rs:147:49: replace && with || in <impl ResizeBufRead for H2StreamReadHalf>::poll_bytes in 14.6s build + 20.1s test
MISSED   src/config.rs:546:29: replace > with < in construct_config in 28.3s build + 2.6s test
MISSED   src/copy.rs:113:9: replace <impl AsyncWriteBuf for WriteAdapter<T>>::poll_flush -> Poll<Result<(),
Error>> with Poll::from(Ok(())) in 16.8s build + 2.8s test
MISSED   src/proxy.rs:764:5: replace ipv6_enabled_on_localhost -> io::Result<bool> with Ok(true) in 18.4s build + 2.7s test
TIMEOUT  src/tls/certificate.rs:117:9: replace Certificate::as_pem -> String with String::new() in 21.5s build + 20.0s test
MISSED   src/identity/manager.rs:245:9: replace Worker::has_id -> bool with true in 25.0s build + 2.7s test
MISSED   src/proxy.rs:581:5: replace maybe_set_transparent -> Result<bool, Error> with Ok(false) in 24.5s build + 2.7s test
TIMEOUT  src/xds/client.rs:632:51: replace * with + in AdsClient::run_internal in 21.4s build + 20.0s test
TIMEOUT  src/config.rs:533:24: replace * with / in construct_config in 17.2s build + 20.1s test
MISSED   src/assertions.rs:25:5: replace size_between_ref with () in 24.4s build + 2.7s test
MISSED   src/tls/workload.rs:228:9: replace <impl Display for DebugAsDisplay<T>>::fmt -> std::fmt::Result with Ok(Default::default()) in 20.1s build + 2.7s test
MISSED   src/test_helpers/linux.rs:68:9: replace <impl Drop for WorkloadManager>::drop with () in 22.4s build + 2.5s test
TIMEOUT  src/proxy/socks5.rs:351:5: replace send_response -> Result<(), Error> with Ok(()) in 33.6s build + 20.1s test
MISSED   src/copy.rs:375:9: replace <impl AsyncWrite for BufReader<R>>::poll_write ->
Poll<io::Result<usize>> with Poll::from(Ok(0)) in 18.1s build + 2.7s test
MISSED   src/copy.rs:92:9: replace <impl AsyncWriteBuf for &mut T>::poll_flush -> Poll<Result<(), Error>> with Poll::from(Ok(())) in 16.5s build + 2.8s test
MISSED   src/state.rs:885:12: delete ! in DemandProxyState::fetch_hostname in 22.8s build + 2.6s test
TIMEOUT  src/xds/client.rs:513:9: replace AdsClient::run_loop -> Duration with Default::default() in 22.2s build + 20.0s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new()) in 24.0s build + 2.6s test
MISSED   src/tls/lib.rs:91:5: replace display_list -> String with "xyzzy".into() in 20.2s build + 2.7s test
MISSED   src/state.rs:632:50: replace == with != in DemandProxyState::resolve_on_demand_dns in 20.3s build + 2.6s test
MISSED   src/telemetry.rs:459:20: delete ! in testing::assert_contains in 48.6s build + 2.6s test
MISSED   src/proxy.rs:632:30: replace == with != in freebind_connect::connect in 20.8s build + 2.7s test
MISSED   src/copy.rs:317:71: replace <= with > in <impl Future for CopyBuf<'_, R, W>>::poll in 21.1s build + 2.6s test
MISSED   src/inpod/statemanager.rs:256:34: replace != with == in
WorkloadProxyManagerState::add_workload_inner in 47.9s build + 2.9s test
MISSED   src/test_helpers/tcp.rs:70:29: replace += with -= in run_client in 14.7s build + 2.9s test
MISSED   src/test_helpers/tcp.rs:77:29: replace += with -= in run_client in 15.0s build + 2.9s test
MISSED   src/state.rs:697:12: delete ! in DemandProxyState::fetch_workload_by_address in 26.4s build + 2.7s test
MISSED   src/inpod/workloadmanager.rs:365:9: replace WorkloadProxyManagerProcessor<'a>::schedule_retry with
() in 27.5s build + 2.9s test
MISSED   src/assertions.rs:26:27: replace > with == in size_between_ref in 22.8s build + 2.7s test
MISSED   src/xds.rs:188:17: replace && with || in ProxyStateUpdateMutator::remove_internal in 14.2s build + 2.8s test
MISSED   src/telemetry.rs:204:9: replace <impl FormatFields for IstioFormat>::format_fields -> std::fmt::Result with Ok(Default::default()) in 18.2s build + 2.7s test
MISSED   src/identity/manager.rs:124:9: replace Identity::trust_domain -> Strng with Default::default() in 24.3s build + 2.6s test
MISSED   src/copy.rs:222:5: replace ignore_shutdown_errors -> Result<(), io::Error> with Ok(()) in 25.1s build + 2.8s test
MISSED   src/config.rs:521:56: replace == with != in construct_config in 25.6s build + 2.6s test
MISSED   src/test_helpers/tcp.rs:172:25: replace == with != in handle_stream in 18.0s build + 2.7s test
MISSED   src/copy.rs:375:9: replace <impl AsyncWrite for BufReader<R>>::poll_write ->
Poll<io::Result<usize>> with Poll::from(Ok(1)) in 47.2s build + 2.7s test
MISSED   src/proxy.rs:688:79: replace == with != in guess_inbound_service in 43.2s build + 2.8s test
MISSED   src/rbac.rs:55:9: replace <impl Display for OptionDisplay<'_, T>>::fmt -> fmt::Result with
Ok(Default::default()) in 24.8s build + 2.7s test
MISSED   src/readiness/server.rs:50:9: replace Server::ready -> readiness::Ready with Default::default() in 43.5s build + 2.7s test
MISSED   src/drain.rs:192:13: replace internal::<impl Debug for ReleaseShutdown>::fmt -> std::fmt::Result with Ok(Default::default()) in 15.0s build + 2.9s test
​
        Trail of Bits​ 19​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/inpod/netns.rs:50:9: replace InpodNetns::capable -> std::io::Result<()> with Ok(()) in 17.5s build + 2.7s test
MISSED   src/inpod/workloadmanager.rs:92:9: replace WorkloadProxyReadinessHandler::not_ready with () in 23.0s build + 2.7s test
MISSED   src/copy.rs:138:41: replace * with + in 17.4s build + 2.7s test
MISSED   src/metrics.rs:156:9: replace <impl From for DefaultedUnknown<RichStrng>>::from -> Self with
Default::default() in 17.3s build + 2.8s test
MISSED   src/xds.rs:385:28: replace < with > in <impl Handler for ProxyStateUpdater>::handle in 57.3s build
+ 2.7s test
MISSED   src/state/workload.rs:737:9: replace WorkloadStore::was_last_identity_on_node -> bool with false in 16.0s build + 2.7s test
MISSED   src/telemetry.rs:187:9: replace <impl Visit for Visitor<'_>>::record_debug with () in 20.7s build + 2.7s test
MISSED   src/proxy.rs:164:9: replace <impl SocketFactory for MarkSocketFactory>::ipv6_enabled_localhost -> io::Result<bool> with Ok(true) in 27.1s build + 2.7s test
MISSED   src/proxy/util.rs:19:26: replace == with != in is_runtime_shutdown in 15.1s build + 2.7s test
TIMEOUT  src/xds/client.rs:577:32: replace += with -= in AdsClient::run in 18.4s build + 20.0s test
TIMEOUT  src/proxy/h2.rs:182:9: replace <impl AsyncWriteBuf for H2StreamWriteHalf>::poll_write_buf ->
Poll<std::io::Result<usize>> with Poll::from(Ok(1)) in 27.0s build + 20.0s test
MISSED   src/inpod/statemanager.rs:370:9: replace WorkloadProxyManagerState::update_proxy_count_metrics with
() in 41.7s build + 2.7s test
MISSED   src/test_helpers.rs:401:41: replace > with == in check_eventually in 26.7s build + 2.7s test
MISSED   src/socket.rs:177:9: replace Listener::set_transparent -> io::Result<()> with Ok(()) in 14.9s build
+ 2.8s test
MISSED   src/inpod/protocol.rs:233:19: replace != with == in validate_ns in 14.0s build + 2.7s test
MISSED   src/config.rs:313:5: replace parse_duration_default -> Result<Duration, Error> with
Ok(Default::default()) in 20.9s build + 2.9s test
MISSED   src/test_helpers/ca.rs:88:21: replace * with + in CaServer::spawn in 20.7s build + 2.9s test
MISSED   src/config.rs:550:30: replace - with / in construct_config in 18.1s build + 2.7s test
MISSED   src/config.rs:82:78: replace * with + in 24.5s build + 2.7s test
MISSED   src/state.rs:124:9: replace WorkloadInfo::matches -> bool with true in 46.7s build + 2.8s test
MISSED   src/config.rs:673:8: delete ! in validate_config in 21.9s build + 2.7s test
MISSED   src/proxy/inbound.rs:524:5: replace parse_forwarded_host -> Option<String> with
Some("xyzzy".into()) in 28.3s build + 2.7s test
MISSED   src/state.rs:894:9: replace DemandProxyState::supports_on_demand -> bool with false in 20.1s build
+ 2.9s test
MISSED   src/state.rs:125:13: replace && with || in WorkloadInfo::matches in 16.9s build + 2.8s test
MISSED   src/copy.rs:138:41: replace * with / in 16.5s build + 2.8s test
TIMEOUT  src/state.rs:126:37: replace == with != in WorkloadInfo::matches in 16.0s build + 20.1s test
MISSED   src/copy.rs:88:9: replace <impl AsyncWriteBuf for &mut T>::poll_write_buf ->
Poll<std::io::Result<usize>> with Poll::from(Ok(0)) in 15.9s build + 2.8s test
MISSED   src/admin.rs:325:5: replace handle_logging -> Response<Full<Bytes>> with
Response::new(Full::new(Default::default())) in 27.6s build + 2.7s test
MISSED   src/proxy.rs:544:9: replace <impl Debug for TraceParent>::fmt -> fmt::Result with
Ok(Default::default()) in 52.6s build + 2.7s test
MISSED   src/state.rs:869:12: delete ! in DemandProxyState::fetch_address in 21.6s build + 2.7s test
MISSED   src/admin.rs:382:15: replace && with || in change_log_level in 21.4s build + 2.8s test
MISSED   src/socket.rs:170:9: replace Listener::set_transparent -> io::Result<()> with Ok(()) in 23.6s build
+ 2.7s test
MISSED   src/tls/control.rs:204:41: replace == with != in grpc_connector in 29.6s build + 2.7s test
MISSED   src/telemetry.rs:225:9: replace <impl FormatEvent for IstioFormat>::format_event -> std::fmt::Result with Ok(Default::default()) in 19.4s build + 2.7s test
MISSED   src/state/policy.rs:100:9: replace PolicyStore::send with () in 19.5s build + 2.6s test
TIMEOUT  src/proxy/pool.rs:215:9: replace PoolState::start_conn_if_win_writelock ->
Result<Option<ConnClient>, Error> with Ok(None) in 26.0s build + 20.0s test
MISSED   src/tls/control.rs:164:9: replace <impl ServerCertVerifier for
AltHostnameVerifier>::supported_verify_schemes -> Vec<SignatureScheme> with vec![] in 26.1s build + 2.9s test
MISSED   src/inpod/netns.rs:100:29: replace == with != in <impl PartialEq for InpodNetns>::eq in 28.2s build
+ 2.7s test
MISSED   src/proxy/metrics.rs:75:9: replace <impl EncodeLabelValue for ResponseFlags>::encode -> Result<(), std::fmt::Error> with Ok(()) in 17.1s build + 2.9s test
MISSED   src/test_helpers/tcp.rs:61:49: replace - with / in run_client in 18.6s build + 2.9s test
TIMEOUT  src/state/workload.rs:720:9: replace WorkloadStore::find_by_info -> Option<Arc<Workload>> with None in 25.6s build + 20.0s test
MISSED   src/inpod/statemanager.rs:339:32: replace && with || in WorkloadProxyManagerState::ready in 28.2s build + 2.8s test
MISSED   src/copy.rs:140:40: replace * with + in 14.5s build + 2.9s test
​
        Trail of Bits​ 20​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from(Full::new(Default::default()))) in 21.6s build + 2.9s test
MISSED   src/proxy/h2/server.rs:104:36: replace * with / in serve_connection in 39.0s build + 2.6s test
MISSED   src/state/workload.rs:737:38: replace || with && in WorkloadStore::was_last_identity_on_node in 19.9s build + 2.7s test
MISSED   src/proxy/h2/server.rs:38:9: replace <impl Debug for H2Request>::fmt -> std::fmt::Result with
Ok(Default::default()) in 23.7s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:71:49: replace * with + in run_client in 28.2s build + 2.8s test
MISSED   src/copy.rs:395:9: replace <impl AsyncWrite for BufReader<R>>::is_write_vectored -> bool with true in 13.8s build + 2.7s test
MISSED   src/time.rs:60:9: replace Converter::subsec_nanos -> u32 with 1 in 17.9s build + 2.6s test
MISSED   src/proxy/util.rs:19:9: replace && with || in is_runtime_shutdown in 14.1s build + 2.6s test
TIMEOUT  src/state.rs:124:9: replace WorkloadInfo::matches -> bool with false in 24.4s build + 20.0s test
MISSED   src/state/workload.rs:740:13: delete ! in WorkloadStore::was_last_identity_on_node in 13.7s build + 2.6s test
MISSED   src/config.rs:547:30: replace - with + in construct_config in 36.6s build + 2.6s test
MISSED   src/proxy/socks5.rs:334:5: replace send_error with () in 21.8s build + 2.8s test
TIMEOUT  src/identity/manager.rs:476:5: replace push_increase with () in 27.8s build + 20.1s test
MISSED   src/xds.rs:217:12: delete ! in ProxyStateUpdateMutator::remove_internal in 28.5s build + 3.8s test
MISSED   src/xds/client.rs:528:48: replace == with != in AdsClient::run_loop in 17.9s build + 2.7s test
MISSED   src/test_helpers/app.rs:383:9: replace ParsedMetrics::dump -> String with String::new() in 24.4s build + 2.7s test
MISSED   src/proxy.rs:562:24: replace != with == in <impl TryFrom for TraceParent>::try_from in 17.0s build
+ 2.7s test
MISSED   src/state/workload.rs:510:17: replace <impl Deserialize for NamespacedHostname>::deserialize::<impl
Visitor for NamespacedHostnameVisitor>::expecting -> fmt::Result with Ok(Default::default()) in 20.3s build
+ 2.7s test
MISSED   src/socket.rs:122:9: replace linux::set_ipv6_transparent -> io::Result<()> with Ok(()) in 27.4s build + 2.7s test
MISSED   src/state.rs:389:58: replace == with != in ProxyState::load_balance in 23.8s build + 2.7s test
MISSED   src/proxy.rs:757:5: replace read_sysctl -> io::Result<String> with Ok(String::new()) in 18.7s build
+ 2.6s test
MISSED   src/proxy.rs:757:5: replace read_sysctl -> io::Result<String> with Ok("xyzzy".into()) in 20.3s build + 2.7s test
MISSED   src/state.rs:391:70: replace == with != in ProxyState::load_balance in 18.6s build + 2.8s test
MISSED   src/config.rs:81:54: replace * with + in 22.7s build + 2.6s test
MISSED   src/telemetry.rs:305:9: replace <impl Visit for JsonVisitory<S>>::record_f64 with () in 16.2s build
+ 2.6s test
MISSED   src/xds/client.rs:529:38: replace == with != in AdsClient::run_loop in 26.2s build + 2.7s test
MISSED   src/inpod/workloadmanager.rs:142:9: replace WorkloadProxyManager::verify_set_mark -> anyhow::Result<()> with Ok(()) in 36.4s build + 2.7s test
MISSED   src/tls/certificate.rs:289:9: replace WorkloadCertificate::dump_chain -> Bytes with
Default::default() in 19.4s build + 2.6s test
MISSED   src/proxy/connection_manager.rs:315:9: replace PolicyWatcher::run with () in 26.3s build + 2.7s test
MISSED   src/proxy/metrics.rs:530:9: replace <impl Drop for ConnectionResult>::drop with () in 46.8s build + 2.6s test
MISSED   src/config.rs:534:42: replace * with + in construct_config in 16.5s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:61:49: replace - with + in run_client in 23.6s build + 2.7s test
MISSED   src/inpod/admin.rs:54:5: replace always_none -> Result<Option<ConnectionManager>, D::Error> with
Ok(Some(Default::default())) in 14.6s build + 2.6s test
MISSED   src/telemetry.rs:74:75: replace == with != in fmt_layer in 14.7s build + 2.7s test
MISSED   src/copy.rs:314:71: replace <= with > in <impl Future for CopyBuf<'_, R, W>>::poll in 14.1s build + 2.7s test
MISSED   src/hyper_util.rs:168:5: replace empty_response -> Response<Full<Bytes>> with
Response::new(Full::new(Default::default())) in 19.3s build + 2.7s test
MISSED   src/proxy.rs:707:54: replace && with || in check_from_waypoint in 23.1s build + 2.7s test
MISSED   src/proxy/pool.rs:535:9: replace <impl Drop for ConnClient>::drop with () in 21.6s build + 2.6s test
MISSED   src/inpod/config.rs:120:9: replace <impl SocketFactory for
InPodSocketFactory>::ipv6_enabled_localhost -> std::io::Result<bool> with Ok(true) in 25.2s build + 2.7s test
TIMEOUT  src/state/workload.rs:239:9: replace Workload::identity -> Identity with Default::default() in 16.7s build + 20.0s test
MISSED   src/dns/server.rs:622:49: replace == with != in service_family_allowed in 15.9s build + 2.7s test
MISSED   src/tls/workload.rs:190:9: replace IdentityVerifier::verify_full_san -> Result<(), rustls::Error> with Ok(()) in 20.9s build + 2.7s test build    src/inpod/admin.rs:119:27: replace -= with += in WorkloadManagerAdminHandler::proxy_down ... 4.9s
​
        Trail of Bits​ 21​
Istio Ztunnel​
        PUBLIC​
​

└             Running `/home/jofra/.rustup/toolchains/stable-aarch64-unknown-linux-gnu/bin/rustc
--crate-name ztunnel --edition=2021 src/lib.rs --error-format=MISSED   src/readiness.rs:41:9: replace
Ready::pending -> HashSet<String> with HashSet::new() in 20.6s build + 2.9s test
MISSED   src/proxy/inbound.rs:524:5: replace parse_forwarded_host -> Option<String> with None in 22.0s build
+ 2.8s test
MISSED   src/config.rs:673:19: replace && with || in validate_config in 21.1s build + 2.9s test
MISSED   src/test_helpers.rs:405:15: replace *= with /= in check_eventually in 30.9s build + 2.8s test
MISSED   src/state/service.rs:107:9: replace EndpointSet::get -> Option<&Endpoint> with None in 18.8s build
+ 2.9s test
MISSED   src/xds/client.rs:531:39: replace == with != in AdsClient::run_loop in 19.2s build + 2.8s test
TIMEOUT  src/state/workload.rs:673:38: replace || with && in WorkloadStore::insert in 14.5s build + 20.1s test
MISSED   src/socket.rs:107:5: replace set_mark -> io::Result<()> with Ok(()) in 20.4s build + 2.8s test
MISSED   src/copy.rs:317:20: replace < with == in <impl Future for CopyBuf<'_, R, W>>::poll in 19.4s build + 2.7s test
MISSED   src/app.rs:317:5: replace init_inpod_proxy_mgr -> anyhow::Result<std::pin::Pin<Box<dyn std::future::Future<Output =()>+Send +Sync>>> with Ok(Pin::from(Box::new(Default::default()))) in 14.2s build + 2.9s test
MISSED   src/tls/certificate.rs:243:47: replace - with / in WorkloadCertificate::cert_and_intermediates in 17.4s build + 2.7s test
MISSED   src/test_helpers.rs:395:18: replace += with *= in check_eventually in 36.7s build + 2.7s test
MISSED   src/test_helpers.rs:395:18: replace += with -= in check_eventually in 17.4s build + 2.7s test
MISSED   src/assertions.rs:26:19: replace || with && in size_between_ref in 23.9s build + 3.0s test
TIMEOUT  src/xds/client.rs:575:9: replace AdsClient::run -> Result<(), Error> with Ok(()) in 24.2s build + 20.0s test
MISSED   src/readiness/server.rs:68:5: replace handle_ready -> Response<Full<Bytes>> with
Response::new(Full::new(Default::default())) in 32.9s build + 3.4s test
MISSED   src/test_helpers/tcp.rs:65:29: replace += with -= in run_client in 24.4s build + 2.8s test
TIMEOUT  src/time.rs:36:9: replace Converter::system_time_to_instant -> Option<Instant> with None in 19.2s build + 20.0s test
MISSED   src/telemetry.rs:245:24: delete ! in <impl FormatEvent for IstioFormat>::format_event in 20.8s build + 2.8s test
MISSED   src/copy.rs:133:41: replace - with + in 14.3s build + 2.7s test
MISSED   src/inpod/workloadmanager.rs:293:9: replace WorkloadProxyManagerProcessor<'a>::retry_proxies with
() in 22.6s build + 2.8s test
MISSED   src/copy.rs:391:9: replace <impl AsyncWrite for BufReader<R>>::poll_write_vectored ->
Poll<io::Result<usize>> with Poll::from(Ok(0)) in 14.8s build + 2.8s test
MISSED   src/xds/metrics.rs:92:9: replace <impl Recorder for Metrics>::record with () in 28.7s build + 2.7s test
MISSED   src/proxy/util.rs:18:17: replace == with != in is_runtime_shutdown in 59.0s build + 2.7s test
MISSED   src/copy.rs:395:9: replace <impl AsyncWrite for BufReader<R>>::is_write_vectored -> bool with false in 18.4s build + 2.7s test
MISSED   src/copy.rs:225:29: replace == with != in ignore_shutdown_errors in 17.8s build + 3.1s test
MISSED   src/admin.rs:338:32: replace || with && in handle_logging in 23.0s build + 2.8s test
TIMEOUT  src/copy.rs:140:40: replace * with / in 46.8s build + 20.0s test
MISSED   src/state.rs:982:9: replace ProxyStateManager::run -> anyhow::Result<()> with Ok(()) in 17.9s build
+ 2.8s test
MISSED   src/main.rs:57:5: replace help -> anyhow::Result<()> with Ok(()) in 27.0s build + 3.2s test
MISSED   src/admin.rs:158:5: replace handle_dashboard -> Response<Full<Bytes>> with
Response::new(Full::new(Default::default())) in 37.1s build + 3.2s test
MISSED   src/test_helpers/tcp.rs:70:29: replace += with *= in run_client in 29.7s build + 3.0s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new(Full::new())) in 22.2s build + 2.9s test
MISSED   src/xds/client.rs:530:21: replace || with && in AdsClient::run_loop in 20.8s build + 3.4s test
MISSED   src/config.rs:81:54: replace * with / in 19.0s build + 2.9s test
TIMEOUT  src/identity/manager.rs:203:9: replace <impl PartialOrd for PendingPriority>::partial_cmp ->
Option<Ordering> with None in 17.8s build + 20.0s test
MISSED   src/inpod/admin.rs:142:9: replace <impl AdminHandler for WorkloadManagerAdminHandler>::key ->
&'static str with "xyzzy" in 16.6s build + 2.9s test
MISSED   src/telemetry.rs:406:9: replace <impl FormatFields for IstioJsonFormat>::add_fields -> fmt::Result with Ok(Default::default()) in 19.7s build + 2.8s test
MISSED   src/proxy.rs:104:9: replace <impl SocketFactory for DefaultSocketFactory>::ipv6_enabled_localhost
-> io::Result<bool> with Ok(true) in 17.0s build + 2.9s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new(Full::from(Default::default()))) in 21.4s build + 2.8s test
TIMEOUT  src/signal.rs:62:9: replace ShutdownTrigger::shutdown_now with () in 27.5s build + 20.0s test
MISSED   src/drain.rs:180:13: replace internal::<impl Debug for Signal>::fmt -> std::fmt::Result with
Ok(Default::default()) in 24.6s build + 2.8s test
​
        Trail of Bits​ 22​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/rbac.rs:64:9: replace <impl Display for Connection>::fmt -> fmt::Result with
Ok(Default::default()) in 18.3s build + 2.8s test
MISSED   src/inpod/config.rs:193:9: replace <impl SocketFactory for
InPodSocketPortReuseFactory>::ipv6_enabled_localhost -> std::io::Result<bool> with Ok(true) in 20.5s build + 2.9s test
TIMEOUT  src/xds/client.rs:632:44: replace * with + in AdsClient::run_internal in 21.7s build + 20.0s test
MISSED   src/xds/client.rs:334:9: replace Config::node -> Node with Default::default() in 29.3s build + 2.9s test
MISSED   src/xds/client.rs:60:9: replace <impl Display for ResourceKey>::fmt -> fmt::Result with
Ok(Default::default()) in 30.5s build + 2.7s test
MISSED   src/copy.rs:311:22: replace += with *= in <impl Future for CopyBuf<'_, R, W>>::poll in 34.0s build
+ 2.9s test
MISSED   src/test_helpers/app.rs:167:9: replace TestApp::inpod_state -> anyhow::Result<HashMap<String, inpod::admin::ProxyState>> with Ok(HashMap::new()) in 15.0s build + 7.5s test
MISSED   src/inpod/statemanager.rs:203:34: delete ! in WorkloadProxyManagerState::reconcile in 16.4s build + 2.8s test
MISSED   src/proxy/h2.rs:211:9: replace <impl AsyncWriteBuf for H2StreamWriteHalf>::poll_flush ->
Poll<Result<(), Error>> with Poll::from(Ok(())) in 17.9s build + 2.7s test
MISSED   src/proxy/h2/server.rs:104:36: replace * with + in serve_connection in 22.3s build + 2.9s test
MISSED   src/telemetry.rs:498:13: replace testing::<impl Write for MockWriter<'_>>::flush -> io::Result<()> with Ok(()) in 19.0s build + 2.8s test
MISSED   src/xds.rs:65:12: delete ! in <impl Display for DisplayStatus<'_>>::fmt in 18.6s build + 2.9s test
MISSED   src/socket.rs:131:20: replace != with == in linux::set_ipv6_transparent in 21.3s build + 3.0s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from_iter([Full::from(Default::default())])) in 21.7s build + 3.0s test
MISSED   src/inpod/statemanager.rs:44:9: replace DrainingTasks::shutdown_workload with () in 28.8s build + 2.9s test
MISSED   src/socket.rs:93:5: replace set_freebind_and_transparent -> io::Result<()> with Ok(()) in 50.0s build + 2.8s test
MISSED   src/metrics.rs:176:9: replace <impl From for DefaultedUnknown<RichStrng>>::from -> Self with
Default::default() in 23.6s build + 2.9s test
TIMEOUT  src/strng.rs:33:5: replace new -> Strng with Default::default() in 27.7s build + 20.0s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from(Full::from(Default::default()))) in 29.9s build + 2.9s test
MISSED   src/inpod/protocol.rs:242:67: replace != with == in validate_ns in 19.3s build + 3.2s test
MISSED   src/inpod/statemanager.rs:339:9: replace WorkloadProxyManagerState::ready -> bool with true in 19.5s build + 2.9s test
MISSED   src/copy.rs:314:20: replace < with == in <impl Future for CopyBuf<'_, R, W>>::poll in 21.7s build + 2.9s test
MISSED   src/test_helpers/netns.rs:175:5: replace drop_namespace with () in 24.3s build + 2.7s test
MISSED   src/identity/caclient.rs:96:46: replace > with < in CaClient::fetch_certificate in 33.5s build + 2.8s test
MISSED   src/inpod/protocol.rs:242:57: replace && with || in validate_ns in 41.4s build + 2.8s test
MISSED   src/inpod/packet.rs:39:50: replace - with + in bind in 23.4s build + 2.8s test
MISSED   src/test_helpers/ca.rs:88:21: replace * with / in CaServer::spawn in 31.4s build + 2.9s test
MISSED   src/admin.rs:414:8: delete ! in handle_jemalloc_pprof_heapgen in 20.2s build + 2.8s test
MISSED   src/tls/workload.rs:234:9: replace <impl Error for DebugAsDisplay<T>>::source -> Option<&(dyn Error
+'static)> with None in 27.1s build + 2.9s test
MISSED   src/state/workload.rs:303:33: replace == with != in <impl TryFrom for ApplicationTunnel>::try_from in 17.6s build + 2.9s test
MISSED   src/config.rs:800:9: replace <impl Display for Address>::fmt -> std::fmt::Result with
Ok(Default::default()) in 15.2s build + 3.3s test
MISSED   src/inpod/protocol.rs:226:5: replace validate_ns -> anyhow::Result<()> with Ok(()) in 46.5s build + 2.7s test
TIMEOUT  src/identity/manager.rs:437:9: replace Worker::update_certs -> bool with true in 28.4s build + 20.0s test
MISSED   src/xds/metrics.rs:99:32: replace += with *= in <impl Recorder for Metrics>::record in 17.1s build
+ 2.7s test
MISSED   src/test_helpers/netns.rs:97:9: replace Namespace::interface -> String with "xyzzy".into() in 15.0s build + 2.9s test
MISSED   src/test_helpers/tcp.rs:162:26: replace == with != in handle_stream in 22.9s build + 2.8s test
MISSED   src/proxy/connection_manager.rs:50:9: replace ConnectionDrain::drain with () in 22.3s build + 2.7s test
MISSED   src/inpod/statemanager.rs:343:9: replace WorkloadProxyManagerState::retry_pending with () in 26.2s build + 2.7s test
MISSED   src/copy.rs:317:20: replace < with > in <impl Future for CopyBuf<'_, R, W>>::poll in 23.8s build + 3.0s test
​
        Trail of Bits​ 23​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/test_helpers/app.rs:380:9: replace ParsedMetrics::metric_info -> HashMap<String, String> with
HashMap::new() in 16.0s build + 2.8s test
TIMEOUT  src/xds/client.rs:587:9: replace AdsClient::run_internal -> Result<(), Error> with Ok(()) in 38.1s build + 20.0s test
MISSED   src/test_helpers/namespaced.rs:140:15: replace < with == in write_to_stderr in 22.7s build + 2.9s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new(Full::new(Default::default()))) in 26.4s build + 2.8s test
MISSED   src/dns/server.rs:384:64: replace == with != in Store::find_server in 21.1s build + 2.9s test
MISSED   src/copy.rs:135:38: replace * with + in 16.7s build + 2.8s test
MISSED   src/xds/metrics.rs:84:9: replace <impl Recorder for Metrics>::record with () in 26.8s build + 2.7s test
MISSED   src/inpod/netns.rs:92:9: replace <impl AsRawFd for InpodNetns>::as_raw_fd -> std::os::unix::io::RawFd with Default::default() in 22.0s build + 3.0s test
MISSED   src/identity/manager.rs:493:9: replace <impl Debug for SecretManager>::fmt -> fmt::Result with
Ok(Default::default()) in 21.1s build + 2.8s test
MISSED   src/inpod/protocol.rs:242:19: replace != with == in validate_ns in 20.1s build + 3.1s test
MISSED   src/identity/manager.rs:78:34: replace || with && in <impl FromStr for Identity>::from_str in 16.4s build + 2.9s test
MISSED   src/config.rs:307:5: replace parse_duration -> Result<Option<Duration>, Error> with Ok(None) in 42.3s build + 2.8s test
MISSED   src/copy.rs:133:41: replace - with / in 22.5s build + 2.9s test
MISSED   src/test_helpers/dns.rs:348:9: replace <impl Forwarder for FakeForwarder>::search_domains ->
Vec<Name> with vec![Default::default()] in 19.4s build + 3.9s test
TIMEOUT  src/state/workload.rs:663:9: replace WorkloadStore::insert with () in 22.0s build + 20.0s test
MISSED   src/test_helpers.rs:165:5: replace localhost_error_message -> String with String::new() in 26.7s build + 3.0s test
MISSED   src/state.rs:145:9: replace <impl Display for ProxyRbacContext>::fmt -> fmt::Result with
Ok(Default::default()) in 28.1s build + 3.3s test
MISSED   src/state/workload.rs:249:9: replace <impl Display for Workload>::fmt -> fmt::Result with
Ok(Default::default()) in 29.4s build + 3.1s test
MISSED   src/time.rs:56:9: replace Converter::elapsed_nanos -> u128 with 1 in 46.9s build + 2.9s test
MISSED   src/tls/control.rs:244:9: replace <impl Service for TlsGrpcChannel>::poll_ready -> Poll<Result<(),
Self::Error>> with Poll::from(Ok(())) in 22.4s build + 2.8s test
MISSED   src/tls/mock.rs:46:9: replace <impl Display for TestIdentity>::fmt -> std::fmt::Result with
Ok(Default::default()) in 23.0s build + 2.8s test
TIMEOUT  src/proxy/pool.rs:277:9: replace PoolState::checkout_conn_under_writelock ->
Result<Option<ConnClient>, Error> with Ok(None) in 30.9s build + 20.0s test
MISSED   src/socket.rs:69:20: delete ! in orig_dst_addr in 30.0s build + 3.8s test
MISSED   src/state/workload.rs:97:9: replace <impl From for Locality>::from -> Self with Default::default()
in 39.1s build + 2.9s test
MISSED   src/tls/csr.rs:29:9: replace CsrOptions::generate -> Result<CertSign, Error> with
Ok(Default::default()) in 26.8s build + 2.9s test
MISSED   src/dns/metrics.rs:163:9: replace <impl Recorder for Metrics>::record with () in 56.2s build + 2.9s test
MISSED   src/proxy/inbound.rs:437:20: delete ! in Inbound::validate_destination in 27.6s build + 2.9s test
TIMEOUT  src/identity/manager.rs:450:5: replace maybe_sleep_until -> bool with false in 24.2s build + 20.0s test
MISSED   src/config.rs:533:24: replace * with + in construct_config in 14.9s build + 2.9s test
MISSED   src/test_helpers/dns.rs:380:30: replace == with != in <impl Forwarder for FakeForwarder>::forward in 30.5s build + 2.8s test
MISSED   src/test_helpers/tcp.rs:104:31: replace * with + in 17.2s build + 2.9s test
MISSED   src/inpod/statemanager.rs:109:9: replace WorkloadProxyManagerState::reset_snapshot with () in 25.0s build + 2.9s test
MISSED   src/proxy/connection_manager.rs:65:9: replace <impl Debug for ConnectionManager>::fmt -> std::fmt::Result with Ok(Default::default()) in 49.9s build + 2.8s test
MISSED   src/xds/client.rs:774:9: replace XdsUpdate<T>::name -> Strng with Default::default() in 20.2s build
+ 2.8s test
MISSED   src/proxy/inbound.rs:524:5: replace parse_forwarded_host -> Option<String> with Some(String::new())
in 27.3s build + 2.9s test
MISSED   src/telemetry.rs:299:9: replace <impl Visit for JsonVisitory<S>>::record_i64 with () in 21.4s build
+ 2.8s test
MISSED   src/telemetry.rs:167:9: replace Visitor<'_>::write_padded -> std::fmt::Result with
Ok(Default::default()) in 19.6s build + 7.0s test
MISSED   src/time.rs:60:9: replace Converter::subsec_nanos -> u32 with 0 in 21.6s build + 2.8s test
MISSED   src/xds/client.rs:529:21: replace || with && in AdsClient::run_loop in 20.4s build + 2.7s test
MISSED   src/proxy.rs:125:41: replace + with - in DefaultSocketFactory::setup_socket in 24.1s build + 2.8s test
​
        Trail of Bits​ 24​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/copy.rs:225:17: replace || with && in ignore_shutdown_errors in 18.0s build + 2.9s test
MISSED   src/test_helpers/netns.rs:263:51: replace + with * in NamespaceManager::child in 14.2s build + 2.8s test
MISSED   src/test_helpers/app.rs:383:9: replace ParsedMetrics::dump -> String with "xyzzy".into() in 22.8s build + 2.8s test
MISSED   src/proxy.rs:672:46: replace == with != in guess_inbound_service in 22.4s build + 3.7s test
MISSED   src/proxy.rs:682:26: replace == with != in guess_inbound_service in 18.9s build + 2.9s test
MISSED   src/admin.rs:431:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::new(Full::new(Default::default()))) in 24.7s build + 2.9s test
MISSED   src/main.rs:32:5: replace main -> anyhow::Result<()> with Ok(()) in 24.4s build + 2.8s test
MISSED   src/xds/client.rs:534:25: replace && with || in AdsClient::run_loop in 18.7s build + 2.9s test
MISSED   src/copy.rs:379:9: replace <impl AsyncWrite for BufReader<R>>::poll_flush -> Poll<io::Result<()>> with Poll::from(Ok(())) in 18.3s build + 2.9s test
MISSED   src/xds/client.rs:474:9: replace AdsClient::is_initial_request_on_demand -> bool with false in 16.1s build + 2.8s test
MISSED   src/state.rs:106:9: replace <impl Display for WorkloadInfo>::fmt -> fmt::Result with
Ok(Default::default()) in 26.1s build + 2.9s test
MISSED   src/config.rs:533:31: replace * with + in construct_config in 26.5s build + 3.3s test
MISSED   src/copy.rs:135:48: replace - with / in 14.4s build + 2.8s test
MISSED   src/xds/client.rs:530:38: replace == with != in AdsClient::run_loop in 30.4s build + 2.8s test
MISSED   src/inpod/statemanager.rs:373:66: delete - in WorkloadProxyManagerState::update_proxy_count_metrics in 18.5s build + 2.8s test
MISSED   src/proxy.rs:110:9: replace DefaultSocketFactory::setup_socket -> io::Result<()> with Ok(()) in 56.0s build + 2.8s test
MISSED   src/config.rs:655:27: replace == with != in construct_config in 26.3s build + 2.8s test
MISSED   src/inpod/packet.rs:50:33: replace | with ^ in connect in 46.1s build + 2.8s test
TIMEOUT  src/time.rs:37:36: replace + with - in Converter::system_time_to_instant in 29.0s build + 20.1s test
MISSED   src/rbac.rs:386:9: replace <impl TryFrom for IpNet>::try_from -> Result<Self, Self::Error> with
Ok(Default::default()) in 20.3s build + 2.9s test
MISSED   src/identity/auth.rs:58:5: replace load_token -> io::Result<Vec<u8>> with Ok(vec![]) in 22.0s build
+ 2.7s test
MISSED   src/metrics.rs:65:9: replace <impl Drop for Deferred<'a, F, T>>::drop with () in 50.6s build + 4.0s test
TIMEOUT  src/proxy/h2.rs:121:9: replace H2StreamWriteHalf::write_slice -> Result<(), std::io::Error> with
Ok(()) in 19.3s build + 20.0s test
MISSED   src/test_helpers/tcp.rs:190:22: replace == with != in handle_stream in 28.8s build + 2.7s test
MISSED   src/inpod/statemanager.rs:334:9: replace WorkloadProxyManagerState::pending_uids -> Vec<String> with vec!["xyzzy".into()] in 29.3s build + 2.9s test
MISSED   src/config.rs:673:22: delete ! in validate_config in 14.0s build + 2.7s test
MISSED   src/config.rs:81:59: replace * with / in 24.2s build + 2.8s test
MISSED   src/config.rs:534:42: replace * with / in construct_config in 16.4s build + 2.8s test
TIMEOUT  src/xds/client.rs:632:51: replace * with / in AdsClient::run_internal in 29.5s build + 20.0s test
MISSED   src/main.rs:76:5: replace proxy -> anyhow::Result<()> with Ok(()) in 17.9s build + 2.7s test
MISSED   src/state.rs:894:9: replace DemandProxyState::supports_on_demand -> bool with true in 16.7s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:104:38: replace * with + in 22.5s build + 2.7s test
MISSED   src/xds.rs:56:9: replace <impl Display for DisplayStatus<'_>>::fmt -> fmt::Result with
Ok(Default::default()) in 23.9s build + 2.7s test
MISSED   src/state/workload.rs:737:9: replace WorkloadStore::was_last_identity_on_node -> bool with true in 23.3s build + 2.6s test
MISSED   src/tls/lib.rs:91:5: replace display_list -> String with String::new() in 20.8s build + 2.7s test
MISSED   src/proxy.rs:764:5: replace ipv6_enabled_on_localhost -> io::Result<bool> with Ok(false) in 21.6s build + 2.7s test
MISSED   src/test_helpers/tcp.rs:206:21: replace > with == in handle_stream in 21.4s build + 2.7s test
MISSED   src/config.rs:82:78: replace * with / in 17.6s build + 2.7s test
MISSED   src/test_helpers/dns.rs:348:9: replace <impl Forwarder for FakeForwarder>::search_domains ->
Vec<Name> with vec![] in 24.4s build + 2.9s test
MISSED   src/state.rs:711:12: delete ! in DemandProxyState::fetch_workload_by_uid in 21.2s build + 2.8s test
MISSED   src/xds/client.rs:449:9: replace <impl Display for XdsSignal>::fmt -> fmt::Result with
Ok(Default::default()) in 22.6s build + 2.8s test
MISSED   src/inpod/statemanager.rs:334:9: replace WorkloadProxyManagerState::pending_uids -> Vec<String> with vec![String::new()] in 26.1s build + 2.7s test
MISSED   src/test_helpers/netns.rs:195:9: replace <impl Drop for NamespaceManager>::drop with () in 22.2s build + 2.5s test
MISSED   src/test_helpers/tcp.rs:71:49: replace * with / in run_client in 14.5s build + 2.7s test
MISSED   src/inpod/statemanager.rs:330:9: replace WorkloadProxyManagerState::have_pending -> bool with false in 15.8s build + 2.7s test
​
        Trail of Bits​ 25​
Istio Ztunnel​
        PUBLIC​
​

MISSED   src/test_helpers/dns.rs:318:9: replace <impl Forwarder for TestDnsServer>::search_domains ->
Vec<Name> with vec![Default::default()] in 19.4s build + 2.7s test
MISSED   src/inpod/statemanager.rs:57:9: replace DrainingTasks::join with () in 16.7s build + 2.8s test
MISSED   src/identity/caclient.rs:177:13: replace mock::CaClient::cert_lifetime -> Duration with
Default::default() in 17.1s build + 2.7s test
MISSED   src/dns/server.rs:643:9: replace <impl Display for Alias>::fmt -> std::fmt::Result with
Ok(Default::default()) in 17.3s build + 2.7s test
MISSED   src/copy.rs:317:45: replace && with || in <impl Future for CopyBuf<'_, R, W>>::poll in 14.4s build
+ 2.8s test
MISSED   src/copy.rs:383:9: replace <impl AsyncWrite for BufReader<R>>::poll_shutdown ->
Poll<io::Result<()>> with Poll::from(Ok(())) in 14.2s build + 2.9s test
MISSED   src/signal.rs:88:9: replace imp::watch_signal with () in 25.6s build + 1.9s test
MISSED   src/proxy.rs:104:9: replace <impl SocketFactory for DefaultSocketFactory>::ipv6_enabled_localhost
-> io::Result<bool> with Ok(false) in 14.4s build + 2.8s test
TIMEOUT  src/xds/client.rs:233:9: replace State::notify_on_demand with () in 27.0s build + 20.0s test
MISSED   src/test_helpers/netns.rs:97:9: replace Namespace::interface -> String with String::new() in 24.8s build + 2.7s test
MISSED   src/proxy/util.rs:18:5: replace is_runtime_shutdown -> bool with false in 17.6s build + 2.8s test
MISSED   src/proxy.rs:164:9: replace <impl SocketFactory for MarkSocketFactory>::ipv6_enabled_localhost -> io::Result<bool> with Ok(false) in 26.4s build + 2.8s test
MISSED   src/xds/client.rs:241:9: replace State::add_resource with () in 22.4s build + 2.8s test
MISSED   src/inpod/packet.rs:31:33: replace | with ^ in bind in 48.0s build + 2.8s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from(Full::new())) in 21.6s build + 2.8s test
MISSED   src/test_helpers.rs:515:9: replace MpscAckSender<T>::wait -> anyhow::Result<()> with Ok(()) in 20.4s build + 2.9s test
MISSED   src/config.rs:546:29: replace > with == in construct_config in 14.5s build + 2.7s test
TIMEOUT  src/state.rs:125:31: replace == with != in WorkloadInfo::matches in 27.5s build + 20.0s test
TIMEOUT  src/test_helpers.rs:510:9: replace MpscAckSender<T>::send -> anyhow::Result<()> with Ok(()) in 19.7s build + 20.0s test
MISSED   src/inpod/statemanager.rs:50:34: delete ! in DrainingTasks::shutdown_workload in 17.2s build + 2.7s test
MISSED   src/socket.rs:85:5: replace orig_dst_addr -> io::Result<SocketAddr> with Ok(Default::default()) in 45.5s build + 2.8s test
MISSED   src/telemetry.rs:393:9: replace <impl FormatFields for IstioJsonFormat>::format_fields -> fmt::Result with Ok(Default::default()) in 25.0s build + 2.7s test
MISSED   src/main.rs:71:5: replace version -> anyhow::Result<()> with Ok(()) in 18.0s build + 2.7s test
MISSED   src/proxy/metrics.rs:235:9: replace OnDemandDnsLabels::with_source -> Self with Default::default()
in 55.2s build + 2.8s test
MISSED   src/copy.rs:204:5: replace ignore_io_errors -> Result<T, io::Error> with Ok(Default::default()) in 26.6s build + 2.7s test
MISSED   src/inpod/statemanager.rs:334:9: replace WorkloadProxyManagerState::pending_uids -> Vec<String> with vec![] in 25.5s build + 2.7s test
MISSED   src/inpod/statemanager.rs:136:20: delete ! in WorkloadProxyManagerState::process_msg in 17.3s build
+ 2.7s test
MISSED   src/readiness.rs:64:17: replace == with != in <impl Drop for BlockReady>::drop in 20.8s build + 2.7s test
MISSED   src/tls/workload.rs:263:12: delete ! in <impl ServerCertVerifier for
IdentityVerifier>::verify_server_cert in 43.6s build + 2.7s test
MISSED   src/xds.rs:281:9: replace ProxyStateUpdateMutator::remove_authorization with () in 19.4s build + 2.8s test
MISSED   src/config.rs:317:5: replace parse_args -> String with "xyzzy".into() in 22.7s build + 2.6s test
MISSED   src/xds.rs:385:28: replace < with == in <impl Handler for ProxyStateUpdater>::handle in 20.2s build
+ 2.9s test
MISSED   src/state.rs:126:13: replace && with || in WorkloadInfo::matches in 14.1s build + 2.7s test
MISSED   src/assertions.rs:26:13: replace < with == in size_between_ref in 14.1s build + 2.7s test
MISSED   src/copy.rs:140:47: replace * with + in 14.9s build + 2.7s test
MISSED   src/tls/lib.rs:54:5: replace provider -> Arc<CryptoProvider> with Arc::new(Default::default()) in 14.0s build + 2.8s test
TIMEOUT  src/identity/manager.rs:542:9: replace SecretManager::post with () in 25.8s build + 20.0s test
MISSED   src/proxy.rs:764:45: replace != with == in ipv6_enabled_on_localhost in 25.5s build + 2.6s test
TIMEOUT  src/proxy/socks5.rs:342:5: replace send_success -> Result<(), Error> with Ok(()) in 19.7s build + 20.0s test
MISSED   src/inpod/admin.rs:54:5: replace always_none -> Result<Option<ConnectionManager>, D::Error> with
Ok(None) in 23.3s build + 2.8s test
MISSED   src/xds/client.rs:533:39: replace == with != in AdsClient::run_loop in 47.8s build + 2.7s test
TIMEOUT  src/xds/client.rs:632:44: replace * with / in AdsClient::run_internal in 24.0s build + 20.0s test
MISSED   src/config.rs:81:59: replace * with + in 14.2s build + 2.9s test
​
        Trail of Bits​ 26​
Istio Ztunnel​
        PUBLIC​
​

TIMEOUT  src/identity/manager.rs:437:9: replace Worker::update_certs -> bool with false in 27.3s build + 20.0s test
MISSED   src/metrics.rs:136:9: replace <impl From for DefaultedUnknown<String>>::from -> Self with
Default::default() in 26.6s build + 2.8s test
MISSED   src/test_helpers/app.rs:79:5: replace with_app with () in 17.9s build + 2.8s test
MISSED   src/config.rs:550:30: replace - with + in construct_config in 22.7s build + 2.7s test
MISSED   src/xds.rs:292:9: replace <impl Handler for ProxyStateUpdater>::handle -> Result<(),
Vec<RejectedConfig>> with Ok(()) in 53.4s build + 2.9s test
MISSED   src/inpod/config.rs:193:9: replace <impl SocketFactory for
InPodSocketPortReuseFactory>::ipv6_enabled_localhost -> std::io::Result<bool> with Ok(false) in 24.7s build
+ 2.7s test
MISSED   src/proxy.rs:554:9: replace <impl Display for TraceParent>::fmt -> fmt::Result with
Ok(Default::default()) in 18.3s build + 2.8s test
MISSED   src/test_helpers/tcp.rs:74:29: replace += with -= in run_client in 21.3s build + 3.0s test
MISSED   src/app.rs:317:5: replace init_inpod_proxy_mgr -> anyhow::Result<std::pin::Pin<Box<dyn std::future::Future<Output =()>+Send +Sync>>> with Ok(Pin::from_iter([Box::new(Default::default())])) in 14.4s build + 2.7s test
MISSED   src/time.rs:56:9: replace Converter::elapsed_nanos -> u128 with 0 in 17.5s build + 2.9s test
MISSED   src/xds.rs:187:16: delete ! in ProxyStateUpdateMutator::remove_internal in 15.7s build + 2.8s test
MISSED   src/inpod/netns.rs:100:9: replace <impl PartialEq for InpodNetns>::eq -> bool with false in 15.0s build + 2.7s test
MISSED   src/proxy/h2.rs:147:52: delete ! in <impl ResizeBufRead for H2StreamReadHalf>::poll_bytes in 14.6s build + 2.7s test
MISSED   src/admin.rs:407:5: replace handle_jemalloc_pprof_heapgen -> anyhow::Result<Response<Full<Bytes>>> with Ok(Response::from_iter([Full::from_iter([Default::default()])])) in 20.7s build + 2.9s test
TIMEOUT  src/tls/mock.rs:157:55: replace + with - in generate_test_certs in 21.0s build + 20.0s test
MISSED   src/proxy/util.rs:18:5: replace is_runtime_shutdown -> bool with true in 18.4s build + 2.8s test
MISSED   src/app.rs:317:5: replace init_inpod_proxy_mgr -> anyhow::Result<std::pin::Pin<Box<dyn std::future::Future<Output =()>+Send +Sync>>> with Ok(Pin::new()) in 24.5s build + 2.8s test
MISSED   src/test_helpers.rs:69:8: delete ! in can_run_privilged_test in 14.1s build + 2.8s test
MISSED   src/metrics.rs:110:9: replace DefaultedUnknown<RichStrng>::display -> Option<DisplayValue<&str>> with None in 26.6s build + 2.7s test 1841 mutants tested in 8h 29m 27s: 418 missed, 584 caught, 789 unviable, 50 timeouts
Figure E.1: cargo mutants results

​
        Trail of Bits​ 27​
Istio Ztunnel​
        PUBLIC​
​

F. Fix Review Results
When undertaking a fix review, Trail of Bits reviews the fixes implemented for issues identified in the original report. This work involves a review of specific areas of the source code and system configuration, not comprehensive analysis of the system.
On February 18, 2025, Trail of Bits reviewed the fixes and mitigations implemented by the
Ztunnel team for the issues identified in this report. We reviewed each fix to determine its effectiveness in resolving the associated issue.
In summary, of the three issues described in this report, Ztunnel has resolved all issues. For additional information, please see the Detailed Fix Review Results below.
ID
Title
Severity
Status 1
No automated process for updating vulnerable dependencies
Medium
Resolved 2
Code paths that trigger error conditions are not tested
Informational
Resolved 3
HTTP forwarded header parser not fuzz tested
Informational
Resolved

​
        Trail of Bits​ 28​
Istio Ztunnel​
        PUBLIC​
​

Detailed Fix Review Results
TOB-ZTN-1: No automated process for updating vulnerable dependencies
Resolved in PR 1400. This PR adds support for Dependabot, which opens PRs to update vulnerable dependencies.
Running cargo audit on Ztunnel’s current main branch (as of February 18, 2025; commit b2939cd) indicates one warning—use of the unmaintained instant crate—as opposed to the three vulnerabilities and three warnings that were reported when the issue was written
(see appendix B).
TOB-ZTN-2: Code paths that trigger error conditions are not tested
Resolved. The client has reviewed the cargo mutants results shown in appendix E and has determined that the gaps in coverage highlighted by these results apply to test code and to code that does not affect correctness.
TOB-ZTN-3: HTTP forwarded header parser not fuzz tested
Resolved in PR 1418. This PR drops the dependency on the http-types crate, and introduces a custom-written HTTP forwarded header parser. It also introduces a fuzzing harness to test this parser.

​
        Trail of Bits​ 29​
Istio Ztunnel​
        PUBLIC​
​

G. Fix Review Status Categories
The following table describes the statuses used to indicate whether an issue has been sufficiently addressed.
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
The issue has been sufficiently resolved.

​
        Trail of Bits​ 30​
Istio Ztunnel​
        PUBLIC​
​

About Trail of Bits
Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high-­end security research with a real­-world attacker mentality to reduce risk and fortify code. With 100+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
We maintain an exhaustive list of publications at https://github.com/trailofbits/publications, with links to papers, presentations, public audit reports, and podcast appearances.
In recent years, Trail of Bits consultants have showcased cutting-edge research through presentations at CanSecWest, HCSS, Devcon, Empire Hacking, GrrCon, LangSec, NorthSec, the O’Reilly Security Conference, PyCon, REcon, Security BSides, and SummerCon.
We specialize in software testing and code review projects, supporting client organizations in the technology, defense, and finance industries, as well as government entities. Notable clients include HashiCorp, Google, Microsoft, Western Digital, and Zoom.
To keep up with our latest news and announcements, please follow @trailofbits on Twitter and explore our public repositories at https://github.com/trailofbits. To engage us directly, visit our “Contact” page at https://www.trailofbits.com/contact or email us at info@trailofbits.com.
Trail of Bits, Inc.​ 497 Carroll St., Space 71, Seventh Floor
Brooklyn, NY 11215 https://www.trailofbits.com​ info@trailofbits.com

​
        Trail of Bits​ 31​
Istio Ztunnel​
        PUBLIC​
​

Notices and Remarks
Copyright and Distribution
© 2025 by Trail of Bits, Inc.
All rights reserved. Trail of Bits hereby asserts its right to be identified as the creator of this report in the United Kingdom.
Trail of Bits considers this report public information; it is licensed to OSTIF under the terms of the project statement of work and has been made public at OSTIF’s request. Material within this report may not be reproduced or distributed in part or in whole without Trail of
Bits' express written permission.
The sole canonical source for Trail of Bits publications is the Trail of Bits Publications page.
Reports accessed through sources other than that page may have been modified and should not be considered authentic.
Test Coverage Disclaimer
All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and agreed-upon project plan.
Security assessment projects are time-boxed and often rely on information provided by a client, its affiliates, or its partners. As a result, the findings documented in this report should not be considered a comprehensive list of security issues, flaws, or defects in the target system or codebase.
Trail of Bits uses automated testing techniques to rapidly test the controls and security properties of software. These techniques augment our manual security review work, but each has its limitations: for example, a tool may not generate a random edge case that violates a property or may not fully complete its analysis during the allotted time. Their use is also limited by the time and resource constraints of a project.

​
        Trail of Bits​ 32​
Istio Ztunnel​
        PUBLIC​
​