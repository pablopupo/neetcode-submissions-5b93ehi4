class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # key = number value = how many times weve seen it 
        for num in nums: 
            hashmap[num] = hashmap.get(num, 0) + 1 
        #{1:1, 2:2, 3:3}
        
        array = [] # [[1, 1], [2, 2], [3, 3]]

        for num, cnt in hashmap.items(): 
            array.append([cnt, num])
        
        array.sort() # [[1, 1], [2, 2], [3, 3]] 

        res =  []

        while len(res) < k:
            res.append(array.pop()[1])

        return res