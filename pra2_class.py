class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

class Customer(Person):
    def __init__(self,name,age,adress,tel):
        super().__init__(name,age)
        self.adress = adress
        self.tel = tel

    def getName(self):
        return '顧客：' + self.name
