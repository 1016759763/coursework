import time
import random
import os
import pickle




def bankview():
    print("************************************************")
    print("*                                              *")
    print("*                                              *")
    print("*        Welcome to visual bank system         *")
    print("*                                              *")
    print("*                                              *")
    print("************************************************")

def banksysfunction():
    print("************************************************")
    print("*                                              *")
    print("*   [1]Create an account     [2]Login account  *")
    print("*                                              *")
    print("*   [3]Change password       [4]Lock account   *")
    print("*                                              *")
    print("*   [5]Unlock account        [0]Exit           *")
    print("*                                              *")
    print("************************************************")

def accountfuction():
    print("************************************************")
    print("*                                              *")
    print("*   [1]Account enquiry           [2]Deposit    *")
    print("*                                              *")
    print("*   [3]Withdraw fund             [4]Transfer   *")
    print("*                                              *")
    print("*   [5]Transaction history       [0]Exit       *")
    print("*                                              *")
    print("************************************************")

class Card:
    def __init__(self, cardID, cardPasswd, balance, cardLock, transaction_detail):
        self.cardID = cardID
        self.cardPasswd = cardPasswd
        self.balance = balance
        self.cardLock = cardLock
        self.transaction_detail = transaction_detail
        
class Transaction_detail:
    def __init__(self, Time, Type, amount):
        self.Time = Time
        self.Type = Type
        self.amount = amount

class Saving(Card):
    def __init__(self, cardID, cardPasswd, balance, transaction_detail, cardLock, types = 'Saving Account', transaction_fee = 1):
        super().__init__(cardID, cardPasswd, balance, cardLock, transaction_detail)
        self.types = types
        self.transaction_fee = transaction_fee
        
    def Saving_enquiry(self):
        print("account number: " + str(self.cardID))
        print("balance: " + str(self.balance))
        print("type : " + self.types)
        print("transaction fee : " + str(self.transaction_fee))
        
class Credit(Card):
    def __init__(self, cardID, cardPasswd, balance, transaction_detail, cardLock, types = 'Credit Account', interest_rate = 0.05, quota = 10000):
        super().__init__(cardID, cardPasswd, balance, cardLock, transaction_detail)
        self.types = types
        self.interest_rate = interest_rate
        self.quota = quota
        
    def Credit_enquiry(self):
        print("account number: " + str(self.cardID))
        print("balance: " + str(self.balance))
        print("type : " + str(self.types))
        print("quota : " + str(self.quota))
        print("interest rate : " + str(self.interest_rate))

class User:
    def __init__(self, name, email, phone, card, pin):
        self.name = name
        self.email = email
        self.phone = phone
        self.card = card
        self.pin = pin

    # def account_enquiry(self):
    #     print("account number: " + str(self.card.cardID))
    #     print("balance: " + str(self.card.balance))

    def withdraw(self):
        while True:
            amount = int(input("PLEASE ENTER WITHDRAW NUMBER: "))
            pin1 = input("PLEASE ENTER YOUR PIN: ")
            if (pin1 == self.pin) and (0 < amount <= self.card.balance):
                if not self.check_PIN(self.pin):
                    print("Incorrect PIN! The account will be locked! ")
                    self.card.cardLock = True
                    return -1
                self.card.balance -= amount
                self.card.transaction_detail.Time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                self.card.transaction_detail.Type.append(" WITHDRAW ")
                self.card.transaction_detail.amount.append(amount)
                print("Withdraw number: ", amount, "Current Balance: ", self.card.balance)
                return -1
            else:
                print("INVALID NUMBER! PLEASE ENTER AGAIN!")

    def deposit(self):
        while True:
            amount = int(input("PLEASE ENTER DEPOSIT NUMBER: "))
            pin1 = input("PLEASE ENTER YOUR PIN: ")

            if (amount < 0) or (pin1 != self.pin):
                print("INVALID NUMBER!  PLEASE TRY IT AGAIN !")
                return -1
            else:
                self.card.balance += amount
                self.card.transaction_detail.Time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                self.card.transaction_detail.Type.append(" DEPOSIT ")
                self.card.transaction_detail.amount.append(amount)
                print("DEPOSIT: ", amount, "Balance: ", self.card.balance)
                return -1
            

    def transfer(self,newuser):
        
        if not newuser:
            print("Sorry, the account is not exsit! Please check it! ")
            return -1
        if newuser.card.cardLock:
            print("Your target account has been locked! ")
            return -1
        while True:
            amount = float(input("Please enter an transfer amount : "))
            if (0 < amount <= 1000):
                if amount > self.card.balance:
                  print("Sorry, your account don't have enough money! Please confirm your balance: ")
                  return -1
                elif amount >= 0 and amount <= self.card.balance:
                    pin = input("ENTER YOUR PIN PLEASE : ")
                    if pin != self.pin:
                        print("Incorrectly! Your account will be locked!! ")
                        self.card.cardLock = True
                        return -1
                    else:
                        print("Vertification successful!")
                        print("Loading........")
                        time.sleep(2)
                        transaction_rate = 0.2
                        transaction_fee = transaction_rate * amount
                        left_money = amount - transaction_fee
                        self.card.balance -= left_money
                        newuser.card.balance += left_money
                        self.card.transaction_detail.Time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        self.card.transaction_detail.Type.append(" Transfer ")
                        self.card.transaction_detail.amount.append(-left_money)
                        newuser.card.transaction_detail.Time.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        newuser.card.transaction_detail.Type.append(" Transfer ")
                        newuser.card.transaction_detail.amount.append(+left_money)
                        print(" Transfer operation succeeded! Transfer amount : " + str(left_money) \
                          + " Balance: " + str(self.card.balance) + " Transaction fee: " + str(transaction_fee))
                        return -1
                else:
                    print("Invalid number! Please try again: ")
                    return -1
            else:
                print(" Invalid number! Please under 1000")
                return -1
    
    def transaction_enquiry(self):
        print(" Time: ", self.card.transaction_detail.Time)
        print(" Type: ", self.card.transaction_detail.Type)
        print(" Amount: ", self.card.transaction_detail.amount)
        
    def check_PIN(self, realPIN):
        for i in range(2,-1,-1):
            tempPIN = input("PLEASE ENTER YOUR PIN AGAIN: ")
            if tempPIN == realPIN:
                return True
            else:
                if i != 0:
                    print(" INCORRECTLY! " + " you have " + str(i) + " chance left!!! ")
                else: 
                    return False        
    

