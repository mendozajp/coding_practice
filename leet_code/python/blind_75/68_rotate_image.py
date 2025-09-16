"""
https://neetcode.io/problems/rotate-matrix?list=blind75
first couple times I looked at this I had no idea. Matrix movements are strange, hard to keep track
of. Was looking at the solution, it makes sense but I was not sure how people actually got to it.
After thinging about it for a while I got to this solution:
So if you want to swap the values of a matrix in place, you want to be swapping 2 values at the 
same time and they should be with each other. Im sure there is a way to not need to do that, 
but being able to do that makes it a lot easier since thats just 1 nested loop starting from
your outer loop. by that I mean, i=0, j=i, then just swap the 2 values corresponding to both
combinations 00, then increment j until len, 01 -> 10 and backwards.
Code wise this is very easy to do, but the matrix is not in a configuration where if we did 
that we would get to a solution. So can we get to look like something were that would work?

there I looked at the target matrix, which looks like this
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
Then swapped all its values with their inverse, 1,0 -> 0,1 and vise versa. Ends up like this
[7, 8, 9]
[4, 5, 6]
[1, 2, 3]
Crazy enough thats just the list of lists reversed, so we can get it in this best case state
with a simple matrix.reverse()

And then you loop and swap and your done.
I doubt a similar strategy will work with anything more complicated. But might be worth
working backwards from the solution to see if you end up seeing anything. 

Here is that solution. The actual solution does i+1 to avoid the diagonal but I didnt have it
to check if it worked and it did so I'll just keep that one to show that I actually get it now.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for i in range(0, len(matrix[0])):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]wsl