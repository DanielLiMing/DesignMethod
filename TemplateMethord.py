#!/usr/bin/python3

'''
模板模式：
重复做相同逻辑的事情，但具体细节不同的场景,相同逻辑抽取父类，具体细节留置子类
'''

class template:
    def __init__(self):
        pass
    
    def logic(self):
        print("do something before ....")
        print(self.do_something_now())
        print("do something after ....")
        
    def do_something_now(self):
        return None
    
class apply_temp1(template):
    def __init__(self):
        pass
    def do_something_now(self):
        return 'apply 1'
    
class apply_temp2(template):
    def __init__(self):
        pass
    def do_something_now(self):
        return 'apply 2'
    
if __name__ == "__main__":
    obj1 = apply_temp1()
    obj2 = apply_temp2()
    obj1.logic()
    obj2.logic()
    print(obj1.__class__)
    print(obj2.__class__)