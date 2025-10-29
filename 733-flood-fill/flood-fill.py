class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        
        oldColor = image[sr][sc]
        q = deque([[sr,sc]])
        m,n = len(image),len(image[0])

        image[sr][sc] = color

        while q:
            print(q)
            r,c = q.popleft()

            checks = [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]

            for rc,cc in checks:
                if rc >= 0 and rc < m and cc >= 0 and cc < n and image[rc][cc] == oldColor:
                    image[rc][cc] = color

                    q.append((rc,cc))
        
        return image




        