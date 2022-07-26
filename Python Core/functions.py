'''
function


'''



# def welcome(**vars):  #|  Function Defination       
#     print(vars)               #|  Function Statement
#     # print(Phone)                        #|  Function Statement

# # welcome('Rohit',34567890,'asdas','asdhuasyk')               #|  Function calling
# # welcome('Rohit',34567890,'asdhuasyk')               #|  Function calling
# welcome(name='Rohit',age=77)               #|  Function calling

# n=4
 
# print(f)


# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     # print(f)
#     return f

# print(fact(5))


'''
lambda function
short function 
one line function
'''

# x = lambda a,b,c:[i*b for i in range(1,a)]

# print(x(4,5,4))

'''
recursion function
when function calls itself
'''

# def loop():
#     print('LOOOOOP')
#     loop()
# loop()


'''
factorial with recursion function
fibonacci series

0 1 1 2 3 5 8

stack
| 1+0 | 1
| 2+1 | 2  
|  4  |
|_____|
'''

def fibo(num):
    if num<=1:
        return num  
            #      1       +        0 
    else:   #      2       +        1
        return (fibo(num-1)+ fibo(num-2))
n=10
for i in range(n):
    print(fibo(i))



