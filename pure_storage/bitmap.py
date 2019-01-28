'''
# DFS method
'''
class Solution:
    def clear_bit(self, A, pos, length):
        if not A or pos < 0 or length <= 0:
            return
        n = len(A)
        for i in range(pos, min(pos+length, n)):
            # set itself = 0
            if A[i] == 0:
                continue
            A[i] = 0
            # set child to 0
            tmp = i
            while 2*tmp + 1 <= n:
                A[2*tmp+1] = 0
                tmp = 2*tmp + 1
            # set parent to 0
            while i > 0:
                if A[int((i-1)/2)] == 0:
                    break
                A[int((i - 1) / 2)] = 0
                i = int((i-1)//2)
    def set_bit(self, A, pos, length):
        if not A or pos < 0 or length <= 0:
            return
        n = len(A)
        for i in range(pos, min(2*pos+1, n, pos+length)):
            if A[i] == 1:
                continue
            A[i] = 1
            # set child
            self.set_bitdown(A, i, n)
            #set parent
            while i > 0:
                if (i % 2 == 0 and A[i-1] == 1) or (i%2 and A[i+1] == 1):
                    A[int((i-1)/2)] = 1
                i = int((i-1)/2)

    def set_bitdown(self, A, x, n):
        if x >= n:
            return
        if 2*x + 1 <= n and A[2*x+1] == 0:
            A[2*x+1] = 1
            self.set_bitdown(A, 2*x+1, n)
        if 2*x + 2 <= n and A[2*x+2] == 0:
            A[2*x+2] = 1
            self.set_bitdown(A, 2*x+2, n)


if __name__ == "__main__":
    s = Solution()
    A = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    print('before ', A)
    res = s.set_bit(A, 3, 1)
    print('after  ', A)
