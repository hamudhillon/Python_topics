'''
oops
Class
objects -> anything who has property and methods or functions
Inheretance

'''

# class A:
#     name='Calss A' #Property
#     def __init__(self,a,b): # Constructor
#         print(a,b)
#     def showInfo(self): #Methods self -> current Instance 
#         print(self.name)
# obj=A('asdhjaskdhjas1',2) #making Object
# objv=A('asdhjaskdhjas1',2) #making Object
# # print(obj.name)
# obj.showInfo()

'''
Make Calculator with the help of class
Make a class Vehical And Make Diffrent objects
like Bike , car
and add functionlities like Basic info Of that Vehical
e.g 
Name -> Verna
Type -> Car
Top Speed -> 150
Avg -> 25
if This vehcial Travale 12 km
it will consume 200 ruppee of petrol

'''


'''
Type
single   - A -> B
multiple   A  B
            C         
multilevel  A -> B -> C
hierarchical  A
            B   C
hybrid  A -> B
            C  D
 
'''

# class A:
#     name='Class A'
#     def __init__(self):
#         print("I am Class A")

# class B(A):
#     # pass
#     def __init__(self) :
#         print("I am Class B")
#         super().__init__()
#         # print(self.name)

# obj=B()


# class vehical:
    
#     def __init__(self,name,type,topspeed,avg):
#         self.__name=name
#         self.typev=type
#         self.top_speed=topspeed
#         self.Avg=avg

#     def info(self):
#         print('Name ',self.__name)
#         print('type ',self.typev)
#         print('top_speed ',self.top_speed)
#         print('Avg ',self.Avg)
    
#     def Avg_petrol(self,dist):
#         petrol=(dist/self.Avg)*100*97.5
#         print(f'''
# If {self.__name} is traveled {dist}/km
# it will consume {petrol} Rupee petrol With Average of {self.Avg}km/l.
#         ''')

# car=vehical('Verna','Car',150,25)
# car.info()
# car.Avg_petrol(12)

# Bike=vehical('Ct100','Bike',100,95)
# Bike.info()
# Bike.Avg_petrol(12)



# class Bike(vehical):
#     def __init__(self, name, topspeed, avg):
#         super().__init__(name, 'Bike', topspeed, avg)


# bike1=Bike('Pulsur',150,60)

# # print('name -> ', bike1.__name)
# bike1.info()


# class SUV(vehical):
#     def __init__(self, name, topspeed, avg):
#         super().__init__(name, 'SUV', topspeed, avg)

# s=SUV('Thar',175,20)
# s.info()
# s.Avg_petrol(10)

# a=10
# b=9

# c='hello'
# d='world'
# print(a+b)
# print(c+d)


# class A:

#     def show(self):
#         print('Class A Show')

# class B(A):

#     def show(self):
#         print('Class B Show')


# A().show()
# B().show()