# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name, adjacent_nodes=[]):
        self.name = name
        self.adjacent_nodes = []
        self.visited = False

    def __repr__(self):
        return str(self.name)

# O(v + e) time - how many children node coming out 
# O(V) space
visited_arr = []
def dfs(node):
    # if node not in visited_arr:
    print(node)
    visited_arr.append(node.name)
    for children in node.adjacent_nodes:
        dfs(children)
    return visited_arr


if __name__ == "__main__":
    # node = Node('5')
    # node2 = Node("3")
    # node3 = Node("7")
    # node4 = Node("2")
    # node5 = Node("4")
    # node6 = Node("8")
  

    # node.adjacent_nodes = [node2, node3]
    # node2.adjacent_nodes = [node4, node5]
    # node3.adjacent_nodes = [node6]
    # node4.adjacent_nodes = []
    # node5.adjacent_nodes = [node6]
    # node6.adjacent_nodes = []
    node = Node('A')
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node9 = Node("I")
    node10 = Node("J")
    node11 = Node("K")
  

    node.adjacent_nodes = [node2, node3, node4]
    node2.adjacent_nodes = [node5, node6]
    node3.adjacent_nodes = []
    node4.adjacent_nodes = [node7, node8]
    node5.adjacent_nodes = []
    node6.adjacent_nodes = [node9, node10]
    node7.adjacent_nodes = [node11]
    node8.adjacent_nodes = []
    node9.adjacent_nodes = []
    node10.adjacent_nodes = []
    node11.adjacent_nodes = []
  
    print(node.name)
    print(dfs(node))
  