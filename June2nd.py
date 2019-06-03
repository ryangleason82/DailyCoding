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
