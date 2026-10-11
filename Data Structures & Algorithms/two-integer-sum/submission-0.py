class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if j != i and nums[i] + nums[j] == target:
                    return sorted((i, j))