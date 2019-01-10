#! /usr/bin/python

# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(tree, arr):
    if tree == None:
        return

    arr.append(tree.val)

    if tree.left == None and tree.right == None:
        arr.append("None")
        return

    traverse(tree.left, arr)
    traverse(tree.right, arr)

    return arr
        
        
def serialize(tree):
    arr = []
    arr = traverse(tree, arr)
    print(arr)

def deserialize(tree):
    return

if __name__ == "__main__":
    tree = Node('root', Node('left', Node('left.left')), Node('right'))
    serialize(tree)
