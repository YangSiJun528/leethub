class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # 초기화
        coins = list(filter(lambda x: x < 10001, coins))
        dp = [2**31] * 10001
        for c in coins:
            dp[c] = 1
            if c == amount:
                return 1
        
        for i in range(1,10001):
            rs = [dp[i]]
            for c in coins:
                if c < 1:
                    continue
                rs.append(dp[i-c]+1)
            if rs:
                dp[i] = min(rs)
        if dp[amount] > 10000:
            return -1
        return dp[amount]

        

# 그 계단 오르기 생각하면 됨
# amount가 n일때 가장 적은 수는 (for c in coins -> n-c)중 가장 적은 수의 +1 한 값
# 근데 특정 경우가 없을수도 있음, 그래서 기본 값으로 충분히 큰 값(2**31)을 부여함. (amount의 최대 값이 (2**31-1) 임)