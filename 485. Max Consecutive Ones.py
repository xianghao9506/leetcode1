class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        max = 0
        if len(nums)==1:
            return 1 if nums[0]==1 else 0
        if len(nums)== 2:
            num =nums.count(1)
            if num == 2:
                    return 2
            if num == 1:
                    return 1
            else: return 0
        for x in nums:
            if x == 1:
                temp += 1
                if temp > max:
                    max = temp
            else:
                if temp > max:
                    max = temp
                    temp = 0
                else:
                    temp = 0

        return max


