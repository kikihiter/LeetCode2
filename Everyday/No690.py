"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """ 
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        """
        210501
        因为只有一个直系上司，必然不会重复
        先哈希表，把员工信息存进去，方便查找
        """
        empMap = {}
        for emp in employees:
            empId, empIm, empSub = emp.id, emp.importance, emp.subordinates
            empMap[empId] = [empIm, empSub]
        
        stack = [id]
        imSum = 0
        while stack != []:
            id = stack.pop()
            imSum += empMap[id][0]
            stack.extend(empMap[id][1])
        return imSum