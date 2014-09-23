#! /usr/bin/python
length = 4 
price = [0, 1, 5,8, 9]
revenue = [0 for i in range(length+1)]
for i in range(length +1):
	revenue[i] = 0
	for j in range (1,i +1):
		if revenue[i] < revenue[i - j] + price[j]:
			revenue[i] = revenue[i - j] + price[j];
print revenue[length];
