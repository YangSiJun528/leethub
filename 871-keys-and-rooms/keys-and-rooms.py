class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = [False] * len(rooms)
        visited_rooms[0] = True
        s = []
        s.extend(rooms[0])

        # DFS
        while s:
            cur_idx = s.pop()
            if not visited_rooms[cur_idx]:
                visited_rooms[cur_idx] = True
                s.extend(rooms[cur_idx])
        
        return False not in visited_rooms 

        