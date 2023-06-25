"""перед всем этим вам нужно установить pip install aptos-sdk"""
import os
import csv
import pandas 
from aptos_sdk.account import Account
from aptos_sdk.client import  RestClient


NODE_URL = os.getenv("APTOS_NODE_URL", "https://rpc.ankr.com/http/aptos/v1")
rest_client = RestClient(NODE_URL)

import os
import csv
import pandas 
from aptos_sdk.account import Account
from aptos_sdk.client import  RestClient


NODE_URL = os.getenv("APTOS_NODE_URL", "https://rpc.ankr.com/http/aptos/v1")
rest_client = RestClient(NODE_URL)


def gen_accounts(amount_wallets, prefix, name_file_csv: str, modes: str):
    wallets = []
    i = 0
    while amount_wallets != i: 
        acct = Account.generate()
        "В отличии от Web3.py библиотеки, сдесть после создания нужно приватник, адресс превести в str так как изначально они идут в своем классе"
        wallet = (str(acct.private_key) ,str(acct.address())) # <---------
        if prefix in str(acct.address):
            wallets.append(wallet)
        i += 1

        'Просмотр классов'
        print(type(acct.address()))
        print(type(str(acct.address())))

    if len(wallets) != 0:
        with open(name_file_csv, mode=modes) as file:
            writer = csv.writer(file)
            if modes == 'w':
                writer.writerow(['private key', 'address'])
            for i in wallets:
                writer.writerow(i)
        print(f'Create: {len(wallets)} wallets')
        # Возвращает путь к файлу
        return name_file_csv
    else:
        print('No created')

"""1) колво адрессов 2) Желаемые префиксы 3) путь по которому будет сохранена таблица (сама создаеться) 4) модификатор записи не трогать"""
gen_accounts(1, '0x', './AptosFolder/testwallets/shitwalletsmake.csv', 'a')
