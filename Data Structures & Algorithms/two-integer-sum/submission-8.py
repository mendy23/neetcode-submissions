class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, x in enumerate(nums):
            if target - x not in store:
                store[x] = i
            else:
                return [store[target - x], i]