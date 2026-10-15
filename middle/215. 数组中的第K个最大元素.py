class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #分治，快排思想；右中左顺序最好
        mid_num = random.choice(nums)

        #大的放右边
        right = []
        for num in nums:
            if num > mid_num:
                right.append(num)
        #相同的放中间
        mid = []
        for num in nums:
            if num == mid_num:
                mid.append(num)
        #小的放左边
        left = []
        for num in nums:
            if num < mid_num:
                left.append(num)
        # k在哪? k看作排名，排名为k,招len个；第一档
        if k <= len(right):
            return self.findKthLargest(right,k)
        # k在哪? 滑档，第二档
        elif k <= len(right) + len(mid):
            return mid_num
        #第三档
        else:
             return self.findKthLargest(left, k-len(right)-len(mid))






