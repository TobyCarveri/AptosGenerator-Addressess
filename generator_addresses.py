"""before pip install aptos-sdk"""
import os
import csv
import pandas 
from aptos_sdk.account import Account


def gen_accounts(amount_wallets, prefix, name_file_csv: str, modes: str):
    wallets = []
    i = 0
    while amount_wallets != i: 
        acct = Account.generate()
        "Unlike the Web3.py library, after creation, you need a private key, address convert the address to str, since initially they go in their class"
        wallet = (str(acct.private_key) ,str(acct.address())) # <---------
        if prefix in str(acct.address):
            wallets.append(wallet)
        i += 1

        'Check different class'
        # print(type(acct.address()))
        # print(type(str(acct.address())))

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

"""1) amount adress 2) your prefix ex. 0xc0ffee.... (long time generate) 3) folder where create a privat key and wallets 4) Modificator for writting 
gen_accounts(1, '0x', './AptosFolder/testwallets/shitwalletsmake.csv', 'a')
