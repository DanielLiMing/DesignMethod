#!/usr/bin/python3
#coding:utf8

'''
提供一个创建一些列相关或相互依赖对象的接口，而无需制定他们具体的类
'''
import random

class PetShop:
    def __init__(self,animal_factory=None):
        self.pet_factory = animal_factory
        
    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("This is a lonely", str(pet))
        print("It says", pet.speak())
        print("It eats",self.pet_factory.get_food())
        
class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "Dog"
class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"
    
class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"
    
class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "Cat food"
    
def get_factory():
    return random.choice([DogFactory,CatFactory])()

shop = PetShop()
for i in range(3):
    shop.pet_factory = get_factory()
    shop.show_pet()
    print("=" * 20)