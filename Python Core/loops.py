'''
Loops
For loop - Controled loop 
while loop - infinte loop

'''
# d,C,E,W=[2,2,3,11]
# print(d)
# print(C)
# print(E)
# # print(W)


# data={
#     # Key :  value
#     'Name':'Harman',
#     'Phone':234567890,
#     'Age':3456
# }
# for k,v in data.items():
#     d,v=k
#     print(f'{ d}:{v} ')

# a=0
    
# while a<=len(data.items()):
#     print(f'a is {data.popitem()[1]}')
#     a+=1

'''
Q1 PRINT prime numbers which come in a range of 1-100
Q2 find factorial of a number
Q3 take a random numbers list and find factorial ,
    even odd and prime number or not 

'''
# n=4
# f=1

# for i in range(1,n+1):
#     f=f*i 
# print(f)


for num in range(1,100):
    c=0
    for i in range(2,num): 
        if num%i==0:
            c=c+1
            break
    
    if c==0 and num !=1:
        print(num, end=' ')