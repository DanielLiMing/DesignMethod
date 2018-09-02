#!/usr/bin/python3

'''
命令模式：
    将一个请求封装成一个对象，从而使不同的请求对客户进行参数化，对请求排队或记录请求日志以及支持可撤销的操作
'''
import os

class MoveFileCommand(object):
    def __init__(self,src,dst):
        self.src = src
        self.dst = dst
        
    def excute(self):
        self()
        
    def __call__(self):
        print("renaming {} to {}".format(self.src,self.dst))
        #os.rename(self.src,self.dst)
        
    def undo(self):
        print("renaming {} to {}".format(self.dst,self.src))
        #os.rename(self.dst,self.src)
        
if __name__ == "__main__":
    command_stack = []
    
    command_stack.append(MoveFileCommand('foo.txt','bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt','baz.txt'))
    
    for cmd in command_stack:
        cmd.excute()
        
    for cmd in reversed(command_stack):
        cmd.undo()
    