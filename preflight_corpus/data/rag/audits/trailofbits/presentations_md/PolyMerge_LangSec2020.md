# Toward Automated

Grammar Extraction via Semantic Labeling of Parser Implementations
Evan Sultanik
Carson Harmon
Bradford Larsen
LangSec Workshop at IEEE Security & Privacy, May 21, 2020

The Problem

The Problem

The Problem
✓
⛔
!
#

The Problem
$

The Problem
$
✓
✓
✓
✓

%
High Level Goals
Create semantic map of the functions in a parser, which will improve grammar extraction.
&
'
???

%
High Level Goals
Create semantic map of the functions in a parser, which will improve grammar extraction.
& parser_function1
↳byte 0, 10, 50
  Object Stream parser_function2
↳byte 10, 74
  Xref parser_function3
↳byte 20
  JFIF

%
High Level Goals
Create semantic map of the functions in a parser, which will improve grammar extraction.
& parser_function1
↳byte 0, 10, 50
  Object Stream parser_function2
↳byte 10, 74
  Xref parser_function3
↳byte 20
  JFIF
Ultimate Goal: Automatically extract a minimal grammar specifying the ﬁles accepted by a parser
Hypothesis: The majority of the potential for maliciousness and schizophrenia will exist in the symmetric diﬀerence of the grammars accepted by a format’s parser implementations

Approach
Semantic Ground Truth
Instrumentation
Associative Labeling
Label the Type Composition
Hierarchy of the input ﬁles
Use universal taint analysis to track all input bytes through the execution of a parser
Merge the results of the ﬁrst two steps to produce a labeling of which functions operate on which types
Detect backtracking
Detect error handling
Diﬀerential analysis

Approach
Semantic Ground Truth
Instrumentation
Associative Labeling
Label the Type Composition
Hierarchy of the input ﬁles
Use universal taint analysis to track all input bytes through the execution of a parser
Merge the results of the ﬁrst two steps to produce a labeling of which functions operate on which types
Detect backtracking
Detect error handling
Diﬀerential analysis
✓

Approach
Semantic Ground Truth
Instrumentation
Label the Type Composition
Hierarchy of the input ﬁles
Use universal taint analysis to track all input bytes through the execution of a parser
✓
Associative Labeling
Merge the results of the ﬁrst two steps to produce a labeling of which functions operate on which types
Detect backtracking
Detect error handling
Diﬀerential analysis
Grammar Extraction
(future work)

Prior Work: Semantic Labeling
Polyglot-Aware
File Identiﬁcation
Resilient Parsing
Syntax Tree
'
???
iNES ROM
PDF
ZIP
Modify parsers for best eﬀort
Instrument to track input byte oﬀsets
Label regions of the input
Produce ground truth iNES [0x0→0x12220]
↳ Magic [0x0→0x3]
   Header [0x4→0xF]
   ⋮
   PRG [0xC210→0x1020F]
   CHR [0x10210→0x12220]
PDF [0x10→0x2EF72F]
↳ Magic [0x10→0x1E]
   Object 1.0 [0x1F→0x12221]
   ↳ Dictionary [0x2A→0x3E]
      Stream [0x3F→0x12219]
      ↳ JFIF Image [0x46→0x1220F]
         ↳ JPEG Segment […]
            ↳ Magic […]
               Marker […]
⋮

PolyFile Ground Truth
'

PolyFile Ground Truth
'

Prior Work: Parser Instrumentation
LLVM
Instrumentation
Taint Tracking
Operate on LLVM/IR
Can work with all open source parsers
Eventually support closed- source binaries by lifting to
LLVM (e.g., with McSEMA or Remill)
Shadow memory inspired by the Data Flow Sanitizer
(dfsan)
Negligible CPU overhead
O(n) memory overhead, where n is the number of instructions executed by the parser
Novel datastructure for eﬃciently storing taint labels dfsan status quo:
훩(1) lookups
훩(n²) storage
PolyTracker:
O(log n) lookups
O(n) storage

