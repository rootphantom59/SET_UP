import os,sys,time,json,random,re,string,platform,base64,uuid,getpass
#----color------#
black="\033[0;30m"       # Black
red="\033[0;31m"         # Red
green="\033[0;32m"       # Green
yellow="\033[0;33m"      # Yellow
blue="\033[0;34m"        # Blue
purple="\033[0;35m"      # Purple
cyan="\033[0;36m"        # Cyan
white="\033[0;37m"       # White

# Bold
bblack="\033[1;30m"      # Black
bred="\033[1;31m"        # Red
bgreen="\033[1;32m"      # Green
byellow="\033[1;33m"     # Yellow
bblue="\033[1;34m"       # Blue
bpurple="\033[1;35m"     # Purple
bcyan="\033[1;36m"       # Cyan
bwhite="\033[1;37m"      # White

#-----clear def---#
def clear():
    os.system('clear')

from os import system as _SUYAIB_
print('\033[1;92m>_𝗖𝗛𝗘𝗔𝗞𝗜𝗡𝗚 𝗨𝗣𝗗𝗔𝗧𝗘...')
os.system('espeak -a 300 "cheaking update" > /dev/null 2>&1')
os.system('git pull > /dev/null 2>&1')
os.system('pip install bs4 requests mechanize > /dev/null 2>&1')

print('\033[1;92m>_𝗜 𝗔𝗠 𝗧𝗘𝗥𝗠𝗨𝗫 𝗙𝗨𝗟𝗟 𝗦𝗘𝗧𝗨𝗣 𝗧𝗢𝗢𝗟𝗦...')
os.system('espeak -a 300 "I am termux full setup tools" > /dev/null 2>&1')

print('\033[1;92m>_𝗜 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗧𝗜𝗞𝗨𝗥 𝗥𝗔𝗛𝗠𝗔𝗡...')
os.system('espeak -a 300 "I made by Atikur Rahman" > /dev/null 2>&1')

print('\033[1;92m>_𝗔𝗧𝗜𝗞𝗨𝗥 𝗥𝗔𝗛𝗠𝗔𝗡 (𝗥𝗢𝗕𝗢𝗧) 𝗦𝗬𝗦𝗧𝗘𝗠 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗜𝗡𝗚...\033[1;30m')
os.system('espeak -a 300 "Atikur Rahman robot system installing" > /dev/null 2>&1')

print('\033[1;92m>_𝗥𝗢𝗕𝗢𝗧 𝗜𝗡𝗦𝗧𝗔𝗟𝗟 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘..{v}\033[1;30m')
os.system('espeak -a 300 "Robot install complete" > /dev/null 2>&1')

print('\033[1;92m>_𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗟𝗢𝗔𝗗𝗜𝗡𝗚...\033[1;30m')
os.system('espeak -a 300 "PLEASE WAIT FOR LOADING..." > /dev/null 2>&1')
time.sleep(1)

logo = """\033[1;36m
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
"""

menu = ("""\033[1;36m
[01]—𝗧𝗘𝗥𝗠𝗨𝗫 𝗕𝗔𝗦𝗜𝗖 𝗦𝗘𝗧𝗨𝗣
[02]—𝗧𝗘𝗥𝗠𝗨𝗫 𝗙𝗨𝗟𝗟 𝗦𝗘𝗧𝗨𝗣
[03]—𝗢𝗨𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟
[04]—𝗠𝗬 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗
[05]—𝗠𝗬 𝗪𝗛𝗔𝗧𝗦 𝗔𝗣𝗣 𝗜𝗗
[00]—𝗧𝗘𝗥𝗠𝗨𝗫 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡
""")

def lock():
    os.system('clear')
    option = input("""
 🔐ENTER PASSWORD: """)
    if option in ['emon']:
        os.system('clear')
        moon()
    else:
        print("🤫SORRY...YOU ARE WRONG PERSON...")

def moon():
    print(logo)
    print(menu)
    xd = input("\x1b[1;92m[✓]\x1b[1;92m_SELECT OPTION: ")
    if xd in ['1','01','A','a']:
        print('\x1b[1;92m{TERMUX BASIC SETUP STARTING...}')
        basic()
        print('\x1b[1;92m{TERMUX BASIC SETUP COMPLETE}')
    if xd in ['2','02','B','b']:
        print('\x1b[1;92m{TERMUX FULL SETUP STARTING...}')
        full()
        print('\x1b[1;92m{TERMUX FULL SETUP COMPLETE}')
    if xd in ['3','03','C','c']:
        print('🤑PLEASE WAIT......')
        channel()
        print('🤑LOADING SUCCESSFULL...')
    if xd in ['4','04','D','d']:
        print('🤑PLEASE WAIT......')
        telegram()
        print('🤑LOADING SUCCESSFULL...')
    if xd in ['5','05','E','e']:
        print('🤑PLEASE WAIT......')
        whats()
        print('😭LOADING UNSUCCESS...')
    if xd in ['0','00']:
        permission()

