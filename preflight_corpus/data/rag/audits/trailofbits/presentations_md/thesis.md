# EXPLOITING PROCESSOR SIDE CHANNELS TO

ENABLE CROSS VM MALICIOUS CODE EXECUTION
By
Sophia M. D’Antoine
A Thesis Submitted to the Graduate
Faculty of Rensselaer Polytechnic Institute in Partial Fulﬁllment of the
Requirements for the Degree of
MASTER OF SCIENCE
Major Subject: COMPUTER SCIENCE
Approved by the Examining Committee:
Professor B¨ulent Yener, Thesis Adviser
Professor Boleslaw Szymanski
Professor David Spooner
Rensselaer Polytechnic Institute
Troy, New York
April 2015
(For Graduation May 2015)

c⃝Copyright 2015 by
Sophia M. D’Antoine
All Rights Reserved ii

CONTENTS
LIST OF FIGURES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
vi
ACKNOWLEDGMENT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
viii
ABSTRACT
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ix 1. INTRODUCTION
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1 2. HARDWARE MEDIUMS IN CLOUD COMPUTING
INFRASTRUCTURE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4 2.1
Standard Cloud Computing Architecture . . . . . . . . . . . . . . . .
4 2.2
Properties of Shared Hardware Resources Used in Side Channel Attacks 8 2.3
Analysis of Transmission and Reception Techniques used across Side
Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12 2.3.1
Central and Graphics Processing Units as a Side Channel Medium 15 2.3.2
The Cache Tiers as a Side Channel Medium . . . . . . . . . .
17 2.3.3
The I/O, Memory and Other System Buses as a Side Channel
Medium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20 2.3.4
The Main Memory and the Dynamic RAM as a Side Channel
Medium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22 2.3.5
The Hard Disk, Including the Disk Drive and Virtual RAM as a Side Channel Medium
. . . . . . . . . . . . . . . . . . . . .
23 2.4
Classiﬁcation of Hardware Units and the Transmitting Methods Used
Across . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24 3. MALICIOUS APPLICATIONS ACROSS THE SIDE CHANNEL MODEL 26 3.1
Characteristics of Malicious Side Channel Use . . . . . . . . . . . . .
27 3.2
Exﬁltration Applications . . . . . . . . . . . . . . . . . . . . . . . . .
30 3.2.1
Continuously Active Receiver, No Transmitter . . . . . . . . .
30 3.2.2
Continuously Active Receiver, One Way Transmitter
. . . . .
31 3.3
Inﬁltration Applications
. . . . . . . . . . . . . . . . . . . . . . . . .
32 iii

3.3.1
Continuously Active Transmitter, No Receiver . . . . . . . . .
32 3.3.2
Continuously Active Transmitter, One Way Receiver
. . . . .
33 3.4
Network Applications . . . . . . . . . . . . . . . . . . . . . . . . . . .
34 3.4.1
Continuously Active Transmitter and Receiver . . . . . . . . .
34 3.5
Summary of Three Architecture Models . . . . . . . . . . . . . . . . .
35 3.6
Summary of Channel Architecture Models . . . . . . . . . . . . . . .
36 4. FORMALIZATION OF THE HARDWARE SIDE CHANNEL MODEL . .
37 4.1
Models to Represent Hardware Side Channels
. . . . . . . . . . . . .
37 4.2
Tuple Representing a Hardware Side Channel
. . . . . . . . . . . . .
40 4.3
Channel Construction
. . . . . . . . . . . . . . . . . . . . . . . . . .
41 5. HARDWARE SIDE CHANNEL IMPLEMENTATION
. . . . . . . . . . .
44 5.1
Out of Order Execution
. . . . . . . . . . . . . . . . . . . . . . . . .
44 5.2
Exploiting Out of Order Execution
. . . . . . . . . . . . . . . . . . .
45 5.3
Transmitting and Receiving Processes . . . . . . . . . . . . . . . . . .
47 5.4
Construction of Seven Attacks . . . . . . . . . . . . . . . . . . . . . .
50 5.5
Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53 5.5.1
Success . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53 5.5.2
Eﬃciency
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53 5.5.3
Detectability
. . . . . . . . . . . . . . . . . . . . . . . . . . .
54 5.6
Description of Implemented Attacks and Results . . . . . . . . . . . .
56 5.6.1
M1 Theft of Encryption Key . . . . . . . . . . . . . . . . . . .
56 5.6.2
M2 Active Program Identiﬁcation . . . . . . . . . . . . . . . .
60 5.6.3
M3 Environment Keying . . . . . . . . . . . . . . . . . . . . .
63 5.6.4
M4 Signal Trigger of Process . . . . . . . . . . . . . . . . . . .
66 5.6.5
M5 CPU Resource Contention . . . . . . . . . . . . . . . . . .
69 5.6.6
M6 Determine VM Co-Location . . . . . . . . . . . . . . . . .
72 5.6.7
M7 Bi-Way Communication . . . . . . . . . . . . . . . . . . .
75 5.7
Summary of Implementation Measurements
. . . . . . . . . . . . . .
78 iv

6. APPLICATION AND POTENTIAL OF INTRUSION
DETECTION TECHNIQUES . . . . . . . . . . . . . . . . . . . . . . . . .
80 6.1
Anomaly-Based Channel Malware Detection . . . . . . . . . . . . . .
81 6.2
Signature-Based Channel Malware Detection . . . . . . . . . . . . . .
83 6.3
Pattern-Based Channel Malware Detection . . . . . . . . . . . . . . .
83 6.4
Inherent Strengths of Hardware Side Channels Against Detection
. .
84 6.5
Potential of Detection Techniques against Side Channel Attacks . . .
86 7. CONCLUSION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
LITERATURE CITED
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91 v

LIST OF FIGURES 2.1
The hardware organization of the xeon family multi-core processors
. .
5 2.2
The diﬀerences in cache architecture between industry multi-core pro- cessing units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7 2.3
Memory hierarchy of related hardware components . . . . . . . . . . . .
12 2.4
Physical resource allocation between virtual instances on a cloud server 14 2.5
Hardware component organization on a multiprocessor server . . . . . .
17 2.6
Primary system buses and their functionality . . . . . . . . . . . . . . .
21 2.7
Mechanisms used to transmit and receive across diﬀerent hardware units 25 3.1
The three permutations of the two processes used in side channel con- structions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27 4.1
A bit stream, with each time frame and its average measurement repre- senting a single bit
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42 5.1
Two threads depicting possible results of the swap . . . . . . . . . . . .
46 5.2
The store instructions in both receiver threads; the second move requires a reorderable load in the processor . . . . . . . . . . . . . . . . . . . . .
49 5.3
A complete diagram of the diﬀerent stages of a deployed attack in a live, cloud computing environment
. . . . . . . . . . . . . . . . . . . . . . .
51 5.4
The encrypted string compared to the leaked string
. . . . . . . . . . .
59 5.5
The bit stream leaked through the receiver showing the repeating pattern associated with running videos in chrome . . . . . . . . . . . . . . . . .
62 5.6
Use of the central processor in synced, concurrent time frames allows the transmission of a signal between two colluding applications in real time 67 5.7
The array values before and after computation . . . . . . . . . . . . . .
71 vi

5.8
The black virtual machine represents the malicious host and the gray virtual machine represents the alternate continual transmitter . . . . . .
73 5.9
A botnet which uses n bots that receive commands and transmit re- sponses to the central authority; our side channel acts as the relay . . .
77 5.10
A table listing the average deploy rate for each of the seven attacks im- plemented as well as the associated standard deviations . . . . . . . . .
78 5.11
A chart visualizing the execution rate of each implementation and the minimum times necessary for each attack’s success . . . . . . . . . . . .
79 6.1
The set of detection techniques applicable to the seven attack categories deployed across the out-of-order-execution side channel
. . . . . . . . .
82 vii

ACKNOWLEDGMENT
I would like to thank Professor Yener for advising me through my master’s thesis.
Jeremy Blackthorne for introducing me to this area of research. Dan Guido and Alex
Sotirov from Trail of Bits for providing me technical resources.
viii

ABSTRACT
Given the rise in popularity of cloud computing and platform-as-a-service, vulnera- bilities inherent to systems which share hardware resources will become increasingly attractive targets to malicious software authors.
This thesis ﬁrst classiﬁes the possible mediums for hardware side channel construction.
Then we construct potential adversarial models associated with each. Additionally, a novel side channel is described and implemented across the central processing unit using out of order execution.
Finally, this thesis constructs seven adversarial applications, one from each adver- sarial model. These applications are deployed across a novel side channel to prove existence of each exploit. We then analyze successful detection and mitigation tech- niques of the side channel attacks.
ix

1. INTRODUCTION
Modern cloud computing services employ the use of shared hardware between diﬀerent virtual machine instances in order to increase eﬃciency and decrease cost. However, when hardware resources, such as the cache [1, 2, 3], are dynamically allocated to dif- ferent virtual machine processes, a single virtual machine can continuously measure artifacts from its virtual allocation of a single hardware component and note changes it did not cause.
This allows the resident of one virtual machine instance to detect changes in the system caused by another virtual machine located on the same physical hardware.
This information leakage allows an adversary to construct a side channel attack used to either record coresident behavior or communicate with a process purposefully gen- erating these system changes [3, 4].
In covert side channels, a receiving software process is used to measure information from the unintentionally accessible hardware component. In the same way, a sending, software processes, located on a diﬀerent virtual machine, provides this information across the hardware resource. In this way, the privacy provided by virtually allocation is bypassed.
The ﬁrst section of this thesis presents a classiﬁcation of the diﬀerent shared hard- ware resources which may be exploited by a virtual machine process. We attempt to organize the diﬀerent characteristics of each hardware medium to acquire the trans- mitting features used in a side channel construction.
1

2
Using these features, we analyze and compare the varied aspects of side channels built across diﬀerent mediums to extract successful and limiting features.
Using these shared hardware mediums, this thesis then presents seven primary mali- cious attack models which may be applied across side channels built on each outlined hardware mediums. The distinctions between each are made according to the meth- ods in which the processes attempts to attack co-resident virtual machines over a side channel, with the intent to extract or alter system information. Together, the mali- cious attack models encompass all malicious channel behaviors. Under each model, speciﬁc malicious processes can be categorized.
Each adversarial model is then analyzed for its potential across diﬀerent hardware side channel architectures, presenting a formalization based on the transmission and reception functions of the channel. Cross applying the set of malicious program mod- els on the set of hardware mediums, outlined in the ﬁrst section, results in all pairs of attack vectors. We then analyze each pair for its applicability in real world cloud computing environments.
Finally, we implement a subset of the malicious program model, hardware medium pairs, targeting all pairs which use the central processing unit as the exploited hard- ware medium.
Using the processor, a novel side channel is constructed. Speciﬁcally, out of order execution is exploited to transmit and receive signals. We explore the use of this information as a channel through which malicious programs can operate covertly.
Provided a sender,receiver, and message encoding schema we can create an eﬀective attack vector with calculable success.

3
We discuss each malicious program implemented across the processor side channel in order to acquire insight into the scope of a hypothetical adversary on a cloud computing infrastructure.

2. HARDWARE MEDIUMS IN CLOUD COMPUTING
INFRASTRUCTURE
Hardware side channels in cloud computing infrastructures rely on shared physical resources as the medium through which information is transferred. To do so, diﬀerent variables unique to the targeted hardware component may be queried, measured or altered by the side channel processes residing on a virtual machine instance.
As the information gathered is speciﬁc to processes using the queried hardware com- ponent, a malicious virtual machine instance may only leak information from other co-resident virtual machines instantiated on the same shared hardware. Any infor- mation gained about a targeted, coresident VM may be polluted with noise caused by any number of benign coresident VM’s.
This section attempts to ﬁrst detail the hardware architecture found in cloud centers, categorize the hardware mediums found in these infrastructures, and cursory explain how side channel processes use them to transmit or receive information.
2.1
Standard Cloud Computing Architecture
In the industry standard for cloud computing infrastructure, a large physical hard- ware system is virtually allocated across a multi-core platform. This virtual allocated of hardware resources increases the eﬃciency of large scale computation for infras- tructure as a service (Iaas).
4

5
As a result, multiple virtually allocated machines share processor time and memory space on a mutually held physical machine. For the sake of this thesis, the assumed architecture of the physical machine will belong to Intels Xeon family.
Depicted in Figure 2.1, is the physical organization of the hardware components which comprise a standard cloud computing server. Previous research done in the
ﬁeld of cloud security and hardware side channels have focused on this model as it best represents the largest market share for Infrastructure-as-a-Service (IaaS) [5, 6].
Figure 2.1: The hardware organization of the xeon family multi-core pro- cessors
Speciﬁcally, this hardware model includes a shared L2 cache across multiple cores and, in some units, an larger L3 cache shared across all processing units (CPUs).

