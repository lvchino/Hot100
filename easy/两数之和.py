# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。

#定义一个数组num
n = [2, 7, 11, 15]
tar = 9

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    def twoSum1(self, nums, target):
        #构建一个空字典
        num_dict = {}
        #遍历列表，构建字典
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        #遍历列表，查找目标元素
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [i,num_dict[target - nums[i]]]

    def twoSum2(self, nums, target):
        # 构建一个空字典
        num_dict = {}
        # 遍历列表，构建字典
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [i, num_dict[target - nums[i]]]
            num_dict[nums[i]] = i


#本地测试
so = Solution()
print(so.twoSum1(n, tar))





