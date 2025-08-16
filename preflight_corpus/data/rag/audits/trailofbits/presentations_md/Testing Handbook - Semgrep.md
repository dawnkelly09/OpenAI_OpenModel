# Testing Handbook: Semgrep appsec.guide


Maciej Domański ~ Matt Schwager ~ Spencer Michaels

●
Available at
○ https://appsec.guide
○ https://github.com/trailofbits/testing-handbook
●
Written by ToB engineers, peer-reviewed & professionally edited
●
Based on actual tools used on security audits
●
References high-quality resources & papers
●
Created with support from tool developers
●
Contains guidance on CI/CD integration
●
The repo is public - we appreciate feedback
Trail of Bits Testing Handbook

Semgrep complements our audits

Semgrep tutorial in 30s 1.
Install
○
$ pip3 install semgrep
○
Also available via brew and docker 2.
Run rulesets
○
$ semgrep --config auto /path/to/code 3.
Triage bugs 👾

A quick introduction to Semgrep
●
Open-source engine and rules
○
Scan code without sharing it with third parties
●
Easy to use
○
One-line installation
○
Custom rules written in the target language
○
Scanning usually takes seconds/minutes (not hours/days)
●
Focuses on a single ﬁle
○
Cross-ﬁle support in Semgrep Pro Engine

A quick introduction to Semgrep
Semgrep Pro Engine (paid)
●
Cross-ﬁle support - for bugs spread across several ﬁles
●
Pro rules - high conﬁdence rules
●
Enterprise languages support (e.g. Apex, Elixir)
Can track data ﬂow
●
Constant propagation - tracks whether a variable has a constant value at the particular point in the program
●
Taint tracking - useful for catching injection bugs, such as cross-site scripting because of lack of sanitization
Large repository of existing rulesets
●
Free for general auditing and CI/CD
● 3rd party rules - universal rules
●
“Noisy rules” - “manual” security research
No need to build the target code
●
Great for security audits on proprietary products
Supports many languages
●
Supports over 30 languages (C#, Go, Java, Javascript,
Kotlin, Ruby, Rust, PHP, C, and more ...)
●
Implementation has varied maturity (Generally
Available/Beta/Experimental)

A quick introduction to Semgrep
●
No need to build the target code
●
Large repository of existing rules
●
Can track data ﬂow
●
Find more ideal use cases in our Testing Handbook
○ https://appsec.guide/docs/static-analysis/semgrep/#ideal-use-case

Supported technologies
●
Languages
○
Generally, Semgrep is very good for C#, Go, Java, JS, TS, Kotlin, Ruby, PHP
○
Mostly, we don’t rely on Semgrep when auditing
■
Solidity
■
C/C++
●
Generic
○
Matches generic patterns in languages it does not support (yet)
●
Structured data
○
JSON
○
YAML
■
Good for GitHub actions, Docker Compose, Kubernetes conﬁg, etc.

A quick introduction to static analysis
●
Analyze code without running it
●
Usually walks an Abstract Syntax Tree (AST)
○
Intermediate representation
○
May or may not require building the code
●
Great for:
○
Bug and error catching
○
Improving code quality
○
Continuous bug prevention (e.g. CI/CD integration)
PARSER
AST

Key Takeaways #1
●
Finds bugs
●
Just: $ semgrep --config auto path/
●
Generally ﬁnds errors within a single ﬁle
●
No need to build a code

How we use Semgrep at
●
Quickly identify low-hanging fruits with prepackaged rules
○
Using standard rulesets
■
$ semgrep --config p/default
■
$ semgrep --config p/javascript
■
See more in Semgrep Registry → https://semgrep.dev/explore

Step 4
Release rule publicly
Step 3
Reﬁne rule during our code audit process, catch false positives and negatives
Step 2
Create private Trail of Bits rule
Step 1
Semgrep rule idea!
Semgrep rule process

●
Expanding private Semgrep library
○
Allows us to identify bugs at scale
○
We gather ideas for new rules (found both in the wild and during audits)
○
Snowball-potential initiative ❄ → allows us to ﬁnd bugs more and more eﬀectively
○
Some of the rules become public
■
Semgrep Registry: https://semgrep.dev/p/trailofbits
■
Original Repository: https://github.com/trailofbits/semgrep-rules
■
$ semgrep --config p/trailofbits
How we use Semgrep at

