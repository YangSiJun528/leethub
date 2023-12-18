class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        mem = {0:cost[0], 1:cost[1]}
        def recurs(idx):
            if idx not in mem:
                mem[idx] = cost[idx] + min(recurs(idx-1), recurs(idx-2))
            return mem[idx]
        return min(recurs(len(cost)-1), recurs(len(cost)-2))

            
# 시작점이 2개여야 함
# 계단 오르는 경우의 수 문제와 달리 Cost가 있어서 그럼