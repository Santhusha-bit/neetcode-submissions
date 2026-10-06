class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if len(self.minArr) == 0:
            self.minArr.append(val)
        else:
            if val<=self.minArr[-1]:
                self.minArr.append(val)

    def pop(self) -> None:
        if len(self.arr) >= 1:
            item = self.arr.pop()
            if self.minArr[-1] == item:
                self.minArr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]
        

    def getMin(self) -> int:
        if len(self.minArr) > 0:
            return self.minArr[-1]


        
