class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #I know this isn't probably the expected answer
        #but python does this with its builtin libraries
        ans = nums + nums
        return ans