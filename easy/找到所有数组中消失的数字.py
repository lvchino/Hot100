# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash1 = {}

        for i in range(1,len(nums)+1):
            hash1[i] = 1

        for num in nums:

            if num in hash1:
                hash1.pop(num)

        return hash1.keys()


