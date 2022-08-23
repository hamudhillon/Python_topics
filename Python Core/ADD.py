
# def numadd(num,num1):
#     return num+num1

# def stradd(str1,str2):
#     return str1+' '+str2


# def add(n1, n2):
#     return n1+n2

# while True:

#     num1=int(input('enter number 1 -> '))
#     num2=int(input('enter number 2 -> '))
#     op=input('''
# Choice Operator 
# enter 1 for add
# enter 2 for sub
# enter 3 for mul
# enter 4 for div
# enter 5 for exit
#     :''')
#     out=0
#     if op=='1':
#         out=add(num1,num2)

#     elif op=='5':
#         break

#     print(f'''
# -------------------
# || Result {out}  ||
# -------------------
#     ''')
# def check(country,gender,age):
#     if country=='india':
#         if age>=18:
#             print('eligible for the vote')
#         else:
#             print('not eligible for the vote')
#     elif country=='south africa':
#         if age>=18 and gender=='male':
#             print('eligible for the vote')
#         elif age>=21 and gender=='female':
#             print('eligible for the vote')
#         else:
#             print('not eligible for the vote')
#     elif country=='north korea':
#         if age>=18 and gender=='male':
#             print('eligible for the vote')
#         else:
#             print('not eligible for the vote')


# country=input('enter country ->')
# age=int(input('enter Age ->'))
# gender=input('enter gender ->')

# check(country,gender,age)


# x=lambda a,b,c:a+b+c
# print(x(2,5,8))


data=[1,2,3]
print([data[i]+data[i+1] for i in range(len(data))])