6
In modern, multi-core systems an increased number of multi-tiered caches are added to overall reduce latencies incurred by time consuming queries to main memory. Such latencies are measurable on the order of several hundred nanoseconds. On average using this structure, for each memory access query, the processor saves time on a scale of two to three orders of magnitude.
Additionally, the multiple cores and processors allow for multi-threaded applications to be executed simultaneously. The diagrams depicted in Figure 2.2 represents how the organization of cache levels for multi-core processing units can vary across hard- ware provider; the Intel Core Duo, Xeon will be the reference point for this thesis’s discussion of security and exploitable side channels.
The Intel Core Duo, Xeon processor contains an even share of shared and unshared memory. Shared memory between processors leads to contention of cache tiers used to store data. For programs running multiple threads with algorithmically complex op- erations across multiple cores, these shared cache tiers are optimal. Programs which do not gain much eﬃciency from shared cache include those which run simultaneous operations on exclusive sets of data.
In cloud computing environments, each virtual machine instance of a customers ma- chine on the physical hardware unit is managed through a hypervisor. This hypervisor acts as a resource scheduler to dynamically allocate the performance equivalent of a single, full processing core (CPU) for the duration requested. This allocation may span across several cores and cache units on the same server if other co-located pro- cesses require more of a resource.

7
Figure 2.2: The diﬀerences in cache architecture between industry multi- core processing units
Multiple virtual machine instances allocated simultaneously are not guaranteed to be co-located on the same shared server. The notion of co-location is the primary element in the success of any hardware based, side channel attack vector [7, 4, 8].
Diﬀerent hardware components of a server, applicable to side channel attacks, shared virtually and modiﬁable by the user, are discussed further in the section below.

8 2.2
Properties of Shared Hardware Resources Used in Side
Channel Attacks
The ﬁrst required property for extracting information from across a cloud computing side channel is location. The third part provider must provision the computing re- sources for the malicious and targeted virtual machine on the same physical unit. The adversarial instance must reside on the same server as the target instance in order to extract target information from the hardware component. For this reason, the most thorough security protection against side channel attacks implemented over a trusted third-party cloud infrastructure is the complete physical isolation of all equipment and hardware for the guaranteed instances. This thesis assumes that there is a sin- gle, unique hypervisor on each server to dynamically divide resources between virtual machines. For attacks targeting cloud computing, the use of the Xen hypervisor du- plicates the cloud environment for all side channel research discussed below.
A product of commercial cloud infrastructures, is the randomization of virtual ma- chine placement adding an additional layer of security. There is only a percentage of chance that the target instance and the malicious instance are placed on the save physical server containing the necessary multi-core microprocessors.
To construct a fully operational side channel attack, we ﬁrst determine if the controlled virtual machine is co-resident with the target. If not, a new instance may be created and tested. This technique is repeated until co-residence is determined. The important function of this technique is the ability for a virtual machine to realize it has achieved co-residency.

9
The research done by RSA labs and University of North Carolina Chapel [7] intro- duced the HomeAlone system which allows a virtual instance to verify its exclusive residency on a physical machine. There technique may be used to determine if a virtual machine is co-residing with another and thus susceptible to a side channel attack, speciﬁcally through exploitation of the shared L2 cache.
For their defensive purposes, a virtual machine veriﬁes that there is no foreign in- stances residing on the hardware. This machine pre-arranges for the ´friendly´ınstances to withhold from cache usage in a pre-determined time frame. During this time, the defensive machine measures an artifact of the shared L2 cache. Any unexpected ac- tivity divulges the presence of an unwanted resident. There are rare limitations to this model, such as an opponent which can withhold cache usage during the period of measurement. However, the general application of this technique, using a variety of heuristics, is highly eﬀective.
Another method used to establish co-residency, a consumer is allowed to purchase a virtual instance on demand and the cloud service provider multiplexes many in- stances across shared hardware [4]. In this work, various side eﬀects of the multiplex- ing system, such as networking speed, proximity and addresses, are exploited to verify co-residency on the same server with a high measurable accuracy. This work found that purchasing an instance immediately after the target, in the same geographical region, highly increased the probability of sharing resources.
In ﬁgure 2.4, a representation can be seen of the co-residency of n virtual instances in a cloud computing server. Also depicted is the allocation, based on client operations, of physical resources by virtualized slices of memory and processor time. The various shared and un-shared cache levels are not shown in this simpliﬁed diagram.

10
The consideration of these two methods does not exclude other potential methods to determine co-residency but merely highlights two broad techniques, measuring hardware and network heuristics. Once the co-location of the adversarial and the target virtual machine instances can be veriﬁed, the side channel attacks discussed in the subsequent sections can be constructed.
The second property, required for implementing a side channel across virtual ma- chines, is shared memory and cores, multiplexing. In cloud environments however this is enabled by default as it is a more proﬁtable setup, allowing the provider to meet the unique constraints of the virtual machines computation. The Xen hypervi- sor must be set to share time-slices of the available CPUs between all virtual guest instances on the server, potentially overbooking the amount of virtual CPUs. As this is the current standard in cloud computing infrastructure, for the scope of this thesis, the Xen architectural model will be assumed.
A feature of this model is the dynamic interplay between memory retrieval, caching and instruction execution slices of the hardware components. When these resources are shared, a single instance can now dynamically aﬀect and react to the surrounding environment; an environment which contains other virtual machine instances.
The third property required for implementing successful, virtual machine side chan- nels is that the channel activity should have a low delta from any benign user activity.
While this property is not a requirement for a functioning channel, it indicates to- wards the deployability of the side channel attack across a live cloud computing infrastructure. A successful channel will use operations that are both non-invasive

11 and non-unique. The invasiveness can be measured in excess resources used outside of any normal operating levels. For example, a system which conveys a message between two virtual machines by ﬁlling the entire cache would be considered highly invasive.
The reality of this channel on a real system communicating without detection is im- probable in that the other co-located machines, deprived of any space in the cache, would catch the attention of the service provider. Limitations on cache use would eﬀectively mitigate the side channel.
The ideal channel must also be non-unique. For example, a channel which relies on routinely using a certain cache address or spiking the processor’s load demonstrates behavior which is highly anonymous. The ideal channel, to avoid rapid detection and hypervisor resource access rules, uses a commonly accessed hardware medium.
A component which supports more active and sporadic behavior allows the channel activity and resource accesses to become statistically insigniﬁcant.
If these three primary system properties are met for any chosen hardware component and side channel attack, then it has the potential for successfully relaying information when deployed across a real world cloud computing system.

12 2.3
Analysis of Transmission and Reception Techniques used across Side Channels
Each physical component which is shared between virtual machines is potentially ex- ploitable for use in a side channel, with varying degrees of success. In order to better analyze the possibilities, we consider all hardware components of a server.
This section discusses each hardware component in order to assess what feature pro- vides the transmission and reception mechanisms.
These features, speciﬁc to the medium, make up part of the side channel´s characteristics, eﬀecting its potential. In
ﬁgure 2.5, the major components of the larger computational environment are shown.
These are the diﬀerent units which will be referenced in this thesis as distinct trans- mitting mediums.
Figure 2.3: Memory hierarchy of related hardware components

13
Figure 2.3 shows a standard memory hierarchy of four hardware units used in mem- ory management. They are shared between the co-residing virtual machine instances.
As speed increases, capacity decreases. The majority of side channels exploit this inherent speed characteristic.
A single virtual machine measuring data retrieval times can discover on which compo- nent of the hierarchy its information is located. This capability is in fact not meant to be hidden and is legitimately used by many programs to optimize operations. How- ever, when hardware is shared, it may become a mechanism to determine location of not only personal data but also the behavior of the co-residing virtual instances.

14
Figure 2.4:
Physical resource allocation between virtual instances on a cloud server

15 2.3.1
Central and Graphics Processing Units as a Side Channel Medium
One of the shared resources, used in side channel attacks, is the processors. This may include the central processing unit, the graphics processing unit, or both as long as the graphical processor is allocated for the purpose of general purpose computing.
The use of the graphics processor to increase computation speed makes its use as a potential side channel in cloud computing even more relevant.
Speciﬁcally, the graphics processor unit (GPU) has a massively paralleled architecture consisting of smaller, more eﬃcient cores designed for handling multiple tasks simultaneously mak- ing it better ﬁt to handle high loads. Using this processor over the central processing unit makes sense in multi-cored, parallel computing.
An information leak from the use of GPGPU (General Purpose GPU computing)
is exploited to leak an AES key through research by Roma Tre University, [9], which exploits the resource managers necessary for GPGPU. The resource managers, CUDA
(by NVIDIA) and OpenCL (by AMD), are used to interface with the graphics proces- sor and to direct its use for computation. These platforms generate system artifacts in speed and memory which may be leveraged as a side channel by an attacker.
Speciﬁcally, the CUDA architecture provides the system with shared memory, global memory, and registers available to the executing processes. This leads to cross vir- tual machine contention of these resources, resulting in information leakage between instances.
The central processing unit has been widely researched as a vector for side chan- nel attacks in cloud infrastructure. The same methods to detect changes in system time and memory can be used for sending signals across the CPU as with the GPU.

16
A side channel over the central processing unit is developed in research by Prince- ton University [10] where the CPUs functional units or FUs, are exploited through a simultaneous multi-threaded process (SMT). Additionally, basic timing attacks are shown across shared processors[11] .
A single central processing unit has a set of functional units which are to be dy- namically allocated to each process running as a SMT thread every cycle. The basis of the covert channel lies in these shared functional units. One process intentionally alters its use of the functional units in predetermined time intervals in order to inter- fere with other processes. When this resource contention occurs, a malicious process is able to discern artifacts from the environment.
The implementation of this side channel relies on measured time, the time it takes for a process to be allocated the appropriate functional units. Execution time will either slow or speed up depending on the state of the allocation. This makes measured time the transmitting vector for signaling between the isolated virtual machines. A proposed security defense against this channel is a selective partitioning solution in which resource sharing is minimized, adding noise and overhead to the system.
For both the graphical and central processor, time, as an eﬀective measurement of resource allocation, enables information leakages across shared hardware. Side Chan- nels developed using this technique are termed covert timing channels and may be constructed across hardware mediums besides the processors.

17 2.3.2
The Cache Tiers as a Side Channel Medium
There are three tiers of cache common in cloud computing servers, the L1, L2, and
L3, each with varied memory space and distance from the the processor. We recog- nize that Amazon cloud services now oﬀer premium C4 instances which run on Intels latest Xeon E5-2666 v3, Haswell, processors.
This new server provides an additional fourth tier of cache memory, L4. However, for the purposes of this thesis, all speciﬁc discussion of cache will address the common architecture only including L1, L2 L3.
Figure 2.5:
Hardware component organization on a multiprocessor server
As these tiers only diﬀer in size and location, cache based side channel techniques developed against speciﬁc tiers of cache apply to all tiers with varied speeds.

18
In general, cache provides high speed memory access for the processing unit as an in- termediary stage before much slower memory requests to main memory are required.
The diﬀerent tiers are labeled according to speed, L1 being the fastest and closest to the processor, and LN being the slowest and farthest away.
L1 provides the quickest and most expensive memory access, as it uses static RAM or SRAM cells. Additionally, L1 cache tiers are tied to a single core on standard multi-core processors as can be seen in Figure 2.5.
The L2 cache tier has become private, dynamically allocated memory, focused on a single processor and its set of cores. Similar to the dynamic partitioning and archi- tecture of the L2, the L3 cache tier acts as a shared pool of memory common to all processing units on a system-on-a-chip (SoC). Higher quantities of L3 cache, and L2 cache, provide faster shared memory for virtual machines and multi-threaded (SMT)
applications.
An adversary can take advantage of these shared resources through contention, mem- ory probing, or preemption in order to leak valuable system information with the intention of forming a side channel.
While L1 cache is tied to a single core, virtualized allocation of a single core be- tween processes or machine instances means the L1 cache is as well. This dynamic sharing becomes a mechanism to measure system artifacts.
Speciﬁcally, the L1 cache is vulnerable to a prime-probe technique. This was used to construct a covert timing channel to exploit the L1 cache and extract an ElGamal

19 decryption key from the co-resident, target virtual instance [12]. A simple program can be implemented which ﬁlls a section of the cache associated with a given oﬀset on each page, a technique called priming. A listening, malicious virtual machine would then query this cache section of the L1 cache page, a technique called probe. The time it takes to querying the cache acts as the transmitted signal.
The addition of diﬀerent methods, such as preemption of the resource scheduler, add speed and accuracy to the channel. However, for all variations of side channel methods, time remains the fundamental measuring unit of a single bit.
Constructing side channels across the L2 cache vary in technique and precision, yet they depend on a prime-probe or preemption technique and use time to distinguish system changes.
A variant on the prime-probe transmitting technique, forcing cache misses can be used by a malicious virtual instance across the L2 cache tier to leak useful environ- ment information [3].
A malicious process may exploit the translation lookaside buﬀer, TLB, and its limited mapping into the L2 cache. This TLB contains only a fraction of the addresses needed to decrease the speed of translating virtual addresses. Accessing all pages known to be in the L2 cache forces a TLB miss. This L2 side channel has a lower bandwidth than a comparable prime-probe channel across the L1 cache given the diﬀerence in proximity to the processor. This utilization of timed memory queries across the L2 cache is identical to timing channels across all cache tiers. The L3 cache oﬀers shared memory pages between processors and dynamically resized virtual cache allocations.
These shared memory pages creates an attack vector to record useful environment

