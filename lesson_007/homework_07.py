from lesson_004.homework_04 import *

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити."""


def multiplication_table(number):
    multiplier = 1
    max_number = 9
    while multiplier <= max_number:
        result = number * multiplier
        if result >= 25:
            break
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1  # Increment the appropriate variable


multiplication_table(5)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""


def sum_numbers(number1, number2):
    result = number1 + number2
    print(f"Summ = {result}")
    return result


sum_numbers(3, 4)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел."""


def average_numbers(numbers):
    summ_numbers = 0
    for number in numbers:
        summ_numbers += number
    summ_numbers /= len(numbers)
    print(f"Average = {summ_numbers}")
    return summ_numbers

average_numbers([1, 3, 5])
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def invert_string(string):
    return string[::-1]

print(invert_string("Hello, world!"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def get_longest_word(string):
    longest_word = ''
    words = string.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(f"The longest word - {get_longest_word('Hello new strange world')}")
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
def get_quantity_distinct_chars(string):
    distinct_line = set(string)
    print(f"Quantity distinct chars from stroke = {len(distinct_line)}")
    if len(distinct_line) > 10:
        print('true')
    else:
        print('false')


get_quantity_distinct_chars("The quick brown fox jumps over the lazy dog")

# task 8
def is_sentence_begin_by_the_time(sentences):
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith('By the time'):
            count += 1
    print(f'{count} sentence begin from "By the time"')


is_sentence_begin_by_the_time(adwentures_of_tom_sawer_sentences)

# task 9
def get_quantity_capital_words(string):
    words = string.split()
    count = 0
    for word in words:
        if word.istitle():
            count = count + 1
    print(f'Quantity words start with capital letter = {count}')

get_quantity_capital_words(adwentures_of_tom_sawer)
# task 10
"""
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими

"""
def get_only_string(*args):
    lst = []
    print(args)
    for i in range(len(args)):
     if type(args[i]) == str:
        lst.append(args[i])
    return lst

print(get_only_string('1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
