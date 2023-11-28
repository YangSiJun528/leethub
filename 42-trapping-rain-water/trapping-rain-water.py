class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:  # 변곡점 = 지금 block이 바로 이전 블록보다 더 높은 경우
                top = stack.pop()

                if not len(stack):  # 스택이 빈다면
                    break
                    
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]])-height[top]
                
                volume += distance * waters

            stack.append(i)     

        return volume

# v1 - 투 포인트
# def trap(self, height: List[int]) -> int:
#     if not height:
#         return 0

#     volume = 0
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]

#     while left < right:
#         left_max, right_max = max(height[left], left_max), max(height[right], right_max)

#         if left_max <= right_max:
#             volume += left_max - height[left]
#             left += 1
#         else:
#             volume += right_max - height[right]
#             right -= 1

#     return volume

# 좌 우 포인터가 블럭의 높이가 높은 곳으로 이동
# 좌 우 max는 좌 우 지나온 블록의 최대 높이를 의미한다. 해당 블록보다 내 블록의 높이가 낮다면 그만큼의 물이 들어갈 수 있다.

# v2 - stack
# 이거 솔직히 못알아들었음
    # def trap(self, height: List[int]) -> int:
    #     volume = 0
    #     stack = []
    # 
    #     for i in range(len(height)):
    # 
    #         while stack and height[i] > height[stack[-1]]:  # 변곡점 = 지금 block이 바로 이전 블록보다 더 높은 경우
    #             top = stack.pop()
    # 
    #             if not len(stack):  # 스택이 빈다면
    #                 break
    # 
    #             distance = i - stack[-1] - 1
    #             waters = min(height[i], height[stack[-1]]) - height[top]
    # 
    #             volume += distance * waters
    #         stack.append(i)
    # 
    #     return volume