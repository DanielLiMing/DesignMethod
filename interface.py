'''
interface(接口)
定义：一种特殊的类声明了若干方法，要求集成该接口的类必须实现这种方法
作用：限制接口的类的方法的名称及调用方式，隐藏了类的内部实现
'''
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
    
class AiliPay(Payment):
    def pay(self,money):
        print("使用支付宝支付%s元" % money)
        
class ApplePay(Payment):
    def pay(self,money):
        print("使用苹果支付%s元" % money)
        
apay = AiliPay()
apay.pay(12)
app = ApplePay()
app.pay(16)