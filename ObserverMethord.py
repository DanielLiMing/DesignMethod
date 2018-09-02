#!/usr/bin/python3

'''
观察者模式：
    定义一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于他的对象都得到通知并被自动更新
'''

class Subject(object):
    def __init__(self):
        self._observers = []
        
    def attch(self,observer):
        if not observer in self._observers:
            self._observers.append(observer)
            
    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except:
            pass
        
    def notify(self,modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
                
class Data(Subject):
    def __init__(self,name = ''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
        
    @property
    def data(self):
        return self._data
    
    @data.setter 
    def data(self,value):
        self._data = value
        self.notify()
    
class HexViewer:
    def update(self,subject):
        print("Hex Viewer:subject %s has data %d" % (subject.name,subject.data))
        
class DecimalViewer:
    def update(self,subject):
        print("Decimal Viewer:subject %s has data %d " % (subject.name,subject.data))
        
def main():
    data1 = Data('data1')
    data2 = Data('data2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attch(view1)
    data1.attch(view2)
    data2.attch(view1)
    data2.attch(view2)
    
    print('Setting Data1 = 10')
    data1.data = 10
    print('Setting Data2 = 15')
    data2.data = 15
    print('Settinf Data1 = 3')
    data1.data = 3
    print('Setting Data2 = 5')
    data2.data = 5
    print("Detach HexViewer from data2 and data1")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting Data1 = 10")
    data1.data = 10
    print("Settinf Data2 = 15")
    data2.data = 15
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    