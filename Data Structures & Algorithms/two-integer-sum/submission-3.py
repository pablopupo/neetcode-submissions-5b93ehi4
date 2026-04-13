class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3 8 5 6
        # l     r
        # target = 13

        my_dict = {} # val -> index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_dict:
                return [my_dict[difference], i]
            my_dict[nums[i]] = i