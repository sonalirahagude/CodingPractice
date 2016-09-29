#! /usr/bin/python

import sys
import numpy

def insertionSort(A):
	for i in xrange(len(A)-1-1,-1,-1):
		key = A[i]
		j = i + 1
		while j<len(A) and A[j] < key:
			A[j-1] = A[j]
			j += 1
		A[j-1] = key

A = [4,3,5,2,1]
insertionSort(A)
print A
