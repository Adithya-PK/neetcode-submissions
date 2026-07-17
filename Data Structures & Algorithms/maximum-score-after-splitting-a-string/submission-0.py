class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ls = s[:i]
            rs = s[i:]
            z = ls.count("0")
            o = rs.count("1")
            score = z + o
            ans = max(ans, score)
        return ans