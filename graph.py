'''
Author: Ludwig Hoon
Email: ldwgkshoon@gmail.com
'''
class node:
	def __init__(self, name):
		self.id=name
		self.neighbour=list()
		return None
		
	def addNeighbour(self, node):
		self.neighbour.append(node)
		return True

class graph:
	def __init__(self):
		self.nodes=dict()
		self.numNodes=0
		return None
	
	def newNode(self, name):
		newNode=node(name)
		self.numNodes+=1
		self.nodes[newNode.id]=list()
		return True
		
	def newEdge(self, nodeA, nodeB):
		return True

	
	