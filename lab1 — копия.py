#1(Рациональные)

from random import randint
from math import gcd

class My_Fraction:
    def __init__(self, num, den):
        if den != 0 and num != 0:
            k = gcd(num, den)
            self.num = num // k
            self.den = den // k
        else:
            raise ValueError

    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        return My_Fraction(randint(num_min, num_max), randint(den_min, den_max))

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num * other, self.den)
        return self

    def __truediv__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.den, self.den * other.num)
        if isinstance(other, int):
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

#1(Иррациональные)
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

#1(Дроби, образующие числа Фибоначи)
from math import gcd
from random import randint

class My_Fraction:
    def __init__(self, num, den):
        if den != 0 and num != 0:
            k = gcd(num, den)
            self.num = num // k
            self.den = den // k
        else:
            raise ValueError

    @staticmethod
    def generate(index_min, index_max):
        n = randint(index_min, index_max)
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b

        return My_Fraction(a, b)

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

a = [My_Fraction.generate(2, 10) for _ in range(5)]

for f in a:
    b = My_Fraction.generate(2, 10)
    cm = f * b
    print(f'{f} * {b} = {cm}')
    cd = f / b
    print(f'{f} / {b} = {cd}')
    n = randint(1, 9)
    cm = f * n
    print(f'{f} * {n} = {cm}')
    cd = f / n
    print(f'{f} / {n} = {cd}')

#2(Студенты)
class Student:
    def __init__(self, full_name="", group_number=0, progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        txt = 'Студент: ' + self.full_name + ' Группа: ' + str(self.group_number)
        txt += ' Оценки:'
        for x in self.progress:
            txt += ' ' + str(x)
        return txt

def SortParam(st):
    return st.full_name

st_size = 5
students = []
for i in range(st_size):
    print("Введите полное имя студента:")
    full_name = input()
    print("Введите номер группы:")
    group_number = input()
    n = 5
    print('Введите', n, 'оценок в столбик:')
    progress = []
    for j in range(n):
        score = int(input())
        progress.append(score)
    st = Student(full_name, group_number, progress)
    students.append(st)

print("Students list:")
for st in students:
    print(st)

students = sorted(students, key=SortParam)

print("Sorted students:")
for st in students:
    print(st)

print("bad students:")
n = 0
for st in students:
    for val in st.progress:
        if val < 3:
            print(st)
            n += 1
            break
if n == 0:
    print("no matches were found.")

#2(Школьники)
class School:
    def __init__(self, full_name="", class_number=0, progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.class_number = class_number
        self.progress = progress

    def __str__(self):
        txt = "Школьник: " + self.full_name + " Класс: " + str(self.class_number)
        txt += " Оценки:"
        for grade in self.progress:
            txt += " " + str(grade)
        return txt

def schoolq():
    school = []
    count = int(input("Введите количество школьников: "))
    for i in range(count):
        print(f"\nШкольник {i+1}:")
        full_name = input("Введите полное имя: ")
        class_number = input("Введите номер класса: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        school.append(School(full_name, class_number, progress))
    return school

schoolkids = schoolq()

print("\nСписок школьников:")
for s in schoolkids:
    print(s)

#2(Бакалавр)
class Bachelor:
    def __init__(self, full_name="", group_number="", progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        txt = "Бакалавр: " + self.full_name + " | Группа: " + str(self.group_number)
        txt += " | Оценки:"
        for grade in self.progress:
            txt += " " + str(grade)
        return txt

def bachelorq():
    bachelors = []
    count = int(input("Введите количество бакалавров: "))
    for i in range(count):
        print(f"\nБакалавр {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        bachelors.append(Bachelor(full_name, group_number, progress))
    return bachelors

bachelors = bachelorq()

print("\nСписок бакалавров:")
for s in bachelors:
    print(s)

#2(Магистр)
class Master:
    def __init__(self, full_name="", group_number="", progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        txt = "Магистрант: " + self.full_name + " | Группа: " + str(self.group_number)
        txt += " | Оценки:"
        for grade in self.progress:
            txt += " " + str(grade)
        return txt

def mastersq():
    masters = []
    count = int(input("Введите количество магистрантов: "))
    for i in range(count):
        print(f"\nМагистрант {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        masters.append(Master(full_name, group_number, progress))
    return masters

masters = mastersq()

print("\nСписок магистрантов:")
for s in masters:
    print(s)

#2(Аспирант)
class Aspirant:
    def __init__(self, full_name="", group_number="", progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        txt = "Аспирант: " + self.full_name + " | Группа: " + str(self.group_number)
        txt += " | Оценки:"
        for grade in self.progress:
            txt += " " + str(grade)
        return txt

def aspirantq():
    aspirants = []
    count = int(input("Введите количество аспирантов: "))
    for i in range(count):
        print(f"\nАспирант {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы/кафедры: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        aspirants.append(Aspirant(full_name, group_number, progress))
    return aspirants

aspirants = aspirantq()

print("\nСписок аспирантов:")
for s in aspirants:
    print(s)

#2(Учителя)
class Teacher:
    def __init__(self, full_name="", subject=""):
        self.full_name = full_name
        self.subject = subject

    def __str__(self):
        return "Преподаватель: " + self.full_name + " | Предмет: " + self.subject

def teachersq():
    teachers = []
    count = int(input("Введите количество преподавателей: "))
    for i in range(count):
        print(f"\nПреподаватель {i+1}:")
        full_name = input("Введите полное имя: ")
        subject = input("Введите предмет: ")
        teachers.append(Teacher(full_name, subject))
    return teachers

teachers = teachersq()

print("\nСписок преподавателей:")
for t in teachers:
    print(t)