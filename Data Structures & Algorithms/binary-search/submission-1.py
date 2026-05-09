class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start, end):
            if start > end:
                return -1
            
            middle = (start + end) // 2

            if nums[middle] == target: 
                return middle
            elif nums[middle] > target: 
                return binarySearch(start, middle - 1)
            elif nums[middle] < target: 
                return binarySearch(middle + 1, end)
            
        return binarySearch(0, len(nums) - 1)
        