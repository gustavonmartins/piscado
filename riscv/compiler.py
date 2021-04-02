"""
This module is used to generate code to be read by the risc machine
"""

from riscv.instruction import InstructionI, InstructionJ, InstructionR, InstructionU


class RiscCompiler:
    """
    Creates assembly code to be read by the risc machine.
    Enter a command via the enter_input function
    """

    def __init__(self):
        self.program_memory = []

    def enter_input(self, op, a, b=None, c=None):
        """
        Enter an assembly command thru this function. For instance:
        enter_input("ADDI", "x0", "x0", 6)
        To write all instructions to a program memory, use createoutput()
        """
        if op == "ADDI":
            self.program_memory.append(
                InstructionI(
                    opcode=int("0010011", 2), rd=a, funct3=int("000", 2), rs1=b, imm=c
                )
            )
        elif op == "ADD":
            self.program_memory.append(
                InstructionR(
                    opcode=int("0110011", 2),
                    rd=a,
                    funct3=int("000", 2),
                    rs1=b,
                    rs2=c,
                    funct7=int("0000000", 2),
                )
            )
            # self.registers[a] = self.registers[b] + self.registers[c]
        elif op == "SLL":
            self.program_memory.append(
                InstructionR(
                    opcode=int("0110011", 2),
                    rd=a,
                    funct3=int("001", 2),
                    rs1=b,
                    rs2=c,
                    funct7=int("0000000", 2),
                )
            )
            # self.registers[a] = self.registers[b] << self.registers[c]
        elif op == "LUI":
            self.program_memory.append(
                InstructionU(opcode=int("0110111", 2), rd=a, imm=b)
            )
            # self.registers[a] = (b >> 12) << 12

        elif op == "JAL":
            self.program_memory.append(InstructionJ(offset=b, rd=a))

    def createoutput(self):
        """
        Writes a program to memory
        """
        return self.program_memory