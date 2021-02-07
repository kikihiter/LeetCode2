class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        """
        A - a + b = B - b + a
        b = (B - A + 2a)/2
        """
        aSum, bSum = 0, 0
        for i in range(len(A)):
            aSum += A[i]
        for j in range(len(B)):
            bSum += B[j]
        for a_ in A:
            if (bSum - aSum + 2*a_)&1 == 1 or (bSum - aSum + 2*a_) <= 0:
                continue
            if (bSum - aSum + 2*a_)/2  in B:
                return [a_, (bSum - aSum + 2*a_)/2]
        