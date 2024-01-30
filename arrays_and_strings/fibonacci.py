

class Solution:

    def fibonacci(self, n ):

        if n <= 1:
            return 1
        
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)



if __name__ == "__main__":
    sol = Solution()
    print(sol.fibonacci(0))
    print(sol.fibonacci(1))
    print(sol.fibonacci(2))
    print(sol.fibonacci(-1))
    print(sol.fibonacci(100))


