class Product:
    """A class that describes a product."""

    def __init__(self, price, description):
        self.price = price
        self.description = description

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("incorrect type")
        if price < 0 or not price:
            raise ValueError("incorrect value")
        self._price = price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("incorrect type")
        if not description or not all(letter.isalpha() for letter in description):
            raise ValueError("incorrect value")
        self._description = description

    def __str__(self):
        return f'Product: {self.price}, {self.description}'


class Customer:
    """A class that describes a customer."""

    def __init__(self, surname, name, phone):
            self.surname = surname
            self.name = name
            self.phone = phone

    @property
    def surname(self):
        return self._surname

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in surname):
            raise ValueError("Invalid name, surname")
        if not surname:
            raise ValueError("string is empty")
        self._surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in name):
            raise ValueError("Invalid name, surname")
        if not name:
            raise ValueError("string is empty")
        self._name = name

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, int):
            raise TypeError("Incorrect type")
        if not phone:
            raise ValueError("string is empty")
        self._phone = phone

    def __str__(self):
        return f'Customer:{self.surname} {self.name}, {self.phone}'


class Order():
    """A class that contain date about customer and product."""

    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Incorrect type")
        self.customer = customer
        self.products = []

    def add_product(self, product):
        """"Method that add the product at empty list 'products'."""
        self.products.append(product)

    def del_product(self, product):
        """"Method that delete the product from list 'products'."""
        if not isinstance(product, Product):
            raise TypeError
        self.products.remove(product)

    def total_value(self):
        """"Method that count and return the total value of product in order."""
        summa = 0
        for item in self.products:
            summa += item.price
        return summa

    def __str__(self):
        return f'Order: {self.customer}, {self.products}'


customer_1 = Customer("Omel", "Ira", 3809702)
order_1 = Order(customer_1)
product_1 = Product(12, "Pen")
product_2 = Product(145, "Book")
product_3 = Product(1, "Fork")
order_1.add_product(product_1)
order_1.add_product(product_2)
order_1.add_product(product_3)
order_1.del_product(product_2)
print(customer_1)
print("Total value 1 order: " + str(order_1.total_value()))
customer_2 = Customer("Dovga", "Oksana", 38097)
order_2 = Order(customer_2)
product2_1 = Product(55, "Note")
product2_2 = Product(5, "Pencil")
order_2.add_product(product2_1)
order_2.add_product(product2_2)
print(customer_2)
print("Total value 2 order: " + str(order_2.total_value()))
