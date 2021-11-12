# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithmic Thinking With Python
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.


def treeMaximumSumPath(node, is_left=True, Lpath={}, Rpath={}):
    if is_left:
        # left sub-tree
        if not node.left:
            Lpath[node.id] = 0
            return 0
        else:
            Lpath[node.id] = node.data + max(
                treeMaximumSumPath(node.left, True, Lpath, Rpath),
                treeMaximumSumPath(node.left, False, Lpath, Rpath),
            )
            return Lpath[node.id]
    else:
        # right sub-tree
        if not node.right:
            Rpath[node.id] = 0
            return 0
        else:
            Rpath[node.id] = node.data + max(
                treeMaximumSumPath(node.right, True, Lpath, Rpath),
                treeMaximumSumPath(node.right, False, Lpath, Rpath),
            )
            return Rpath[node.id]


def maxsum_path(root):
    Lpath = {}
    Rpath = {}
    treeMaximumSumPath(root, True, Lpath, Rpath)
    treeMaximumSumPath(root, False, Lpath, Rpath)
    print(("Left-path:", Lpath))
    print(("Right-path:", Rpath))
    path2sum = dict((i, Lpath[i] + Rpath[i]) for i in list(Lpath.keys()))
    i = max(path2sum, key=path2sum.get)
    print(("The path going through node", i, "with max sum", path2sum[i]))
    return path2sum[i]

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

def solution2(root):
    global max_path
    max_path = float("-inf")

    def helper(node):
        if node is None:
            return 0
        gain_left = max(0, helper(node.left))
        gain_right = max(0, helper(node.right))

        global max_path
        max_path = max(max_path, node.data + gain_left + gain_right)

        return node.data + max(gain_left, gain_right)

    helper(root)

    return max_path

if __name__ == "__main__":

    btree = BinaryTree(1)
    btree.left = BinaryTree(2)
    btree.right = BinaryTree(3)
    btree.left.left = BinaryTree(4)
    btree.left.right = BinaryTree(5)
    btree.right.left = BinaryTree(6)
    btree.right.right = BinaryTree(7)
    # treeMaximumSumPath(btree)

    print(solution2(btree))