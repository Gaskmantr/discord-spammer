import os
import requests
import random
import time

def banner():
    print("""
                             ____
                            / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __
                            \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ | '__|
                             ___) | |_) | (_| | | | | | | | | | | |  __| |
                            |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
                                  |_|
                                                                    Coded by GaskmanTR 1337 """)
    
banner()


print("""
[1]- Joiner     [3]- Leaver

[2]- Spammer    [4]- Checker

""")

while True:

    all_proxies = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all').text
    x = all_proxies.split()
    b = random.choice(x)



    sor = int(input("1 / 2 / 3 / 4:"))
    

    if sor == 1:

        invite = input("Lütfen sunucunu adresini giriniz :")
        with open("token.txt", "r") as f:
            for line in f:
                header = {
                    'authorization': line.strip("\n"),
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/79.0.3945.117 Safari/537.36'}

                deneme = {'http':'http://'+b}
                r = requests.post("https://discord.com/api/v8/invites/" + invite, headers=header, proxies=deneme)
                if r.status_code == 200:
                    print(str(r) + "Başarılı")


    elif sor == 2:
        idd = input("Lütfen kanal idsini giriniz :")
        message = input("Lütfen mesajınızı giriniz :")
        while True:
            with open("token.txt", "r") as f:
                for line in f:
                    header = {
                        'authorization': line.strip("\n"),
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/79.0.3945.117 Safari/537.36'}
                    deneme = {'http': 'http://' + b}
                    r = requests.post("https://discordapp.com/api/v6/channels/" + idd + "/messages", json={'content': message},headers=header, proxies=deneme)
                    print(r)



    elif sor == 3:
        leave = input("Lütfen sunucunu idisini giriniz :")

        with open("token.txt", "r") as f:
            for line in f:
                header = {
                    'Authorization': line.strip("\n"),
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/79.0.3945.117 Safari/537.36'}
                deneme = {'http': 'http://' + b}
                r = requests.delete("https://canary.discordapp.com/api/v6/users/@me/guilds/" + leave, headers=header,proxies=deneme)
                print(r)


    elif sor == 4:
        invite = input("Lütfen sunucunu adresini giriniz :")
        with open("token.txt", "r") as f:
            for line in f:
                header = {
                    'authorization': line.strip("\n"),
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/79.0.3945.117 Safari/537.36'}

                deneme = {'http':'http://'+b}
                r = requests.post("https://discord.com/api/v8/invites/" + invite, headers=header, proxies=deneme)
                if r.status_code == 200:
                    print(line)
    else:
        print("Geçersiz cevap.")

