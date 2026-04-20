class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pares = {"(" :")","{":"}","[":"]"}
        if len(s) % 2 != 0: return False
        for c in s:
            if c in pares:
                stack.append(pares[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return not stack