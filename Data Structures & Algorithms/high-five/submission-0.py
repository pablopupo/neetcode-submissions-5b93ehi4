class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        i = 0
        solution = []
        items.sort(key=lambda x:(x[0],-x[1]))
        n = len(items)
        while i < n: 
            id = items[i][0]
            sum_values = 0
            for k in range(i,i+K):
                sum_values += items[k][1]
            while i < n and items[i][0] == id: 
                i += 1
            solution.append([id,sum_values//5])
        return solution


            
