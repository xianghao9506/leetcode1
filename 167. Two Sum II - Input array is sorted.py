class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(numbers):
            if (target - num) in num_dict:
                return [num_dict[target - num], i + 1]
            num_dict[num] = i + 1

"""
numbers = [2,7,11,15]
target = 9

for x in numbers:
    if (target - x) in numbers[numbers.index(x) + 1:]:
        print(numbers.index(x)+1, (numbers[numbers.index(x)+1:].index(target-x))+2)
        break

"""