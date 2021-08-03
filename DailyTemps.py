class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack):
                ans[i] = stack[-1] - i
            stack.append(i)
            
        return ans