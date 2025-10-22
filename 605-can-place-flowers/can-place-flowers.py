class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n == 0
        elif len(flowerbed) == 2:
            return (flowerbed[0] + flowerbed[1] == 0 and n <=1) or (flowerbed[0] + flowerbed[1] == 1 and n ==0)
        
        i = 0
        while i < len(flowerbed):

            if i - 1 < 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 1
            elif i+1 < len(flowerbed) and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 2
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 1
            else:
                i += 1
            if n == 0:
                return True
            
        
        return n <= 0
            
        





        