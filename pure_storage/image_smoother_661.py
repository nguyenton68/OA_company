class Solution:
    def imgSmoother(self, M):
        row, col = len(M), len(M[0])
        def calc(r, c):
            count = tot_sum = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    nxt_row = r + i
                    nxt_col = c + j
                    if 0 <= nxt_row < row and 0 <= nxt_col < col:
                        count += 1
                        # 0xff = 11111111 represent 8 bits
                        tot_sum += M[nxt_row][nxt_col] & 0xff
            return tot_sum//count

        for i in range(row):
            for j in range(col):
                M[i][j] = M[i][j] | calc(i,j) << 8

        for i in range(row):
            for j in range(col):
                M[i][j] = M[i][j] >> 8
        return M

if __name__ == "__main__":
    s = Solution()
    res = s.imgSmoother([[2, 0, 3, 5, 4],\
                         [1, 3, 2, 1, 0],\
                         [0, 0, 1, 1, 1],\
                         [9, 7, 5, 2, 0]])
    for i in range(len(res)):
        print(res[i])