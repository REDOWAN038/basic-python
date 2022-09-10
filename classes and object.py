

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showMessage(self):
        print('welcome', self.name)

    def showInfo(self):
        print(self.name, self.age)

p1 = Person('redowan',22)
print(p1.name, p1.age)
p1.showMessage()
p1.age = 23
p1.showInfo()