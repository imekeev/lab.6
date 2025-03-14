import os

path = input()

if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(filename)
    print(directory)
else:
    print("Does not exist")