#!/usr/bin/python3

'''
享元模式:
    运用共享技术有效的支持大量细粒度的对象
'''
import weakref

class Card(object):
    _CardPoll = weakref.WeakValueDictionary()
    
    def __new__(self, value, suit):
        obj = Card._CardPoll.get(value+suit, None)
        if not obj:
            obj = object.__new__(self)
            Card._CardPoll[value+suit] = obj 
            obj.value, obj.suit = value, suit
        return obj 
    def __repr__(self):
        return "<Card:%s%s>" % (self.value,self.suit)
    
if __name__ == '__main__':
    c1 = Card('9','h')
    c2 = Card('9','h')
    c2.value = '8'
    print(c1,c2)
    print(c1 == c2)
    print(id(c1),id(c2))