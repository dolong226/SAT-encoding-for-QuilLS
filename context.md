# CLAUDE.md

## Project Identity

QuilLS-SAT is a **research reimplementation** of the 2025 arXiv paper:

> Depth-Optimal Quantum Layout Synthesis as SAT

The goal of this repository is to faithfully reconstruct the SAT encoding
described in the paper, independently from the original QuilLS implementation.

This is a **student research project** focused on:

- understanding the encoding design
- reproducing constraints exactly
- experimenting with SAT formulations

This repository is NOT a production system.

---

## Primary Goals

1. Correct reproduction of the paper encoding
2. Readable implementation aligned with mathematical formulation
3. Easy future experimentation and extension

Priority order:
Correctness > Readability > Extensibility > Performance


---

## Explicit Non-Goals

Claude MUST NOT assume this repository aims to:

- build a full quantum compiler
- reproduce the entire QuilLS system
- optimize runtime performance
- introduce complex abstractions
- redesign architecture

---

## Core Design Philosophy

- Keep variable names identical to the paper
- Constraints should map directly to equations
- Code should read like the encoding description
- Prefer explicit logic over clever abstractions
- SAT variables must remain visible and understandable

The repository intentionally favors clarity over engineering sophistication.

---

## Project Pipeline

.qasm → parser → dependency DAG → SAT encoding → SAT solver → decoded schedule

---

## Repository Structure
quills-sat/
│
├── src/
│ │
│ ├── encoding/ # Core SAT encoding (heart of repo)
│ │ ├── variables.py # Boolean variables:
│ │ │ mp, oc, et, ut, ct, at, dt, sw, st, asm
│ │ ├── mapping.py # Constraints 1–3: logical ↔ physical mapping
│ │ ├── connectivity.py # Constraints 4–5: hardware connectivity
│ │ ├── gates.py # Constraints 6–12: scheduling & DAG ordering
│ │ ├── swaps.py # Constraints 13–19: 3-step SWAP semantics
│ │ ├── assumptions.py # Constraint 20: incremental SAT assumptions
│ │ └── helpers.py # AtMostOne / ExactlyOne / AtMostN utilities
│ │
│ ├── circuit/ # Input quantum circuit model
│ │ ├── parser.py # .qasm parsing
│ │ ├── dag.py # Dependency DAG construction
│ │ └── gate.py # Gate abstraction
│ │
│ ├── platform/ # Hardware coupling graph
│ │ ├── topology.py
│ │ └── presets.py
│ │
│ ├── solver.py # Incremental SAT loop (Algorithm 1)
│ └── main.py # CLI entrypoint
│
├── tests/ # Constraint correctness tests
├── benchmarks/ # Evaluation circuits
├── pyproject.toml
└── README.md


---
========================================================================
## Current Implementation Status

This section tracks what is already implemented.
Claude MUST read this before proposing new code.

---

### circuit/

gate.py
  class GateType(Enum):
      UNARY = 1
      CX = 2
      # SWAP, CXX

  class Gate
  var: gate_id, name, gate_type, qubits
  func: is_unary, is_cx, control_qubit, target_qubit, str, repr


---

### platform/
topology.py
  class Topology:
    var: n_qubits, edges, adjacency
    func: post_init, is_connectedm neighbors, degree, shortest_distance, nodes, edge_set, str

preset.py
  func: line_topology, grid_2x2, ibmq_tenerife
====================================================================================
---
## Naming Rules

Claude MUST follow:

- Keep SAT variable names identical to the paper notation
- Constraint files correspond directly to constraint numbering
- Avoid renaming mathematical concepts
- Prefer explicit loops over hidden abstractions

---

## Rules Claude MUST Follow

### DO

- preserve repository structure
- keep encoding logic explicit
- match paper semantics exactly
- add comments when logic is unclear
- ask clarification questions when uncertain

### DO NOT

- change constraint logic
- optimize encodings
- refactor architecture
- introduce abstraction layers
- hide SAT variables behind classes
- rename variables from the paper
- rewrite working code unnecessarily

---

## When Code Is Unclear

Claude SHOULD:

1. Ask questions first
2. Refer to paper semantics
3. Add explanatory comments
4. Avoid speculative implementations

Claude MUST NOT guess missing logic.

---

## Editing Philosophy

This repository behaves more like a **research notebook**
than a production software project.

Correctness and traceability to the paper always dominate
engineering elegance.
