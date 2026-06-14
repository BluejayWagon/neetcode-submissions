class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        tempHash = {}
        for i in range(len(nums)):
            if tempHash and nums[i] in tempHash:
                return [tempHash[nums[i]], i]
            tempHash[target - nums[i]] = i
        
