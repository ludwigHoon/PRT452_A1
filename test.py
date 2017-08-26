'''
Author: Ludwig Hoon
Email: ldwgkshoon@gmail.com
'''

import unittest
import graph as g

'''
This graph program will have the following implementations:
1. The graph is undirected
2. The graph is represented in python dictionary 
'''

class testGraph(unittest.TestCase):
	#Setting up
	def setUp(self):
		self.graph=g.graph()
	
	#Testing the creation of a graph
	def testGraphCreation(self):
		self.assertTrue(self.graph)
	
	#Testing the creation of a node
	def testNodeCreation(self):
		self.assertTrue(self.graph.newNode('a'))
	
	#Testing the creation of multiple node
	def testNodesCreation(self):
		for i in range(10):
			self.assertTrue(self.graph.newNode(i))
	
	
	#Testing the creation of an edge
	
	
	

if __name__== '__main__':
	unittest.main()
	testGraph.graphCreation()
	