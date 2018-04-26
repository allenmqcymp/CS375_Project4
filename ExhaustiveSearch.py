'''
This algorithm will find all possible subsets of a given set and report their sum
These sums can then be checked against the sum inputed in the problem and return true/false based on that


'''
#This defines the subset sum algorithm
def subsetsum(numbers, target):
    size = 1
    all_subsets = []
    while size <= len(numbers):
        for subs in allSubset(numbers, size):
            all_subsets.append(subs)
        size += 1
    return all_subsets

# size is the given size
def allSubset(numbers, size):
    if len(numbers) <= 0 or size <= 0:
        yield []
    else:
        for index, number in enumerate(numbers):
            for combination in allSubset(numbers[index+1:], size-1):
                yield [number]+combination

def main():
    a=[1, 4, 9, 8, 5, 9, 10, 8, 9, 1]
    l = subsetsum(a,6)
    print(len(l))

if __name__ == "__main__":
    main()
