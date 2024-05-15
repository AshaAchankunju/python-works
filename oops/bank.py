class Bank:
    ac_num:int
    name:str
    ac_type:str
    ifsc_code:int
    branch:str
    balance:int
    dep_amount:int
    wdraw_amt:int

    def create_accnt(self,ac_num,name,ac_type,ifsc_code,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance
       
    
    def deposit_amt(self,dep_amount):
        self.balance+=dep_amount
        print("available balance: ",self.balance)

    def withdraw_amt(self,wdraw_amt):
        if wdraw_amt>self.balance:
            print("insufficient balance")
        else:
            self.balance-=wdraw_amt
            print(f"{self.ac_num} has been debited with {wdraw_amt}, available balance: {self.balance}")
    def get_balance(self):
        print("your available balance= ",self.balance)

cust1=Bank()
cust1.create_accnt(1234,"Asha","savings",15427,"kollam",50000)
cust1.deposit_amt(50000)
cust1.withdraw_amt(10000)
cust1.get_balance()
