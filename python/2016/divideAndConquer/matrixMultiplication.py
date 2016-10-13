#! /usr/bin/python

def matrixMul(A, B):
	R = [[0 for x in range(len(A))] for y in range(len(B[0]))]
	# If the number of columsn of A is not equal to the rows of B, return
	if len(A[0]) != len(B) :	
		return
	for i in range(0, len(A)):
		for j in range(0, len(B[0])):
			R[i][j] = 0
 			for k in range(0, len(B)):
				R[i][j] += A[i][k]*B[k][j]
	return R


A = [[1,2], [3,4]]
A = [[1,2], [3,4]]
R = matrixMul(A, A)
print R
			
