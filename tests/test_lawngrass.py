from src.lawn_grass import LawnGrass


def test_lawn_grass_init():
    l = LawnGrass("Газон", "Трава", 500, 100, "Russia", "10 days", "green")
    assert l.name == "Газон"
    assert l.country == "Russia"
    assert l.germination_period == "10 days"
    assert l.color == "green"
