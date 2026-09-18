class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k=rowShift[i]
            newRow=[0]*n
            for j in range(n):
                newRow[(j-k+n)%n]=grid[i][j]
            grid[i]=newRow
        for j in range(n):
            k=colShift[j]
            newCol=[0]*n
            for i in range(n):
                newCol[(i-k+n)%n]=grid[i][j]
            for i in range(n):
                grid[i][j]=newCol[i]
        return grid