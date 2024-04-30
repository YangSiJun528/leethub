class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ']':'[', ')':'('}
        for c in s:
            if c in '}])':
                if not stack:
                    return False
                if stack.pop() != mapping[c]:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True
        