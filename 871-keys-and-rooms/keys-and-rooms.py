class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(cur_v):
            visited.add(cur_v)
            print(cur_v, visited)
            for v in rooms[cur_v]:
                if v not in visited:
                    dfs(v)
            return len(visited) == len(rooms)
        return dfs(0)

# 생각해보나 dict 필요없음