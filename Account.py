import random
import datetime
import random
import re
import pymysql

con=pymysql.connect('localhost','root','')
db=con.cursor()
db.execute("use bank")

class NewAccount:
	def __init__(self,Name,Place,Mobile,AccNo,Pass,Email):
		self.Name=Name
		self.Mobile=Mobile
		self.Place=Place
		self.AccNo=AccNo
		self.Pass=Pass
		self.Email=Email

def Insert():
        db.execute("insert into acc(name,phone,place,acc,email)values(%s,%s,%s,%s,%s)",(o1.Name,o1.Mobile,o1.Place,o1.AccNo,o1.Email))
        con.commit()
        
                
#Generate Account number
def AccNo():
	bankname="INDI"
	year=str(datetime.datetime.now().year)
	month=str(datetime.datetime.now().month)
	date=str(datetime.datetime.now().day)
	rand=str(random.randrange(1000,9999))
	return bankname+year+month+date+rand
#Generate OTP
def OTP():
	otp=random.randrange(1000,9999)
	return otp	


def passgen():
	lets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	specs=['!','@','#','$','%','^','&','*','(',')','_','-']
	let=random.choice(lets)
	let1=random.choice(lets)
	let2=random.choice(lets)
	let3=random.choice(lets)
	num=str(random.randrange(1000,9999))
	spec=str(random.choice(specs))
	spec1=str(random.choice(specs))
	spec2=str(random.choice(specs))
	spec3=str(random.choice(specs))
	return let+let1+let2+let3+num+spec+spec1+spec2+spec3

def VerifyPass(a):
	print (a)
	if re.search("\w",a) and re.search("\@|\#|\$|\%|\^|\&|\*|\(\)|\_",a):
					
		print ("Password is Strong")
		o1.Pass=NewPass
		return True
	else:
		print ("Password is Weak")


def showall():
        db.execute("use bank")
        db.execute("select * from acc")
        for i in db:
                print(i)

print("Enter Choice \n1. Add New \n2. View Data ")
choice=int(input(""))
if choice==1:
        #Name,Place,Mobile,AccNo,Pass,Email
        name=input("Name:")
        place=input("Place: ")
        phno=input("Mobile: ")
        email=input("Email: ")



        o1=NewAccount(name,place,phno,AccNo(),passgen(),email)
        print("Account Number: ",o1.AccNo)
        print("User Name     : ",o1.Name)
        print("Phone Number  : ",o1.Mobile)
        print("Your OTP is ",OTP())
        print (o1.Pass)

        NewPass=input("Do you want to change your password: ")

        if NewPass=='yes':
                temppass=input("Enter your Current Password: ")
                if temppass==o1.Pass:
                        NewPass=input("Enter Your New Pass")
                        VerifyPass(NewPass)
                        print("New Pass : ", o1.Pass)
                        Insert()        

                else:
                        print("Wrong Password! Try again")
if choice==2:
        showall()
