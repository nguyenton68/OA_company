class Solution:
    def draw_circle(self, r2):
        x = 1
        y = 0
        res = set()
        while x*x <= r2:
            for y in range(x+1):
                if x*x + y*y == r2:
                    res.update({(x,y),(x,-y),(-x,-y),(y,x), (y,-x)})
            x += 1
        print(res)

# 633 leetcode
#binary search
    def draw_circle2(self, r2):
        x = 1
        ans = set()
        while x*x <= r2:
            low = 0
            high = x
            while low <= high:
                mid = low +(high-low)//2
                if x*x + mid*mid == r2:
                    ans.update({(x,mid), (x,-mid), (-x, mid), (-x, -mid), (mid,x), (mid,-x), (-mid,-x),(-mid,x)})
                    break
                elif x*x + mid*mid > r2:
                    high = mid - 1
                else:
                    low = mid + 1
            x += 1
        return ans

    def draw_circle_Bresenham(self, r2):
        x = 0
        y = int((r2)**0.5)
        d = 3 - 2*y
        res = set()
        while x < y:
            res.update({(x,y),(x,-y),(-x,-y),(-x,y),(y,x),(y,-x),(-y,-x),(-y,x)})
            if d <= 0:
                d = d + 4*x - 6
            else:
                y -= 1
                d = d + 4*x - 4*y + 10
            x += 1
        print(res)
        return len(res)



if __name__ == "__main__":
    s = Solution()
    res = s.draw_circle_Bresenham(4)
    print(res)