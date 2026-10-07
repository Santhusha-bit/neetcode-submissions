class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                area = h * abs(i - index)
                maxArea = max(area, maxArea)
                start = index 
            stack.append((start, heights[i]))

        for i, h in stack:
            maxArea = max(maxArea, h *(len(heights)-i))

        return maxArea           