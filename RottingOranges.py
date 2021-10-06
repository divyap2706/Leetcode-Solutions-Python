from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        if rows==0: #if the grid is empty return -1
            return -1
        cols=len(grid[0])
        fresh=0 #count of fresh oranges
        rotten=deque() #queue of rotten oranges
        for r in range(rows): #Traverse all oranges and add it in fresh or rotten queue
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        minutes=0 #To track the minutes
        while rotten and fresh>0: #BFS
            minutes+=1
            for i in range(len(rotten)):
                x,y=rotten.popleft() #remove the 1st item in rotten queue
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]: #check in all four directions for fresh oranges
                    xx,yy=x+dx,y+dy
                    if xx<0 or xx==rows or yy<0 or yy==cols: #ignore if it's out of the grid boundary
                        continue
                    if grid[xx][yy]==0 or grid[xx][yy]==2: #if it's an empty node or already in the rotten queue, ignore
                        continue
                    fresh-=1 #reduce the fresh count
                    grid[xx][yy]=2 #increase the rotten count
                    rotten.append((xx,yy)) #add the newly rotten orange's coordinates in the queue

        return minutes if fresh==0 else -1

# Time complexity=O(rows*columns)
# Space complexity=O(rows*columns)




        
