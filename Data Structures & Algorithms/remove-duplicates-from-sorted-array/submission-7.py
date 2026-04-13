class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for n in range(1, len(nums)):
            if nums[n] != nums[n-1]:
                nums[l] = nums[n]
                l += 1
        return l