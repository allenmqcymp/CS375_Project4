'''
 * Maan Qraitem
 * Hill Climbing Algorithm
'''


import random


def find_neighbor(l, s):

	t = s[:]

	l_set = set(l)
	l_set_list = list(l_set)

	i_set, j_set = random.sample(range(0, len(l_set_list)), 2)

	l_i = l_set_list[i_set]
	l_j = l_set_list[j_set]

	if (l_i in s):
		t.remove(l_i)

	else:
		t.append(l_i)

	if (l_j in s):
		if (random.random() < 0.5):
			t.remove(l_j)

	else:
		if (random.random() < 0.5):
			t.append(l_j)

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

	return residue(current, k)


def main():
	print(hill_climbing([1,2,3,4], 100, 7))

if __name__ == "__main__":
	main()
