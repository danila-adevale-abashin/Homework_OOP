import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def first_product():
    return Product(
        name='Oppo',
        description='Быстрый флагман',
        price=34.999,
        quantity=4
    )

@pytest.fixture
def second_product():
    return Product(
        name='Wivo',
        description='Капец какой быстрый флагман',
        price=44.999,
        quantity=2
    )

@pytest.fixture
def first_category():
    return Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                    'удобства жизни',
        products=[Product('Oppo', 'Быстрый флагман', 34.999, 4),
                  Product('Oppo', 'Старая версия', 24.999, 5)]
    )

@pytest.fixture
def second_category():
    return Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                    'удобства жизни, и не только',
        products=[Product(
            name='Wivo',
            description='Капец какой быстрый флагман',
            price=44.999,
            quantity=2
        )]
    )