class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        有限状态机，主要思路是统计各个位置上1出现的次数，除以3，导出只出现一次的数。
        在运算过程中，各个位置（后面只讨论一位，因为各个位实际上是相同的）出现1的次数除以3，会有三种情况，分别是0,1,2
        需要用两个数字（只含0和1并且只能占一位）来表示这三个状况，0对应00,1对应01,2对应10
        三个状态转化关系为0->1->2->0,即00->01->10->00
        虽然运算过程中会有三种状态，但是实际上，全部遍历完之后，各个位置上只有两种状况，0和1，即00,01
        我们的目的就是找到最终结果中，01状态的点，即one=0,two=1的点位
        每次操作，读取到的数有0,1（二进制只有01）两种情况
        读取到0的时候，状态不发生变化，读取到1的时候，状态变化至下一个
        即,if num == 0:continue elif num == 1:if one,two == 0,0:one,two=0,1;elif ot== 0,1:ot=1,0;elif ot==1,0:ot=0,0
        单拿出one来讨论，我们希望(num,one)=(0,0)->0;(0,1)->1;(1,0)->two=0时,one=0 two=1时,one=0
        """
        """
        以前分析的时候，分析到一半的时候断掉了。
        不管以前的，重新来看这道题。
        210326
        其本质是统计各个位置1出现的次数。
        用一个数字one来表示，我们希望3的倍数次的位置全部为0，而余1的那个位置为1，那么这个数字one即为所求数字，现在单拿出一个位置来考虑。
        这个位置不是1就是0，只能表示两种状态，而事实上，在遍历过程中，对1的计数除以3可能的结果有0,1,2三种情况，没办法完全表示，我们引入另一个辅助数字two。对应余数为0时，我们希望one=0，two=0;余数为1时，one=1;余数为2时，one=0。
        遍历过程中，当前数字的这个位置为num，非1即0，对于传入为0的时候，我们不需要改变当前计数；
        而当num==1时，需要增加计数，此时one==1，则one->0;
        若one==0，需要由two来判断one未来的变化趋势，这里对变化趋势的定义可以有多种形式，我们暂且这样规定：
        one==0，two==1 => one=0, two=0
        one==0, two==0 => one=1, two=0
        one==1, two==0 => one=0, two=1
        那么变化过程可以描述为：
        if num == 0:
            one, two = one, two
        elif num == 1:
            if one == 1:
                one, two = 0,1
            elif one == 0:
                one, two = ~two, 0
        简化一下
        elif num == 1:
            one, two = ~one&~two, one
        再简化一下
        one, two = (one&~num)|(~one&~two&num), (two&~num)|(one&num)
        我的这个表达式比答案的复杂挺多，但是通过的测试，没有什么问题，就是没那么美观
        究其原因，答案的one，two是分两行来写，two是根据改变完状态的one来定义的，具体的分析过程（逻辑设置）和我的有很大不同
        """
        one, two = 0, 0
        for num in nums:
            one, two = (one&~num)|(~one&~two&num), (two&~num)|(one&num)
        return one