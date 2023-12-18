class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {(0,0):1}

        def dfs(i, j):
            if (i,j) not in mem:
                cnt = 0
                if i-1 >= 0:
                    cnt += dfs(i-1,j)
                if j-1 >= 0:
                    cnt += dfs(i,j-1)
                mem[(i,j)] = cnt
            return mem[(i,j)]
        return dfs(m-1,n-1)