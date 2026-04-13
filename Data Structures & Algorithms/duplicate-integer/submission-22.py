class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       saw = set()
       for num in nums:
            if num in saw: 
                return True
            saw.add(num)
       return False