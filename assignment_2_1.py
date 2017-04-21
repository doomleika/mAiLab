"""mAiLab assignment 2-1: generate 5 random numbers"""

import datetime
import logging

from functions import list_of_random_n


def main():
    logging.debug('{} starting'.format(datetime.datetime.now()))
    number = 5
    print(list_of_random_n(number))
    logging.debug('{} finished'.format(datetime.datetime.now()))


if '__main__' == __name__:
    logging.basicConfig(level=logging.INFO)
    main()
