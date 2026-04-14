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
                options.append([s[l]])
                l += 1
        res = []

        def dfs(index, curr):

            if index == len(options):
                res.append(curr)
                return

            for o in options[index]: 
                for e in o:
                    dfs(index + 1, curr + e)
        
        dfs(0, "")
        return sorted(res)
