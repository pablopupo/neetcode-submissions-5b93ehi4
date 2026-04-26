class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [[1,  2,  4,  8]
        # [10, 11, 12, 13]
        # [14, 20, 30, 40]] target = 10

        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            middleRow = (top + bottom) // 2
            if target < matrix[middleRow][0]:
                bottom = middleRow - 1
            elif target > matrix[middleRow][-1]:
                top = middleRow + 1
            else:
                break
        
        if top > bottom:
            return False
        
        l, r = 0, columns - 1

        while l <= r:
            middle = (l + r) // 2
            if target < matrix[middleRow][middle]:
                r = middle - 1
            elif target > matrix[middleRow][middle]:
                l = middle + 1
            else:
                return True

        return False