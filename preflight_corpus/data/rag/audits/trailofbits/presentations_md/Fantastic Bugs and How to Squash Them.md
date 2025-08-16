# Fantastic Bugs and

How to Squash Them; or, the Crimes of Solidity
Evan Sultanik
@ESultanik

`whoami`

What should you take away from this talk?

• Experienced Ethereum developers
✓ Learn from the most common mistakes of your peers
✓ Learn new tooling for improving your SDLC
What should you take away from this talk?

• Experienced Ethereum developers
✓ Learn from the most common mistakes of your peers
✓ Learn new tooling for improving your SDLC
• Programmers who are new to smart contracts
✓ Learn what not to do
✓ Learn what to do
What should you take away from this talk?

• Experienced Ethereum developers
✓ Learn from the most common mistakes of your peers
✓ Learn new tooling for improving your SDLC
• Programmers who are new to smart contracts
✓ Learn what not to do
✓ Learn what to do
• People interested in the technology
✓ Learn about the state of the ecosystem
• Everyone else?
What should you take away from this talk?
Meme-O-Meter

Outline
• Solidity the Language
• Solidity Implementation and Tooling
• On the Horizon
• Bugs!
• What You Can Do About It
Hi, I’m Trippy, your programming assistant. I help you not get tripped up on Solidity.

Outline
• Solidity the Language
• Solidity Implementation and Tooling
• On the Horizon
• Bugs!
• What You Can Do About It
It looks like you are trying to write a bug- free Solidity contract…

Solidity, the Language

Programming Language Checklist by Colin McMillen, Jason Reed, and Elly Jones. 
You appear to be advocating a new:
[ ] functional  [ ] imperative  [X] object-oriented  [X] procedural [X] stack-based
[ ] "multi-paradigm"  [ ] lazy  [ ] eager  [X] statically-typed  [ ] dynamically- typed
[ ] pure  [ ] impure  [ ] non-hygienic  [ ] visual  [ ] beginner-friendly
[X] non-programmer-friendly  [ ] completely incomprehensible programming language.  Your language will not work.  Here is why it will not work.
You appear to believe that:
[ ] Syntax is what makes programming difficult
[ ] Garbage collection is free                [ ] Computers have infinite memory
[X] Nobody really needs:
    [ ] concurrency  [ ] a REPL  [X] debugger support  [ ] IDE support  [ ] I/O
    [ ] to interact with code not written in your language
[ ] The entire world speaks 7-bit ASCII
[ ] Scaling up to large software projects will be easy
[ ] Convincing programmers to adopt a new language will be easy
[ ] Convincing programmers to adopt a language-specific IDE will be easy
[ ] Programmers love writing lots of boilerplate
[ ] Specifying behaviors as "undefined" means that programmers won't rely on them
[X] "Spooky action at a distance" makes programming more fun
Your language will not work.

You appear to believe that:
[ ] Syntax is what makes programming difficult
[ ] Garbage collection is free                [ ] Computers have infinite memory
[X] Nobody really needs:
    [ ] concurrency  [ ] a REPL  [X] debugger support  [ ] IDE support  [ ] I/O
    [ ] to interact with code not written in your language
[ ] The entire world speaks 7-bit ASCII
[ ] Scaling up to large software projects will be easy
[ ] Convincing programmers to adopt a new language will be easy
[ ] Convincing programmers to adopt a language-specific IDE will be easy
[ ] Programmers love writing lots of boilerplate
[ ] Specifying behaviors as "undefined" means that programmers won't rely on them
[X] "Spooky action at a distance" makes programming more fun
Unfortunately, your language (has/lacks):
[ ] comprehensible syntax  [ ] semicolons  [ ] significant whitespace  [ ] macros
[ ] implicit type conversion  [ ] explicit casting  [X] type inference
[ ] goto  [ ] exceptions  [X] closures  [ ] tail recursion  [ ] coroutines
[ ] reflection  [X] subtyping  [ ] multiple inheritance  [X] operator overloading
[ ] algebraic datatypes  [X] recursive types  [ ] polymorphic types
[ ] covariant array typing  [X] monads  [ ] dependent types
[ ] infix operators  [ ] nested comments  [ ] multi-line strings  [X] regexes
[ ] call-by-value  [ ] call-by-name  [ ] call-by-reference  [ ] call-cc
The following philosophical objections apply:

