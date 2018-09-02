#!/usr/bin/python3

'''
解释器模式：
    给定一个语言，定义他文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子
'''

class Context:
    def __init__(self):
        self.input = ""
        self.output=""
        
class AbstructExpression:
    def Interpret(self,context):
        pass
    
class Expression(AbstructExpression):
    def Interpret(self, context):
        print("terminal interpret")
        
class NonterminalExpression(AbstructExpression):
    def Interpret(self, context):
        print("Nonterminal interpret")
        
if __name__ == "__main__":
    context= "qqqq"
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)