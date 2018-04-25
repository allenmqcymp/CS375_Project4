# random search algo for the subset sum problem
# CS 375 Project 4
import random

def random_search(l, max_threshold, k):
    if k == 0:
        return True
        
    residue = k
    count = 0
    while count < max_threshold:
        sample = random.sample(l, random.randrange(1, len(l)) )
        try_sum = sum(sample)
        if try_sum == k:
            return True
        elif abs(try_sum - k) < abs(residue):
            residue = abs(try_sum - k)
        count += 1
    print("failed to find solution")
    return residue

def main():
    print(random_search([1,2,3,18,1], 10000, 9))

if __name__ == "__main__":
    main()