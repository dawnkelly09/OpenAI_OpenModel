# Using Graph-Based Machine

Learning Algorithms for
Software Analysis
ITEA Cybersecurity Workshop
Michael D. Brown 31 August 2023

Software Analysis 2
Goal: Automatically determine facts about a program’s properties and behaviors.
Used extensively in compilers, security, and reverse engineering.
Must make trade-oﬀs - impossible to collect a complete set of program facts in general / non-trivial cases.

Software Analysis 3
Many core problems cannot be solved deterministically:
●
Phase ordering
●
Precise binary decompilation
●
Declaring software vulnerability free
SoTA tools employ heuristics and / or rely on humans
Meaningful gains are few and far between despite sizable research investments.

Using ML Techniques for Software Analysis 4
Advances can be made via AI/ML:
●
AI/ML not bound by the constraints of traditional software analysis
●
Approximates human problem solving on fuzzy tasks

Using ML Techniques for Software Analysis 5
Challenges:
●
How do we represent software in a way that AI/ML techniques can ingest?
●
What is the right program representation to use?
…. and Pitfalls:
●
Easy to apply ML to unsuitable problems (soundness)
●
Can we get enough data?

Key Insights 6 1) How do we represent software in a way that these techniques can ingest?
Programs are inherently graph-like, so use existing graph-based ML algorithms

Key Insights 7 2) What is the right program representation to use?
Depends on the application!
We can use compiler / decompiler tools to convert software to the right representation for our problem.

Key Insights 8 3) What problems are suitable for ML-based software analysis?
ML systems cannot be expected to be 100% accurate:
DON’T use them when soundness is required!
Useful for many security and reversing applications – tolerant of false positives.

Applications 9 4) Can we get enough data?
Real world data is hard to
ﬁnd in volume, but…
New automated program generation tools and benchmarking datasets makes creating quality synthetic datasets realistic.

Applications 10
Two recent successes using graph-based ML over the last several years 1.
VulChecker: Scans source code for vulnerabilities 2.
CORBIN: Recover symbolic mathematics from binaries
Both tools developed under funding from DARPA I2O

VulChecker

VulChecker 12
Problem: Certain types of high-risk vulnerabilities are diﬃcult for traditional code scanners to discover. Can
ML-based systems do better?
Is this a good problem for ML? – Yes
●
No requirement for soundness – existing code scanning workﬂows produce false positives
●
Use existing benchmark datasets as training data

VulChecker Overview 13
Source Code
Vulnerability
Labels
LLVM
Compiler
Enriched Program
Dependency Graph
Graph Processing
Deployed Model
Model Training
Structure2Vec
Training
Deployment
Source Code
Vulnerability Alerts

VulChecker Data Strategy 14
Bootstrap model with NIST Juliet dataset, supplement with as many real-world samples as possible.
Juliet Dataset
• Low Fidelity – Programs are synthetic “toys”
• Low Effort – Programs are labelled with in-line comments, very straightforward to harvest
• High Contrast – Malicious and benign versions of each example
• High Volume - Thousands / CWE
Samples from CVE database
• High Fidelity – Real-world samples in complex programs
• High Effort – Engineering required to localize and scrape samples
• Low Contrast – CVE databases don’t include references to patched code
• Low Volume – Dozens at best

VulChecker Data Strategy 15
Improve synthetic sample ﬁdelity via augmentation with real-world structures
Augmentation procedure 1.
Inject nodes from synthetic samples into benign code 2.
Adjust edges to maintain control-flow and data-flow integrity
Note: Properties of the graph processing ensure non-interference for dataflows

VulChecker Data Processing int a = 0; int b = 3; if(c > 100){ b = b * a;
} else { b = a;
}
Op: Allocate
Type: Int
Val: 0
Op: Allocate
Type: Int
Val: 3
Op: Compare
Type: Int
Val: 100
Op: C Branch
Type: void
Val: None
Op: Multiply
Type: Int
Val: None
Op: Store
Type: int
Val: None
Op: Store
Type: int
Val: None
Use compiler infrastructure to convert source code to simpliﬁed enriched graph representation (ePDG)

VulChecker Training and Deployment
From larger graph structure, extract sub paths and classify as vulnerable or not vulnerable.

VulChecker Evaluation
Compared VulChecker against 4 other ML tools and commercial
SAST tool across 5 CWEs
(Train – Augmented data, Test – RW data)

CORBIN

CORBIN 20
Problem: Legacy CPS need updates to improve performance or safety. Source code not available to patch. If we can recover control loops we can re-implement ﬁrmware easily.

CORBIN 21
Is this a good problem for ML? – Yes
●
No requirement for soundness – reverse engineering workﬂows are tolerant of errors, recovered code won’t be used blindly.
●
Can generate synthetic data sets for math constructs easily
●
Diversity and complexity are open problems, however

CORBIN Overview 2222
Binary
Construct
Labels
Decompiler
(to LLVM)
Enriched Program
Dependency Graph
Graph Processing
Deployed Model
Model Training
Training
Deployment
Binary
Symbolic Mathematics

CORBIN Data Strategy 2323
Amplify small volume of real-world / SME derived samples with logical and syntactical mutations

CORBIN Data Strategy 2424
Logically mutate single zone to multi-zone controller

CORBIN Data Strategy 2525
Syntactic mutation: capture programmer induced variance

CORBIN Data Processing 2626
Uses same base approach as VulChecker, with domain-speciﬁc improvements.
Many complex mathematical functions are handled by libraries:
●
Libm
●
Lapack
In ePDG these are function call nodes – we reduce them to atomic math operations

CORBIN Training and Deployment 2727
Graph to Graph approach
●match subgraphs / nodes corresponding to mathematical constructs
●condense to symbolic representation

CORBIN Results 2828
On synthetic data holdout set:
●Strong performance across all trained constructs
●
To be expected – same production procedure from source
On autopilot software:
●Many misclassiﬁcations, some limited success
●
Limitations largely due to imprecise binary to LLVM IR lifting
Conclusion: Approach is viable – but training on source code derived samples did not transfer to binary derived samples.

Key Takeaways

Key Takeaways 1.
Problem formulation is important - our successes relied on focused feature selection.
- Unlikely to ﬁnd success directly applying models (including LLMs!)
2.
ML approaches supplement, not replace, traditional
(i.e., algorithmic) approaches.
- Prioritize problems that rely on human expertise 3.
Make synthetic data as real as possible for good results!
30

Contact 31
Michael D. Brown
Principal Security Engineer michael.brown@trailofbits.com

References/Links 32
VulChecker Paper https://www.usenix.org/conference/usenixsecurity23/presentation/mirsky
VulChecker @ Github https://github.com/ymirsky/VulChecker