# symbolically executing a fuzzy tyrant or, how to fuck literally anything a tragedy in four symbolic acts of Verdi's Nabucco


dramatis personae
[lojikil.com]
Stefan Edwards (lojikil) is not presently logged in.

- Assurance Practice Lead at Trail of Bits
- Twitter/Github/Lobste.rs: lojikil
- Works in: Defense, FinTech, Blockchain, IoT, compilers, vCISO services, threat modeling
- Previous: net, web, adversary sim, &c.
- Infosec philosopher, programming
language theorist, everyday agronomer, father.
- As heard on Absolute AppSec (multiple) and Risky
Business (No. 559).

WARNING: DEAF
WARNING: Noo Yawk

overture our traged ies:
1. prologos (Jerusalem)
2. the traditional kingdoms (The Impious Ones)
i. what are they & how do they work ii. coverage?
3. a fuzzy tyrant (The Prophecy)
i. of fuzzing and traditional testing ii. understanding property coverage 4. his symbolic execution (The Broken Idol)
i. program space & analysis ii. concolic and symbolic 3

prologos: Jerusalem this talk covers three main items:
1. how can we "do better" than traditional tooling?
2. what does this look like?
3. can we make "formal" tools more accessible?
4

prologos: Jerusalem (or, what the actual fuck, loji?)
three main take aways:
1. traditional tools have a traditional place 2. formal verification techniques are accessible for everyone 3. a rough intro to program analysis 5

prologos: Jerusalem program analysis?
programs have a "space" intended actions vs unintended many techniques to discover effectively: formalized & detailed debugging 6

prologos: Jerusalem source: Weird Machines 7

prologos: Jerusalem many, many types of "weird machines" using MOV  as a OISC on x86
Python's pickle
ROP gadgets 8

prologos: Jerusalem 9

prologos: Jerusalem more than anything: this talk is about understanding code
Malware
White/Clear box testing
Stolen/RE'd code 10

act 1: traditional testing scene 1: Traditional infosec testing techniques and their forebearance upon our understanding of systems sennet: Enter: certain traditional tools 11

a1s1: our traditional dichotomy 12

a1s1: what are they static: linters, code formatters, unsafe function checkers,...
dynamic: runners, sandboxes, various execution environments...
basically: the most simple sorts of tests possible low barrier to entry, low quality of bugs caught 13

a1s1: example code int main(void) { char *foo = nil, bar[64] = {0};

     foo = malloc(sizeof(char) * 128);

     if(!foo) {

printf("foo is nil\n");
     }

     foo = gets(foo);

     strcpy(foo, bar);

     printf("%s\n", bar);

     free(foo); return 0;
} 14

a1s1: rats 15

a1s1: rats we get two hits: gets  and strcpy fgets  rec is good strcpy  rec ... not as much about as simple as we can get code in list of findings out 16

17

a1s1: splint better: we get six hits (FP) initializer x 2, gets , NPE, potential memory leak but strcpy  tho?
still, p simple:
code in list of findings 18

a1s1: issues lots of FPs easily fooled (ever seen nopmd  in Java code?)
completely misses intent:
strcpy(foo, bar)  is wrong same for naive dynamic testing: easily fooled 19

a1s2: how they work this all goes back to how these tools work very simple models for code 20

a1s2: how they work
Splint builds a more informationally‑dense model of code 21

a1s2: how they work => coverage the model of a thing impacts what we can test int main(void) { char buf[7] = "\0\0\0\0\0\0", foo[7] = "GrrCon";

    strcpy(buf, foo);

    printf("%s\n", buf);

    return 0;
} 22

a1s3: coverage 23

a1s3: coverage (or, why do I care?)
as {program, malware, ...} analysts, we need to model our code adversaries will have decent understanding of their intent
... which we must discover 24

act 2: a fuzzy tyrant scene 1: On the differences between what is oft referred to as fuzzing and what we mean by fuzzing sennet: Enter: modern fuzzy tyrants 25

