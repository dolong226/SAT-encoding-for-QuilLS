# QuilLS-SAT

A lightweight and independent reimplementation inspired by QuilLS.

This project does not aim to reproduce the full original system. 
Its current focus is SAT encoding design, constraint simplification, and experiments with alternative formulations.

## Reference

Original QuilLS repository:
https://github.com/anbclausen/quills

## Pipeline 

.qasm → parser → dependency DAG → SAT encoding → SAT solver → decoded schedule