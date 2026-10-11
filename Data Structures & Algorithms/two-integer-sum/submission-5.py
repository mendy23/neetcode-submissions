class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums): 
            c = target - x
            if c in complements:
                if i != complements[c]:
                    return [i, complements[c]]