#предпосылки к пременению наследования
'''реализация класса savingaccount в соответствии с диаграмой выглядит след. образом'''
from distutils.command.check import check


class SavingsAccount:
    def __init__(self, account_nember, interest_rate, currency='USD'):
# иницилизация объекта сберегательного счета
        self.account_number= account_nember
        self.balance=0
        self.interest_rate=interest_rate
#процентная ставка
        self.currency=currency
#валюта
    def deposit(self, amount):
#внесение депозита на счет
        self.balance+=amount
    def withdraw(self, amount):
        '''снятие средств со счета'''
        if self.balance>= amount:
            self.balance-= amount
        else:
            print('Insufficient funds')
    def calculate_interest(self):
        '''расчет и начисления процентов на остаток по счету'''
        interest= self.balance * self.interest_rate
        self.balance+=interest
'''выполнять операцию со сберегательным счётом мы можем след. образом:'''
saving_account= SavingsAccount(account_nember='SAV=001',interest_rate=0.05, currency='USD')
'''использование методов класса'''
saving_account.deposit(1000)
'''внесение депозита на счет '''
saving_account.calculate_interest()
'''рассчет и начисления процентов'''
#выводим информацию о сберегательном счёте
print("Savings account №{}, balance: {}, interest rate: {}". format(
saving_account.account_number,
    saving_account.balance,
    saving_account.interest_rate))
#переходим к классу расчетного счета - ChekingAccout
class CheckingAccount:
    def __init__(self, account_number,
                 transaction_fee, currency='USD'):
        '''инициализация объекта расчетного счета'''
        self.account_number= account_number
        '''номер аккаунта'''
        self.balance= 0
        '''баланс'''
        self.transaction_fee=transaction_fee
        '''комисия за снятие'''
        self.currency= currency
        '''валюта'''
    def deposit(self,amount):
        '''внесение депозита на счет'''
        self.balance+=amount
    def withdraw(self,amount):
        '''снятие средств со счета'''
        if self.balance>= amount:
            self.balance-= amount
        else:
            print("Insufficient funds")
    def deduct_transaction_fee(self):
        '''вычет комиссии за транзакцию'''
        self.balance -= self.transaction_fee
#выполнять операции с расчетным счётом мы можем след. образом
checking_account= CheckingAccount(account_number="CHK-001",
                                  transaction_fee=2.50,
                                  currency="USD")
'''использование методов класса'''
checking_account.deposit(1000)
'''внесение депозита на счета'''
checking_account.withdraw(500)
'''снятие суммы со счета'''
print("Checking account № {}, balance: {}, transaction fee: {}". format(
    checking_account.account_number,
    checking_account.balance,
    checking_account.transaction_fee
))

