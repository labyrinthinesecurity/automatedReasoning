# Automated reasoning for native Cloud, scalable security automation

![alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/reasoning.jpeg)

## What is automated reasoning?

Automated reasoning solves problems as if they were mathematical proofs. It leverages solvers based on Satisfiability Modulo Theories (SMT).
There are many solvers around, the one I'm using is Z3. It is fitted with many built-in theories and is quite easy to use in Python:

```
import z3
sol=Solver()
```

I have written a primer which should get you started: https://www.linkedin.com/pulse/primer-automated-reasoning-cloud-engineers-christophe-parisel

## How Z3 and SMT solvers work?

Say you want to solve a problem involving two expressions: y < x+5 and y > x + 3

With the help of ***congruence closure***, the solver will place each expression in its own equivalence class, then it will try to transform the expressions to put them into a smal number of equivalence classes. THis process is called ***unification***

Here we have only 2 equivalence classes, so we just need to find a way to unify them into a single class. If we manage to do so, then we will have found a solution to our problme.

Unification works as follows: depending on the nature of the expressions at hand, the solver will use the rules of a ***theory*** to transform the expressions and put them into normal form. 

In our example, te expressions deal with integers, so the solver will use the rules of the ***natural numbers theory***, things like distributivity, commutativity, etc

## What can it bring to native Cloud control frameworks?

### The legacy, non-native way
Here is the usual approach you take to implement a control:
- design the control
- build it
- run it continuously in-place
- manage anomalies
- manage false positives
- record detailed control execution for forensic analysis and/or audits- conduct change management as program increments (PIs)

### A cloud native way
Now with automated reasoning, since you operate **anything-as-cod**e (infrastructure-as-code at least),
chances are you may translate your control objective into a mathematical formula to be proven by an unsupervised, automated solver. A new avenue unlocks for your team:
- design the formula
- feed it from authoritative sources (“axioms”): ground truth + static data- prove it continuously
- manage anomalies as unproven theorems (“nontheorems”)
- conduct change management as what-if scenarios

### Expected benefits
- no false positives
- lightweight, powerful change management
- eligible to quantum speedup
- no need to keep records for forensic analysis and/or audits (only
execution timestamps and anomalies)

Automation (because it is unattended), scalability and formal verifications. The latter is notably useful for auditors.

## What you will find in this repository

Here you will find two kinds of material:
- ***recipes*** for illustrating how to implement basic, resuable patterns
- ***control designs*** explain how to implement actual security or compliance controls from the ground up

## References

- Azure: A practical Automated Reasoning implementation in Azure Networking + what-if scenarios: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/secguru.pdf
- AWS: Be curious about automated reasoning by Werner Vogels https://www.allthingsdistributed.com/2022/03/curious-about-automated-reasoning.html

## License information

The top image is copyright Adobe Photo Stock. Used with permission. 

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
