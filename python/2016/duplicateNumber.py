#! /usr/bin/python

def duplicateNumber(A):
	diff = 0
	for i in range(len(A)):
		diff += (i+1) - A[i]
	return diff


import unittest
class SolutionTester(unittest.TestCase):
	def test1(self):
		A = [1,2,3,3,5]
		self.assertEquals(duplicateNumber(A),4)


unittest.main()
