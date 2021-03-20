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

    def execute(self, rs1, rs2):
        if self.funct3 == int("000", 2):
            return rs1 + rs2
        elif self.funct3 == int("001", 2):
            return rs1 << rs2


@dataclass
class InstructionU:
    opcode: int
    rd: str
    imm: int

    def execute(self):
        return (self.imm >> 12) << 12


@dataclass
class InstructionJ:
    offset: int
