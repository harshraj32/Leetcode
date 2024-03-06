class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        # doing face up from front and face down from bottom
        tokens = sorted(tokens)
        i = 0
        j = len(tokens) - 1
        score = 0
        max1 = 0
        while i <= j:
            if power >= tokens[i]:
                # print("face up")
                score += 1
                power -= tokens[i]
                i += 1
                max1 = max(max1, score)

            elif score > 0:
                # print("face down")
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break

        return max1
