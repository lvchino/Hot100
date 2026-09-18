class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
    #定义一个Dp数组
        dp = [1, 2]
        for i in range(2, n-1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n-1]

