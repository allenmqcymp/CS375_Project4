'''
  * Maan Qraitem 
  * CS 375 
  * Test the approximating algorithms on the generated data_approx
  * Data Info: 
  		* Numbers range between 1 and 10^12
  		* Each list is of length 100
  		* Total samples = 50
'''


import numpy as np 
from greedy_search import greedy_search
from  random_search import random_search
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing

RANGE_MIN = 1
RANGE_MAX = 10**12
K = 25*RANGE_MAX
TOTAL_SIZE = 100
TOTAL = 50
METHODS_NUM = 4
MAX_THRESHOLD = 1000

core = {"random": [random_search, 0], "greedy": [greedy_search, 1], "hill_climbing": [hill_climbing, 2]
			, "simulated_annealing" : [simulated_annealing, 3]}


samples = np.genfromtxt('./data/data_approx.csv', delimiter=',')
reisudes = np.zeros((TOTAL, METHODS_NUM))

def fill_in_reisude(method): 
	for i in range(TOTAL): 
		func = core[method][0]
		idx = core[method][1]
		reisudes[i, idx] = func(samples[i,:].tolist(), MAX_THRESHOLD, K)


def main(): 
	fill_in_reisude("random")
	print("-------- Done with Random ----------")
	fill_in_reisude("greedy")
	print("-------- Done with greedy ----------")
	fill_in_reisude("hill_climbing")
	print("-------- Done with hill_climbing ----------")
	fill_in_reisude("simulated_annealing")
	print("-------- Done with simulated_annealing ----------")
	np.savetxt("./reisudes_data.csv", samples, delimiter=',', comments="")



if __name__ == "__main__":
	main()