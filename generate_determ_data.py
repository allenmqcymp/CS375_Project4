'''
    Test code for the two deterministic algorithms - subset
'''
# the numbers of integers to test is as follows:

# 10, 50, 100, 1000, 10_000, 100_000, 1_000_000, 10_000_000

# if any run takes longer than 1 hour, then we'll terminate and say that no result has been found

# the k value to search for is the range of the length of the list
# shifted by 1/2 the length of the list
# for example, if the list was 100 elements long, then the k value would be a random value from 50 to 150

# the interval to choose the numbers is [1, 100]

import os.path
import random

RANGE_MIN = 1
RANGE_MAX = 100

DEST = "./determ_data/"

# Generates a sample data
def generate_sample(length):
    r_list = []
    for i in range(length):
        r_list.append(random.randrange(RANGE_MIN, RANGE_MAX + 1))
    return r_list

	
def generate_data():
    # generate according to sizes
    sizes = [10**1, 5 * 10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]
    for sz in sizes:
        path = os.path.join(DEST, "{}.txt".format(sz) )
        with open(path, 'w') as f:
            for item in generate_sample(sz):
                f.write("%s\n" % item)


generate_data()


