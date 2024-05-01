class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        OVER = 2**31 # 1 <= coins[i] <= 2**31 - 1 -> 기본값을 최대값보다 크게
        dp = [OVER] * (amount+1)

        for c in coins:
            if c <= amount:
                dp[c] = 1

        for n in range(1,(amount+1)):
            for c in coins:
                if n-c > 0:
                    dp[n] = min(dp[n-c] + 1, dp[n])
        if dp[amount] == OVER:
            return -1
        return dp[amount]
            


# climbing-stairs와 비슷함.
# n위치까지 올 수 있는 최소 경우의 수를 DP 테이블에 저장하거나 재귀호출에서 반환하면 됨
#   for c in coins -> dp[n-c]