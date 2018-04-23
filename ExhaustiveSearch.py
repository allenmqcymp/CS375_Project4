'''
This algorithm will find all possible subsets of a given set and report their sum
These sums can then be checked against the sum inputed in the problem and return true/false based on that


'''
output=[]

def Subset(array,start,end,sum,output):
	#The start index and the end index tell the recursive calls where to start and end on the
	#input array
	
	
	#Sum is the current sum in the recursive call
		if(start>end):
			#We have iterated through all permutations in this recursive call
			#add it to the output list
			output.append(sum)
			return;
		
		
		#Call this method recursively including the starting element
		Subset(array,start+1,end,sum+=array[start])
		
		#Call this method not including the starting element in the sum
		Subset(array,start+1,end,sum)


def checkOutput(output,value):
	for sum in output:
		if sum==value:
			return true
	return false
	