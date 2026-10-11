class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classToReq = defaultdict(list)
        visit = set()

        for c, r in prerequisites:
            classToReq[c].append(r)

        def dfs(c):
            if c in visit:
                return False

            if classToReq[c] == []:
                return True

            visit.add(c)
            for r in classToReq[c]:
                if not dfs(r):
                    return False

            visit.remove(c)
            classToReq[c] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True        
        