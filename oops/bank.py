import datetime

class Bank:
    b_name="sbi"
    def create_account(self,accno,c_name,balance):
        self.accno=accno
        #self.bank_name=bank_name
        self.c_name=c_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(Bank.b_name,"a/c",self.accno,"credited with",amount,"on" ,datetime.datetime.now(),"available balance is",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed")
        else:
            self.balance-=amount
            print(Bank.b_name,"a/c",self.accno,"debited with",amount,"on",datetime.date.today(),"available balance is",self.balance)

        def balance_enq(self):
            print(self.balance)

obj=Bank()
obj.create_account(11001122,"Anu",500)
obj.deposit(1000)
obj.withdraw(400)
