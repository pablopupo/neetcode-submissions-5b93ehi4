class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 4, 5, 6]
        # [0, 1]
        d = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in d:
                return [d[result], i]
            d[nums[i]] = i
        