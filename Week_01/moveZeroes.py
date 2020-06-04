class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

#1. 数组
# '''
# 统计零元素个数，然后将非零元素放到数组的前面
# '''
        # count = 0
        # new_nums = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
        # print(count)
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         print("i value", i, "num value: ", nums[i])
        #         new_nums.append(nums[i])
        # j = 0
        # while j < count:
        #     new_nums.append(0)
        #     j += 1
        # print("new nums: ", new_nums)
        # nums = new_nums
        # return nums

#2. 双指针
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        
        return nums
