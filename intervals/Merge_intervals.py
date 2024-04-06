class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:

            start, end = i[0], i[1]

            if not stack:
                stack.append(i)

            if start > stack[-1][1]:
                stack.append(i)

            elif stack[-1][1] >= start:
                old_start, old_end = stack.pop()
                stack.append([min(old_start, start), max(old_end, end)])

        return stack
