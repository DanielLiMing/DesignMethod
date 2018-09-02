#!/usr/bin/python3
#coding:utf8

'''
组合模式：将对象组合成树形结构以表示“部分-整体”的层次结构，Composite使得用户对单个对象和组合对象具有一致性
'''

class Component:
    def __init__(self,strName):
        self.m_strName = strName
    def add(self,com):
        pass
    def Display(self,nDepth):
        pass
    
class Leaf(Component):
    def add(self,com):
        print("leaf can't add")
        
    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)
        
class Composite(Component):
    def __init__(self, strName):
        self.m_strName = strName
        self.c = []
        
    def add(self, com):
        self.c.append(com)
        
    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)
        for com in self.c:
            com.Display(nDepth+2)
            
if __name__ == "__main__":
    p = Composite("Wong")
    p.add(Leaf("Lee"))
    p.add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.add(Leaf("San"))
    p.add(p1)
    p.Display(1)
    