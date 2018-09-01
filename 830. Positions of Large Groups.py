class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
#对于每个字母 输出个数
# 判断个数大于等于3
# 输出该类字母的index和 index+ 个数


# 统计

S = "aaa"
large_group = []
test = []
rows = len(S)
print(len(S))
count = 1

for i in range(rows-1):
    if S[i] == S[i+1]:
        count+=1
    if count == rows and count>=3:
        test.append([0,count-1])
        break
    if S[i] != S[i+1] or (i+1 == rows-1):  ### !!!!!!!!!!!!!!!!!!!!
        #if count == len(S):
            #test.append([S[0],S[0+count]])
            #break
        if count >=3 and (i+1 == rows-1):
            test.append([i - count +2, i+1])
            break
        if count >= 3:
            large_group.append(count)
            #S_index[S_i][S_i] = (S.index(S[i]) - count)
            #S_index[S_i][S_i] = S.index(S[i])
            #test[S_i] = (i- count)
            #test[S_i+1] = i
            test.append([i- count+1,i])
        count = 1

print(test)