class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numslength = len(nums)
        counter = 0
        max = 0
        for i in range(numslength):
            if nums[i] == 1:
                counter = counter + 1
                if counter > max:
                    max = counter
            else:
                counter = 0
        return max