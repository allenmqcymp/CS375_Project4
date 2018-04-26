'''
This algorithm will find all possible subsets of a given set and report their sum
These sums can then be checked against the sum inputed in the problem and return true/false based on that


'''
#This defines the subset sum algorithm
def subsetsum(numbers, target):
   size = 1
   subsets = []
   while size <= len(numbers):
      for subs in allSubset(numbers, size):
         if sum(subs) == target:
            subsets.append(subs)
      size += 1
   return subsets

#this will recursively find all the subsets in the set and allow them to be used above
def allSubset(numbers, size):
   if len(numbers) <= 0 or size <= 0:
      yield []
   else:
      for index, number in enumerate(numbers):
         for combination in allSubset(numbers[index+1:], size-1):
            yield [number]+combination
            
a=[1,2,3,4,5,6]

print(subsetsum(a,5))
