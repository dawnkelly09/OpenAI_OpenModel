# 1

Never a dill moment
Exploiting machine learning pickle ﬁles

2
What is Pickling?
Pickle: module for serializing and de-serializing arbitrary Python objects
Pickling: process of converting Python object into byte stream
Unpickling: converting a byte stream back into a Python object
Allows you to serialize custom objects easily

3
Pickling Example:

4
Slicing A Pickle totally_safe_trust_me.pkl
Disassembled Pickle Opcodes
Decompiled Python Equivalent
Neighbor! Boom! Big reveal: I'm a pickle.
What do you think about that? I turned myself into a pickle! W-what are you just staring at me for, bro. I turned myself into a pickle, Neighbor!

5
Unpickling (deserialization) has its own instruction set and VM!
Can call into arbitrary Python code
Pickles are a streaming format
“Pickle bombs” have become an attack vector
Pickling is not secure

6
Machine Learning/NLP/CV Model Serialization
Do you know how pickles are stored? It’s jarring!
PyTorch, TensorFlow, spaCy, arm, scikit learn, Azure ML, theano
Pickling allows for easy serialization of custom models
Models use Python pickling and its variants
Trained models are distributed as pickle ﬁles

7
Models are Anonymously Shared Online!
Pickle ACE/RCE well known in the security community
Many ML practitioners have no CS, let alone security, background
Admonitions to “follow the warnings in the Pickle documentation,” but no direct warnings
Pretrained models often shared
Never a Dill Moment

8
Mitre Adversarial Machine Learning Threat Matrix
(ATLAS)
In which it is revealed that yet another ﬁle format contains a weird machine

9
How do we dill with it? Introducing “Fickling”
Decompiler: Pickle VM → Python AST → Human-Readable Python
Static Analyzer: Detect overtly malicious code
(e.g., use of eval, exec, os.system, subprocess.call, &c.)
Binary Rewriter:
Inject arbitrary code into an existing pickle (such as an ML model)
Open-Source: https://github.com/trailofbits/fickling pip3 install fickling
Divining the meaning of the “F” in “Fickling”: left as an exercise to the reader

10
Proof of Concept Exploits
●
Exﬁltrate local ﬁles
○
Proprietary code, proprietary models
●
Potential RCE on proprietary ML systems
○
Microsoft Azure ML (not yet tested, but plausible)
●
Add arbitrary classiﬁcation delays (DoS)
●
Replace trained model with “backdoored” model
●
Model poisoning attacks
●
Swap out model parameters or tensors
○
Time of day, time zone, system locale/language, IP address

11

12

13
ReSpOnSiBlE DiScLoSuRe
Reported to PyTorch on January 25th, received reply January 27th
“…Models linked on PyTorch Hub index are vetted for quality and utility but don't do any background checks on the people publishing the model, or carefully audit the code for security before adding a link to the github repository on the PyTorch Hub indexing page. …”
Basically, a WONTFIX
Caveat sciscitator
We relish the thought of a day when pickling will no longer be used to deserialize untrusted ﬁles

14
What Sci-Kit Learn Has to Say

15
Immediate Steps
●
If you must use pickle, use ﬁckling for safer unpickling
●
Follow best practices
○
Use the PyTorch state_dict and load_state_dict functions
●
Switch to other ﬁle formats
○
ONNX
○
PPML
○
HDF5
○
SavedModel
○
Protobuf
○
JSON
○
TF Lite
○
CoreML

16
The “Summoning Demons” Approach
●
We do need to think about novel ML attacks
○
Countferﬁt, PrivacyRaven, IBM ART, PyTorchFi
●
But these “demons” need to be “summoned”
○
Vulnerabilities in ﬁle formats, libraries, server architectures, etc.
○
ATLAS Matrix
Most importantly

17
What Should We Actually Do
●
Make 👏 our 👏 tools 👏 secure 👏 by 👏 default
●
Minimize access to the model ﬁles
○
Threat modeling is key
●
Sign models and validate signatures
○
Use model cards and incorporate this
●
Manage your the model’s lifecycle
○
MLFlow
●
Monitor your model. Audit logs
○
Detect attacks as they happen
●
Validate your inputs
●
Test your models thoroughly
○
Unit tests, property tests, fuzzing, etc.

18
Conclusions
●
Pickling is a convenient but very unsafe serialization
●
Due to its convenience, pickling has become commonplace in ML
●
This represents a serious supply chain risk to the ML community
●
We need to make our tools secure by default
We relish the thought of a day when pickling will no longer be used to deserialize untrusted ﬁles

19
Suha S. Hussain
Carson Harmon
Jim Miller
Evan Sultanik
󰳕 https://github.com/trailofbits/fickling
💬 https://empireslacking.herokuapp.com/
📄 https://www.trailofbits.com/post/never-a-dill-moment-exploiting-machine-learning-pickle-files
@suhackerr
@carsonharmon12
James.Miller
@trailofbits.com
@ESultanik

20