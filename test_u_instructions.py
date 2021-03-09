from risc_machine import RiscMachine


def test_load_upper_immediate():
    rm = RiscMachine()
    rm.enter_cmd("LUI", "x1", int("FFEECCDD", 16))
    assert rm.inspect_register("x1") == int("FFEEC000", 16)