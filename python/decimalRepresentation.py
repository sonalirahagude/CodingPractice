#! /usr/bin/python

#Write a function which, given two integers (a numerator and a denominator), prints the decimal representation of the rational number "numerator/denominator". 
#Since all rational numbers end with a repeating section, print the repeating section of digits inside parentheses

def decimalRep(num,den):
	before = num/den
	remainder = num%den
	 
	if(remainder == 0) :
		return str(before)
	
	remainderList = {}
	decimalPart = []
	i = 0;
	while (1) :
		if (remainder in remainderList):
			decimalPart.insert(remainderList[remainder], '(');	
			decimalPart.append(')');
			break
		remainderList[remainder] = i
		i = i + 1
		remainder = remainder*10
		decimalPart.append( str(remainder/den))
		remainder = remainder%den
	return str(before) + "." + ''.join(decimalPart)

print decimalRep(58,2828)
print decimalRep(8,16)
print decimalRep(22,7)
print decimalRep(5,9)
print decimalRep(15,5)
