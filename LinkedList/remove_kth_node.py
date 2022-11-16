# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    dummy = head
    counter = 0
    while dummy is not None:
        counter += 1
        dummy = dummy.next
    if counter == k:
        # Remove the K-th node
        head.value = head.next.value
        head.next = head.next.next
    else:
        print(counter - k - 1)
        for i in range(counter - k - 1):
            head = head.next
        head.next = head.next.next 
    pass

# Traversing a linkedlist
def printLinkedList1(node):
  arr = []
  while True:
    arr.append(node.value)
    # print(node.value)
    if node.next is None:
      break
    node = node.next
  print(arr)

def printLinkedList2(node):
  arr = []
  while node is not None:
    arr.append(node.value)
    # print(node.value)
    node = node.next
  print(arr)
    
node1 = Node(1)
node2 = Node(1)
node3 = Node(3)
node4 = Node(4)
node5 = Node(4)
node6 = Node(4)
node7 = Node(5)
node8 = Node(6)
node9 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9


printLinkedList1(node1)
# printLinkedList2(node1)
removeKthNodeFromEnd(node1,1)
printLinkedList1(node1)
# removeKthNodeFromEnd(node1,1)

# print(node1)
# print(node1.next)
# print(node1.next.next)
# print(node1.next.next.next)
