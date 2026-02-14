"""
Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
import math
from abc import abstractmethod, ABC


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.sideA = side_a
        self.sideB = side_b

    def get_area(self):
        return self.sideA * self.sideB

    def get_perimeter(self):
        return (self.sideA + self.sideB) * 2


class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * self.PI

    def get_perimeter(self):
        return 2 * self.radius * self.PI

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c))

    def get_perimeter(self):
        return self.__side_a+ self.__side_b + self.__side_c

shapes = [
    Rectangle(3, 4),
    Rectangle(2, 5),
    Circle(6),
    Circle(4),
    Triangle(3, 4, 5),
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area = {shape.get_area():.2f}")
    print(f"  Perimeter = {shape.get_perimeter():.2f}")
