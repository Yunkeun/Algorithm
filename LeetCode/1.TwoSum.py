class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLength = len(nums)
        for i in range(numsLength):
            for j in range(i+1, numsLength):
                twoSumValue = nums[i] + nums[j]
                if twoSumValue == target:
                    return [i, j]
        