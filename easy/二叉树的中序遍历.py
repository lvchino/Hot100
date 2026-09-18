# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        else:
            # 递归遍历左子树，根节点，右子树
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



