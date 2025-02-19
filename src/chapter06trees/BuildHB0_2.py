# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithmic Thinking With Python
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.

count = 0


class AVLNode:
    def __init__(self, data, balanceFactor, left, right):
        self.data = data
        self.balanceFactor = 0
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.root = None

    def inOrderPrint(self):
        self.recInOrderPrint(self.root)

    def recInOrderPrint(self, root):
        if root != None:
            self.recInOrderPrint(root.left)
            print((root.data))
            self.recInOrderPrint(root.right)

    def insert(self, data):
        newNode = AVLNode(data, 0, None, None)
        [self.root, taller] = self.recInsertAVL(self.root, newNode)

    def recInsertAVL(self, root, newNode):
        if root == None:
            root = newNode
            root.balanceFactor = 0
            taller = True
        elif newNode.data < root.data:
            [root.left, taller] = self.recInsertAVL(root.left, newNode)
            if taller:
                if root.balanceFactor == 0:
                    root.balanceFactor = -1
                elif root.balanceFactor == 1:
                    root.balanceFactor = 0
                    taller = False
                else:
                    root = self.rightLeftRotate(root)
                    taller = False
        else:
            [root.right, taller] = self.recInsertAVL(root.right, newNode)
            if taller:
                if root.balanceFactor == -1:
                    root.balanceFactor = 0
                    taller = False
                elif root.balanceFactor == 0:
                    root.balanceFactor = 1
                else:
                    root = self.rightLeftRotate(root)
                    taller = False
        return [root, taller]

    def rightLeftRotate(self, root):
        X = root.right
        if X.balanceFactor == 1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.singleRightRoate(r)
        else:
            Y = X.left
            if Y.balanceFactor == -1:
                root.balanceFactor = 0
                X.balanceFactor = 1
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = -1
                X.balanceFactor = 0
            Y.balanceFactor = 0
            root.right = self.singleLeftRotate(X)
            root = self.singleRightRoate(root)
        return root

    def rightLeftRotate(self, root):
        X = root.left
        if X.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.singleLeftRotate(root)
        else:
            Y = X.right
            if Y.balanceFactor == -1:
                root.balanceFactor = 1
                X.balanceFactor = 0
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = 0
                X.balanceFactor = -1
            Y.balanceFactor = 0
            root.left = self.singleRightRoate(X)
            root = self.singleLeftRotate(root)
        return root

    def singleRightRoate(self, r):
        X = root.right
        root.right = X.left
        X.left = r
        return X

    def singleLeftRotate(self, root):
        W = root.left
        root.left = W.right
        W.right = root
        return W

    def height(self):
        return self.recHeight(self.root)

    def recHeight(self, root):
        if root == None:
            return 0
        else:
            leftH = self.recHeight(root.left)
            rightH = self.recHeight(root.right)
            if leftH > rightH:
                return 1 + leftH
            else:
                return 1 + rightH


def BuildHB0_2(l, r):
    mid = l + (r - l) // 2
    if l > r:
        return None
    avlNode = AVLTree()
    avlNode.root = avlNode
    avlNode.left = BuildHB0_2(l, mid - 1)
    avlNode.right = BuildHB0_2(mid + 1, r)
    avlNode.data = mid
    return avlNode


def tester():
    avlNode = BuildHB0_2(0, 15)
    avlNode.inOrderPrint()
    print(("height = ", avlNode.height()))


if __name__ == "__main__":
    tester()
