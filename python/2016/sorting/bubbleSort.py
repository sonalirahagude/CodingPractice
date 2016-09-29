#! /usr/bin/python

def bubbleSort(A):
	for i in range(len(A)-1,0,-1):
		j = 0
		while (j < i):
			if(A[j] > A[j+1]):
				swap(A,j,j+1)
			j+=1

def swap(A,i,j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp


A = [4,6,9,8,7,3,5,2,1]
bubbleSort(A)
print A
			
