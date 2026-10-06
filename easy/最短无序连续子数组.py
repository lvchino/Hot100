from mammoth.docx.complex_fields import begin


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_value = nums[0]
        left_value = nums[-1]

        begin = 0
        end = -1

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            #一直出现升序，就一直不更新右边界
            if nums[i] >= right_value:
                right_value = nums[i]
            #但凡出现降序，就更新右边界，
            #保证右边界往右都是升序，因为如果往右有降序，就会更新右边界。
            else:
                end = i

        for i in range(len(nums)-1,-1,-1):
            #一直出现降序，就一直不更新左边界，一直降序到头，就说明全程降序，全程有序
            if nums[i] <= left_value:
                left_value = nums[i]
            #如果中途出现升序，
            #那就说明这里一直到头不是单调递减的，因此要把左边界往这个点前面移动
            else:
                begin = i

        return end - begin + 1