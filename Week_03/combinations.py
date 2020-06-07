class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, k, temp):
            if k == 0:
                res.append(temp)
            for j in range(i, n + 1):
                backtrack(j + 1, k - 1, temp + [j])

	backtrack(1, k, [])

        return res