import time, os, sys

#Variables
path = "."
if len(sys.argv) > 2:
    path = str(sys.argv[1])     #Path where the files are searched
debug = False                   #Debug controller
imp = "import time, os, sys"    #Imports
if len(sys.argv) > 2:
        filename = sys.argv[2]  #Filename for created file
else:
    filename = None

def search():
    py_counter = 0
    for file in os.listdir(path):
        if file.endswith(".py"):
            print(file)
            py_counter += 1
            open_file(file)
    
    print("")
    if py_counter < 1:
        print(f"No .py files found in path {path}")
    else:
        print(f"Found {py_counter} .py file(s) in path: {path}")

def open_file(file):
    if debug: print(file)
    f = open(path + "\\" + file, "r")
    content = f.read()
    if debug: print(content)
    if content.startswith("import"):
        print("Content:")
        print(content, end="\n\n")
    else:
        f = open(path + "\\" + file, "w")
        print(f"{file} is empty or has no import")
        f.write(imp)
        print(f"New content: {imp}")
        
        

def main():
    print("")
    if filename != None and filename.endswith(".py"):
        print(f"Creating file {filename}")
        f = open(path + "\\" + filename, "w")
        f.write(imp)
    else:
        search()
        if debug: print(len(sys.argv))

main()