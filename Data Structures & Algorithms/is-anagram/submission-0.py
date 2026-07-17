class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans=sorted(s)==sorted(t)
        return ans