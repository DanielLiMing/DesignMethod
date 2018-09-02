#!/usr/bin/python3
'''
中介者模式：
    用一个中介对象来封装一系列对象的交互，中介者使各对象不需要显示的相互引用，而且可以独立的改变他们之间的交互
'''
import time


class TC:
    def __init__(self):
        self._tm = None
        self._bProblem = 0
        
    def setup(self):
        print("Setting uo the Test")
        time.sleep(1)
        self._tm.prepareReporting()
        
    def execute(self):
        if not self._bProblem:
            print("Execute the test")
            time.sleep(1)
        else:
            print("Problem in setup, Test not execute..")
            
    def tearDown(self):
        if not self._bProblem:
            print("Tearing Down")
            time.sleep(1)
            self._tm.publishReport()
            
    def setTM(self,tm):
        self._tm = tm 
        
    def setProblem(self,value):
        self._bProblem = value
        
class Reporter:
    def __init__(self):
        self._tm = None
        
    def prepare(self):
        print("Reporter class is parpering to report the results")
        time.sleep(1)
        
    def report(self):
        print("Report the results of Test")
        time.sleep(1)
        
    def setTM(self, tm):
        self._tm = tm 
        
class DB:
    def __init__(self):
        self._tm = None
        
    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(1)
        import random
        if random.randrange(1,4) ==3:
            return -1
        
    def update(self):
        print("update the test results in Datsbase")
        time.sleep(1)
        
    def setTM(self,tm):
        self._tm = tm
        
class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None
        
    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()
            
    def setReporter(self,reporter):
        self._reporter = reporter
        
    def setDB(self,db):
        self._db = db
        
    def publishReport(self):
        self._db.update()
        rvalue = self._reporter.report()
        
    def setTC(self, tc):
        self._tc = tc
        
if __name__ == "__main__":
    print("*" * 20)
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setReporter(reporter)
    tm.setDB(db)
    reporter.setTM(tm)
    db.setTM(tm)
    while True:
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        