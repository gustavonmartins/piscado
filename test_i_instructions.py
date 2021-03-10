from risc_machine import RiscMachine


def test_addi():
    rm = RiscMachine()

    assert rm.inspect_register("x0") == 0

    rm.enter_cmd("ADDI", "x1", "x0", 5)
    rm.run_one_cycle()
    assert rm.inspect_register("x1") == 5

    rm.enter_cmd("ADDI", "x2", "x1", 6)
    rm.run_one_cycle()
    assert rm.inspect_register("x2") == 11

    rm.enter_cmd("ADDI", "x0", "x1", 6)
    assert rm.inspect_register("x0") == 0
