# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithmic Thinking With Python
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.

"""Binary Tree Class and its methods"""
# | 135  | 6.6 Binary Tree Traversals | src\chapter06trees\BinaryTree.py |


class BinaryTree:
    def __init__(self, data):
        self.data = data  # root node
        self.left = None  # left child
        self.right = None  # right child

    # set data
    def set_data(self, data):
        self.data = data

    # get data
    def get_data(self):
        return self.data

    # get left child of a node
    def getLeft(self):
        return self.left

    # get right child of a node
    def getRight(self):
        return self.right

    # get left child of a node
    def setLeft(self, left):
        self.left = left

    # get right child of a node
    def setRight(self, right):
        self.right = right

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp


# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root, result):
    if not root:
        return

    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)


# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root, result):
    if not root:
        return

    inorderRecursive(root.left, result)
    result.append(root.data)
    inorderRecursive(root.right, result)


# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return

    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)


# Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order
def preorderIterative(root, result):
    if not root:
        return

    stack = []
    stack.append(root)
    # print("stack - ", root.data, print_stack(stack))
    while stack:
        node = stack.pop()
        # print("pop - ", node.data, print_stack(stack))
        result.append(node.data)
        if node.right:
            # print("push right - ", node.right.data, print_stack(stack))
            stack.append(node.right)
        if node.left:
            # print("push left - ", node.left.data, print_stack(stack))
            stack.append(node.left)


# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root, result):
    if not root:
        return

    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            # print("push - ", node.data, print_stack(stack))
            node = node.left
        else:
            node = stack.pop()
            print("pop - ", node.data, print_stack(stack))
            result.append(node.data)
            node = node.right


# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None


import queue


def levelOrder(root, result):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)
    n = None

    while not q.empty():
        n = q.get()  # dequeue FIFO
        print("get - ", n.data)
        result.append(n.data)
        if n.left is not None:
            q.put(n.left)
            print("put - ", n.left.data)

        if n.right is not None:
            q.put(n.right)
            print("put - ", n.right.data)


def print_stack(stack):
    return list(node.data for node in stack)


# root = BinaryTree(11)
# print((root.get_data()))

# root.insertLeft(1)
# root.insertLeft(10)
# root.insertLeft(1100)
# print((root.getLeft().get_data()))
# root.insertRight(5)
# print((root.getRight().get_data()))
# root.getRight().set_data(2)
# print((root.getRight().get_data()))

if __name__ == "__main__":
    btree = BinaryTree(1)
    btree.left = BinaryTree(2)
    btree.right = BinaryTree(3)
    btree.left.left = BinaryTree(4)
    btree.left.right = BinaryTree(5)
    btree.right.left = BinaryTree(6)
    btree.right.right = BinaryTree(7)

    pre, inorder, post = [], [], []

    # preorderRecursive(btree, pre)
    # inorderRecursive(btree, inorder)
    # postorderRecursive(btree, post)

    # print(pre, inorder, post)

    pre, inorder, post = [], [], []

    # preorderIterative(btree, pre)
    # print(pre)

    # inorderIterative(btree, inorder)
    # print(inorder)

    levelorder = []
    levelOrder(btree, levelorder)
    print(levelorder)
