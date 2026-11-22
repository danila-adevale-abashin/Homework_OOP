import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(name="Oppo", description="Быстрый флагман", price=34999, quantity=4)


@pytest.fixture
def second_product():
    return Product(name="Wivo", description="Капец какой быстрый флагман", price=44999, quantity=2)


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
        "удобства жизни",
        products=[Product("Oppo", "Быстрый флагман", 34999, 4), Product("Oppo", "Старая версия", 24999, 5)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
        "удобства жизни, и не только",
        products=[Product(name="Wivo", description="Капец какой быстрый флагман", price=44999, quantity=2)],
    )
