class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in numMap:
                return [numMap[difference], i]
            numMap[n] = i
            