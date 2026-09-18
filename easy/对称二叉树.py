#给你一个二叉树的根节点 root ， 检查它是否轴对称。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def ismirror(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False

        return (
            l.val == r.val
            and self.ismirror(l.left, r.right)
            and self.ismirror(l.right, r.left)
        )

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        return self.ismirror(root.left, root.right)

