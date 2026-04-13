class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ins = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1
            chars[ins] = chars[i]
            ins += 1

            if group > 1:
                for digit in str(group):
                    chars[ins] = digit
                    ins += 1
                
            i += group
        
        return ins