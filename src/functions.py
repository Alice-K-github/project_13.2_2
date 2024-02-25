class Category:
    """Класс категорий: наименование, описание, товар (+подсчёт всего категорий и продуктов)"""
    name: str
    description: str
    products: list
    all_category = 0
    unique_products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.all_category += 1

        Category.unique_products_count += Category.unique_products(self.__products)

    @classmethod
    def unique_products(cls, __products: list) -> int:
        set_names = []
        for product_ in __products:
            if str(product_.title) not in set_names:
                set_names.append(product_.title)
        return len(set_names)

    """достаёт параметры товара из класса продукт"""

    @property
    def product_list(self, product_):
        # self.__product.append(new_product)
        product_items = []
        for item in product_:
            product_items = Product(item.name, item.description, item.price, item.quantity)
        return product_items

    """добавляет продукт"""

    @property
    def add_product(self, product_list):
        self.__products.append(product_list)

    """выводит Продукт, 80 руб. Остаток: 15 шт."""

    @property
    def product_stat(self):
        for item in self.__products:
            return f"{item.name}, {item.price}. Остаток: {item.quantity} шт."


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

    """Ввод нового продукта"""

    @property
    def get_items(self):
        items = []
        product_name = input("Введите наименование: ")
        product_description = input("Введите описание: ")
        product_price = input("Укажите цену: ")
        product_quantity = input("Укажите количество: ")
        items.append(product_name + product_description + product_price + product_quantity)
        return items

    """Добавление новго продукта"""

    @property
    def new_product(self):
        self.name, self.description, self.price, self.quantity = self.get_items
        new_product_items = [self.name + self.description + str(self.price) + str(self.quantity)]
        return new_product_items

    """чё..."""
    @new_product.setter
    def new_product(self, price: new_product[2]):
        if int(self.new_product[price]) <= 0:
            print("Цена введена некорректно")
            return False
        else:
            return True