20 artifacts [13].
One such constructed channel relies on pages, shared on the L3 cache tier, and suc- cessfully leaked the private key from the GnuPG implementation of RSA [13]. A malicious virtual instance ﬂushes a line of memory from the cache hierarchy and waits a set time frame. Then the malicious process queries the line and times how long the response takes.
If the victim instance queried the line, then the attacker now knows exactly what data the victim was accessing. This channels bandwidth relies on the granularity of the chosen time frame, sacriﬁcing accuracy for speed.
For cache tiers, L1, L2, and L3, the measurement of time, speciﬁcally memory access time, is the key reception mechanism. Optimizations of the query algorithm may increase bandwidth, but essentially they still rely on querying time or values.
2.3.3
The I/O, Memory and Other System Buses as a Side Channel
Medium
The system buses are necessary for high speed data transfers between diﬀerent mem- ory or computational units. There are several diﬀerent times of buses, as can be seen below in Figure 2.6. Each bus transports diﬀerent types of data via its bus line and connects the appropriate units.

21
Figure 2.6: Primary system buses and their functionality
These buses are required for physical communication between computing units and are shared across all virtual machine instances on the server. A side channel can be built using any of the shared buses to leak system behavior.
For example, a side channel may be constructed using memory bus contention [14].
This channel measures possible access to the memory bus as the unit to record a binary signal. To force a signal, atomic instructions from the x86 instruction set may be used, by a transmitting application, to block uncached data access through the memory bus.
Eﬀectiveness of this channel relies on locking all processors out of an essential hard- ware component, the memory bus. This greatly increases the possibility for detection in contrast to the timing based side channel used over other transmission mediums.
As many processes accessing the memory bus increase contention, the resulting chan- nel is subject to frequent interference and a great level of environment noise.

22 2.3.4
The Main Memory and the Dynamic RAM as a Side Channel
Medium
The main memory is physically located much farther from the processors than the cache resulting in a larger access latency. However, a side channel may be developed with moderate success across diﬀerent segments of the main memory.
Measurement of a pre-determined data segment in shared main memory reliably leaks environment information. The mechanism used to force contention of this shared data segment varies between speciﬁc implementations of the channel.
A side channel may be constructed to target memory paging one systems supporting
SMT. Paging occurs as a result of a process requiring more memory than what is available. The system scheduler then pages these processes and corresponding data between main memory and the disk. A transmitting process can force paging by
ﬁlling the main memory. A listening process can measure the shared address space allocated by the system. This measurement leaks the intentional memory use of the coresiding process which is then mapped to a binary signal.
A side channel can be implemented to exploit main memory on cloud servers, speciﬁ- cally the dynamic random access memory or DRAM [15]. A malicious virtual process may measure a value from a memory address on the DRAM. This value may or may not be accessed immediately, leaking whether or not that speciﬁc memory address was used by another process. The success or failure of a query may then be mapped to a binary signal. In channels built across this hardware unit, memory contention is used as the transmitting mechanism.

23 2.3.5
The Hard Disk, Including the Disk Drive and Virtual RAM as a
Side Channel Medium
Co-residing virtual instances eﬀectively share physical hard disk space while being virtually isolated. These virtual machines eﬀectively force or monitor hard disk space contention to transmit a signal. By measuring ﬁle read times, a process can record whether or not the ﬁle was operated on by another process and form a successful side timing channel. This method may be used for transmitting and receiving and is a variation of the prime-probe technique [4].
Added optimizations to timing channel, such as symbol and frame synchronization between processes, resulted in a one thousand times increased the bandwidth [16].
The basis of this channel relies on rapidly accessing ﬁles in a known locations on the hard disk. This forces ﬁle contention with other processes accessing them. A sim- ple side channel is constructed from this contention. A mutli-threaded, transmitting process quickly accesses a chosen set of ﬁles while the receiver tries to access them with varied read times. The physical disk drive segments, once ﬁlled, cannot be as easily re-purposed as the temporary memory units. Additionally, any disk read times will be slower inherently than read times of the other memory units as it is physically farther from the processor. These two characteristics of the disk drive results in a lower potential bandwidth.
Exploitation of any physically shared, but virtually allocated resource can lead to successfully measuring information from a computation environment. When these measured changes are caused intentionally by a co-residing virtual instance, recep- tion of a transmitted message is possible and the construction of a side channel.

24 2.4
Classiﬁcation of Hardware Units and the Transmitting
Methods Used Across
Each hardware unit’s functionality results in speciﬁc constraints speciﬁc which aﬀect how a side channel can be constructed across it. The data, found in Figure 2.7, out- lines the mechanisms through which transmission and reception of data occurs.
The category, Transmitting Mechanism, describes a side channels technique to force a behavior in a given hardware medium.
Under this category, there are two pri- mary techniques, resource contention and prime-probe. Resource contention occurs with the forced contention of a hardware units shared functionality or storage ca- pacity. When the transmitter controls a segment of a unit’s resource, the receiver may measure limited access to that resource. Prime-probe occurs when a transmitter manipulates data stored in a segment of the resource.
The category, Reception Mechanism, describes a side channels reception technique to measure behavior from a given hardware medium.
Under this category, there are two primary techniques, measuring time and memory access. Measuring time to record a signal relies on an arranged time frame in which the measurement will be taken as well as an expected measurement value. This means that any noise in the system which increases latency in resource access will negatively eﬀect the signal.
Measuring memory access to record a signal has less susceptibility to system noise. A receiving process can than access this memory segment and analyze the received data.
Cloud computing server architecture shares physical resources between virtualized instances which include ﬁve major, distinct hardware units listed in Figure 2.7.

25
Each of these units may act as mediums across which co-resident, virtual machines construct a side channel using a transmitting and receiving mechanism to commu- nicate. Unique programming implementations of transmitting and receiving mecha- nisms may diﬀer for each physical unit. The table in Figure 2.7 lists which mechanisms apply across diﬀerent physical units.
This section provides an organization of possible side channel hardware mediums as well as fundamental transmitting and receiving mechanisms which may be applied in speciﬁc malicious applications.
Figure 2.7:
Mechanisms used to transmit and receive across diﬀerent hardware units

3. MALICIOUS APPLICATIONS ACROSS THE SIDE
CHANNEL MODEL
With the increasing number of side channel attacks developed across the diﬀerent hardware components shared in cloud environments
[17, 18, 19], this section at- tempts to classify potential attacks speciﬁcally tailored to exploit these side channels.
The prerequisite for any side channel is the ability to transmit and receive information by exploiting speciﬁc hardware components - such as the cache, the processors, etc.
The attack models described must reduce down to a transmission and a reception mechanism.
A “transmitter” alters a exploited hardware component in a repeatable way, gen- erating an artifact which the receiver measures from the same medium. For example, to generate a signal across a cache based side channel, a transmitter may alter the data available in the cache. A “receiver” can then query a targeted location and meaningfully compared results from this query to expected ones.
This simpliﬁed model of a transmission and a reception process reduces the possi- ble set of malicious functions which could be carried out across a chosen side channel.
This section focuses on categorizations for malware types contained in this possible set. While prior research will be used to exemplify the categorizations made, this section will not pursue a detailed analysis of all malware types, but only those types relevant to side channels. With a typology of malicious behaviors which exploit side channels, it is possible to further analyze documented attack vectors as well as po- tential novel attacks.
26

27
This section assumes a symmetric multiprocessing system, a modern virtual machine manager, a exploitable hardware side channel and an optimized algorithm to max- imize bandwidth across the channel. The categories described are abstracted from speciﬁc side channel implementations so as to be applicable to a larger set of processes.
Figure 3.1:
The three permutations of the two processes used in side channel constructions 3.1
Characteristics of Malicious Side Channel Use
This section presents three classes to organize the malicious behavior which is possible across side channels. These categorizations are meant to capture all types of malicious applications, both traditional and novel, which rely on a hardware based side channel.
The “exﬁltrate” and “inﬁltrate” categories, seen in Figure 3.1, have a distinct one way property. This means that either the sending or the receiving process of the side channel is under continual operation in the system environment. The remaining process is not the focus of the application and is either never used or used only once, independent of the surrounding system activity.

28
The “network” category has a bi-way property and relies on continually operating sending and receiving processes in order to eﬀect or record system activity.
The ﬁrst category, exﬁltrate, refers to malicious applications which are constructed with the intent of exﬁltrating system data or information. Processes in this cate- gory rely on the receiving process, where information is received through reaction to changes in the environment. Continuous operation of these reactive applications allow the adversary to eﬀectively record the system changes over a given time period.
When there is no transmitting process running, the receiving processes is reacting only to the artifacts of the targeted co-resident processes.
This record of shared hardware activity over a targeted medium can be mapped to known patterns, exﬁltrating co-resident operations and information. For example, a coresident virtual machine running encryption operations will require cache resources in a pattern mappable to the encryption operations. The co-resident, receiving pro- cess setup to operate over a cache based side channel will react in a pattern similar to those of the victims encryption and can subsequently exﬁltrate the encryption key
[3, 20].
This category also encompasses malicious application functions which include a minor role for a transmission process. In these situations, the transmitter pre-agrees on a time frame with the receiver and is co-resident. The transmitter aﬀects the hardware medium, creating an artifact so that the receiver can record a unique, coordinated signal. However, as the transmitter has no method of noting system responses, it cannot adjust its broadcast. This gives a one time property to the transmitting pro- cess.

29
The inﬁltrate category contains applications in which the main operating process is the transmitter and not the receiver. These applications continually transmit ac- tivity or data into the shared hardware. The eﬀects of these operations are then seen in the reactions that the non-colluding, targeted virtual machines have in response to the altered environment.
This category also encompasses malicious application functions which include a mi- nor role for a receiving process. The reception process operates once and without any knowledge before or after of the transmitter. One example of a side channel attack, used to determine if one malicious virtual machine is colocated with another, relies on a continual transmitter and a one way receiver [4, 7].
The third category, network, jointly operates both the reception and transmission processes continuously. A common example of a malicious application modeled in this way is the construction of a communication channel. Two colluding, co-residing virtual machines can covertly communicate to one another. Each of the communi- cant applications have both a transmission and reception function which operate in a known time frame. This joint sender-transmitter programs may either aﬀect the environment to convey a message or react to the environment to receive a message
[14].
These three main categories shown in ﬁgure 3.1 attempt to organize the diﬀerent primitives from which an adversary may model a malicious side channel applications.
The distinctions between each category are based on diﬀerent combinations of trans- mitting, receiving behavior.
These distinctions ultimately determine the possible functionality of the malicious application.

30 3.2
Exﬁltration Applications
The ”exﬁltrate” category encompasses side channel applications which leak system information. Malicious programs exhibiting exﬁltration behavior continually operate a receiving process. In some cases a transmission process is used once to meaningfully alter the state of the shared hardware.
3.2.1
Continuously Active Receiver, No Transmitter
A hardware side channel application which contains a continuously active reception process, and no transmitter, will react to the changes in the targeted hardware com- ponent that it exploits. Exﬁltration applications record system state over time. This record of system information may be analyzed to understand the activity or state of the coresident virtual machine. A set of common malicious application types which may utilize this single reception structure is presented.
Cryptographic key theft is the most common application documented in literature and targets a hardware side channel using a single reception process. Malicious pro- grams of this type use a receiver to record the changes in the targeted hardware component, most popularly hardware cache. Patterns recorded may be mapped to known patterns which result from diﬀerent encryption operations, such as multi- plication, to leak information about the key. Accounting for noise in the recorded pattern increases the likelihood of successfully retrieving a cryptographic key [21, 12].
Activity logging refers to the monitoring and recording of co-residing virtual ma- chine behavior. A speciﬁc demonstration of this type of malicious functionality is keylogging
[22]. When built across a side channel, the receiving process acquires

31 artifacts from the user activity in the coresident virtual machines.
Pre-acquired measurements of the aﬀects a particular user activity has to the tar- geted medium allow the recording adversary to exﬁltrate sensitive information about user behavior, such as keystrokes.
Malicious applications using a continuous receiver may also employ environmental keying across a side channel [4, 7]. Comparison between an expected record with the actual record of measurements taken from the targeted hardware environment, allows the malicious application to key the virtual machine’s allocated hardware and decide how to execute. Environmental keying has many uses, such as enabling hardware speciﬁc execution, avoiding emulation or other security programs which by running on the same hardware, change the measurements taken from the environment.
3.2.2
Continuously Active Receiver, One Way Transmitter
A transmitting process is added to the receiving application model presented above.
The addition of this transmitter, located in a coresident, colluding virtual machine, provides the functionality in the attack model to broadcast a signal through a shared hardware component. The receiver reads this pre-arranged signal and decides to take actions accordingly. As the transmitter cannot receive information from the system, it cannot adjust its transmission in response to external factors. We present a ma- licious application type which uses this single receiver, one way transmitter structure.
A transmitting application may act as a trigger for a receiving application through transmitting a broadcast signal by altering information on a shared hardware medium.
The signal must be unique so that other, coresident applications may not generate processes which benignly alter the hardware medium in the same pattern. A receiving

