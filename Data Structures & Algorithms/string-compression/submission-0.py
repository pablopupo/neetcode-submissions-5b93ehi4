class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0
        
        while i < len(chars):
            length = 1
            while (length + i) < len(chars) and chars[length + i] == chars[i]:
                length += 1
            chars[insert] = chars[i]
            insert += 1
            if length > 1:
                for digit in str(length):
                    chars[insert] = digit
                    insert += 1
            i += length
        return insert