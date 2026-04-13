class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # Initialize as the last element, current goal

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0