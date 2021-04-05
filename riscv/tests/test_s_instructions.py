"""
This tests the implementation of S-type instructions
"""

from riscv.compiler import RiscCompiler
from riscv.risc_machine import RiscMachine


def test_store_and_load_word():
    """
    Tests if memory receives data
    """

    rc = RiscCompiler()

    # Register x11 receives value
    rc.enter_input("ADDI", "x11", "x0", 27)
    rc.enter_input("ADDI", "x12", "x0", 1024)

    # Stores in memory
    rc.enter_input("SW", "x11", 4, "x12")

    # Load from memory
    rc.enter_input("LW", "x9", 4, "x12")

    program_memory = rc.createoutput()

    assert len(program_memory) == 4
    rm = RiscMachine(program=program_memory)
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x9") == 27


def test_store_and_load_word_again():
    """
    Tests if memory receives data
    """

    rc = RiscCompiler()

    # Register x11 receives value
    rc.enter_input("ADDI", "x11", "x0", 30)
    rc.enter_input("ADDI", "x12", "x0", 512)

    # Stores in memory
    rc.enter_input("SW", "x11", 32, "x12")

    # Load from memory
    rc.enter_input("LW", "x5", 32, "x12")

    program_memory = rc.createoutput()

    assert len(program_memory) == 4
    rm = RiscMachine(program=program_memory)
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    assert rm.inspect_register("x5") == 30
