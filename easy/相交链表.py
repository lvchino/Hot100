# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB

        while(a is not None):
            b = headB
            while(b is not None):
                if a == b:
                    return a
                else:
                    b = b.next
            a = a.next

        return None

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a != b:

            if a is None:
                a = headB
            else:
                a = a.next

            if b is None:
                b = headA
            else:
                b = b.next

        if a == b:
            return a
        else:
            return None


