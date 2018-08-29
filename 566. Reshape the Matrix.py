class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])
        group = []
        for i in range(rows):
            for j in range(cols):
                group.append(nums[i][j])
        if rows * cols != r * c:
            return nums
        else:
            new_list = []
            for i in range(int(len(group) / c)):
                new_list.append(group[i * c:(i + 1) * c])

            return  new_list

