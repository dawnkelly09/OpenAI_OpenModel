# PrivacyRaven: Comprehensive

Privacy Testing for Deep Learning
Suha S. Hussain

whoami
●
●
●
●
● 2

Auditing Deep Learning 3
●
●
●
●
How can this system be attacked?

Privacy Violations
Data Reconstruction
Intellectual Property
Re-identiﬁcation model extraction model inversion membership inference 4

Threat Model
PrivacyRaven implements  label-only black-box attacks.
5
Training
Dataset
Model
API
Adversary
Model Owner
Data Owner
Consumer

Affordances
●
●
●
● 6

Model Extraction

Attack Objectives
Model with High Fidelity
Model with High Accuracy
ﬁnancially motivated reconnaissance-motivated 8

A Framework for Model Extraction
Model extraction attacks can be partitioned into multiple phases.
9
Synthesis
Training
Retraining

Extract an MNIST model model = train_mnist_victim()
def query_mnist(input_data):
    return get_target(model, input_data)
emnist_train, emnist_test = get_emnist_data()
attack = ModelExtractionAttack(query_mnist, 100,
    (1, 28, 28, 1), 10,
    (1, 3, 28, 28),
    "copycat",
    ImagenetTransferLearning, 1000, emnist_train, emnist_test,
)
10
Launch an attack in under 15 lines of code

Extraction Results
●
●
●
●
● 11

Membership Inference

An Overview of Membership Inference 13
●
●
Objective: Re-identiﬁcation

A Framework for Membership Inference
Membership inference attacks can also be partitioned into multiple phases.
14
Extraction
Robustness
Training

Model Inversion

An Overview of Model Inversion 16
●
●
●
Objective: Obtain memorized data

Upcoming Features
●
●
●
●
●
●
● 17

Thank you for your time!
Are there any questions?
Repository:
github.com/trailofbits/PrivacyRaven
Contact:
suha.hussain@trailofbits.com james.miller@trailofbits.com