import sqlite3 
connect = sqlite3.connect('Bank.db')
cursor = connect.cursor()
from functions import generate_Account_Number,generate_pin,encrypt_pin


# cursor.execute("create table Accounts(name varchar(32) not null, Acc_num number(11) primary key, Gender varchar(6) not null, Mobile number(10) unique, aadhar number(12) unique, address varchar(40) not null, mail varchar(30) not null, dob date, Acc_type varchar(20) not null, nomine varchar(32), bal number default(1000), pin number default('0000'));")
# print('Table Created Successfully')

while True:
    print("*"*10,"Welcome to Naa Bank","*"*10)
    op = int(input("SELECCT THE BELOW OPTIONS \n1)Acc Creation \n2)Set Pin \n3)Check balance \n4)Deposit \n5)Withdraw \n6)Amount Transfer \n"))
    if op == 1:
        name = input('Enter Your Name:')
        Acc_num = generate_Account_Number()
        print('Your Account Number:',Acc_num)
        Mobile = input('Enter Your Mobile Number:')
        aadhar = input('Enter Your Aadhar Number: ')
        address = input('Enter Your Address: ')
        mail = input('Enter your Mail ID:')
        while True:
            Gender = input('Enter your Gender:')
            if Gender == 'Male':
                break
            elif Gender == 'Female':
                break
            elif Gender == 'Others':
                break
            else:
                print('Invalid Gender')
        dob = input('Enter Your Date of Birth: ')
        while True:
            Acc_type = input('Enter Account Type: \n1)Savings Account \n2)Current Account \n3)Joint Account \n5)Withdraw \n')
            if Acc_type == '1':
                Acc_type = 'Savings Account'
                break
            elif Acc_type == '2':
                Acc_type = 'Current Account'
                break
            elif Acc_type == '3':
                Acc_type = 'Joint Account'
                break
            else:
                print('Inavalid Account type')
        nomine = input('Enter Nomine Name: ')
        cursor.execute(f"INSERT into Accounts (name,Acc_num,Mobile,aadhar,address,mail,Gender,dob,Acc_type,nomine) values ('{name}','{Acc_num}','{Mobile}','{aadhar}','{address}','{mail}','{Gender}','{dob}','{Acc_type}','{nomine}')")
        connect.commit()
        print('Account Created Successfully')

    elif op == 2:
        Mobile = input('Enter Your Mobile Number:')
        aadhar = input('Enter Your Aadhar Number: ')
        cursor.execute(f"select Acc_num from Accounts where Mobile = '{Mobile}' and aadhar = '{aadhar}'")
        account = cursor.fetchone()
        if account :
            pin_num = generate_pin()
            print('Your Pin Number:',pin_num)
            cursor.execute(f"update Accounts set pin = '{encrypt_pin(pin_num)}' where Mobile = '{Mobile}' and aadhar = '{aadhar}'")
            connect.commit()

    elif op == 3:
        Acc_num = input('Enter Your Account Number: ')
        pin = input('Enter Your Pin: ')
        cursor.execute(f"select bal from Accounts where Acc_num = '{Acc_num}' and pin = '{encrypt_pin(pin)}'")
        bal = cursor.fetchone()
        if bal:
            print('Your Balance is:',bal[0])
        else:
            print('inavalid pin')

    elif op == 4:
        Acc_num = input('Enter the Account Number:')
        pin = input('Enter the pin:')
        data = cursor.execute(f"select bal from Accounts where Acc_num = '{Acc_num}' and pin = '{encrypt_pin(pin)}'").fetchone()
        balance = data[0]
        Deposit = int(input('Enter the Amount to Deposit:'))
        if Deposit >= 100:
            new_bal = balance + Deposit
            cursor.execute(f"update Accounts set bal = '{new_bal}' where Acc_num = '{Acc_num}' and pin ='{encrypt_pin(pin)}'")
            connect.commit()
            print('The Balance is:',balance)
        else:
            print('Enter the valid Amount')

    elif op == 5:
        Acc_num = input('Enter the Account Number:')
        pin = input('Enter the pin:')
        data = cursor.execute(f"select bal from Accounts where Acc_num = '{Acc_num}' and pin = '{encrypt_pin(pin)}'").fetchone()
        balance = data[0]
        withdraw = int(input('Enter the Amount to Withdraw:'))
        if withdraw >= 100:
            new_bal = balance - withdraw
            cursor.execute(f"update Accounts set bal = '{new_bal}' where Acc_num = '{Acc_num}' and pin = '{encrypt_pin(pin)}'")
            connect.commit()
            print('The Balance is:',balance)
        else:
            print('Enter the valid Amount')
            
    elif op == 6:
        f_Acc = input("Enter the Sender's Account Number:")
        pin = input('Enter the pin:')
        t_Acc = input("Enter the Reciever's Account Number:")
        Amount = int(input('Enter the Amount:'))
        cursor.execute(f"select bal from Accounts where Acc_num = '{f_Acc}' and pin = '{encrypt_pin(pin)}'")
        Sender = cursor.fetchone()
        if Amount >= 100:
            bal = Sender[0]
            new_bal = bal - Amount
            Sender = cursor.execute(f"update Accounts set bal = '{new_bal}' where Acc_num = '{f_Acc}' and pin = '{encrypt_pin(pin)}'")
            connect.commit()
            cursor.execute(f"select bal from Accounts where Acc_num = '{t_Acc}'")
            Reciever = cursor.fetchone()
            if Reciever:
                bal = Reciever[0]
                new_bal = bal + Amount
                Reciever = cursor.execute(f"update Accounts set bal = '{new_bal}' where Acc_num = '{t_Acc}'")
                connect.commit()
                print("Transaction Successful😊")
            else:
                print("Transaction Failed")
        else:
            print('Enter the valid amount')
    else:
        print("The Account Alredy Exists")