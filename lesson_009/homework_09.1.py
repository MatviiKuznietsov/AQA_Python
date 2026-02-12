"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""

class Rhombus:
    def __init__(self, side_a, coner_a):
        self.side_a = side_a
        self.coner_a = coner_a
        self.coner_b = None

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side should be greater than 0")
            super().__setattr__(name, value)
        elif name == "coner_a":
            if not (0 < value < 180):
                raise ValueError("Corner should be between 0 and 180 degrees")
            super().__setattr__(name, value)
            super().__setattr__("coner_b", 180 - value)
        else:
            super().__setattr__(name, value)

rhombus1 = Rhombus(5, 60)
print(rhombus1.side_a)   # 5
print(rhombus1.coner_a)  # 60
print(rhombus1.coner_b)  # 60
