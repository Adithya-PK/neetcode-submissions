class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        c=0
        while l < len(nums):
            if r==l:
                l+=1
                r=len(nums)-1
                continue
            if nums[l] == nums[r]:
                c+=1
            r-=1
        return c
