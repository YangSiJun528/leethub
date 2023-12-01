class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_num = max(prices)
        answer = 0
        for i in range(len(prices)):
            lowest_num = min(lowest_num, prices[i])
            answer = max(answer, prices[i] - lowest_num)
        return answer