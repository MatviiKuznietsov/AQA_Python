'''
Генератори:

Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
Ітератори:

Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
Декоратори:

Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
'''


# ========================================================================

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


print(list(even_numbers(10)))


# ========================================================================

def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        a, b = b, a + b


print(list(fibonacci(100)))


# ========================================================================

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


for x in ReverseIterator([1, 2, 3, 4]):
    print(x)

#========================================================================

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1
            if num % 2 == 0:
                return num
        raise StopIteration


for x in EvenIterator(10):
    print(x)
#========================================================================

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        print(f"[LOG] args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[LOG] result={result}")
        return result

    return wrapper


@logger
def sum_numbers(a, b):
    return a + b


sum_numbers(3, 5)
#========================================================================

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {e}")
            return None

    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b


print(divide(10, 2))
print(divide(10, 0))
