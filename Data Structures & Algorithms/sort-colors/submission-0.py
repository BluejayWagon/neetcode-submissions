class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucketArr = [0,0,0]
        for num in nums:
            bucketArr[num] += 1
        
        i = 0
        for n in range(len(bucketArr)):
            for j in range(0, bucketArr[n]):
                nums[i] = n
                i += 1
        
