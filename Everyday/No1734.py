class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        """
        210511
        0001 0010 0011 0100 0101 0110
        x1^x5 = 0001    1
        x1^x2 = 0110    6
        x2^x5 = 0111    7
        x4^x5 = 0110    6
        x1 x2 x3 x4 x5
        x1^x2 x2^x3 x3^x4 x4^x5
        x1^x3 x2^x4 x3^x5
        x1^x2^x3^x4 x2^x3^x4^x5
        x1^x5
        x1^x2^...^xn = 0    (n=3,7,11)
                     = 1    (n=1,5,9)
        x1^x2^...^x(n-1) = encoded[0]^en[2]..^en[-2]
        xn = 
        """
        n = len(encoded)+1
        num1 = 0 if n % 4 == 3 else 1
        num2 = 0
        for i in range(n-1):
            if i&1==0:
                num2 ^= encoded[i]
        last = num1^num2
        ans = [0] * (n-1)
        ans.append(last)
        for i in range(n-2,-1,-1):
            ans[i] = encoded[i] ^ ans[i+1]
        return ans