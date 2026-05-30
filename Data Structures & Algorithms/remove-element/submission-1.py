class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == val:
                if i != len(nums) - 1:
                    while nums[i] == val:
                        counter += 1
                        for j in range(i,len(nums)):
                            if j != len(nums) - 1 :
                                newindex = j + 1
                                nums[j] = nums[newindex]
                            else:
                                nums[j] = None
                else:
                    counter += 1
                    nums[i] = None
        k = len(nums) - counter
        return k