#! /usr/bin/python
import sys
import numpy

X=3;
Y=3;
W = numpy.zeros((X,Y))

# base cases
W[0][0]=1

#marked points
mX = 1
mY = 2 
W[mX][mY] = 0

for i in range(X):
	for j in range(Y):
		#skip marked points
		if(i == mX and j == mY):
			continue
		#skip base case
		elif(i-1 < 0 and j-1 < 0):
			continue
		elif(i-1 < 0):
			W[i][j] = W[i][j-1]
		elif(j-1 < 0 ):
			W[i][j] = W[i-1][j]
		else:
			W[i][j] = W[i-1][j] + W[i][j-1]	

print W
