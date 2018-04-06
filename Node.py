class Node:

	def __init__(self, data, other=None, index=0):
		self.__data  	= data
		self.__nextNode = nextNode
		self.__index 	= index
	
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
	def index(self):
		return self.__index

	@index.setter
	def index(self, new):
		self.__index = new

	