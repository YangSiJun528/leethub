class Solution:
    def dp(self, m, n, mem):
        if m < 0 or n < 0:
            return 0
        if (m,n) not in mem:
            mem[(m,n)] = self.dp(m-1, n, mem) + self.dp(m, n-1, mem)
        return mem[(m,n)]

    def uniquePaths(self, m: int, n: int) -> int:
        # 0,0이 finish 영역이라고 가정 
        return self.dp(m-1, n-1, {(0,0):1})
            
            

# 어쨌든 방해물이 없으니꺄 움직일 수 있는데로만 가면 무조건 최소 횟수
# 가능한 경우의 수를 작성하면 됨
# finish 기준으로 수를 올려가면서 접근하면 될 듯?
# 아니면 재귀로 끝 도착하면 1씩 더하던가