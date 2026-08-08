class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0]*length
        for r in range(length-1, -1, -1):
            if r+1<length:
                comp = r+1
                if temperatures[comp]>temperatures[r]:
                    ans[r] = 1
                else:
                    while ans[comp]!=0:
                        comp += ans[comp]
                        if temperatures[comp]>temperatures[r]:
                            ans[r] = comp-r
                            break
        return ans
