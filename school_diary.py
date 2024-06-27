import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks

def print_marks():
    for student in students:
        print(f"{student}: {students_marks[student]}")

def add_mark(student, class_, mark):
    if student in students_marks and class_ in students_marks[student]:
        students_marks[student][class_].append(mark)
    else:
        print("Ученик или предмет не найден.")

def delete_mark(student, class_, mark):
    if student in students_marks and class_ in students_marks[student]:
        if mark in students_marks[student][class_]:
            students_marks[student][class_].remove(mark)
        else:
            print("Оценка не найдена.")
    else:
        print("Ученик или предмет не найден.")

def edit_mark(student, class_, old_mark, new_mark):
    if student in students_marks and class_ in students_marks[student]:
        if old_mark in students_marks[student][class_]:
            idx = students_marks[student][class_].index(old_mark)
            students_marks[student][class_][idx] = new_mark
        else:
            print("Оценка не найдена.")
    else:
        print("Ученик или предмет не найден.")

def average_marks(student):
    if student in students_marks:
        total_marks = 0
        count = 0
        for marks in students_marks[student].values():
            total_marks += sum(marks)
            count += len(marks)
        return total_marks / count if count > 0 else 0
    else:
        print("Ученик не найден.")
        return 0

def add_student(student):
    if student not in students:
        students.append(student)
        students_marks[student] = {class_: [] for class_ in classes}
    else:
        print("Ученик уже существует.")

def delete_student(student):
    if student in students:
        students.remove(student)
        del students_marks[student]
    else:
        print("Ученик не найден.")

def add_class(class_):
    if class_ not in classes:
        classes.append(class_)
        for student in students_marks:
            students_marks[student][class_] = []
    else:
        print("Предмет уже существует.")

def delete_class(class_):
    if class_ in classes:
        classes.remove(class_)
        for student in students_marks:
            del students_marks[student][class_]
    else:
        print("Предмет не найден.")

while True:
    print('''Список команд:
    1. Добавить оценку ученика по предмету
    2. Удалить оценку ученика по предмету
    3. Редактировать оценку ученика по предмету
    4. Вывести средний балл по всем предметам по каждому ученику
    5. Добавить ученика
    6. Удалить ученика
    7. Добавить предмет
    8. Удалить предмет
    9. Вывести все оценки по всем ученикам
    10. Выход из программы''')

    command = int(input("Введите команду: "))

    if command == 1:
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку: "))
        add_mark(student, class_, mark)
    elif command == 2:
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        mark = int(input("Введите оценку для удаления: "))
        delete_mark(student, class_, mark)
    elif command == 3:
        student = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        old_mark = int(input("Введите старую оценку: "))
        new_mark = int(input("Введите новую оценку: "))
        edit_mark(student, class_, old_mark, new_mark)
    elif command == 4:
        for student in students:
            avg = average_marks(student)
            print(f"{student}: Средний балл = {avg:.2f}")
    elif command == 5:
        student = input("Введите имя нового ученика: ")
        add_student(student)
    elif command == 6:
        student = input("Введите имя ученика для удаления: ")
        delete_student(student)
    elif command == 7:
        class_ = input("Введите название нового предмета: ")
        add_class(class_)
    elif command == 8:
        class_ = input("Введите название предмета для удаления: ")
        delete_class(class_)
    elif command == 9:
        print_marks()
    elif command == 10:
        break
    else:
        print("Неверная команда, попробуйте снова.")
