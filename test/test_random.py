from unittest import TestCase

from myrandgen import *


class TestRandomGen(TestCase):

    def test_generate_0(self):
        # Setup
        expected = 0
        # Execute
        target = list_of_random_n(0)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_1(self):
        # Setup
        expected = 1
        # Execute
        target = list_of_random_n(1)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_10(self):
        # Setup
        expected = 10
        # Execute
        target = list_of_random_n(10)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_100(self):
        # Setup
        expected = 100
        # Execute
        target = list_of_random_n(100)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_1000(self):
        # Setup
        expected = 1000
        # Execute
        target = list_of_random_n(1000)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_10000(self):
        # Setup
        expected = 10000
        # Execute
        target = list_of_random_n(10000)
        # Assert
        self.assertEqual(expected, len(target))

    def test_generate_100000(self):
        # Setup
        expected = 100000
        # Execute
        target = list_of_random_n(100000)
        # Assert
        self.assertEqual(expected, len(target))


class TestAverage(TestCase):

    def test_zero(self):
        # Setup
        values = []
        expected = 0
        # Execute
        avg = average_of_list(values)
        # Assert
        self.assertEqual(expected, avg)

    def test_one(self):
        # Setup
        values = [512.12]
        expected = 512.12
        # Execute
        avg = average_of_list(values)
        # Assert
        self.assertEqual(expected, avg)

    def test_two(self):
        # Setup
        values = [8, 2]
        expected = 5
        # Execute
        avg = average_of_list(values)
        # Assert
        self.assertEqual(expected, avg)

    def test_10(self):
        # Setup
        values = [10 for _ in range(10)]
        expected = 10
        # Execute
        avg = average_of_list(values)
        # Assert
        self.assertEqual(expected, avg)

class TestStandardDeviation(TestCase):

    def test_std(self):
        # Setup
        values = [4, 6, 4, 6, 4, 6]
        expected = 1
        # Execute
        sd = standard_deviation_of_list(values)
        # Assert
        self.assertEqual(expected, sd)
