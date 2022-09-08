
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


# data=[1,2,3]
# print([data[i]+data[i+1] for i in range(len(data))])


# import sqlite3
# conn=sqlite3.connect('data.db')
# cursor=conn.cursor()
# q='CREATE TABLE t3(name VARCHAR(100))'
# # cursor.execute(q)
# print(cursor.execute('''INSERT INTO t3(name) VALUES ('Random')'''))
# conn.commit()
# # print(db.execute('''SELECT name FROM t1'''))
# cursor.close()

# import sqlite3

# conn=sqlite3.connect('data.db')
# def query_run(query):
#     data=conn.execute(query)
#     conn.commit()
#     return data

# def insert_rec(Name,Add,Pass):
#     query=f'''
#     INSERT INTO users(Name,Address,Password) VALUES(
#         '{Name}',
#         '{Add}',
#         '{Pass}'
#     )
#     '''
#     query_run(query)

# def update_rec(field,value,id):
#     query=f'''
#     UPDATE users SET {field}='{value}' WHERE id={id}
#     '''
#     query_run(query)
# def delete_rec(id):
#     query=f'''
#     DELETE FROM users WHERE id={id}
#     '''
#     query_run(query)
# query='''
# CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# Name VARCHAR(255),
# Address VARCHAR(255),
# Password VARCHAR(255)
# )
# '''
# query_run(query)
# # insert_rec('Dhillon','Chd','123')
# # update_rec('Password','321',1)
# # delete_rec(2)

# query='''
#     SELECT * FROM users
# '''

# data=query_run(query)
# for i in data:
#     print(i[3])


# conn.close()


import sqlite3
conn=sqlite3.connect('data.db')
def query_run(query):
    data=conn.execute(query)
    conn.commit()
    return data

def insert_rec(Name,Add,Pass):
    query=f'''
    INSERT INTO users(Name,Address,Password) VALUES(
        '{Name}',
        '{Add}',
        '{Pass}'
    )
    '''
    query_run(query)
query='''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Name VARCHAR(255),
Address VARCHAR(255),
Password VARCHAR(255)
)
'''
query_run(query)

choice=input('''
1 Signup
2 Login

''')
if choice=='1':
    name=input('Enter Name -> ')
    address=input('Enter Address -> ')
    Password=input('Enter Password -> ')
    insert_rec(name,address,Password)
elif choice=='2':
    name=input('Enter Name -> ')
    Password=input('Enter Password -> ')
    query=f'''
        SELECT * FROM users WHERE Name='{name}' AND Password='{Password}'
    '''
    data=query_run(query)
    data=data.fetchone()
    if data:
       print(f'''
Welcome {data[1]}
Name -> {data[1]}
Address -> {data[2]}
''')
    else:
        print('User Not found')

else:
    print('Wrong Input ')