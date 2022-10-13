import math
from fractions import Fraction


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def operation(self):
        return Fraction(self.__numerator, self.__denominator)

    def calculation(self):
        return self.__numerator / self.__denominator


    @property
    def numerator(self):
     return self.__numerator

    @property
    def denominator(self):
     return self.__denominator

    @numerator.setter
    def numerator(self, numerator):
     if not isinstance(numerator, int):
        raise TypeError("Incorrect data")
     self.__numerator = numerator

    @denominator.setter
    def denominator(self, denominator):
     if not isinstance(denominator, int):
        raise TypeError("Incorrect data")
     if not denominator:
        raise ZeroDivisionError("Incorrect data")
     self.__denominator = denominator


obj1 = Rational(2, 4)
print(obj1.operation())
print(obj1.calculation())
