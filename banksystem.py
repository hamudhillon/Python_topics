'''
Login
Signup
Bank op
JSON
'''
import os
import json
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
            'Address':Address
        }
        }
        return data

    def signup(self):
        check=os.path.isfile(self.filename)

        if check:
            newdata=self.getdata()
            fr=open(self.filename,'r')
            data=json.loads(fr.read())
            fr.close()
            data.update(newdata)
            fw=open(self.filename,'w')
            json.dump(data,fw)
            fw.close()
        else:
            data=self.getdata()
            fw=open(self.filename,'w')
            json.dump(data,fw)
            fw.close()
    def login(self):
        username=input('Enter Username -> ')
        Password=input('Enter Password -> ')
        fr=open(self.filename,'r')
        data=json.loads(fr.read())
        fr.close()
        if username in data:
            if Password == data[username]['Password']:
                print('Welcome')
            else:
                print('Wrong Password')
        else:
            print('User Not Found')
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