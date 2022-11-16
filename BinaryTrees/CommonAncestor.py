class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

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

print(findCommonAncestor(root, 4, 6))