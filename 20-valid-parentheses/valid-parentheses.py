class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            #print(stack, c)
            if c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif c == "(":
                stack.append(")")
            elif not stack or stack.pop() != c: 
                    return False
        return len(stack) == 0
