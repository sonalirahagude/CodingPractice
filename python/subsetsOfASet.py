#! /usr/bin/python
 
set = [1,2,3]

def subsets (array, index):
	listOfLists = []
	if (index == len(array)):
		# add an empty set, this is a base case
		lists = []
		listOfLists.append(lists)
	else:
		listOfLists = subsets(array,index+1)
		newList= []
		currentLists = []
		for lists in listOfLists:
			#newList = lists[:]
			newList = list(lists)
			newList.append(array[index])
			currentLists.append(newList)
		listOfLists.extend(currentLists)
	return listOfLists


finalLists = subsets(set, 0)
for lists in finalLists:
	print lists
	print "*"*25
