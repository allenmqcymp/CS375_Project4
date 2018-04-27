# tests the 2 deterministic algorithms against the randomly generated data set
from timeit import default_timer as timer
import os
import random

import generate_determ_data as gen

import dp_search as dp
import exhaustive_search2 as exhaus

from greedy_search import greedy_search
from  random_search import random_search
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing

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
        K_dict[ct] = sum(random.sample(list_dict[ct], random.randrange(1, len(list_dict[ct])))) + \
                                    random.randint(min(list_dict[ct]), max(list_dict[ct]))
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

# size is an int
def test__approx(size, func, k_dict, l_dict):
    l = l_dict[str(size)]
    k = k_dict[str(size)]
    start = timer()
    func(l, 1000, k)
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


    print()
    print("Size, Algo, Time")
    for size in dp_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test__approx(size, greedy_search, k_dict, list_dict)
            print("{}, Greedy Search, {}".format(size, time))

    print()
    print("Size, Algo, Time, MAX_threshold")
    for size in dp_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test__approx(size, random_search, k_dict, list_dict)
            print("{}, Random Search, {}, 1000".format(size, time))

    print()
    print("Size, Algo, Time, MAX_threshold")
    for size in dp_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test__approx(size, hill_climbing, k_dict, list_dict)
            print("{}, Hill Climbing, {}, 1000".format(size, time))

    print()
    print("Size, Algo, Time, MAX_threshold")
    for size in dp_sizes:
        for _ in range(5):
            gen.generate_data()
            list_dict, k_dict = setup_test_data()
            time = test__approx(size, simulated_annealing, k_dict, list_dict)
            print("{}, Simulated Annealing, {}, 1000".format(size, time))


if __name__ == "__main__":
    main()
