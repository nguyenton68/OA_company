class O1Set:
# add O(1)
# remove O(1)
# contain O(1)
# clear O(N)
# iterate O(N)
    def __init__(self, n):
        self.arr = [0]*(n+1)

    def push(self, val):
        self.arr[val] = 1

    def remove(self, val):
        if self.arr[val] == 0:
            return -1
        else:
            self.arr[val] = 0

    def contain(self, val):
        if self.arr[val] == 1:
            return True
        else:
            return False

    def clear(self):
        self.arr = [0]*(n+1)

    def iterate(self):
        res = [index for index, val in enumerate(self.arr) if val == 1]
        return res


class O1Set2:

    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def remove(self, val):
        self.arr.remove(val)

    def contain(self, val):
        if val in self.arr:
            return True
        else:
            return False

    def clear(self):
        self.arr = []

    def iterate(self):
        res = [i for i in self.arr]
        return res

class O1Set3:

    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.counter = 1

    def push(self, val):
        self.arr[val] = self.counter

    def remove(self, val):
        if self.arr[val] != self.counter:
            return -1
        else:
            self.arr[val] = 0
            return 1

    def contain(self, val):
        if self.arr[val] != self.counter:
            return -1
        else:
            return 1

    def clear(self):
        self.counter += 1

    def iterate(self):
        res = [index for index, val in enumerate(self.arr) if val == self.counter]
        return res


class O1Set4:
# Use 2 arrays: bucket and sequential array
# Add O(1)
# Remove O(1)
# Contain O(1)
# clear O(N)
# Iterate O(N):
    def __init__(self, n):
        self.n = n
        self.bucket = [-1]*(self.n + 1)
        self.arr = []
        self.cur_index = 0

    def push(self, val):
        # if val already in, update val
        if self.bucket[val] != -1:
            self.remove(val)
        self.arr.append(val)
        self.bucket[val] = self.cur_index
        self.cur_index += 1

    def remove(self, val):

        if self.cur_index == 0:
            return -1

        index = self.bucket[val]
        x = self.arr[-1]
        self.arr[index] = x
        self.arr.pop()
        self.bucket[val] = -1
        self.bucket[x] = index
        self.cur_index -= 1

    def contain(self, val):
        if self.bucket[val] != -1:
            return True
        else:
            return False

    def clear(self):
        self.bucket = [-1]*(self.n+1)
        self.arr = []

    def iterate(self):
        res = [i for i in self.arr]
        return res




s = O1Set4(5)
print(s.push(1))
print(s.push(5))
print(s.push(3))
print(s.push(3))
print(s.remove(3))
print(s.iterate())