def basic():
    os.system('termux-setup-storage')
    os.system('')
    pkg_update = "pkg update"
    pkg_upgrade = "pkg upgrade"
    os.system(pkg_update)
    os.system(pkg_upgrade)
    os.system('pkg install python')
    os.system('pkg install python2')
    os.system('pkg install python3')
    os.system('pkg install wget')
    os.system('pkg install git')
    os.system('pkg install bash')
    os.system('pkg install python-pip')
    os.system('pip2 install wget')
    os.system('pip install bs4')
    os.system('pip2 install bs4')
    os.system('pip install requests')
    os.system('pip2 install requests')
    os.system('pip install mechanize')
    os.system('pip2 install mechanize')
    os.system('pkg install php')
    os.system('pip install php')
    os.system('pip2 install php')

def full():
    os.system("termux-setup-storage")
    os.system('')
    pkg_update = "pkg update"
    pkg_upgrade = "pkg upgrade"
    os.system(pkg_update)
    os.system(pkg_upgrade)
    os.system('pkg install python')
    os.system('pkg install python2')
    os.system('pkg install python3')
    os.system('pkg install python-pip')
    os.system('pkg install wget')
    os.system('pkg install fish')
    os.system('pkg install ruby')
    os.system('pkg install help')
    os.system('pkg install git')
    os.system('pkg install dnsutils')
    os.system('pkg install php')
    os.system('pkg install perl')
    os.system('pkg install lua')
    os.system('pkg install parallel')
    os.system('pkg install nmap')
    os.system('pkg install bash')
    os.system('pkg install clang')
    os.system('pkg install nano')
    os.system('pkg install w3m')
    os.system('pkg install hydra')
    os.system('pkg install figlet')
    os.system('pkg install cowsay')
    os.system('pkg install curl')
    os.system('pkg install tar')
    os.system('pkg install zip')
    os.system('pkg install unzip')
    os.system('pkg install net-tools')
    os.system('pkg install tor -y')
    os.system('pkg install sudo -y')
    os.system('pkg install wireshark')
    os.system('pkg install wgetrc')
    os.system('pkg install wcalc')
    os.system('pkg install openssl')
    os.system('pkg install openssl-tool')
    os.system('pkg install bmon')
    os.system('pkg install vpn')
    os.system('pkg install unrar')
    os.system('pkg install toilet')
    os.system('pkg install proot')
    os.system('pkg install net-tools')
    os.system('pkg install vim')
    os.system('pkg install vim-python')
    os.system('pkg install ired')
    os.system('pkg install goaccess')
    os.system('pkg install golang')
    os.system('pkg install tmux')
    os.system('pkg install kibi')
    os.system('pkg install tsu')
    os.system('pkg install mtools')
    os.system('pkg install file')
    os.system('pkg install vis')
    os.system('pkg install pass')
    os.system('pkg install pick')
    os.system('pkg install chroot')
    os.system('termux-chroot')
    os.system('pkg install macchanger')
    os.system('pkg install ninja')
    os.system('pkg install elixir')
    os.system('pkg install fakeroot')
    os.system('pkg install swift')
    os.system('pkg install xmlstarlet')
    os.system('pkg install netcat')
    os.system('pkg install texinfo')
    os.system('pkg install wren')
    os.system('pkg install cvs')
    os.system('pkg install gatling')
    os.system('pkg install ffmpeg')
    os.system('pkg install screen')
    os.system('pkg install neofetch')
    os.system('pkg install mariadb')
    os.system('pkg install picolisp')
    os.system('pkg install cmatrix')
    os.system('pkg install dropbear')
    os.system('pkg install openssh')
    os.system('pkg install python-pip')
    os.system('pip2 install wget')
    os.system('pip install bs4')
    os.system('pip2 install bs4')
    os.system('pip install requests')
    os.system('pip2 install requests')
    os.system('pip install mechanize')
    os.system('pip2 install mechanize')
    os.system('pip install php')
    os.system('pip2 install php')

def channel():
    os.system('xdg-open https://t.me/Anonymous_Phantom_BD')
def telegram():
    os.system('xdg-open @ROOT_PHANTOM_BPBD')
def whats():
    print('SORRY FOR THAT')
def permission():
    os.system('termux-setup-storage')

lock()
