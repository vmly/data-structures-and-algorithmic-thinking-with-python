# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                        : info@careermonk.com
# Creation Date                 : 2014-01-10 06:15:46
# Last modification             : 2008-10-31
#               by              : Narasimha Karumanchi
# Book Title                    : Data Structures And Algorithms Made In Java
# Warranty                      : This software is provided "as is" without any
#                                  warranty; without even the implied warranty of
#                                   merchantability or fitness for a particular purpose.

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class reorderLists:
    def reverse(self, head):
        dummy = prev = Node(0)
        while head:
            next = head.__next__
            head.next = prev.__next__
            prev.next = head
            head = next
        return dummy.__next__

    def getMiddleNode(self, head):
        slow = fast = head
        while fast.__next__ and fast.next.__next__:
            fast = fast.next.__next__
            slow = slow.__next__
        head = slow.__next__
        slow.next = None
        return head

    def reorderList(self, head):
        if not head or not head.__next__:
            return head
        head2 = self.getMiddleNode(head)
        head2 = self.reverse(head2)
        p = head
        q = head2
        while q:
            qnext = q.__next__  # store the next node since q will be moved
            q.next = p.__next__
            p.next = q
            p = q.__next__
            q = qnext
        return head
