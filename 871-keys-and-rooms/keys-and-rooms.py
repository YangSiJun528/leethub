class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        dict_rooms = {}
        for i in range(len(rooms)):
            dict_rooms[i] = rooms[i]
        print(dict_rooms)
        def dfs(cur_v):
            visited.add(cur_v)
            print(cur_v, visited)
            for v in dict_rooms[cur_v]:
                if v not in visited:
                    dfs(v)
            return len(visited) == len(rooms)
        return dfs(0)
