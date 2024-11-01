import random
from data import bank
def if_new_user(response):
    if response == "n":
        print("Thank you. Visit us again.")
    else:
        new_dict={}
        new_name=input("PLease enter your name:")
        new_dict['account_holder_name']=new_name
        new_account_number=random.randint(100000, 999998)
        new_dict['account_number']=new_account_number
        balance_amount=float(input("Enter a balance amount:"))
        while balance_amount < 2500:
            amount_remaining = float(2500) - balance_amount
            balance_added = float(input(f"Enter Rs.{amount_remaining} more as minimum deposit"))
            balance_amount+=balance_added
        new_dict['balance']= balance_amount


        bank.append(new_dict)
        print("New account has been created.")
        print(new_dict)

def deposit(acc_no):
    dep_amount = float(input("Please enter the amount of money to be deposited."))
    for i in bank:
        if i['account_number'] == int(acc_no):
            new_amount = dep_amount + i['balance']
            i['balance'] = new_amount
            break

    print(f"Amount of Rs.{dep_amount} has been deposited to your account.")
    print(f"Your current balance is Rs.{new_amount}")
    print(i)

def withdraw(acc_no):
    withdraw_amount = float(input("Please enter the amount of money to be withdrawn. "))
    for dict in bank:
        if dict['account_number'] == int(acc_no):
            if dict['balance'] < withdraw_amount:
                print("Sorry! Your account doesn't have the necessary amount of balance.")
            else:
                new_amount = dict['balance']- withdraw_amount
                dict['balance'] = new_amount
                print(f"Amount of Rs.{withdraw_amount} has been withdrawn from your account")
                print(f"Your current balance is Rs.{dict['balance']}.")
                print(dict)


print("----Welcome To SBI Bank----")
print("")
print("Are U an Existing User ??")
print("")
print("Press: Y-> Yes     N-> No")
print("")
a = input("Enter your response: ")
flag = 0
while (1):
    if a.upper() == 'Y':
        break
    elif a.upper() == 'N':
        break
    else:
        print("")
        print("Please enter a valid Response")
        print("")
        print("Are U an Existing User ??")
        print("")
        print("Press: Y-> Yes     N-> No")
        print("")
        a = input("Enter your response: ")
if a.upper() == 'Y':
    print("Ok,Nice to Know")
    print("")
    count = 5
    acc_num = input("Please Enter Your Account Number: ")
    while len(acc_num) != 6 and count != 0:
        acc_num = input("Please Enter a Valid Account Number:")
        count = count - 1
    if count == 0:
        print("Hmm...Looks like U are Not an Acoount Holder.. :( ")
        print("")
        print("Would You Like to Create a New Bank Account?? ")
        print("")
        print("Press: Y-> Yes     N->No")
        print("")
        b = input("Enter your response: ")
        while (1):
            if b.upper() == 'Y':
                break
            elif b.upper() == 'N':
                break
            else:
                print("!!!Please Enter a Valid Response!!!")
                print("")
                print("Would You Like to Create a New Bank Account?? ")
                print("")
                print("Press: Y-> Yes     N-> No")
                print("")
                b = input("Enter your response: ")
        if b.upper() == 'Y':
            if_new_user()
        else:
            print("Thank You Visit Again")
    else:
        for p in bank:
            if p['account_number'] == int(acc_num):
                flag=1
                print("::::Your ACCOUNT::::")
                print("")
                print(p)
                print(":::::::::::::::::::::")
                print("")
                print("Please Choose your Action:")
                print("")
                print("Press: 1-> Withdrawl    2-> Deposit")
                res = int(input("Enter your Response: "))
                while (1):
                    if res == 1:
                        break
                    elif res == 2:
                        break
                    else:
                        print("!!!Please enter a Valid Response!!!")
                        print("")
                        print("::::Your ACCOUNT::::")
                        print("")
                        print(p)
                        print(":::::::::::::::::::::")
                        print("")
                        print("Please Choose your Action:")
                        print("")
                        print("Press: 1-> Withdrawl    2-> Deposit")
                        res = int(input("Enter your Response: "))

                if res == 1:
                    withdraw(acc_num)
                    break
                else:
                    deposit(acc_num)
                    break
        if flag == 0:
            print("Account number doesn't match with existing accounts.")
            print("..")
            print("Would You Like to Create a New Bank Account?? ")
            print("")
            print("Press: Y-> Yes     N->No")
            print("")
            b = input("Enter your response: ")
            while (1):
                if b.upper() == 'Y':
                    break
                elif b.upper() == 'N':
                    break
                else:
                    print("!!!Please Enter a Valid Response!!!")
                    print("")
                    print("Would You Like to Create a New Bank Account?? ")
                    print("")
                    print("Press: Y-> Yes     N-> No")
                    print("")
                    b = input("Enter your response: ")
            if b.upper() == 'Y':
                if_new_user(b)
            else:
                print("Thank You Visit Again")

elif a.upper() == 'N':
    r = input("Would You like to create a new Bank Account? Type Y -> Yes N -> No. ").lower()
    if_new_user(r)

f=open("data.py","w")
f.writelines("bank = ")
con = str(bank)
for i in con:
    if i == '{':
        f.writelines("\n{")
    else:
        f.writelines(i)
f.close()