学习笔记

二分查找

前提条件：
1. 目标函数有序，即具有单调性（单调递增或者递减）
2. 存在上下界
3. 能够通过索引访问，即能够通过索引下标访问

left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
   elif array[mid] < target:
        left = mid + 1
    else:
        right = mid + 1
