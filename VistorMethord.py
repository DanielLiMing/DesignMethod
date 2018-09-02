#!/usr/bin/python3

'''
访问者模式：
    表示一个作用于某对象结构中的各元素的操作，他可使你在不改变各元素的类的前提下定义作用于这些元素的新操作
'''

class Person:
    def Accept(self,visitor):
        pass
    
class Man(Person):
    type = 'Man'
    def Accept(self, visitor):
        visitor.GetManConclusion(self)
        
class Woman(Person):
    type = 'Woman'
    def Accept(self, visitor):
        visitor.GetWomainConclusion(self)
        
class Action:
    def GetManConclusion(self,person):
        pass
    def GetWomainConclusion(self,person):
        pass
    
class Success(Action):
    type = 'success'
    def GetManConclusion(self, person):
        print('%s %s时，背后多半有一个伟大的女人' %(person.type, self.type))
    def GetWomainConclusion(self, person):
        print('%s %s时，背后大多有一个不成功的男人' %(person.type, self.type))
    
class Failing(Action):
    type = 'fail'
    def GetManConclusion(self, person):
        print('%s %s时，闷头喝酒，谁也不用劝' %(person.type, self.type)) 
    def GetWomainConclusion(self, person):
        print('%s %s时，眼泪汪汪，谁也劝不了' %(person.type, self.type))
        
class ObjectStructure:
    elements = []
    def Attch(self,element):
        self.elements.append(element)
        
    def Detach(self,element):
        self.elements.remove(element)
        
    def Display(self,visitor):
        for e in self.elements:
            e.Accept(visitor)
            
def main():
    o = ObjectStructure()
    o.Attch(Man())
    o.Attch(Woman())
    
    o.Display(Success())
    o.Display(Failing())
    return

if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            