class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has = {}
        for x in nums:
            if x in has:
                has[x]+=1
            else:
                has[x]=1

        for x in nums:
            if has[x]>len(nums)/2:
                return x