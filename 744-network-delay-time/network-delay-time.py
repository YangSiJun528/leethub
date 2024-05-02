import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(lambda: [])
        for t in times:
            graph[t[0]].append((t[1], t[2])) # path, cost
        
        costs = {}
        pq = []
        cnt = 0
        last = 0
        heapq.heappush(pq, (0, k)) # cur_cost, start

        while pq:
            cost, node = heapq.heappop(pq)
            if node not in costs:
                costs[node] = cost
                cnt += 1
                last = cost
                for next_node, next_cost in graph[node]:
                    heapq.heappush(pq, (cost+next_cost, next_node))
        if cnt != n:
            return -1
        return last