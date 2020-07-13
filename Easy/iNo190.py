class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # print n
        # n = list(str(n))
        # print n
        # for i in range(len(n)/2):
        #     n[i], n[-i-1] = n[-i-1], n[i]
        # print n
        # n = "".join(n)
        # return int(n)
        n = bin(n)
        n = list(str(n))
        # print n
        del n[0]
        del n[0]
        l = len(n)
        n = n[::-1]
        while l != 32:
            n.append("0")
            l += 1
        n = "".join(n)
        return int("0b"+n, base = 2)