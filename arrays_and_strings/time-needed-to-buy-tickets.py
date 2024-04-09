class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        print(queue)
        time = 0
        while queue[k] > 0:
            time += 1
            if k == 0 and queue[k] - 1 == 0:
                break
            elif k == 0 and queue[k] - 1 > 0:
                k = len(queue) -1
                queue.append(queue.popleft() - 1)
            
            elif queue[0] - 1 == 0 and k != 0:
                queue.popleft()
                k -= 1
            elif queue[0] - 1 > 0 and k != 0:
                k -= 1
                queue.append(queue.popleft() - 1)

        return time  

                

            

        