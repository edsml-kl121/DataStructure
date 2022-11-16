# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def solution2(l, k):
  newNode = l
  while newNode:
    if newNode.next and newNode.next.value == k:
      newNode.next = newNode.next.next
    else:
      newNode = newNode.next
  
  if l and l.value == k:
    return l.next
  else:
    return l


def solution(l, k):
    if l is None:
      return []
    currentNode = l
    lastDup = False
    while True:
        # printLinkedList1(l)
        if currentNode.value == k and currentNode.next is not None:
            currentNode.value = currentNode.next.value
            currentNode.next = currentNode.next.next
        # printLinkedList1(l)
        print(currentNode.value, currentNode.next)
        if currentNode.value == k and currentNode.next is None:
            currentNode.value = "last"
            lastDup = True
        print("lala")
        # printLinkedList1(l)
        if currentNode.next == None:
            print("break", currentNode.value, k)
            break
        if currentNode.value != k:
          currentNode = currentNode.next
    if lastDup:
        # printLinkedList1(l)
        nothing = remLast(l)
        if nothing == []:
            return []
        # printLinkedList1(l)
    return l

def remLast(l):
    if l.value == "last" or l is None:
        return []
    currentNode = l
    while True:
        if currentNode.next.value == "last":
            currentNode.next = None
            break
        currentNode = currentNode.next
    print(l.value)
    return l

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
    
# node1 = Node(1)
# node2 = Node(1)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(4)
# node6 = Node(4)
# node7 = Node(5)
# node8 = Node(6)
# node9 = Node(6)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7
# node7.next = node8
# node8.next = node9

node1 = Node(7)
node2 = Node(7)
node1.next = node2
node3 = Node(5)
node2.next = node3
node4 = Node(2)
node3.next = node4

printLinkedList1(node1)
sol = solution2(node1, 7)
print("the sol", sol)
printLinkedList1(sol)
# print(sol == node1)