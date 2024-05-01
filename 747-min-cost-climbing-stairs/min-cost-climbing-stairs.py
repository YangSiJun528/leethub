class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:2] + [1000] * (len(cost)-2)
        for i in range(2, len(cost)): 
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])
        