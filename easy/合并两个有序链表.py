#将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#输入：l1 = [1,2,4], l2 = [1,3,4]
#输出：[1,1,2,3,4,4]
#解释：将两个链表合并为一个升序链表，并返回链表的头节点。

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head

        while l1 and l2:#当两个列表都不为空时

            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next

            else:
                current.next = l2
                l2 = l2.next

            current = current.next
        #将剩余的节点直接连接到结果链表的末尾
        if l1:
            current.next = l1
        else:
            current.next = l2
        #返回结果链表的头节点
        return head.next





