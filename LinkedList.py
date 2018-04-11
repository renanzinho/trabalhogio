from Node import Node

class DoubleLinkedList:

	def __init__(self, head=None):
		self.__head  = head
		if head is None:
			self.__count = 0
		else:
			self.__count = 1

	@property
	def head(self):
		return self.__head

	def __len__(self):
		return self.__count

	def add(self, newNode):
		newNode = Node(newNode)

		if self.__head is None:
			self.__head = newNode
			self.__count += 1
		else:
			tempNode = self.__head
			newNode.nextNode = self.__head
			self.__head.previousNode = newNode
			self.__head = newNode
			self.__count += 1

	def addAt(self, newNode, index):
		newNode = Node(newNode)

		if index > self.__count or index < 0:
			print('Index out of range')
			return False

		elif index == 0:
			self.add(self, newNode)
			self.__count += 1
			return True

		else:
			tempNode = self.__head
			i = 0
			while i < index - 1:
				tempNode = tempNode.nextNode
				i += 1

			if index == self.__count:
				tempNode.nextNode = newNode
				newNode.previousNode = tempNode
			else:
				newNode.nextNode = tempNode.nextNode
				tempNode.nextNode.previousNode = newNode
				tempNode.nextNode = newNode
				newNode.previousNode = tempNode
			
			self.__count += 1
			return True

	def remove(self, item):
		tempNode = self.__head
		i = 0
			
		while tempNode.data != item and i < self.__count:
			tempNode = tempNode.nextNode
			i += 1

		if i == 0:
			self.__head = self.__head.nextNode
			self.__count -= 1
			return tempNode.data
		elif i == self.__count - 1:
			tempNode.previousNode.nextNode = None
			self.__count -= 1
			return tempNode.data
		elif i < self.__count - 1:
			tempNode.previousNode.nextNode = tempNode.nextNode
			tempNode.nextNode.previousNode = tempNode.previousNode
			self.__count -= 1
			return tempNode.data
		else:
			print('Item not found')
			return False

	def removeAt(self, index):
		tempNode = self.__head
		i = 0

		if i < 0 or i >= self.__count:
			print('Index out of range')
			return False
		else:
			while i < index:
				tempNode = tempNode.nextNode
				i += 1
			if i == 0:
				self.__head = self.__head.nextNode
				self.__count -= 1
				return tempNode.data
			elif i == self.__count - 1:
				tempNode.previousNode.nextNode = None
				self.__count -= 1
				return tempNode.data
			else:
				tempNode.previousNode.nextNode = tempNode.nextNode
				tempNode.nextNode.previousNode = tempNode.previousNode
				self.__count -= 1
				return tempNode.data

	def search(self, item):
		i = 0
		tempNode = self.__head

		while i < self.__count and tempNode.data != item:
			tempNode = tempNode.nextNode
		return tempNode

	def searchId(self, item);
		i = 0
		tempNode = self.__head

		while i < self.__count and tempNode.data.idCandidato != item:
			tempNode = tempNode.nextNode
		return tempNode

	def __str__(self):
		tempNode = self.__head
		i = 0
		string = ''
		while i < self.__count:
			string += str(tempNode.data) + ', '
			tempNode = tempNode.nextNode 
			i += 1
		return string[:-2]

	def __repr__(self):
		return str(self)



