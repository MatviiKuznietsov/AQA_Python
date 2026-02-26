import unittest
from lesson_012.homework12 import (
    multiplication_table,
    average_numbers,
    is_sentence_begin_by_the_time,
    get_quantity_distinct_chars,
    is_h_exist_in_word
)

class TestHomeworks(unittest.TestCase):

    # multiplication_table tests
    def test_multiplication_table_basic(self):
        self.assertEqual(multiplication_table(2), [2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_multiplication_table_break_condition(self):
        self.assertEqual(multiplication_table(5), [5, 10, 15, 20])

    # average_numbers tests
    def test_average_numbers_positive(self):
        self.assertEqual(average_numbers([2, 4, 6]), 4)

    def test_average_numbers_single_value(self):
        self.assertEqual(average_numbers([10]), 10)

    def test_average_numbers_empty_list(self):
        with self.assertRaises(ValueError):
            average_numbers([])

    # is_sentence_begin_by_the_time tests
    def test_sentence_count_basic(self):
        sentences = ["By the time I arrived", "Hello world", "By the time we left"]
        self.assertEqual(is_sentence_begin_by_the_time(sentences), 2)

    def test_sentence_count_zero(self):
        sentences = ["Hello", "World"]
        self.assertEqual(is_sentence_begin_by_the_time(sentences), 0)

    # get_quantity_distinct_chars tests
    def test_distinct_chars_true(self):
        self.assertTrue(get_quantity_distinct_chars("abcdefghijk"))

    def test_distinct_chars_false(self):
        self.assertFalse(get_quantity_distinct_chars("abc"))

    # is_h_exist_in_word tests
    def test_h_exist_lowercase(self):
        self.assertTrue(is_h_exist_in_word("hello"))

    def test_h_exist_uppercase(self):
        self.assertTrue(is_h_exist_in_word("Hello"))

    def test_h_not_exist(self):
        self.assertFalse(is_h_exist_in_word("world"))


if __name__ == "__main__":
    unittest.main()