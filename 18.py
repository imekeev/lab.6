import os

path = input()

if os.path.exists(path):
    if os.path.isfile(path):
        if os.access(path, os.W_OK):
            os.remove(path)
        else:
            print("Can't be removed")
    else:
        print("This is not a file")
else:
    print("Path does not exist")