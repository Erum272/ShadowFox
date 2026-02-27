from models import BankAccount
from utils import save_account, get_accounts, overwrite_accounts


def create_account():

    name = input("Enter Account Holder Name: ")
    balance = input("Enter Initial Balance: ")

    account = BankAccount(name, balance)

    save_account(account)

    print("✅ Account Created Successfully")


def view_accounts():

    accounts = get_accounts()

    if not accounts:

        print("No accounts found")

    else:

        print("\n--- Account List ---")

        for name, balance in accounts:

            print("Name:", name, "| Balance:", balance)


def deposit_money():

    name = input("Enter account name: ")
    amount = input("Enter deposit amount: ")

    accounts = get_accounts()

    updated = []

    for acc_name, balance in accounts:

        if acc_name.lower() == name.lower():

            account = BankAccount(acc_name, balance)

            new_balance = account.deposit(amount)

            updated.append((acc_name, new_balance))

            print("💰 Deposit Successful")

        else:

            updated.append((acc_name, balance))

    overwrite_accounts(updated)


def withdraw_money():

    name = input("Enter account name: ")
    amount = input("Enter withdraw amount: ")

    accounts = get_accounts()

    updated = []

    for acc_name, balance in accounts:

        if acc_name.lower() == name.lower():

            account = BankAccount(acc_name, balance)

            result = account.withdraw(amount)

            if result == "Insufficient Balance":

                print(result)

                updated.append((acc_name, balance))

            else:

                updated.append((acc_name, result))

                print("💸 Withdrawal Successful")

        else:

            updated.append((acc_name, balance))

    overwrite_accounts(updated)


while True:

    print("\n=== Bank Management System ===")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        deposit_money()

    elif choice == "4":
        withdraw_money()

    elif choice == "5":
        break

    else:
        print("Invalid choice")