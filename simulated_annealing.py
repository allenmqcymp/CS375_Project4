'''
 * Maan Qraitem
 * simulated annealing Algorithm 
'''


import random 


def find_neighbor(l, s):

	t = s[:]

	i, j = random.sample(range(0, len(l)), 2)

	if (l[i] in s):
		t.remove(l[i])

	else: 
		t.append(l[i])

	if (l[j] in s):
		if (random.random() < 0.5):
			t.remove(l[j])

	else: 
		if (random.random() < 0.5): 
			t.append(l[j])

	return t


def residue(s, k): 
	total = sum(s)
	return abs(total - k)


def simulated_annealing(l, max_threshold, k):

	if (k == 0): 
		return

	count = 0 
	current = random.sample(l, random.randrange(1, len(l)) )
	smallest_residue = residue(current, k)

	while count < max_threshold: 

		neighbor = find_neighbor(l, current)

		if (residue(neighbor, k) < residue(current, k)):
			current = neighbor

		else: 
			prob = (residue(neighbor, k) - residue(current, k)) / (10000000000 * (0.8**(count/300)))
			if (random.random() < prob):
				current = neighbor

		if (residue(current, k) < smallest_residue): 
			smallest_residue = residue(current, k)

		count += 1

	return (smallest_residue, current)

print(simulated_annealing([1,2,3,4], 100, 7))