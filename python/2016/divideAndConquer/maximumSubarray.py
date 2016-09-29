#! /usr/bin/python

def maxSubArr(A):
	maxSum = 0
	maxStart = 0
	maxEnd = 0

	curSum = 0
	curSt = 0
	for curPos in range(len(A)):
		if (curSum + A[curPos] >= curSum):
			curSum = curSum + A[curPos] 
		else:
			#Check if the curSum before was greater than maxSum, if yes, reset maxSum and pointers
			if curSum > maxSum:
				maxSum = curSum
				maxStart = curSt
				maxEnd = curPos - 1
			#Reset curSum and skip this position as it clearly negative
			curSt = curPos + 1
			curSum = 0

	if curSum > maxSum:
		maxSum = curSum
		maxStart = curSt
		maxEnd = curPos
	
	print maxStart, maxEnd, maxSum


A = [-4,4,5,-3,2,1,8,0,4,-1]
maxSubArr(A)	
