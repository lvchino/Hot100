class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #先排序
        nums.sort()
        n = len(nums)
        #用数组res存放结果
        res = []
        #固定一个数
        #注意是n-2；要给y或者z留位置
        for i in range(n-2):
            x = nums[i]
            #防止x重复
            if i != 0 and nums[i-1] == x: continue
            #有序两数之和
            #left从前往后，right从后往前
            left = i+1
            right = n-1
            while left < right :
                y = nums[left]
                z = nums[right]
                xyzsum = x + y + z
                #判断当前和与Target的关系
                #情况1
                if xyzsum < 0: left += 1
                #情况2
                if xyzsum == 0:
                    #1.输出结果
                    res.append([x,y,z])
                    #2.输出后要记得更新指针！！！！
                    left+= 1
                    #right-=1
                    #3.去重！！！！！
                    while left < right and y == nums[left] : left+=1
                    while left < right and z == nums[right] : right-=1
                #情况3
                if xyzsum > 0: right -= 1
        return res

