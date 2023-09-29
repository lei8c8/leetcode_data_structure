class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> list[str]:
        idKey -= 1
        self.arr[idKey] = value
        if self.ptr < idKey:
            return []
        ans = []
        while self.ptr < len(self.arr) and self.arr[self.ptr]:
            ans.append(self.arr[self.ptr])
            self.ptr += 1
        return ans