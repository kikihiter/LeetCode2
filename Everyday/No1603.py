class ParkingSystem(object):
    """
    感觉只需要三个数就可以满足要求了
    每次入车，车辆上限减一即可
    因为这个系统完全不成熟，也没有出车的函数，所以我也不考虑得那么完善
    210319
    """
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.b = big
        self.m = medium
        self.s = small


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            self.b -= 1
            n = self.b
        elif carType == 2:
            self.m -= 1
            n = self.m
        elif carType == 3:
            self.s -= 1
            n = self.s
        return n >= 0        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)