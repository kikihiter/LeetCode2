class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        210430
        之前做过啊
        很经典的题
        位运算，三个状态之间互相转换
            00  01  10
        two 0   0   1      
        one 0   1   0
        
        two 0   1   0
        one 1   0   0
        if putIn == 0:                                                                              | two,one = putIn&(~two&one)|(~putIn&two), putIn&(~two&~one)|(~putIn&one)
            two, one = two, one                                                                     |
        elif putIn == 1:                                                                            |
            if two == 1:                                        |two, one = ~two&one, ~two&~one     |
                two = 0                                         |
                one = 0                                         |
            elif two == 0:                                      |
                if one == 0:          |two, one = one, ~one     |
                    two = 0           |     
                    one = 1           |
                elif one == 1:        |
                    two = 1           |
                    one = 0           |

        """
        one,two = 0, 0
        for num in nums:
            two,one = num&(~two&one)|(~num&two), num&(~two&~one)|(~num&one)
        return one