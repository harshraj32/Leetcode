
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for index, i in enumerate(intervals):
            start, end = i[0], i[1]
            
            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[index:]
            elif end < newInterval[0]:
                res.append(i)       
            else:
                newInterval[0] , newInterval[1] = min(start, newInterval[0]) , max(end, newInterval[1])

        res.append(newInterval)     

        return res