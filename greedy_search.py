# random search algo for the subset sum problem
# CS 375 Project 4

def greedy_search(l, k):
    if k == 0:
        return True

    # timsort with worst case nlogn
    l.sort(reverse=True)
    # repeatedly pop off head of the list
    subset = []
    while len(l) > 0:
        try_val = l.pop(0)
        if sum(subset) + try_val == k:
            return True
        elif sum(subset) + try_val < k:
            subset.append(try_val)
    return abs(k - sum(subset))

def main():
    print(greedy_search([1,2,3,1,1], 7))

if __name__ == "__main__":
    main()
        
        