32 processes located on a colluding virtual machine will continuously record information from the targeted component until it receives this prearranged signal. After the trig- gering pattern is received, the application can then launch additional functions, such as process initialization or masking to dynamically avoid detection or hide intended information.
3.3
Inﬁltration Applications
The “inﬁltrate” category encompasses side channel applications which cause activity in or inject data into the targeted hardware component. Malicious programs exhibit- ing inﬁltration behavior continually operate a transmitting process. In some cases a reception process is used once to meaningfully alter the state of the shared hardware.
3.3.1
Continuously Active Transmitter, No Receiver
A hardware side channel application which uses a continuously active transmission process, and no transmitter will generate disturbances in the targeted hardware com- ponent. This application will inﬂuence how the system allocates resources between coresident virtual machines as well as what data is queriable from diﬀerent hardware components, aﬀecting the performance of the coresident processes. Depending on the function of the malicious application, the injected information may be tailored to target speciﬁc performance changes.
“Hardware denial of service” refers to the performance impact that the malicious transmitting process causes in the shared hardware component. Applications in this category use a transmitter to alter the data stored in a hardware component or to force prioritization [9, 10]. The speciﬁc function of the transmitting application may rely

33 on a speciﬁc pattern of operations or data injected into the hardware medium, either to exploit the scheduling algorithm or to overwrite speciﬁc data stored in temporary memory.
Accounting for noise caused by coresident operations and prioritization algorithms used by the scheduler increases the likelihood of successfully modifying performance of coresident processes.
3.3.2
Continuously Active Transmitter, One Way Receiver
In this category, a one time receiving process is added to the malicious application model which relies on a continuous transmission process. The addition of this receiver, located in a coresident, colluding virtual machine, provides a reception functionality in the attack model. The transmitter beacons continuously, leaving an artifact in a tar- geted hardware medium which may be read by the reception process. As the receiving process has no method for sending a response, it may only read the continuous signal from the system in the time frame that the transmitter is active. We present a ma- licious application type which uses this single transmitter, one way receiver structure.
This transmission and reception model may be exploited to determine virtual ma- chine colocation. Applications of this type use a transmitting process located on a virtual machine residing on the targeted shared hardware. The receiving process can then move between diﬀerent, allocated virtual machines at random, recording activity of a hardware medium from each one. When the receiving process records the pre- arranged signal, it can then assume it is collocated with the virtual machine running the transmitting process [4, 7].

34 3.4
Network Applications
The “network” category deﬁnes side channel applications which both transmit and receive signals across a targeted hardware component. Malicious programs exhibiting communicating behavior continually operate both a receiving and transmitting pro- cess, much like modern network endpoints.
3.4.1
Continuously Active Transmitter and Receiver
The implementation of a basic communication network across a hardware side chan- nel requires that both communicating applications, running in collocated virtual machines, have joint transmission and reception processes. By avoiding traditional network-based detection methods, communicating side channels built across shared hardware have stronger security properties including covert transmission and in- creased privacy.
Command and control functionality relies on the bi-way communication possible through the use of multiple, coresident virtual machine applications. Applications of this type agree on a time frame and on a single, authority application. Speciﬁcally, botnets operate in this way, where each botnet node contains a joint transmission and reception process and communicates with the collocated, authority node [19]. Some functions of this authority node include choosing on important signals, time frames or protocol variables.

35 3.5
Summary of Three Architecture Models
Three categories are introduced to describe the malicious side channel programs which are structured with the intent to either exﬁltrate, inﬁltrate or communicate across a shared hardware medium.
Diﬀerent pairings of the transmitting and receiving processes in an application form the distinguishing factor used to categorize potential adversarial models. Under each category, speciﬁc application functionality and behavior types form a basis for sub- categorization.
While these groupings do not attempt to exhaust existing attack models, they attempt to provide a view into potential malicious actions across a side channel using the constraints of the transmission and reception pairing. We hope this typology will initiate further discussion on the potential for traditional malware functionality to be applied to modern, cloud based, side channels.

36 3.6
Summary of Channel Architecture Models
– Malicious Attack Type:
• Exﬁltration (Receiver Only)
– M1 ∈Cryptographic Key Theft
– M2 ∈Activity Monitoring
– M3 ∈Environmental Keying
– M4 ∈Triggered by Broadcast Signal
• Inﬁltration (Sender Only)
– M5 ∈Resource Denial of Service
– M6 ∈Determine VM Coresidency
• Network (Receiver & Sender)
– M7 ∈Command & Control Communication

4. FORMALIZATION OF THE HARDWARE SIDE
CHANNEL MODEL
We formalize the two distinguishing factors of side channel construction, the hard- ware exploited and the processes used, to create a tuple representing distinct channel implementations. Each channel implementation represents an attack vector across which speciﬁc malicious applications may be deployed.
4.1
Models to Represent Hardware Side Channels
The ﬁrst distinguishing factor is the speciﬁc hardware resource used to transmit and receive environment information. This shared hardware component is exploited by the sending and receiving processes.
Second is the three speciﬁc implementation architectures discussed in Section 4 - sending process only, receiving process only, or use of both processes.
Each of the three architectures is associated with speciﬁc attack models, also dis- cussed in Section 4. They are listed according to which of the processes the attack model uses. For example, a communicating attack, M7, requires both processes.
37

38
Distinguishing Factor 1
Hardware Side Channel Mediums:
• Processor
– central
– graphical
• Cache Tiers
– L1
– L2
– L3
• System Bus
• Main Memory
• Hard Disk Storage

39
Distinguishing Factor 2
Channel Architecture S/R Models
– Malicious Attack Types Applicable:
• C1 : Exﬁltration (Receiver Only)
– M1 ∈Cryptographic Key Theft
– M2 ∈Activity Monitoring
– M3 ∈Environmental Keying
– M4 ∈Triggered by Broadcast Signal
• C2 :Inﬁltration (Sender Only)
– M5 ∈Resource Denial of Service
– M6 ∈Determine VM Coresidency
• C3 :Network (Receiver & Sender)
– M7 ∈Command-and-Control Communication
Network

40 4.2
Tuple Representing a Hardware Side Channel
We take all possible cross-sections of Category 1 and Category 2. Each cross section contains a single element from each. This forms a set of tuples. Each tuple includes a single hardware medium and channel architecture S/R Model pair. This set provides a complete framework within which diﬀerent channel attacks can be grouped.
A tuple represents a speciﬁc side channel across which a subset of the malicious attack models can be applied. Each application has speciﬁc characteristics and upper bounds for success.
C = Channel Construction =
{ Hardware Medium, Channel Architecture }
C1 = CPU, Receiver
C2 = CPU, Sender
C3 = CPU, Sender&Receiver
Each of the Malicious Attack Models can be applied across the channel construc- tions which implement the associated Channel Architecture S/R Model it is listed beneath above. While the attack models may be attempted under diﬀerent channel architectures, success is hindered by the lack of the necessary sending or receiving processes.

41
For a fully functioning attack, a speciﬁc piece of malware that falls under the applied
Channel Architecture Attack Model, represented by Mx, runs across the given Cx.
Mx x Cx
Speciﬁc characteristics and properties are associated with each Cx running software,
Mx. Implementation in the following section focuses on channels C1, C2, and C3 which use the processor as the hardware medium and represent the three possible permu- tations of the sending and receiving processes. We then quantify diﬀerent artifacts from each Mx associated with each of the three channel possibilities.
4.3
Channel Construction
The channel constructions Cx must have a pre-set time period in which an artifact is measured multiple times from the hardware. The average of these measurements can than be mapped to a single bit signal. The receiver or sender is constructed as a program which has a set number of iterations over the reception or transmission code used to take a single measurement from the hardware medium. Each iteration is one measurement and the number of iterations is the number of measurements averaged together. The time it takes for this number of iterations is a single time frame, fi, used to measure a single bit.
The set number of iterations can be dynamically or statically increased in order to have a larger window in which to collect hardware measurements. This results in a higher likelihood for success in receiving the correct average measurement which maps to the correct bit.

42
Alternatively, this number can be decreased in order to allow for a fast receipt of a bit which decreases accuracy. This relationship holds true for n time frames in series used to collect an n bit message. In Figure 4.1, a series of time frames in series form a bit stream.
fi = time frame to measure a bit
As there is one bit sent per time frame, the bandwidth of the channel Cx, represented as bi, is inversely correctly to fi.
bi = 1 fi
The time frame fi is dependent on the constraints of the hardware medium, Hx, across which the Cx is built. This is an artifact of the time a single hardware measurement takes to collect by the process. For example, hardware mediums located further from the processor are most likely mediums which have longer minimum time frames as it takes longer for a single query to physically reach the component.
1 fi
Figure 4.1: A bit stream, with each time frame and its average measure- ment representing a single bit

43
There are three channel constructions per each Hx, each which are implemented using one of the channel architectures. This set of Cx will have the same value for an optimal bi and therefore of fi given that these values are functions of the hardware component.
The reason for this invariability is that the transmission and reception processes iterate over code that is tailored to interact with a speciﬁc hardware medium. The code iterations do not depend on whether the processes are being used alone or jointly.
We show that the optimal fi and bi do not vary with channels of the same hardware medium. We do this by choosing to use the three channel constructions, represented in this thesis by C1, C2, and C3 deﬁned above, which are implemented using the central processor (CPU) hardware medium, Hcpu. Across these channels, variable malware types will be implemented to show what attack vectors are possible across the three diﬀerent architecture models.

5. HARDWARE SIDE CHANNEL IMPLEMENTATION
We implement the three possible channel constructions, C1, C2, and C3, across the central processing unit, Hcpu. To do this, we create a novel side channel by exploiting a function necessary in modern processor optimization: out-of-order-execution.
5.1
Out of Order Execution
In constructing the three channel types, out-of-order-execution must be exploited.
To exploit this behavior, we create an algorithm which reliably forces out-of-order- execution occurrences across all shared CPU’s. This implies that the algorithm itself must not overload the processor and get optimized oﬀof the shared hardware.
Also known as dynamic scheduling, out of order execution is a direct result of proces- sor optimization [23]. To increase processing power, modern computer architecture implements multi-staged pipelining, allowing for simultaneous execution of multiple instructions. Ideally, this occurs every clock cycle at full capacity, however hazards arise which degrade the overall performance time of the machine. One such hazard would be a delay caused by an instruction set which requires a great deal of cycles and there are other instructions require its output [24, 25].
For example, take loads and stores to main memory which both require many more cycles than an arithmetic operation. If the information used in either instruction is necessary for future operations the processor creates a bubble to avoid a potential hazard which results in computational errors [23]. This bubble is a delay in the in- 44

45 struction pipeline until the hazard has passed.
Processor optimization ﬁlls in the resulting pipeline bubbles with instructions that have been determined not to depend on the current pending ones. This is called out of order execution, when instruction execution order in the processor is not the order sent to it from higher level processes.
All hazards resolved by this method result in a pipeline order which is determined by the processor to be executed without hazards. However the processor does return the output to the higher processes in the order that it was given, ideally with the logically correct computation results [25].
5.2
Exploiting Out of Order Execution
Certain reordering scenarios result in computations that are not expected. Take for example two threads, one with initial values X = 0 and r1 = 0, the other with initial values Y = 0 and r2 = 0. When the program executes, X = Y = 1 and a swapping occurs where r1 = Y and r2 = X. Logically, the expected ﬁnal values of r1 and r2 should be respectively (0, 1) or (1, 0) depending on which thread executes fastest.
Alternatively in the case of syncing threads, (1, 1) may also be expected. However, if the thread instructions are executed out of order, where r1 and r2 are set before the values of Y and X, then the ﬁnal values of r1 and r2 will be (0, 0). A diagram of this process can be illustrated as seen in Figure 5.1

46
Figure 5.1: Two threads depicting possible results of the swap
The illogical output, (0, 0) can be exploited as an unintended leaking of processor behavior. A program will record external environment changes by measuring the fre- quency of the four diﬀerent outputs.

47
Iterating through this computation many times returns an average frequency of out- of-order-execution outputs divided by total number of outputs recorded, or number of iterations. Comparing this frequency against a baseline frequency exposes valuable system information of all processes running on a certain set of shared cores.
5.3
Transmitting and Receiving Processes
We construct the three channel architectures: exﬁltrating, inﬁltrating, and network as separate side channel. To do this, a pair of transmitting and receiving processes exploit the shared central processing unit. The transmitter must force out-of-order- execution to occur and the receiver must record these occurrences.
The receiver is constructed using the method described above to record out-of-order- execution occurrences. A loop in constructed for each time frame which iterates over a single measuring function. This function contains the two threads used to record one of four operation results. After the loop is complete, the sum of out-of-order- execution results is divided by the total number of iterations to get a percentage.
This percentage is compared against a baseline percent of out-of-order-executions to determine if the sending process is transmitting a high bit. The absence of a high bit received in a single time frame implies a low bit. Pseudo code representative of this process used to retrieve a single bit signal is seen in Algorithm 1.
The transmitting process forces the shared central processing unit to execute the operations of the sending processes two threads out of order in order to transmit

