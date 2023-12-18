class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0
        mem = {0:0, 1:1, 2:2}
        def cnt_stairs(num):

            if num < 1: # top 또는 넘어감
                if num == 0: # num이 top에 위치함
                    cnt += 1
                return cnt
            if num not in mem:
                mem[num] = cnt_stairs(num-1) + cnt_stairs(num-2)
            return mem[num]
        return cnt_stairs(n)

# 2^45 = 3.5184372e+13 -> 완전탐색으로 불가능

# 반복 - 값이 끝에 도달하면 cnt+1, 넘어가면 중지하되 cnt는 그대로, 끝에 도달하지 않으면 반복
# DP는 결국 큰 문제를 작은 하위 문제로 나누는 형식이여야 함