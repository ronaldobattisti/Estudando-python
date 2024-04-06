import os
from typing import List, Dict
from models.account import Account
import jsonpickle

FILE: str = "Chapter_26_Bank/files"
FILE_DATA: str = "C:/Users/RONAL/Desktop/Python/Programacao_python_do_basico_ao_avancado/Chapter_26_Bank/files/files.txt"


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
    return os.path.exists('files/files.txt')


def create_blank_file():
    open(FILE_DATA, 'w').close()


def load_from_file() -> List:
    accounts: List = []

    if file_exists():
        with open(FILE_DATA, 'r') as file:
            content = file.read().split('\n')
            for line in content:
                account = jsonpickle.decode(line)
                accounts.append(account)
    return accounts


def save_in_file(accounts: List) -> None:
    with open(FILE_DATA, 'w') as file:
        for account in accounts:
            file.write(jsonpickle.encode(account) + '\n')
