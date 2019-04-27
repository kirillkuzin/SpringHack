from eth_account import Account
from cryptos import *

c = Bitcoin(testnet=True)

def generate_wallet(seed_phrase):
    private_key = sha256(seed_phrase)
    account = Account.privateKeyToAccount(private_key)
    public_key = account.address
    return private_key, public_key
