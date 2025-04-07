class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s = ''
        def palindrome(s,i,j):
            nonlocal max_s
            temp_s = ''
      
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    temp_s = s[i:j+1]
                    if len(temp_s) > len(max_s):
                        max_s = temp_s
                    i -= 1
                    j += 1
                else:
                    return

                     
        
        res = ''
        for i in range(len(s)):
            
            #for odd
            palindrome(s,i,i)

            #for even
            palindrome(s,i, i+1)
        
        return max_s




        