from risc_machine import RiscMachine


def test_arithmetic_register_to_register():
    rm = RiscMachine()

    rm.enter_cmd("ADDI", "x1", "x0", 50)
    rm.enter_cmd("ADDI", "x2", "x0", 60)
    rm.enter_cmd("ADD", "x3", "x1", "x2")
    assert rm.inspect_register("x3") == 110


def test_shift_left_left():
    rm = RiscMachine()

    rm.enter_cmd("ADDI", "x1", "x0", int("00000000000000000000000000001100", 2))
    rm.enter_cmd("ADDI", "x2", "x0", 2)
    rm.enter_cmd("SLL", "x3", "x1", "x2")
    assert rm.inspect_register("x3") == int("00000000000000000000000000110000", 2)

    rm.enter_cmd("ADDI", "x1", "x0", int("00000000000000000000000000011100", 2))
    rm.enter_cmd("ADDI", "x2", "x0", 2)
    rm.enter_cmd("SLL", "x3", "x1", "x2")
    assert rm.inspect_register("x3") == int("00000000000000000000000001110000", 2)

    rm.enter_cmd("ADDI", "x1", "x0", int("00000000000000000000000001011100", 2))
    rm.enter_cmd("ADDI", "x2", "x0", 2)
    rm.enter_cmd("SLL", "x3", "x1", "x2")
    assert rm.inspect_register("x3") == int("00000000000000000000000101110000", 2)
