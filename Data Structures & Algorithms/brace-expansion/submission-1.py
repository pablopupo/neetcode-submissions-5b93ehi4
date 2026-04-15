class Solution:
    def expand(self, s: str) -> List[str]:
        l = 0
        options = []

        while l < len(s):
            if s[l] == "{":
                option = []
                r = l + 1
                while s[r] != "}":
                    if s[r] == ",":
                        r += 1
                    option.append(s[r])
                    r += 1
                options.append(option)
                l = r + 1
            else:
                options.append(s[l])
                l += 1

        result = []
        def backtrack(index, currentString):
            if len(options) == index:
                result.append(currentString)
                return

            for letter in options[index]:
                backtrack(index + 1, currentString + letter)
            
        backtrack(0, "")
        return result