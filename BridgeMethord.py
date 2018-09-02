#!/usr/bin/python3
#coding:utf8

'''
将抽象部分与他的实现部分分离。使他可以独立变化
'''

class DrawingAPI1(object):
    def draw_circle(self,x,y,radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))
        
class DrawingAPI2(object):
    def draw_circle(self,x,y,radius):
        print('API2.circle at {}:{} radius {}'.format(x,y,radius))
        
class CircleSheap(object):
    def __init__(self,x,y,radius,drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
        
    def draw(self):
        self._drawing_api.draw_circle(self._x,self._y,self._radius)
        
    def scale(self,pct):
        self._radius = pct
        

def main():
    shapes = {
        CircleSheap(1,2,3,DrawingAPI1()),
        CircleSheap(4,5,6,DrawingAPI2())
        }
    
    for shape in shapes:
        shape.scale(2.5)
        shape.draw()

if __name__ == '__main__':
    main()    