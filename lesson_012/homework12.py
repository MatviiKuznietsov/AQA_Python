"""
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
def multiplication_table(number):
    result_list = []
    multiplier = 1
    while multiplier <= 9:
        result = number * multiplier
        if result >= 25:
            break
        result_list.append(result)
        multiplier += 1
    return result_list


def average_numbers(numbers):
    if not numbers:
        raise ValueError("Empty list")
    return sum(numbers) / len(numbers)


def is_sentence_begin_by_the_time(sentences):
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith('By the time'):
            count += 1
    return count


def get_quantity_distinct_chars(stroke):
    distinct_count = len(set(stroke))
    return distinct_count > 10


def is_h_exist_in_word(word):
    return 'h' in word.lower()