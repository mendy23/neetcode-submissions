class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexOf = sorted((x, idx) for idx, x in enumerate(nums))
        i, j = 0, len(nums) - 1

        while i != j:
            sum = indexOf[i][0] + indexOf[j][0]
            if sum == target:
                return sorted((indexOf[i][1], indexOf[j][1]))
            elif sum < target:
                i += 1
            else:
                j -= 1
