'''
Login
Signup
Bank op
JSON
'''
import os
import json

from numpy import insert
class Bank:
    filename='BANKDATA.json'
    def getdata(self):
        username=input('Enter Username -> ')
        Name=input('Enter Name -> ')
        Phone=input('Enter Phone -> ')
        Password=input('Enter Password -> ')
        Address=input('Enter Address -> ')
        data={
            username:{
            'Name':Name,
            'Phone':Phone,
            'Password':Password,
            'Address':Address,
            'Balance':0.0
        }
        }
        return data

    def signup(self):
        check=os.path.isfile(self.filename)

        if check:
            newdata=self.getdata()
            data=self.fetch_data()
            data.update(newdata)
            self.send_data(data)
        else:
            data=self.getdata()
            self.send_data(data)
    def login(self):
        username=input('Enter Username -> ')
        Password=input('Enter Password -> ')
        db=self.fetch_data()
        if username in db:
            if Password == db[username]['Password']:
                print('Welcome')
                while True:
                    if not self.bankOP(db,username):
                        break
            else:
                print('Wrong Password')
        else:
            print('User Not Found')

    def fetch_data(self):
        fr=open(self.filename,'r')
        data=json.loads(fr.read())
        fr.close()
        return data
    def send_data(self,data):
        fw=open(self.filename,'w')
        json.dump(data,fw)
        fw.close()
    def bankOP(self,db,username):
        op=input(
'''
1️⃣ Check Balance
2️⃣ Add Money
3️⃣ Widthdraw Money
4️⃣ Transfer Money
5️⃣ Exit
''')
        if op=='1':
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
        elif op=='2':
            add_bal=float(input('Enter Amount to add -> '))
            balance=db[username]['Balance']
            db[username]['Balance']=balance+add_bal
            self.send_data(db)
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
        elif op=='3':
            sub_bal=float(input('Enter Amount to Withdraw -> '))
            balance=db[username]['Balance']
            db[username]['Balance']=balance-sub_bal
            self.send_data(db)
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
        elif op=='4':
            toUSER=input('Enter Username to whom you want to send money \n')
            toAMMT=float(input('Enter Amount -> '))
            if toUSER in db:
                if toAMMT <=db[username]['Balance']:
                    db[toUSER]['Balance']=db[toUSER]['Balance']+float(toAMMT)
                    
                    db[username]['Balance']=db[username]['Balance']-float(toAMMT)
                    self.send_data(db)
                    print('💸MONEY SENT!')
                else:
                    print('Low Balance')
            else:
                print('User Not Found ')
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
        elif op=='5':
           return False
obj=Bank()
option=int(input('''
1️⃣ Signup
2️⃣ Login
'''))
if option==1:
    obj.signup()
elif option==2:
    obj.login()
else:
    print('Check Your eyes')