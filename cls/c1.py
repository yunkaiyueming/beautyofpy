class Dog:
    eal = '尾巴'

    def __init__(self,food,voice):
        self.food=food
        self.voice = voice
    
    def eat(self):
        print('dog eat %s' % self.food)
    
    def bark(self):
        print('dog bark %s' % self.voice)

    def set_eal(self, eal):
        Dog.eal = eal


dog1 = Dog('狗粮','汪汪汪')
dog2 = Dog('狗粮1','汪汪汪2')

dog1.eat()
dog1.bark()

dog2.eat()
dog2.bark()
print(dog1.eal, dog2.eal, Dog.eal)

dog1.set_eal('长尾1')
print(dog1.eal, dog2.eal, Dog.eal)
