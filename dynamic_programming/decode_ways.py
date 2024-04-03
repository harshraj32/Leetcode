class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        if s == "":
            return 1

        dp[0] = 1
        dp[1] = 1 if s[0] is not "0" else 0

        for i in range(2, n + 1):
            oneDigit = int(s[i - 1])
            twoDigit = int(s[i - 2] + s[i - 1])

            if oneDigit >= 1:
                dp[i] += dp[i - 1]

            if twoDigit >= 10 and twoDigit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
