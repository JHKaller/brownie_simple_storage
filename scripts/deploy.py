from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    #.env acc
    #account = accounts.add(config["wallets"]["from_key"])
    #If we want to work with a self-created account. 1. terminal --> brownie accounts new [name]. 2. this will prompt us to add a private key (remember to add 0x). 3. Once added it will create an account. Can be checked with brownie accounts list
    #account = accounts.load("[name]")
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



def main():
    deploy_simple_storage() 

#If I want to deploy on a test network.
#brownie run scripts/deploy.py --network rinkeby

#brownie console --> opens a shell in which I already have all imports and can just individually run code