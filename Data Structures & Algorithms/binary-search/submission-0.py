class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(start, end):
            if start > end:
                return -1

            middle = (start + end) // 2
            
            if target == nums[middle]: 
                return middle 
            elif target > nums[middle]: 
                return binarySearch(middle + 1, end)
            elif target < nums[middle]:
                return binarySearch(start, middle - 1)
            

        return binarySearch(0, len(nums) - 1)
