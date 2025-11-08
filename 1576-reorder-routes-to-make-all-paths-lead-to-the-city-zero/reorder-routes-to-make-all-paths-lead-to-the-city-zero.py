class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        neighbors = {}
        connection = set()

        for u, v in connections:
            neighbors.setdefault(u,[]).append(v)
            neighbors.setdefault(v,[]).append(u)
            connection.add((u,v))


        q = deque([0])
        visited = [False]*n
        reverses = 0
        visited[0] = True

        while q:

            node = q.popleft()

            for v in neighbors[node]:
                if not visited[v]:
                    print(node,v)
                    visited[v] = True
                    
                    if (v,node) not in connection:
                        reverses += 1
                        connection.add((v,node))
                    q.append(v)
        
        return reverses

            