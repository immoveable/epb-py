from epb import Regulator, energy_class, total_consumption


def test_energy_class():
    assert energy_class(Regulator.BRUSSELS, 100) == "C+"


def test_total_consumption():
    assert total_consumption(100, 250) == 25_000
