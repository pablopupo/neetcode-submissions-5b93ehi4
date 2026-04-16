class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
"""
 Input: nums = [1,2,3,2,2]

    index = 0
    nums[index] = 1
    nums[1] = 2
    nums[2] = 3
    nums[3] = 2
    nums[2] = 3
    nums[3] = 2
              Y
         |---------|
  X      |         \\
---------|         |
         |---------|
         Z

slow = X + Y
fast = X + 2Y + Z

2(slow) = fast
2(X+Y) = X+2Y+Z
2X + 2Y = X + 2Y + Z
X = Z """