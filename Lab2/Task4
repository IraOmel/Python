class BinaryTree:
    """"A class Binary tree that contains background information of product prices."""

    def __init__(self, code, price):
        if not isinstance(price, int) or not isinstance(code, int):
            raise TypeError("incorrect type")
        if price < 0 or code < 0 or not code or not price:
            raise ValueError("incorrect value")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """"A function that insert elements to a binary tree."""
        if self.code:
            if code == self.code:
                raise ValueError("the code cannot be repeated")
            if code < self.code:
                if not self.left:
                    self.left = BinaryTree(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if not self.right:
                    self.right = BinaryTree(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code

    def find_price(self, code):
        """"A function that return price of product by its code."""
        if code < self.code:
            if not self.left:
                raise ValueError("not found")
            return self.left.find_price(code)
        elif code > self.code:
            if not self.right:
                raise ValueError("not found")
            return self.right.find_price(code)
        else:
            return self.price

    def cost(self, code, quantity):
        """"A function that return total cost of products."""
        price_of_product = self.find_price(code)
        res = price_of_product * quantity
        return res


obj1 = BinaryTree(1, 23)
obj1.insert(2, 10)
obj1.insert(3, 11)
obj1.insert(4, 44)
obj1.insert(5, 65)
obj1.insert(6, 77)
product_code = int(input("Enter code of product:"))
amount = int(input("Enter quantity:"))
if product_code < 0 or amount < 0 or not product_code or not amount:
    raise ValueError("incorrect value")
print("Total value:" + str(obj1.cost(product_code, amount)))
