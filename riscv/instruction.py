"""
Describes all Risc V ISA instructions as Python objects
"""
from dataclasses import dataclass


@dataclass
class InstructionI:
    """
    Represents I instructions
    """

    opcode: int
    rd: str
    funct3: int
    rs1: str
    imm: int

    def execute(self, rs1):
        """Calls risc machine to execute this instruction"""
        return rs1 + self.imm


@dataclass
class InstructionR:
    """
    Represents R instructions
    """

    opcode: int
    rd: str
    funct3: int
    rs1: str
    rs2: str
    funct7: int

    def execute(self, rs1, rs2):
        """Calls risc machine to execute this instruction"""
        out = None
        if self.funct3 == int("000", 2):
            out = rs1 + rs2
        elif self.funct3 == int("001", 2):
            out = rs1 << rs2
        return out


@dataclass
class InstructionU:
    """
    Represents U instructions
    """

    opcode: int
    rd: str
    imm: int

    def execute(self):
        """Calls risc machine to execute this instruction"""
        return (self.imm >> 12) << 12


@dataclass
class InstructionJ:
    """
    Represents J instructions
    """

    offset: int
    rd: str

    def execute(self):
        """Calls risc machine to execute this instruction"""
        return self.offset
