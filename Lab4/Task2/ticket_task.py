import time
import uuid
import json
from datetime import datetime, date
from constants import ADVANCE_DISCOUNT, LATE_DISCOUNT, STUDENT_DISCOUNT, DAYS_ADVANCE, DAYS_LATE


class Buyer:
    """A class that describes a buyer."""

    def __init__(self, surname, name, occupation=""):
        self.surname = surname
        self.name = name
        self.occupation = occupation

    @property
    def surname(self):
        return self._surname

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        if not isinstance(occupation, str):
            raise TypeError("Incorrect type")
        if not all(letter.isalpha() for letter in occupation):
            raise ValueError("Invalid value")
        if not occupation:
            self._occupation = ""
        self._occupation = occupation

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
        return f'Buyer: {self.surname} {self.name} {self.occupation}'


class Ticket:
    """A class that describes a regular ticket"""

    def __init__(self, buyer, event):
        if not isinstance(buyer, Buyer):
            raise TypeError("Incorrect type")
        self.buyer = buyer
        self.id = uuid.uuid1()
        self.price = data[event]['cost']

    def price_of_ticket(self):
        return self.price

    def type_of_ticket(self):
        return f'Regular'

    def __str__(self):
        return f'\n{self.type_of_ticket()} ticket ID:{self.id}\nPrice: {self.price_of_ticket()}\n' \
               f'{self.buyer.name} {self.buyer.surname} {self.buyer.occupation}'


class Advance(Ticket):
    def price_of_ticket(self):
        return self.price - self.price * ADVANCE_DISCOUNT

    def type_of_ticket(self):
        return Advance.__name__


class Student(Ticket):
    def price_of_ticket(self):
        return self.price * STUDENT_DISCOUNT

    def type_of_ticket(self):
        return Student.__name__


class Late(Ticket):
    def price_of_ticket(self):
        return self.price + self.price * LATE_DISCOUNT

    def type_of_ticket(self):
        return Late.__name__


class Order:
    """Class that construct the order"""

    def __init__(self, buyer, event, date_order):
        if not isinstance(buyer, Buyer):
            raise TypeError("Incorrect type")
        self.buyer = buyer
        self.event = event
        self.ticket = Ticket(self.buyer, self.event)
        self.date_order = date_order

        @property
        def event(self):
            return self._event

        @property
        def date_order(self):
            return self._date_order

        @event.setter
        def event(self, event):
            if not isinstance(event, str):
                raise TypeError("Incorrect type")
            if event not in data.keys():
                raise ValueError("no such event")
            self._event = event

        @date_order.setter
        def date_order(self, date_order):
            try:
                self._date_order = date_order
                if isinstance(date_order, str):
                    self._date_order = datetime.strptime(date_order, "%Y.%m.%d")
            except ValueError as err:
                raise

    def date_count(self):
        data[self.event]['tickets'] -= 1
        if data[self.event]['tickets'] <= 0:
            raise ValueError("no tickets")
        data1 = datetime.strptime(self.date_order, "%d.%m.%Y")
        data2 = datetime.strptime(data[self.event]['date'], "%d.%m.%Y")
        if data1 > data2:
            raise ValueError("incorrect date")
        days = abs((data2 - data1).days)
        return days

    def type_of_ticket(self):
        num_days = self.date_count()
        if num_days >= DAYS_ADVANCE and not self.buyer.occupation:
            ob = Advance(self.buyer, self.event)
        elif num_days <= DAYS_LATE and not self.buyer.occupation:
            ob = Late(self.buyer, self.event)
        elif self.buyer.occupation == "student":
            ob = Student(self.buyer, self.event)
        else:
            ob = self.ticket
        return ob

    def find_ticket(self, id_ticket):
        if not isinstance(id_ticket, str):
            raise TypeError("incorrect date")
        with open("info_about_orders.json", 'r') as file:
            orders = json.load(file)
            list_t = []
            for item in orders:
                list_t.append(orders[item]['id'])
                if id_ticket in list_t:
                    return f'\nFind ticket:{orders[item]}'


with open('event.json', 'r') as file:
    data = json.load(file)

buyer1 = Buyer("Nic", "Rio")
order1 = Order(buyer1, "IT-event1", "08.02.2021")
my_ticket = order1.type_of_ticket()
print(my_ticket)

buyer2 = Buyer("Olya", "Ale")
order2 = Order(buyer2, "IT-event2", "12.11.2019")
my_ticket2 = order2.type_of_ticket()
print(my_ticket2)

buyer3 = Buyer("Oksana", "Dov", "student")
order3 = Order(buyer3, "IT-event2", "12.11.2021")
my_ticket3 = order3.type_of_ticket()
print(my_ticket3)

print(order1.find_ticket("45d62982-47ad-11ec-9f47-80c5f2143d4a"))

tickets = {my_ticket.type_of_ticket(): my_ticket.__dict__, my_ticket2.type_of_ticket(): my_ticket2.__dict__,
           my_ticket3.type_of_ticket(): my_ticket3.__dict__}
with open('info_about_orders.json', 'a+') as f:
    json.dump(tickets, f, indent=4, default=str)
