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
    def getdata(self,accno):
       
        username=input('Enter Username -> ')
        Name=input('Enter Name -> ')
        Phone=input('Enter Phone -> ')
        Password=input('Enter Password -> ')
        Address=input('Enter Address -> ')
        data={
            username:{
            'Account no':accno,
            'Name':Name,
            'Phone':Phone,
            'Password':Password,
            'Address':Address,
            'Balance':0.0,
            'Last 5 Transitions':[]
        }
        }
        return data

    def signup(self):
        check=os.path.isfile(self.filename)
        if check:
            data=self.fetch_data()
            accno=int('2022'+str(len(data)+1))
            newdata=self.getdata(accno)
            data.update(newdata)
            self.send_data(data)
        else:
            accno=20221
            data=self.getdata(accno)
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
5️⃣ All Transitions
6️⃣ Logout
''')
        if op=='1':
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
            return True
        elif op=='2':
            add_bal=float(input('Enter Amount to add -> '))
            balance=db[username]['Balance']
            db[username]['Balance']=balance+add_bal
            db[username]['Last 5 Transitions'].append(self.trans_format(username,add_bal,'deposit'))
            self.send_data(db)
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
            return True
        elif op=='3':
            sub_bal=float(input('Enter Amount to Withdraw -> '))
            balance=db[username]['Balance']
            db[username]['Balance']=balance-sub_bal
            db[username]['Last 5 Transitions'].append(self.trans_format(username,sub_bal,'widthdraw'))
            self.send_data(db)
            
            print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
💰 BALNACE - {db[username]['Balance']}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
            return True
        elif op=='4':
            toACC=input('Enter Account no to whom you want to send money \n')
            toUSER=self.searchUSER(db,toACC)
            if toUSER:
                print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
 USER - {toUSER}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
                toAMMT=float(input('Enter Amount -> '))
                if toAMMT <=db[username]['Balance']:
                    db[toUSER]['Balance']=db[toUSER]['Balance']+float(toAMMT)
                    
                    db[username]['Balance']=db[username]['Balance']-float(toAMMT)
                    db[username]['Last 5 Transitions'].append(self.trans_format(toUSER,toAMMT,'send'))
                    db[toUSER]['Last 5 Transitions'].append(self.trans_format(username,toAMMT,'receive'))
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
            return True

        elif op=='5':
            for t in db[username]['Last 5 Transitions']:
                print(
f'''
➖➖➖➖➖➖➖➖➖➖➖➖➖
{t}
➖➖➖➖➖➖➖➖➖➖➖➖➖
''')
            return True
        elif op=='6':
           return False
    
    def searchUSER(self,db,acc):
        for u in db:
            if float(acc)==float(db[u]['Account no']):
                return u
            else:
                continue
    def trans_format(self,to,amt,action):
        from datetime import datetime
        tf={
            'User':to,
            'ammount':amt,
            'date':str(datetime.now()),
            'Action':action
        }
        return tf
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