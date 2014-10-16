#! /usr/bin/python
import sys
import numpy

steps = 5
C = [0]*steps; 
# base cases
C[0] = 1;
C[1] = 2;
C[2] = 4;
for i in range(3,steps):
	C[i] = C[i-1] + C[i-2] + C[i-3]
print C
