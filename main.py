from math import gcd

class My_Fraction:
    def __init__(self, num, den):
        if den != 0 and num != 0:
            k = gcd(num, den)
            self.num = num // k
            self.den = den // k
        else:
            raise ValueError("Числитель и знаменатель должны быть не нулевыми.")

    @staticmethod
    def generate(cls):
        a = int(input("Введите первое число Фибоначчи: "))
        b = int(input("Введите второе число Фибоначчи: "))
        count = int(input("Введите количество чисел в ряду (не менее 2): "))
        if count < 2:
            print("Количество чисел должно быть не менее 2.")
            return []
        fib = [a, b]
        for i in range(2, count):
            fib.append(fib[i-1] + fib[i-2])
        fractions = []
        for i in range(count - 1):
            fractions.append(cls(fib[i], fib[i+1]))
        return fractions

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num * other, self.den)
        raise TypeError

    def __truediv__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.den, self.den * other.num)
        if isinstance(other, int):
            return My_Fraction(self.num, self.den * other)
        raise TypeError

fractions = My_Fraction.generate()
print("\nРяд Фибоначчи:")
for frac in fractions:
    print(frac)
