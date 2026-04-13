class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            num2 = target - nums[i]
            if num2 in numMap:
                return [numMap[num2], i]
            numMap[n] = i
