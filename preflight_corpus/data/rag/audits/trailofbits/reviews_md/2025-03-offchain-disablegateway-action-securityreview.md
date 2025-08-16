# Offchain DisableGateway Action for

USDT
Security Assessment (Summary Report)
March 12, 2025

Prepared for:​
Harry Kalodner, Steven Goldfeder, and Ed Felten​
Offchain Labs

Prepared by: Gustavo Grieco and Tarun Bansal

Table of Contents
Table of Contents​ 1
Project Summary​ 2
Executive Summary​ 3
About Trail of Bits​ 4
Notices and Remarks​ 5

​
        Trail of Bits​ 1​
Offchain DisableGateway Action for USDT​
        PUBLIC​
​

Project Summary
Contact Information
The following project manager was associated with this project:
Mary O’Brien, Project Manager mary.obrien@trailofbits.com
The following engineering director was associated with this project:​

Josselin Feist, Engineering Director, Blockchain josselin.feist@trailofbits.com
The following consultants were associated with this project:
​
Gustavo Grieco, Consultant​
​
Tarun Bansal, Consultant
​ gustavo.grieco@trailofbits.com​
​ tarun.bansal@trailofbits.com
Project Timeline
The significant events and milestones of the project are listed below.
Date​
Event
February 24, 2025​
Delivery of report draft
February 28, 2025 ​
Report readout meeting
March 12, 2025​
Delivery of final summary report

​
        Trail of Bits​ 2​
Offchain DisableGateway Action for USDT​
        PUBLIC​
​

Executive Summary
Engagement Overview
Offchain Labs engaged Trail of Bits to review the governance action that disables the USDT standard gateway for deposits, in preparation for using USDT0. These changes correspond to PR #334 (873c0e9).
The commit in scope involves setting up a dummy gateway in the token bridge of the
Arbitrum One rollup for USDT. Essentially, this change disables USDT user deposits. The deposits should be already handled by the new USDT infrastructure, named USDT0.
A team of two consultants conducted the review from February 20 to February 21, 2025, for a total of two engineer-days of effort. With full access to source code and documentation, we performed a manual review of the code in scope.
Observations and Impact
The code review uncovered no issues.
We focused our efforts on checking the correct procedure to safely modify the configuration of the token bridge. We also checked if external users could block or delay the action and looked for any exceptional behavior in the (re)execution of retryable tickets needed to complete this configuration change.
We did not review any of the USDT codebase nor its on-chain configuration. This audit focused on the correct interaction between the governance action and the token bridge.
Recommendations
We recommend that Offchain Labs make sure the community is aware of this change.
When the gateway is disabled, it will cause an unexpected revert for either users or third-party integrations.

​
        Trail of Bits​ 3​
Offchain DisableGateway Action for USDT​
        PUBLIC​
​

About Trail of Bits
Founded in 2012 and headquartered in New York, Trail of Bits provides technical security assessment and advisory services to some of the world’s most targeted organizations. We combine high-­end security research with a real­-world attacker mentality to reduce risk and fortify code. With 100+ employees around the globe, we’ve helped secure critical software elements that support billions of end users, including Kubernetes and the Linux kernel.
We maintain an exhaustive list of publications at https://github.com/trailofbits/publications, with links to papers, presentations, public audit reports, and podcast appearances.
In recent years, Trail of Bits consultants have showcased cutting-edge research through presentations at CanSecWest, HCSS, Devcon, Empire Hacking, GrrCon, LangSec, NorthSec, the O’Reilly Security Conference, PyCon, REcon, Security BSides, and SummerCon.
We specialize in software testing and code review projects, supporting client organizations in the technology, defense, and finance industries, as well as government entities. Notable clients include HashiCorp, Google, Microsoft, Western Digital, and Zoom.
Trail of Bits also operates a center of excellence with regard to blockchain security. Notable projects include audits of Algorand, Bitcoin SV, Chainlink, Compound, Ethereum 2.0,
MakerDAO, Matic, Uniswap, Web3, and Zcash.
To keep up to date with our latest news and announcements, please follow @trailofbits on
Twitter and explore our public repositories at https://github.com/trailofbits. To engage us directly, visit our “Contact” page at https://www.trailofbits.com/contact, or email us at info@trailofbits.com.
Trail of Bits, Inc.​ 228 Park Ave S #80688
New York, NY 10003 https://www.trailofbits.com​ info@trailofbits.com

​
        Trail of Bits​ 4​
Offchain DisableGateway Action for USDT​
        PUBLIC​
​

Notices and Remarks
Copyright and Distribution
© 2025 by Trail of Bits, Inc.
All rights reserved. Trail of Bits hereby asserts its right to be identified as the creator of this report in the United Kingdom.
Trail of Bits considers this report public information; it is licensed to Offchain Labs under the terms of the project statement of work and has been made public at Offchain Labs’ request. Material within this report may not be reproduced or distributed in part or in whole without Trail of Bits’ express written permission.
The sole canonical source for Trail of Bits publications is the Trail of Bits Publications page.
Reports accessed through sources other than that page may have been modified and should not be considered authentic.
Test Coverage Disclaimer
All activities undertaken by Trail of Bits in association with this project were performed in accordance with a statement of work and agreed upon project plan.
Security assessment projects are time-boxed and often reliant on information that may be provided by a client, its affiliates, or its partners. As a result, the findings documented in this report should not be considered a comprehensive list of security issues, flaws, or defects in the target system or codebase.
Trail of Bits uses automated testing techniques to rapidly test the controls and security properties of software. These techniques augment our manual security review work, but each has its limitations: for example, a tool may not generate a random edge case that violates a property or may not fully complete its analysis during the allotted time. Their use is also limited by the time and resource constraints of a project.

​
        Trail of Bits​ 5​
Offchain DisableGateway Action for USDT​
        PUBLIC​
​