from math import sqrt, isqrt
from random import randint

class My_Fraction:
    def __init__(self, num, den):
        if den != 0 and num != 0:
            self.num = num
            self.den = den
        else:
            raise ValueError

    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        while True:
            n = randint(num_min, num_max)
            if isqrt(n) ** 2 != n:
                irr_num = sqrt(n)
                break
        while True:
            n = randint(den_min, den_max)
            if isqrt(n) ** 2 != n:
                irr_den = sqrt(n)
                break
        return My_Fraction(irr_num, irr_den)

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, (int, float)):
            return My_Fraction(self.num * other, self.den)
        return self

    def __truediv__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.den, self.den * other.num)
        if isinstance(other, (int, float)):
            return My_Fraction(self.num, self.den * other)
        raise TypeError

a = [My_Fraction.generate(1, 9, 1, 9) for i in range(5)]
for f in a:
    b = My_Fraction.generate(1, 9, 1, 9)
    cm = f * b
    print(f'{f} * {b} = {cm}')
    cd = f / b
    print(f'{f} / {b} = {cd}')
    n=randint(1, 9)
    cm = f * n
    print(f'{f} * {n} = {cm}')
    cd = f / n
    print(f'{f} / {n} = {cd}')
