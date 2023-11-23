class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


# v1 - n^2
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []

#         for c in s:
#             if c.isalnum():
#                 strs.append(c.lower())
#         #print(strs, len(strs))

#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False

#         return True


# v2 - n
# import collections

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         q = collections.deque()

#         for c in s:
#             if c.isalnum():
#                 q.append(c.lower())
#         #print(strs, len(strs))

#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False

#         return True