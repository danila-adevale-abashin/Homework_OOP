class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """Сеттер для изменения цены товара"""
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        if new_price < self.__price:
            answer = input('Понизить цену? (y/n): ')
            if answer.lower() != 'y':
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list | None = None) -> 'Product':
        """Создает объект Product из словаря"""
        if existing_products:
            for p in existing_products:
                if p.name == product_dict["name"]:
                    p.quantity += product_dict["quantity"]
                    p.price = max(p.price, product_dict["price"])
                    return p
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )