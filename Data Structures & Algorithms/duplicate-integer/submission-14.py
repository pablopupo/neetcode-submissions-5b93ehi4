class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {} # key: number , value: num of appearances

        for num in nums:
            
            hashmap[num] = hashmap.get(num, 0) + 1

            if hashmap.get(num) > 1:
                return True
        return False
