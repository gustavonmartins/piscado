"""
This implements a machine able of executing Risc V instructions
"""
from riscv.instruction import (
    InstructionI,
    InstructionR,
    InstructionU,
    InstructionJ,
)


class RiscMachine:
    """
    This implements a machine able of executing Risc V instructions.
    Needs to be passed
    """

    def __init__(self, program=None):
        self.registers = {"x0": 0, "x1": 0, "x2": 0, "x5": 0, "x10": 0}
        self.program_memory = program
        self.pc = 0
        self.ir = None
        self.mar = None
        self.mdr = None

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
        rd = current_instruction.rd
        if isinstance(current_instruction, InstructionI):
            if rd != "x0":
                rs1_value = self.registers[current_instruction.rs1]
                self.registers[rd] = current_instruction.execute(rs1_value)

        if isinstance(current_instruction, InstructionR):
            if rd != "x0":
                rs1_value = self.registers[current_instruction.rs1]
                rs2_value = self.registers[current_instruction.rs2]
                self.registers[rd] = current_instruction.execute(
                    rs1_value,
                    rs2_value,
                )

        if isinstance(current_instruction, InstructionU):
            if rd != "x0":
                self.registers[rd] = current_instruction.execute()

        if isinstance(current_instruction, InstructionJ):
            if rd != "x0":
                self.registers[rd] = self.pc
            self.pc += current_instruction.execute() - 1
