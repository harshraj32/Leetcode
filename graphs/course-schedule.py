class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hashmap = {i: [] for i in range(numCourses)}
        visited = set()

        def dfs(i, nums):

            if i in visited:
                return False

            if not nums:
                return True

            visited.add(i)
            for num in nums:
                if not dfs(num, hashmap[num]):
                    return False

            visited.remove(i)
            hashmap[i] = []

            return True

        for i in prerequisites:
            if i[0] not in hashmap:
                hashmap[i[0]] = list()

            hashmap[i[0]].append(i[1])

        for i in range(numCourses):

            if not dfs(i, hashmap[i]):
                return False

        return True
