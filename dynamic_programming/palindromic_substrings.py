#brute force

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        def ispanlindrome(s):
            i = 0 
            j = len(s) -1
            while(i<j):
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(n):
            temp_str = ''
            for j in range(i,n):
                temp_str += s[j]
                
                if ispanlindrome(temp_str):
                    count += 1
        return count

                
                
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def count_palindrome(s,i,j):
            nonlocal res
            temp_s = ''
            while i >= 0 and j < len(s):

                if s[i] == s[j]:
                    temp_s = s[i:j+1]
                    res.append(temp_s)
                    i -= 1
                    j += 1
                
                else:
                    return
        
        for i in range(len(s)):

            count_palindrome(s,i,i)
            count_palindrome(s,i,i+1)
        
        return len(res)


                
