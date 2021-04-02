"""
Tests some basic registers properties
"""
from riscv.risc_machine import RiscMachine
from riscv.compiler import RiscCompiler


def test_x0_is_immutable():
    """
    Tests immutability of x0 register
    """
    rm = RiscMachine()
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x0", "x0", 100)
    program = rc.createoutput()
    rm.program_memory = program
    rm.run_one_cycle()

    assert rm.inspect_register("x0") == 0
