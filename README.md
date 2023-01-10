# Automated reasoning for native Cloud, scalable security automation

This repository contains two kinds of material:
- ***recipes*** for illustrating how to implement specific patterns
- ***control designs*** 

## An introduction to automated reasoning

Automated reasoning solves problems like mathematical proofs. It leverages unattended solvers based on Satisfiability Modulo Theories (SMT).
There are many solvers around, the one I'm using is Z3. It is fitted within many built-in theories and is quite easy to use in Python:

```
import z3
sol=Solver()
```


## What can it bring to Cloud customers?

Automation (because it is unattended), scalability and formal verifications. The latter is notably useful for auditors.

## References

- Azure: A practical Automated Reasoning implementation in Azure Networking + what-if scenarios: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/secguru.pdf
- AWS: Be curious about automated reasoning by Werner Vogels https://www.allthingsdistributed.com/2022/03/curious-about-automated-reasoning.html

## License information

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
