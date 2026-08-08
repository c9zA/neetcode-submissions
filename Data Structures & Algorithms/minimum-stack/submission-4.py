class MinStack:

    def __init__(self):
        self.arr = []
        self.curMin = 0

    def push(self, val: int) -> None:
        if len(self.arr)==0:
            self.curMin = val
        self.arr.append(val-self.curMin)
        if self.curMin-val>0:
            self.curMin = val

    def pop(self) -> None:
        if self.arr:
            if self.arr[-1]<0:
                self.curMin -= self.arr[-1]
            self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]+self.curMin if self.arr and self.arr[-1]>0 else self.curMin


    def getMin(self) -> int:
        return self.curMin if self.arr else -1
