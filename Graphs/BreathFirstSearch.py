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

visited_arr = []

# O(v + e) time - all the nodes and iterate the children note with a for loop as well
# O(v) space - store the 11 nodes
def bfs(node):
    # Write your code here.
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        visited_arr.append(current.name)
        for child in current.adjacent_nodes:
            queue.append(child)
    return visited_arr


if __name__ == "__main__":
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
  
    print(bfs(node))
  