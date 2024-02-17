class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        print("heap at first: ", heap)
        for i in range(len(heights) - 1):

            diff = heights[i+1] - heights[i]
            print("diff: ",diff)
            if diff > 0 :
                heapq.heappush(heap,diff)
                print("heap before ladders: ", heapq)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    print("heap after ladders: ", heapq)
                if bricks < 0:
                    return i 
        return len(heights) - 1 