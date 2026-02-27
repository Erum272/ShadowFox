def save_account(account):

    with open("data.txt", "a") as file:

        file.write(account.to_string())


def get_accounts():

    accounts = []

    try:

        with open("data.txt", "r") as file:

            for line in file:

                name, balance = line.strip().split(",")

                accounts.append((name, balance))

    except FileNotFoundError:

        pass

    return accounts


def overwrite_accounts(accounts):

    with open("data.txt", "w") as file:

        for name, balance in accounts:

            file.write(f"{name},{balance}\n")