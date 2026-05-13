# Build dependency graph, compute fullS(g) & fullP(g)
from collections import defaultdict, deque
from dataclasses import dataclass, field

from circuit.parser import Circuit

@dataclass
class DAG:

    # successor adjacency list
    _succ: dict[int, list[int]] = field(default_factory=lambda: defaultdict(list))

    # predecessor adjancency list
    _pred: dict[int, list[int]] = field(default_factory=lambda: defaultdict(list))

    gate_ids: list[int] = field(default_factory=list)

    # Direct Successor
    def successors(self, g: int) -> list[int]:
        return list(self._succ[g])
    
    # Direct predecessors
    def predecessors(self, g: int) -> list[int]:
        return list(self._pred[g])
    
    def full_successors(self, g: int) -> list[int]:
        return self._reachable(self._succ, g)
    
    def full_predecessors(self, g: int) -> list[int]:
        return self._reachable(self._pred, g)

    # Generic Reachability 
    def _reachable(self, adj: dict, start: int) -> list[int]:
        # Tìm toàn bộ node reachable từ start
        # BFS
        visited = set()

        queue = deque(adj[start])

        while queue:

            node = queue.popleft()

            if node not in visited:

                visited.add(node)

                queue.extend(adj[node])

        return list(visited)
    
# DAG Builder

def build_dependency_dag(circuit: Circuit) -> DAG:
    dag = DAG()

    dag.gate_ids = [g.gate_id for g in circuit.gates]

    last_on_qubit: dict[int, int] = {}

    for gate in circuit.gates:

        for qubit in gate.qubits:
            if qubit in last_on_qubit:

                # predecessor trực tiếp
                pred_id = last_on_qubit[qubit]

                # Thêm edge:
                # Tránh duplicate edge
                if gate.gate_id not in dag._succ[pred_id]:

                    dag._succ[pred_id].append(gate.gate_id)

                    dag._pred[gate.gate_id].append(pred_id)
            last_on_qubit[qubit] = gate.gate_id

    return dag