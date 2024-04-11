class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = nums + nums
        return ans
nums = [1, 2, 1]
print(getConcatenation(nums)) 