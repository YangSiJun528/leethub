import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        len_x = len(grid)
        ways = [(1,1), (1,0), (1,-1), (-1,1), (0,1), (-1,-1), (-1,0), (0,-1)]
        visited = set()
        q = collections.deque()
        q.append((0,0,1))

        while q:
            cur_x, cur_y, cur_cnt = q.popleft()
            if (cur_x, cur_y) not in visited:
                visited.add((cur_x, cur_y))
                if (cur_x, cur_y) == (len_x-1,len_x-1):
                    return cur_cnt
                for way in ways:
                    next_x, next_y, next_cnt = cur_x+way[0], cur_y+way[1], cur_cnt+1
                    if next_x >= 0 and next_y >= 0 and next_x < len_x and next_y < len_x and grid[next_x][next_y] == 0:
                        q.append((next_x, next_y, next_cnt))
        return -1
        

        