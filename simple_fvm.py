#
# Created by Brendan Berg on 01.11.2019
#

import numpy as np


class SimpleFVM(object):
    def __init__(self, iterations):
        self.__iterations = iterations

    def iterate(self):
        self.__iterations -= 1
        return self.__iterations >= 0


def solve_for_velocity_field(velocity_field, pressure_field):
    return velocity_field
