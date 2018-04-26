# generates all the subsets of a list

from itertools import chain, combinations
import random

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) )

def exhaustive_search(l, k):
    subsets = powerset(l)
    random.shuffle(subsets)
    print(subsets)
    for s in subsets:
        if sum(s) == k:
            return True
    return False

def main():
    a = [1,2,3]
    print(exhaustive_search(a, 9))

if __name__ == "__main__":
    main()