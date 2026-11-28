from src.product import Product

class Smartphone(Product):
    """ Класс продуктов 'Смартфоны' """
    name: str
    description: str
    price: float
    quantity: int
    efficiency: str # производитель
    model: str # модель
    memory: float # объем встроенной памяти
    color: str # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color