a2s1: on fuzzing traditionally: throwing random data at an app what we mean: random mutation testing, property testing can be mutated at the string level can be highly structured 26

a2s1: on fuzzing def in the toolbox: fuzzdb, SecLists, IntruderPayloads...
missing: mutation of program state remember our weird machines 27

a2s1: on fuzzing what we expect: string naive: random bytes mutation: accept valid data, and output N variants grammar: accept a definition of data, generate random data property testing: define functions, mutate data perhaps with instrumentation into program state 28

a2s1: on fuzzing the goal: greater depth of coverage beyond what humans can see results speak for themselves:
personally, 50+ significant bugs from Radamsa in 2 years afl has a repo, with at least 332 CVEs listed clearly random testing finds serious issues
... but...
29

a2s2: a fuzzy notion of coverage what do we get coverage wise?
we generate data and watch program result want: program to walk other paths get: deeply shrugging man emoji 30

a2s2: a fuzzy notion of coverage different ways to increase coverage:
reach into the binary/system (afl)
deeply specify program invariants (property testing)
newer techniques, such as grey‑box fuzzing discover new territory within a program 31

a2s2: a fuzzy notion of coverage fundamental point: we need to uncover paths programs themselves are just graphs constrained by conditions constrained by input can we discover & graph all paths?
32

act 3: his symbolic execution scene 1: my dear, the depths of your program space run far and wide, let me explore the paths and constraints of your heart as a symbol of our love sennet: Enter: a constrained guillotine 33

a3s1: program space at their hearts, programs are just graphs:
nodes represent actions edges represent constraints if(j < k) { console.log("j is less than k");
} else { console.log("j is greater  than or equal to k");
} 34

a3s1: program space 35

a3s1: program space symbolic execution (and related techniques) provide us these graphs generate graphs & constraints, then solve them by various means extremely useful for security
KLEE, Manticore, Mythril, &c 36

a3s1: program space the problem: work on binary code as malware analysts, we may not always have binary
VBA/VBScript, JScript, JavaScript, PowerShell esp. useful for uncovering hosts, second stage, &c most solutions are fancy sandboxes require complete code for execution 37

a3s1: program space decided to fix that: github.com/lojikil/uspno.9
"Unnamed Symbex Project No. 9" focus on HLLs primarily JS & VBScript works on partial code safe by default very new: began life 26 SEP 2019
Basically: an ugly Scheme‑dialect + Python Library 38

a3s2: concolic & symbolic concolic execution: execution with specific (concrete) values symbolic execution:
39

a3s2: concolic & symbolic we want to map program space tags (UUIDs) show unique locations traces show values + tags that created data 40

a3s2: concolic & symbolic but more importantly... unknown (symbolic) data 41

a3s2: concolic & symbolic but who cares? consider:
(if (variable foo ::pure-symbolic)
    (value 12 ::int trace: 12 tag: 91ac...)
    (value 13 ::int trace: 13 tag: e8ab...))
we know nothing about foo we do know sometimes we get 12, sometimes 13 42

a3s2: concolic & symbolic ask questions
PathExecution  gives a value/code under a specific true constraint
ForkPathExectution  gives us both sides of an execution path 43

a3s2: concolic & symbolic find the constraints underwhich code executes coming soon: generate reasonable strategies for the same execute code both concretely & symbolically with both micro‑execution & standard execution models 44

quick break: micro‑execution given an {env, stack, ...}, execute one instruction/form helpful for understanding impact of an instruction/form https://github.com/lifting‑bits/microx https://patricegodefroid.github.io/public_psfiles/icse2014.pdf 45

a3s2: concolic & symbolic lots to do i. flesh out the JS parser ii. fix ANF & lambda lifting iii. more tests iv. more strategies (for generation, &c)
my use: understanding constraints in gnarly code my future use: exercising them 46

fin thanks for coming questions?
47