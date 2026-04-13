class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        numset = set()
        for num in nums: 
            if num in numset: 
                return True
            numset.add(num)
        return False