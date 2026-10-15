class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        right = 0
        left = 0

        if not s: return 0

        window = set()

        while right < len(s):

            if s[right] not in window:
                window.add(s[right])
                res = max(res, len(window))
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
            # 删除左边元素后要将右指针元素补入
            window.add(s[right])
            right += 1

        return res

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        res = 0

        if not s: return 0
        cur_window = set()

        while right < len(s):

            while s[right] in cur_window:
                cur_window.remove(s[left])
                left += 1

            cur_window.add(s[right])
            res = max(res, len(cur_window))
            right += 1
        return res