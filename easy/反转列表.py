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
        a = head
        nodes = []
        #将链表存入列表中
        while a is not None:
            nodes.append(a)
            a = a.next
        #将列表反转
        rev = nodes[::-1]
        #将反转后的列表重新连接成链表
        for i in range(len(rev)-1):
            rev[i].next = rev[i+1]
        #注意处理最后一个node,即之前的head,避免成环
        if len(rev) > 0:
            rev[-1].next = None
            return rev[0]
        return None

