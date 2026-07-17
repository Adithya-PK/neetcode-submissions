class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        ans=(nums[0]*nums[1])-(nums[-1]*nums[-2])
        if ans < 0:
            ans = ans * -1
        return ans