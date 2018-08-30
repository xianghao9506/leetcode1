class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rows = len(nums)
        seta = set(nums)  # [1,2]
        for i in seta:
            if nums.count(i) > (rows / 2):
                return i


