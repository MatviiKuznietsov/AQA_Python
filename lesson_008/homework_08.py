"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.__average_mark = 0

    def set_average_mark(self, average_mark):
        self.__average_mark = average_mark

    def get_average_mark(self):
        return self.__average_mark


student_vova = Student(name='Vova', surname="Trofimov", age=20)
student_vova.set_average_mark(50)
print(f"Student: \nname - {student_vova.name},"
      f"\nsurname - {student_vova.surname},"
      f"\nage - {student_vova.age},"
      f"\naverage_mark - {student_vova.get_average_mark()}")

