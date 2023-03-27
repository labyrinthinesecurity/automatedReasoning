# Continuous Control Monitoring (SOC 2, PCI-DSS, ...)

Phil Venables outlines the importance of continuous control monitoring as [Force 4 of cybersecurity](https://www.philvenables.com/post/fighting-security-entropy):

  ![Force 4](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/controls/ContinuousCompliance/Force4.PNG)
  
## Automating Master Data

In the PaaS Cloud, we can leverage a huge opportunity to automate the monitoring of many security and compliance controls: Cloud providers keep up a realtime, comprehensive CMDB of customer assets. APIs like **Azure Resource Graph**, **AWS resources explorer** or **steampipe** are easy and fast to query.

In fact, these APIs have become the actual Master Data of all our deployed assets: they are the *ground truth*. We must feed our cloud IT security and compliance controls with their inputs.

## Compliance Continuum

For a control to be 'compliant' to any certification standard, it must meet two critical criteria:
- spacial compliance: this is the usual way we see control operations. The control must be reliable and comprehensive with regards its functional scope. For example, if a control is supposed to enforce a Bastion for remote access, this control must have no possible bypass (by a legacy network access point, by small group of privileged users, by non-standard ports/encapsulation, etc)
- temporal compliance: the control must have no continuity break over the certification period (eg: a 6 months SOC2 certification perdio).

## Automated Cloud Compliance Continuum
