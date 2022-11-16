class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(t, s):
    current_sum = 0
    hasPath = [False]
    answer = traverse_helper(t, current_sum, s, hasPath)
    print("ss",answer, hasPath)
    return hasPath[-1]


def traverse_helper(tree, running_sum, s, hasPath):
    if tree is None:
      return
    print(tree.value)
    print("outside", hasPath)
    if running_sum == s:
        hasPath.append(True)
        print('hoi', hasPath)
        return hasPath
    traverse_helper(tree.left, running_sum + tree.value, s, hasPath)
    traverse_helper(tree.right, running_sum + tree.value, s, hasPath)


node1 = BinaryTree(4)
node2 = BinaryTree(1)
node3 = BinaryTree(3)
node4 = BinaryTree(-2)
node5 = BinaryTree(1)
node6 = BinaryTree(2)
node7 = BinaryTree(3)
node8 = BinaryTree(-2)
node9 = BinaryTree(-3)

# node2.right = node5
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node7
node3.left = node5
node3.right = node6
node6.left = node8
node6.right = node9
# node4.right = node9

print(solution(node1, 7))