48
Algorithm 1 Receiver Pseudo-Code 1: procedure ReceiveBit 2:
n ←# of iterations in time frame fi 3:
sum ←0
▷The summation of OoOE 4:
for k = 0, k++, while k < n do 5:
X ←0
▷The initial variable values 6:
r1 ←0 7:
Y ←0 8:
r2 ←0 9:
parallel Z ←(X ∥Y ), rn ←(r1 ∥r2) do 10:
Z ←1
▷Two threads setting variables in parallel 11:
rn ←¬Z 12:
end parallel 13:
if r1 ≡0 AND r2 ≡0 then 14:
sum+ = 1
▷The (0,0) case implies OoOE occurred 15:
end if 16:
end for 17:
if sum ÷ n ≥threshold % then 18:
return 1
▷A high bit is received 19:
end if 20:
return 0
▷A low bit is received 21: end procedure a single high bit. To send a low bit, the transmitting process simply refrains from operating, allowing the processor to execute the receiving threads in one of the three expected orders. The construction of this transmitter relies on a shared time frame, fi, which is representative of the time it takes the receiver to complete n iterations in the ReceiveBit procedure, see Algorithm 1.
During this time frame, the transmitting process may repeatedly execute out-of-order- execution inducing assembly instructions. These are memory fence instructions, in x86, mfence, lfence, and sfence, used to force the processor to complete the time in- tensive transmitting process loads before the loads of the receiver.

49
This means that the processor optimizes the receiver operations by preemptively loading variable values needed to be stored before these variables are altered.
In
Figure 5.2, the second move instruction in both threads requires this targeted load of the variable value.
Figure 5.2:
The store instructions in both receiver threads; the second move requires a reorderable load in the processor
In transmitting a high bit, the sending process alters the order of the receiver’s thread instructions in the processor as can be seen in Algorithm 2. In transmitting a low bit, no interfering instructions are executed. Either operation happens continuously during the given time frame.
Algorithm 2 Processor Delayed Stores, Preemptive Loads 1: procedure ProcessorReorder
▷assuming all variables set to 0 2:
parallel Z ←(X ∥Y ), rn ←(r1 ∥r2) do 3:
load [ Z]
▷loading value, storing in subsequent variable 4:
store [ rn]
5:
load 1 6:
store [ Z]
7:
end parallel 8: end procedure

50 5.4
Construction of Seven Attacks
We construct a simplistic out-of-order-execution side channel. We use this to deploy an application from each of the seven attack models. The current CPU side channel construction is tailored to the contrived testing environment where there are only a few virtual machines running.
Using the requirements of a successful covert channel discussed earlier in this the- sis, we present Figure 5.3 highlighting a complete attack vector. These stages include determining co-residency, a requirement for any hardware based exploitation. Next, the physical interference or observation of a speciﬁc hardware unit, below the L1 cache is listed. Then noise reducing functions applied to the received data to average away noise and other environment variables. And ﬁnally, the malware can eavesdrop from inside the receiving process based on information leaked from co-resident virtual machines.
For the sake of our implementation, we assumed that co-residency is pre-determined.
Also, that a satisfactory noise canceling algorithm was used. These assumptions were implemented by reducing the total number of running virtual machines to 6, all of which were instantiated on a single Xen server using software conﬁgurations which reﬂect those of the Amazon Cloud Computing service[26].
The implemented side channel by adversarial virtual machines is comprised of a single sender and receiver as described above in Section 4.2. Attack models which require only an active receiver to operate fall under the exﬁltration category described pre- viously in this thesis. Similar categorization of attack models as either inﬁltration or network programs holds true for models requiring only a sender or both processes.

51
Figure 5.3: A complete diagram of the diﬀerent stages of a deployed attack in a live, cloud computing environment
For the sake of this thesis, 7 diﬀerent attacks, one Mx from each malicious attack type found in Section 3.6, is implemented to test for time frame, fi, applicability to diﬀerent architecture models, success limitations, susceptibility to noise, and de- tectability. A listing of the speciﬁc attack objectives, ordered by the malicious attack type they belong to, can be seen below.

52
Implemented Attacks
M 1 = encryption key theft
M 2 = detection of co-located running program
M 3 = capturing unique environment ids
M 4 = malicious process triggered
M 5 = interfere with coresident CPU usage
M 6 = colluding VM detection
M 7 = botnet communication
Where M1−4 require only a receiving program, M5−6 require only a sending pro- gram, and M7 requires both a sender and a receiver. The metrics used to assess each implementation are applied uniformly across all process and are further detailed in the following subsection.

53 5.5
Metrics 5.5.1
Success
The success of applying a malicious application, Mx, across chosen channel, Cx, can be measured. First, through the ability for the malware to function using only the processes of the channel. This will be measured by ﬂagging the malicious application as being either C1, C2 or C3 compatible. This means that it relies on that speciﬁc sender or receiver process to operate.
Additionally we record whether more than a single bit is needed to a received or transmitted signal in order to make it useful to the malware’s functionality. This will give insight into the overhead necessary to complete the attack. We measure this metric against an optimal bandwidth, bi, and time frame, fi.
Applicable Channels
C1, C2, C3
Minimum Bits Required for Success of Attack 1-bit / 1 Process Alteration 5.5.2
Eﬃciency
The eﬃciency of the malicious side channel attack will be measured. Speciﬁcally, we measure the speed and capacity of the malware.On a larger scale, the possibility of repeating the same malicious attack is measured in the number of repetitions possible until degradation of the channel. This gives insight into the malware’s persistence and potential scope. An eﬃcient attack will not vary under continual use.
Resilience
# repetitions before degradation

54 5.5.3
Detectability
A major component of the malicious attack model is avoiding detection. We measure the level at which it can avoid observation or any unwanted identiﬁcation. To test the covertness of the channel, the potential for defensive mechanisms applied by the server host assessed. Speciﬁcally, we measure the possibility for an intelligent sched- uler or hypervisor to detect unwarranted hardware behavior.
Finally, we look at several detection techniques used in malware detection and apply it to malware across hardware side channels. These include, malicious ﬁle signature recognition, detection of the anomalies generated by malicious hardware activity, and
ﬁnally monitoring resource elements.
Intelligent Hypervisor
% resource use visibility
Susceptibility to Detection Techniques
(listed below)
Speciﬁc Detection Techniques Used:
• Signature Based
• Anomaly Based
– Speciﬁcation Based
– Pattern Recognition
• Protected Resource Ownership
Signature based detection is, by deﬁnition, a detection system based on known sig- natures of malicious activity. If a process signature is seen on the system matching one of the known signatures, the system can respond.

55
This applies best to systems with access to all static programs inside a virtual ma- chine. As cloud hypervisors can only access active resource use and allocation, this thesis assumes the client’s static data is private, the beneﬁts of implementing signa- ture based detection is minimal.
Anomaly based detection is, by deﬁnition, a detection system targeting computer intrusions and anomalous activity by monitoring system activity patterns and clas- sifying it as either acceptable or deviating from what is standard. Under this um- brella falls speciﬁcation based detection which relies on speciﬁcations that describe the intended behavior and resource usage of a virtual machine to identify anomalies at runtime. Pattern recognition, another anomaly based method, detects undesired patterns in hardware resource usage to identify side channel like behavior and take action accordingly. As these two techniques directly react to active changes in system activity, it has the most potential for defense against side channel attacks in the cloud.
Protected resource ownership refers to locking out untrusted users or third party virtual machine from using a hardware resource either at all, or while another, pro- tected virtual machine is operating on that resource. This inherently decreases cloud computing eﬃciencies achieved through sharing hardware and is not a viable solution to cloud computing infrastructure. However restricting virtual machine resource con- sumption two completely isolate processes eﬀectively mitigates side channel attacks.

56 5.6
Description of Implemented Attacks and Results
We construct a side channel which sends and receives information by exploiting out- of-order execution. This side channel is deployed across virtual machine instances that reside on a Xen hypervisor and are collocated. Additionally, the environment contains four benign virtual machines idling on the system to mimic a live cloud computing environment. All virtual machines share the central processing unit.
We then construct seven diﬀerent attacks as listed in Section 4.2.4 across this side channel using the same out-of-order execution sending or receiving processes.
5.6.1
M1 Theft of Encryption Key
The ﬁrst set of attacks are termed Cryptographic Key Theft as discussed in Section 3. Applications of this set are classiﬁed as being an exﬁltrating side channel attacks which rely exclusively on a receiving application, channel C1. We implement M1 an application belonging to this set. The intended attack leaks the secret key of an en- cryption algorithm.
In literature, the use of a hardware side channel to leak private keys is widely used to attest to the precision as well as the threat level of the side channel. These include attacks against running encryption and decryption processes as well as a spectrum of algorithms including AES, ElGamal, DES, and RSA [20, 12, 27, 3].
Speciﬁcally, we attempt to demonstrate this attack in a simple lab setting with one active client and one malicious virtual machine. This removes the variable element of noise from the proof of concept attack.

57
Additionally, we target a simple XOR encryption algorithm inside a victim process.
The client implementation uses c++ and a randomly generated encryption key. Each byte is randomly chosen between a range of ten and a hundred.
The attack is begins immediately after the client virtual instance launches its en- cryption function and ends after. During this time frame, the receiver inside the malicious virtual machine records out-of-order-execution patterns from the shared central processing unit. This is done in using the protocol discussed in the ﬁrst few subsections of Section 4. The bit pattern which is recorded is then a function of the
XOR operations executed by the victim’s encryption process.
The encryption process was run one hundred times, re-encrypting the same basic string of length 64 ﬁlled with ascii ’A’s. Every other set of eight bytes are XOR-ed using a randomly generated byte, each XOR uses seven thousand small xors of the same number for the purpose of testing the proof of concept. The seed for this ran- dom factor was provided by the standard c++ rand() function.
The reason we chose to only XOR every other set of eight bytes was to create an obvious ﬂuctuation between central processor contention. The purpose of this was to generate binary activity, either encryption activity or none, by the encryption proof of concept on the CPU in order to reliably receive executed operations in the malicious virtual machine. Future work may include the application of intelligent algorithms to the current, simplistic receiver in order to parse and identify leaked CPU behavior induced by higher order encryption algorithms. The receiving application eavesdrops from the co-located, malicious virtual machine and runs the out-of-order-execution recording process outlined earlier in this section.

58
The receiver implemented for this attack was able to reliably identify the diﬀerent
XOR blocks and non-XOR blocks of eight bytes, or sixteen bits, which were executed by the targeted encrypting process. There was a lack of granularity in the received number of out-of-order-executions per time frame which prohibited us from mapping speciﬁc levels of out-of-order-executions to the values randomly used in the byte-
XOR. Instead, each block of out-of-order-executions were declared either a ’1’ or a
’0’. A ’1’ refers to values received in a time frame which may be mapped, with a de- gree of certainty, to a XOR operation being executed by the victim. A ’0’ implies no
XOR was taking place. The recorded result of this attack may be seen in Figure 5.6.1.
It is apparent that the blocks of out-of-order-execution containing bit strings of ’1’ are mappable to the byte blocks which were XOR-ed, the XOR-ed bytes are represented by a single byte, ’B’. The four encrypted blocks of eight bytes each, shown above, took the receiver 4.9525 seconds on average to leak across the central processing unit with a standard deviation of 0.15606 seconds.
Using the eight byte block method to create clear time frames of encryption, the receiver was able to map blocks of active-XOR and nonactive encryption with an accuracy of 85.9375%. This accuracy is signiﬁcantly high enough to conﬁdently map the periods of high and low operations in our chosen encryption algorithm. The sum- mary of these ﬁndings may be found in ﬁgure 5.10 at the end of this section.
The success of this attack lies in the ability for the malicious virtual machine to leak active behavior from the co-resident process. This may be seen as an attack on both the privacy aspect of transparent behavior by a client in cloud computing en- vironments. Also, this attack highlights the possibility of a simplistic, but successful attempt to learn the victim’s encryption algorithm used by a process.

59
Future work on this topic includes learning algorithms as well as general improve- ments on the reception channel to achieve increased precision rates. Additionally, this would allow an attacker to better connect diﬀerent out-of-order-execution pat- terns with complex encryption schemes as well as speciﬁc numeric values being used in them.
Starting Bytes:
AAAAAAAA AAAAAAAA AAAAAAAA AAAAAAAA
Encrypted Bytes:
AAAAAAAA BBBBBBBB AAAAAAAA BBBBBBBB
Bits Leaked:
0000000000000001 1011011011111101 0000000000000010 1111111101011101
Figure 5.4: The encrypted string compared to the leaked string

60 5.6.2
M2 Active Program Identiﬁcation
Applications built to eavesdrop on concurrent processes fall under the second attack category outlined in Section 3. Attacks from this group uniquely identify co-active applications. For this subset, we chosen to implement malware M2. Speciﬁcally, this processes eavesdrops on system behavior using the channel deﬁned above. Recording speciﬁc, repeated out-of-order-execution patterns allows M2 to map behavior to spe- ciﬁc process identiﬁers.
For the purposes of this thesis, our implementation of M2 was constructed on channel type C1. This is implied for the activity monitory category outlined in Section 3. We ran M2 one hundred times. Each duration lasted for 32 time frames, or roughly 3 sec- onds. During these runs, ﬁve co-located virtual machines were actively running. The targeted virtual machine was running instances of YouTube inside Google Chrome.
For our proof of concept, we sought to eavesdrop on this VM and conﬁdently identify, with a high degree of certainty, what application, if any, was being run.
For each period of reception, the malicious application would record a bit stream of length 32. The pattern of bits averaged over several runs was then used to classify the co-active process as either being a high or low generator of out-of-order-execution.
From there, the average bit pattern could then be mapped to a prerecorded pattern of a known active Chrome session stored inside the malicious application binary.
The average time of each run was 3.13294 seconds, assuming the program was record- ing a bit stream of length 32. There were ﬁve co-located VM’s sharing the central processing unit with the one virtual machine actively running the victim process.

