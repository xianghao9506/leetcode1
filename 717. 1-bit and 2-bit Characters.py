class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
## 如果倒数第二位是0 最后一位肯定是1bit
## 如果倒数第二位是1 X10 X=1：
