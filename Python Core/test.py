

from typing import Type, final


data=[1,2,34,4]
'''
Loop
collection -> eli
range -> custom itr
range -> list -> index
take a randomn number of a list e.g [1,3,4,5,7,8]
and show which number is even or odd
make a list of number taken from user
'''
# for i in range(len(data)):
#     print(i , data[i])   

# SizeOfList=int(input('Enter Size Of list -> '))
# l=[]
# for i in range(SizeOfList):
#     # print('hello')
#     eli=int(input('Enter Element -> '))
#     l.append(eli)

# for i in l:
#     if i%2==0:
#         print('Even')
#     else:
#         print('Odd')


# eli=[int(x) for x in input('enter Elements -> ').split()]
# eli=list(map(int,input('enter Elements -> ').split()))
# print(eli)
'''
Take a String and count the vowels from it and also count the 
ocurance of each vowel  

'''
'''
{
    1:'odd',
    4:'even',
    7:'odd',
}

WHILE

break
continue
pass
'''
# 2 4 8 16 32 
'''
*
**
***
****
'''
# a=1
# while a<=5:
#     print('A is Zero')
#     pass
#     a+=1

# if a==0:
#     pass


'''
FUNCTIONS
'''
# c=0

# def MYFUNC(a):
#     print(a)
# print(MYFUNC(c+1))

# x=lambda a,b,c,d:a+b+c+d
# print(x(1,3,4,5))

'''
CLASS
object

'''
# class car:
#     name='verna'
#     model_year=2018
#     def show_info(self):
#         print(self.name)
#     def set_valus(self,n):
#         self.name=n
# c=car()
# c.show_info()
# c.set_valus('Random')
# c.show_info()


# class vehical:
#     def __init__(self,t):
#         self.type=t
#     def set_values(self,n,m,y):
#         self.name=n
#         self.model=m
#         self.year=y
#     def show(self):
#         print(self.name) 
#         print(self.model)
#         print(self.year)

# class car(vehical):
#         def __init__(self):
#             super().__init__('car')
# c=car()
# print(c.type)
# c.set_values('verna','bb',2000)
# c.show()

'''
Exception Handling

'''
# print(a)
# try:
#     int('lajsjhdjashgjd')
# except NameError:
#     print('ss')
# except:
#     print('other')

# raise TypeError('asjdhasjkhdkjashdjkash')

# class Myerror(Exception):
#     pass 

# raise Myerror('asdljhasjdkkadhjashl')


# from math import factorial

# print(factorial(400))

import wikipedia
# print(wikipedia.summary('INDIA'))

print('📛📛📛📛📛📛')