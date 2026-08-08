class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSp = []
        count = 0
        length = len(position)
        for i in range(length):
            posSp.append((position[i], speed[i]))
        posSp.sort()
        maxT = -float('inf')
        for i in range(length-1, -1, -1):
            pos, sp = posSp[i]
            curT = (target-pos)/sp
            if curT>maxT:
                count += 1
                maxT = curT
        return count
                

        