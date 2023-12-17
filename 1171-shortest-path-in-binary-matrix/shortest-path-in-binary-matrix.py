import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        valid_x = lambda x: x < len(grid) and x >= 0
        valid_y = lambda y: y < len(grid) and y >= 0

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visited = set((0,0))
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        q = collections.deque()
        q.append((0,0,1))
        
        while q:
            cur_x, cur_y, cur_cnt = q.popleft()
            if (cur_x, cur_y) == (len(grid)-1, len(grid)-1):
                return cur_cnt
                
            for i in range(8):
                next_x = dx[i] + cur_x
                next_y = dy[i] + cur_y
                if (
                    valid_x(next_x) and valid_y(next_y) 
                    and (next_x,next_y) not in visited
                    and grid[next_x][next_y] == 0):
                    q.append((next_x,next_y,cur_cnt+1))
                    visited.add((next_x,next_y))
        return -1
        