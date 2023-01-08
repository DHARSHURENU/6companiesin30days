class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for i, j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        
        st = [i for i in range(numCourses) if indegree[i] == 0]
        queue = deque(st)
        cnt = 0
        while queue:
            i = queue.popleft()
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
            cnt += 1
        return cnt == numCourses
