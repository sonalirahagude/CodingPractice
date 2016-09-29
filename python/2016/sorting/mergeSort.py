#! /usr/bin/python

def mergeSort(A,i,j):
	if j <= i:
		return
	mid = (i + j)/2
	mergeSort(A,i,mid)
	mergeSort(A,mid+1,j)
	merge(A,i,mid,j);


def merge(A, i, m, j):
	L = [0]*(m-i + 1)
	R = [0]*(j-(m+1) + 1)
	st = 0
	while (st < m -i+1):
		L[st] =  A[i+st]
		st += 1

	st = 0
	while ( st < j -m):
		R[st] = A[m+1+st]
		st += 1
#	print "i:" + str(i)
#	print "m:" + str(m) 
#	print "j:" + str(j)
#	print "L:" + str(L)
#	print "R:" + str(R)
#	print "--------------"
	x = 0
	y = 0
	st = i
	while x < len(L) and y < len(R):
		if L[x] < R[y]:
			A[st] = L[x]
			x +=1
		else:
			A[st]=R[y]
			y +=1
		st+=1
	while x < len(L):
		A[st] = L[x]
		x +=1
		st+=1
	while y < len(R):
		A[st]=R[y]
		y +=1
		st+=1


A = [4,3,5,6,2,1]
mergeSort(A,0,len(A)-1)
print A
