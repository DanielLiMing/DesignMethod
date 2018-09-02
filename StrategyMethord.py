#!/usr/bin/python3

'''
策略模式:
    定义一系列算法，把他们一个个封装起来，并且可以使他们可以相互替换，本模式可以使算法可独立于他的客户而变化
'''
import types

class StrategyExample:
    def __init__(self,func = None):
        self.name = "Strategy Example 0"
        if func is not None:
            self.execute = types.MethodType(func,self)
    def execute(self):
        print(self.name)
        
def func1(self):
    print(self.name+"from execute1")
    
def func2(self):
    print(self.name +"from execute2")
    
if __name__ == "__main__":
    strate0 = StrategyExample()
    
    strate1 = StrategyExample(func1)
    strate1.name = "1111111111111"
    
    strate2 = StrategyExample(func2)
    strate2.name = "2222222222222"
    
    strate0.execute()
    strate1.execute()
    strate2.execute()