The following philosophical objections apply:
[ ] Programmers should not need to understand category theory to write "Hello,
World!"
[ ] Programmers should not develop RSI from writing "Hello, World!"
[ ] The most significant program written in your language is its own compiler
[ ] The most significant program written in your language isn't even its own compiler
[X] No language spec
[X] "The implementation is the spec"
   [ ] The implementation is closed-source  [ ] covered by patents  [ ] not owned by you
[X] Your type system is unsound  [X] Your language cannot be unambiguously parsed
   [X] a proof of same is attached
   [ ] invoking this proof crashes the compiler
[ ] The name of your language makes it impossible to find on Google
[ ] Interpreted languages will never be as fast as C
[ ] Compiled languages will never be "extensible"
[ ] Writing a compiler that understands English is AI-complete
[ ] Your language relies on an optimization which has never been shown possible
[ ] There are less than 100 programmers on Earth smart enough to use your language
[ ] ____________________________ takes exponential time
[ ] ____________________________ is known to be undecidable
Your implementation has the following flaws:
[ ] CPUs do not work that way
[ ] RAM d t k th t

Your implementation has the following flaws:
[ ] CPUs do not work that way
[ ] RAM does not work that way
[ ] VMs do not work that way
[X] Compilers do not work that way
[ ] Compilers cannot work that way
[ ] Shift-reduce conflicts in parsing seem to be resolved using rand()
[ ] You require the compiler to be present at runtime
[ ] You require the language runtime to be present at compile-time
[X] Your compiler errors are completely inscrutable
[X] Dangerous behavior is only a warning
[ ] The compiler crashes if you look at it funny
[ ] The VM crashes if you look at it funny
[X] You don't seem to understand basic optimization techniques
[X] You don't seem to understand basic systems programming
[ ] You don't seem to understand pointers
[ ] You don't seem to understand functions
Additionally, your marketing has the following problems:
[ ] Unsupported claims of increased productivity
[ ] Unsupported claims of greater "ease of use"
[ ] Obviously rigged benchmarks
   [ ] Graphics, simulation, or crypto benchmarks where your code just calls handwritten assembly through your FFI

Additionally, your marketing has the following problems:
[ ] Unsupported claims of increased productivity
[ ] Unsupported claims of greater "ease of use"
[ ] Obviously rigged benchmarks
   [ ] Graphics, simulation, or crypto benchmarks where your code just calls handwritten assembly through your FFI
   [ ] String-processing benchmarks where you just call PCRE
   [ ] Matrix-math benchmarks where you just call BLAS
[ ] Noone really believes that your language is faster than:
    [ ] assembly  [ ] C  [ ] FORTRAN  [ ] Java  [ ] Ruby  [ ] Prolog
[ ] Rejection of orthodox programming-language theory without justification
[ ] Rejection of orthodox systems programming without justification
[ ] Rejection of orthodox algorithmic theory without justification
[ ] Rejection of basic computer science without justification
Taking the wider ecosystem into account, I would like to note that:
[ ] Your complex sample code would be one line in: _______________________
[ ] We already have an unsafe imperative language
[ ] We already have a safe imperative OO language
[ ] We already have a safe statically-typed eager functional language
[ ] You have reinvented Lisp but worse
[X] You have reinvented Javascript but worse
[ ] You have reinvented Java but worse
[ ] You have reinvented C++ but worse
[ ] You have reinvented PHP but worse

    [ ] assembly  [ ] C  [ ] FORTRAN  [ ] Java  [ ] Ruby  [ ] Prolog
