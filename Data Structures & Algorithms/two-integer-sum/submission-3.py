class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, x in enumerate(nums):
            c = target - x
            if c in complements:
                return [complements[c], i]
            complements[x] = i
        return []
