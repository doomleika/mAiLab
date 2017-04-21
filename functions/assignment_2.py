"""Functions for assignment 2"""

import random


def list_of_random_n(n):
    """generates n of random values"""
    return [random.uniform(-1, 1) for _ in range(n)]


def total_of_list(a_list):
    """Calculates the total value of the list"""
    total = 0
    for i in a_list:
        total += i
    return total


def average_of_list(a_list):
    """Calculates the average value of the list"""
    length = len(a_list)
    if 0 == length:
        return 0
    total_value = total_of_list(a_list)
    return total_value / length


def standard_deviation_of_list(a_list):
    """Generates standard deviation of the list"""
    average_value = average_of_list(a_list)
    diff_list = [(i - average_value) ** 2 for i in a_list]
    return average_of_list(diff_list)
