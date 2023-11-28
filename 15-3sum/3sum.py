class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기 - 같은 값인 경우
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_idx, right_idx = i + 1, len(nums) - 1
            while left_idx < right_idx:
                sum_num = nums[i] + nums[left_idx] + nums[right_idx]
                if sum_num < 0:
                    left_idx += 1
                elif sum_num > 0:
                    right_idx -= 1
                else:
                    # 정답이므로 스킵
                    answer.add((nums[i], nums[left_idx], nums[right_idx]))
                    # 투포인트 종료 or 넘길 포인트 값이 바뀌는 경우
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx += 1
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]:
                        right_idx -= 1
                    left_idx += 1
                    right_idx -= 1

        return answer