class Banksystem:
    def __init__(self, allUsers):
        self.allUsers = allUsers

    def creatUser(self):
        name = input("ENTER YOUR NAME PLEASE : ")
        email = input("ENTER YOUR EMAIL ADDRESS : ")
        phone = input("ENTER YOUR PHONE NUMBER PLEASE : ")
        prestoreMoney = int(input("ENTER THE MONEY YOU WANT TO SAVE : "))
        onePasswd = input("ENTER YOUR PASSWORD : ")
        while True:
            types = input("PLEASE SELECT CREDIT OR SAVING ACCOUNT : ")
            if not types.isalnum():
                print("The input is invalid. Please try again.")
            else:
                if not self.check_Passwd(onePasswd):
                    print("Failed to open account due to incorrect password.")
                    return -1
                else:
                    break

        cardStr = random.randint(1000000, 9999999)  # create seven digits number
        cardpin = random.randint(1000, 9999)
        transaction_detail = Transaction_detail([], [], [])
        if "s" in types.lower():
            card = Saving(cardStr, onePasswd, prestoreMoney, transaction_detail, False)
        elif "c" in types.lower():
            card = Credit(cardStr, onePasswd, prestoreMoney, transaction_detail, False)
        user = User(name, phone, email, card, str(cardpin))
        self.allUsers[str(cardStr)] = user

        print("Successful! PLEASE NOTE YOUR ACCOUNT NUMBER!", cardStr)
        print("THIS IS YOUR PIN NUMBER, SAVE IT!", cardpin)
                
    def check_Passwd(self, realPasswd):
        for i in range(2,-1,-1):
            tempPasswd = input("Please enter your Password number: ")
            if tempPasswd == realPasswd:
                return True
            else:
                if i != 0:
                    print("Incorrectly!" + "you have " + str(i) + " chance left.")
                else:
                    return False
                
    def check_PIN(self, realPIN):
        for i in range(2,-1,-1):
            tempPIN = input("Please enter your PIN number: ")
            if tempPIN == realPIN:
                return True
            else:
                if i != 0:
                    print("Incorrectly!" + "you have " + str(i) + " chance left.")
                else:
                    return False

    def login(self):
        accountnum = input("Please enter your account number: ")
        user = self.allUsers.get(accountnum)
        if not user:
            print("Sorry, the account does not exist.")
            return -1
        if user.card.cardLock:
            print("Sorry, the account is frozen. Please unlocked it.")
            return -1
        if not self.check_Passwd(user.card.cardPasswd):
            print("Incorrect PIN! The account will be locked.")
            user.card.cardLock = True
            return -1
        else:
            print("loading...")
            time.sleep(2)
            print("The account login succeeded.")
            return user
        

    def changepasswd(self):
        cardnum = input("PLEASE ENTER YOUR CARD ID: ")
        user = self.allUsers.get(cardnum)
        if not user:
            print("Sorry, the account is not exsit! ")
            return -1
        if user.card.cardLock:
            print("Sorry, your account has been locked ! Unlocked it please! ")
            return -1
        if not self.check_PIN(user.pin):
            print("Incorrect PIN! The account will be locked ! ")
            user.card.cardLock = True
            return -1
        print(" Vertification successful! ")
        while True:
            newpasswd = input("Enter your new password please: ")
            if newpasswd == user.card.cardPasswd:
                print("Don't enter the same password! Please try it again! ")
            else:    
                print("Loading.....")
                time.sleep(2)
                user.card.cardPasswd = newpasswd
                print("Successful!")
                return -1

    def lockaccount(self):
        cardnum = input("PLEASE ENTER YOUR CARD NUMBER : ")
        user = self.allUsers.get(cardnum)
        passwd = input("PASSWORD PLEASE: ")

        if not user:
            print("INVALID NUMBER!!! PLEASE CHECK AGAIN!")
            return -1
        if user.card.cardLock:
            print(" This card has been locked! Please connect with staff to unlock! ")
            return -1
        if passwd == user.card.cardPasswd:
            user.card.cardLock = True
            print("YOUR ACCOUNT HAS BEEN LOCKED!")
        else:
            print(" Invalid operation! ")
            return -1
        
    def unlock(self):
        accountnum = input(" PLEASE ENTER YOUR ACCOUNT NUMBER : ")
        user = self.allUsers.get(accountnum)
        if not user:
            print("Your account don't exist !")
            return -1
        if not user.card.cardLock:
            print(" Soryy, The account has been locked ! ")
            return -1
        if not self.check_PIN(user.pin):
            print(" Incorrectly PIN! Failed unlock!!")
            return -1
        else:
            print("Verification successful!! ")
            tempname = input(" Please enter your name: ")
            if tempname != user.name:
                print(" Vertification Failed! Check your name please: ")
                return -1
            else:
                temphone = input(" Please enter your phone number : ")
                if temphone != user.phone:
                    print(" Incorrectly! Check your phone number please : ")
                    return -1
                else:
                    tempemail = input(" Enter your email address please: ")
                    if tempemail != user.email:
                        print(" Error! Please enter right email address! ")
                        return -1
                    else:
                        print(" Loading ... ")
                        time.sleep(2)
                        print(" Vertification successful! The account unlock ! ")
                        user.card.cardLock = False
    
    def save(self):
        filepath = os.path.join(os.getcwd(), "allusers.txt")
        f = open(filepath, "w")
        f.write(str(self.allUsers))
        

