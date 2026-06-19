class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCount = [0,0,0]

        for num in nums:
            colorCount[num] += 1

        i = 0
        for n in range(len(colorCount)):
            for j in range(colorCount[n]):
                nums[i] = n
                i += 1
        