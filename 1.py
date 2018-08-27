class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """







list = [[0,1,0],[1,1,0],[0,0,1],[1,1,0]]
#for row in list:
    #row.reverse()

rows = len(list)
cols = len(list[0])
for row in range(rows):
    list[row] = list[row][::-1]
    for col in range(cols):
        list[row][col] ^= 1
print(list)

