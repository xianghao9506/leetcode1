class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for x in nums:
                if x == 0:
                    nums.append(x)
                    nums.remove(x)



nums = [0,1,0,3,12]

for x in nums:
    if nums[nums.index(x):]== 0:
        break
    else:
        if x == 0:
            nums.append(x)
            nums.remove(x)
print(nums)
"""
class Solution:
    def moveZeroes(self, nums):
        
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        
        start = 0
        for num in nums:
            if num != 0:
                nums[start] = num
                start += 1
        nums[start:] = [0] * (len(nums) - start)
        
"""