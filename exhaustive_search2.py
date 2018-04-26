# generates all the subsets of a list

from itertools import chain, combinations
import random

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def exhaustive_search(l, k):
    for s in powerset(l):
        if sum(s) == k:
            return True
    return False

def main():
    a = [1,2,3]
    print(exhaustive_search(a, 9))

if __name__ == "__main__":
    main()