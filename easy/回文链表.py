class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l = head
        front_node = head
        nodes = []
        while l is not None:
            nodes.append(l)
            l = l.next
        i = 1

        while i <= len(nodes) :

            if nodes[-i].val != front_node.val:
                return False
            if nodes[-i] == front_node:
                return True
            front_node = front_node.next
            i+=1
        if len(nodes)%2==0:
            return True
        return False

    def isPalindrome1(self, head):
        vals = []
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1]