class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0: return True

        i = 0
        while i < len(flowerbed):

            left_ok = (i == 0) or (flowerbed[i-1] == 0)
            right_ok = (i + 1 == len(flowerbed)) or flowerbed[i+1] == 0
            # print(flowerbed, n, i, left_ok, right_ok, (flowerbed[i] == 0) )
            if left_ok and (flowerbed[i] == 0) and right_ok:
                flowerbed[i] = 1
                i += 2
                n -= 1
                
            else:
                i += 1
            
            if n == 0:
                return True
            
            
            
        
        return n <= 0
            
        





        