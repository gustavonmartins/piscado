"""
This implements a machine able of executing Risc V instructions
"""
from riscv.instruction import (
    InstructionI,
    InstructionR,
    InstructionU,
    InstructionJ,
    InstructionS,
)


class RiscMachine:
    """
    This implements a machine able of executing Risc V instructions.
    Load it with a program first, then execute cycles to see it running
    """

    def __init__(self, program=None):
        self.registers = {"x0": 0, "x1": 0, "x2": 0, "x5": 0, "x9": 0, "x10": 0}
        self.program_memory = program
        self.pc = 0
        self.ir = None
        self.mar = None
        self.mdr = None
        self.program_secondary_memory = [None] * 2048

    def inspect_register(self, register):
        """
        Allows user to see contents of a specific register
        """
        return self.registers.get(register)

    def run_one_cycle(self):
        """
        Executes one instructions. Needs to be run as many times as instructions
        """
        self._fetch()
        # self.decode()
        self._execute()

    def _fetch(self):
        self.mar = self.pc
        self.mdr = self.program_memory[self.mar]
        self.ir = self.mdr

        # Increase counter for next turn
        self.pc = self.pc + 1

    def _execute(self):
        current_instruction = self.ir
        if isinstance(current_instruction, InstructionI):
            rd = current_instruction.rd
            if rd != "x0":
                rs1_value = self.registers[current_instruction.rs1]
                if current_instruction.opcode == int("0010011", 2):
                    self.registers[rd] = current_instruction.execute(rs1_value)
                elif current_instruction.opcode == int("0000011", 2):
                    memory_position = current_instruction.execute(rs1_value)
                    self.registers[rd] = self.program_secondary_memory[memory_position]

        if isinstance(current_instruction, InstructionR):
            rd = current_instruction.rd
            if rd != "x0":
                rs1_value = self.registers[current_instruction.rs1]
                rs2_value = self.registers[current_instruction.rs2]
                self.registers[rd] = current_instruction.execute(
                    rs1_value,
                    rs2_value,
                )

        if isinstance(current_instruction, InstructionU):
            rd = current_instruction.rd
            if rd != "x0":
                self.registers[rd] = current_instruction.execute()

        if isinstance(current_instruction, InstructionJ):
            rd = current_instruction.rd
            if rd != "x0":
                self.registers[rd] = self.pc
            self.pc += current_instruction.execute() - 1

        if isinstance(current_instruction, InstructionS):
            rd = current_instruction.rs2
            if rd != "x0":
                target_pos_on_memory = (
                    self.registers[current_instruction.rs1] + current_instruction.imm
                )
                self.program_secondary_memory[target_pos_on_memory] = self.registers[
                    current_instruction.rs2
                ]
