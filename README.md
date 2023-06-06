#Объекты и классы. Инкапсуляция, наследование и полиморфизм

Класс Mentor родительский для Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).
Имя, фамилия и список закрепленных курсов у каждого преподавателя реализованы на уровне родительского класса.

Класс Reviewer реализует метод проставления оценок студентам за домашние задание и нахождение средней оценки для каждого студента.
Класс Student - метод проставления оценок лекторам за лекции, а также нахождение средней оценки для каждого лектора.
Лектор закреплен за тем курсом, на который записан студент.

У классов Student и Lecturer есть методы сравнения между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

Создано по 2 экземпляра у каждого класса, вызваны все созданные методы, а также реализованы две функции:

1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса;
2. для подсчета средней оценки за лекции всех лекторов в рамках курса.