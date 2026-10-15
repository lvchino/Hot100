# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 当前指针
        cur = head
        if not cur: return cur

        # 后续指针
        nxt = head.next

        # 前面指针
        pre = None

        while cur is not None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre




