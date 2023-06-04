class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        sum_grades = 0
        courses_in_progress_print = ', '.join(self.courses_in_progress)
        finished_courses_print = ', '.join(self.finished_courses)

        for course in self.grades:
            sum_grades += len(self.grades[course])

        self.average_rating = sum(map(sum, self.grades.values())) / sum_grades

        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_print}\n' \
              f'Завершенные курсы: {finished_courses_print}'

        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Сравнение некорректно')
            return 0
        return self.average_rating < student.average_rating


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """ Могут получать оценки за лекции от студентов"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}
        self.average_rating = 0

    def __str__(self):
        sum_grades = 0

        for course in self.grades_for_lectures:
            sum_grades += len(self.grades_for_lectures[course])

        self.average_rating = sum(map(sum, self.grades_for_lectures.values())) / sum_grades
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {self.average_rating}'

        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Сравнение некорректно')
            return 0
        return self.average_rating < lecturer.average_rating


class Reviewer(Mentor):
    """ Могут выставлять студентам оценки за домашние задания"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФЙамилия: {self.surname}'
        return res


if __name__ == "__main__":

    first_student = Student('Olga', 'Ivanova')
    first_student.finished_courses += ['Go']
    first_student.courses_in_progress += ['Python']

    second_student = Student('Petr', 'Smirnov')
    second_student.finished_courses += ['C++']
    second_student.courses_in_progress += ['Go']

    first_lecturer = Lecturer('Irina', 'Sidorova')
    first_lecturer.courses_attached += ['Python', 'Git']

    second_lecturer = Lecturer('Ivan', 'Sidorov')
    second_lecturer.courses_attached += ['Go', 'C++']

    first_reviewer = Reviewer('Dmitriy', 'Popov')
    first_reviewer.courses_attached += ['Go', 'C++']

    second_reviewer = Reviewer('Denis', 'Petrov')
    second_reviewer.courses_attached += ['Python']

    first_student.rate_lecture(first_lecturer, 'Python', 8)
    first_student.rate_lecture(first_lecturer, 'Python', 9)
    first_student.rate_lecture(first_lecturer, 'Python', 10)

    second_student.rate_lecture(second_lecturer, 'Go', 6)
    second_student.rate_lecture(second_lecturer, 'Go', 8)
    second_student.rate_lecture(second_lecturer, 'Go', 10)

    first_reviewer.rate_hw(second_student, 'Go', 6)
    first_reviewer.rate_hw(second_student, 'Go', 8)
    first_reviewer.rate_hw(second_student, 'Go', 10)

    second_reviewer.rate_hw(first_student, 'Python', 4)
    second_reviewer.rate_hw(first_student, 'Python', 5)
    second_reviewer.rate_hw(first_student, 'Python', 9)

    print(f'Студенты:\n\n{first_student}\n\n{second_student}\n')

    if {first_student > second_student} == True:
        print(f'Средняя оценка за д/з у {first_student.name} {first_student.surname}' \
            f' больше чем у {second_student.name} {second_student.surname}\n')
    else:
        print(f'Средняя оценка за д/з у {first_student.name} {first_student.surname}' \
            f' меньше чем у {second_student.name} {second_student.surname}\n')

    student_courses = [
        ['Go', [second_student.name, second_student.surname]],
        ['Python', [first_student.name, first_student.surname]]
    ]

    def average_grade_all_studenst(courses):
        sum_total = 0
        for course in courses:
            if course[0] in first_student.courses_in_progress:
                sum_total += first_student.average_rating
            if course[0] in second_student.courses_in_progress:
                sum_total += second_student.average_rating
        print(f'Средняя оценка за все домашние задания у студентов: {sum_total}\n')

    all_students = average_grade_all_studenst(student_courses)

    print(f'Лекторы:\n\n{first_lecturer}\n\n{second_lecturer}\n')

    if {first_lecturer > second_lecturer} == True:
        print('Средняя оценка за лекции у' \
            f'{first_lecturer.name} {first_lecturer.surname}' \
            f' больше чем у {second_lecturer.name} {second_lecturer.surname}\n')
    else:
        print('Средняя оценка за лекции у' \
            f' {first_lecturer.name} {first_lecturer.surname}' \
            f' меньше чем у {second_lecturer.name} {second_lecturer.surname}\n')

    lecturer_courses = [
        ['Go', 'C++', [second_lecturer.name, second_lecturer.surname]],
        ['Python', 'Git', [first_lecturer.name, first_lecturer.surname]]
    ]

    def average_grade_all_lecturers(courses):
        sum_total = 0
        for course in courses:
            if course[0] in first_lecturer.courses_attached:
                sum_total += first_lecturer.average_rating
            if course[0] in second_lecturer.courses_attached:
                sum_total += second_lecturer.average_rating
        print(f'Средняя оценка за все лекции составляет: {sum_total}')

    all_lecturers = average_grade_all_lecturers(lecturer_courses)
