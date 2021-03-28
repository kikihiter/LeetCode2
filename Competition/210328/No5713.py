class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        """
        210328
        遍历，存在列表中
        """
        if not word or word == "":
            return 0
        num = ""
        nums = []
        for s in word:
            if ord(s)<48 or ord(s)>57:
                if num != "":
                    num = int(num)
                    if num not in nums:
                        nums.append(num)
                num = ""
            else:
                num += s
        if num != "":
            num = int(num)
            if num not in nums:
                nums.append(num)
        return len(nums)
                