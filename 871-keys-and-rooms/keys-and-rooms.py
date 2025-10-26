class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(node):
            visited.add(node)

            for n in rooms[node]:
                if n not in visited:
                    dfs(n)
        
        dfs(0)


        return len(visited) == len(rooms)

        