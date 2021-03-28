from risc_machine import RiscMachine
from compiler import RiscCompiler


def test_jal():
    rc = RiscCompiler()
    rc.enter_input("JAL", "x1", 2)
    rc.enter_input("ADD", "x5", "x0", "x10")
    rc.enter_input("ADDI", "x10", "x0", 1000)
    rc.enter_input("JAL", "x0", -2)

    rm = RiscMachine()
    rm.program_memory = rc.createoutput()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x5") == 1000
