'''
 * Maan Qraitem
 * Hill Climbing Algorithm 
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


def hill_climbing(l, max_threshold, k):

	if (k == 0): 
		return

	count = 0 
	current = random.sample(l, random.randrange(1, len(l)) )
	
	while count < max_threshold: 

		new_neighbor = find_neighbor(l, current)

		if (residue(new_neighbor, k) < residue(current, k)):
			current = new_neighbor

		count += 1

	return (residue(current, k), current)

print(hill_climbing([1,2,3,4], 100, 7))