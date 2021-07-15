import os

try:
    os.makedirs(os.path.join(os.getcwd(), "DIR1", "Dir1", "Dir2"))
except FileExistsError:
    pass
try:
    os.makedirs(os.path.join(os.getcwd(), "DIR1", "Dir1", "Dir3", "dir4"))
except FileExistsError:
    pass

os.chdir(os.path.join(os.getcwd(), "DIR1"))
open("File.txt", 'w')
choice = input("Del??? ")
path = os.getcwd()
if choice == 'yes':
    while True:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)
            break
        for item in os.listdir():
            if item.endswith("txt"):
                os.remove(item)
                continue
            try:
                print(item)
                print(os.listdir())
                os.rmdir(item)
            except:
                os.chdir(item)
                break
        else:
            os.chdir("..")
print(os.getcwd())
