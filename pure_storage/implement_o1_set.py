class my_set:
    def __init__(self, n):
        self.n = n
        self.counter = 1
        self.arr = [0]*(n+1)

    def insert(self, val):
        #if the value already in set, return False
        if val < 1 or val > self.n or self.arr[val] == self.counter:
            return
        self.arr[val] = self.counter

    def remove(self, val):
        if val < 1 or val > self.n or self.arr[val] == 0:
            return
        self.arr[val] = 0

    def contain(self, val):
        if val < 1 or val > self.n:
            return False
        return self.arr[val] == self.counter

    def clear(self):
        self.counter += 1

    def iterate(self):
        res = [i for i in self.arr if self.arr[i] == self.counter]
        return res


class my_setv2:
    def __init__(self, n):
        self.arr = []

    def insert(self, val):
        if val in self.arr:
            return
        self.arr.append(val)

    def remove(self, val):
        self.arr.remove(val)

    def contain(self, val):
        return True if val in self.arr else False

    def clear(self):
        self.arr = []




if __name__ == "__main__":
    s = my_set(6)
    s.insert(3)
    s.insert(2)
    s.insert(7)
    print(s.contain(3))
