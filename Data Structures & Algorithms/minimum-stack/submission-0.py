class MinStack:

    def __init__(self):
        self.arr = []
        self.small = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.small or (self.small and self.small[-1]>=val):
            self.small.append(val)


    def pop(self) -> None:
        if self.arr:
            temp = self.arr.pop()
            if self.small and temp == self.small[-1]:
                self.small.pop()
                


    def top(self) -> int:
        return self.arr[-1] if self.arr else 0


    def getMin(self) -> int:
        return self.small[-1] if self.small else -1
