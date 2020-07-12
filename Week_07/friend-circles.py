class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        le = len(M)
        count = 0
        visited = set()
        
        def dfs(i):
            for j in range(le):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(le):
            if  i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count
