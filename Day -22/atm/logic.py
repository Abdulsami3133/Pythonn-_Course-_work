data = {
    123456:{'name':"sami",'pin':1234,'balance':5000,'history':[]},
    234567:{'name':"Zaib",'pin':3133,'balance':6000,'history':[]},
    345678:{'name':"Sajid",'pin':3121,'balance':4000,'history':[]}
}

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")

def menu():
    print(f"Welcome to the ATM, {data[acc_num]['name']}")
    print('[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')

def checkbalance():
    print(f"Hello {data[acc_num]["name"]},")
    print("Current Balance:",data[acc_num]["balance"],end='\n\n')

def deposit():
    amount = int(input("Enter the Amount to deposit: "))
    data[acc_num]["balance"]+=amount
    data[acc_num]["history"].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")
    checkbalance()

def withdraw():
    amount = int(input("Enter the amount to be Withdraw: "))
    if data[acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["history"].append(f"{amount} is Withdraw")
        print(f"{amount} is withdraw Successfully")
        checkbalance()
    else:
        print("Insufficient Balance")


def viewtransaction():
    if data[acc_num]["history"]:
        print("=============== Transaction History ===========")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("=========== End of the Transactions ==========") 
    else:
        print("No Transaction History")           