class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(t):
    return symmetryCheck(t, t)

def symmetryCheck(tree1, tree2):
    if tree1 is None and tree2 is None:
      return True
    if tree1 and tree2:
      if tree1.value == tree2.value:
        return symmetryCheck(tree1.left, tree2.right) and symmetryCheck(tree1.right, tree2.left)
    return False


node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(2)
node4 = BinaryTree(3)
node5 = BinaryTree(4)
node6 = BinaryTree(4)
node7 = BinaryTree(3)

# node2.right = node5
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
# node4.right = node9

print(solution(node1))