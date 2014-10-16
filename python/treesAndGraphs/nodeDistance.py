#! /usr/bin/python
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
 	self.parent = None

def connodeListuctTree(root):
	root = Tree()
	node = root
	root.data = 4
	for i in range(3,-1,-1):
		node.left = Tree()
		node.left.parent=node
		node.left.data = i
		#print node.left.data
		node = node.left
	node  = root
	for i in range (5,9):
		node.right = Tree()
		node.right.parent=node
		node.right.data = i
		node = node.right

#	print root.data;
#	print root.left.data;
#	print root.left.left.data;
#	print root.left.left.left.data;
#	print root.left.left.left.left.data;
#	print root.right.data;
#	print root.right.right.data;
#	print root.right.right.right.data;
	#print root.left.right.data;
	return root
	
	
def findDistance(root, nodeData, pos):
	#calculate the height of nodes needed
	#first find the node,
	node = root
	nodeHeight = 0
	while(node != None):
		if(node.data == nodeData):
			break
		elif (node.data > nodeData): #go left
			node = node.left
			nodeHeight = nodeHeight + 1
		else: 			    #go right
			node = node.right
			nodeHeight = nodeHeight + 1

	if(node == None):
		return "node not found"
	
	print node.data
	print nodeHeight
	upperLevel = nodeHeight - pos
	lowerLevel = nodeHeight + pos
	nodeList = ""
	if(upperLevel >= 0 ):
		nodeList = findNodesAtLevel(upperLevel, root)
	nodeList= nodeList + " " + findNodesAtLevel(lowerLevel, root)
	return nodeList;	

def findNodesAtLevel(level, root):
	#do an inorder traversal
	print "level: " + str(level)  
	if (root == None):
		return ""
	print "data: " + str(root.data)
	if(level ==0) :
		return str(root.data)
	print root.left.data
	print root.right.data
	nodeList = " " +  findNodesAtLevel(level-1,root.left)
	nodeList = nodeList + " " +  findNodesAtLevel(level-1,root.right)
	return nodeList
	

root = None
root = connodeListuctTree(root)
nodeList = findDistance(root, 4, 1)	
print nodeList
