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

class testNode(unittest.TestCase):
	#Setting up node for testing
	def setUp(self):
		self.node=g.node('a')
	
	#Checking if the node is named correctly
	def testNodeName(self):
		self.assertEqual(self.node.id, 'a')
	
	#Checking if the node neighbour is correct
	def testNodeNeighbour(self):
		self.assertEqual(self.node.neighbour, [])
	
	#Checking if node is able to add neighbour
	def testAddNeighbour(self):
		self.assertTrue(self.node.addNeighbour('a'))
		self.assertEqual(self.node.neighbour, ['a'])
		self.assertTrue(self.node.addNeighbour('b'))
		self.assertEqual(self.node.neighbour, ['a', 'b'])

	#Checking if node is able to add multiple neighbours
	def testAddMultipleNeighbour(self):
		names=list()
		for i in range(10):
			name=chr(ord('a')+i)
			names.append(name)
			self.assertTrue(self.node.addNeighbour(name))
		self.assertEqual(self.node.neighbour, names)
		
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
		self.assertEqual(self.graph.nodes, {'a':[]})
	
	#Testing creation of multiple nodes
	def testMultipleNodesCreation(self):
		for i in range(10):
			name=chr(ord('a')+i)
			self.assertTrue(self.graph.newNode(name))
		
	#Testing the creation of an edge
	def testEdgeCreation(self):
		#Creating an edge when the nodes do not exist
		self.assertFalse(self.graph.newEdge('a', 'b'))
		
		#Creating an edge when only one node exists
		self.assertTrue(self.graph.newNode('a'))
		self.assertFalse(self.graph.newEdge('a', 'b'))
		
		#Creating an edge when both nodes exist
		self.assertTrue(self.graph.newNode('b'))
		self.assertTrue(self.graph.newEdge('a', 'b'))
		
		#Ensuring that the edge reflects the nodes are connected
		self.assertEqual(self.nodes['a'], 'b')
		self.assertEqual(self.nodes['b'], 'a')
		
	def testEdgesCreation(self):
		#Creating 2 edges between 3 nodes that exist
		self.assertTrue(self.graph.newNode('a'))
		self.assertTrue(self.graph.newNode('b'))
		self.assertTrue(self.graph.newNode('c'))
		self.assertFalse(self.graph.newEdge('a', 'b'))
		self.assertFalse(self.graph.newEdge('b', 'c'))
		self.assertEqual(self.nodes['a'], 'b')
		self.assertEqual(self.nodes['b'], ['a', 'c'])
		self.assertEqual(self.nodes['c'], 'b')
				
	def testConnection(self):
		#Testing the connection when the nodes do not exist
		self.assertEqual(self.graph.connect('a', 'b'), False)
		
		#Testing the connection when only one node exists
		self.assertTrue(self.graph.newNode('a'))
		self.assertEqual(self.graph.connect('a', 'b'), False)
		
		#Testing the connection when both nodes exist, but not connected
		self.assertTrue(self.graph.newNode('a'))
		self.assertTrue(self.graph.newNode('b'))
		self.assertEqual(self.graph.connect('a', 'b'), False)
		
		#Testing the connection when both nodes exists and are connected
		self.assertTrue(self.graph.newNode('a'))
		self.assertTrue(self.graph.newNode('b'))
		self.assertFalse(self.graph.newEdge('a', 'b'))
		self.assertEqual(self.graph.connect('a', 'b'), True)

if __name__ == '__main__':
	unittest.main()