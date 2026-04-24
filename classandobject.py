####class student:
####    def __init__(self,name,id):
####        self.name=name
####        self.id=id
####
####    def display(self):
####        print(self.name,self.id)
####
####student_1=student("shyam",1212)
####student_1.display()
##'''
##Access Specifiers
##------------------
##
##1.Public
##Syntax-----name
##we can use it anywhere in the program
##2.protected
##syntax----
##this is only for internal use
##3.Private
##syntax---name
##this one is restricted
##
##Self
##-----
##-->This keyword is instance variable and unique for each object
##
##'''
##'''
##class some:
##    def __init__(self):
##        self.public="Public"
##        self.protected="protected"
##        self.private="private"
##user=some()
##print(user.public)
##print(user.protected)
##print(user.private)
##
##
####class car:
####    def __init__(self):
####        self.public="car"
####        self.protected="keys"
####        self.private="insurance"
####user=car()
####print(self.public)
####print(self.__protected)
####print(self.__private)'''
##
####class student:
####    def __init__(self):
####        self.name="mohan"
####        self._id=1234
####        
####user=student()
####print(user._id)
##
##
##
##
##
##
##
##
##class student:
##    def __init__(self):
##        self.name="mohsn"
##        self._marks=85
##class child(student):
##    def display(self):
##        print(self._marks)
##obj=child()
##obj.display()
##        
##
##
##
##
####class Student:
####    def __init__(self):
####        self._marks = 85   
####
####class Child(Student):
####    def display(self):
####        print(self._marks)
####
####obj = Child()
####obj.display()
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
check=0
while check==0:
    bank_num=input('1.SBI\n2.ICICI\n3.HDFC\n4.Axis\n5.Indian Bank\n6.BOI\nEnter the respective number of the bank you want to choose: ')
    if bank_num in '123456':
        bank_dict={'1':'SBI','2':'ICICI','3':'HDFC','4':'Axis','5':'Indian Bank','6':'BOI'}
        bank_name=bank_dict[bank_num]
        check=1
    else:
        print('Enter Valid Input')
        print('')
print('')
print(f'Create your {bank_name} Bank Account \n---------------------------------------------------------------')
your_name=input('Enter your name: ')
check=0
while check==0:
    your_pin=input('Enter your pin: ')
    if your_pin.isdigit()==True and len(your_pin)==4:
        check=1
    else:
        if your_pin.isdigit()==False:
            print('enter pin involving only numbers')
        else:
            print('enter 4-digit pin')
check=0
while check==0:
    your_balance=input('Enter your bank balance: ')
    if your_balance.isdigit()==True and len(your_balance)<6:
        your_balance=int(your_balance)
        check=1
    else:
        if your_balance.isdigit()==False:
            print('enter valid input')
        else:
            print('maximum balance can be 1 lakh exclusive')
bank_account={'name':your_name,'pin':your_pin,'balance':your_balance,'transaction_history': []}
print('')
print(f'Your Name: {your_name}\nYour Pin: {your_pin}\nYour Balance: {your_balance}')
print(f'Your {bank_name} Bank Account is Sucessfully Created \n---------------------------------------------------------------')
print('')
while(1):
    check=0
    while check<3:
        pin_entered=input('Enter your pin: ')
        if pin_entered==bank_account['pin']:
            check=4
        else:
            check+=1
            print(f'The pin you entered is incorrect, you have {3-check} attempts left')
    if check==3:
        print('Please contact customer care')
        exit()
    print('')
    check=0
    while check<3:
        functionality_num=input('HOME PAGE\n-------------------\n1.WithDraw\n2.Deposite\n3.Change Pin\n4.Transaction History\n5.Balance\nEnter the respective number of operation you want to perform: ')
        if functionality_num in '12345':
            check=4
        else:
            check+=1
            print(f'Enter valid input as mentioned you have {3-check} attempts left')
            print('')
    if check==3:
        print('Please contact customer care')
        exit()
    print('')
    if functionality_num=='1':
        check=0
        while check<3:
            withdraw_amount=input('Enter the Amount you want to WithDraw: ')
            if withdraw_amount.isdigit()==True:
                withdraw=int(withdraw_amount)
                if withdraw%100!=0:
                    print('You can WithDraw only in 100s')
                elif withdraw<=bank_account['balance']:
                    bank_account['balance']-=withdraw
                    print(f'{withdraw} Amount is WithDrawn Sucessfully')
                    balance=bank_account['balance']
                    bank_account['transaction_history'].append(f'{withdraw} Amount is WithDrawn Sucessfully and your bank balance is {balance}')
                    check=4
                else:
                    print('Insufficient Funds in your Bank Balance')
            else:
                check+=1
                print(f'Enter valid input as  mentioned you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='2':
        check=0
        while check<3:
            deposite_amount=input('Enter the Amount you want to Deposite: ')
            if deposite_amount.isdigit()==True:
                deposite=int(deposite_amount)
                if deposite%100!=0:
                    print('You can Deposite only in 100s')
                elif deposite>99999:
                    print('The maximum amount you can Deposite is 1 lakh exclusive')
                else:
                    bank_account['balance']+=deposite
                    print(f'{deposite} Amount is Deposited Sucessfully')
                    balance=bank_account['balance']
                    bank_account['transaction_history'].append(f'{deposite} Amount is Deposited Sucessfully and your bank balance is {balance}')
                    check=4
            else:
                check+=1
                print(f'Enter valid input as  mentioned you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='3':
        check=0
        while check<3:
            old_pin=input('Enter your old pin: ')
            if old_pin==bank_account['pin']:
                check=0
                new_pin=input('Enter your new pin: ')
                if new_pin.isdigit()==True and len(new_pin)==4:
                    check=0
                    re_enter_new_pin=input('Re enter your new pin: ')
                    if re_enter_new_pin==new_pin:
                        bank_account['pin']=new_pin
                        bank_account['transaction_history'].append(f'You have changed your old pin {old_pin} to new pin {new_pin}')
                        print(f'Your pin has changed to {new_pin} Successfully')
                        check=4
                    else:
                        check+=1
                        print(f'The pin you re entered is wrong, you have {3-check} attempts left')
                else:
                    check+=1
                    if new_pin.isdigit()==False:
                        print(f'Enter pin involving numbers, you have {3-check} attempts left')
                    else:
                        print(f'Pin should be of 4 digits, you have {3-check} attempts left')
            else:
                check+=1
                print(f'The pin you entered is incorrect, you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='4':
        print('Transaction History: ')
        if len(bank_account['transaction_history'])!=0:
            for i in bank_account['transaction_history']:
                print(i)
        else:
            print('you didnt perform any action')
        print('')
    else:
        balance=bank_account['balance']
        bank_account['transaction_history'].append(f'You checked your balance which is {balance}')
        print(f'Your Bank Balance: {balance}')
        print('')
    check=0
    while check<3:
        repeat=input('1.Home Page\n2.Exit\nEnter the respective number of operation you want to perform: ')
        if repeat=='1':
            print('---------------------------------------------------------------')
            print('')
            check=4
        elif repeat=='2':
            print(f'Thank you {your_name}')
            exit()
        else:
            check+=1
            print(f'Enter valid input as mentioned you have {3-check} attempts left')
            print('')
    if check==3:
        print('Please contact customer care')
        exit()




















##
##
##
