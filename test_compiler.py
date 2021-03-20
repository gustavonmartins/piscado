from compiler import RiscCompiler


def test_amount_of_statements():
    """
    Ensures that amount of statemens produced is as expected
    """
    rc = RiscCompiler()
    rc.enter_input("ADDI", "x1", "x2", 6)
    rc.enter_input("SLL", "x3", "x2", "x1")

    program_memory = rc.createoutput()
    assert len(program_memory) == 2


def test_amount_of_statements_with_x0():
    """
    Ensures that amount of statemens produced is as expected
    """
    rc = RiscCompiler()
    rc.enter_input("ADDI", "x0", "x2", 6)
    rc.enter_input("ADD", "x0", "x2", "x2")
    rc.enter_input("ADDI", "x1", "x2", 6)
    rc.enter_input("SLL", "x3", "x2", "x1")

    program_memory = rc.createoutput()
    assert len(program_memory) == 4
