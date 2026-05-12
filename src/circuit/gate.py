# Gate object
from enum import Enum
from typing import Tuple, List

class GateType(Enum):
    """Define quantum gates"""
    UNARY = 1
    CX = 2
    # SWAP, CXX

class Gate:

    def __init__(self, gate_id: int, name: str, gate_type: GateType, qubits: Tuple[int, ...]):
        self.gate_id = gate_id
        self.name = name
        self.gate_type = gate_type
        self.qubits = qubits

    @property
    def is_unary(self) -> bool:
        return self.gate_type == GateType.UNARY

    @property
    def is_cx(self) -> bool:
        return self.gate_type == GateType.CX

    @property
    def control_qubit(self) -> int:
        if not self.is_cx:
            raise ValueError(f"Không phải cổng CX")
        
        return self.qubits[0]

    @property
    def target_qubit(self) -> int:
        if not self.is_cx:
            raise ValueError(f"Không phải cổng CX")
        
        return self.qubits[1]

    def __str__(self) -> str:
        """
        Trả về chuỗi biểu diễn của cổng.
        Ví dụ: "g_1: CX(q0, q1)" hoặc "g_2: H(q2)"
        """
        qubit_str = ", ".join(f"q{q}" for q in self.qubits)

        return f"g_{self.gate_id}: {self.name}({qubit_str})"
        
    def __repr__(self) -> str:
        """
        Trả về chuỗi đại diện nội bộ của object.
        """
        return (
            f"Gate("
            f"gate_id={self.gate_id}, "
            f"name='{self.name}', "
            f"gate_type={self.gate_type}, "
            f"qubits={self.qubits}"
            f")"
        )