PolyTracker Instrumentation
{
  "ensure_solid_xref": [ 2276587, 2276588
  ],
  "fmt_obj": [ 2465223, 2465224, 2465225, 2465226, 2465227, 2465228, 2465240, 2465241, 2465242, 2465243, 2465244, 2465245, 2465246, 2465258, 2465259, 2465260, 2465261, 2465262
  ]
}

PolyTracker Instrumentation
{
  "ensure_solid_xref": [ 2276587, 2276588
  ],
  "fmt_obj": [ 2465223, 2465224, 2465225, 2465226, 2465227, 2465228, 2465240, 2465241, 2465242, 2465243, 2465244, 2465245, 2465246, 2465258, 2465259, 2465260, 2465261, 2465262
  ]
} iNES [0x0→0x12220]
↳ Magic [0x0→0x3]
   Header [0x4→0xF]
   ⋮
   PRG [0xC210→0x1020F]
   CHR [0x10210→0x12220]
PDF [0x10→0x2EF72F]
↳ Magic [0x10→0x1E]
   Object 1.0 [0x1F→0x12221]
   ↳ Dictionary [0x2A→0x3E]
      Stream [0x3F→0x12219]
      ↳ JFIF Image [0x46→0x1220F]
         ↳ JPEG Segment […]
            ↳ Magic […]
               Marker […]
⋮

PolyTracker Instrumentation
{
  "ensure_solid_xref": [ 2276587, 2276588
  ],
  "fmt_obj": [ 2465223, 2465224, 2465225, 2465226, 2465227, 2465228, 2465240, 2465241, 2465242, 2465243, 2465244, 2465245, 2465246, 2465258, 2465259, 2465260, 2465261, 2465262
  ]
} iNES [0x0→0x12220]
↳ Magic [0x0→0x3]
   Header [0x4→0xF]
   ⋮
   PRG [0xC210→0x1020F]
   CHR [0x10210→0x12220]
PDF [0x10→0x2EF72F]
↳ Magic [0x10→0x1E]
   Object 1.0 [0x1F→0x12221]
   ↳ Dictionary [0x2A→0x3E]
      Stream [0x3F→0x12219]
      ↳ JFIF Image [0x46→0x1220F]
         ↳ JPEG Segment […]
            ↳ Magic […]
               Marker […]
⋮
❓ fmt_obj
Object
Dictionary ensure_solid_xref
Trailer
XRef

The Challenge of
Associative Labeling
How can we associate types in the ﬁle format to the set of functions most specialized in operating on that type?
Observations
Raw mapping is not necessarily injective:
There will rarely be a perfect bijection between the types and functions
Monolithic
Function
Parser 1
Specialized
Function
Specialized
Function
Specialized
Function
Parser 2
A parser’s functional implementation will rarely be isomorphic to the type hierarchy or syntax tree of the input ﬁle

Information Entropy
• For each type, collect the functions that operate on that type
• Calculate P(t, f) = the probability that a speciﬁc type occurs within a function
• Calculate the “genericism” of a function G : F → ℝ

• Use G to sort the functions associated with a type, discarding all but the smallest (most specialized) standard deviation
Idea: Use information entropy to measure function specialization

The parser has a single function responsible for parsing multiple types
Monolithic
Function
Parser 1
Problem: Code is Too Monolithic

The parser has a single function responsible for parsing multiple types
Problem: Code is Too Monolithic
• Calculate the dominator tree of the syntax tree

The parser has a single function responsible for parsing multiple types
Problem: Code is Too Monolithic
• Calculate the dominator tree of the syntax tree

• Remove a function from the matching for a type if there exists an ancestor of the type in the dominator tree that maps to the same function

• Calculate the dominator tree of the syntax tree

• Remove a function from the matching for a type if there exists an ancestor of the type in the dominator tree that maps to the same function
The parser has a single function responsible for parsing multiple types
Problem: Code is Too Monolithic

• Calculate the dominator tree of the syntax tree

• Remove a function from the matching for a type if there exists an ancestor of the type in the dominator tree that maps to the same function
The parser has a single function responsible for parsing multiple types
Problem: Code is Too Monolithic parse_pdf_dictionary

• Calculate the dominator tree of the syntax tree

