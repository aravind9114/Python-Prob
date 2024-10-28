class Bank:
    
    def __init__(self,customer_id,customer_name,balance,wraw=0,dep=0):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.balance=balance
        self.wraw=wraw
        self.dep=dep
    
    def display_customer(self):
        print("=============DETAILS FUNCTION===============")
        print("Customer ID:{}".format(self.customer_id))
        print("Customer Name:{}".format(self.customer_name))
        print("Balance={}".format(self.balance))
    
    def withdraw(self,amount=0):
        amount=int(input("Enter amount to withdraw:"))
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("=============WITHDRAW FUNCTION===============")
            print("Amount Withdrawn={}".format(amount))
            print("New Balance={}".format(self.balance))
        else:
            print("=============WITHDRAW FUNCTION===============")
            print("insufficient fund!!!!!!")
    
    def deposit(self,amount=0):
        amount=int(input("Enter amount to deposit:"))
        self.balance=self.balance+amount
        print("=============DEPOSIT FUNCTION===============")
        print("Amount Deposited={}".format(amount))
        print("New Balance={}".format(self.balance))

c=Bank(1,"Akshay",2000)
print("================================BANKING=====================================")
n=0
while n!=4:
    print("1.View Account Details\n2.Withdraw Amount\n3.Deposit Amount\n4.Exit")
    n=int(input("Please Select an Operation:"))

    if n==1:
        c.display_customer()
    elif n==2:
        c.withdraw()
    elif n==3:
        c.deposit()
    elif n==4:
        print("\n********BYE************")
    else:
        print("Please select a valid operation")