[ ] Rejection of orthodox programming-language theory without justification
[ ] Rejection of orthodox systems programming without justification
[ ] Rejection of orthodox algorithmic theory without justification
[ ] Rejection of basic computer science without justification
Taking the wider ecosystem into account, I would like to note that:
[ ] Your complex sample code would be one line in: _______________________
[ ] We already have an unsafe imperative language
[ ] We already have a safe imperative OO language
[ ] We already have a safe statically-typed eager functional language
[ ] You have reinvented Lisp but worse
[X] You have reinvented Javascript but worse
[ ] You have reinvented Java but worse
[ ] You have reinvented C++ but worse
[ ] You have reinvented PHP but worse
[ ] You have reinvented PHP better, but that's still no justification
[ ] You have reinvented Brainfuck but non-ironically
In conclusion, this is what I think of you:
[X] You have some interesting ideas, but this won't fly.
[X] This is a bad language, and you should feel bad for inventing it.
[X] Programming in this language is an adequate punishment for inventing it.

In conclusion, this is what I think of you:
[X] You have some interesting ideas, but this won't fly.
[X] This is a bad language, and you should feel bad for inventing it.
[X] Programming in this language is an adequate punishment for inventing it.

if(1 | 0 < 1) {
    /* case 1 */
} else {
    /* case 2 */
}

if(1 | 0 < 1) {
    /* case 1 */
} else {
    /* case 2 */
}
C, C++, Javascript, Java, …

if(1 | 0 < 1) {
    /* case 1 */
} else {
    /* case 2 */
}
C, C++, Javascript, Java, …
Solidity
LEEEROYYY JENKINS!
Such Language!
Much Bugs!
WOW!

if(1 | 0 < 1) {
    /* case 1 */
} else {
    /* case 2 */
}
C, C++, Javascript, Java, …
Solidity
LEEEROYYY JENKINS!
Such Language!
Much Bugs!
WOW!
Lesson: Don’t assume
Solidity behaves like most other languages!

for (var i = 0; i < foo.length; ++i) {
    foo[i] = i;
}
What does foo[1337] look like after this?

for (var i = 0; i < foo.length; ++i) {
    foo[i] = i;
}
What does foo[1337] look like after this?
Lesson: Always use explicit types!

How to Write a Solidity Parser
(1) ☕
(2) Look up the oﬃcial grammar

How to Write a Solidity Parser
(1) ☕
(2) Look up the oﬃcial grammar
(3) "
(4) Struggle to get a parser generator to accept it

How to Write a Solidity Parser
(1) ☕
(2) Look up the oﬃcial grammar
(3) "
(4) Struggle to get a parser generator to accept it
(5) #
(6) Discover that the grammar is not correct

How to Write a Solidity Parser
(1) ☕
(2) Look up the oﬃcial grammar
(3) "
(4) Struggle to get a parser generator to accept it
(5) #
(6) Discover that the grammar is not correct
(7) $
(8) Discover that existing parsers were #YOLO’d by hand

How to Write a Solidity Parser
(1) ☕
(2) Look up the oﬃcial grammar
(3) "
(4) Struggle to get a parser generator to accept it
(5) #
(6) Discover that the grammar is not correct
(7) $
(8) Discover that existing parsers were #YOLO’d by hand
(9) % ⚰

One Does Not Simply
Implement the Shunting Yard Algorithm

One Does Not Simply
Implement the Shunting Yard Algorithm 1 | 0 < 1

contract C{
    struct myStruct{
        function(uint) my_func;
    }
    
    function test(){
        myStruct m;
        
        m.my_func = call_log;
        m.my_func(0);
        
        m.my_func = call_log2;
        m.my_func(0);
    }
    
    function call_log(uint a){
        Log(a);
    }
    
    function call_log2(uint a){
        Log2(a);
    }
    
    event Log(uint);
    event Log2(uint);
}

contract C{
    struct myStruct{
        function(uint) my_func;
    }
    
    function test(){
        myStruct m;
        
        m.my_func = call_log;
        m.my_func(0);
        
        m.my_func = call_log2;
        m.my_func(0);
    }
    
    function call_log(uint a){
        Log(a);
    }
    
    function call_log2(uint a){
        Log2(a);
    }
    
    event Log(uint);
    event Log2(uint);
}
Solidity Spec.
Solidity Compiler a struct that contains a pointer to a function

contract C{
    struct myStruct{
        function(uint) my_func;
    }
    
    function test(){
        myStruct m;
        
        m.my_func = call_log;
        m.my_func(0);
        
        m.my_func = call_log2;
        m.my_func(0);
    }
    
    function call_log(uint a){
        Log(a);
    }
    
    function call_log2(uint a){
        Log2(a);
    }
    
    event Log(uint);
    event Log2(uint);
}
Solidity Spec.
Solidity Compiler a struct that contains a pointer to a function
Lesson: The sole, canonical reference for
Solidity is the source code of its sole compiler.

