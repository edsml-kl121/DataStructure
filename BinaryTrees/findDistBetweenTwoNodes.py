class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def FindDistanceBetweenTwoNodes(node, p, q):
  CommonAncestorVal = findCommonAncestor(node, p, q)
  paths = []
  depthHelper(node, p, paths)
  depthHelper(node, q, paths)
  depthHelper(node, CommonAncestorVal, paths)
  return paths[0] + paths[1] - 2 * paths[2]

def depthHelper(node, value, paths, depth=0):
  if node is None:
    return
  
  if node.val == value:
    paths.append(depth)

  depthHelper(node.left, value, paths, depth + 1)
  depthHelper(node.right, value, paths, depth + 1)



def findCommonAncestor(root, p, q):
  ans = []
  RecursiveHelper(root, p, q, ans)
  return ans[0]
    
def RecursiveHelper(currNode, p, q, ans):
  if currNode is None:
    return False
  
  left = RecursiveHelper(currNode.left, p, q, ans)
  right = RecursiveHelper(currNode.right, p, q, ans)

  mid = currNode.val == p or currNode.val == q

  if (left + right + mid) >= 2:
    ans.append(currNode.val)
  return left or right or mid


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(FindDistanceBetweenTwoNodes(root, 1, 8))