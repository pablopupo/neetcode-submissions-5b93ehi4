class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        HashMap = {}

        for num in nums:
            HashMap[num] = HashMap.get(num, 0) + 1
            if HashMap.get(num) > 1:
                return True
        return False