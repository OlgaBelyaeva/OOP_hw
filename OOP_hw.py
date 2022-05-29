# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade__(self):
        all_grade = []
        for value in self.grades.values():
            all_grade += value
        res = round(sum(all_grade) / len(all_grade), 2)
        return res

    def __str__(self):
        res = f"""
Имя студента: {self.name} 
Фамилия студента: {self.surname} 
Средняя оценка за домашние задания: {self.__average_grade__()} 
Курсы в процессе изучения: {', '.join(self.courses_in_progress)} 
Завершенные курсы: {', '.join(self.finished_courses)}"""
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f"""
Неверный ввод. Сравнивать студента можно тольк с другим студентом""")
            return
        return self.__average_grade__() < other.__average_grade__()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade__(self):
        all_grade = []
        for value in self.grades.values():
            all_grade += value
        res = round(sum(all_grade) / len(all_grade), 2)
        return res

    def __str__(self):
        res = f"""
Имя лектора: {self.name} 
Фамилия лектора: {self.surname} 
Средняя оценка лектору за лекции: {self.__average_grade__()}"""
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f"""
Неверный ввод. Сравнивать лектора можно тольк с другим лектором""")
            return
        return self.__average_grade__() < other.__average_grade__()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"""
Имя ревьюэра: {self.name}
Фамилия ревьюэра: {self.surname}"""
        return res


def everage_grade_students(list, course):
    all_grades_students = []
    for student in list:
        for key, value in student.grades.items():
            if key == course:
                all_grades_students += value
            else:
                pass
    res = f"""
Средняя оценка за домашние задания по всем студентам на курсе {course}: {round(sum(all_grades_students) / len(all_grades_students), 2)}"""
    return res


def everage_grade_lecturer(list, course):
    all_grades_lecturer = []
    for lecturer in list:
        for key, value in lecturer.grades.items():
            if key == course:
                all_grades_lecturer += value
            else:
                pass
    res = f"""
Средняя оценка за лекции всех лекторов в рамках курса {course}: {round(sum(all_grades_lecturer) / len(all_grades_lecturer), 2)}"""
    return res


best_student = Student('Sponge', 'Bob', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses = ['Введение в программирование']

super_student = Student('Patrick', 'Star', 'male')
super_student.courses_in_progress += ['Python']
super_student.finished_courses = ['Введение в программирование', 'Git']

cool_reviewer = Reviewer('Krusty', 'Krab')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Git', 4)
cool_reviewer.rate_hw(super_student, 'Python', 4)
cool_reviewer.rate_hw(super_student, 'Python', 3)

great_reviewer = Reviewer('Squidvard', 'Tentacles')
great_reviewer.courses_attached += ['Python']
great_reviewer.rate_hw(best_student, 'Python', 10)
great_reviewer.rate_hw(best_student, 'Python', 9)
great_reviewer.rate_hw(super_student, 'Python', 7)
great_reviewer.rate_hw(super_student, 'Python', 7)

cool_lecturer = Lecturer('Sheldon', 'Plankton')
cool_lecturer.courses_attached += ['Git']

great_lecturer = Lecturer('Karen', 'Plankton')
great_lecturer.courses_attached += ['Python', 'Git']

best_student.rate_hw(cool_lecturer, 'Git', 7)
best_student.rate_hw(cool_lecturer, 'Git', 9)
best_student.rate_hw(great_lecturer, 'Python', 10)
best_student.rate_hw(great_lecturer, 'Python', 8)
best_student.rate_hw(great_lecturer, 'Git', 6)
best_student.rate_hw(great_lecturer, 'Git', 7)

super_student.rate_hw(great_lecturer, 'Python', 7)
super_student.rate_hw(great_lecturer, 'Python', 7)

student_list = [best_student, super_student]

lecturer_list = [cool_lecturer, great_lecturer]

print(best_student.grades)
print(super_student.grades)
print(cool_lecturer.grades)
print(great_lecturer.grades)
print(cool_reviewer)
print(great_reviewer)
print(cool_lecturer)
print(great_lecturer)
print(best_student)
print(super_student)
print()
print(best_student < super_student)
print(best_student > super_student)
print(cool_lecturer > great_lecturer)
print(cool_lecturer < great_lecturer)
print(best_student < great_lecturer)
print(everage_grade_students(student_list, 'Python'))
print(everage_grade_students(student_list, 'Git'))
print(everage_grade_lecturer(lecturer_list, 'Python'))
print(everage_grade_lecturer(lecturer_list, 'Git'))