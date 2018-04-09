from Node import Node
from LinkedList import DoubleLinkedList

n1 = Node(20)
a = DoubleLinkedList()
a.add(20)
a.add(10)
a.addAt(100,1)

print(a.search(20).data)