61
The standard deviation of this experiment was 0.14234 seconds. The success rate of mapping active, unknown applications to one of two sets , either out-of-order- execution generators or not, was 100%. However given more system noise, such as the numerous applications which would be co-resident in a highly active cloud server, the addition of higher order algorithms need to be applied to parse out identifying information from a system.
The lab environment contained six virtual machines running on a single Xen server.
Under these conditions, the speciﬁc identiﬁcation of a running instance of Chrome, as opposed to other programs artiﬁcially used to generate noise, was successful on a average of 0.93%. This is signiﬁcantly high enough to reliably identify a client run- ning video instances inside this browser process. An overview of the results of this attack, M2 can be found in Figure 5.10.
The success of this basic attack carries implications on both a privacy and information security level as well as on a systems level. When concurrent processes continually leak data across virtual machines, the privacy of a user’s activity may be called into question.
Future work on this topic includes further testing and statistical averaging to cre- ate a larger database of patterns mapped to their associated processes, i.e. Safari,
Firefox, or IE, under diﬀerent system loads, i.e. while 1 virtual machine is running or 10.

62
The possibility for a mapping is shown to exist through this thesis’s preliminary work.
Given the possible precision an attack could achieve, identiﬁcation of speciﬁc program execution by a client is detectable. An example of this precise identiﬁcation may be an attack conﬁdently identifying a user’s physical input into a running program.
Bits Leaked from System Baseline Activity:
...0000 000000000 000000000 00000000 000000000 000000000...
Bits Leaked from Client Running Chrome:
...0100 010101011 010101011 01010010 010101011 010010010...
Figure 5.5:
The bit stream leaked through the receiver showing the re- peating pattern associated with running videos in chrome
If ﬁgure 5.6.2, the results of this described attack may be observed in two diﬀerent segments of the bits leaked from the CPU’s out-of-order-execution. In this receiver, each bit represents 100,000 individual out-of-order-execution checks average together in order to reduce the aﬀect of noise on the ﬁnal bit stream. Each bit of this continual stream was recorded, on average, in 0.18806 seconds. As can be seen, while the victim was not running any programs, the bit stream was entirely ’0’; however, after opening
Chrome to play a video, the bit stream stabilized into the pattern shown above.
This speciﬁc test was repeated 100 times in order to positively identify a mapping between the targeted application and out-of-order-execution patterns exﬁltrated from the system.

63 5.6.3
M3 Environment Keying
Environment identifying programs are the third attack category outlined in Section 3. They rely exclusively on the receiving side channel application. For this reason, they may be labeled as processes which rely on channel type C2. These channels are deﬁned as using only a reception process to record out-of-order-execution patterns as a bit stream. This stream represents the environment in which the malicious virtual machine resides [4].
For our speciﬁc implementation of an application from this malicious process cat- egory, we chose to implement a simple environmental keying malware. The attack contains two distinct phases. The ﬁrst is a malicious virtual machine runs an envi- ronmental keying side channel program to generate a unique key used to identify the system. The second stage uses a piece of malware located on a victim virtual ma- chine that contains an encrypted payload. This application uses a replicated receiver to record system out-of-order-execution patterns. If the patterns recorded match the targeted pattern identiﬁed by the malicious host, the malware decrypts its payload.
The crux of this attack lies in the generation of a unique environmental key which iden- tiﬁes the targeted environment. This allows a malicious application to gain location- awareness in order to expose its malicious behavior only when located on the proper virtual machine [4, 8, 7].
For our simpliﬁed implementation of this attack scenario, we set up 6 virtual machines on a Xen server with one machine categorizes as the malicious host and another as the victim. The receiver on the host VM receives a bit stream, the unique identiﬁer, using the out-of-order-execution receiver discussed earlier in this section.

64
A malicious application with an encrypted payload and the unique ID may then be dropped onto the target VM. This malicious process immediately begins the du- plicated receiving process to eavesdrop on the central processing unit behavior and
ID the environment. If the identiﬁers match, it unpacks the payload and executes.
Host identity-based encryption may also be possible using this attack setup assuming the unique identifying string can be 100% recovered by the malicious process running inside the targeted virtual machine. This may require future work in channel opti- mization and averaging out system noise. For the sake of this thesis, we show that a unique identiﬁer can be recovered by 83% which allows the application to decide if the identiﬁer it records and the one pre-recorded by the host malicious virtual ma- chine are close enough to conﬁdently assert that the environment is the right one and execute accordingly.
The host virtual machine ran the out-of-order-execution receiver to collect a key of length 32 bits, this averaged out to 27.2925 seconds, or 3.41156 seconds per 4 bit segments and a standard deviation of 0.06478 seconds. An example of an unique environment key can be see in ﬁgure 5.6.2.
This key was then encoded into the deployed malware containing the encrypted drop- per which was then installed on the targeted virtual machine.
Once started, the application began the out-of-order-execution receiver to record the same length bit stream as the host receiver captured. This 32 bit sequence was compared to the en- coded bit stream representing the environment in which the malware should unpack.

65
This process was executed for 100 trails to compute an average percent similarity be- tween the environment the malware was in and the expected environment identiﬁer.
Under the contrived circumstances of this laboratory setting, we found that the mal- ware recorded an environmental identiﬁer which correctly matched its environment to the one represented by the host’s encoding identiﬁer with 96.875% accuracy. This matching was deemed suﬃciently high enough to conﬁdently identify the targeted system.
Future work on this subset of malicious applications can build from the use an out- of-order-execution side channel to identify unique environment keys. This work will include creating intelligent algorithms to better record individual bits based on the frequency of out-of-order-executions. The goal would be to generate a receiver which can guarantee a repeatable reception of a speciﬁc bit stream. Once the key can be guaranteed, it may be used in the actual encryption/decryption on the payload.
In the current status of the attack, the received environment key can be deemed similar enough to correctly identify the system. This allows the receiver to be used as a binary decider. If the bit stream eavesdropped oﬀthe CPU is close by a given threshold to the original recorded by the host, the environment is positively identiﬁed and the malware executes. This inherently poses a threat to the privacy and security of virtual machines stored in the cloud and leaks valuable location information. As this attack was successful, future development on applications in this category also show potential to successful exﬁltration.

66 5.6.4
M4 Signal Trigger of Process
Our implementation of M4 belongs to the last exﬁltrating attack model speciﬁed in
Section 3.
This attack model requires a transmitting as well as a reception pro- cess which are located on two distinct co-resident virtual machines. Additionally, it requires a pre-arranged time frame as both processes must have overlapping active periods for the success of the attack.
This attack model may use channel types C1 or C2 depending on which of the two processes is continually running. Either the sending process transmits continually waiting for the receiver read the signal. Or the receiving processes idles until it reads a one time signal.
Both methods rely on the use of message transmission across our constructed channel, to exploit forced variance in the out-of-order-executions oﬀof the CPU. The channel processes use the same algorithms outlined earlier in this section and used by all attacks described in this thesis.
In ﬁgure 5.6, the use of the continually operating receiver can be seen. The receiver reads out-of-order-execution patterns from the shared central processing unit in pre- arranged time frames. At the start, the transmitting program transmits the signal
”111..” as a bit stream. It forces high levels of out-of-order-executions repeatedly for several time frames. Each time frame represents a single bit. The receiver detects the high bit stream and launches its intended attack.
The resulting length of time necessary to run four bits in this described attack one hundred times repeatedly in the same environment is 1.79025 seconds with a standard deviation of 0.07816.

67
Figure 5.6: Use of the central processor in synced, concurrent time frames allows the transmission of a signal between two colluding applications in real time
The environment of this laboratory system contains six idling virtual machines of which only two are active. One is the malicious host containing the sending process and other contains the reception process which is continually listening for the beacon signal. Additionally, we assume the collocation of the two interactivity virtual ma- chines could be veriﬁed prior to the attack. The ability for an accurate time frame to be calculated from inside diﬀerent virtual machines is also assumed.
Experimentation with this attack using multiple transmitting processes from in- side diﬀerent virtual machines to increase the frequency of the forced out-of-order- executions seen across the shared central processing unit by the targeted receiving process, resulted in degradation of the signal’s precision.

68
Initially, increasing the number of senders did improve the broadcast signal’s band- width. However, using the maximum number of machines virtually allocated on one physical server increased the noise to an amplitude higher than the out-of-order- execution signal. This meant that the precision gained through multiple senders in- creasing the bandwidth was minimized by the noise of the system,forcing miss-reads in the receiver and failing the attack. Further experimentation is needed to test the limits of increasing signal strength through introducing additional concurrent senders versus increasing system load and noise levels.
Building more complex attacks oﬀof this simple triggering signal requires little eﬀort on the part of the advisory. This advisory to wrap the receiver in a obfuscating pro- gram with an arbitrary payload to execute upon receiving the signal.
Our basic attack model implemented to transmit a signal between two colluding parties co-located on shared hardware realizes a basic proof of concept channel at- tack. The implications of this simplistic, exﬁltration vector span across violations of both unauthorized data access as well as active interference with the target’s private virtual machine.

69 5.6.5
M5 CPU Resource Contention
The ﬁfth set of malicious applications, from Section 3, is Resource Denial of Service.
It is classiﬁed as an inﬁltrating side channel attack. This is deﬁned by speciﬁc ap- plications which rely exclusively on a transmitting application, channel construction two, C2. We construct M5 as a speciﬁc application belonging to this set. The purpose of this attack is to force contention of central processing unit resources for targeted processes.
In literature, the contention of any resource which negatively eﬀects the targeted user is often referred to as a Denial-of-Service attack (DoS) [15, 28]. This elemental intrusion of the user’s environment does not require the least level of precision com- pared to other attacks discussed in this thesis.
Compared to other adversarial models, this attack category, M5, requires the greatest, consistent signal amplitude in order to signiﬁcantly impede the CPU computations for the co-active processes. The diﬃculty with this interference comes from the hyper- visor’s resource scheduler and optimizations which attempt to decrease the constant load caused by the transmitter.
To consistently force out-of-order-executions in the processor, the transmitter must use larger time frames, fi. This allows the transmitter to execute more out-of-order- execution generating assembly code to account for the few instructions which are optimized out of the time frame, fi, by the hypervisor.
The eﬀect of large time frames is an increased execution time for the attack, M5.
For this thesis, we implement a speciﬁc, M5, which attempts to interfere with the tar- get’s computations through increasing the out-of-order-executions in the processor.

70
After a certain threshold level of these executions, the processor returns invalid or reordered values to the target process, thereby meeting our requirements for a denial- of-service attack. In our scenario, the service required by the target process is pro- cessor execution of speciﬁcally ordered instructions to result in precise values.
The predicted increase in the minimum duration needed to successfully execute this attack is see in our implementation, M5, against an isolated victim process running in four consecutive time frames, fi. The average run time of 2.21538 seconds is measured from one hundred tests run on a Xen server with 6 virtual machines. The standard deviation these runs is 0.11023 seconds.
These results imply that the increase in bandwidth of the transmitted signal ef- fects the precision of each run and generating higher variance in minimum time frame durations needed to interfere with the victim process. Additionally, the increase in signal strength from using multiple sending processes added noise to the out-of-order- executions read in each time frame.
Combined, the decrease in precision from the larger fi and the noise from the larger number of sending processes used to increase signal strength adversely aﬀected the intended binary transmission. The attack M5 operated successfully with the use of one to four virtual machines, operating at a threshold above the generated noise and variance. However, the attack failed under ﬁve virtual machines operating the transmission process. 5 virtual machines used to send a broadcast signal to clog the processor is the limit of the signal strength for the size of the laboratory Xen envi- ronment.

71
The attack success was measured in value miscalculation as computed for the vic- tim process. On average, the successful runs of attack M5 caused a 50% value loss in the computation of the targeted operations. The target process ran a while loop which read from an array and, in two threads, multiplied it by a constant value, storing the results back in the same index. This array could then be compared to the expected values pre-computed at the end. Incorrect values meant that the thread order was incorrectly altered by the processor, showing that the adversary was successful for the time frame of that array index’s computation.
Example Target Process Array Before Calculations
[7, 4, 0, 9, 2, 8, 5, 7, 0, 9, 8, 7, 1, 2, 9, 4, 8, 5, 7, 3, 0, 2, 8]
Target Process Array After Multiplication with 5
[35, 20, 0, 9, 10, 8,5, 35, 0, 45, 8,7,1, 10, 45, 20, 8, 25, 7, 15, 0, 2,8]
Target Process Array Expected Calculations
[35, 20, 0, 45, 10, 40, 25, 35, 0, 45, 40, 35, 5, 10, 45, 20, 40, 25, 35, 15, 0, 10, 40]
Figure 5.7: The array values before and after computation
Figure 5.7 shows values of the array which were adversely aﬀect during the computa- tion due to the out-of-order-executions forced by the malicious transmitting process.
The success of this speciﬁc attack was 43.43% based on the number of stores in the ar- ray which were reordered to occur prior to the multiplication instruction. Additional testing to determine limitations of this attack on larger scale cloud environments will help. Increased noise tightens the boundaries of malicious applications which fall under this category.

