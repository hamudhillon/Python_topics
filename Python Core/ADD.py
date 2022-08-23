
# def numadd(num,num1):
#     return num+num1

# def stradd(str1,str2):
#     return str1+' '+str2


def add(n1, n2):
    return n1+n2

while True:

    num1=int(input('enter number 1 -> '))
    num2=int(input('enter number 2 -> '))
    op=input('''
Choice Operator 
enter 1 for add
enter 2 for sub
enter 3 for mul
enter 4 for div
enter 5 for exit
    :''')
    out=0
    if op=='1':
        out=add(num1,num2)

    elif op=='5':
        break

    print(f'''
-------------------
|| Result {out}  ||
-------------------
    ''')