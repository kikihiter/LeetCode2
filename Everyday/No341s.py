class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.size = len(nestedList) if nestedList else 0
        self.iterator = None
        self.i = 0
    
    def next(self) -> int:
        cur = self.nestedList[self.i]
        if cur.isInteger():
            self.i += 1
            return cur.getInteger()
        else: return self.iterator.next()
    
    def hasNext(self) -> bool:
        while self.i < self.size:
            cur = self.nestedList[self.i]
            if cur.isInteger(): return True
            else:
                if self.iterator == None:
                    self.iterator = NestedIterator(cur.getList())
                if self.iterator.hasNext(): return True
                else: 
                    self.iterator = None
                    self.i += 1
        return False

"""
评论区大佬的解法，有可取之处，我就贴过来了
重点在self.iterator，解法本质上是class的递归
"""