# tests the 2 deterministic algorithms against the randomly generated data set
from timeit import default_timer as timer
import os
import random

import generate_determ_data as gen

import dp_search as dp
import exhaustive_search2 as exhaus


MAX_VAL = 100
PATH = "./determ_data/"

# sets up the test data
def setup_test_data():
    K_dict = {}
    list_dict = {}
    for p in os.listdir(PATH):
        # from "10000.txt" gives "10000"
        ct = os.path.splitext(p)[0]
        list_dict[ct] = construct_list(os.path.join(PATH, p))
        count = int(ct)
        K_dict[ct] = count * MAX_VAL + 1
    return list_dict, K_dict


# constructs a list from a txt file
def construct_list(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return [int(c.strip()) for c in content]

# size is an int
def test(size, func, k_dict, l_dict):
    l = l_dict[str(size)]
    k = k_dict[str(size)]
    start = timer()
    func(l, k)
    end = timer()
    # time
    return end - start

def main():

    dp_sizes = [10, 50, 100, 500, 1000, 1500]
    exhaus_sizes = [10, 15, 20, 22, 25, 28]

    # test dp first
    print("Size, Algo, Time")
    for size in dp_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test(size, dp.dp_search, k_dict, list_dict)
            print("{}, DP, {}".format(size, time))

    print()
    print("Size, Algo, Time")
    for size in exhaus_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test(size, exhaus.exhaustive_search, k_dict, list_dict)
            print("{}, BF, {}".format(size, time))

    
if __name__ == "__main__":
    main()