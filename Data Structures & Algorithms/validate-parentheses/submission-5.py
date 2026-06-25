class Solution:
    def isValid(self, s: str) -> bool:
        validSearch = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s:
            if char in validSearch:
                if not stack or stack[-1] != validSearch[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack