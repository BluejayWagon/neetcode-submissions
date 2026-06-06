class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempArr = []
        for i in nums:
            if i in tempArr:
                return True
            tempArr.append(i)
        return False