from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description.startswith("Смартфоны, как средство")
    assert first_category.product_count == 3
    assert first_category.category_count >= 2


def test_add_product(first_category):
    initial_count = first_category.product_count
    p = Product("Новый", "Описание", 1000, 1)
    first_category.add_product(p)
    assert first_category.product_count == initial_count + 1


def test_products_getter(first_category):
    result = first_category.products
    assert isinstance(result, str)
    assert "Oppo, 34999 руб. Остаток: 4 шт.\n" in result
    assert "Oppo, 24999 руб. Остаток: 5 шт.\n" in result


def test_products_getter_empty():
    empty_cat = Category("Пустая", "Описание")
    assert empty_cat.products == ""
