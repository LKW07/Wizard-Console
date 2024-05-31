import os, time, string, random

path = os.getcwd() + "/"
s_path = os.getcwd() + "/" + "_internal" + "/"

os.system("cls")
os.system("color 7")

def info():
    os.system("cls")
    print("Wizard-Console [Version 1.0.0 - 24.05.2024]")
    print("(c) Leander Weiss. Alle Rechte vorbehalten", end="\n\n")

def help():
    print("help - Zeigt diese Hilfe an")

def getCommand():
    c_path = os.getcwd()
    cmd = input(f"{c_path}>")
    return cmd

def commands(cmd):
    if cmd.startswith("cd") == True:
        try:
            os.chdir(cmd[3:])
        except:
            print("path not found")
    
    elif cmd.startswith("mkdir") == True:
        os.mkdir(cmd[6:])
    
    elif cmd.startswith("echo") == True:
        print(cmd[5:])
    
    elif cmd.startswith("del") == True:
        os.remove(cmd[3:])
    
    elif cmd.startswith("ls") == True:
        #print(os.listdir())
        out = os.system("dir")
    
    elif cmd.startswith("cls") == True or cmd.startswith("clear") == True:
        os.system("cls")
    
    elif cmd.startswith("rs") or cmd.startswith("update") == True:
        os.system("cls")
        pid = os.getpid()
        os.system(f"start cmd /k python3 {path}main.py & taskkill /PID {pid} /F")
        #info()
    
    elif cmd.startswith("start"):
        os.system("start")
    
    elif cmd == "exit":
        exit
    
    
    elif cmd == "info":
        info()
    
    
    elif cmd == "help":
        help()
        
    
    else:
        spezial(cmd)

def spezial(cmd):
    if os.path.exists(f"{s_path}{cmd}.py"):
        os.system( f"python3 {s_path}{cmd}.py")
    else:
        print(f"Der Befehl '{cmd}' ist entweder falsch geschrieben oder\nkann nicht gefunden werden", end="\n\n")


# Main loop
info()
while True:
    try:
        os.chdir(path)
        os.system("title Wizard-Console")
        cmd = getCommand()
        commands(cmd)
    
    except KeyboardInterrupt:
        print("\n")