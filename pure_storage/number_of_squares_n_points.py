class Solution:
    def count_squareO4(self, points):
        #given: list[list]
        # O(n^4) solution
        n = len(points)
        ans = 0
        for p1 in range(n):
            for p2 in range(p1+1, n):
                for p3 in range(p2+1, n):
                    for p4 in range(p3+1, n):
                        if self.isValidSquare( points[p1], points[p2], points[p3], points[p4]):
                            ans += 1
        return ans
# [0 0 1 0 1 1 1 0
#  1 0 1
    def count_squareO3(self, points):
        # O(N^3)
        ps = set([tuple(p) for p in points])
        n = len(points)
        ans = 0
        visited = set()
        for p1 in range(n):
            for p2 in range(p1+1, n):
                for p3 in range(p2+1, n):
                    new_point = self.get_4th_point(points[p1], points[p2], points[p3])
                    if new_point and tuple(new_point) in ps:

                        tmp = set([tuple(p) for p in [points[p1], points[p2], points[p3], new_point]])
                        if len(tmp) != 4:
                            continue
                        res = [tuple(p) for p in [points[p1], points[p2], points[p3], new_point]]
                        res.sort()

                        if tuple(res) not in visited:
                            visited.add(tuple(res))
                            ans += 1
        print(visited)
        return ans

    def get_4th_point(self, p1, p2, p3):
        #check which one is the 90 deg
        if self.is_90deg(p2, p1, p3):
            if self.getDist(p1, p2) == self.getDist(p3, p2):  # square
                return [p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1]]
        elif self.is_90deg(p3, p2, p1):
            if getDist(p1, p3) == getDist(p3, p2):
                return [p1[0] - p3[0] + p2[0], p1[1] - p3[1] + p2[1]]
        elif self.is_90deg(p1, p2, p3):
            if getDist(p1, p2) == getDist(p3, p1):
                return [-p1[0] + p3[0] + p2[0], -p1[1] + p3[1] + p2[1]]
        else:
            return None

    def is_90deg(self, A, B, C): #A^ = 90 deg
        if (B[1] - A[1]) * (C[1] - A[1]) + (B[0] - A[0]) * (C[0] - A[0]) == 0:
            return True
# A------B AB=BD=AC=CD and AD = CB
# |
# |   x
# |
# C------D
# follow up is given n points and find how many squares
    def isValidSquare(self, p1, p2, p3, p4):
        def d(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2

        if ((d(p1,p2)==d(p2,p3)==d(p3,p4)==d(p1,p4)) and (d(p1,p3)==d(p2,p4))) or \
                ((d(p1,p2) == d(p2,p4) == d(p3,p4) == d(p1,p3)) and (d(p1,p4) == d(p2,p3))) or \
                ((d(p1,p3) == d(p2,p3) == d(p2,p4) == d(p1,p4)) and (d(p1,p2) == d(p3,p4))):
            return True
        return False

    def count_squareO2(self, p):
        p_set = set([tuple(i) for i in p])
        n = len(p)
        visited = set()
        ans = 0
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                new_points = self.get_2points(p[p1], p[p2], p_set)
                #print(new_points)
                if new_points and tuple(new_points[0]) in p_set and tuple(new_points[1]) in p_set:
                    new_list = [tuple(i) for i in [p[p1], p[p2], new_points[0], new_points[1]]]
                    new_list.sort()
                    #print(new_list)
                    if tuple(new_list) not in visited:
                        visited.add(tuple(new_list))
                        ans += 1
        print(visited)
        return ans

    def get_2points(self, A, B, p_set):
        midX = float((A[0] + B[0])/2)
        midY = float((A[1] + B[1])/2)

        dx =  midX - A[0]
        dy =  midY - A[1]
        pnt3 = [int(midX - dx), int(midY + dy)]
        pnt4 = [int(midX + dx), int(midY - dy)]
        if pnt3 == pnt4:
            return None
        if A[0] + B[0] != pnt3[0] + pnt4[0] or A[1] + B[1] != pnt3[1] + pnt4[1]:
            return None
        return [pnt3, pnt4]

if __name__=="__main__":
    s = Solution()
    p = [[0,0], [0,1], [1,0], [1,1]]
    res = s.count_squareO2(p)
    print(res)