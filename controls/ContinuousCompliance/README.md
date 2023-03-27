# Continuous Control Monitoring (SOC 2, PCI-DSS, ...)

Phil Venables outlines the importance of continuous control monitoring as [Force 4 of cybersecurity](https://www.philvenables.com/post/fighting-security-entropy):

  ![Force 4](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/controls/ContinuousCompliance/Force4.PNG)
  
## Automating Master Data

In the PaaS Cloud, we can leverage a huge opportunity to automate the monitoring of many security and compliance controls: Cloud providers keep up a realtime, comprehensive CMDB of customer assets. APIs like **Azure Resource Graph**, **AWS resources explorer** or **steampipes** are easy and fast to query.

In fact, these APIs have become the actual Master Data of all our deployed assets: they are the *ground truth*. 

A key Cloud security and commpliance principle is that we must feed our controls with ground truth.

## Compliance Continuum

For a control to be 'compliant' to any certification standard, it must meet two critical criteria:
- **spacial compliance**: this is the usual way we see control operations. The control must be reliable and comprehensive with regards its functional scope. For example, if a control is supposed to enforce a Bastion for remote access, this control must have no possible bypass (by a legacy network access point, by small group of privileged users, by non-standard ports/encapsulation, etc)
- **temporal compliance**: the control must have no continuity break over the certification period (eg: a 6 months SOC2 certification period).

## Automating Cloud Compliance Continuum

Automated reasoning is a new and powerful way to perform **unsupervised** control monitoring on infrastructure-as-code assets.

A very nice and useful feature of this technology is that we can use it to provide proofs of control execution on both spacial and temporal axis:

- the "HubAndSpoke" control is an example of how to conduct automated reasoning on the spacial axis. It **proves** that a specific Cloud security pattern (the Hub & Spoke pattern) is enforced in an Azure Tenant or an AWS organization.
- the "ContinuousCompliance" control is an example of how to conduct automated reasoning on the temporal axis. It **proves** that a specific control is enforced continuously over a period.

**Combining both controls into one let us prove compliance over the whole continuum**. 

Not only does it expand the traditional way we handle controls by adding the temporal dimension, but it also delivers undisputable proofs to auditors and human controlers. All this without using up any manpower! Except of course for handling anomalies.
