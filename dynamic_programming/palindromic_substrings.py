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

                
                
        