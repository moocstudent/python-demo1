from graphviz import Digraph


class Node:
    def __init__(self, key,color="red", left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, other):
        if (self is None and other is not None) or (self is not None and other is None):
            return False
        return (self.key == other.key) and (self.color == other.color) and (self.parent == other.parent)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.key < other.key)

    def __gt__(self, other):
        return (self.key > other.key)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, "black")
        self.root = self.nil

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.nil
        node.right = self.nil
        node.color = "red"
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = "black"
            return
        if node.parent.parent == None:
            return
        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "black"
    # RedBlackTree deletion and fix_delete methods omitted for brevity


def draw_tree(tree, filename='tree'):
    def add_edges(graph, node):
        if node != tree.nil:
            if node.left != tree.nil:
                graph.edge(str(node.key), str(node.left.key), color=node.left.color)
                add_edges(graph, node.left)
            if node.right != tree.nil:
                graph.edge(str(node.key), str(node.right.key), color=node.right.color)
                add_edges(graph, node.right)

    dot = Digraph(comment='Red-Black Tree')
    add_edges(dot, tree.root)
    dot.render(filename, view=True)


tree = RedBlackTree()
tree.insert(Node(1))
tree.insert(Node(2))
tree.insert(Node(3))
draw_tree(tree, 'tree')
