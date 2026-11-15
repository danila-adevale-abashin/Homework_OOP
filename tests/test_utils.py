import json

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_category_from_json, read_json


# Тестирование № 1
def test_read_json_success(tmp_path):
    """Тест: успешное чтение валидного JSON-файла."""
    test_file = tmp_path / "test_data.json"

    expected_data = {
        "categories": [
            {"name": "Смартфоны", "description": "Описание"},
            {"name": "Ноутбуки", "description": "Описание"},
        ]
    }

    with open(test_file, "w", encoding="utf8") as f:
        json.dump(expected_data, f, ensure_ascii=False)

    result = read_json(str(test_file))

    assert result == expected_data
    assert isinstance(result, dict)


def test_read_json_file_not_found():
    """Тест: ошибка, если файл не существует."""
    with pytest.raises(FileNotFoundError):
        read_json("non_existent_file.json")


# Тестирование № 2


def test_create_category_from_json():
    """Тест: создание объектов из словаря."""
    json_data = [
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {"name": "Телефон", "description": "Умный", "price": 50000.0, "quantity": 10},
                {"name": "Ноутбук", "description": "Мощный", "price": 80000.0, "quantity": 5},
            ],
        }
    ]

    categories = create_category_from_json(json_data)

    assert isinstance(categories, list)
    assert len(categories) == 1

    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Электроника"
    assert len(category.products) == 2

    product = category.products[0]
    assert isinstance(product, Product)
    assert product.name == "Телефон"
    assert product.price == 50000.0