How we use Semgrep at
●
Triaging
○
SARIF
■
$ semgrep --sarif p/default
■
SARIF Viewer extension in Visual Studio Code
■
We are releasing the SARIF Explorer soon!
●
Become a beta tester - send us an e-mail! webinar-sarif@trailofbits.com
○
Fast false positive ﬁltering
●
Ephemeral rules
○
When manually auditing code
○
Alternative to the (rip)grep & weggli
○
$ semgrep -e 'exec(...)' --lang=py

Key Takeaways #2
●
There are lots of rulesets
○
$ semgrep --config p/default
$ semgrep --config p/xss
$ semgrep --config p/trailofbits
●
Find out more rulesets in Semgrep Registry
○ https://semgrep.dev/explore
●
Use SARIF
●
Build your private rule portfolio

Example custom rule
●
Just a YAML ﬁle
●
The simplest rule:

rules:
 - id: command-injection pattern: exec.Command(...)
   message: Potential command injection languages: [go]
   severity: ERROR command-injection.yml

How to write custom rules easily
●
Use Semgrep Playground! → https://semgrep.dev/playground
○
“IDE in a browser” for writing custom Semgrep rules
○
Gives immediate feedback: a rule inspection, underlines errors, etc.
○
Share button to get unique link for a written rule with code
○
Two modes of a rule creation: simple and advanced

Basic syntax
●
Ellipses → ...
○
Allow for ﬂexible pattern matching
○
Match zero or more arguments, statements, parameters, etc.

Basic syntax
●
Metavariables → $X $Y $Z $WHATEVER
○
Match any code element, such as variables, functions, arguments, classes, etc.
○
Capture and track the use of values across a code scope
○
Can be interpolated into other parts of a rule, including other patterns

Basic syntax
●
Operators
○
Allow you to combine diﬀerent patterns, for example, logically (OR, AND, NOT)
○
“Semgrep, inform me if this speciﬁc line is in the code BUT don’t raise an error if this one line of code exist too” pattern
Find code matching this expression patterns
Logical AND of multiple patterns pattern-either
Logical OR of multiple patterns pattern-regex
Find code matching this PCRE-compatible pattern in multiline mode pattern-not
Logical NOT - remove ﬁndings matching this expression pattern-not-inside
Keep ﬁndings that do not lie inside this pattern
...
● https://appsec.guide/docs/static-analysis/semgrep/advanced/
● https://semgrep.dev/docs/writing-rules/rule-syntax/

Key Takeaways #3
●
Semgrep patterns mimic the target code
○ for (...)
○ var xyz = $WHATEVER
●
Use patterns to combine logic together
○ pattern, patterns, pattern-either, pattern-regex, pattern-inside, metavariable-regex, metavariable-pattern, metavariable-comparison, pattern-not, pattern-not-inside, pattern-not-regex ...
●
Leverage Semgrep Playground with simple & advanced mode
●
Docs: https://semgrep.dev/docs/writing-rules/rule-syntax/

Semgrep, please inform me when...
Two of those line codes exist:
if (1 < 2)
AND os.system() with any argument
So, I need a rule that requires two of the patterns to be present in the code (logical AND)
Basic syntax - Example #1
Solution: patterns

Basic syntax - Example #2
Semgrep, please inform me when...
One of the potentially dangerous functions is used:
os.system()
OR exec()
So, I need a rule that requires one of the patterns to be present in the code (logical OR)
Solution: pattern-either

Basic syntax - Example #3
Semgrep, please inform me when…
You match any IP address:
192.168.0.1, 1.1.1.1, etc.
So, I need a rule that matches speciﬁc regex pattern to be present in the code
Solution: pattern-regex

A slightly more advanced rule - Example #4
Semgrep, please inform me when… 1.
One of the potentially dangerous functions is used: evil() OR unsafe()
○
We know pattern-either from the previous example!
2.
BUT don’t throw an error if one of them has the following option: safe=True
Solution: pattern-either + pattern-not

