from risc_machine import RiscMachine


def test_jump():
    """"""
    rm = RiscMachine()

    rm.enter_section(".X2Is3")
    rm.enter_cmd("ADDI", "x2", "x0", 3)

    rm.enter_section("main")
    rm.enter_cmd("ADDI", "x1", "x0", 1)
    rm.enter_cmd("J", ".X2Is3")

    # This command will be ignored
    rm.enter_cmd("ADDI", "x2", "x0", 2)

    rm.run()
    assert rm.inspect_register("x2") == 30