Another interesting challenge we found to parse Solidity was that the language uses the same symbol (comma) as a separator for expression lists but also as an operator for the expression itself. … This causes a serious problem because when the parser ﬁnds a comma in the input it does not know if it is an operator for the current expression (matching the Expression rule) or a separator to the current expression and the beginning of a new one
(matching ExpressionList). This is a potential problem for any parser due to the ambiguity of matching either rule when encountering a comma.
the ambiguity of matching either rule when encountering a comma.
This is a potential problem for any parser due to

…we found out that Solidity’s type system is far from being safe with respect to any type of error:
in many occasions, contract interfaces are not consulted at compile-time, and this makes the execution raise an exception and the user waste money.

Solidity
Implementation and Tooling

The diﬀerence between an amateur and a professional is: you write your own compiler.

16 Block Trace 18,538 invocations of EXP by Martin Holst Swende
Well over half were calculating 160 raised to the power of 1
Martin’s GitHub proﬁle pic:
⏱ 4m 18538x4
=~25% 20000x16

16 Block Trace 18,538 invocations of EXP by Martin Holst Swende
Well over half were calculating 160 raised to the power of 1
Martin’s GitHub proﬁle pic:
⏱ 4m 18538x4
=~25% 20000x16
Lesson: Solidity is bad at optimization, but getting better, kinda
(more on this later)

Exponentiation: How does it work?
// We need cleanup for EXP because 0**0 == 1, but 0**0x100 == 0
Using the ** operator with an exponent of type shorter than 256 bits can result in unexpected values.

Exponentiation: How does it work?
// We need cleanup for EXP because 0**0 == 1, but 0**0x100 == 0
Using the ** operator with an exponent of type shorter than 256 bits can result in unexpected values.
Lesson: The compiler is still immature

Things Are Improving

Things Are Improving
Changing

Things Are Improving
Changing
Adapted from https://xkcd.com/1428/
SOLIDITY DEV

Things Are Improving
Changing
Adapted from https://xkcd.com/1428/
SOLIDITY DEV
Lesson: Expect breaking changes during the course of your project!

Upgradable Contracts

