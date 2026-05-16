# src/main.py

"""
Simple test entrypoint for the SAT-based quantum transpiler.

Hiện tại main này dùng để test:
    - QASM parser
    - Circuit representation
    - Dependency DAG
    - Platform topology
    - SAT variable generation
    - Helper functions

"""

from pprint import pprint

# ============================================================
# Circuit
# ============================================================

from circuit.parser import parse_qasm
from circuit.dag import build_dependency_dag

# ============================================================
# Platform
# ============================================================

# hoặc:
# from src.platform.topology import Topology

# ============================================================
# SAT Encoding
# ============================================================

from encoding.variables import VarPool

# helper functions (nếu có)
# from src.encoding.helpers import ...


# ============================================================
# Utility Printers
# ============================================================

def print_circuit(circuit):
    print("\n" + "=" * 60)
    print("CIRCUIT")
    print("=" * 60)

    print(circuit)

    for gate in circuit.gates:
        print(
            f"[g{gate.gate_id:02}] "
            f"{gate.name:<4} "
            f"qubits={gate.qubits}"
        )


def print_dag(dag):
    print("\n" + "=" * 60)
    print("DEPENDENCY DAG")
    print("=" * 60)

    for g in dag.gate_ids:
        succ = dag.successors(g)
        pred = dag.predecessors(g)

        print(
            f"g{g:02} | "
            f"pred={pred} | "
            f"succ={succ}"
        )


def print_transitive_dependencies(dag):
    print("\n" + "=" * 60)
    print("TRANSITIVE DEPENDENCIES")
    print("=" * 60)

    for g in dag.gate_ids:
        print(
            f"g{g:02} | "
            f"full_pred={sorted(dag.full_predecessors(g))} | "
            f"full_succ={sorted(dag.full_successors(g))}"
        )


def print_platform(platform):
    print("\n" + "=" * 60)
    print("PLATFORM")
    print("=" * 60)

    print(platform)

    # Tùy implementation topology của bạn
    if hasattr(platform, "edges"):
        print("Edges:")
        for e in platform.edges:
            print(" ", e)


def print_variables(V):
    print("\n" + "=" * 60)
    print("SAT VARIABLES")
    print("=" * 60)

    # tạo thử vài biến
    vars_to_test = [
        V.mp(0, 1, 0),
        V.mp(1, 2, 0),
        V.sw(1, 2, 3),
        V.c(5, 2),
        V.a(5, 3),
        V.asm(10),
    ]

    for lit in vars_to_test:
        print(
            f"{lit:>4} -> {V.name(lit)}"
        )


# ============================================================
# Main
# ============================================================

def main():

    # ========================================================
    # Parse circuit
    # ========================================================

    qasm_path = "benchmarks/collection/4gt13_92.qasm"

    print(f"\nLoading QASM: {qasm_path}")

    circuit = parse_qasm(qasm_path)

    print_circuit(circuit)

    # ========================================================
    # Build DAG
    # ========================================================

    dag = build_dependency_dag(circuit)

    print_dag(dag)

    print_transitive_dependencies(dag)

    # ========================================================
    # Load platform
    # ========================================================

    # Tùy implementation presets.py của bạn
    #
    # Ví dụ:
    #     get_platform("tokyo")
    #     get_platform("grid_5")
    #

    # ========================================================
    # SAT Variable Pool
    # ========================================================

    V = VarPool()

    print_variables(V)

    # ========================================================
    # Example: dependency checks
    # ========================================================

    print("\n" + "=" * 60)
    print("DEPENDENCY CHECKS")
    print("=" * 60)

    for gate in circuit.gates:

        g = gate.gate_id

        preds = dag.predecessors(g)

        if preds:
            print(
                f"Gate g{g} depends on {preds}"
            )
        else:
            print(
                f"Gate g{g} has no dependencies"
            )

    # ========================================================
    # Example: CX gates
    # ========================================================

    print("\n" + "=" * 60)
    print("CX GATES")
    print("=" * 60)

    for gate in circuit.gates:

        if gate.name == "cx":

            q1, q2 = gate.qubits

            print(
                f"g{gate.gate_id}: "
                f"CX({q1}, {q2})"
            )

    print("\nDone.\n")


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()