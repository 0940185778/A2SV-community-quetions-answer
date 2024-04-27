class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        operations = n - 1

        for i in range(operations):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

   
        zeroes_count = nums.count(0)
        non_zeroes = [num for num in nums if num != 0]
        result = non_zeroes + [0] * zeroes_count

        return result
