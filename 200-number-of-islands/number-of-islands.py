import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        cnt = 0
        q = collections.deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                #print(grid)
                if grid[x][y] == "1":
                    cnt += 1
                    q.append((x,y))
                    while q:
                        cur_x, cur_y = q.popleft()
                        for i in range(4):
                            next_x = dx[i] + cur_x
                            next_y = dy[i] + cur_y
                            if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) and grid[next_x][next_y] == "1":
                                q.append((next_x, next_y))
                                grid[next_x][next_y] = "-1"
        return cnt


                    
        