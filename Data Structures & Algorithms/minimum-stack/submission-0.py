class MinStack:

    def __init__(self):
        self.val : list = []

    def push(self, val: int) -> None:
        if val.is_integer:
            self.val.append(val)
        else:
            self.val.append(None)
    def pop(self) -> None:
        self.val.pop(-1)

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return sorted(self.val)[0]
        
