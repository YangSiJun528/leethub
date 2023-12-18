class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        mem = {0:cost[0], 1:cost[1]}
        for idx in range(2, len_cost):
            if idx not in mem:
                mem[idx] = cost[idx] + min(mem[idx-1], mem[idx-2])
        return min(mem[len_cost-1], mem[len_cost-2])

            
# 시작점이 2개여야 함
# 계단 오르는 경우의 수 문제와 달리 Cost가 있어서 그럼
# top의 cost는 0임