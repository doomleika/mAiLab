"""Assignment 2 for mAiLab"""

import logging
import random
import datetime


random_numbers = 10


def list_of_random_n(n):
    return [random.uniform(-1, 1) for _ in range(n)]

def total_of_list(a_list):
    """"""
    total = 0
    for i in a_list:
        total += i
    return total

def average_of_list(a_list):
    length = len(a_list)
    if(length == 0):
        return 0
    total_value = total_of_list(a_list)
    return total_value / length

def standard_deviation_of_list(a_list):
    average_value = average_of_list(a_list)
    diff_list = [(i - average_value) ** 2 for i in a_list]
    return average_of_list(diff_list)

if '__main__' == __name__:

    logging.basicConfig(level=logging.INFO)

    logging.info('Right now {}'.format(datetime.datetime.now()))

    random_list = list_of_random_n(100)
    logging.info('All values: {}'.format(random_list))

    avg = average_of_list(random_list)
    logging.info('Average: {}'.format(avg))

    standard_deviation = standard_deviation_of_list(random_list)
    logging.info('Standard deviation: {}'.format(standard_deviation))
