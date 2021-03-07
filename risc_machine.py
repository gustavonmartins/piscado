class RiscMachine:
    def __init__(self):
        self.registers={"x0": 0, "x1":0, "x2":0}

    def enter_cmd(self, cmd):
        if len(cmd)==4:
            (op, a, b,c) = cmd
            if op=="ADDI" and a != "x0":
                self.registers[a] = self.registers[b]+c
            elif op=="ADD" and a != "x0":
                self.registers[a] = self.registers[b]+self.registers[c]
            elif op=="SLL"  and a != "x0":
                self.registers[a] = self.registers[b] << self.registers[c]

        elif len(cmd)==3:
            (op, a, b) = cmd
            if op=="LUI" and a != "x0":
                self.registers[a]=(b >>12)<<12


    def inspect_register(self, register):
        return self.registers.get(register)
