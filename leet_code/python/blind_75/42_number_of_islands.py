"""
https://neetcode.io/problems/count-number-of-islands?list=blind75
First graphs question, was pretty off the mark on this one, simply because I don't really know 
how to do traversals with graphs yet so set a very clear timebox. Actually ended up stopping
beforehand since I didn't have many leads on how to approach it in a reasonable timeframe. 

Regardless the solution is pretty cool. This is my first pass, doesnt even return anything.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recurve(x: int, y: int) -> None:
            if 0 < x < (len(grid[0])-1):
                left = x - 1
                right = x + 1 
        i, j, groups = 0, 0, 0
        while i < len(grid):
            stack = []
            while j < len(grid[0]):
                if grid[i][j] == 0:
                    j += 1
                    continue
                else:
                    stack.append(grid[i][j]) 

"""
This is the solution, specifically the DFS approach. I primarily thought the BFS approach but still
couldnt really put it into practice. 

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]     # init directions is pretty cool, makes it alot cleaner, they do go every direction as well. 
        ROWS, COLS = len(grid), len(grid[0])                # defining lengths right away to make sure we can move around as we want
        islands = 0

        def dfs(r, c):                                      # takes in row and column, x and y
            if (r < 0 or c < 0 or r >= ROWS or              # since they do transitions in the recuve calls, they check if the provided coords are valid
                c >= COLS or grid[r][c] == "0"              # instead of checking if they would be valid before passing through, which is also a lot cleaner
            ):
                return

            grid[r][c] = "0"                                # setting the 0 to make sure we don't count it again
            for dr, dc in directions:                       # going through all directions one at a time to their maximum depth, setting their 1s to 0s
                dfs(r + dr, c + dc)                         # thats kinda the whole point, since each connecting structure we see is only gonna be 1 island. 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)                               # every connecting setup is only 1 island, this essentually greygoose wipes away islands and adds 
                    islands += 1                            # it to the counter, so subsequent interations will just see 0s and can move on faster.

        return islands


"""
Came back the next day to see if I could do it, was able to figure it out. Overall simple enough.
Found myself just doing depth first search. Maybe we should try another one with breath?
I generally like the idea of going through a stack more since recuve is a bit harder to read
but since this one is simple enough I guess its fine. 
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsearch(row, column):
            if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
                # row and column are valid, good to check
                if grid[row][column] == '1':
                    grid[row][column] = '0'
                    dfsearch(row-1,column)
                    dfsearch(row+1,column)
                    dfsearch(row,column+1)
                    dfsearch(row,column-1)
            return  


        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':                                   # remember i and j are ints and the values in grid are strings
                    islands += 1
                    dfsearch(i,j)

        return islands

