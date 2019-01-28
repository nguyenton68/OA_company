import heapq
class Solution:
    def get_skyline2(self, buildings):
        points = sorted([i for b in buildings for i in [b[0], b[1]]])
        res = []
        i = 0
        heap = []
        for pt in points:

            #leave old tall building
            while heap and heap[0][1] <= pt:
                heapq.heappop(heap)

            #is it new building
            # while loop here
            while i < len(buildings) and buildings[i][0] == pt:
                heapq.heappush(heap,(-buildings[i][2], buildings[i][1])) #height and ypos
                i += 1
            height = -heap[0][0] if heap else 0

            #append new tallest building into result
            if not res or height != res[-1][1]:
                res.append([pt, height])
        return res


if __name__ == "__main__":
    s = Solution()

    buildings = [[2,9,10], [3,7,15], [5,12,12], [15,20,20], [19,24,8]]
    res = s.get_skyline2(buildings)
    print(res)