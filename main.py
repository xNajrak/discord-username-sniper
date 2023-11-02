import tls_client
from colorama import init,Fore,Back
import fade
import random
import string
import threading
import os
import ctypes

# CONFIG #
USERNAME_GENERATION_METHOD = "RANDOM" # DICTIONARY , RANDOM
RANDOM_METHOD_LENGTH = 3 # FOR RANDOM OPTION
RANDOM_METHOD_WHATUSE = "ALL" # ALL , STRING , NUMBER

DICTIONARY_API = "https://random-word-api.herokuapp.com/word"
THREADS = 250
# CONFIG #

init()
session = tls_client.Session(client_identifier="chrome_115", random_tls_extension_order=True)
with open('proxies.txt', 'r') as file:
    proxies = [line.strip() for line in file]
    file.close()
with open('tokens.txt', 'r') as file:
    tokens = [line.strip() for line in file]
    file.close()

class stats:
    checked = 0
    taken = 0
    sniped = 0
def updatetitle():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Nickname Sniper - Checked: {stats.checked} | Taken: {stats.taken} | Sniped: {stats.sniped}")
threading.Thread(target=updatetitle).start()

def checkUsername():
    username = generateUsername()
    url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed" #https://discord.com/api/v9/users/@me/pomelo-attempt
    headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                #"authorization": random.choice(tokens),
                "cache-control": "no-cache",
                "content-type": "application/json",
                "cookie": "__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US",
                "origin": "https://discord.com",
                "pragma": "no-cache",
                "referer": "https://discord.com/channels/@me",
                "sec-ch-ua": f'"Google Chrome";v="115", "Chromium";v="115", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            }
    jsondata = {
        "username": username
    }
    try:
        req = session.post(url, headers=headers, json=jsondata, proxy={
                "http": "http://" + random.choice(proxies),
                "https": "http://" + random.choice(proxies),
            })
    except:
        return
    if req.status_code == 200:
        stats.checked += 1
        checktaken = req.json()['taken']
        if checktaken == True:
            print(f" {Back.LIGHTRED_EX}  ✕  {Back.RESET} {Fore.WHITE}Username Taken - {username}")
            stats.taken += 1
        else:
            stats.sniped += 1
            print(f" {Back.LIGHTGREEN_EX}  ✓  {Back.RESET} {Fore.WHITE}Username Sniped - {username}")
            with open("output.txt", "a") as f:
                f.write(f"{username}\n")

def generateUsername():
    if USERNAME_GENERATION_METHOD == "DICTIONARY":
        response = session.get(DICTIONARY_API)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                word = data[0]
                return word
            else:
                characters = string.ascii_letters + string.digits
                return ''.join(random.choice(characters) for _ in range(RANDOM_METHOD_LENGTH))
        else:
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(RANDOM_METHOD_LENGTH))

    elif USERNAME_GENERATION_METHOD == "RANDOM":
        if RANDOM_METHOD_WHATUSE == "ALL":
            characters = string.ascii_letters + string.digits
        elif RANDOM_METHOD_WHATUSE == "STRING":
            characters = string.ascii_letters
        elif RANDOM_METHOD_WHATUSE == "NUMBER":
            characters = string.digits
        else:
            characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(RANDOM_METHOD_LENGTH))
    else:
        print("Invalid method....")
        print(f"{Fore.WHITE}Press any key...")
        os.system("pause > NUL")
        exit(1)

def loopThread():
    while True:
        checkUsername()
        
print(fade.pinkred(f"""
      •    ┓    ┏┏┓
┓┏┏┓┏┓┓┏┓┏┓┃┏  ━┫ ┫
┛┗┛┗┗┻┃┛ ┗┻┛┗   ┗┗┛
      ┛            
"""))
print(f"{Back.WHITE}{Fore.BLACK} Made with {Fore.LIGHTRED_EX}❤ {Fore.BLACK} for {Fore.LIGHTRED_EX}{Fore.BLACK}EVERYONE! {Back.RESET}")
print(f"{Back.WHITE}{Fore.BLACK} Created by {Fore.LIGHTRED_EX}xnajrak & sentire {Fore.BLACK} {Back.RESET}")
print(f"{Back.WHITE}{Fore.BLACK} Discord: {Fore.LIGHTRED_EX}xnajraczekk {Fore.BLACK} {Back.RESET}")
print(f"{Back.WHITE}{Fore.BLACK} https://github.com/xNajrak/discord-username-sniper {Back.RESET}")
threadsstarted = []
for _ in range(THREADS):
    thread = threading.Thread(target=loopThread)
    threadsstarted.append(thread)
    thread.start()
for th in threadsstarted:
    th.join()

print(f"{Fore.WHITE}Press any key...")
os.system("pause > NUL")
exit(1)
