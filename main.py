import os, time, string, random, subprocess, sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else: path = os.getcwd() + "\\"

print(path)
s_path = os.getcwd() + "\\" + "spezial" + "\\"
c_path = os.getcwd()
debug = False

os.system("cls")
os.system("color 7")

def info():
    os.system("cls")
    print("Wizard-Console [Version 1.0.1 - 30.05.2024]")
    print("(c) Leander Weiss. Alle Rechte vorbehalten", end="\n\n")

def help():
    print("help - Zeigt diese Hilfe an")

def getCommand():
    time.sleep(0.1) 
    c_path = os.getcwd()
    cmd = input(f"{c_path}!>")
    #print(cmd)
    return cmd

def commands(cmd):
    if cmd.startswith("cd") == True:
        cmd = cmd[3:]
        try:
            if debug: print(cmd)
            os.chdir(cmd)
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
        os.system(f"start cmd /k python3 {path}main.py {path} & taskkill /PID {pid} /F")
        #info()
    
    elif cmd.startswith("start"):
        os.system("start")
    
    elif cmd.startswith("code") == True:
        cmd = cmd[5:]
        os.system(f"code {cmd}")
    
    elif cmd == "exit":
        exit
    
    
    elif cmd == "info":
        info()
    
    
    elif cmd == "help":
        help()
    
    elif cmd == "" or cmd == " ":
        pass
        
    
    else:
        spezial(cmd)

def spezial(cmd):
    argvs = []
    cmds = cmd.split(" ")
    data = cmds[0]
    cmds.pop(0)
    for i in range(len(cmds)):
        argvs.append(cmds[i])
    
    argvs = "".join(argvs)
    if debug: print(f"Args: {argvs}")
        
    if os.path.exists(f"{s_path}{data}.py"):
        print(data)
        print(cmd)
        if debug:
            if len(argvs) < 0: print(argvs[0])
        #os.system( f"python3 {s_path}{data}.py {argvs}")#EOFError
        #result = subprocess.run(["python3", f"{s_path}{data}.py {argvs}"], check = True, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)#Still EOFError
        process = subprocess.Popen(["python3", f"{s_path}{data}.py {argvs}"])
        process.wait()
        if debug: print("Zest")
    else:
        if cmd != "":
            print(f"Der Befehl '{cmd}' ist entweder falsch geschrieben oder\nkann nicht gefunden werden", end="\n\n")



def joke(cmd):
    os.system(cmd)


# Main loop
info()
os.chdir(path)
while True:
    try:
        os.system("title Wizard-Console")
        cmd = getCommand()
        commands(cmd)
    
    except KeyboardInterrupt:
        print("\n")