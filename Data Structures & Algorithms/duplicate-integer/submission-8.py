class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            if count_map.get(num) > 1:
                return True

        return False