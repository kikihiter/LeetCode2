class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        用一个词典记录学习课程key所需要的全部前置课程value，前置课程的顺序不考虑
        """
        if len(prerequisites)<2:
            return True

        preCourses, nextCourses = {}, {}
        for a,b in prerequisites:
        # 初始化这个词典，将前置课程信息，全部储存进词典
            if a not in preCourses:
                preCourses[a] = [b]
            else:
                if b not in preCourses[a]:
                    preCourses[a].append(b)
            # if b not in nextCourses:
            #     nextCourses[b] = [a]
            # else:
            #     if a not in nextCourses[b]:
            #         nextCourses[b].append(a)
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
                    return False
                return True
        


        # for course in range(0,numCourses):
        #     if course in completed:
        #     # 已经完成了这门课程的检验
        #         continue
        #     if course not in preCourses:
        #         continue
        #     studying = preCourses[course]
        #     studied = [course]
        #     while studying != []:
        #         t = studying.pop(-1)
        #         if t in studied:
        #             return False
        #         studied.append(t)
        #         if t in preCourses:
        #             studying.extend(preCourses[t])
        #     completed.extend(studied)
        # return True