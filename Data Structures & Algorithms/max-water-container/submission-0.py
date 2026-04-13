class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1

        while l != r:
            current = (r - l) * min(heights[r], heights[l])
            
            res = max(current, res)

            if heights[l] > heights[r]:
                r -= 1

            else:
                l += 1

        return res