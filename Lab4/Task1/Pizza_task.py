import json
from datetime import date, datetime
import calendar


class Pizza:
    """A class that describes a pizza."""

    def __init__(self):
        self.list_of_ingredients = {}

    def add_ingredients(self, component):
        """"Method that add the ingredients at empty dict 'list_of_ingredients'."""
        for item in component:
            if item not in ingredients.keys():
                raise ValueError("cannot add such product")
            if not isinstance(item, str):
                raise TypeError("incorrect data")
            self.list_of_ingredients.update({item: ingredients[item]})
        self.price = sum(list(self.list_of_ingredients.values())) + self.price

    def __repr__(self):
        return f'\nPizza of {self.type_pizza()} - {self.name_of_pizza} {self.first_price()} -> ' \
               f' Price with add: {self.price}' \
               f'\nIngredients: {self.description}, Additional ingredients: {self.list_of_ingredients}'


class Monday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Monday.__name__]['pizza']
        self.price = info[Monday.__name__]['cost']
        self.description = info[Monday.__name__]['ingredients']

    def type_pizza(self):
        return Monday.__name__

    def first_price(self):
        return info[Monday.__name__]['cost']


class Tuesday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Tuesday.__name__]['pizza']
        self.price = info[Tuesday.__name__]['cost']
        self.description = info[Tuesday.__name__]['ingredients']

    def type_pizza(self):
        return Tuesday.__name__

    def first_price(self):
        return info[Tuesday.__name__]['cost']


class Wednesday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Wednesday.__name__]['pizza']
        self.price = info[Wednesday.__name__]['cost']
        self.description = info[Wednesday.__name__]['ingredients']

    def type_pizza(self):
        return Wednesday.__name__

    def first_price(self):
        return info[Wednesday.__name__]['cost']


class Thursday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Thursday.__name__]['pizza']
        self.price = info[Thursday.__name__]['cost']
        self.description = info[Thursday.__name__]['ingredients']

    def type_pizza(self):
        return Thursday.__name__

    def first_price(self):
        return info[Thursday.__name__]['cost']


class Friday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Friday.__name__]['pizza']
        self.price = info[Friday.__name__]['cost']
        self.description = info[Friday.__name__]['ingredients']

    def type_pizza(self):
        return Friday.__name__

    def first_price(self):
        return info[Friday.__name__]['cost']


class Saturday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Saturday.__name__]['pizza']
        self.price = info[Saturday.__name__]['cost']
        self.description = info[Saturday.__name__]['ingredients']

    def type_pizza(self):
        return Saturday.__name__

    def first_price(self):
        return info[Saturday.__name__]['cost']


class Sunday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Sunday.__name__]['pizza']
        self.price = info[Sunday.__name__]['cost']
        self.description = info[Sunday.__name__]['ingredients']

    def type_pizza(self):
        return Sunday.__name__

    def first_price(self):
        return info[Sunday.__name__]['cost']


class Customer:
    """A class that describes a customer."""

    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @property
    def surname(self):
        return self._surname

    @property
    def name(self):
        return self._name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in surname):
            raise ValueError("Invalid surname")
        if not surname:
            raise ValueError("String is empty")
        self._surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in name):
            raise ValueError("Invalid name")
        if not name:
            raise ValueError("String is empty")
        self._name = name

    def __str__(self):
        return f'Customer: {self.surname} {self.name}'


class Order:
    """Class that construct the order and count the total value"""
    def __init__(self, customer, day):
        if not isinstance(customer, Customer):
            raise TypeError("Incorrect type")
        self.customer = customer
        self.day = day
        self.pizza = Pizza()
        self.pizza_list = []

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        try:
            self._day = day
            if isinstance(day, str):
                self._day = datetime.strptime(day, "%Y.%m.%d")
        except ValueError as err:
            raise

    def type_of_pizza(self):
        """Method that return pizza-of-day"""
        dict_pizza = {"Monday":Monday(), "Tuesday": Tuesday(), "Wednesday": Wednesday(),"Thursday":Thursday(),
                      "Friday": Friday(), "Saturday":Saturday(), "Sunday": Sunday()}
        return dict_pizza[calendar.day_name[self.day.weekday()]]

    def add_pizza(self, add_pizza):
        """"Method that add the pizza at order."""
        if not isinstance(add_pizza, list):
            raise TypeError("Incorrect type")
        for item in add_pizza:
            if not isinstance(item, Pizza):
                raise TypeError("Incorrect type")
        for i in add_pizza:
            self.pizza_list.append(i)

    def total_value(self):
        """"Method that count and return the total value of order."""
        summa = 0
        for item in self.pizza_list:
            summa += item.price
        return summa

    def __str__(self):
        return f'\n {self.customer}, {self.pizza_list}'


with open('pizza_of_day.json', 'r') as file:
    info = json.load(file)
with open('ingredients.json', 'r') as file:
    ingredients = json.load(file)

customer1 = Customer("Ira", "Omel")
order1 = Order(customer1, "2021.11.12")
pizza1 = order1.type_of_pizza()
pizza1.add_ingredients(["tomato", "ham"])
pizza2 = order1.type_of_pizza()
pizza2.add_ingredients(["pineapples"])
order1.add_pizza([pizza1, pizza2])
print(order1)
print("\nTotal value order: " + str(order1.total_value()))

customer2 = Customer("Ira", "Mal")
order2 = Order(customer2, "2021.11.14")
pizza3 = order2.type_of_pizza()
pizza3.add_ingredients(["corn", "pineapples"])
pizza2 = order2.type_of_pizza()
order2.add_pizza([pizza3])
print(order2)
print("\nTotal value order: " + str(order2.total_value()))

with open('pizza_order.json', 'w') as file:
    json.dump(pizza3.__dict__, file, indent=2)

add_ingredients = {
    "cheese": 25,
    "mushrooms": 10,
    "ham": 30,
    "squid": 50,
    "shrimp": 50,
    "tomato": 5,
    "pepper": 5,
    "olive": 5,
    "salami": 25,
    "pineapples": 10,
    "corn": 10,
    "chicken": 30
}
with open('ingredients.json', 'w') as file:
    json.dump(add_ingredients, file, indent=2)
