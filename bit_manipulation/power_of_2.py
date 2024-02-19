class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        return n > 0 and (n & (n-1)) == 0
    

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        return int(log2(n)) == log2(n)