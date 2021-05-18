operations = 0

class Atm(object):
    def __init__(self, pinNumber, cardNumber, balance):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
        self.balance = balance
    def withdraw(self):
        withdrawalAmount = int(input("How much do you want to withdraw?"))
        print(int(withdrawalAmount),"withdrawed from your balance.")
        self.balance = self.balance - withdrawalAmount
        choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.")
    def deposit(self):
        depositAmount = int(input("How much do you want to deposit?"))
        print(int(depositAmount),"deposited into your balance.")
        self.balance = self.balance + depositAmount
        choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.")
    def enquiry(self):
        print("You have ",self.balance," in your account.")
        choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.")
myCard = Atm("2832","498-6923-3492",700)

atmCards = [
    myCard
]

# while choices != '1':
#     choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.") 
# while choices != '2':
#     choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.")    
# while choices != '3':
#     choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.")       

choices = input("Which operation do you want to perform? \n Type in '1' to withdraw. \n Type in '2' to deposit. \n Type in '3' to check your balance.") 

if(choices == '1'):
    myCard.withdraw()
elif(choices == '2'):
    myCard.deposit()
elif(choices == '3'):
    myCard.enquiry()

