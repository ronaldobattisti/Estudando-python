import os
from typing import List, Dict
from models.account import Account
import json

FILE: str = "Chapter_26_Bank/files"
FILE_DATA: str = "C:/Users/RONAL/Desktop/Python/Programacao_python_do_basico_ao_avancado/Chapter_26_Bank/files/files.json"


def cenvert_value(value: float) -> str:
    return f'R$ {value:,.2f}'


def return_menu() -> str:
    return '''
    ###############################
    ###### Select a option: #######
    ###############################
    1 - Create account
    2 - Withdraw
    3 - Deposit
    4 - Transference
    5 - List accounts
    6 - Exit
    '''


def file_exists():
    os.chdir(
        'C:/Users/RONAL/Desktop/Python/Programacao_python_do_basico_ao_avancado/Chapter_26_Bank/')
    return os.path.exists('files/files.json')


def create_blank_file():
    open(FILE_DATA, 'w').close()


def load_from_file() -> List:
    accounts: List[Account] = []

    if file_exists():
        with open(FILE_DATA, 'r') as file:
            content = json.load(file)
            for line in content:
                ac = Account(
                    number=line["number"], name=line["name"], balance=line["balance"])
                print(ac)
                accounts.append(ac)
    return accounts


def save_in_file(accounts: List[Account]) -> None:
    account_dict: Dict[Account] = {}
    accounts_json: List[Dict[Account]] = []
    for item in accounts:
        account_dict = {'number': item.number,
                        'name': item.name,
                        'balance': item.balance}
        accounts_json.append(account_dict)
    # print(accounts_json)
    with open(FILE_DATA, 'w') as file:
        json.dump(accounts_json, file, indent=4)


def find_accound_by_number(accounts: List[Account], number: int):
    for item in accounts:
        if item.number == number:
            account = item
    print(account)
    return account


def find_next_number(accounts: List[Account]) -> int:
    numbers_list: List[int] = []
    for item in accounts:
        numbers_list.append(item.number)
    next_number = max(numbers_list) + 1
    return next_number
