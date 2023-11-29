class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# num / 2 = pair의 개수
# 정렬한 상태에서 짝수 인덱스 값을 기준으로 실행하면 됨

# v1
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         answer = 0

#         for i in range(0,len(nums), 2):
#             answer += nums[i]

#         return answer
