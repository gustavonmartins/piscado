from risc_machine import RiscMachine


def test_jump():
    """"""
    rm = RiscMachine()

    rm.enter_cmd("ADDI", "x1", "x0", 1)
    rm.enter_cmd("ADDI", "x3", "x0", 3)
    rm.enter_cmd("J", 2)

    rm.enter_cmd("ADDI", "x3", "x0", 30)

    # This command will be ignored
    rm.enter_cmd("ADDI", "x2", "x0", 2)

    rm.run_one_cycle()
    rm.run_one_cycle()
    rm.run_one_cycle()

    rm.run()
    assert rm.inspect_register("x3") == 3
    assert rm.inspect_register("x3") != 30
