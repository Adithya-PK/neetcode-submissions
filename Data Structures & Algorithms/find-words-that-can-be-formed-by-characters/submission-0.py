class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        ans = 0

        for i in chars:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i in words:
            dt = d.copy()     
            flag = True

            for j in i:
                if j in dt and dt[j] > 0:
                    dt[j] -= 1
                else:
                    flag = False
                    break

            if flag:
                ans += len(i)

        return ans