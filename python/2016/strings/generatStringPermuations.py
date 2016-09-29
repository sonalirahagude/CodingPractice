#! /usr/bin/python
import sys
import numpy



def generatePermutations(s):
	if len(s) == 1:
		arr = [s]
		return arr;
	arr = generatePermutations(s[0:len(s)-1])
	new_arr = appendInEveryPosition(arr,s[len(s)-1])	
	return new_arr

def appendInEveryPosition(arr,c):
	newarr = [];
	str_len = len(arr[0]);
	
	for i in range(0, len(arr)):
		newarr.append(c + arr[i])
		for j in range (1, str_len+1):
			newarr.append(arr[i][0:j] + c + arr[i][j:str_len])
	return newarr;



s = "abcd";
arr = generatePermutations(s)
print arr
