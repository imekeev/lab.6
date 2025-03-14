import os

path = input()

if os.path.exists(path):
    filename = os.path.basename(path) //имя файля
    directory = os.path.dirname(path) //достает папку с файлом
    print(filename)
    print(directory)
else:
    print("Does not exist")
