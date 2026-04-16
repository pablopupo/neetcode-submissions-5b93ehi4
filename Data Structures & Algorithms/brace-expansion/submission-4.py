class Solution:
    def expand(self, s: str) -> List[str]:
        i = 0
        options = []
        while i < len(s):
            if s[i] == "{":
                j = i + 1
                option = []
                while j < len(s) and s[j] != "}":
                    if s[j] == ",":
                        j += 1
                    option.append(s[j])
                    j += 1
                options.append(option)
                i = j + 1
            else:
                options.append(s[i])
                i += 1
        
        output = []
        
        def backtrack(index, currentString):
            if index == len(options):
                output.append(currentString)
                return

            for letter in options[index]:
                backtrack(index + 1, currentString + letter)
        
        
        backtrack(0, "")
        return output

