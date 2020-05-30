# python字典（哈希）
# 1. 统计数组中每个元素出现的次数；
# 2. 对字典进行排序；
# 2. 返回出现频率前k高的元素；
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dicts = collections.defaultdict(int)
#         # dicts = collections.Counter(nums)
#         res = []
#         for i in nums:
#             dicts[i] += 1
#         print(dicts)
#         dicts_new = sorted(dicts.items(), key = lambda x: x[1], reverse = True)
#         print(dicts_new)
#         for key, value in dicts_new:
#             print(key)
#             res.append(key)
#         return res[:k]

# python堆实现
# 1. 统计数组中所有元素的出现次数；
# 2. 使用堆对数据进行处理，即可得到按从小到大的顺序的数组
# 3. 返回出现频率前k高的元素；
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq as hq

        dicts = collections.Counter(nums)
        return hq.nlargest(k, dicts.keys(), key = dicts.get)
