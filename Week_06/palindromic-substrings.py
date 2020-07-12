class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            for j in range(2):
                left = i 
                right = i + j
                while left >= 0 and right < n and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
        return res
