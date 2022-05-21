import requests

def transaction_for_address(address):
    url = f"https://api.covalenthq.com/v1/1/address/{address}/transactions_v2/?key=ckey_eb29565e970e4b46930dca374df"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data1 = response.json()
        return data1
    else:
        return 'error'

def transaction(hash):
    url= f"https://api.covalenthq.com/v1/1/transaction_v2/{hash}/?key=ckey_eb29565e970e4b46930dca374df"
    response = requests.request("GET", url)
    if response.status_code == 200:
        data1 = response.json()
        return data1
    else:
        return 'error'

