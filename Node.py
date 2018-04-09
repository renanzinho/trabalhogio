class Node:

	def __init__(self, data, nextNode=None, previousNode=None):
		self.__data  		= data
		self.__nextNode 	= nextNode
		self.__previousNode = previousNode
	
	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, new):
		self.__data = new

	@property
	def nextNode(self):
		return self.__nextNode

	@nextNode.setter
	def nextNode(self, new):
		self.__nextNode = new

	@property
	def previousNode(self):
		return self.__previousNode

	@previousNode.setter
	def previousNode(self, new):
		self.__previousNode = new
