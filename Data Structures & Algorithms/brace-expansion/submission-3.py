class Solution:
    def expand(self, s: str) -> List[str]:
        
        l = 0
        options = [] # [["a", "b"], "c", ["d", "e"], "f"]
        
        while l < len(s):
            if s[l] == "{":
                option = []
                r = l + 1
                while r < len(s) and s[r] != "}":
                    if s[r] == ",":
                        r += 1
                    option.append(s[r])
                    r += 1
                options.append(option)
                l = r + 1
            else:
                options.append([s[l]])
                l += 1

        output = [] # ["acdf", "acef", "bcdf", "bcef"]
        
        def backtracking(index, currentString):

            if len(options) == index:
                output.append(currentString)
                return

            for letter in options[index]:
                backtracking(index + 1, currentString + letter)

        backtracking(0, "")

        return output



