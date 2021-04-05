"""
This module is used to generate code to be read by the risc machine
"""

from riscv.instruction import (
    InstructionI,
    InstructionJ,
    InstructionR,
    InstructionU,
    InstructionS,
)


class RiscCompiler:
    """
    Creates assembly code to be read by the risc machine.
    Enter a command via the enter_input function
    """

    def __init__(self):
        self.program_memory = []

    def enter_input(self, op, first, second=None, third=None):
        """
        Enter an assembly command thru this function. For instance:
        enter_input("ADDI", "x0", "x0", 6)
        To write all instructions to a program memory, use createoutput()
        """
        if op == "ADDI":
            self.program_memory.append(
                InstructionI(
                    opcode=int("0010011", 2),
                    rd=first,
                    funct3=int("000", 2),
                    rs1=second,
                    imm=third,
                )
            )
        elif op == "ADD":
            self.program_memory.append(
                InstructionR(
                    opcode=int("0110011", 2),
                    rd=first,
                    funct3=int("000", 2),
                    rs1=second,
                    rs2=third,
                    funct7=int("0000000", 2),
                )
            )
            # self.registers[first] = self.registers[second] + self.registers[third]
        elif op == "SLL":
            self.program_memory.append(
                InstructionR(
                    opcode=int("0110011", 2),
                    rd=first,
                    funct3=int("001", 2),
                    rs1=second,
                    rs2=third,
                    funct7=int("0000000", 2),
                )
            )
            # self.registers[first] = self.registers[second] << self.registers[third]
        elif op == "LUI":
            self.program_memory.append(
                InstructionU(opcode=int("0110111", 2), rd=first, imm=second)
            )
            # self.registers[first] = (second >> 12) << 12

        elif op == "JAL":
            self.program_memory.append(InstructionJ(offset=second, rd=first))

        elif op == "SW":
            self.program_memory.append(
                InstructionS(
                    opcode=int("0100011", 2),
                    imm=second,
                    rs1=third,
                    rs2=first,
                    funct3=int("010", 2),
                )
            )

        elif op == "LW":
            self.program_memory.append(
                InstructionI(
                    opcode=int("0000011", 2),
                    rd=first,
                    rs1=third,
                    funct3=int("010", 2),
                    imm=second,
                )
            )

    def createoutput(self):
        """
        Writes a program to memory
        """
        return self.program_memory
