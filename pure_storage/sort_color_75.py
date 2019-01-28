class Solution:
    def sortColor(self, nums):
        low, high = -1, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            elif nums[i] == 0:
                low += 1
                nums[low], nums[i] = nums[i], nums[low]
                i += 1
            else:
                i += 1
        print(nums)

if __name__ == "__main__":
    s = Solution()
    res = s.sortColor([2,0,1])
    print(res)