• Remove a function from the matching for a type if there exists an ancestor of the type in the dominator tree that maps to the same function
The parser has a single function responsible for parsing multiple types
Problem: Code is Too Monolithic parse_pdf_dictionary

• If those functions are always called sequentially, then we ideally only want the single function that initiates the sequence
• Calculate the dominator tree of the runtime control ﬂow graph
• For each type, remove any functions in the matching that have an ancestor in the dominator tree that is also in the matching
The parser has many, tightly coupled functions collectively responsible for parsing a single type
Specialized
Function
Specialized
Function
Specialized
Function
Parser 2
Problem: Code is Too Cohesive

• If those functions are always called sequentially, then we ideally only want the single function that initiates the sequence
• Calculate the dominator tree of the runtime control ﬂow graph
• For each type, remove any functions in the matching that have an ancestor in the dominator tree that is also in the matching
The parser has many, tightly coupled functions collectively responsible for parsing a single type
Problem: Code is Too Cohesive

pdf_load_xref pdf_read_start_xref pdf_prime_xref_index

pdf_load_xref pdf_read_start_xref pdf_prime_xref_index
PDF
XRef

pdf_load_xref pdf_read_start_xref pdf_prime_xref_index
PDF
XRef

Results
•Runs inO(|F|n log |T|) time
◦
F = # functions in the parser
◦
T = # types (or production rules) in the grammar
◦ n = # bytes in the input ﬁle
•Mappings for various parsers and ﬁle formats
•Implementation in the polymerge application distributed with
PolyFile:
◦ pip3 install polyfile

Results: MuPDF
(Generated from a single parse of a single PDF)
PDF Object
PDF Dictionary
PDF Object Version
PDF Object Content
PDF Object ID fz_isprint lex_string next_ﬂated pdf_process_stream twoway_memmem
PDF
PDF Trailer
PDF Comment fz_clamp fz_strtof pdf_load_version
Key Value Pair
Key
Value pdf_process_keyword lex_name lex_white
PDF Start XRef pdf_read_start_xref
PDF XRef pdf_read_xref_sections
FT_Stream_ReadAt pdf_show_char pdf_token_from_keyword
FT_Stream_Seek cff_index_access_element cff_slot_load fz_bound_glyph fz_bound_text fz_read pdf_read_old_xref

Results: MuPDF
(Generated from a single parse of a single PDF)
twoway_memmem
PDF
PDF Trailer
PDF Comment fz_clamp fz_strtof pdf_load_version
PDF Start XRef pdf_read_start_xref
PDF XRef pdf_read_xref_sections fz_read pdf_read_old_xref

