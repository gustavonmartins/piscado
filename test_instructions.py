from risc_machine import RiscMachine


def test_arithmetic():
    rm = RiscMachine()

    assert rm.inspect_register("x0") == 0

    rm.enter_cmd(("ADDI","x1","x0",5))
    assert rm.inspect_register("x1") == 5

    rm.enter_cmd(("ADDI","x2","x1",6))
    assert rm.inspect_register("x2") == 11

    rm.enter_cmd(("ADDI","x0","x1",6))
    assert rm.inspect_register("x0") == 0

def test_arithmetic_register_to_register():
    rm=RiscMachine()

    rm.enter_cmd(("ADDI","x1","x0",50))
    rm.enter_cmd(("ADDI","x2","x0",60))
    rm.enter_cmd(("ADD","x3","x1","x2"))
    assert rm.inspect_register("x3") == 110

def test_shift_left_left():
    rm=RiscMachine()  

    rm.enter_cmd(("ADDI","x1","x0",int('00000000000000000000000000001100',2)))
    rm.enter_cmd(("ADDI","x2","x0",2))
    rm.enter_cmd(("SLL","x3","x1","x2"))
    assert rm.inspect_register("x3") == int('00000000000000000000000000110000',2)

    rm.enter_cmd(("ADDI","x1","x0",int('00000000000000000000000000011100',2)))
    rm.enter_cmd(("ADDI","x2","x0",2))
    rm.enter_cmd(("SLL","x3","x1","x2"))
    assert rm.inspect_register("x3") == int('00000000000000000000000001110000',2)

    rm.enter_cmd(("ADDI","x1","x0",int('00000000000000000000000001011100',2)))
    rm.enter_cmd(("ADDI","x2","x0",2))
    rm.enter_cmd(("SLL","x3","x1","x2"))
    assert rm.inspect_register("x3") == int('00000000000000000000000101110000',2)

def test_load_upper_immediate():
    rm=RiscMachine()  
    rm.enter_cmd(("LUI","x1",int('FFEECCDD',16)))
    assert rm.inspect_register("x1")==int('FFEEC000',16)