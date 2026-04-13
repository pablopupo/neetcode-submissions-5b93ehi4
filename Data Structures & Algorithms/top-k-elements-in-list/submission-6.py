class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {} # {num, count}

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1
        
        # numCount = {1:1, 5,2, 3:3} and k = 2 => return [5, 3]

        arr = []

        for key, value in numCount.items():
            arr.append([value, key])

        arr.sort() # [[1:1], [2,5], [3:3]]

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
            
        return res