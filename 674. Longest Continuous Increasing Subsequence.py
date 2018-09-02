class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_l = 1
        count = 1
        n = len(nums)

        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                max_l = max(max_l, count)
                count = 1
        return (max(max_l, count))



nums = [2,2,2,2,2]
max_l = 1
count = 1
n = len(nums)


for i in range(n-1):
    if nums[i+1] > nums[i]:
        count+=1
    else:
        max_l = max(max_l ,count)
        count = 1

print(max(max_l,count))