Combining operators together
●
Sometimes it’s possible to create the same logic in diﬀerent ways
○
Carefully test Semgrep rules to identify edge-case nuances
○
The most optimized rule usually wins. See the Optimizing Semgrep Rules in our Testing Handbook
●
The order of child patterns in a patterns operator does not aﬀect the ﬁnal result
●
Read the patterns operator evaluation strategy
○ https://semgrep.dev/docs/writing-rules/rule-syntax/#patterns-operator-evalu ation-strategy

Auto ﬁx
●
Automatically ﬁx bugs found by Semgrep rules
○
No worries, you can do a dry run before
●
Speeds up the process of patching vulnerabilities
●
It’s very informative for developers
○
Shows both the bug and how to ﬁx it so devs learn what to avoid in the future
●
The fix-regex variant applies regex replacements

●
Mastering operator combinations may initially require trial and error. This is okay!
●
Leverage Semgrep Playground for testing
●
Test your rules on the real code
○
Have a couple large repositories in a speciﬁc language at hand
○ 0-days for free ↑
●
Learn from existing rules and our informative Semgrep blog posts
○ https://blog.trailofbits.com/category/semgrep/
●
Over time, rules improve and reﬁne, reducing false positives and increasing true ones
●
It’s impossible to create a universal rule that meets all standards. Some rules tend to be more noisy.
Key Takeaways #4

Semgrep in CI/CD
Semgrep in CI
Semgrep Cloud Platform
Standalone CI job setup
●
Centralized app to manage ﬁndings, conﬁgure rulesets and notiﬁcations
●
Conﬁgured by clicking elegantly in GUI
●
Free for up to 10 devs
●
Highly customizable, depending on the provider
●
Mainly based on the conﬁguration ﬁle
(like GitHub Workﬂow)
●
Free
See the full comparison: https://semgrep.dev/docs/semgrep-ci/overview/#feature-comparison

How to introduce Semgrep to your CI/CD 1.
Get acquainted with documentation related to your CI vendor
○
For example, with GitHub Actions
○
See oﬃcial Semgrep docs and our CI chapter of the Testing Handbook 2.
Incorporate incrementally - try out a pilot test ﬁrst on a repository
○
Don’t overwhelm devs with too many results
○
Use rules that provide high conﬁdence and true positive results
○
Use comments to ignore false positives:
// nosemgrep: go.lang.security.audit.xss 3.
Schedule a full Semgrep scan on the main branch 4.
Include a diﬀ-aware scanning approach when an event triggers (e.g., a pull request)
○
Scans only changes in ﬁles on a trigger
○
Maintains eﬃciency 5.
Conﬁgure Semgrep to block the PR pipeline with unresolved ﬁndings

Semgrep in CI/CD - More tips for your organization 1.
Obtain your ideal rulesets chain
○
Check out non-security rulesets, such as best practices rules
○
Cover other aspects: shell scripts, conﬁguration ﬁles, Dockerﬁles 2.
Consider writing custom rules for found bugs
○
Create an internal repository to aggregate custom Semgrep rules
○
Encourage developers to jot down ideas for Semgrep rules (e.g., on a Trello board)
3.
Create a place for the team to discuss Semgrep (e.g., a Slack channel)
○
Support for writing custom rules
○
Troubleshooting
More information in our How to introduce Semgrep to your organization blog post https://blog.trailofbits.com/2024/01/12/how-to-introduce-semgrep

Where to ﬁnd support 1.
Semgrep Community Slack
○ https://go.semgrep.dev/slack
○
Great place to ask for help with custom rule development or using the tool 2.
Semgrep GitHub Issues
○ https://github.com/semgrep/semgrep/issues
○
Report bugs
○
Suggest new features 3.
#testing-handbook channel in the Empire Hacking Slack
○ https://slack.empirehacking.nyc/
○
ToB is happy to help (:
○
Give us feedback on the Testing Handbook!

Summary
●
Testing Handbook: https://appsec.guide/
●
Check out our blog: https://blog.trailofbits.com/
○ 30 new Semgrep rules: Ansible, Java, Kotlin, shell scripts, and more
○
How to introduce Semgrep to your organization
○
Secure your Apollo GraphQL server with Semgrep
○
Secure your machine learning with Semgrep
○
Discovering goroutine leaks with Semgrep
●
Our public audit reports show how Semgrep behaves for real https://github.com/trailofbits/publications
●
ToB public Semgrep rules: https://github.com/trailofbits/semgrep-rules