class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # if len(prerequisites)==1:
        #     a = [x for x in range(numCourses)]
        #     a.remove(prerequisites[0][0])
        #     a.append(prerequisites[0][0])
        #     return a
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]
        preCourses = {}
        for a,b in prerequisites:
        # 初始化这个词典，将前置课程信息，全部储存进词典
            if a not in preCourses:
                preCourses[a] = [b]
            else:
                if b not in preCourses[a]:
                    preCourses[a].append(b)
        completed = []
        while 1:
            for a, b in preCourses.items():
                for course in b:
                    if course in preCourses and course not in completed:
                    # 当a的前置课程中存在未确定的课程时，a课程存疑
                        break
                else:
                # a的全部前置课程都验证可行了，将a添加到completed中
                    completed.append(a)
                    del preCourses[a]
                    break
            else:
                if len(preCourses) != 0:
                    return []
                a = [x for x in range(numCourses)]
                for cou in completed:
                    a.remove(cou)
                    a.append(cou)
                return a