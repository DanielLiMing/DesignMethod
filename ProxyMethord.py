#!/usr/bin/python3

'''
代理模式:
    为其他对象提供一种代理以控制对这个对象的访问
'''

import time

class SaleManager:
    def work(self):
        print("Sale Manager working...")
        
    def talk(self):
        print("Sale Manager ready to talk")
        
class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None
        
    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SaleManager()
            time.sleep(2)
            self.sales.talk()
        else:
           time.sleep(2)
           print("Sales Manager is busy")
           
if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work() 