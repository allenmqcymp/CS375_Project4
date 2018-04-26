<<<<<<< HEAD
'''
This algorithm will find all possible subsets of a given set and report their sum
These sums can then be checked against the sum inputed in the problem and return true/false based on that


'''


def Subset(array,start,end,sum,output):
	#The start index and the end index tell the recursive calls where to start and end on the
	#input array
	
	
	#Sum is the current sum in the recursive call
		if(start>end):
			#We have iterated through all permutations in this recursive call
			#add it to the output list
			output.append(sum)
			return
		
		
		#Call this method recursively including the starting element
		Subset(array,start+1,end,sum+array[start],output)
		#Call this method not including the starting element in the sum
		Subset(array,start+1,end,sum,output)


def checkOutput(output,value):
	for sum in output:
		if sum==value:
			return True
	return False


#this method will actually test the exhaustive search and combine the two methods above
array=[]
def subsetSum(array,k):
    output=[]
    Subset(array,0,len(array),k,output)
    return checkOutput(output,k)

def main():
	print(subsetSum([1,4,7,8,9,10], 19) )


if __name__ == "__main__":
	main()






	
=======
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
>>>>>>> 86435f79591b405abc52e9eb6483a7425e325180
