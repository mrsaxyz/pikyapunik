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
