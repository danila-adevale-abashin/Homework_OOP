from src.product import Product


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
