# Beethoven X

 Deployment Review
 February 4, 2022
 Prepared for:
 Daniel Mk
 Beethoven X
 Mr. Kind Human
 Beethoven X
 Prepared by:
 Simone Monica

 About Trail of Bits
 Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high- end security research with a real -world attacker mentality to reduce risk and fortify code. With 80+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
 We maintain an exhaustive list of publications at  https://github.com/trailofbits/publications , with links to papers, presentations, public audit reports, and podcast appearances.
 In recent years, Trail of Bits consultants have showcased cutting-edge research through presentations at CanSecWest, HCSS, Devcon, Empire Hacking, GrrCon, LangSec, NorthSec, the O’Reilly Security Conference, PyCon, REcon, Security BSides, and SummerCon.
 We specialize in software testing and code review projects, supporting client organizations in the technology, defense, and ﬁnance industries, as well as government entities. Notable clients include HashiCorp, Google, Microsoft, Western Digital, and Zoom.
 Trail of Bits also operates a center of excellence with regard to blockchain security. Notable projects include audits of Algorand, Bitcoin SV, Chainlink, Compound, Ethereum 2.0,
 MakerDAO, Matic, Uniswap, Web3, and Zcash.
 To keep up to date with our latest news and announcements, please follow  @trailofbits  on
 Twitter and explore our public repositories at  https://github.com/trailofbits .  To engage us directly, visit our “Contact” page at  https://www.trailofbits.com/contact ,  or email us at info@trailofbits.com .
 Trail of Bits, Inc.
 228 Park Ave S #80688
 New York, NY 10003 https://www.trailofbits.com info@trailofbits.com
 Trail of Bits 1

 Notices and Remarks
 Copyright and Distribution
 © 2022 by Trail of Bits, Inc.
 All rights reserved. Trail of Bits hereby asserts its right to be identiﬁed as the creator of this report in the United Kingdom.
 This report is considered by Trail of Bits to be public information; it is licensed to  Beethoven
 X  under the terms of the project statement of work  and has been made public at
 Beethoven X’s request. Material within this report may not be reproduced or distributed in part or in whole without the express written permission of Trail of Bits.
 Test Coverage Disclaimer
 All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and mutually agreed upon project plan.
 Security assessment projects are time-boxed and often reliant on information that may be provided by a client, its aﬃliates, or its partners. As such, the ﬁndings documented in this report should not be considered a comprehensive list of security issues, ﬂaws, or defects in the target system or codebase.
 Trail of Bits 2

 Table of Contents
 About Trail of Bits 1
 Notices and Remarks 2
 Table of Contents 3
 Executive Summary 4
 Project Summary 5
 Project Targets 6
 Summary of Recommendations 7
 A. Incident Response Recommendations 8
 Trail of Bits 3

 Executive Summary
 Overview
 Beethoven X engaged Trail of Bits to review the deployment of its smart contracts. From
 January 31 to February 4, 2022, one consultant conducted a review of the client-provided source code, with one person-week of eﬀort. Details of the project’s timeline and test targets are provided in subsequent sections of this report.
 Project Scope
 Our testing eﬀorts were focused on the identiﬁcation of ﬂaws related to a misconﬁgured deployment that could result in a compromise of the target system; however, the implementations of the contracts were out of scope. We also sought to conﬁrm that the deployed contracts are a correct Balancer V2 fork.
 Summary of Findings
 The review did not uncover any deployment or conﬁguration issues that could impact the system. However, we found that the lack of an incident response plan was problematic (see
 Appendix A ). We also raised concerns regarding the  dynamic fee pool setting on the UI, which could be a front-running opportunity for a malicious pool owner. Finally, the version of Gnosis Safe in use was not up to date with the latest release at the time of the review.
 Trail of Bits 4

 Project Summary
 Contact Information
 The following managers were associated with this project:
 Dan Guido , Account Manager
 Sam Greenup , Project Manager dan@trailofbits.com sam.greenup@trailofbits.com
 The following engineer was associated with this project:
 Simone Monica , Consultant simone.monica@trailofbits.com
 Project Timeline
 The signiﬁcant events and milestones of the project are listed below.
 Date
 Event
 January 28, 2022
 Pre-project kickoﬀ call
 February 4, 2022
 Delivery of report draft
 February 4, 2022
 Report readout meeting
 February 9, 2022
 Delivery of ﬁnal report
 Trail of Bits 5

 Project Targets
 The engagement involved a review of the deployed targets listed below.
 Beethoven X—Deployment
 Repository https://github.com/beethovenxﬁ/balancer-v2-monorepo
 Branches beethovenx-deployments-latest beethovenx-authorizer-helpers
 Versions bbc50d6cb9945f324d86f0fd22ccf91e0dd0e64b 9772f894d1f34619341846d5c074437996201c08
 Type
 Solidity
 Platform
 Ethereum
 The following are the deployed contract addresses in the Fantom network:
 vault 0x20dd72Ed959b6147912C2e529F0a0C6 51c33c9ce protocolFeesCollector 0xC6920d3a369E7c8BD1A22DbE385e11d 1F7aF948F authorizer 0x974D3FF709D84Ba44cde3257C0B5B0b 14C081Ce9 weightedPoolFactory 0x60467cb225092cE0c98936193431117 5f437Cf53 weightedPool2TokensFactory 0x92b377187bcCC6556FceD2f1e6DAd65 850C20630 stablePoolFactory 0x55df810876354Fc3e249f701Dd78DeD
 E57991F8D liquidityBootstrappingPoolFactory 0x458368B3724B5a1c1057A00b28eB03F
 Eb5b64968 metaStablePoolFactory 0x70b55Af71B29c5Ca7e67bD199525036 4C4bE5554
 Trail of Bits 6

 Summary of Recommendations
 Trail of Bits recommends that Beethoven X take the following actions:
 ●  Develop a detailed incident response plan to ensure that the Beethoven X team can promptly address any issues that arise ( Appendix A ).
 ●  Develop a monitoring system to track the contracts’ behavior ( Appendix A ).
 ●  For pools with dynamic fees whose owners are not Beethoven's multisignature wallet, provide a warning in the UI regarding the risks of these pools.
 ●  Update Gnosis Safe to the latest version (1.3).
 Trail of Bits 7

 A. Incident Response Recommendations
 In this section, we provide recommendations around the formulation of an incident response plan.
 ●  Identify who (either speciﬁc people or roles) is responsible for carrying out the mitigations (deploying smart contracts, pausing contracts, upgrading the front end, etc.).
 ○  Specifying these roles will strengthen the incident response plan and ease the execution of mitigating actions when necessary.
 ●  Document internal processes for situations in which a deployed remediation does not work or introduces a new bug.
 ○  Consider adding a fallback scenario that describes an action plan in the event of a failed remediation.
 ●  Clearly describe the intended process of contract deployment.
 ●  Consider whether and under what circumstances Beethoven X will make aﬀected users whole after certain issues occur.
 ○  Such issues could include an individual or aggregate loss, a loss resulting from user error, a contract ﬂaw, and a third-party contract ﬂaw.
 ●  Document how Beethoven X plans keep up to date on new issues, both to inform future development and to secure the deployment toolchain and the external on-chain and oﬀ-chain services that the system relies on.
 ○  For each language and component, describe the noteworthy sources for vulnerability news. Subscribe to updates for each source. Consider creating a special private Discord channel with a bot that will post the latest vulnerability news; this will help the team keep track of updates all in one place. Also consider assigning speciﬁc team members to keep track of the vulnerability news of a speciﬁc component of the system.
 ●  Consider scenarios involving issues that would indirectly aﬀect the system.
 ●  Determine when and how the team would reach out to and onboard external parties (auditors, aﬀected users, other protocol developers, etc.).
 ○  Some issues may require collaboration with external parties to eﬃciently remediate them.
 Trail of Bits 8

 ●  Deﬁne contract behavior that is considered abnormal for oﬀ-chain monitoring.
 ○  Consider adding more resilient solutions for detection and mitigation, especially in terms of speciﬁc alternate endpoints and queries for diﬀerent data as well as status pages and support contacts for aﬀected services.
 ●  Combine issues and determine whether new detection and mitigation scenarios are needed.
 ●  Perform periodic dry runs of speciﬁc scenarios in the incident response plan to
 ﬁnd gaps and opportunities for improvement and to develop muscle memory.
 ○  Document the intervals at which the team should perform dry runs of the various scenarios. For scenarios that are more likely to happen, perform dry runs more regularly. Create a template to be ﬁlled in after a dry run to describe the improvements that need to be made to the incident response plan.
 Trail of Bits 9