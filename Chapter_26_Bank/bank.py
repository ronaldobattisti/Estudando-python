
from utils import helper
from exceptions.exceptions import OutOfRangeException
from models.account import Account
from typing import List, Dict

# accounts: List = []


def main() -> None:
    if helper.file_exists():
        accounts = helper.load_from_file()
        Account.counter = helper.find_next_number(accounts)
    menu(accounts)


def menu(accounts: List[Account]) -> None:
    print(helper.return_menu())
    try:
        option = int(input())
        if option == 1:
            accounts = register_account(accounts)
            print(accounts)
            helper.save_in_file(accounts)
        elif option == 2:
            account_number = int(input("Select the account number: "))
            withdraw_value = float(input("Input the withdraw value: "))
            accounts = withdraw(account_number, withdraw_value, accounts)
        elif option == 3:
            account_number = int(input("Select the account number: "))
            deposit_value = float(input("Input the deposit value: "))
            accounts = deposit(account_number, deposit_value, accounts)
        elif option == 4:
            account_origin = int(input("Select the origin account number: "))
            account_destination = int(
                input("Select the destination account number: "))
            transfer_value = float(input("Input the transfer value: "))
            accounts = transference(
                account_origin, account_destination, transfer_value, accounts)
        elif option == 5:
            list_accounts(accounts)
        elif option == 6:
            exit(0)
        else:
            raise OutOfRangeException(option)
    except (ValueError, OutOfRangeException, UnboundLocalError) as err:
        print(f"Invalid value: {err}")
    menu(accounts)


def register_account(accounts) -> None:
    name: str = str(input("Write the client's name: "))
    if name_not_in_use(name, accounts):
        balance: float = float(input("Input the initial balance: "))
        ac = Account(name=name, balance=balance)
        accounts.append(ac)
    else:
        print("Name already in use")
    return accounts


def name_not_in_use(name: str, accounts: List[Account]) -> bool:
    buffer: bool = True
    for account in accounts:
        if account.name == name:
            buffer = False
    return buffer


def withdraw(account_number: int, withdraw_value: float, accounts: List[Account]) -> None:
    for item in accounts:
        if item.number == account_number:
            account = item
    if account.balance >= withdraw_value:
        account.balance -= withdraw_value
        print(f"You withdrew {withdraw_value} mangos")
    else:
        print(f"Not enought cash, strange! You have just {account.balance}")
    helper.save_in_file(accounts)
    return accounts


def deposit(account_number: int, deposit_value: float, accounts: List[Account]) -> None:
    for item in accounts:
        if item.number == account_number:
            account = item
    account.balance += deposit_value
    print(f"You deposited {deposit_value} pilas")
    helper.save_in_file(accounts)
    return accounts


def transference(account_origin: int, account_destination: int, transfer_value: float, accounts: List[Account]):
    for item in accounts:
        if item.number == account_origin:
            account_origin = item
        if item.number == account_destination:
            account_destination = item

    if account_origin.balance >= transfer_value:
        account_origin.balance -= transfer_value
        account_destination.balance += transfer_value
    else:
        print(
            f"Not enought cash, strange! You have just {account_origin.balance}")
    helper.save_in_file(accounts)
    print(f"{account_origin.name} transfered {transfer_value} to {account_destination.name}")
    list_accounts(accounts)
    return accounts


def list_accounts(accounts):
    for account in accounts:
        print(account)


if __name__ == '__main__':
    main()
