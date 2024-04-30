class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_n = 0
        mem = {}

        for n in nums:
           mem[n] = True

        for n in nums:
            if n in mem and n-1 not in mem:
                i = n
                cur_max = 0
                while i in mem and mem[i]:
                    mem[i] = False
                    i += 1
                    cur_max += 1
                    max_n = max(max_n, cur_max)

        return max_n
        