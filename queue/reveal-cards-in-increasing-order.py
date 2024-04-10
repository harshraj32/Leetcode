class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)

        queue = deque([x for x in range(n)])
        deck.sort()
        ans = [0] * n
        print(deck)
        for i in range(n):
            print(queue)
            ind = queue.popleft()
            if queue:
                queue.append(queue.popleft())

            ans[ind] = deck[i]
        return ans
