from risc_machine import RiscMachine
from compiler import RiscCompiler


def test_add():
    rm = RiscMachine()
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x1", "x0", 50)
    rc.enter_input("ADDI", "x2", "x0", 60)
    rc.enter_input("ADD", "x3", "x1", "x2")

    program_memory = rc.createoutput()
    rm.program_memory = program_memory

    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    assert rm.inspect_register("x3") == 110


def test_sll():
    rm = RiscMachine()
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x1", "x0", int("00000000000000000000000000001100", 2))
    rc.enter_input("ADDI", "x2", "x0", 2)
    rc.enter_input("SLL", "x3", "x1", "x2")

    program_memory = rc.createoutput()
    rm.program_memory = program_memory

    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    assert rm.inspect_register("x3") == int("00000000000000000000000000110000", 2)

    rc.enter_input("ADDI", "x1", "x0", int("00000000000000000000000000011100", 2))
    rc.enter_input("ADDI", "x2", "x0", 2)
    rc.enter_input("SLL", "x3", "x1", "x2")
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    assert rm.inspect_register("x3") == int("00000000000000000000000001110000", 2)

    rc.enter_input("ADDI", "x1", "x0", int("00000000000000000000000001011100", 2))
    rc.enter_input("ADDI", "x2", "x0", 2)
    rc.enter_input("SLL", "x3", "x1", "x2")
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    assert rm.inspect_register("x3") == int("00000000000000000000000101110000", 2)
