class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

def remove_dup(linkedlist):
    currentLinkedList = linkedlist
    while currentLinkedList is not None:
        nextDistinctNode = currentLinkedList.next
        while nextDistinctNode is not None and currentLinkedList.value == nextDistinctNode.value:
            nextDistinctNode = nextDistinctNode.next
        # print(currentLinkedList.value, nextDistinctNode.value)
        currentLinkedList.next = nextDistinctNode
        currentLinkedList = nextDistinctNode
    return linkedlist
    
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


# print(node1)
# print(node1.next)
# print(node1.next.next)
# print(node1.next.next.next)
# print(node1.next.next.next.next)

remove_dup(node1)

print(node1)
print(node1.next)
print(node1.next.next)
print(node1.next.next.next)
