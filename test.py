"""
Author: Wojciech Kondracki 310941
Date: 08.03.2024
"""

from logic import exhaustive, heuristic
import numpy as np
import time

# Define the weights of the items
m = np.array([8, 3, 5, 2])
# Set the maximum weight of the backpack to be half of the total weight of items
M = np.sum(m) / 2
# Define the values of the items
p = np.array([16, 8, 9, 6])

# Generate random weights for a larger set of items - 23 items
m_rand = np.random.randint(1, 30, 23)
M_rand = np.sum(m_rand) / 2  # Set the max weight to half of the total
p_rand = np.random.randint(1, 30, 23)

# Generate second set of random weights and values for testing - 24 items
m_rand2 = np.random.randint(1, 30, 24)
M_rand2 = np.sum(m_rand2) / 2
p_rand2 = np.random.randint(1, 30, 24)

# Generate third set of random weights and values for testing - 1000 items
m_rand3 = np.random.randint(1, 30, 10000)
M_rand3 = np.sum(m_rand2) / 2
p_rand3 = np.random.randint(1, 30, 10000)

# Generate fourth set of random weights and values for testing - 2000 items
m_rand4 = np.random.randint(1, 30, 20000)
M_rand4 = np.sum(m_rand2) / 2
p_rand4 = np.random.randint(1, 30, 20000)

if __name__ == '__main__':
    # Test the exhaustive search function on the given set
    items, value, mass = exhaustive(m, p, M)
    print("Exhaustive method: ", items, value, mass)

    # Test the simple heuristic method on the given set
    items, value, mass = heuristic(m, p, M)
    print("Simple heuristic method: ", items, value, mass)

    print("-- 23 items set --")

    # Measure execution time of the exhaustive search on the first random set
    start = time.process_time()
    exhaustive(m_rand, p_rand, M_rand)
    end = time.process_time()
    total = end - start
    print("Exhaustive method: {0:02f}s".format(total))

    # Measure execution time of the simple heuristic method on the first random set
    start = time.process_time()
    heuristic(m_rand, p_rand, M_rand)
    end = time.process_time()
    total = end - start
    print("Simple heuristic method: {0:02f}s".format(total))

    print("-- 24 items set --")

    # Measure execution time of the exhaustive search on the second random set
    start = time.process_time()
    exhaustive(m_rand2, p_rand2, M_rand2)
    end = time.process_time()
    total = end - start
    print("Exhaustive method: {0:02f}s".format(total))

    # Measure execution time of the simple heuristic method on the second random set
    start = time.process_time()
    heuristic(m_rand2, p_rand2, M_rand2)
    end = time.process_time()
    total = end - start
    print("Simple heuristic method: {0:02f}s".format(total))

    print("-- 10000 items set --")

    # Measure execution time of the simple heuristic method on the third random set
    start = time.process_time()
    heuristic(m_rand3, p_rand3, M_rand3)
    end = time.process_time()
    total = end - start
    print("Simple heuristic method: {0:02f}s".format(total))

    print("-- 20000 items set --")

    # Measure execution time of the simple heuristic method on the fourth random set
    start = time.process_time()
    heuristic(m_rand4, p_rand4, M_rand4)
    end = time.process_time()
    total = end - start
    print("Simple heuristic method: {0:02f}s".format(total))
