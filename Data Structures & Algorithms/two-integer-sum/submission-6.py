class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempHash = {}

        for i in range(len(nums)):
            if nums[i] in tempHash:
                return [tempHash[nums[i]], i]
            difference = target - nums[i] 
            tempHash[difference] = i