# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printall(self):
      currentNode = self.head
      while currentNode.tail is not None:
          print(currentNode)
          currentNode = currentNode.tail

    def setHead(self, node):
        # Write your code here.
        self.tail = self.head
        self.head = node
        return

    def setTail(self, node):
        # Write your code here.
        currentNode = self.head
        while currentNode.tail is not None:
            currentNode = currentNode.tail
        currentNode.tail = node
        return

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        return

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        return

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        return

    def removeNodesWithValue(self, value):
        # Write your code here.
        return

    def remove(self, node):
        # Write your code here.
        return

    def containsNodeWithValue(self, value):
        # Write your code here.
        return


node1_1 = Node(1)
node1_2 = Node(2)
node1_3 = Node(3)
node1_4 = Node(4)
node1_5 = Node(5)

node1_1.next = node1_2
node1_2.next = node1_3
node1_3.next = node1_4
node1_4.next = node1_5


start = DoublyLinkedList().head = node1_1
start.tail = node1_2

printall(start)