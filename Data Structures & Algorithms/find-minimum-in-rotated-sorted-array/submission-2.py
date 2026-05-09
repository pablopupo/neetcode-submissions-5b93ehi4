class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(start, end): 
            middle = (start + end) // 2
            if start == middle:
                if nums[start] > nums[end]:
                    return nums[end]
                else:
                    return nums[start]

            if nums[end] > nums[start]:
                return nums[start]
                
            elif nums[start] > nums[end]: 
                if nums[start] > nums[middle]:
                    return binarySearch(start, middle)
                else:
                    return binarySearch(middle, end)
        return binarySearch(0, len(nums) - 1)