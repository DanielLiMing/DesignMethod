#!/usr/bin/python3

'''
外观模式:
    为子系统的一组接口提供一个一致的界面，Facade定义一个高层接口，这个接口使得这一子系统更加容易使用
'''
import time

SLEEP = 0.5

class TC1:
    def run(self):
        print("### In Test 1 ### ")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")
        
class TC2:
    def run(self):
        print("### In Test 2 ###")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running Test")
        time.sleep(SLEEP)
        print("Tearing Down")
        time.sleep(SLEEP)
        print("Test Fineshed\n")
        
class TC3:
    def run(self):
        print("### In Test 3 ###")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running Test")
        time.sleep(SLEEP)
        print("Tearing Down")
        time.sleep(SLEEP)
        print("Test Finished\n")
        
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [i for i in (self.tc1,self.tc2,self.tc3)]
        
    def runAll(self):
        [i.run() for i in self.tests]
        
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()