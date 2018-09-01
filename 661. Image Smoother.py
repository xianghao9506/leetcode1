class Solution:
    def imageSmoother(self, M):
        dirs, lrc = [(x, y) for x in range(-1,2) for y in range(-1,2)], [len(M), len(M[0])]
        ans = [[0]* lrc[1] for _ in range(lrc[0])]
        def sum2(i, j):
            ans, count = 0, 0
            for c1, c2 in dirs:
                nr, nc = i + c1, j + c2
                if 0 <= nr < lrc[0]  and 0 <= nc < lrc[1]:
                    count += 1
                    ans += M[nr][nc]
            return ans//count
        for i in range(lrc[0]):
            for j in range(lrc[1]):
                ans[i][j] = sum2(i,j)
        return ans