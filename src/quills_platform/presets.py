# Standard topologies: line, tenerife, guadalupe,...
from quills_platform.topology import Topology

def line_topology(n: int) -> Topology:
    edges = [(i, i+1) for i in range (n-1)]

    return Topology(n_qubits=n, edges=edges)

def grid_2x2() -> Topology:

    return Topology(
        num_qubits=4,
        edges=[
            (0, 1),
            (0, 2),
            (1, 3),
            (2, 3)
        ]
    )


def ibmq_tenerife() -> Topology:

    return Topology(
        num_qubits=5,
        edges=[
            (0, 1),
            (1, 2),
            (1, 3),
            (3, 4)
        ]
    )