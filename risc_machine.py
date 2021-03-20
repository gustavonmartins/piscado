from instruction import InstructionI, InstructionR, InstructionU, InstructionJ


class RiscMachine:
    def __init__(self):
        self.registers = {"x0": 0, "x1": 0, "x2": 0}
        self.program_memory = []
        self.pc = 0
        self.ir = None
        self.mar = None
        self.mdr = None

        # Useful when creating code
        self.writer_pc = 0

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
        if isinstance(self.ir, InstructionI):
            if self.ir.rd != "x0":
                self.registers[self.ir.rd] = self.ir.execute(
                    self.registers[self.ir.rs1]
                )
        if isinstance(self.ir, InstructionR):
            if self.ir.rd != "x0":
                self.registers[self.ir.rd] = self.ir.execute(
                    self.registers[self.ir.rs1], self.registers[self.ir.rs2]
                )
        if isinstance(self.ir, InstructionU):
            if self.ir.rd != "x0":
                self.registers[self.ir.rd] = self.ir.execute()
        if isinstance(self.ir, InstructionJ):
            self.pc += self.ir.offset
