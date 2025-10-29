class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        provinces = 0

        def dfs(n):
            visited.add(n)
            for i, conn in enumerate(isConnected[n]):
                if conn == 1 and not i in visited:
                    dfs(i)



        for i in range(0, len(isConnected)):
            if not i in visited:
                dfs(i)
                provinces += 1
        
        return provinces
