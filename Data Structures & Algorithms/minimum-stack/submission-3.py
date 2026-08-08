class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.arr)>0:
            self.arr.append((val, min(self.arr[-1][1], val)))
        else:
            self.arr.append((val, val))


    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0] if self.arr else 0


    def getMin(self) -> int:
        return self.arr[-1][1] if self.arr else -1
