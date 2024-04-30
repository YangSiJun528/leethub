class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            if target - nums[i] in mem:
                return (mem[target - nums[i]], i)
            mem[nums[i]] = i
        