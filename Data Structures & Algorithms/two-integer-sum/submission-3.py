class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempHash = {}
        for i in range(len(nums)):
            num = nums[i]
            key = target - num
            if num in tempHash:
                return [tempHash[num],i]
            tempHash[key] = i