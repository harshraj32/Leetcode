class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(string):
            
            i = 0
            j = len(string)- 1

            while(i<j):
                
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        for s in words:

            if isPalindrome(s):
                return s

        return ""
            