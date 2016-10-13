#! /usr/bin/python

def AddOne(A):
	i = len(A) - 1
	sum = A[i] + 1
	A[i] = sum%10
	carry = sum/10
	 
	while carry > 0 and i > 0 :
		i -= 1
		sum = A[i] + carry
		A[i] = sum%10
		carry = sum/10
	if carry > 0:
		A.insert(i,carry)
	print A
	print i
	k = 0
	for k in range(0,i+1):
		if(A[k] != 0):
			break
	print k
	for j in range(0,k):
		A.pop(0)
	return A


A = [0,0,9,9,9]
#A = [0,1,2,3]
#A = [ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]
#A = [ 0, 6, 0, 6, 4, 8, 8, 1 ]
#A = [ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ]
#A = [ 0, 0 ,4]
AddOne(A)
print A
