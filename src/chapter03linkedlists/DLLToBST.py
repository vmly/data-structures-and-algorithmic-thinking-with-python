# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithms Made In Java
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.


def DLLtoBalancedBST(head):
    if not head or not head.__next__:
        return head
    temp = FindMiddleNode(
        head
    )  # Refer Linked Lists chapter for this function. We can use two-pointer logic to find the middle node
    p = head
    while p.__next__ != temp:
        p = p.__next__
    p.next = None
    q = temp.__next__
    temp.next = None
    temp.prev = DLLtoBalancedBST(head)
    temp.next = DLLtoBalancedBST(q)
    return temp
