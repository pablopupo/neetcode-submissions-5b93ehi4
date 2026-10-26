class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # make a queue 
        # what variables will we need
        #double for loop goint through matrix
        #create queue and count how many fresh fruits we have
        # what directions will we go in? 
        #start processing the queue
        #remember the length of the queue since its time sensitive (we only have x num of rotten fruit at a time)
        # check the neighbors if they can become rotten
        #make them motten
    #add them to the quue
        # decrement how many fresh there are 
        #decrement time
        q = deque()
        time, fresh = 0,0
        ROW, COL = len(grid), len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0: 
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row,col = dr + r, dc + c
                    if (row < 0 or row == len(grid) or col <0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