Results: QPDF
(Generated from a single parse of a single PDF)
PDF Object
PDF Dictionary
PDF Object Version
PDF Object Content
PDF Object ID
QPDF::pipeStreamData(PointerHolder<QPDF::EncryptionParameters>, PointerHolder<InputSource>, QPDF&, int, int, long long, unsigned long, QPDFObjectHandle, bool, Pipeline*, bool, bool)
QPDFObjectHandle::getUIntValue()
PDF
PDF Trailer
PDF Comment
QPDF::ﬁndHeader()
QUtil::is_digit(char)
Key Value Pair
Key
Value
Pl_Count::write(unsigned char*, unsigned long)
QIntC::IntConverter<unsigned long, long long, false, true>::convert(unsigned long const&)
QPDFObjectHandle::getIntValue()
QPDFWriter::unparseObject(QPDFObjectHandle, int, int, unsigned long, bool)
QPDF_String::unparse[abi:cxx11](bool)
QUtil::int_to_string_base[abi:cxx11](long long, int, int)
QUtil::uint_to_string_base[abi:cxx11](unsigned long long, int, int)
QPDF_Name::normalizeName(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
PDF Start XRef
QPDF::parse(char const*)
PDF XRef
QIntC::IntConverter<long long, int, true, true>::convert(long long const&)
QPDFXRefEntry::getType() const
QPDF_Stream::setStreamDescription()
Buffer::Buffer(unsigned long)
ContentNormalizer::handleToken(QPDFTokenizer::Token const&)
Pl_Buffer::getBuffer()
Pl_Buffer::write(unsigned char*, unsigned long)
Pl_Flate::handleData(unsigned char*, unsigned long, int)
QPDF::readObject(PointerHolder<InputSource>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, int, bool)
QPDF_Dictionary::getKeys[abi:cxx11]()
QPDF_Integer::~QPDF_Integer()
std::_Rb_tree<int, std::pair<int const, long long>, std::_Select1st<std::pair<int const, long long> >, std::less<int>, std::allocator<std::pair<int const, long long> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, long long> >*)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::_Identity<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_erase(std::_Rb_tree_node<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >*)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::_Identity<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_get_insert_unique_pos(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_M_erase(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >*)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::equal_range(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >* std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_M_copy<std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_Alloc_node>(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > const*, std::_Rb_tree_node_base*, std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_Alloc_node&)
std::map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, QPDFObjectHandle, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::operator[](std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
void __gnu_cxx::new_allocator<std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::destroy<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >(std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>*)
void std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle>, std::_Select1st<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_M_construct_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> const&>(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >*, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> const&)
QPDF::read_xrefTable(long long)

Results: QPDF
(Generated from a single parse of a single PDF)
PDF Object
PDF Dictionary
PDF Object Version
PDF Object Content
PDF Object ID
QPDF::pipeStreamData(PointerHolder<QPDF::EncryptionParameters>, PointerHolder<InputSource>, QPDF&, int, int, long long, unsigned long, QPDFObjectHandle, bool, Pipeline*, bool, bool)
QPDFObjectHandle::getUIntValue()
PDF
PDF Trailer
PDF Comment
QPDF::ﬁndHeader()
QUtil::is_digit(char)
Key Value Pair
Key
Value
Pl_Count::write(unsigned char*, unsigned long)
QIntC::IntConverter<unsigned long, long long, false, true>::convert(unsigned long const&)
QPDFObjectHandle::getIntValue()
QPDFWriter::unparseObject(QPDFObjectHandle, int, int, unsigned long, bool)
QPDF_String::unparse[abi:cxx11](bool)
QUtil::int_to_string_base[abi:cxx11](long long, int, int)
QUtil::uint_to_string_base[abi:cxx11](unsigned long long, int, int)
QPDF_Name::normalizeName(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
PDF Start XRef
QPDF::parse(char const*)
PDF XRef
QIntC::IntConverter<long long, int, true, true>::convert(long long const&)
QPDFXRefEntry::getType() const
QPDF_Stream::setStreamDescription()
Buffer::Buffer(unsigned long)
ContentNormalizer::handleToken(QPDFTokenizer::Token const&)
Pl_Buffer::getBuffer()
Pl_Buffer::write(unsigned char*, unsigned long)
Pl_Flate::handleData(unsigned char*, unsigned long, int)
QPDF::readObject(PointerHolder<InputSource>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, int, bool)
QPDF_Dictionary::getKeys[abi:cxx11]()
QPDF_Integer::~QPDF_Integer()
std::_Rb_tree<int, std::pair<int const, long long>, std::_Select1st<std::pair<int const, long long> >, std::less<int>, std::allocator<std::pair<int const, long long> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, long long> >*)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::_Identity<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_erase(std::_Rb_tree_node<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >*)
std::_Rb_tree<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::_Identity<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_get_insert_unique_pos(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
har_traits<char>, std::allocator<char> > const, QPDFObjectHandle> > >::_M_construct_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> const&>(std::_Rb_tree_node<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> >*, std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, QPDFObjectHandle> const&)
QPDF::read_xrefTable(long long)

Results: QPDF
(Generated from a single parse of a single PDF)
PDF Object
PDF Dictionary
PDF Object Version
PDF Object ID
QPDF::pipeStreamData(PointerHolder<QPDF::EncryptionParameters>, PointerHolder<InputSource>, QPDF&, int, int, long long, unsigned long, QPDFObjectHandle, bool, Pipeline*, bool, bool)
QPDFObjectHandle::getUIntValue()
PDF
PDF Trailer
PDF Comment
QPDF::ﬁndHeader()
QUtil::is_digit(char)
Key Value Pair
Key
Value
Pl_Count::write(unsigned char*, unsigned long)
QIntC::IntConverter<unsigned long, long long, false, true>::convert(unsigned long const&)
QPDFObjectHandle::getIntValue()
QPDFWriter::unparseObject(QPDFObjectHandle, int, int, unsigned long, bool)
QPDF_String::unparse[abi:cxx11](bool)
QUtil::int_to_string_base[abi:cxx11](long long, int, int)
QUtil::uint_to_string_base[abi:cxx11](unsigned long long, int, int)
QPDF_Name::normalizeName(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
PDF Start XRef
QPDF::parse(char const*)
PDF XRef
QIntC::IntConverter<long long, int, true, true>::convert(long long const&)
QPDFXRefEntry::getType() const
QPDF_Stream::setStreamDescription()
ator<char> > >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_get_insert_unique_pos(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
QPDF::read_xrefTable(long long)

Results: QPDF
(Generated from a single parse of a single PDF)
PDF Object Version
PDF Object ID
PDF
PDF Trailer
PDF Comment
QPDF::ﬁndHeader()
QUtil::is_digit(char)
QIntC::IntConverter<unsigned long, long long, false, true>::convert(unsigned long const&)
QUtil::uint_to_string_base[abi:cxx11](unsigned long long, int, int)
normalizeName(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
PDF Start XRef
QPDF::parse(char const*)
PDF XRef ng long, int, true, true>::convert(long long const&)
QPDFXRefEntry::getType() const
QPDF_Stream::setStreamDescription()
QPDF::read_xrefTable(long long)

Results: libjpeg
(Generated from a single parse of a single JPEG)
JPEG File
JPEG read_markers segments consume_markers jinit_d_coef_controller jpeg_make_d_derived_tbl start_iMCU_row start_pass start_pass_main segment magic marker length image_data data
ﬁrst_marker next_marker segment_app0 segment_sof0 segment_sos num_components components version_major version_minor density_units density_x density_y thumbnail thumbnail_x thumbnail_y get_interesting_appn examine_app0 image_width image_height bits_per_sample jpeg_core_output_dimensions initial_setup master_selection start_spectral_selection appr_bit_pos end_spectral start_pass_huff_decoder component id quantization_table_id sampling_factors huffman_table default_decompress_parms latch_quant_tables

Results: libjpeg
(Generated from a single parse of a single JPEG)
start_pass segment_sof0 image_width image_height bits_per_sample jpeg_core_output_dimensions initial_setup master_selection ection

Next Step:
Grammar Extraction
•AUTOGRAM: (Zeller, et al., 2016) Uses data-ﬂow analysis
◦
No type information other than what can be inferred from native types in the code
◦
Can be improved with our type mapping from the associative labeling
•Mimid: (Zeller, et al., 2019) Uses static control-ﬂow analysis
◦
Can also be improved by our type mapping
◦
Needs to infer indirect control-ﬂow that we can deﬁnitively observe with our runtime instrumentation
•We can observe control-ﬂow events like backtracking and infer types at the same time

Future Directions
•Diﬀerential Analysis of Parsers
◦
Use graph matching to map the functions of one parser to another
◦
Automatically identify feature diﬀerences
•Diﬀerential Analysis over a Corpus of Files
◦
Not all ﬁles exercise will exercise all functionality of a parser
◦
Combine the output of multiple ﬁles (including intentionally malformed ﬁles) to maximize coverage
•Type Hierarchy Learning
◦
If there is no ground truth, learn the type hierarchy from the data structures of the parser

Conclusions
•Introduced new technique for semantically labeling types operated on by parsers
•Works with a single run of a parser on a single ﬁle
•Next step: integrate with grammar extraction
•Tools are currently available:
◦ https://github.com/trailofbits/polyfile
◦ https://github.com/trailofbits/polytracker

Contact Info
Carson Harmon
Brad Larsen
@reyeetengineer
@BradLarsen
Thanks!
Evan Sultanik

@ESultanik https://github.com/trailofbits/polyfile https://github.com/trailofbits/polytracker