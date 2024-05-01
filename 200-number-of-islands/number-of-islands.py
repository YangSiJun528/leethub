import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_cnt = 0
        len_m = len(grid)
        len_n = len(grid[0])
        ways = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        s = []

        for m in range(len_m):
            for n in range(len_n):
                if grid[m][n] == '1' and (m, n) not in visited:
                    island_cnt += 1
                    # DFS Start
                    s.append((m,n))
                    while s:
                        cur_m, cur_n = s.pop()
                        if (cur_m,cur_n) not in visited:
                            visited.add((cur_m, cur_n))
                            for way in ways:
                                next_m, next_n = way[0]+cur_m, way[1]+cur_n
                                if next_m >= 0 and next_n >= 0 and next_m < len_m and next_n < len_n and grid[next_m][next_n] == '1':
                                    s.append((next_m, next_n))
        return island_cnt

        