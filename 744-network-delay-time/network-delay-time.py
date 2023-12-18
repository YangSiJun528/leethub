import heapq, collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))
            #graph[time[1]] - 현재 node가 바라보는? edge가 없을때, 빈 배열 설정
        costs = {}
        pq = []
        print(graph)
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))
        return max(costs.values()) if len(costs) == n else -1
        
# max 안쓰고 그냥 max_value 변수 만들고 갱신하는 식으로 해도 될 듯?