'''
  * Maan Qraitem 
  * CS 375 
  * Generates data for testing the approximations methods.
  * Data Info: 
  		* Numbers range between 1 and 10^12
  		* Each list is of length 100
  		* Total samples = 50
'''


import numpy as np 


RANGE_MIN = 1
RANGE_MAX = 10**12
K = 25*RANGE_MAX
TOTAL_SIZE = 100
TOTAL = 50

samples = np.zeros((50, 100))


# Generates a sample data
def generate_sample(): 
	return np.random.randint(RANGE_MIN, RANGE_MAX, TOTAL_SIZE)


#Add TOTAL number of samples to @param: dest. 
def create_data(dest): 
	for i in range(TOTAL): 
		dest[i,:] = generate_sample()


create_data(samples)

#saves the samples array to a csv file 
np.savetxt("./data/data_approx.csv", samples, delimiter=',', comments="")


