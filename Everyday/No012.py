class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        210514
        """
        ans = ""
        qian, num = num/1000, num%1000
        # while qian>0 :
        #     ans += 'M'
        #     qian -= 1
        bai, num = num/100, num%100
        # if bai == 9:
        #     ans += "CM"
        # elif bai == 5:
        #     ans += 'D'
        # elif bai == 4:
        #     ans += "CD"
        # elif 0 < bai < 4:
        #     while bai>0:
        #         ans += 'C'
        #         bai -= 1
        # elif 5 < bai < 9:
        #     ans += 'D'
        #     while bai > 5:
        #         ans += 'C'
        #         bai -= 1
        shi, num = num/10, num%10
        # if shi == 9:
        #     ans += "XC"
        # elif shi == 5:
        #     ans += 'L'
        # elif shi == 4:
        #     ans += "XL"
        # elif 0 < shi < 4:
        #     while shi > 0:
        #         ans += 'X'
        #         shi -= 1
        # elif 5 < shi < 9:
        #     ans += 'L'
        #     while shi > 5:
        #         ans += 'X'
        #         shi -= 1
        # qianList = ["M","MM","MMM"]
        # ans = ans if qian == 0 else ans + qianList[qian-1]
        # baiList = ["C","CC","CCC","CD","C","DC","DCC","DCCC","CM"]
        # ans = ans if bai == 0 else ans + baiList[bai-1]
        # shiList = ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        # ans = ans if shi == 0 else ans + shiList[shi-1]
        # geList = ["I","II", "III","IV","V","VI","VII","VIII","IX"]
        # ans = ans if num == 0 else ans + geList[num-1]
        """
        还可以优化
        """
        qianList = ["","M","MM","MMM"]
        ans += qianList[qian]
        baiList = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ans += baiList[bai]
        shiList = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ans += shiList[shi]
        geList = ["","I","II", "III","IV","V","VI","VII","VIII","IX"]
        ans += geList[num]
        return ans