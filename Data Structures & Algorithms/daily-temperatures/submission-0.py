class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                p = stack.pop()
                res[p] = t - p
            stack.append(t)

        return res