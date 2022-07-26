'''
List         Set          Tuple          Dict  

[]          {}            ()             {}
list()      set()         tuple()        dict()

Store any   --             --             --
kind of 
data

Mutable     Mutable       Immutable     Mutable
(Changeble)

Ordered     Unordered     Ordered      Custom Order
(index)                   --           (Keys)    

Elements                               Keys And Value
seprated    ---           ---          Pairs which is 
with ,                                 seprated with ,

-------------------Functions---------------------------
LIST          SET             TUPLE          DICT

append()     add()             ----         update()   
insert()     update()          ----         pop()
sort()       remove()                       popitems()
reverse()    pop()                          get() 
pop()        discard()                      keys()
remove()                                    values()
extends()                                   items()
clear()                                     clear() 
'''

'''
LIST
collection of elements(data)
      0 1 2 3  4   5 
data=[1,2,3,4,'a','b']
     -6-5-4-3 -2  -1              

Slicing
data[1:4] -> [2,3,4]
'''

# fruits=['apple','banana','lichi','orange']
# print(fruits)
# fruits.append('mango')
# print(fruits)
# fruits.insert(1,'grapes')
# print(fruits)
# print(fruits.remove('lichi'))
# print(fruits)
# print(fruits.pop(0))
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.extend(['guava','watermelon'])
# print(fruits)
# fruits.clear()
# print(fruits)

'''
SET
Unique elements
Unorder
'''

# numbers={1,2,3,4,5}
# print(numbers)
# numbers.add(9)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers.add(9)
# print(numbers)
# numbers.pop()
# print(numbers)
# print(numbers.pop())
# print(numbers)

'''
TUPLE
'''
# numbers=(1,3,4,55,5,6,6)
# print(numbers)
# print(numbers[-1])
# print(numbers[2:5])

'''
DICT
oxford
words: meanings
  |
  V
unique

keys : Values
(unique)
'''

# data={
#     # Key :  value
#     'Name':'Harman',
#     'Phone':234567890,
#     'Age':3456
# }

# print(data['Name'])
# data['Name']='Random'
# print(data['Name'])
# print(data['Phone'])
# print(data)

# data.update({'Address':'ashjdga ashd jkash d','status':True})
# print(data)

# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.get('Address'))
# print(data.pop('Age'))

# print(data)

# data.popitem()
# print(data)
# data.clear()
# print(data)

'''
Conditions
if/else

if a==0{

}

if a==0:
  print('a is zero')
else:
  print('a is not zero')

'''
a=int(input('Enter a Number'))
print(type(a))
if a==0:
  print('a is zero')

elif a==1:
  print('a is one')
else:
  print('a is not zero nor one')
