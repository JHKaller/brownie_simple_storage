from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange: Set up all the piece the we need to prepare.
    account = accounts[0]
    # Act: We define the functionality of our program.
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert: Define what the outcome should be.
    assert starting_value == expected


def test_updating_storage():
    # Arrange: Set up all the piece the we need to prepare.
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account}) #we deploy here since its part of the preperation
    # Act: We define the functionality of our program.
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Assert: Define what the outcome should be.
    assert expected == simple_storage.retrieve()

    #IF YOU ONLY WANT TO TEST ONE FUNCION: brownie test -k [function name]
    #brownie test --pdb --> to easily interact with functions
    #brownie test -s --> more detailed test result
    #brownie networks list --> Shows all available blockchains to deploy on.
        #Ethereum provides mainnet + testnet. Under Development you can deploy via Ganache but your applications will directly be scraped after running.