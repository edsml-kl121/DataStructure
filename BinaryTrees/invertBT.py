class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(N)
# Space O(N) maximum 
def InvertBT(node):
    queue = [node]
    while len(queue) != 0:
      current = queue.pop(0)
      if current is None:
        continue
      swap(node)
      InvertBT(node.left)
      InvertBT(node.right)

# Time O(N)
# Space O(N) maximum 
def InvertBT_d(node):
    if node is None:
      return
    swap(node)
    InvertBT_d(node.left)
    InvertBT_d(node.right)

def swap(node):
    node.left, node.right = node.right, node.left

node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)
node8 = BinaryTree(8)
node9 = BinaryTree(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

print(node1.left.left.left.value)
InvertBT_d(node1)
# print(node1.value)
print(node1.right.right.right.value)