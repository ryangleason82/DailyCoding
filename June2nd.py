# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.


class Node:
    arr = []

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, Node):
        return self.inOrderTraversal(Node)

    def inOrderTraversal(self, node):
        if(node != None):
            self.inOrderTraversal(node.left)
            self.arr.append(node.val)
            self.inOrderTraversal(node.right)

    def deserialize(self, arr):
        root = 1
        i = 1
        n = 1
        self.insertLevelOrder(arr, root, i, n)
        return True

    def insertLevelOrder(self, arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = self.insertLevelOrder(arr, root.left, 2*i+1, n)
            root.right = self.insertLevelOrder(arr, root.right, 2*i+2, n)
        return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(node.serialize(node))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

# Solution

def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

# We can approach this problem by first figuring out what we would like the serialized tree to look like. Ideally, it would contain the minimum information required to encode all the necessary information about the binary tree. One possible encoding might be to borrow S-expressions from Lisp. The tree Node(1, Node(2), Node(3)) would then look like '(1 (2 () ()) (3 () ()))', where the empty brackets denote nulls.

# To minimize data over the hypothetical wire, we could go a step further and prune out some unnecessary brackets. We could also replace the 2-character '()' with '#'. We can then infer leaf nodes by their form 'val # #' and thus get the structure of the tree that way. Then our tree would look like 1 2 # # 3 # #.