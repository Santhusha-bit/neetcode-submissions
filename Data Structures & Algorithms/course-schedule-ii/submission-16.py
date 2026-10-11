class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        classToPre = defaultdict(list)
        visit = set()
        classOrder = []

        for c, p in prerequisites:
            classToPre[c].append(p)

        visit = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False

            if c in visit:
                return True

            cycle.add(c)

            for p in classToPre[c]:
                if dfs(p) == False:
                    return False

            cycle.remove(c)
            visit.add(c)
            classOrder.append(c)
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return []
            
        return classOrder


        # classToPre = defaultdict(list)
        # visit = set()
        # classOrder = []

        # for c, p in prerequisites:
        #     classToPre[c].append(p)

        # def dfs(c):
        #     if c in visit:
        #         return False

        #     if classToPre[c] == []:
        #         if c not in classOrder:
        #             classOrder.append(c)
        #         return True

        #     visit.add(c)

        #     for p in classToPre[c]:
        #         if not dfs(p):
        #             return False
        #         elif p not in classOrder:
        #             classOrder.append(p)

        #     visit.remove(c)
        #     classToPre[c] = []
        #     return True

        # for n in range(numCourses):
        #     if not dfs(n):
        #         return []
        #     elif n not in classOrder:
        #         classOrder.append(n)
            
        # return classOrder
