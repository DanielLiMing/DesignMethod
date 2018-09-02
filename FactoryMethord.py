#!/usr/bin/python3
#coding:utf8

'''
Factory Method

意图：定义一个创建对象的接口，让子类决定实现哪一个类，Fectory Methord使一个类实例化延迟到其子类
适用类：当一个类不知道他所必须创建的类的时候，
      当一个类希望他的子类来指定他所创建的对象的时候
'''

class ChinaGetter:
    """ initnal"""
    def __init__(self):
        self.trans = dict(dog=u"小狗",cat=u"小猫")
    
    def get(self,msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)
        
class EnglishGetter:
    def get(self,msgid):
        return str(msgid)
    
def get_localizer(language="English"):
    languages = dict(English=EnglishGetter,China=ChinaGetter)
    return languages[language]()

e, g = get_localizer("English"), get_localizer("China")

for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))   
        