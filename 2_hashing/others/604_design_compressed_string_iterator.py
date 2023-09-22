import re

class StringIterator:

    def __init__(self, compressedString: str):
        self.counter_array = []
        for token in re.findall('\D\d+', compressedString):
            self.counter_array.append([token[0], int(token[1:])])
        self.current_idx = 0
        self.length = len(self.counter_array)

    def next(self) -> str:
        if not self.hasNext():
            return " "
        ans = self.counter_array[self.current_idx][0]
        self.counter_array[self.current_idx][1] -= 1
        if self.counter_array[self.current_idx][1] == 0:
            self.current_idx += 1
        return ans

    def hasNext(self) -> bool:
        if self.current_idx >= self.length:
            return False
        elif self.current_idx == self.length - 1:
            return self.counter_array[-1][1] > 0
        return True


if __name__ == '__main__':
    StringIterator("L111e22t1C1o1d1e11")