#! /usr/bin/python
import sys
import numpy

length = 6
rows = [30, 35, 15, 5, 10, 20]
columns = [35, 15, 5,10, 20, 25] 
cost = numpy.zeros((6,6))
index = numpy.zeros((6,6))
start=0
end=0
diagonals=length
for i in range(length):
	for count in range (diagonals):
		i = start + count;
		j = end + count;
		# break out of the loop if i and j are the same. this is our base case.
		if(i == j):
			break
		cost[i][j] = sys.maxint
		for k in range(i,j):
			q = cost[i][k] + cost[k+1][j] + rows[i]*columns[j]*columns[k]
			if(q < cost[i][j]):
				cost[i][j] = q
				index[i][j] = k
	
	end = end + 1;
	diagonals = diagonals - 1;
print cost
print index
