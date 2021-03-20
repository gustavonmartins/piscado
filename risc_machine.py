from instruction import InstructionI, InstructionR, InstructionU, InstructionJ


class RiscMachine:
    def __init__(self):
        self.registers = {"x0": 0, "x1": 0, "x2": 0}
        self.program_memory = []
        self.pc = 0
        self.ir = None
        self.mar = None
        self.mdr = None

    def inspect_register(self, register):
        return self.registers.get(register)

    def run_one_cycle(self):
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
            if current_instruction.rd != "x0":
                rd = current_instruction.rd
                rs1_value = self.registers[current_instruction.rs1]

                self.registers[rd] = current_instruction.execute(rs1_value)

        if isinstance(current_instruction, InstructionR):
            if current_instruction.rd != "x0":
                rd = current_instruction.rd
                rs1_value = self.registers[current_instruction.rs1]
                rs2_value = self.registers[current_instruction.rs2]
                self.registers[rd] = current_instruction.execute(
                    rs1_value,
                    rs2_value,
                )

        if isinstance(current_instruction, InstructionU):
            if current_instruction.rd != "x0":
                rd = current_instruction.rd
                self.registers[rd] = current_instruction.execute()

        if isinstance(current_instruction, InstructionJ):
            self.pc += current_instruction.execute()
