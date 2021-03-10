from dataclasses import dataclass


@dataclass
class InstructionI:
    opcode: int
    rd: str
    funct3: int
    rs1: str
    imm: int


@dataclass
class InstructionR:
    opcode: int
    rd: str
    funct3: int
    rs1: str
    rs2: str
    funct7: int


@dataclass
class InstructionU:
    opcode: int
    rd: str
    imm: int
