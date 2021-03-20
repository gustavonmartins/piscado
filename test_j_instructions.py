from risc_machine import RiscMachine
from compiler import RiscCompiler


def test_jump():
    """"""
    rm = RiscMachine()
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x1", "x0", 1)
    rc.enter_input("ADDI", "x3", "x0", 3)
    rc.enter_input("J", 2)

    rc.enter_input("ADDI", "x3", "x0", 30)

    # This command will be ignored
    rc.enter_input("ADDI", "x2", "x0", 2)

    program_memory = rc.createoutput()
    rm.program_memory = program_memory

    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x3") == 3
    assert rm.inspect_register("x3") != 30
