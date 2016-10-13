#! /usr/bin/python

class Solution:

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        B = [ele for ele in A]
        for i in range(1,len(B)):
            key = B[i]
            j = i - 1
            #while j >= 0 and iDigit > getFirstDigit(A[j]):
            arrI = self.getDigitArray(key)
            arrJ = self.getDigitArray(B[j])

            while j >= 0 and self.isLarger(arrI,arrJ):

                B[j+1] = B[j]
                j -= 1
		if j >= 0:
                    arrJ = self.getDigitArray(B[j])
                    arrI = self.getDigitArray(key)
            B[j+1] = key
            #print B
        s = ''
	if len(B) > 0 and B[0] == 0:
		return '0'
        for i in range(len(B)):
            s += str(B[i])
        return s

    def isLarger(self,arrA,arrB):
	aa = ''.join(map(str,arrA))
	bb =  ''.join(map(str,arrB))

	aabb = int(aa + bb)
	bbaa = int(bb + aa)
	if(aabb > bbaa):
	    return True
	else:
	    return False
		
    def getDigitArray(self,a):
	if a == 0:
	    return [0]
        arr = []
        while a > 0 :
            digit = a%10
            a = a/10
            arr.insert(0,digit)
        return arr
    
import unittest
class SolutionTester(unittest.TestCase):

    def test1(self):
	s = Solution()
        A = [4,3,78,32]
        self.assertEquals('784332',s.largestNumber(A))

    def test2(self):
	s = Solution()
        A = [8, 89]
        self.assertEquals('898',s.largestNumber(A))

    def test3(self):
	s = Solution()
        A = [0,0,0,0,0]
        self.assertEquals('0',s.largestNumber(A))

    def test4(self):
	s = Solution()
        A = [ 9, 99, 999, 9999, 9998 ]
        self.assertEquals('99999999999998',s.largestNumber(A))

    def test5(self):
	s = Solution()
        A = [ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]
        self.assertEquals('9648527226766636354854724412368319',s.largestNumber(A))


    def test6(self):
	s = Solution()
        A = [ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]
        self.assertEquals('99197494093090589587787286882579979879178278077273570968668667867566465335024704093953663633573372982927126124019124113',s.largestNumber(A))


s = Solution()

#st = s.largestNumber(A)
#print st
#print myval

unittest.main()



