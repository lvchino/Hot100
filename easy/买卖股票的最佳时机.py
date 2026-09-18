# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #求最大利润,初始为0
        max1 = 0
        #初始化dp
        n = len(prices)
        dp = [[0]*n for i in range(n)]
        for i in range(1,n) :
            dp[0][i] = prices[i] - prices[0];
            max1 = max(max1, dp[0][i])

        for i in range(1,n-1) :
            for j in range(i+1,n):
                #卖出时间j相同，买入时间i不同的转移公式,
                # dp[i-1][j]提前一天买入的总利润
                # + prices[i-1]提前一天买的钱还给你，
                # - prices[i]表示付推迟一天买的钱
                dp[i][j] = prices[i-1] - prices[i] + dp[i-1][j];
                max1 = max(max1, dp[i][j])
        return max1

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 求最大利润,初始为0
        max1 = 0
        # 对每一天来说，最大利润 = 今日卖价 - 历史最低价格;这个天数大于2.
        n = len(prices)
        # 史低初始为第一天售价
        history_low = prices[0]
        if n == 1:
            return 0
        for i in range(1, n):
            # 记录当前利润
            curr = prices[i] - history_low
            # 更新最大利润
            max1 = max(curr, max1)
            # 更新史低价格
            history_low = min(history_low, prices[i])
        return max1
