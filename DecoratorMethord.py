#!/usr/bin/python3
#coding:utf8

'''
修饰模式：
    动态的位一个对象添加一些额外的职责，就增加功能来说，Decorator模式相比生成子类更加灵活
'''

class foo(object):
    def f1(self):
        print("oiginal f1")
        
    def f2(self):
        print("original f2")
        
class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee
        
    def f1(self):
        print("decorated f1")
        self._decoratee.f1()
        
    def __getattr__(self,name):
        return getattr(self._decoratee,name)
    
u = foo()
v = foo_decorator(u)
v.f1()
v.f2()
