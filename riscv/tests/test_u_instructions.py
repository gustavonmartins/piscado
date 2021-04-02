"""
Tests instructions of U type
"""
from riscv.risc_machine import RiscMachine
from riscv.compiler import RiscCompiler


def test_lui():
    """
    Tests LUI instructions
    """
    rm = RiscMachine()
    rc = RiscCompiler()

    rc.enter_input("LUI", "x1", int("FFEECCDD", 16))

    program_memory = rc.createoutput()
    rm.program_memory = program_memory

    rm.run_one_cycle()
    assert rm.inspect_register("x1") == int("FFEEC000", 16)
