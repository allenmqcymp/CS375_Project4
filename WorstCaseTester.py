'''
This program will test the worst case time complexity of all the algorithms in the project
'''
import random
import time


def WorstCaseTest():
    n=0
    a=[]
    while n<=100:
        #We will step up to an array size of n=100, by 10 each step
        i=0
        sum=0
        while i<=n:
            #we want to make an array of size n
            a.append(i)
            sum+=i
        #Then shuffle the list
        random.shuffle(a)
        #now generate a input integer that makes every case a worst case, let this be defined as k
        k=sum+10# We are simply adding 10 to the value of the sum in order to make sure the sum doesn't exist
        #Now we need to run all of the tests
        
        Startmillisec=int(round(time.time()*1000))
        