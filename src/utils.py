import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf8") as file:
        data = json.load(file)
    return data


def create_category_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    json_data = read_json("data/products.json")
    category_data = create_category_from_json(json_data)
    print(category_data)
    print(category_data[0].name)
    print(category_data[0].products)
    print(category_data[0].products[0].name)
