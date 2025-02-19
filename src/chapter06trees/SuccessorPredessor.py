# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithmic Thinking With Python
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.

# Successror of a node in BST
def successorBST(root):
    temp = None
    if root.getRight():
        temp = root.getRight()
        while temp.getLeft():
            temp = s.getLeft()
    return temp


# Predecessor of a node in BST
def predecessorBST(root):
    temp = None
    if root.getLeft():
        temp = root.getLeft()
        while temp.getRight():
            temp = temp.getRight()
    return temp
