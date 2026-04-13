class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numCount = set()

        for num in nums:
            if num in numCount:
                return True
            numCount.add(num)

        return False