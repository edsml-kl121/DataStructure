class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def sum_linked_list(linkedList1, linkedList2):
    new_linked_list = Node(0)
    current_linkedlist = new_linked_list
    counter = 0
    currentlist1 = linkedList1
    currentlist2 = linkedList2
    while currentlist1 is not None or currentlist2 is not None or counter != 0:

        first_value = currentlist1.value if currentlist1 is not None else 0
        second_value = currentlist2.value if currentlist2 is not None else 0
        sum = first_value + second_value + counter
        current_value = sum % 10

        newnode = Node(current_value)
        current_linkedlist.next = newnode
        current_linkedlist = current_linkedlist.next
        counter = sum // 10
        currentlist1 = currentlist1.next if currentlist1 is not None else None
        currentlist2 = currentlist2.next if currentlist2 is not None else None
    return new_linked_list.next


node1_1 = Node(2)
node1_2 = Node(4)
node1_3 = Node(7)
node1_4 = Node(1)

node1_1.next = node1_2
node1_2.next = node1_3
node1_3.next = node1_4

node2_1 = Node(9)
node2_2 = Node(4)
node2_3 = Node(5)
node2_1.next = node2_2
node2_2.next = node2_3

new_list = sum_linked_list(node1_1, node2_1)

print(new_list.value)
print(new_list.next.value)
print(new_list.next.next.value)
print(new_list.next.next.next.value)