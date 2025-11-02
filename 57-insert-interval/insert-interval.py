class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        newStart,newEnd = newInterval[0],newInterval[1]
        i = 0
        res = []

        while i < len(intervals) and newStart > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and newEnd >= intervals[i][0]:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1

        res.append([newStart, newEnd])

        while i < len(intervals):
            res.append(intervals[i])
            print('3')
            i += 1

        return res
            
                

            


        