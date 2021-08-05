class Account:
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        self.__balance = balance # __ 속성은 비공개

    def deposit(self, amount):
        if amount + self.__balance >= 10000000:
            print('잔액이 1000만원 이상이면 입금할 수 없습니다.')
            return
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount
    
    def __str__(self):
        return f'계좌번호: {self.ano}, 소유주: {self.owner}, 잔액: {self.__balance:9,d}'