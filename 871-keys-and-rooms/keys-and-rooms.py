import collections

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = [False] * len(rooms)
        visited_rooms[0] = True
        q = collections.deque()
        q.extend(rooms[0])

        while q:
            cur_idx = q.popleft()
            if not visited_rooms[cur_idx]:
                visited_rooms[cur_idx] = True
                q.extend(rooms[cur_idx])
        
        return False not in visited_rooms 

        