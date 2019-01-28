class Solution:
    def valid_square(self, p1, p2, p3, p4):
        p = [p1, p2, p3, p4]
        print(p)
        #points.sort(key=lambda x: (x[0], x[1]))
        p = sorted(p, key=lambda x: (x[0], x[1]))
        if self.d(p[0], p[1]) == self.d(p[0],p[2]) == self.d(p[1],p[3]) == self.d(p[2],p[3]):
            if self.d(p[0],p[3]) == self.d(p[1],p[2]):
                return True
            return False
        return False

    def d(self, x, y):
        return (x[0] - y[0])**2 + (x[1] - y[1])**2

if __name__ == "__main__":
    s = Solution()
    res = s.valid_square([0,0],[1,0],[0,1],[1,1])
    print(res)