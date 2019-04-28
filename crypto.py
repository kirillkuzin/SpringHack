import web3
from web3 import Web3
from eth_account import Account
from cryptos import *

c = Bitcoin(testnet=True)
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/581ac5ee379c41e88b28e2cafe87421b"))

def generate_wallet(seed_phrase):
    private_key = sha256(seed_phrase)
    account = Account.privateKeyToAccount(private_key)
    public_key = account.address
    return private_key, public_key

def get_balance(public_key):
    balance_in_wei = w3.eth.getBalance(public_key)
    balance_in_ether = Web3.fromWei(balance_in_wei, "ether")
    return str(balance_in_ether)
