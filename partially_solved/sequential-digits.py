class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:


        n = "123456789"
        ans = []
        
        l = len(str(low))
        h = len(str(high))

        for i in range(l, h+1):
            for j in range(9-i + 1):
                if(int(n[j:j+i]) >= low and int(n[j:j+i]) <= high):

                    ans.append(int(n[j:j+i]))




        return ans
        