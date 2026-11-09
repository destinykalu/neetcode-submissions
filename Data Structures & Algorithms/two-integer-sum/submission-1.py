class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {} 

        for i, val in enumerate(nums):
            difference = target - val

            if difference in prevNums:
                return [prevNums[difference], i]
            prevNums[val] = i