Upgradable Contracts
(
(
)
01010101

Upgradable Contracts
(
(
)
11111100 01010101
*
*

Upgradable Contracts
(
(
)
11111100 01010101
*
*
Lesson: If you absolutely have to use the DELEGATECALL proxy upgrade pattern, then you must always make sure the storage layout of your new contract matches the old one!

Backward Compatibility?

0.4.24 .sol
Backward Compatibility?
Solidity 0.5.0

0.4.24 .sol
Backward Compatibility?
Solidity 0.5.0

⋮

⋮

⋮
Lesson: Use solc-select!

Optimizations are Dangerous
• Compiler optimization still in active development
• Independent compiler audit in November of 2018 concluded optimizations are dangerous
• Numerous high severity bugs related to the optimizer, many excluded from the changlog
• There are likely latent bugs

Optimizations are Dangerous
• Compiler optimization still in active development
• Independent compiler audit in November of 2018 concluded optimizations are dangerous
• Numerous high severity bugs related to the optimizer, many excluded from the changlog
• There are likely latent bugs
Lesson: Don’t turn on solc optimizations unless you really, really know what you are doing

On the Horizon

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
All of this has happened before … and will happen again.

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
The “If” production rule is never used!
All of this has happened before … and will happen again.

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
The “If” production rule is never used!
The default switch case isn’t followed by a ‘:’
All of this has happened before … and will happen again.

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
The “If” production rule is never used!
The default switch case isn’t followed by a ‘:’
“switch foo” is a legal production in this grammar
All of this has happened before … and will happen again.

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
The “If” production rule is never used!
The default switch case isn’t followed by a ‘:’
“switch foo” is a legal production in this grammar
StringLiteral can’t be represented without casting
All of this has happened before … and will happen again.

They’re Proposing a New
Intermediate Representation, YUL
Block = '{' Statement* '}'
Statement =
    Block |
    FunctionDefinition |
    VariableDeclaration |
    Assignment |
    Expression |
    Switch |
    ForLoop |
    BreakContinue
FunctionDefinition =
    'function' Identifier '(' TypedIdentifierList? ')'
    ( '->' TypedIdentifierList )? Block
VariableDeclaration =
    'let' TypedIdentifierList ( ':=' Expression )?
Assignment =
    IdentifierList ':=' Expression
Expression =
    FunctionCall | Identifier | Literal
If =
    'if' Expression Block
Switch =
    'switch' Expression Case* ( 'default' Block )?
Case =
    'case' Literal Block
ForLoop =
    'for' Block Expression Block Block
BreakContinue =
    'break' | 'continue'
FunctionCall =
    Identifier '(' ( Expression ( ',' Expression )* )? ')'
Identifier = [a-zA-Z_$] [a-zA-Z_0-9]*
IdentifierList = Identifier ( ',' Identifier)*
TypeName = Identifier | BuiltinTypeName
BuiltinTypeName = 'bool' | [us] ( '8' | '32' | '64' | '128' | '256' )
TypedIdentifierList = Identifier ':' TypeName ( ',' Identifier ':' TypeName )*
Literal =
    (NumberLiteral | StringLiteral | HexLiteral | TrueLiteral | FalseLiteral) ':'
TypeName
NumberLiteral = HexNumber | DecimalNumber
HexLiteral = 'hex' ('"' ([0-9a-fA-F]{2})* '"' | '\'' ([0-9a-fA-F]{2})* '\'')
StringLiteral = '"' ([^"\r\n\\] | '\\' .)* '"'
TrueLiteral = 'true'
FalseLiteral = 'false'
HexNumber = '0x' [0-9a-fA-F]+
DecimalNumber = [0-9]+
The “If” production rule is never used!
The default switch case isn’t followed by a ‘:’
“switch foo” is a legal production in this grammar
StringLiteral can’t be represented without casting
All of this has happened before … and will happen again.
SlithIR
EVM::SSA

Solidity Alternatives
• Even more immature
• Lack of security tooling
• Diﬀerent semantics!

Bugs!

Compiler Warnings

Compiler Warnings
Warning: “throw” is deprecated in favour of “revert()”,
“require()” and
“assert()”

Compiler Warnings assert;
+

Compiler Warnings

Reentrancy

Reentrancy
,

Reentrancy
, Deploy Attack Contract

Reentrancy
, pwn()

Reentrancy
, pwn()

Reentrancy
, pwn()

Reentrancy
, pwn()

Reentrancy
, pwn()

Reentrancy
, pwn()

Reentrancy
, pwn()
Lesson: Use the
“checks, effects, interactions” pattern!

)
)
Malicious External Calls
,
-

)
)
Malicious External Calls
,
-

)
)
Malicious External Calls
,
-

)
)
Malicious External Calls
,
-
Lesson: Don’t trust external contracts!

Zero Initialization

Zero Initialization

Zero Initialization
Lesson: Unlike in most other languages, uninitialized keys will result in uninitialized memory, which is zeroed.

Array Length Manipulation

Array Length Manipulation
Lesson: Never manually manipulate the length of an array!

Transaction “Frontrunning”
(
)
01010101

Transaction “Frontrunning”
(
)
01010101
.

Transaction “Frontrunning”
(
)
01010101
.

Transaction “Frontrunning”
(
)
01010101
/
.0 1

Transaction “Frontrunning”
(
)
01010101
/
.
.

Transaction “Frontrunning”
(
)
01010101
/
.
.

Transaction “Frontrunning”
(
)
01010101
/
*
.
.
2

Transaction “Frontrunning”
(
)
01010101
/
*
.
.
Lesson: Transactions are public, and aren’t guaranteed to be mined in order 2

Randomness
• The blockchain does not provide any cryptographically secure source of randomness
‣ Block hashes are random, but miners can manipulate them
‣ Miners can also inﬂuence timestamps

