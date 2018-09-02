#!/usr/bin/python3
#!coding:utf8

'''
保证一个类只有一个实例，并提供一个访问他的全局访问点
'''

class Singleton(object):
    def __new__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            self._instance = super().__new__(self)
        return self._instance
    
if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self,s):
            self.s = s
            
        def __str__(self):
            return self.s
        
    s1 = SingleSpam('spam')
    print(id(s1),s1)
    s2 = SingleSpam('spa')
    print(id(s1),s1)
    print(id(s2),s2)

    
    
    