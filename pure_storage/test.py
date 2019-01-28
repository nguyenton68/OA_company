class Solution:
    def count_square(self, p):
        p_set = set([tuple(i) for i in p])
        n = len(p)
        visited = set()
        ans = 0
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                new_points = self.get_2points(p[p1], p[p2], p_set)
                # [[point1], [point2]]
                #print(new_points)
                if new_points and tuple(new_points[0]) in p_set and tuple(new_points[1]) in p_set:
                    new_list = [tuple(i) for i in [p[p1], p[2], new_points[0], new_points[1]]]
                    new_list.sort()
                    if tuple(new_list) not in visited:
                        ans += 1
                        visited.add(tuple(new_list))
        return ans

    def get_2points(self, x1, x2, p_set):
        if x1 == x2:
            return None
        midX = (x1[0] + x2[0])//2
        midY = (x1[1] + x2[1])//2
        dx = x1[0] - midX
        dy = x1[1] - midY
        p1 = [midX + dx, midY - dy]
        p2 = [midX - dx, midY + dy]
        if tuple(p1) not in p_set or tuple(p2) not in p_set:
            return None
        if p1[0] + p2[0] != x1[0] + x2[0] or p1[1] + p2[1] != x1[1] + x2[1]:
            return None
        return [p1, p2]



if __name__=="__main__":
    s = Solution()
    p = [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1], [1,2], [0,0]]
    res = s.count_square(p)
    print(res)