class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        hash = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in hash:
                stack.append(char)
            else:
                if not stack:
                    return False
                if hash[stack.pop()] != char:
                    return False

        return not stack