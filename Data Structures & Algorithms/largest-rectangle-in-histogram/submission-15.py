class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lrStack = [0]
        rlStack = [n-1]
        lr = [-1]
        rl = [n]*len(heights)
        for i in range(1, n):
            while lrStack and heights[i]<=heights[lrStack[-1]]:
                lrStack.pop()
            if lrStack:
                lr.append(lrStack[-1])
            else:
                lr.append(-1)
            lrStack.append(i)
               
            # if heights[i]>=heights[lrStack[-1]]:
            #     if heights[i]==heights[lrStack[-1]]:
            #         lrStack.pop()
            #     lr.append(lrStack[-1]) if lrStack else lr.append(-1)
            #     lrStack.append(i)
            # else:
            #     lrStack.pop()
            #     while lrStack:
            #         if heights[i]>heights[lrStack[-1]]:
            #             lr.append(lrStack[-1])
            #             lrStack.append(i)
            #             break
            #         lrStack.pop()
            #     if not lrStack:
            #         lr.append(-1)
            #         lrStack.append(i)

            if heights[-1-i]>=heights[rlStack[-1]]:
                if heights[-i-1]==heights[rlStack[-1]]:
                    rlStack.pop()
                rl[-i-1] = rlStack[-1] if rlStack else n
                rlStack.append(n-i-1)
            else:
                rlStack.pop()
                while rlStack:
                    if heights[-i-1]>heights[rlStack[-1]]:
                        rl[-i-1] = rlStack[-1]
                        rlStack.append(n-i-1)
                        break
                    rlStack.pop()
                if not rlStack:
                    rl[-i-1] = n
                    rlStack.append(n-i-1)
        print(lr)
        print(rl)
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i]*(rl[i]-lr[i]-1))
        return ans
                    

