#! /usr/bin/python

def selectionSort(A):
	for i in range(len(A)-1):
		smallest = A[i];
		smallestIndex = i;
		for j in range(i+1,len(A)):
			if A[j] < smallest :
				smallest = A[j]
				smallestIndex = j		
		swap(A,smallestIndex,i)


def swap (A, i ,j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp


A = [4,3,8,7,9,5,6,2,1]
selectionSort(A)
print A
