from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    # always gives me the newest state of the contract (i.e. favourite number) (whenever I update it, it will be stored on the blockchain, even the old versions)
    #ABI, Address is all stored within brownie



def main():
    read_contract()