Randomness
• The blockchain does not provide any cryptographically secure source of randomness
‣ Block hashes are random, but miners can manipulate them
‣ Miners can also inﬂuence timestamps
• Everything in a contract is publicly visible
‣ Random numbers can’t be generated until after all lottery entries have been recorded

Randomness
• The blockchain does not provide any cryptographically secure source of randomness
‣ Block hashes are random, but miners can manipulate them
‣ Miners can also inﬂuence timestamps
• Everything in a contract is publicly visible
‣ Random numbers can’t be generated until after all lottery entries have been recorded
• Computers will always be faster than the blockchain
‣ Any number a contract could generate can be pre- calculated oﬀ-chain faster

Don’t try to be clever with number theory

Don’t try to be clever with number theory winner = entries[blockHash % entries.length];

Everybody with me!
You can’t do random on a blockchain

Everybody with me!
You can’t do random on a blockchain
Lesson: If you really need randomness, use a trusted off-chain oracle.

Pre-Signed Transfers

Pre-Signed Transfers
Lesson: Always check the return value of ecrecover!
Better yet, avoid it!

What Can You Do
About It?

What can be done?
Buy our free, open source products.
https://github.com/trailofbits/…
Manticore Symbolic Execution
Slither Static Analysis
Echidna Property Based Fuzzer
Rattle EVM to SSA Lifter
Etheno Test Framework Integration
Ethersplay Visual EVM Disassembler pyevmasm Bytecode Analysis evm-opcodes
VM Reference not-so-smart-contracts common vulnerability database awesome-ethereum-security security best practices blockchain-security-contacts it’s surprisingly hard to disclose bugs

(Not So) Smart Contracts
Educational Tool
Learn about EVM and Solidity Vulnerabilities
Working Examples of Contracts
Real Vulnerabilities Found in the Wild
Reference Material
Useful when Auditing Code https://github.com/crytic/not-so-smart-contracts

• What? Comprehensive list of security contacts for blockchain applications
• Why? Projects worth $10MM+ should have a way to engage with security researchers
• Features
‣ Vuln disclosure program best practices
‣ Deployed addresses template for dapps
‣ Existing contact info for over 100 projects (Blockchains, dapps, ERC20 and 721 tokens, Exchanges, Wallet software)
Community Information
• What? Curated list of community- maintained and open-source references
• Why? Everything in one place: no more searching through stack overﬂow, github, and reddit
• Features
‣ Resources for secure development,
CTFs & wargames, and even speciﬁc podcast episodes
‣ Identiﬁes security tools for visualization, linting, bug ﬁnding, veriﬁcation, and reversing
‣ Pointers to related communities
Awesome Ethereum Security
Blockchain Security Contacts https://github.com/crytic/awesome-ethereum-security and /blockchain-security-contacts

• Inputs: Solidity code
• Outputs:
‣ Detected errors (extensive list of vulnerability detectors included)
‣ Warnings of poor coding practices
‣ Inheritance graph and contract summary
Slither
Smart Contract Static Analysis
• Solidity and Vyper vulnerability detection
• Low false positives
• Easily integrates into CI pipeline
• Very fast (milliseconds)
• Supports advanced value- and taint-tracking
• Python-based detector API https://github.com/crytic/slither
Slither is open source!

Slither Installation and Usage
$ pip3 install slither-analyzer then
$ slither contract.sol or
$ truffle compile; slither .
That’s literally it!

Slither Installation and Usage
$ pip3 install slither-analyzer then
$ slither contract.sol or
$ truffle compile; slither .
That’s literally it!
Lesson: Slither is super easy and quick! No excuse not to integrate it in your CI pipeline.

Problem: Test for New Bugs contract Simple { function f(uint a){
        // .. lot of paths and conditions

        if (a == 65) {
           // leads to a bug here
        }
    }
}

Problem: Test for New Bugs contract Simple { function f(uint a){
        // .. lot of paths and conditions

        if (a == 65) {
           // leads to a bug here
        }
    }
}
It looks like you want to detect classes of bugs that have never been seen before!

• Inputs: Solidity code and tests
• Outputs:
‣ List of invariants Echidna was able to violate
‣ Minimal call sequence to trigger discovered violations
Echidna
Smart Contract Property Tester
• Generates and execute many contract inputs
• Generate intelligent, grammar-based inputs
• Seamlessly integrate into developer workﬂows
• Run thousands of generated inputs per second
• Automatically generate minimal testcases
• Highly extensible via Haskell API https://github.com/crytic/echidna
Echidna is open source!

