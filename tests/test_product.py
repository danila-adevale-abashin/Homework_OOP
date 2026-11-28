from src.product import Product
import pytest


def test_product_init(first_product):
    assert first_product.name == "Oppo"
    assert first_product.description == "Быстрый флагман"
    assert first_product.price == 34999
    assert first_product.quantity == 4


def test_price_getter(first_product):
    assert first_product.price == 34999


def test_price_setter_positive(first_product):
    first_product.price = 40000
    assert first_product.price == 40000


def test_price_setter_negative(first_product, capsys):
    first_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == 34999  # цена не изменилась


def test_new_product():
    data = {
        "name": "Xiaomi",
        "description": "Бюджетный",
        "price": 20000,
        "quantity": 5,
    }
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Xiaomi"
    assert p.price == 20000
    assert p.quantity == 5


def test_product_str(first_product):
    assert str(first_product) == "Oppo, 34999 руб. Остаток: 4 шт."


def test_product_add(first_product, second_product):
    # 34999 * 4 + 44999 * 2 = 139996 + 89998 = 229994
    assert first_product + second_product == 229994


def test_product_add_with_non_product(first_product):
    with pytest.raises(TypeError):
        first_product + 123


def test_product_add_same_type():
    p1 = Product("A", "B", 100, 2)
    p2 = Product("C", "D", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3  # 800


def test_product_add_different_types():
    from src.smartphone import Smartphone
    from src.lawn_grass import LawnGrass
    p1 = Product("A", "B", 100, 2)
    s1 = Smartphone("S", "D", 100, 2, "high", "X", 128, "black")
    l1 = LawnGrass("L", "D", 100, 2, "Russia", "10 days", "green")

    with pytest.raises(TypeError):
        p1 + s1
    with pytest.raises(TypeError):
        s1 + l1
