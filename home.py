# class Man():
#     def __init__(self,name="Munarbek",age=29,cash_balance=1000000000000000.000,privet_house=True):
#         self.name=name
#         self.age=age
#         self.cash_balance=cash_balance
#         self.privet_house=True

#     def info_about(self):
#         return (self.name,self.age,self.cash_balance,self.privet_house)
 
#     def making_money(self,money):
#         self.cash_balance += money
#         return money
        

#     def buying_house(self,house='house'):
#         if self.cash_balance - house > 0 :
#            self.cash_balance -=house
#            self.privet_house = True
        

# class My_house():
#     def get_House(self,area,cost):
#         self.area=area
#         self.cost=cost
#         return area,cost

#     def House_discount(self,percentage:1500):
#         self.cost -= (self.cost * percentage)


# class Mini_House():
#     def M_house(self,area:40.0,cost:98500):
#         self.cost=cost
#         self.area = area 
# m=Man("Munarbek",29,1000000000000000,True)
# mk=Man(1000000)

# print(m.info_about())





#  class student ():
#    def __init__(self,name ='Ivan', age = 18, groupNumber = '10A'):
#        self.name=name
#        self.age=age
#        self.groupNumber=groupNumber

#    def getName(self,name="Munarbek"):
#        self.name=name
#        return name
#    def getAge (self,age=20):
#        self.age=age
#        return age

#    def GetGroupNumber(self,groupNumber='b1'):
#        self.groupNumber=groupNumber
#        return groupNumber

#    def setNameage(self,name='Baaababa',age=22):
#        self.name=name
#        self.age=age
#        return name,age

#    def setGroupNumber(self,groupNumber='a0'):
#        self.groupNumber=groupNumber
#        return groupNumber

# student1=student(name='Munarbek',age=29,groupNumber='G3')
# student2=student(name='palancha',age=20,groupNumber='A1')
# student3=student(name='Tukuncho',age=21,groupNumber='b1')
# student4=student(name='Baaababa',age=22,groupNumber='b21')
# student5=student(name='Vse',age=100,groupNumber='a0')

# print(student1.getName())




# class Car:
#     def __init__(self,color,type,year):
#         self.color=color
#         self.type=type
#         self.year=year

#     print("Автомобиль заведен")    

#     def car_is_stopped(self):
#         return True
#     print("Автомобиль заглушен")
    
#     def car_year(self):
#         return self.year
#     print(car_year)

#     def Type_Car(self):
#         return self.type
#     print(Type_Car)

#     def Car_Color(self):
#         return self.color
#     print(Car_Color)

# my_car=Car('Black','Sedan',2021)
# print(my_car.car_year())    

