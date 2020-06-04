class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

#1. 遍历数组
#   先将一个值存入一个变量
#   然后将另外的值，存入另一个变量
#   累加尝试，是否两数之和等于目标值

        # lis = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             print('num i: ', nums[i])
        #             print('num j: ', nums[j])
        #             if target == nums[i] + nums[j]:
        #                 lis.append(i)
        #                 lis.append(j)
        #                 return lis


        # lis = []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             lis.append(i)
        #             lis.append(j)
        #             return lis

#   用单层循环，判断target - nums[i]是否在数组里
        # lis = []
        # for i in range(len(nums) - 1):
        #     temp = target - nums[i]
        #     if temp in nums[i + 1:]:
        #         j = nums.index(temp, i + 1)
        #         lis.append(i)
        #         lis.append(j)
        #         return lis

#2. 哈希
#   将数组元素放到一个字典里
#   将数组的元素存储为键值，下表存储为值

        dict = {}

        for i, num in enumerate(nums):
            dict[num] = i

        for i in range(len(nums)):
            temp = target - nums[i]
            if dict.get(temp) and i != dict.get(temp):
                return i, dict.get(temp)
