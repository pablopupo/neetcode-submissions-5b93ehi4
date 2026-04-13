class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r: 
            if s[l] != s[r]: 
                subl, subr = s[l+1:r+1], s[l:r]
                return (subl == subl[::-1] or subr == subr[::-1])
            l += 1  
            r -= 1
        return True