#! /usr/bin/python

import sys
import numpy

def insertionSort(A):
	for i in range(1,len(A)):
		key = A[i]
		j = i-1
		while j >= 0  and key < A[j]:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = key

A = [4,3,2,1]
insertionSort(A)
print A
