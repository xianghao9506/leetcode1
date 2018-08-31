class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setn = set(nums)
        if len(nums) == len(setn):
            return  False
        else:
            return  True
