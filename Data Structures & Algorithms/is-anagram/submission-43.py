class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        sets = {}
        sett = {}
        
        for char in s:
            sets[char] = sets.get(char,0) + 1
        for char in t: 
            sett[char] = sett.get(char,0) + 1
        return sets == sett