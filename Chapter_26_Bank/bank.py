
from utils import helper
from exceptions.exceptions import OutOfRangeException
from models.account import Account
from typing import List, Dict

accounts: List = []


def main() -> None:
    '''if helper.file_exists():
        accounts = helper.load_from_file()'''
    menu()


def menu() -> None:
    helper.return_menu()
    try:
        option = int(input())
        if option == 1:
            register_account()
            helper.save_in_file(accounts)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            list_accounts()
        elif option == 6:
            pass
        else:
            raise OutOfRangeException(option)
    except (ValueError, OutOfRangeException) as err:
        print(f"Invalid value: {err}")
    menu()


def register_account() -> None:
    name: str = str(input("Write the client's name: "))
    if name_not_in_use(name):
        balance: float = float(input("Input the initial balance: "))
        ac = Account(name=name, balance=balance)
        accounts.append(ac)
    else:
        print("Name already in use")


def name_not_in_use(name: str) -> bool:
    buffer: bool = True
    for account in accounts:
        if account.name == name:
            buffer = False
    return buffer


def withdraw():
    pass


def deposit():
    pass


def transference():
    pass


def list_accounts():
    for account in accounts:
        print(account)


def exit():
    pass


if __name__ == '__main__':
    main()
