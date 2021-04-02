"""
Tests some basic registers properties
"""
from riscv.risc_machine import RiscMachine
from riscv.compiler import RiscCompiler


def test_x0_is_immutable():
    """
    Tests immutability of x0 register
    """
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x0", "x0", 100)

    program_memory = rc.createoutput()
    rm = RiscMachine(program=program_memory)

    assert rm.inspect_register("x0") == 0

    rm.run_one_cycle()

    assert rm.inspect_register("x0") == 0
