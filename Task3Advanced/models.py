class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = float(balance)


    def deposit(self, amount):

        self.balance += float(amount)

        return self.balance


    def withdraw(self, amount):

        if float(amount) > self.balance:

            return "Insufficient Balance"

        else:

            self.balance -= float(amount)

            return self.balance


    def to_string(self):

        return f"{self.name},{self.balance}\n"