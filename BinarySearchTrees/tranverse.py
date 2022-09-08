def inOrderTraverse(node, node_vals = []):
    if node is not None:
        inOrderTraverse(node.left, node_vals)
        node_vals.append(node.value)
        inOrderTraverse(node.right, node_vals)
        return node_vals

def preOrderTraverse(node, node_vals = []):
    if node is not None:
        node_vals.append(node.value)
        preOrderTraverse(node.left, node_vals)
        preOrderTraverse(node.right, node_vals)
        return node_vals

def postOrderTraverse(node, node_vals = []):
    if node is not None:
        postOrderTraverse(node.left, node_vals)
        postOrderTraverse(node.right, node_vals)
        node_vals.append(node.value)
        return node_vals


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node1 = BinaryTree(1)
node2 = BinaryTree(2)
node5_1 = BinaryTree(5)
node5_2 = BinaryTree(5)
node10 = BinaryTree(10)
node15 = BinaryTree(15)
node22 = BinaryTree(22)

node10.left = node5_1
node10.right = node15
node5_1.left = node2
node5_1.right = node5_2
node2.left = node1
node10.right = node15
node15.right = node22

print(inOrderTraverse(node10))
print(preOrderTraverse(node10))
print(postOrderTraverse(node10))
