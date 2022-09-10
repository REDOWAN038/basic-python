
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(self.name, self.age,end=' ')

class Student(Person):
    def __init__(self,name,age,graduationYear):
        super().__init__(name,age)
        self.graduationYear = graduationYear

    def showInfo(self):
        super().showInfo()
        print(self.graduationYear)



st1 = Student('redowan',22,2024)
st1.showInfo()