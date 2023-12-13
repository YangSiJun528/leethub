class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        answer = 0 

        for num in nums:
            if num in cache and num - 1 not in cache:
                step = 0
                next = num
                while next in cache:
                    next += 1
                    step += 1
                answer = max(answer, step)
        return answer