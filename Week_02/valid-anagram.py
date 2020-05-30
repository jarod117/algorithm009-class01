# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         if sorted(s) != sorted(t):
#             return False
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = collections.defaultdict(int)
        for i in s:
            dict[i] += 1
        for i in t:
            dict[i] -= 1
        for val in dict.values():
            if val:
                return False
        return True