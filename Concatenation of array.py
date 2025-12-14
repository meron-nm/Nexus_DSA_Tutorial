class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums) # x=nums.extend(nums returns none!!!!!)
        return nums
nums=[2,3,4,5]
print(Solution().getConcatenation(nums))
