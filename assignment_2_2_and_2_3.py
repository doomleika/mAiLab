"""mAiLab assignment 2-2: generate 10/100/1000/10000/100000 random numbers within -1~1"""

from datetime import datetime
import logging

from functions import list_of_random_n, average_of_list, standard_deviation_of_list


def main():
    logging.debug('{} starting'.format(datetime.now()))
    list_length = [10 ** i for i in range(1, 6)]
    for length in list_length:
        logging.info('Generating {} random numbers...'.format(length))
        timestamp_before_generate = datetime.now()
        numbers = list_of_random_n(length)
        time_used = timestamp_before_generate - datetime.now()
        logging.info('used {} microseconds'.format(time_used.microseconds))
        avg = average_of_list(numbers)
        sd = standard_deviation_of_list(numbers)
        print('Average of list of {}: {}'.format(length, avg))
        print('Standard deviation of list of {}: {}'.format(length, sd))
    logging.debug('{} finished'.format(datetime.now()))


if '__main__' == __name__:

    logging.basicConfig(level=logging.INFO)
    main()