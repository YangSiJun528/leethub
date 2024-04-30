class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rs = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and s[-1][0] < t:
                prev_t = s.pop()
                rs[prev_t[1]] = i - prev_t[1]
            s.append((t,i))
        return rs
        