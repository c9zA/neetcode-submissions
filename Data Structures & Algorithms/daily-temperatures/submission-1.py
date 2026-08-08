class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = deque()
        ans = [0]*len(temperatures)
        for r in range(len(temperatures)):
            while dq and dq[-1][0]<temperatures[r]:
                t, idx = dq[-1]
                dq.pop()
                ans[idx] = r-idx
            dq.append((temperatures[r], r))
        return ans

