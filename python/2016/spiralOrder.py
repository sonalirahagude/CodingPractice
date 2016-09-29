#! /usr/bin/python
import sys
import numpy

def spiralOrder(A):
	result = []

	printCount = 0
	# get the total, compare it with the printCount, 
	# 	so that you know where to stop
	total = len(A)*len(A[0])
	# direction [right down left up]
	# direction = [0, 1, 2, 3]
	upOrLef = -1;
	downOrRight = 1;
	roundCount = len(A[0])-1;
	xstart = 0;
	ystart = 0;
	while(1) :
		for direction in range(4):
					
			#print xstart, ystart
			if(direction == 0) :				
				for j in xrange(roundCount):
					print A[xstart][ystart + j]
					printCount+=1
					if printCount == total:
						break
				ystart = ystart + roundCount
			if(direction == 1) :
				for i in xrange(roundCount):
					print A[xstart + i][ystart]
					printCount+=1
					if printCount == total:
						break
				xstart = xstart + roundCount
			if(direction == 2) :
				for j in xrange(roundCount):
					print A[xstart][ystart-j]
					printCount+=1
					if printCount == total:
						break
				ystart = ystart - roundCount
			if(direction == 3) :
				for i in xrange(roundCount):
					print A[xstart-i][ystart]
					printCount+=1
					if printCount == total:
						break
				xstart = xstart - roundCount + 1 #skip one level now
				ystart += 1
				if roundCount > 2:
					roundCount-=2
				else:
					roundCount-=1
			if printCount == total:
				break
		if printCount == total:
			break

	return result

A = [[1,2], [3,4]]
A = [[1,2,3], [4,5,6],[7,8,9]]
A = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralOrder(A)
