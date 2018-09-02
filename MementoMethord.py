#!/usr/bin/python3

'''
备忘录模式：
    在不破坏封装性的前提下，捕获一个对象内部的状态，并在对象之外保存这个状态，这样以后可以将该对象恢复到原先保存的状态
'''

import copy 

def Memento(obj, deep = False):
    state = (copy.copy if deep else copy.deepcopy)(obj.__dict__)
    def Restore():
        obj.__dict__ = state 
    return Restore 

class Transcation:
    deep = False 
    def __init__(self,*targets):
        self.targets = targets
        self.Commit()
        
    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]
        
    def Rollback(self):
        for state in self.states:
            state()
            
def transactional(methord):
    def wrappedMethord(self,*args, **kwargs):
        state = Memento(self)
        try:
            return methord(self,*args,**kwargs)
        except:
            state()
            raise
    return wrappedMethord

class NumObj(object):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return '<%s:%r>' % (self.__class__.__name__,self.value)
    
    def Increment(self):
        self.value += 1
        
    @transactional
    def DoStuff(self):
        self.value = '111'
        self.Increment()
        
if __name__ == '__main__':
    n = NumObj(-1)
    print(n)
    
    t = Transcation(n)
    try:
        for i in range(3):
            n.Increment()
            print(n)
        t.Commit()
        print('commited ...')
        for i in range(3):
            n.Increment()
            print(n)
        n.value += 'x'
        print(n)
    except:
        t.Rollback()
        print('-- rolled back')
        
    print(n)
    
    print('-- noe doing stuff ...')
    try:
        n.DoStuff()
    except:
        print('Doing stuff failed')
        import traceback
        traceback.print_exc(0)
        pass
    print(n)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            