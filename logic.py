"""
Author: Wojciech Kondracki 310941
Date: 08.03.2024
"""

import numpy as np


def exhaustive(mass, value, max_weight):
    """
    Searches using the exhaustive method to find the optimal solution
    for the backpack problem.

    Parameters:
        mass (np.array): Array containing the weights of items.
        value (np.array): Array containing the values of items.
        max_weight (float): Maximum allowable weight.

    Returns:
        tuple: Tuple containing the array of the optimal set of items,
               the total value and the weight of this set.
    """

    items_count = mass.size
    res_items = []
    res_value = 0
    res_mass = 0

    for num in range(0, 2 ** items_count):
        bin_num = format(num, '0' + str(items_count) + 'b')
        bin_arr = np.array([int(b) for b in bin_num])

        curr_mass = sum(np.multiply(mass, bin_arr))
        curr_value = sum(np.multiply(value, bin_arr))

        if curr_mass <= max_weight and curr_value > res_value:
            res_value = curr_value
            res_mass = curr_mass
            res_items = bin_arr

    return res_items, res_value, res_mass


def heuristic(mass, value, max_weight):
    """
    Finds an approximate solution to the backpack problem
    using a simple heuristic.

    Parameters:
        mass (np.array): Array containing the weights of items.
        value (np.array): Array containing the values of items.
        max_weight (float): Maximum allowable weight.

    Returns:
        tuple: Tuple containing the array with an approximate set of items,
               the total value and the weight of this set.
    """

    prop = np.divide(value, mass)
    min_mass = np.min(mass)

    curr_mass = 0
    res_value = 0
    res_mass = 0
    res_items = np.zeros(mass.size, dtype=int)

    stop_flag = False

    while not stop_flag:
        ind = np.argmax(prop)
        curr_mass += mass[ind]
        if min_mass + curr_mass > max_weight:
            stop_flag = True
        else:
            res_value += value[ind]
            res_mass += curr_mass
            prop[ind] = -1
            res_items[ind] = 1

    return res_items, res_value, res_mass
