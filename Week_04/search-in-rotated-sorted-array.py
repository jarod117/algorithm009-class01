class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # print(f'left value: {left}')
            # print(f'right value: {right}')
            # print(f'mid value: {mid}')
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    # print('enter left sequence, in sequence, step #1')
                else:
                    left = mid + 1
                    # print('enter left sequence, out sequence, step #2')
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    # print('enter right sequence, out sequence, step #3')
                else:
                    right = mid - 1
                    # print('enter right sequence, in youxu, step #4')
        return left if nums[left] == target else -1
