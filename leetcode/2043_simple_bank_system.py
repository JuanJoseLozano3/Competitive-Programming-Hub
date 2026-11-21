class Bank:

    def __init__(self, balance: list[int]):
        self.listas = balance
        return None

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if(account1 > len(self.listas) or account2 > len(self.listas)):
            return False
        if(self.listas[account1-1]>=money):
            self.listas[account1-1]-=money
            self.listas[account2-1]+=money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if(account > len(self.listas)):
            return False
        self.listas[account-1]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if(account > len(self.listas)):
            return False
        if(self.listas[account-1]>=money):
            self.listas[account-1]-=money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)