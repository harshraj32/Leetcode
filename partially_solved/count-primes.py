class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [0]*(n+1)
        def isPrime(n):
            if n < 2:
                return False

            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        for i in range(2,n+1):
            if isPrime(i): 
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        return dp[n-1]
        