class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count = {1: 2, 2:4,} freq[2] frequency at the count index append list of nums bc count = index
        #[1,1,1,2,2,100] freq = 0,1,2,3,4,5,6 len freq = 7 incldue 6 not 0 
        count = Counter(nums)
        freq = [[] for i in range (len(nums) + 1)]
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res