def main():
    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filepath, "rb")
    allUsers = pickle.load(f)
    Bank = Banksystem(allUsers)
    
    bankview()

    while True:
        banksysfunction()
        option_banksysF = input("Please enter an operation: ")
        if option_banksysF == "1":
            Bank.creatUser()
            Bank.save()
        elif option_banksysF == "2":
            account_1 = Bank.login()
            if account_1 == -1:
                print("PLEASE TRY AGAIN:")

            else:
                while True:
                    accountfuction()
                    option_banksysF = input("Please enter an opertion option: ")
                    if option_banksysF == "1":
                        print(account_1.card.types)
                        if account_1.card.types == 'Credit Account':
                            account_1.card.Credit_enquiry()
                        elif account_1.card.types == 'Saving Account':
                            account_1.card.Saving_enquiry()
                        else:
                            print("Invalid types! Please check again! ")
                            return -1
                    elif option_banksysF == "2":
                        account_1.deposit()
                        Bank.save()
                    elif option_banksysF == "3":
                        account_1.withdraw()
                        Bank.save()
                    elif option_banksysF == "4":
                        if account_1.card.types == 'Saving Account':
                            newaccount = input("PLEASE ENTER TARGET ACCOUNT: ")
                            newuser = Bank.allUsers.get(newaccount)
                            account_1.transfer(newuser)
                            Bank.save()
                            
                        elif account_1.card.types == 'Credit Account':
                            print(" Sorry, Credit Account doesn't support transfer function!")
                            
                        else:
                            print("Invalid types! Check it again! ")
                            
                    elif option_banksysF == "5":
                        account_1.transaction_enquiry()
                        Bank.save()
                    elif option_banksysF == "0":
                        print("loading...")
                        time.sleep(2)
                        print("Logout successfully!")
                        break
                    else:
                        print("The input is invalid. Please try again")
        elif option_banksysF == "3":
            Bank.changepasswd()
            Bank.save()
        elif option_banksysF == "4":
            Bank.lockaccount()
            Bank.save()
        elif option_banksysF == "5":
            Bank.unlock()
            Bank.save()
        elif option_banksysF == "0":
            f = open(filepath, 'wb')
            pickle.dump(Bank.allUsers, f)
            f.close()
            print("Loading....")
            time.sleep(2)
            print("Bank system exit successfully!")
            return -1
        time.sleep(1)

if __name__ == "__main__":
    main()
