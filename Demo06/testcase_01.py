# from unittest import TestCase
import unittest


def my_sum(a, b):
    return a + b


class my_test(unittest.TestCase):
    def test_01(self):
        print(my_sum(10, 10))

    def test_02(self):
        print(my_sum(0, 100))

