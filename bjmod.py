class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

        print (f'Hi {owner}, welcome to Banco De Maretima! You have a balance of {balance}.')


    def dep(self,amt):
        self.balance = self.balance + amt
        print(f'Thanks for your deposit of {amt}, {self.owner}.Your current balance is {self.balance}')

    def withd(self,amt):
        if amt < self.balance:
            self.balance = self.balance - amt
            print (f'Hi {self.owner}. You have made a withdrawal of {amt}, your new balance is {self.balance}')
        else:
            print ('Call yo mama, you outta money!')
    def currbal(self):
        self.balance
        print (self.balance)

    def __int__(self):
         return self.balance
    def reset(self):
        self.balance = 0