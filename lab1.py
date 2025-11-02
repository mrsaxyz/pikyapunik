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

class My_Fraction:
    def __init__(self, num, den):
        if den != 0 and num != 0:
            k = gcd(num, den)
            self.num = num // k
            self.den = den // k
        else:
            raise ValueError

    @staticmethod
    def generate():
        def i_f(p):
            f = input(p)
            n, d = map(int, f.split('/'))
            return My_Fraction(n, d)

        f1 = i_f("Введите первую дробь: ")
        f2 = i_f("Введите вторую дробь: ")

        c = int(input("Введите количество чисел в ряду Фибоначчи: "))

        s = [f1, f2]
        for _ in range(c - 2):
            n = s[-1].num * s[-2].den + s[-2].num * s[-1].den
            d = s[-1].den * s[-2].den
            s.append(My_Fraction(n, d))

        return s

    def __str__(self):
        return f'{self.num}/{self.den}'

fib_s = My_Fraction.generate()

print("\nРяд Фибоначчи:")
for f in fib_s:
    print(f)


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

# Школьники
class School:
    def __init__(self, full_name="", class_number=0, progress=None, hobby=""):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.class_number = class_number
        self.progress = progress
        self.hobby = hobby  # Увлечение школьника

    def __str__(self):
        txt = f"Школьник: {self.full_name} | Класс: {self.class_number} | Увлечение: {self.hobby} | Оценки:"
        for grade in self.progress:
            txt += f" {grade}"
        return txt

def schoolq():
    school = []
    count = int(input("Введите количество школьников: "))
    for i in range(count):
        print(f"\nШкольник {i+1}:")
        full_name = input("Введите полное имя: ")
        class_number = input("Введите номер класса: ")
        hobby = input("Введите увлечение школьника: ")  # Увлечение
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        school.append(School(full_name, class_number, progress, hobby))
    return school

schoolkids = schoolq()

print("\nСписок школьников:")
for s in schoolkids:
    print(s)


# Бакалавры
class Bachelor:
    def __init__(self, full_name="", group_number="", progress=None, specialization=""):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress
        self.specialization = specialization

    def __str__(self):
        txt = f"Бакалавр: {self.full_name} | Группа: {self.group_number} | Специализация: {self.specialization} | Оценки:"
        for grade in self.progress:
            txt += f" {grade}"
        return txt

def bachelorq():
    bachelors = []
    count = int(input("Введите количество бакалавров: "))
    for i in range(count):
        print(f"\nБакалавр {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы: ")
        specialization = input("Введите специализацию бакалавра: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        bachelors.append(Bachelor(full_name, group_number, progress, specialization))
    return bachelors

bachelors = bachelorq()

print("\nСписок бакалавров:")
for s in bachelors:
    print(s)


# Магистранты
class Master:
    def __init__(self, full_name="", group_number="", progress=None, thesis_title=""):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.thesis_title = thesis_title
        self.progress = progress

    def __str__(self):
        txt = f"Магистрант: {self.full_name} | Группа: {self.group_number} | Тема диплома: {self.thesis_title} | Оценки:"
        for grade in self.progress:
            txt += f" {grade}"
        return txt

def mastersq():
    masters = []
    count = int(input("Введите количество магистрантов: "))
    for i in range(count):
        print(f"\nМагистрант {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы: ")
        thesis_title = input("Введите тему дипломной работы: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        masters.append(Master(full_name, group_number, progress, thesis_title))
    return masters

masters = mastersq()

print("\nСписок магистрантов:")
for s in masters:
    print(s)


# Аспиранты
class Aspirant:
    def __init__(self, full_name="", group_number="", research_area="", progress=None):
        if progress is None:
            progress = []
        self.full_name = full_name
        self.group_number = group_number
        self.research_area = research_area
        self.progress = progress

    def __str__(self):
        txt = f"Аспирант: {self.full_name} | Группа: {self.group_number} | Область исследований: {self.research_area} | Оценки:"
        for grade in self.progress:
            txt += f" {grade}"
        return txt

def aspirantq():
    aspirants = []
    count = int(input("Введите количество аспирантов: "))
    for i in range(count):
        print(f"\nАспирант {i+1}:")
        full_name = input("Введите полное имя: ")
        group_number = input("Введите номер группы/кафедры: ")
        research_area = input("Введите область научных исследований: ")
        n = int(input("Введите количество оценок: "))
        progress = []
        for j in range(n):
            grade = int(input(f"Введите оценку {j+1}: "))
            progress.append(grade)
        aspirants.append(Aspirant(full_name, group_number, research_area, progress))
    return aspirants

aspirants = aspirantq()

print("\nСписок аспирантов:")
for s in aspirants:
    print(s)


# Преподаватели
class Teacher:
    def __init__(self, full_name="", subject="", years_of_experience=0):
        self.full_name = full_name
        self.subject = subject
        self.years_of_experience = years_of_experience

    def __str__(self):
        return f"Преподаватель: {self.full_name} | Предмет: {self.subject} | Опыт работы: {self.years_of_experience} лет"

def teachersq():
    teachers = []
    count = int(input("Введите количество преподавателей: "))
    for i in range(count):
        print(f"\nПреподаватель {i+1}:")
        full_name = input("Введите полное имя: ")
        subject = input("Введите предмет: ")
        years_of_experience = int(input("Введите количество стаж: "))
        teachers.append(Teacher(full_name, subject, years_of_experience))
    return teachers

teachers = teachersq()

print("\nСписок преподавателей:")
for t in teachers:
    print(t)
