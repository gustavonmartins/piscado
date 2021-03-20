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

    def enter_cmd(self, op, a, b=None, c=None):
        if op == "ADDI" and a != "x0":
            self.program_memory.append(
                InstructionI(
                    opcode=int("0010011", 2), rd=a, funct3=int("000", 2), rs1=b, imm=c
                )
            )
        elif op == "ADD" and a != "x0":
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
        elif op == "SLL" and a != "x0":
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
        if op == "LUI" and a != "x0":
            self.program_memory.append(
                InstructionU(opcode=int("0110111", 2), rd=a, imm=b)
            )
            # self.registers[a] = (b >> 12) << 12

        if op == "J":
            self.program_memory.append(InstructionJ(offset=a))

    def inspect_register(self, register):
        return self.registers.get(register)

    def enter_section(self, section):
        pass

    def run(self):
        pass

    def run_one_cycle(self):
        self.fetch()
        self.decode()
        self.execute()

    def fetch(self):
        self.mar = self.pc
        self.mdr = self.program_memory[self.mar]
        self.ir = self.mdr

        # Increase counter for next turn
        self.pc = self.pc + 1

    def execute(self):
        if isinstance(self.ir, InstructionI):
            self.registers[self.ir.rd] = self.registers[self.ir.rs1] + self.ir.imm
        if isinstance(self.ir, InstructionR):
            self.registers[self.ir.rd] = self.ir.execute(
                self.registers[self.ir.rs1], self.registers[self.ir.rs2]
            )
        if isinstance(self.ir, InstructionU):
            self.registers[self.ir.rd] = self.ir.execute()
        if isinstance(self.ir, InstructionJ):
            self.pc += self.ir.offset

    def decode(self):
        pass
