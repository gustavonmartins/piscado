"""
Tests I type instructions
"""
from riscv.risc_machine import RiscMachine
from riscv.compiler import RiscCompiler


def test_addi():
    """
    Tests ADDI instruction
    """

    rc = RiscCompiler()

    rc.enter_input("ADDI", "x1", "x0", 5)

    program_memory = rc.createoutput()
    rm = RiscMachine(program=program_memory)

    rm.run_one_cycle()
    assert rm.inspect_register("x1") == 5


def test_many_addi():
    """
    Tests batch of ADDI instructions
    """
    rc = RiscCompiler()

    rc.enter_input("ADDI", "x0", "x0", 6)
    rc.enter_input("ADDI", "x1", "x0", 1)
    rc.enter_input("ADDI", "x2", "x1", 2)
    rc.enter_input("ADDI", "x3", "x1", 30)

    program = rc.createoutput()
    rm = RiscMachine(program=program)
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x0") == 0
    assert rm.inspect_register("x1") == 1
    assert rm.inspect_register("x2") == 3
    assert rm.inspect_register("x3") == 31
