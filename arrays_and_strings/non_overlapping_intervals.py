class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        #sort
        l1 = sorted(intervals, key = lambda x:x[1])
        print(l1)
        #counting
        count = 0
        i = 0
        min1 = -math.inf

        for i in range(0, len(l1)):
            
            if l1[i][0] >= min1:
                min1 = l1[i][1]
                        
            else:
                count +=1
                    

        return count
            
