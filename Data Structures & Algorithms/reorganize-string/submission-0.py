class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-count, char] for char,count in count.items()]
        heapq.heapify(heap)
        prev = None
        res = ''
        while heap or prev:
            if prev and not heap: 
                return ''
            count, char = heapq.heappop(heap)
            res += char
            count += 1

            if prev: 
                heapq.heappush(heap,prev)
                prev = None
            
            if count != 0: 
                prev = [count, char]
        return res
# make a counter and reverse the count and char
#heapify it
#