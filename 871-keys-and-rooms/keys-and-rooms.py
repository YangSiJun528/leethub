class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
                return True

        visited = set()
        def dfs(cur_v):
            visited.add(cur_v)
            for v in rooms[cur_v]:
                if v not in visited:
                    dfs(v)
            return len(visited) == len(rooms)
        return dfs(0)

# 생각해보나 dict 필요없음 + 불필요한 print 제거
# 예외 경우(rooms가 0일떄) 추가