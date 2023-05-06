class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False
rezult = Person("Захар" , 15)
rezult1 = Person("Даша" , 19)
print("Проверка есть ли 18 лет")
print("Захар:" , rezult.is_adult())
print("Даша:" , rezult1.is_adult())