72 5.6.6
M6 Determine VM Co-Location
One fundamental requirement to create a side channel is establishing co-location of the virtual machines. These virtual machines must share one or more hardware com- ponents. This requirement is discussed in Section 1 and 2.
From the malicious process category termed Determine VM Co-Location, which re- quires channel type C2, we implement M6. This application exploits out-of-order- execution on the central processing unit to create a side channel. It then veriﬁes co-location with another colluding, malicious virtual machine with a threshold degree of certainty.
For the experimental setup, shown in ﬁgure 5.8, we hosted six virtual machines on a Xen Server with one selected as the malicious host receiver. This virtual machine attempts to verify its physical location. From the remaining virtual instances, we chose at random another to alternate between acting as a colluding virtual machine.
If the malicious host VM determined co-location during a period that the chosen VM was colluding, a success was recorded. If it determined co-location during a period that the chosen VM was benign, a failure was determined and vice versa.

73
Figure 5.8:
The black virtual machine represents the malicious host and the gray virtual machine represents the alternate continual transmitter
The chosen, colluding VM continuously transmits a signal composed of time frames, fi, which is read once by the malicious host VM, started on the Xen server.
Once the receiving process ﬁnishes this one time read of oﬀthe central processing unit, it makes a binary decision, comparing the read activity levels to a pre-determined threshold value. Based on the lack of noise in the simplistic environment used for our implementation, the threshold can be set closer to the expected results.
Running this scenario two hundred times interspersed with cases where co-location should be detected and should not, the overall percentage of correct co-location de- tection was 97% under the assumption of no concurrent, active processes that would signiﬁcantly impact the noise threshold of the channel.

74
This level of successful identiﬁcations was in part a result of the increased length of each time frame, allowing to better average out any false positive readings. However, this did impact the overall time necessary for the attack, M6, bringing the minimum duration that the adversary needs to record the system for four time frames to an average of 3.13295 seconds. The standard deviation of this measurement between all experimental results was 0.2171 seconds. These results make this successful attack the longest of the seven categories implemented for this thesis. Further research may be done using varied testing environments to better test the boundaries of this attack at larger scales.
Based on our initial survey of the cloud computing environment, there are two distin- guishing variables to explore. First, the increased levels of or variance in noise from surrounding processes. Additionally, the partial processor co-location where a virtual instance is allocated time on processors belonging to two or more separate cores on the same server. Both factors listed are suﬃcient to interfere with the success of an attack by M6. Also, they are common enough to be present in the majority of live cloud computing systems.
The one time reception of an unique signal which is transmitted by a continuous sending process classiﬁes this attack as operational across a channel architected C2 as deﬁned in Section 3. M6 creates an information leakage between virtual machines which should otherwise be operating in isolated segments of the hardware. The inﬁl- tration of the shared hardware system by the transmitor allows the colluding process to leave an artifact in a region of the server where the user is otherwise not privileged to access. The success of this attack can then be seen as a violation of privacy, an unauthorized escalation of privileges, as well as a physical exploitation of the processor pipeline.

75 5.6.7
M7 Bi-Way Communication
The ﬁnal channel category of the three, C3, requires the continual operation of both a transmitting process and a reception process. This generates a bi-way communication between two colluding applications located in separate, co-located virtual machines.
The category termed Command-and-Control Communication Network contains all malicious applications which rely on this channel architecture. Our implementation of malicious application M7 is a subset of this group, exploiting the environment using channel C3.
Speciﬁcally, M7 attempts to successfully create a covert channel for two malicious virtual machines. This allows the virtual machines to communicate without generat- ing highly visible network traﬃc caused through normal mechanisms.
For our experimentation, we used the same environment setup as with the previ- ous attack implementations. This includes the Xen server and six virtual instances which share all physical cores available on the server. Additionally, we assumed that there is a pre-arranged start and stop agreed on between both processes. We assume there is a pre-established time frame duration in which a single bit is measured. Test- ing under these conditions, the variable of noise was included through either active or inactive, co-resident virtual machines.
In the implementation of M7, the two malicious hosts each contain both side channel processes, one sender and one receiver. The processes are alternated between to gen- erate bi-way, binary communication. A single test run included four bits transmitted and received by both parties. A success was measured when more than two of the four bits recorded matched those that were sent.

76
One virtual machine was designated as sending ﬁrst and listening second, the other virtual machine took the opposite role. The receiver ﬁnished recording the system after four time frames to acquire the entire binary message. Following this, the trans- mitter residing on the same virtual machine began sending the designated four bits.
The duration of these two stages make up the length of the communication attempted.
In order to maintain an average percentage of correctly received bits, each time frame, fi, was found to be 0.95107 seconds given only the four idling virtual machines in the experimental settings. This number may change depending on speciﬁc system variables. The time frame duration raised the time to 3.80428 seconds for a single four bit message to be sent. This attack is the longest of the seven described for this thesis. The standard deviation on one hundred tests was 0.13538 seconds, the third highest variance of the seven attacks.
Overall, the minimum time needed to generate a successful attack where more than half the total number of transmitted bits are correctly received increased. Further research into optimization algorithms and communication protocols would undoubt- edly decrease this time. For instance, an example communications algorithm may be implemented such that a single bit is transmitted three times in a row and the receiver takes the most common bit as the intended message.
One element of the communication channel is that it transmits messages via a broad- cast signal. All shared processor activity may be received by any number of eaves- dropping virtual machines provided they use an identical receivers and a synchronized time frame. Therefore, communicating parties using the hardware side channel can- not be certain that co-located processes are unaware of the transmissions.

77
However, the processor side channel may be considered to provide covert commu- nications given the obscurity of the medium over which the message is sent. The hardware processor provides this covertness for our out-of-order-execution channel as the majority of communication monitoring eﬀorts target dynamic observation of active network traﬃc. While M7 was implemented to transmit and receive between a single malicious host and a single malicious client application, there is potential for further attack development.
The broadcast nature of the physical side channel may be exploited in order to in- tentionally communicate with multiple virtual machines containing a reception and transmission application. Using multiple virtual machines colluding with a central malicious host VM, a botnet may be generated which resides on a single physical server as outlined in Figure 5.9.
Figure 5.9: A botnet which uses n bots that receive commands and trans- mit responses to the central authority; our side channel acts as the relay

78 5.7
Summary of Implementation Measurements
Figure 5.10: A table listing the average deploy rate for each of the seven attacks implemented as well as the associated standard deviations

79
Figure 5.11: A chart visualizing the execution rate of each implementation and the minimum times necessary for each attack’s success

6. APPLICATION AND POTENTIAL OF INTRUSION
DETECTION TECHNIQUES
This thesis outlines seven attack categories deployed across variations of our out-of- order execution side channel. An application from each category is then implemented.
Presented with these adversarial models, we attempt to highlight the major detection techniques for an intelligent hypervisory. Consider that each malicious application requires signal transfer, either exﬁltrating or inﬁltrating, across the central processor.
This use inherently mimics malware’s use of a traditional network.
We target a set of defensive methods applicable to our channel construction. These are outlined in Figure 6.1.
In order to detect this malicious activity, a process residing on a host machine may be monitored in three ways [29]. Through dynamic analysis of their interaction with external processes and protected resources, termed Anomaly-Based. Through static identiﬁcation of known malicious programs, termed Signature-Based. Through matching recorded activity patterns with known untrusted or restricted behaviors, termed Pattern-Based. A subset of these techniques may be applied to defend against applications which exploit hardware side channels.
80

81 6.1
Anomaly-Based Channel Malware Detection
Anomaly based detection is, by deﬁnition, a system for detecting computer intrusions and misuse [30]. This is done by monitoring system level activity and classifying it as either normal or anomalous.We apply this technique to hardware side channels.
A pattern of activity across the targeted hardware medium is instigated by the chan- nel’s transmission or reception processes. This pattern may be recorded or observed by the hypervisor. Using anomaly based detection methods, the hypervisor may rec- ognize communication like activity, the repeated resource consumption, coming from a virtual machine instance.
Speciﬁcation based system monitoring uses a dictionary of expected behaviors and resource consumption habits for each virtual machine [31, 32]. This gives the hy- pervisor insight into what should be considered anomalous behaviors. For example, a virtual instance registered as hosting a static website requires sporadic use of the processor. An intelligent hypervisor could associated scarce processor use with this machine. If the virtual machine begins requiring long periods of processor time for computation, suspicion would be raised.

82
Figure 6.1: The set of detection techniques applicable to the seven attack categories deployed across the out-of-order-execution side channel

83 6.2
Signature-Based Channel Malware Detection
Signature based defensive methods is most often implemented by antivirus software
[33]. It uses a dictionary of static signatures or hashes generated per ﬁle or segment of code. If an program or a subset of it can be hashed and found in the dictionary, the host determines the program to be malicious. The technique of blacklisting hashes can be applied to side channel attacks.
In this case, a particular block of shared memory resource used by a procress could be hashed. This helps determine if a known side channel process is residing in memory or if a process is ﬁlling segments of memory with blacklisted contents [34].
Alternatively, the memory used by one virtual instance may be hashed and later rehashed after other processes executed or time elapsed. This would provide insight into repeatedly emptied or repeatedly queried blocks of memory.
6.3
Pattern-Based Channel Malware Detection
Pattern-based detection methods monitor system behavior. The system may then recognize communication-like activity originating from one or more virtual machine instances. Two distinct method types stem from pattern based detection. Tracing runtime activity and static analysis of binary data [35].

84
Of the two, the latter cannot easily be applied to malicious side channel detecting as it would require full access to a user’s programs residing in the virtual machine. We assume the hypervisor does not have read privileges for client data inside a virtual machine. Static Pattern-Based methods are out of scope for side channel detection.
Alternatively, analysis of runtime activity traces applies to the side channel attack model. Consider an intelligent hypervisor which records system activity of the hard- ware resource leveraged by the side channel to communicate.
The cyclical trans- mission of bits by forcing a speciﬁc resource state inherently generates detectable patterns.
The hypervisor dynamically learns which patterns are safe and which indicate anoma- lous activity [30, 35]. If prior runtime traces are acquired from an example system, the hypervisor can compare recorded and expected patterns. Then positive identify malicious side channel communication can be made.
6.4
Inherent Strengths of Hardware Side Channels Against
Detection
Hardware layer side channels possess numerous strengths over other types. These weaker implementations include side channels built using network artifacts, such as social media [36]. Shared hardware side channels, by nature of their construction, cir- cumvent many defensive mechanisms usually applicable to these network or software level exploits.

85
In cloud computing infrastructures, the virtual machine’s contents are opaque to the third party host. Therefore all static malware detection techniques are of little value.
All that is available to the hypervisor is the interaction of the processes at runtime with the physical system. We present an intelligent hypervisor or host system to exploit these interactions.
The intelligent hypervisor records a user’s expected resource consumption, runtime behaviors, and other identiﬁers. These properties allow restrictions to be set on re- sources and co-executing process interaction. These modiﬁcations also support the defensive methods discussed in the previous section. However, numerous changes to the current state of the hypervisor and its anonymous allocation of virtual machine resources are required.
Another common security measure, easily defeated by hardware side channel attacks, is the use of sandboxed environments. Sandboxes isolate executing programs from the live system and record behaviors [37]. They place a layer of virtualization between the side channel and the hardware medium used in the communication. This defen- sive mechanism, by its presence, disrupts the fundamental medium of the side channel.
In this sandbox, a reception process, querying the hardware component, is made aware that the noise levels or response timings have changed. The readings from the system will either not be as expected or fail generate meaningful signals. Once the target environment is abstracted away from the hypervisor, the signal being sent and received is adversely perceived by the side channel processes. The side channel application may then idle until the hardware readings indicate the removal of the sandbox. In this defensive techniques, observation aﬀects the channel as well as the expected hardware responses and access capabilities.

86
Overall, the use of static software analysis or sandboxing by the host does not reliably defend against hardware based side channels. Furthermore, they are easily mitigated by a side channel’s reception of unexpected hardware behaviors.
6.5
Potential of Detection Techniques against Side Channel
Attacks
In our experiments, we assume that the data stored inside a virtual machine is opaque to the hypervisor. Static analysis of a user’s binaries is not permitted as per cloud based privacy rules [26]. Therefore, all that may be used to detect side channel ex- ploitation is the dynamic interaction between a virtual machine’s processes and the surrounding shared hardware.
Recording full system activity over a period of time generates records of distinct resource consumption patterns. The hypervisor may then match these records with known resource consumption habits that are not permitted. Advancements in ma- chine learning and pattern matching will further enhance the eﬀectiveness of these techniques in side channel detection.
Additionally, some typical malware detection techniques may also be applied for the detection of side channels [38, 37].
Examples of techniques from this subset include monitoring system calls, recording resource queries, and prohibiting repeated behaviors on which side channels depend. These techniques are implemented at the hypervisor or host level. When such queries occur, the intelligent hypervisor may decide whether the call is blacklisted, whitelisted, or suspicious.

87
Detection of communication behavior across the hardware not only discloses the pres- ence of a hardware side channel exploit, but also uncovers what malicious transmission is sent and received given the broadcast property of the signal.
On average, protection methods which prohibit virtual machines access to shared hardware resources are most eﬀective [39, 40, 41]. However, such methods reduce the intended performance of the cloud system.
Given the strong parallelism between network communication and resource based side channels, the application of Signature, Anomaly and Pattern Based detection tech- niques should be further explored. Eﬀective techniques include dynamic and static methods. Dynamic methods monitor resource consumption patterns of individual processes. Static methods hash and analyze used memory spaces of the processes over time [42, 33].

