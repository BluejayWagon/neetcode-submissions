class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter = 0
            else:
                counter += 1
                result = max(result, counter)
        return result