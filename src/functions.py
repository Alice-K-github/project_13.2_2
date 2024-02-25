
class Category:
    """Класс категорий: наименование, описание, товар (+подсчёт всего категорий и продуктов)"""
    name: str
    description: str
    product: list
    all_category = 0
    unique_products_count = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product

        Category.all_category += 1

        Category.unique_products_count += Category.unique_products(self.product)

    @classmethod
    def unique_products(cls, product: list) -> int:
        set_names = []
        for product_ in product:
            if str(product_.title) not in set_names:
                set_names.append(product_.title)
        return len(set_names)


class Product:
    """Класс товаров: наименование, описание, цена, количество"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

