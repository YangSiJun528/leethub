class Solution:
    def __init__(self):
        self.mem = {}
        self.cost = None

    def dp(self, cur_idx):
        if cur_idx not in self.mem:
            self.mem[cur_idx] = min(self.dp(cur_idx-1), self.dp(cur_idx-2)) + self.cost[cur_idx]
        return self.mem[cur_idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.mem[0] = cost[0]
        self.mem[1] = cost[1]
        self.cost = cost
        return min(self.dp(len(cost)-1), self.dp(len(cost)-2))
        