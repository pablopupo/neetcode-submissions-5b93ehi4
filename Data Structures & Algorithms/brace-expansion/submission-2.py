class Solution:
    def expand(self, s: str) -> List[str]:
        options = []
        l = 0
        while l < len(s):
            if s[l] == "{":
                r = l + 1
                option = []
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


        results = []
        def backtracking(index, currentString):
            if index == len(options):
                results.append(currentString)
                return

            for letter in options[index]:
                backtracking(index + 1, currentString + letter)
        
        backtracking(0, "")
        return results