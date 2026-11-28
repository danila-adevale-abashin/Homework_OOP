from src.smartphone import Smartphone


def test_smartphone_init():
    s = Smartphone("iPhone", "Смартфон", 100000, 5, "high", "15 Pro", 256, "black")
    assert s.name == "iPhone"
    assert s.efficiency == "high"
    assert s.model == "15 Pro"
    assert s.memory == 256
    assert s.color == "black"
