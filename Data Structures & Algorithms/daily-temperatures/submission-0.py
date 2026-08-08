class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = deque()
        ans = [0]*len(temperatures)
        dq.append((temperatures[0], 0))
        for r in range(1, len(temperatures)):
            while dq:
                t, idx = dq[-1]
                if t<temperatures[r]:
                    dq.pop()
                    ans[idx] = r-idx
                else:
                    break
            dq.append((temperatures[r], r))
        return ans