Echidna Example

Echidna Example
Lesson: Echidna is not as fast as Slither, but it is still quick enough to be useful in your CI pipeline. Unlike Slither, it is capable of discovering wholly new classes of bugs.

• Inputs: Solidity code (optional) or raw
EVM bytecode
• Outputs:
‣ List of detected ﬂaws
‣ Veriﬁed properties
‣ Execution traces of discovered paths
Manticore
Smart Contract Veriﬁer
• Uses symbolic execution of EVM
• Deeply explores possible contract states across multiple transactions and contracts
• Discover functions directly from bytecode
• Detect contract ﬂaws like int overﬂows, uninitialized memory/storage usage, and more
• Verify customized program assertions
• Highly scriptable and extensible via Python
API https://github.com/trailofbits/manticore
Manticore is open source!

contract Simple { function f(uint a){
        // .. lot of paths and conditions

        if (a == 65) { revert();
        }
    }
}
Manticore Example

contract Simple { function f(uint a){
        // .. lot of paths and conditions

        if (a == 65) { revert();
        }
    }
}
$ manticore simple.sol 2018-02-28 17:06:21,650: [25981] m.main:INFO: Beginning analysis 2018-02-28 17:06:21,803: [25981] m.ethereum:INFO: Starting symbolic transaction: 1 2018-02-28 17:06:22,098: [25981] m.ethereum:INFO: Generated testcase No. 0 - REVERT 2018-02-28 17:06:23,185: [25981] m.ethereum:INFO: Generated testcase No. 1 - REVERT 2018-02-28 17:06:24,206: [25981] m.ethereum:INFO: Finished symbolic transaction: 1 | Code Coverage: 100% |
Terminated States: 3 | Alive States: 1 2018-02-28 17:06:24,213: [32058] m.ethereum:INFO: Generated testcase No. 2 - STOP 2018-02-28 17:06:25,269: [25981] m.ethereum:INFO: Results in /examples/mcore_zua0Yl
Manticore Example

contract Simple { function f(uint a){
        // .. lot of paths and conditions

        if (a == 65) { revert();
        }
    }
}
$ manticore simple.sol 2018-02-28 17:06:21,650: [25981] m.main:INFO: Beginning analysis 2018-02-28 17:06:21,803: [25981] m.ethereum:INFO: Starting symbolic transaction: 1 2018-02-28 17:06:22,098: [25981] m.ethereum:INFO: Generated testcase No. 0 - REVERT 2018-02-28 17:06:23,185: [25981] m.ethereum:INFO: Generated testcase No. 1 - REVERT 2018-02-28 17:06:24,206: [25981] m.ethereum:INFO: Finished symbolic transaction: 1 | Code Coverage: 100% |
Terminated States: 3 | Alive States: 1 2018-02-28 17:06:24,213: [32058] m.ethereum:INFO: Generated testcase No. 2 - STOP 2018-02-28 17:06:25,269: [25981] m.ethereum:INFO: Results in /examples/mcore_zua0Yl
Manticore Example
Manticore can verify that your code satisfies its invariants, but it can take a long time to run!

Conclusions
• Solidity isn’t a great language, but we’re stuck with it (for now)
• Don’t assume Solidity behaves like a “normal” language
• Don’t trust the Solidity documentation; the sole compiler implementation is canon
• Don’t enable Solidity compiler optimizations
• Avoid the “DELEGATECALL” upgrade pattern
• Don’t trust calls to external contracts
• Remember that everything on the blockchain is public
• Don’t assume transactions will be mined in order (or at all!)
• Read “(Not So) Smart Contracts”
• Add Slither and Echidna into your CI pipeline
• Use Manticore to verify the correctness of your contracts

Thanks!
@ESultanik

Acknowledgements
Et pl. al.
Ryan Stortz
Jay Little
Josselin Feist
Stefan Edwards
JP
@withzombies
@computerality
@montyly
@lojikil
@japesinator
Thanks!
@ESultanik