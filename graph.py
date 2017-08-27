'''
Author: Ludwig Hoon
Email: ldwgkshoon@gmail.com
'''

'''
Expected user input:
1. Number of nodes
2. Number of edges
3. Name/ID of nodes
4. Pairs of nodes that are connected
'''
'''
class node:
	def __init__(self, name):
		self.id=name
		self.neighbour=list()
		return None
		
	def addNeighbour(self, node):
		self.neighbour.append(node)
		return True
'''

class graph:
	def __init__(self):
		self.nodes=dict()
		self.numNodes=0
		return None
	
	def newNode(self, name):
		if not (name in self.nodes.keys()):
			self.numNodes+=1
			self.nodes[name]=list()
			return True
		else:
			print("Node already exists")
			return False
		
	def newEdge(self, nodeA, nodeB):
		if not (nodeA in self.nodes.keys() and nodeB in self.nodes.keys()):
			print("Nodes not here yet")
			return False
		else:
			if (nodeA in self.nodes[nodeB] or nodeB in self.nodes[nodeA]):
				print('Edge already exists')
				return False
			else:
				self.nodes[nodeA].append(nodeB)
				self.nodes[nodeB].append(nodeA)
				return True
	
	def connect(self, nodeA, nodeB):
		return False

def option():
	print('1. Input graph')
	print('2. Check connectivity')
	print('3. Quit')
	selection=input('Choice>> ')
	try:
		selection=int(selection)
		if (selection == 1) or (selection == 2) or (selection == 3):
			return selection
		else:
			raise Exception
	except:
		print('!!!Invalid choice!!!')
		option()

		
if __name__ == '__main__':
	G=graph()
	choice=option()	