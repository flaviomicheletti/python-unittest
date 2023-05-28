import unittest
from unittest.mock import MagicMock


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name


class BankTransaction:
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount

    def execute(self):
        try:
            self.source.withdraw(self.amount)
            self.destination.deposit(self.amount)
        except ValueError:
            return False
        return True


class TestBank(unittest.TestCase):
    def test_bank_account_deposit(self):
        account = BankAccount("John")
        assert account.get_name() == "John"
        assert account.get_balance() == 0

        account.deposit(100)
        assert account.get_balance() == 100

    def test_bank_account_withdraw(self):
        account = BankAccount("John", 100)
        account.withdraw(50)
        assert account.get_balance() == 50

    def test_bank_account_insufficient_funds(self):
        source = BankAccount("John", 100)

        with self.assertRaises(ValueError):
            source.withdraw(200)

    def test_bank_transaction_execute_success(self):
        source = BankAccount("John", 100)
        destination = BankAccount("Mary", 200)

        transaction = BankTransaction(source, destination, 10)

        assert transaction.execute() == True
        assert source.get_balance() == 90
        assert destination.get_balance() == 210

    def test_bank_transaction_execute_failure(self):
        source = BankAccount("John", 100)
        destination = BankAccount("Mary")

        transaction = BankTransaction(source, destination, 120)

        assert transaction.execute() == False
        assert source.get_balance() == 100
        assert destination.get_balance() == 0

#
# 100%
#