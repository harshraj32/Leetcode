class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            
            if stack and t > stack[-1][1]:
                while stack and t > stack[-1][1] :
                    top = stack.pop()
                    
                    ans[top[0]] = i - top[0]
                    
            stack.append([i, t])
            
                
                




        return ans