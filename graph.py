'''
Author: Ludwig Hoon
Email: ldwgkshoon@gmail.com
'''

'''
Expected user input:
1. Nodes' ID/name
2. Nodes' ID/name that are connected
'''

class graph:
	def __init__(self):
		self.nodes=dict()
		return None
	
	def newNode(self, name):
		if not (name in self.nodes.keys()):
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
		if (nodeA in self.nodes.keys() and nodeB in self.nodes.keys()):
			if (nodeA in self.nodes[nodeB] and nodeB in self.nodes[nodeA]):
				return True
			else:
				return False
		else:
			print('Nodes not in graph')
			return False


def option():
	print('1. New node')
	print('2. New edge')
	print('3. Check connectivity')
	print('4. Reset')
	print('5. Quit')
	selection=input('Choice>> ')
	try:
		selection=int(selection)
		if selection >=1 and selection <=5:
			return selection
		else:
			raise Exception
	except:
		print('!!!Invalid choice!!!')
		option()

		
if __name__ == '__main__':
	G=graph()
	while True:
		choice=option()	
		if choice==1:
			print('\nCreating new node')
			name=input('Enter node name/ID: ')
			if(G.newNode(name)):
				print('Succeed')
			else:
				print('Failed')
			
		if choice==2:
			print('\nCreate new edge')
			nodeA=input('Enter 1st node: ')
			nodeB=input('Enter 2nd node: ')
			if(G.newEdge(nodeA, nodeB)):
				print('Succeed')
			else:
				print('Failed')
			
		if choice==3:
			print('\nChecking connectivity')
			nodeA=input('Enter 1st node: ')
			nodeB=input('Enter 2nd node: ')
			if(G.connect(nodeA, nodeB)):
				print('Connected')
			else:
				print('Not connected')
			
		if choice==4:
			G=graph()
			print('Reset')
		
		if choice ==5:
			break
		
		print('\n\n\n')
		
	print('End')	