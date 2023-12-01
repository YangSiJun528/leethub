class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


        
# 다 곱해논 값이 나누기는 0 때문에 안됨 + 나누기 사용불가 조건
# 시간복잡도 O(n)이여야 함
# 나를 오 -> 왼 곱의 값에 오 <- 왼 값의 곱을 구하면 됨