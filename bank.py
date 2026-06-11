class Bank:
    def __init__(self, amount):
        self.amount = amount

    def getBalance(self):
        print("Current Balance is ", self.amount)

    def getDeposite(self, amount):
        self.amount = self.amount + amount

    def withdraw(self, amount):
        self.amount = self.amount - amount


# Create Object
myobj = Bank(1000)

myobj.getBalance()
myobj.getDeposite(90000)
myobj.getBalance()
myobj.withdraw(100000)
myobj.getBalance()
#creat object