88
Eﬀective Detection Techniques:
• Signature Based
– Analysis of memory block signatures over time
• Anomaly Based
– Speciﬁcation Based
∗Limiting system calls
– Pattern Recognition
∗Resource use patterns
∗Repeated data manipulation
• Protected Resource Ownership
– Isolate Virtual Machine Hardware
– Blacklist resource access by concurrent processes
All three categories outlined in Figure 6.1 show strong potential for detection of side channel exploitation in the cloud. Techniques from each of these categories mitigate the potential vulnerabilities from sharing hardware. They do not interfere with the eﬃciencies gained through sharing resources by isolating resources or prohibiting co- location. Further research into these three techniques will better tailor the defensive methods to large scale cloud environments.

7. CONCLUSION
In this thesis, we establish a basis for classifying seven potential adversarial models through identifying side channel primitives. To do so, we assess the properties inher- ent to all side channel exploits across the spectrum of shared hardware components.
Necessary factors include static time frames, co-location, and pre-arranged channel protocols. Assuming these factors, we classify our potential adversarial models by their functionality. To further divide these models, we create three distinct channel types - exﬁltrating, inﬁltrating, or networking under which diﬀerent attack models belong.
Using this classiﬁcation, we create seven distinct malware models which encompass all possible malware implementations. Each model possesses unique requirements for sending and receiving processes. Additionally, each model instruments singular algo- rithms for achieving the desired attack with available data. We classify the models under one of the three channel architectures. This allows for architecture speciﬁc features and impediments to be taken into account during implementation.
In order to provide a proof of concept for our typologies, we create seven novel ma- licious applications, each of which are associated with an attack model. Each of the seven malware implementations exploit the primitives of our out-of-order-execution side channel. The environment used mimics that of a standard cloud running a Xen hypervisor and several benign virtual machines.
Assessing the above ﬁndings, we conclude that exploitation of out-of-order-execution across the CPU shows potential for attacking large scale cloud environment.
89

90
Additionally, shared hardware behavior can be recorded or altered, and subsequently mapped to speciﬁc functions. This lack of anonymity has implications for the future of user security in the cloud. Also, creating covert communication between multiple virtual machines has direct potential for a live environment. Further research in areas of all seven malware attack models would target optimization, noise reduction, and speed.
We outlined the three main categories for dynamic OoOE side channel detection which show promise for hypervisor-level security - Resource, Signature, and Anomaly.
Dynamic security and resource consumption monitoring must be pursued in order to maintain the current level of both process anonymity and private data storage in
Infrastructure-as-a-Service.
Ideally, this work will provide an eﬀective means for evaluating preexisting and novel side channel attack vectors. Also, we present attacks which show the vulnerabilities present in modern cloud environments. Emphasizing these areas will focus future research into developing oﬀensive side channel applications and innovating solutions to future cloud based security vulnerabilities.

LITERATURE CITED
[1] M. Godfrey and M. Zulkernine, “Preventing cache-based side-channel attacks in a cloud environment,” IEEE Trans. Cloud Comput, vol. 2, pp. 395–408, Oct.
2014.
[2] J. Shi, X. Song, H. Chen, and B. Zang, “Limiting cache-based side-channel in multi-tenant cloud using dynamic page coloring,” in IEEE/IFIP 41st Int. Conf.
on Dependable Syst. and Networks Workshops, pp. 194–199, June 2011.
[3] C. Percival, “Cache missing for fun and proﬁt,” in Proc. of BSDCan, 2005.
[4] T. Ristenpart, E. Tromer, H. Shacham, and S. Savage, “Hey, you, get oﬀof my cloud: Exploring inform. leakage in third-party compute clouds,” in Proc. of the 16th ACM Conf. on Comput. and Commun. Security, CCS ’09, (New York,
NY, USA), pp. 199–212, ACM, 2009.
[5] K. Gurudutt, “Considerations in software design for multi-core multiprocessor architectures,” May 2013.
www.ibm.com/developerworks/aix/library/au-aix-multicore-multiprocessor,
[Accessed Dec. 17, 2014].
[6] P. Brady, “Memory hierarchy,” 2008.
www.pixelbeat.org/docs/memory hierarchy, [Accessed Jan. 2, 2015].
[7] Y. Zhang, A. Juels, A. Oprea, and M. K. Reiter, “Homealone: Co-residency detection in the cloud via side-channel anal.,” in IEEE Security Privacy, SP
’11, (Washington, DC, USA), pp. 313–328, IEEE Comput. Soc., 2011.
91

92
[8] S Yu, XL Gui, JC Lin, JF Wang, and XJ Zhang, “Detecting vms co-residency in the cloud: using cache-based side channel attacks,” Electron. and Elect.
Eng., vol. 19, no. 5, p. 7378, 2013.
[9] R. Di Pietro, F. Lombardi, and A. Villani, “Cuda leaks: information leakage in gpu architectures,” arXiv preprint arXiv:1305.7383, 2013.
[10] Z. Wang and R. B. Lee, “Covert and side channels due to processor architecture,” in Proc. of the 22nd Annu. Comput. Security Appl. Conf.,
ACSAC ’06, (Washington, DC, USA), pp. 473–482, IEEE Comput. Soc., 2006.
[11] J. Chen and G. Venkataramani, “Cc-hunter: Uncovering covert timing channels on shared processor hardware,” in 2014 47th Annu. IEEE/ACM Int. Symp. on
Microarchitecture (MICRO), pp. 216–228, Dec. 2014.
[12] Y. Zhang, A. Juels, M. K. Reiter, and T. Ristenpart, “Cross-vm side channels and their use to extract private keys,” in ACM Conf. on Comput. and
Commun. Security, CCS ’12, (New York, NY, USA), pp. 305–316, ACM, 2012.
[13] Y. Yarom and K. E. Falkner, “Flush+ reload: a high resolution, low noise, l3 cache side-channel attack.,” IACR Cryptology ePrint Archive, vol. 2013, p. 448, 2013.
[14] Z. Wu, Z. Xu, and H. Wang, “Whispers in the hyper-space: High-speed covert channel attacks in the cloud,” in Proc. of the 21st USENIX Conf. on Security
Symp., Security’12, (Berkeley, CA, USA), pp. 9–9, USENIX Assoc., 2012.
[15] T. Moscibroda and O. Mutlu, “Memory performance attacks: Denial of memory service in multi-core syst,” in Proc. of 16th USENIX Security Symp.
on USENIX Security Symp., SS’07, (Berkeley, CA, USA), pp. 18:1–18:18,
USENIX Assoc., 2007.

93
[16] B. Lipinski, W. Mazurczyk, and K. Szczypiorski, “Improving hard disk contention-based covert channel in cloud computing environment,” CoRR, vol. abs/1402.0239, 2014.
[17] Z. Tari, “Security and privacy in cloud computing,” IEEE Trans. Cloud
Comput, vol. 1, pp. 54–57, May 2014.
[18] D. Fernandes, L. Soares, J. Gomes, M. Freire, and P. Incio, “Security issues in cloud environments: a survey,” Int. J. of Inform. Security, vol. 13, no. 2, pp. 113–170, 2014.
[19] Y. Zhang, A. Juels, M. K. Reiter, and T. Ristenpart, “Cross-tenant side-channel attacks in paas clouds,” in Proc. of the 2014 ACM SIGSAC Conf.
on Comput. and Commun. Security, CCS ’14, (New York, NY, USA), pp. 990–1003, ACM, 2014.
[20] D. A. Osvik, A. Shamir, and E. Tromer, “Cache attacks and countermeasures:
the case of AES,” in The Cryptographers Track at the RSA Conf. on Topics in
Cryptology, pp. 1–20, Springer-Verlag, 2005.
[21] E. Tromer, D. Osvik, and A. Shamir, “Eﬃcient cache attacks on AES, and countermeasures,” J. of Cryptology, vol. 23, no. 1, pp. 37–71, 2010.
[22] A. Tannous, J. Trostle, M. N. Hassan, S. E. McLaughlin, and T. Jaeger, “New side channels targeted at passwords,” in Proc. of the 2008 Annu. Comput.
Security Appl. Conf., ACSAC ’08, (Washington, DC, USA), pp. 45–54, IEEE
Comput. Soc., 2008.
[23] J. E. Smith and A. R. Pleszkun, “Implementation of precise interrupts in pipelined processors,” SIGARCH Comput. Archit. News, vol. 13, no. 3, pp. 36–44, 1985.

94
[24] W. Hwu and Y. N. Patt, “Hpsm, a high performance restricted data ﬂow architecture having minimal functionality,” SIGARCH Comput. Archit. News, vol. 14, pp. 297–306, May 1986.
[25] R. M. Tomasulo, “An eﬃcient algorithm for exploiting multiple arithmetic units,” IBM J. Res. Dev., vol. 11, no. 1, pp. 25–33, 1967.
[26] Amazon, “Amazon ec2 instances.” Online, Dec. 2014.
[27] Y. Tsunoo, T. Saito, T. Suzaki, and M. Shigeri, “Cryptanalysis of des implemented on computers with cache,” in Springer LNCS Proc. of CHES, pp. 62–76, Springer-Verlag, 2003.
[28] D. Grunwald and S. Ghiasi, “Microarchitectural denial of service: insuring microarchitectural fairness,” in Proc. 35th Annu. IEEE/ACM Int. Symp. on
Microarchitecture, pp. 409–418, 2002.
[29] J. Wu, L. Ding, Y. Wu, N. Min-Allah, S. U. Khan, and Y. Wang, “C2detector:
a covert channel detection framework in cloud computing,” Security and
Communication Networks, vol. 7, no. 3, pp. 544–557, 2014.
[30] M. Gander, M. Felderer, B. Katt, A. Tolbaru, R. Breu, and A. Moschitti,
“Anomaly detection in the cloud: Detecting security incidents via mach.
learning,” in Trustworthy Eternal Syst. via Evolving Software, Data and
Knowledge (A. Moschitti and B. Plank, eds.), vol. 379 of Commun. in Comput.
and Inform. Sci., pp. 103–116, Springer Berlin Heidelberg, 2013.
[31] D. Molnar, M. Piotrowski, D. Schultz, and D. Wagner, “The program counter security model: Automat. detection and removal of control-ﬂow side channel attacks,” ICISC’05, (Berlin, Heidelberg), pp. 156–168, Springer-Verlag, 2006.

95
[32] C.-Y. Tseng, P. Balasubramanyam, C. Ko, R. Limprasittiporn, J. Rowe, and
K. Levitt, “A speciﬁcation-based intrusion detection syst. for aodv,” in Proc. of the 1st ACM Workshop on Security of Ad Hoc and Sensor Networks, SASN ’03,
(New York, NY, USA), pp. 125–134, ACM, 2003.
[33] S. Naval, V. Laxmi, M. S. Gaur, and P. Vinod, “Spade: Signature based packer detection,” in Proc. of the 1st Int. Conf. on Security of Internet of Things,
SecurIT ’12, (New York, NY, USA), pp. 96–101, ACM, 2012.
[34] L. H´elou¨et and A. Roumy, “Covert channel detection using information theory,” arXiv preprint arXiv:1102.5586, 2011.
[35] R. Lanotte, A. Maggiolo-Schettini, and A. Troina, “Time and probability-based inform. ﬂow anal.,” IEEE Trans. Softw. Eng., vol. 36, no. 5, pp. 719–734, 2010.
[36] N. Lawson, “Side-channel attacks on cryptographic software,” IEEE Security
Privacy, vol. 7, pp. 65–68, Nov. 2009.
[37] M. Saher and J. Pathak, “Malware and exploit campaign detection sys. and method.” U.S. Patent 20150074810, March, 12, 2015.
[38] I. Kyte, P. Zavarsky, D. Lindskog, and R. Ruhl, “Enhanced side-channel analysis method to detect hardware virtualization based rootkits,” in Internet
Security (WorldCIS), 2012 World Congr. on, pp. 192–201, June 2012.
[39] R. Martin, J. Demme, and S. Sethumadhavan, “Timewarp: Rethinking timekeeping and performance monitoring mechanisms to mitigate side-channel attacks,” in Proc. of the 39th Annu. Int. Symp. on Comput. Architecture, ISCA
’12, (Washington, DC, USA), pp. 118–129, IEEE Comput. Soc., 2012.
[40] T. Kim, M. Peinado, and G. Mainar-Ruiz, “Stealthmem: Syst.-level protection against cache-based side channel attacks in the cloud,” in Proc. of the 21st

96
USENIX Conf. on Security Symp., Security’12, (Berkeley, CA, USA), pp. 11–11, USENIX Assoc., 2012.
[41] V. Varadarajan, T. Ristenpart, and M. Swift, “Scheduler-based defenses against cross-vm side-channels,” in 23rd USENIX Security Symp. (USENIX
Security 14), (San Diego, CA), pp. 687–702, USENIX Assoc., 2014.
[42] M. Milenkovi´c, A. Milenkovi´c, and E. Jovanov, “Using instruction block signatures to counter code injection attacks,” ACM SIGARCH Comput.
Architecture News, vol. 33, no. 1, pp. 108–117, 2005.