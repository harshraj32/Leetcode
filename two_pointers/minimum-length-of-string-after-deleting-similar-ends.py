class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n - 1
        count = 0
        while i < j:

            if s[i] != s[j]:
                return n - count

            elif s[i] == s[i + 1] and i + 1 < j:
                i += 1
                count += 1

            elif s[j] == s[j - 1] and j - 1 > i:
                j -= 1
                count += 1

            else:
                i += 1
                j -= 1
                count += 2

        return n - count
