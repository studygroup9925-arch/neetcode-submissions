class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        repeated=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    repeated=grid[i][j]
                seen.add(grid[i][j])
        for i in range(1,n*n+1):
            if i not in seen:
                return [repeated,i]
        return [-1,-1]