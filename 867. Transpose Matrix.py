#小角标对换  考虑到行列不一样相等：要建立新的矩阵，再把原矩阵的行列复制给新矩阵的列行

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        new_list = [([0] * rows) for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                new_list[j][i] = A[i][j]

        return new_list

